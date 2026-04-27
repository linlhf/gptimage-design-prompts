---
name: gptimage-design-prompts
description: Generate GPT Image 2 and ChatGPT Images prompts for architecture, landscape, interior, and urban design image generation or editing from sketches, plans, photos, models, moodboards, material references, diagrams, and presentation-board needs. Use this skill when the user wants professional design visualization prompts, image-editing instructions, or optional API-ready settings for gpt-image-2.
metadata:
  short-description: GPT Image prompts for design visualization
---

# GPT Image Design Prompts

## Overview

Use this skill to compile design visualization requests into GPT Image 2 prompts. The default workflow is copy-paste mode: produce an English prompt for ChatGPT Images, plus a concise Chinese explanation and optional API settings.

Do not recreate or quote long source prompt books. Extract the user's intent, choose the closest design workflow, and rewrite it as a model-ready prompt for GPT Image 2.

## Default Output Contract

Return this structure unless the user asks for a different format:

```markdown
## GPT Image 2 Prompt
[English prompt ready to paste into ChatGPT]

## 中文意图说明
[说明目标效果、需要保留的内容、需要修改的内容]

## ChatGPT 使用方式
[说明上传哪些参考图、复制哪段 prompt、下一轮怎么改]

## Recommended API Settings
model: gpt-image-2
mode: generate | edit
size: 1536x1024 | 1024x1536 | 1024x1024 | auto
quality: medium | high | auto
```

Default to an English main prompt. Use Chinese for explanation, user-facing notes, and exact Chinese labels that must appear in the image. If the image must include Chinese text, list the exact labels separately and tell the model to render them exactly.

## Workflow Decision

1. Identify the input type: no image, sketch, floor plan, site plan, photo, SketchUp/model screenshot, rendering, moodboard, material reference, diagram, or board layout.
2. Identify the task: generate, edit, retexture, transform view, diagram, technical drawing, moodboard, presentation board, or multi-step workflow.
3. If reference images are involved, specify their roles clearly: base image, style reference, material reference, plant list, layout reference, or previous output.
4. Compile the prompt with this skeleton:
   - task and output type
   - input-image constraints
   - elements to preserve
   - design changes to apply
   - style, material, planting, furniture, and context details
   - camera, projection, composition, and aspect ratio
   - lighting, atmosphere, rendering or diagram style
   - final use case
   - what not to change
5. Recommend ChatGPT usage first. Mention API execution only when the user explicitly asks to generate files through API.

## Mode Rules

**Copy-paste mode is the default.** Produce a prompt that the user can paste into ChatGPT Desktop App with uploaded reference images. Describe image order when useful: "Upload the base image first, then the material reference."

**API mode is explicit.** Only use API mode when the user says to directly generate an image, call the API, or save a generated image locally. Read `references/gpt-image-2-api.md` before giving API instructions or running `scripts/generate_gpt_image.py`.

**Multi-round image editing.** For iterative design changes, keep the prompt short and scoped to one change per round when preserving geometry, perspective, or design intent matters.

## Style and Size Defaults

For ChatGPT Desktop, describe composition in natural language:

- Architecture or landscape perspective: `landscape 3:2 composition`
- A1 board, poster, section, elevation: `vertical poster composition`
- Plan, axonometric diagram, material board: `square or clean board-like composition`
- Interior perspective: `landscape interior visualization composition`

For API settings, use:

- `1536x1024` for horizontal renderings, landscape scenes, urban views, and wide boards
- `1024x1536` for vertical boards, sections, elevations, posters, and tall diagrams
- `1024x1024` for moodboards, material boards, icons, and modular diagrams
- `auto` when the prompt should decide

Use `medium` for exploration and `high` for final presentation images.

## Prompt Pattern Reference

Load `references/prompt-patterns.md` when the task involves a specific design scenario or workflow. It contains compact templates for:

- sketch/model to rendering
- photo renovation
- retexture and material transfer
- plan to bird's-eye or perspective
- floor plan to interior rendering
- axonometric and isometric diagrams
- CAD-like technical linework
- moodboards and material boards
- timeline and site analysis diagrams
- architecture, landscape, and urban design workflows
- A1 presentation-board prompts

## Quality Rules

- Preserve design geometry, scale, perspective, and layout when the input image is a plan, model, sketch, or photo.
- Be explicit about what must not change: original massing, camera angle, building proportions, path layout, tree positions, room relationships, or material reference.
- Use design-domain vocabulary: photorealistic architectural visualization, MIR-style rendering, clean axonometric diagram, CAD-like black linework, competition board, restrained pastel diagram, soft natural daylight.
- Avoid overloading a single prompt with rendering, analysis, labels, and board layout at once. Break complex outputs into rounds.
- Warn that precise text, dense labels, strict plan accuracy, and full presentation-board typography may need iteration.
