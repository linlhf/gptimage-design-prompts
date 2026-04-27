# GPT Image 2 API Notes

Use this reference only when the user explicitly asks to run API generation, save images locally, or prepare API parameters.

## Current Default

The user currently relies on ChatGPT Plus and may not have an API key. Do not require API access for normal prompt work.

Default behavior:

- Generate an English prompt for ChatGPT Images.
- Explain which reference images to upload and in what order.
- Provide recommended settings as guidance, not as required execution.

## When to Use API Mode

Use API mode only when the user explicitly asks for direct generation through Codex, local image output, batch generation, or reproducible parameter control.

Before running the script:

1. Confirm the task is a single generation/edit rather than an open-ended design conversation.
2. Check `OPENAI_API_KEY`.
3. Use `scripts/generate_gpt_image.py`.
4. Explain API cost and model access errors if they occur.

## API Settings

Recommended defaults:

```yaml
model: gpt-image-2
mode: generate
size: auto
quality: auto
output_format: png
```

Use:

- `1536x1024` for horizontal renderings, wide landscapes, streetscapes, and urban scenes.
- `1024x1536` for vertical boards, sections, elevations, and poster-like diagrams.
- `1024x1024` for moodboards, material boards, square diagrams, and modular image sets.
- `auto` when exact dimensions are less important than model judgment.

Use `medium` for exploration and `high` for final presentation outputs. If the user asks for speed or low cost, suggest `low` or `auto`.

## Image API vs Responses API

Use Image API for a single image generation or edit with clear inputs.

Use Responses API conceptually for multi-turn editing where the design depends on previous conversation state. The bundled script is intentionally a minimal Image API helper; do not pretend it supports full multi-turn memory.

## Known Limitations to Mention

- Precise text and dense labels may require several rounds.
- Complex A1 boards often work better when generated in stages.
- Strict plan accuracy and exact geometry are not guaranteed; use "preserve exactly" constraints and inspect results.
- API model access, organization verification, and billing are account-dependent.
- The script should fail clearly when `OPENAI_API_KEY` is missing or the SDK/model is unavailable.
