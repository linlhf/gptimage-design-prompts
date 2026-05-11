# Codex Subscription Mode

Use this reference when the user explicitly wants Codex to generate images directly without an OpenAI API key.

## What It Does

This mode runs the local Codex CLI with image generation enabled:

```bash
python scripts/generate_via_codex.py \
  --prompt "Create a photorealistic architectural visualization..." \
  --output-dir ./outputs
```

It requires a logged-in Codex CLI session with image generation available. It does not read `OPENAI_API_KEY`.

## When To Use

Use this mode only when the user asks for direct generation in Codex, subscription-based generation, Plus/Pro logged-in generation, or "no API key" local image output.

Keep copy-paste mode as the default when the user only needs a prompt for ChatGPT.

## Input Images

Pass reference images with repeated `--image` flags:

```bash
python scripts/generate_via_codex.py \
  --image ./base-scene.png \
  --image ./material-reference.png \
  --prompt "Use the first image as the base scene and the second image only as the material reference..."
```

In the prompt, define image roles clearly: base scene, material reference, style reference, plan, model screenshot, or previous output.

## Output Behavior

Generated files are copied into `outputs/` by default. The script first looks for images saved by Codex under:

```text
~/.codex/generated_images/<session-id>/
```

If that folder is unavailable, it extracts image payloads from the matching session JSONL under:

```text
~/.codex/sessions/
```

When replying to the user in Codex Desktop, display the generated local image with an absolute Markdown image path:

```markdown
![Generated image](/absolute/path/to/output.png)
```

## Limitations

- This depends on local Codex CLI features and the user's logged-in subscription state.
- It is not the same as the Images API and does not expose all API parameters.
- WebSocket warnings followed by HTTP fallback can appear and are usually non-fatal if the command completes.
- If no image appears, ask the user to confirm the CLI is logged in and image generation is enabled.
