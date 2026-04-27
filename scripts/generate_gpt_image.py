#!/usr/bin/env python3
"""Minimal GPT Image 2 helper for explicit API-mode requests."""

from __future__ import annotations

import argparse
import base64
import os
import sys
import time
from pathlib import Path


VALID_SIZES = {"auto", "1024x1024", "1536x1024", "1024x1536"}
VALID_QUALITY = {"auto", "low", "medium", "high"}
VALID_FORMATS = {"png", "jpeg", "webp"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate or edit an image with gpt-image-2. Requires OPENAI_API_KEY."
    )
    parser.add_argument("--prompt", required=True, help="Prompt text to send to gpt-image-2.")
    parser.add_argument(
        "--mode",
        choices=("generate", "edit"),
        default="generate",
        help="Use edit when passing one or more input images.",
    )
    parser.add_argument(
        "--input-image",
        action="append",
        default=[],
        help="Path to an input/reference image. Repeat for multiple images.",
    )
    parser.add_argument("--size", choices=sorted(VALID_SIZES), default="auto")
    parser.add_argument("--quality", choices=sorted(VALID_QUALITY), default="auto")
    parser.add_argument("--output-format", choices=sorted(VALID_FORMATS), default="png")
    parser.add_argument(
        "--output-dir",
        default=".",
        help="Directory where generated image files should be written.",
    )
    parser.add_argument("--model", default="gpt-image-2")
    return parser.parse_args()


def require_api_key() -> None:
    if not os.environ.get("OPENAI_API_KEY"):
        print(
            "OPENAI_API_KEY is not set. This skill defaults to copy-paste prompt mode; "
            "set OPENAI_API_KEY only when you want Codex to call the API directly.",
            file=sys.stderr,
        )
        raise SystemExit(2)


def import_client():
    try:
        from openai import OpenAI
    except Exception as exc:  # pragma: no cover - depends on local environment
        print(
            "The openai Python package is not available. Install it before API mode.",
            file=sys.stderr,
        )
        print(f"Import error: {exc}", file=sys.stderr)
        raise SystemExit(2)
    return OpenAI()


def decode_image_payload(item) -> bytes:
    if hasattr(item, "b64_json") and item.b64_json:
        return base64.b64decode(item.b64_json)
    if isinstance(item, dict) and item.get("b64_json"):
        return base64.b64decode(item["b64_json"])
    raise RuntimeError("API response did not include b64_json image data.")


def write_outputs(response, output_dir: Path, output_format: str) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    paths: list[Path] = []
    data = getattr(response, "data", None) or []
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    for index, item in enumerate(data, start=1):
        image_bytes = decode_image_payload(item)
        path = output_dir / f"gpt-image-2-{timestamp}-{index}.{output_format}"
        path.write_bytes(image_bytes)
        paths.append(path)
    return paths


def open_images(paths: list[str]):
    handles = []
    try:
        for raw_path in paths:
            path = Path(raw_path).expanduser()
            if not path.exists():
                raise FileNotFoundError(f"Input image not found: {path}")
            handles.append(path.open("rb"))
        return handles
    except Exception:
        for handle in handles:
            handle.close()
        raise


def main() -> int:
    args = parse_args()
    require_api_key()
    client = import_client()

    common = {
        "model": args.model,
        "prompt": args.prompt,
        "size": args.size,
        "quality": args.quality,
        "output_format": args.output_format,
    }

    try:
        if args.mode == "edit":
            if not args.input_image:
                print("--mode edit requires at least one --input-image.", file=sys.stderr)
                return 2
            handles = open_images(args.input_image)
            try:
                response = client.images.edit(image=handles, **common)
            finally:
                for handle in handles:
                    handle.close()
        else:
            if args.input_image:
                print(
                    "Input images were provided with --mode generate. Use --mode edit for image inputs.",
                    file=sys.stderr,
                )
                return 2
            response = client.images.generate(**common)
    except Exception as exc:
        print(f"Image API request failed: {exc}", file=sys.stderr)
        return 1

    paths = write_outputs(response, Path(args.output_dir).expanduser(), args.output_format)
    if not paths:
        print("Image API request completed but returned no images.", file=sys.stderr)
        return 1
    for path in paths:
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
