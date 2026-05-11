#!/usr/bin/env python3
"""Generate images through logged-in Codex CLI subscription mode.

This helper does not use OPENAI_API_KEY. It runs:
    codex exec --enable image_generation ...

When Codex image generation succeeds, images are usually saved under
~/.codex/generated_images/<session-id>/. The script copies those images into a
project output directory. If that folder is unavailable, it falls back to
extracting base64 image payloads from the matching Codex session JSONL file.
"""

from __future__ import annotations

import argparse
import base64
import binascii
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Iterable


SESSION_RE = re.compile(
    r"^rollout-\d{4}-\d{2}-\d{2}T\d{2}-\d{2}-\d{2}-(?P<session_id>.+)\.jsonl$"
)
DATA_URL_RE = re.compile(r"^data:(?P<mime>image/[-+\w.]+);base64,(?P<data>.+)$", re.DOTALL)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Generate images with a logged-in Codex CLI subscription, or extract "
            "images from an existing Codex session JSONL file."
        )
    )
    parser.add_argument(
        "--prompt",
        help="Prompt to pass to Codex image generation. Required unless --extract-session is used.",
    )
    parser.add_argument(
        "--image",
        action="append",
        default=[],
        help="Optional input/reference image path. Repeat for multiple images.",
    )
    parser.add_argument(
        "--output-dir",
        default="outputs",
        help="Directory where extracted/generated images should be copied.",
    )
    parser.add_argument("--prefix", default="codex-image", help="Output filename prefix.")
    parser.add_argument("--codex-bin", default="codex", help="Path to the codex executable.")
    parser.add_argument(
        "--cd",
        default=str(Path(__file__).resolve().parents[1]),
        help="Working directory passed to codex exec.",
    )
    parser.add_argument(
        "--sandbox",
        default="workspace-write",
        help="Sandbox mode passed to codex exec.",
    )
    parser.add_argument(
        "--extract-session",
        help="Extract images from an existing Codex session JSONL instead of running codex.",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=900,
        help="Maximum seconds to wait for codex exec.",
    )
    return parser.parse_args()


def session_id_from_path(path: Path) -> str | None:
    match = SESSION_RE.match(path.name)
    return match.group("session_id") if match else None


def codex_home() -> Path:
    return Path.home() / ".codex"


def recent_session_files(start_time: float) -> list[Path]:
    sessions_root = codex_home() / "sessions"
    if not sessions_root.exists():
        return []
    files = [
        path
        for path in sessions_root.rglob("rollout-*.jsonl")
        if path.is_file() and path.stat().st_mtime >= start_time - 2
    ]
    return sorted(files, key=lambda p: p.stat().st_mtime, reverse=True)


def detect_extension(image_bytes: bytes, fallback: str = "png") -> str:
    if image_bytes.startswith(b"\x89PNG\r\n\x1a\n"):
        return "png"
    if image_bytes.startswith(b"\xff\xd8\xff"):
        return "jpg"
    if image_bytes.startswith(b"RIFF") and image_bytes[8:12] == b"WEBP":
        return "webp"
    return fallback


def extension_from_mime(mime: str | None) -> str:
    if mime == "image/jpeg":
        return "jpg"
    if mime == "image/webp":
        return "webp"
    return "png"


def make_output_path(output_dir: Path, prefix: str, index: int, extension: str) -> Path:
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    return output_dir / f"{prefix}-{timestamp}-{index}.{extension}"


def copy_generated_images(session_files: Iterable[Path], output_dir: Path, prefix: str) -> list[Path]:
    generated_root = codex_home() / "generated_images"
    copied: list[Path] = []
    seen: set[Path] = set()
    if not generated_root.exists():
        return copied

    output_dir.mkdir(parents=True, exist_ok=True)
    for session_file in session_files:
        session_id = session_id_from_path(session_file)
        if not session_id:
            continue
        session_image_dir = generated_root / session_id
        if not session_image_dir.exists():
            continue
        for image_path in sorted(session_image_dir.iterdir()):
            if not image_path.is_file() or image_path in seen:
                continue
            seen.add(image_path)
            extension = image_path.suffix.lstrip(".") or "png"
            target = make_output_path(output_dir, prefix, len(copied) + 1, extension)
            shutil.copy2(image_path, target)
            copied.append(target)
    return copied


def iter_image_payloads(obj) -> Iterable[tuple[bytes, str]]:
    if isinstance(obj, dict):
        if obj.get("type") == "image_generation_call" and isinstance(obj.get("result"), str):
            try:
                data = base64.b64decode(obj["result"], validate=True)
                yield data, detect_extension(data)
            except (binascii.Error, ValueError):
                pass

        for value in obj.values():
            yield from iter_image_payloads(value)
    elif isinstance(obj, list):
        for value in obj:
            yield from iter_image_payloads(value)
    elif isinstance(obj, str):
        match = DATA_URL_RE.match(obj)
        if match:
            try:
                data = base64.b64decode(match.group("data"), validate=True)
                yield data, extension_from_mime(match.group("mime"))
            except (binascii.Error, ValueError):
                pass


def extract_images_from_session(session_file: Path, output_dir: Path, prefix: str) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    paths: list[Path] = []
    seen_hashes: set[str] = set()

    with session_file.open("r", encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                continue
            for image_bytes, extension in iter_image_payloads(record):
                digest = hashlib.sha256(image_bytes).hexdigest()
                if digest in seen_hashes:
                    continue
                seen_hashes.add(digest)
                path = make_output_path(output_dir, prefix, len(paths) + 1, extension)
                path.write_bytes(image_bytes)
                paths.append(path)
    return paths


def run_codex(args: argparse.Namespace) -> list[Path]:
    if not args.prompt:
        print("--prompt is required unless --extract-session is used.", file=sys.stderr)
        raise SystemExit(2)

    for raw_image in args.image:
        image_path = Path(raw_image).expanduser()
        if not image_path.exists():
            print(f"Input image not found: {image_path}", file=sys.stderr)
            raise SystemExit(2)

    start_time = time.time()
    with tempfile.NamedTemporaryFile(prefix="codex-image-last-message-", suffix=".txt") as last_message:
        command = [
            args.codex_bin,
            "exec",
            "--enable",
            "image_generation",
            "--sandbox",
            args.sandbox,
            "--cd",
            args.cd,
            "--output-last-message",
            last_message.name,
        ]
        for image in args.image:
            command.extend(["--image", str(Path(image).expanduser())])
        command.append(args.prompt)

        completed = subprocess.run(
            command,
            text=True,
            capture_output=True,
            timeout=args.timeout,
            check=False,
        )
        if completed.returncode != 0:
            if completed.stdout:
                print(completed.stdout, file=sys.stderr)
            if completed.stderr:
                print(completed.stderr, file=sys.stderr)
            print(
                "Codex image generation failed. Confirm that Codex CLI is installed, "
                "logged in, and has image_generation available.",
                file=sys.stderr,
            )
            raise SystemExit(completed.returncode)

    output_dir = Path(args.output_dir).expanduser()
    sessions = recent_session_files(start_time)
    paths = copy_generated_images(sessions, output_dir, args.prefix)
    if paths:
        return paths

    for session_file in sessions:
        paths.extend(extract_images_from_session(session_file, output_dir, args.prefix))
        if paths:
            return paths

    print(
        "Codex completed but no generated image was found. Check ~/.codex/sessions "
        "and ~/.codex/generated_images for the latest run.",
        file=sys.stderr,
    )
    raise SystemExit(1)


def main() -> int:
    args = parse_args()
    output_dir = Path(args.output_dir).expanduser()
    if args.extract_session:
        session_file = Path(args.extract_session).expanduser()
        if not session_file.exists():
            print(f"Session file not found: {session_file}", file=sys.stderr)
            return 2
        session_files = [session_file]
        paths = copy_generated_images(session_files, output_dir, args.prefix)
        if not paths:
            paths = extract_images_from_session(session_file, output_dir, args.prefix)
    else:
        paths = run_codex(args)

    if not paths:
        print("No images were extracted.", file=sys.stderr)
        return 1

    for path in paths:
        print(path.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
