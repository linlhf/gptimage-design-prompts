---
name: gptimage-design-prompts
description: Generate GPT Image 2 and ChatGPT Images prompts for architecture, landscape, interior, and urban design image generation or editing from sketches, plans, photos, models, moodboards, material references, diagrams, and presentation-board needs. Use this skill when the user wants professional design visualization prompts, image-editing instructions, optional API-ready settings for gpt-image-2, or direct local image generation through logged-in Codex CLI subscription mode.
metadata:
  short-description: GPT Image prompts for design visualization
---

# GPT Image Design Prompts

## Overview

Use this skill to compile design visualization requests into GPT Image 2 prompts. The default workflow is copy-paste mode: produce an English prompt for ChatGPT Images, plus a concise Chinese explanation and optional API settings.

When the user explicitly asks Codex to generate images directly and they do not have an API key, use Codex subscription mode with `scripts/generate_via_codex.py`.

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

Identify inputs and task, then **immediately load the matching template from `references/prompt-patterns.md` before writing any prompt**. Never write from general knowledge alone — always anchor the output to a template, even when the task feels familiar.

### Pre-Step — Check user input completeness

Before classifying inputs and tasks, check whether the user's request contains enough signal to pick a row from the mapping table in Step 3. The minimum required signals are:

1. **Input type** — what reference material the user is providing (sketch / plan / model / photo / moodboard / multiple images / nothing)
2. **Target output** — what they want produced (rendering / colored plan / axonometric / renovation / board / etc.)

If either signal is missing or ambiguous, **ask one short clarifying question first** instead of guessing. Examples:

- User says "帮我做个图" with no image and no target → ask: "你想要什么类型的图？是建筑渲染、平面图、轴测图，还是分析图？有没有参考图可以上传？"
- User uploads an image but says only "帮我改改" → ask: "想往哪个方向改？比如换成现代风格、加植物、改成竞赛图板、还是转成另一个视角？"
- User uploads 2+ images without explaining their roles → ask: "第一张和第二张图分别是干什么用的？比如哪张是参考材质、哪张是要修改的场景？"

Optional signals (preserve list, style direction, final use case) — fill in sensible defaults from the matched template's `Preserve list` and `Recommended keywords` if the user didn't specify. **Do not** invent the input type or target if they're unclear — those two signals are required to pick the correct template.

Only after both required signals are present, proceed to Step 1.

### Step 1 — Classify the input

What did the user provide?

- no image (text-only request)
- hand-drawn sketch
- floor plan / site plan (top-down line drawing)
- SketchUp / Rhino / white-model screenshot
- existing rendering
- site / building / street photo
- moodboard or material reference (one image)
- multiple reference images (moodboard + site, materials + plan, etc.)
- existing diagram (axonometric, analysis, etc.)
- board layout / presentation board draft

### Step 2 — Classify the task

What does the user want?

- generate a new image from scratch
- render a sketch or model
- transform view (plan → axon, plan → bird's-eye, 3D → plan, etc.)
- retexture / change materials / change facade
- photo renovation (modernize, transform, restyle)
- apply moodboard to a scene
- floor plan to interior rendering
- produce an analysis diagram (massing, circulation, zoning, timeline)
- produce a presentation board (A1, competition, portfolio)
- multi-step workflow (architecture / landscape / urban design)

### Step 3 — Look up the matching template

Use this mapping to find the right section in `references/prompt-patterns.md`. Load that section before writing the prompt.

| Input | Task | Section in prompt-patterns.md |
|-------|------|-------------------------------|
| sketch | → rendering | `# sketch-to-render` |
| SU/Rhino/white model | → rendering | `# model-to-render` |
| floor plan / site plan | → colored presentation plan | `# plan-to-colored-plan` |
| floor plan / site plan | → axonometric / isometric | `# plan-to-axonometric` |
| floor plan / site plan | → bird's-eye perspective | `# plan-to-birdseye` |
| 3D rendering / model | → plan / elevation / section | `# 3d-to-2d` |
| photo of building / street | → renovation / restyle | `# photo-renovation` |
| photo + material reference | → retexture | `# retexture` |
| moodboard + base scene | → apply moodboard to scene | `# moodboard-to-image` |
| any scene | → moodboard / material board | `# scene-to-moodboard` |
| interior floor plan | → interior rendering | `# floorplan-to-interior` |
| any input | → analysis diagram | `# analysis-diagram` |
| any input | → CAD-like technical line drawing | `# cad-linework` |
| any input | → timeline / site evolution | `# timeline-analysis` |
| any input | → presentation board (A1, competition) | `# presentation-board` |
| project brief | → architecture multi-step workflow | `# workflow-architecture` |
| project brief | → landscape multi-step workflow | `# workflow-landscape` |
| project brief | → urban design multi-step workflow | `# workflow-urban` |

If two rows could match, pick the one closer to the user's final output. If nothing matches, pick the closest row, load it, and adapt — never skip the lookup.

### Step 4 — Compile the prompt with the template's skeleton

Each template in `prompt-patterns.md` provides:
- a tested skeleton
- preserve-list defaults
- common failure modes for that scenario
- recommended keywords for lighting, materials, style

Fill in the user's specifics on top of the skeleton. Do not invent the structure from scratch.

### Step 5 — Recommend ChatGPT usage first

Mention API execution only when the user explicitly asks to generate files through API or Codex subscription mode.

## Multi-Image Role Declaration

When the user provides 2+ reference images, every prompt must start with explicit role labels for each image. This is the single biggest cause of bad output in moodboard, material-transfer, and retexture tasks — the model mixes up which image is the source of geometry and which is the source of materials.

### Required format

Open the prompt with role-tagged image references, for example:

- "Image 1 (the moodboard): use only for material palette, plant species, and texture selection. Do not copy its layout or composition."
- "Image 2 (the base site photo): preserve its geometry, camera angle, layout, and surroundings. Apply elements from Image 1 onto this scene."

### Rules

- Never write "the first image" or "the second image" alone — always include the semantic role in parentheses immediately after.
- For every image, state in one short clause what to **take from it** and what to **ignore from it**.
- If image order in ChatGPT upload matters, also tell the user the upload order in the `## ChatGPT 使用方式` section.
- Common roles to label clearly: base scene, base plan, base model, style reference, material reference, plant reference, moodboard, previous output, layout reference, color palette reference.

### Example

> Image 1 (the plant moodboard): use only as a reference for plant species, leaf textures, and color palette. Do not change the site geometry based on this image.
> Image 2 (the backyard site photo): preserve the lawn boundary, paving edges, building wall, and camera angle. Integrate the plants from Image 1 along the lawn edges and near the paving.

## Mode Rules

**Copy-paste mode is the default.** Produce a prompt that the user can paste into ChatGPT Desktop App with uploaded reference images. Describe image order when useful: "Upload the base image first, then the material reference."

**Codex subscription mode is explicit.** Use this when the user asks to generate an image directly in Codex through their logged-in subscription, Plus/Pro account, or no-API-key workflow. Read `references/codex-subscription-mode.md`, then run `scripts/generate_via_codex.py`. After generation, show saved image paths and, in Codex Desktop, render the image with an absolute Markdown image path.

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

`references/prompt-patterns.md` is the template library. The Workflow Decision step **must** load the matching H1 section from this file before writing any prompt.

Loading rule: do not read the whole file. Open it and jump directly to the H1 anchor from the Workflow Decision table (e.g. `# sketch-to-render`, `# moodboard-to-image`).

If the matching section is a placeholder (no skeleton filled in yet), use its `Preserve list` and `Recommended keywords` as scaffolding and compose the rest from the user's specifics.

## Quality Rules

- Preserve design geometry, scale, perspective, and layout when the input image is a plan, model, sketch, or photo.
- Be explicit about what must not change: original massing, camera angle, building proportions, path layout, tree positions, room relationships, or material reference.
- Use design-domain vocabulary: photorealistic architectural visualization, MIR-style rendering, clean axonometric diagram, CAD-like black linework, competition board, restrained pastel diagram, soft natural daylight.
- Avoid overloading a single prompt with rendering, analysis, labels, and board layout at once. Break complex outputs into rounds.
- Warn that precise text, dense labels, strict plan accuracy, and full presentation-board typography may need iteration.
- When the input is a plan or sketch and the task is rendering, always state explicitly that the model must preserve plan geometry, scale, and tree/element positions — these are the most commonly lost details.
- When the task involves moodboards or material transfer, state explicitly which image contributes materials and which contributes geometry, using the Multi-Image Role Declaration format.
- When the user asks for an A1 board, competition panel, or analysis diagram with labels, warn that text rendering and dense typography may need a second editing round, and suggest generating the visuals first and the labels separately.
