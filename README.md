# GPT Image Design Prompts

A Codex skill for compiling architecture, landscape, interior, and urban design requests into high-quality GPT Image 2 / ChatGPT Images prompts.

The default workflow is copy-paste mode: Codex generates an English prompt and Chinese intent notes, then you paste the prompt into ChatGPT with any reference images. API generation is optional and reserved for users who have an OpenAI API key.

## What This Skill Does

- Creates GPT Image 2 prompts for design visualization and image editing.
- Supports sketches, plans, site plans, photos, SketchUp/model screenshots, renderings, moodboards, material references, diagrams, and presentation-board requests.
- Produces English main prompts for better design-generation stability, with Chinese notes for review.
- Recommends image mode, size, and quality settings for future API use.
- Includes an optional API helper script that only runs when explicitly invoked.

## Typical Use

In Codex:

```text
Use $gptimage-design-prompts to create a GPT Image 2 prompt from my hand-drawn landscape plan.
```

Then upload the reference image in ChatGPT and paste the generated prompt.

## Skill Files

- `SKILL.md` - Core workflow and output contract.
- `references/prompt-patterns.md` - Design prompt pattern library.
- `references/gpt-image-2-api.md` - API-mode guidance.
- `scripts/generate_gpt_image.py` - Optional local API helper.
- `agents/openai.yaml` - Codex skill metadata.

## Install Locally

Copy this folder into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R gptimage-design-prompts ~/.codex/skills/
```

Restart Codex if the skill does not appear immediately.

## Optional API Mode

API mode is not required for normal use. To use it, set `OPENAI_API_KEY`, install the OpenAI Python package, and run the script explicitly:

```bash
export OPENAI_API_KEY="your-api-key"
python scripts/generate_gpt_image.py \
  --prompt "Create a photorealistic architectural visualization..." \
  --size 1536x1024 \
  --quality high \
  --output-dir ./outputs
```

Without `OPENAI_API_KEY`, the script exits with a clear message and does not generate files.

## License

MIT
