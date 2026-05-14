# Overview

This file is the template library for `SKILL.md`. The skill's Workflow Decision step maps each input+task combination to one of the H1 sections below. Each section provides a tested prompt skeleton, a default preserve-list, common failure modes, and recommended keywords.

When loaded, jump directly to the matching H1 anchor — do not read the whole file linearly.

Every section follows this internal structure:

- **When to use**: one-line trigger description
- **Inputs expected**: what reference images the user should provide
- **Prompt skeleton**: fill-in-the-blank English prompt template
- **Preserve list**: what must not change from the input
- **Common failure modes**: what typically goes wrong, and how to phrase the prompt to prevent it
- **Recommended keywords**: domain vocabulary for lighting, materials, style, view
- **Output settings hint**: aspect ratio / API size recommendation

Shared core compiler:

```text
Create [output type] from the provided [input type]. Preserve [geometry/perspective/layout/proportions] exactly. Transform it into [target design result]. Apply [materials/plants/furniture/context]. Use [camera/projection/composition]. Lighting should be [lighting]. The style should be [visual style]. The final image should be suitable for [portfolio/competition board/client review/design presentation]. Do not change [protected elements].
```

# sketch-to-render

**When to use:** Turn a hand-drawn architectural or landscape sketch into a finished rendering.

**Inputs expected:** One sketch image plus project type, materials, scene context, and desired atmosphere.

**Prompt skeleton:**
```text
Turn the provided architectural sketch or model screenshot into a photorealistic architectural visualization. Preserve the original camera angle, massing, facade proportions, and main spatial relationships. Apply realistic facade materials including [glass/stone/wood/concrete/metal/stucco]. Add subtle landscape, street context, people, and environmental details without changing the design. Use soft natural daylight, realistic shadows, and a clean professional rendering style suitable for an architecture portfolio.
```

For MIR-like atmosphere:

```text
Use a restrained MIR-style architectural visualization: cinematic but calm composition, natural color grading, realistic material texture, soft daylight, gentle shadows, refined vegetation, and a mature atmospheric mood. Avoid exaggerated contrast or fantasy elements.
```

**Preserve list (defaults):**
- Original sketch geometry, massing, and proportions
- Camera angle, composition, and spatial relationships
- Tree, path, facade, and element positions when visible

**Common failure modes:**
- The model redesigns the project -> state "preserve the original design, proportions, and layout exactly."
- Sketch linework disappears into a generic building -> name the key sketch elements to preserve.

**Recommended keywords:**
- Lighting: soft natural daylight, realistic shadows, overcast diffuse light
- View: original sketch camera angle, eye-level perspective, three-quarter architectural view
- Style: photorealistic architectural visualization, MIR-style rendering, portfolio-ready
- Materials: glass, stone, wood, concrete, metal, stucco, refined vegetation

**Output settings hint:** landscape 3:2 composition / API size `1536x1024`

# model-to-render

**When to use:** Turn a SketchUp, Rhino, white-model, clay render, or massing screenshot into a realistic architectural visualization.

**Inputs expected:** One model screenshot plus material direction, context, lighting, and desired rendering style.

**Prompt skeleton:**
```text
Turn the provided architectural sketch or model screenshot into a photorealistic architectural visualization. Preserve the original camera angle, massing, facade proportions, and main spatial relationships. Apply realistic facade materials including [glass/stone/wood/concrete/metal/stucco]. Add subtle landscape, street context, people, and environmental details without changing the design. Use soft natural daylight, realistic shadows, and a clean professional rendering style suitable for an architecture portfolio.
```

For MIR-like atmosphere:

```text
Use a restrained MIR-style architectural visualization: cinematic but calm composition, natural color grading, realistic material texture, soft daylight, gentle shadows, refined vegetation, and a mature atmospheric mood. Avoid exaggerated contrast or fantasy elements.
```

**Preserve list (defaults):**
- Original camera angle, massing, facade rhythm, and proportions
- Building footprint, openings, roofline, and main volumes
- Model composition and horizon line

**Common failure modes:**
- The model becomes a different building -> require exact preservation of massing and facade proportions.
- Over-styled output loses design clarity -> request restrained architectural realism and avoid fantasy elements.

**Recommended keywords:**
- Lighting: soft daylight, realistic shadows, warm interior glow, overcast diffuse
- View: original model camera angle, street view, bird's-eye, courtyard view
- Style: photorealistic architectural visualization, MIR-style rendering, clean professional rendering
- Materials: glass curtain wall, concrete, stone, wood, metal, paving, landscape context

**Output settings hint:** landscape 3:2 composition / API size `1536x1024`

# plan-to-colored-plan

**When to use:** Convert a hand-drawn or rough site/landscape plan into a clean colored presentation plan.

**Inputs expected:** One top-down plan image; optional notes about planting, paving, water, circulation, and color style.

**Prompt skeleton:**
```text
Convert the provided hand-drawn landscape plan into a clean professional colored landscape architecture plan. Strictly preserve the original layout, geometry, path alignment, tree locations, planting areas, water features, and spatial composition. Improve the linework and geometry, add soft green planting textures, top-view trees and shrubs, subtle paving patterns, and muted professional colors. Remove sketch noise and hand-drawn artifacts. The final plan should look polished and presentation-ready.
```

**Preserve list (defaults):**
- Original top-down layout, boundaries, paths, and paving edges
- Tree, shrub, water, building, and site-element positions
- Scale relationships and plan orientation

**Common failure modes:**
- Tree or path positions drift -> explicitly say "preserve tree locations, path alignment, and planting areas exactly."
- Output becomes a perspective view -> require "top-down plan view, not a 3D rendering."

**Recommended keywords:**
- Lighting: flat plan rendering, no directional shadows, subtle ambient shading
- View: top-down plan, orthographic plan, presentation plan
- Style: colored landscape architecture plan, muted professional colors, portfolio-ready
- Materials: soft green planting textures, top-view trees, shrubs, paving patterns, water textures

**Output settings hint:** square or board-like composition / API size `1024x1024` or `1536x1024`

# plan-to-axonometric

**When to use:** Convert a plan, model, or design into a clean axonometric, isometric, or 60-degree landscape view.

**Inputs expected:** One plan/model image plus desired axonometric angle, diagrammatic vs realistic style, and important site elements.

**Prompt skeleton:**
```text
Convert the provided plan, model, or design into a clean [axonometric/isometric] diagram. Preserve the original spatial organization and proportions. Use a white or very light background, fine consistent linework, simple volumes, muted colors, and minimal shadows. Clearly differentiate buildings, landscape, paths, water, public space, and key nodes. The result should be diagrammatic, readable, and suitable for a competition board.
```

For realistic 60-degree landscape axon:

```text
Generate a clean 60-degree isometric 3D landscape model view. Preserve the original plan geometry and layout exactly. Include buildings, trees, planting areas, paths, plaza spaces, seating, terrain, water features, and all key site elements. Use restrained realistic materials, natural lighting, ambient occlusion, and soft shadows. Keep the image clear and professional for landscape architecture presentation.
```

**Preserve list (defaults):**
- Plan geometry, layout, spatial hierarchy, and proportions
- Building footprints, landscape zones, paths, water, and nodes
- Relative scale and orientation

**Common failure modes:**
- The axon invents a new layout -> require exact preservation of original plan geometry and layout.
- Too much realism hurts readability -> specify clean linework, muted colors, and minimal shadows.

**Recommended keywords:**
- Lighting: natural lighting, ambient occlusion, soft shadows
- View: 60-degree isometric, axonometric diagram, clean 3D model view
- Style: competition board, restrained realistic materials, diagrammatic, readable
- Materials: simple volumes, trees, planting areas, paths, plaza spaces, terrain, water features

**Output settings hint:** square or clean board-like composition / API size `1024x1024`

# plan-to-birdseye

**When to use:** Transform a site, landscape, or masterplan drawing into a 3D bird's-eye rendering or follow-up perspective.

**Inputs expected:** One top-down plan plus project type, desired context, materials, planting, and camera direction.

**Prompt skeleton:**
```text
Transform the provided site or landscape plan into a 3D bird's-eye architectural rendering. Preserve the plan layout, building footprints, path network, landscape zones, and spatial hierarchy. Generate realistic depth, scale, tree canopies, paving, facade materials, and surrounding urban context. Use soft daylight and a clean professional visualization style suitable for urban design presentation.
```

Follow-up prompts:

```text
Lower the camera to an eye-level perspective while preserving the same design, materials, and surrounding context. View the scene from [courtyard/street/garden/plaza] looking toward [building/landscape area].
```

```text
Create a human-eye-height perspective from [specific viewpoint]. Put [foreground element] in the foreground and [building/open space] in the background. Preserve all previous design details.
```

**Preserve list (defaults):**
- Plan layout, building footprints, path network, and landscape zones
- Spatial hierarchy, open spaces, water, planting, and key nodes
- Original design logic and scale relationships

**Common failure modes:**
- Bird's-eye view ignores the plan -> say "preserve the plan layout, footprints, paths, and zones exactly."
- Perspective follow-up loses prior design -> say "preserve all previous design details."

**Recommended keywords:**
- Lighting: soft daylight, clean daylight, realistic shadows
- View: 3D bird's-eye architectural rendering, eye-level perspective, courtyard view
- Style: urban design presentation, clean professional visualization
- Materials: tree canopies, paving, facade materials, urban context, landscape zones

**Output settings hint:** landscape 3:2 composition / API size `1536x1024`

# 3d-to-2d

**When to use:** Convert a 3D rendering, model screenshot, or massing image into a plan, elevation, section, or orthographic drawing.

**Inputs expected:** One 3D image/model screenshot plus requested drawing type, scale/detail level, and whether labels should be included.

**Prompt skeleton:**
```text
Convert the provided 3D [rendering/model screenshot] into a clean [plan/elevation/section] drawing. Preserve the original building massing, proportions, facade rhythm, openings, roofline, landscape context, and spatial relationships as much as possible. Use orthographic architectural drawing logic, crisp black linework, clear hierarchy, and a white background. Do not invent new major design elements. Keep labels minimal unless exact labels are provided.
```

**Preserve list (defaults):**
- Building massing, proportions, facade rhythm, and openings
- Main site relationships, ground plane, landscape context, and section logic

**Common failure modes:**
- The model invents unseen geometry -> say "infer only what is visible and keep uncertain areas simple."
- Perspective artifacts remain in the drawing -> require "orthographic architectural drawing logic."

**Recommended keywords:**
- Lighting: no rendering light, white background, flat technical drawing
- View: orthographic plan, front elevation, longitudinal section, cross section
- Style: CAD-like architectural drawing, crisp black linework, line-weight hierarchy
- Materials: material indications only if visible, no photorealistic textures

**Output settings hint:** vertical poster or board-like composition / API size `1024x1536` for sections/elevations, `1024x1024` for plans

# photo-renovation

**When to use:** Renovate, modernize, restyle, or transform a building, street, backyard, plaza, or interior photo.

**Inputs expected:** One base photo plus target design, protected elements, materials, furniture, planting, lighting, and intended use.

**Prompt skeleton:**
```text
Renovate the space in the original photo into [target design]. Maintain the original perspective, camera position, main massing, and site layout. Update [facade/backyard/street/interior] with [specific materials and elements]. Add [landscape/furniture/signage/lighting/people] as appropriate. Use realistic textures, soft natural daylight, and a clean contemporary design language. The final image should feel like a believable built project, not a concept collage.
```

Add detail for stronger edits:

```text
Specify paving material, plant species or plant character, furniture type, facade materials, signage style, window treatment, and lighting mood. Keep additions physically plausible and aligned with the original scale.
```

**Preserve list (defaults):**
- Original photo perspective, camera position, and horizon
- Main massing, site layout, scale, and surrounding context

**Common failure modes:**
- Photo becomes a concept collage -> request believable built project realism and physical plausibility.
- Camera changes too much -> explicitly preserve perspective and camera position.

**Recommended keywords:**
- Lighting: soft natural daylight, realistic shadows, golden hour, warm interior glow
- View: original photo perspective, street-level view, courtyard view
- Style: clean contemporary design language, believable built project, photorealistic renovation
- Materials: paving, plant species, facade materials, signage, windows, furniture, lighting

**Output settings hint:** landscape 3:2 composition / API size `1536x1024`

# retexture

**When to use:** Transfer a material, texture, facade treatment, poster, or graphic from one reference image onto a target surface in another image.

**Inputs expected:** At least two images: a base scene and a material/graphic reference. The prompt must begin with role labels.

**Prompt skeleton:**
```text
Image 1 (the base scene): preserve the original perspective, surface geometry, lighting direction, shadows, scale, and surrounding context. Image 2 (the material reference): use only as the source for [material/texture/graphic], not as a layout or composition reference. Replace [target surface] in Image 1 with the material, texture, or graphic from Image 2. Blend the new material naturally so it appears physically attached to the surface.
```

Existing retexture template:

```text
Use Image 1 as the base scene and Image 2 as the material reference. Replace [target surface] in Image 1 with the material, texture, or graphic from Image 2. Preserve the original perspective, surface geometry, lighting direction, shadows, scale, and surrounding context. Blend the new material naturally so it appears physically attached to the surface.
```

For posters or graphics:

```text
Place the graphic from Image 1 onto [surface] in Image 2. Match the perspective, scale, lighting, surface distortion, shadows, and ambient reflections. The graphic should look printed or installed on the surface, not pasted flat on top.
```

**Preserve list (defaults):**
- Base-scene perspective, geometry, lighting direction, shadows, scale, and context
- Target surface boundaries and installation logic

**Common failure modes:**
- The model copies the material image layout -> state that the material reference is not a composition reference.
- The material looks pasted on -> request perspective matching, surface distortion, shadows, and ambient reflections.

**Recommended keywords:**
- Lighting: matched lighting direction, ambient reflections, realistic shadows
- View: preserve original base-scene camera angle
- Style: photorealistic material replacement, physically attached, naturally blended
- Materials: facade cladding, paving, stone, brick, tile, fabric, poster graphic, printed surface

**Output settings hint:** match base image composition / API size `auto` or `1536x1024`

# moodboard-to-image

**When to use:** Apply a moodboard, plant palette, material palette, or style reference to a base scene without copying the moodboard layout.

**Inputs expected:** At least two images: moodboard/style reference and base scene/site/photo/plan. The prompt must begin with role labels.

**Prompt skeleton:**
```text
Image 1 (the moodboard): use only for material palette, color palette, lighting mood, plant species, textures, and design language. Do not copy its layout or composition. Image 2 (the base scene): preserve its geometry, camera angle, layout, scale, and surroundings. Apply the design direction from Image 1 onto Image 2 to create a coherent [interior/architecture/landscape] scene with realistic materials, consistent style, and soft natural lighting.
```

Existing moodboard-to-scene template:

```text
Use the moodboard as the design direction for a new [interior/architecture/landscape] scene. Translate the materials, color palette, lighting mood, and design language into a coherent spatial rendering. Do not copy the moodboard layout. Create a believable finished design with realistic materials, consistent style, and soft natural lighting.
```

**Preserve list (defaults):**
- Base-scene geometry, camera angle, layout, scale, and surroundings
- Moodboard materials, palette, texture language, lighting mood, and plant/style cues

**Common failure modes:**
- Moodboard layout replaces the site geometry -> start with explicit image role labels and say "do not copy the moodboard layout."
- Base scene becomes unrecognizable -> preserve geometry, camera angle, scale, and surroundings.

**Recommended keywords:**
- Lighting: soft natural lighting, lighting mood from moodboard, warm diffuse
- View: preserve base-scene camera angle, spatial rendering
- Style: coherent design language, believable finished design, realistic materials
- Materials: color palette, material palette, plant species, textures, furniture, facade elements

**Output settings hint:** match base image composition / API size `auto` or `1536x1024`

# scene-to-moodboard

**When to use:** Extract a design direction from a scene or reference image and turn it into a moodboard or material board.

**Inputs expected:** One or more reference images plus desired board type, project domain, and whether labels are needed.

**Prompt skeleton:**
```text
Analyze the reference image and extract its main [architectural/landscape/interior] design elements. Create a clean flat-lay moodboard showing key materials, colors, textures, furniture, planting, lighting, and detail samples. Arrange elements in a balanced grid on a neutral background. Use concise labels only if needed. The board should feel curated, professional, and ready for design presentation.
```

**Preserve list (defaults):**
- Source image's material palette, color logic, texture character, and design mood
- Relevant furniture, planting, lighting, facade, or detail cues

**Common failure modes:**
- Board includes unrelated items -> specify the domain and the exact elements to extract.
- Labels become inaccurate -> keep labels concise or generate label-free first.

**Recommended keywords:**
- Lighting: soft studio lighting, neutral background, flat-lay
- View: moodboard grid, material board, flat-lay composition
- Style: curated professional board, balanced grid, design presentation
- Materials: material samples, color swatches, planting, textures, furniture, detail samples

**Output settings hint:** square board-like composition / API size `1024x1024`

# floorplan-to-interior

**When to use:** Convert an interior floor plan into a 3D room or interior perspective rendering.

**Inputs expected:** One floor plan plus viewpoint/camera direction, room type, style, materials, furniture, and lighting.

**Prompt skeleton:**
```text
Create a 3D interior rendering based on the provided floor plan. Use the camera angle indicated by [arrow/room/view direction]. Maintain accurate room proportions, circulation, wall positions, and spatial relationships. Design the interior in [style] with [materials/colors/furniture]. Add realistic lighting, soft textiles, plants, and lived-in details while keeping the space clean and architectural. Use a landscape interior visualization composition.
```

**Preserve list (defaults):**
- Room proportions, circulation, wall positions, and openings
- Spatial relationships and camera direction

**Common failure modes:**
- Plan layout becomes generic -> require accurate room proportions and wall positions.
- Camera direction is ignored -> name the room and viewing direction explicitly.

**Recommended keywords:**
- Lighting: realistic lighting, soft textiles, warm diffuse, natural daylight
- View: landscape interior visualization, eye-level interior perspective
- Style: clean architectural interior, [minimal/cozy/luxury/contemporary]
- Materials: wall finish, floor finish, furniture, textiles, plants, lighting fixtures

**Output settings hint:** landscape interior visualization composition / API size `1536x1024`

# analysis-diagram

**When to use:** Produce a diagram explaining strategy, function, zoning, circulation, sustainability, or spatial relationships. For time-based site evolution, see `# timeline-analysis`.

**Inputs expected:** Any plan, model, rendering, site image, or project brief plus the analysis topic and label requirements.

**Prompt skeleton:**
```text
Transform the provided design into a clean diagrammatic illustration. Preserve the original geometry and spatial relationships. Use flat pastel colors, thin black linework, simple icons, circular callouts, dashed arrows, and restrained labels to explain [functions/flows/sustainability strategies/program zones]. Avoid realistic textures and heavy shadows. The diagram should be clear enough for a design review or competition board.
```

**Preserve list (defaults):**
- Base geometry, spatial relationships, building/site outlines, and circulation logic
- Key zones, flows, nodes, public spaces, and landscape systems

**Common failure modes:**
- Diagram becomes a rendering -> say "avoid realistic textures and heavy shadows."
- Labels become illegible -> suggest generating the visuals first and labels separately.

**Recommended keywords:**
- Lighting: flat diagram light, minimal shadows, white background
- View: plan diagram, axonometric analysis, strategy diagram
- Style: restrained pastel diagram, thin black linework, simple icons, dashed arrows
- Materials: flat color fills, callouts, arrows, icons, zone overlays

**Output settings hint:** square or vertical board-like composition / API size `1024x1024` or `1024x1536`

# cad-linework

**When to use:** Convert a plan, sketch, diagram, or image into clean CAD-like black-and-white technical linework.

**Inputs expected:** Any drawing/image that needs technical line extraction; optional line-weight hierarchy and label policy.

**Prompt skeleton:**
```text
Convert the provided plan into a clean black-and-white CAD-like technical drawing. Preserve all geometry, scale relationships, paths, boundaries, tree and shrub positions, and layout exactly. Use only black lines on a white background. Use line-weight hierarchy: thicker lines for primary boundaries and building or hardscape outlines, thinner lines for secondary details, and very fine lines for auxiliary details. Remove all labels, arrows, shadows, textures, colors, gradients, and fills.
```

**Preserve list (defaults):**
- Geometry, scale relationships, paths, boundaries, trees, shrubs, and layout
- Primary and secondary line hierarchy

**Common failure modes:**
- Color or shading remains -> say "only black lines on a white background."
- Geometry shifts -> require exact preservation of all geometry and scale relationships.

**Recommended keywords:**
- Lighting: no lighting, no shadows, white background
- View: top-down technical drawing, orthographic plan, elevation linework
- Style: CAD-like black linework, line-weight hierarchy, clean technical drawing
- Materials: no material textures, line-only representation

**Output settings hint:** square or board-like composition / API size `1024x1024`

# timeline-analysis

**When to use:** Create timeline, site evolution, historical phasing, or temporal analysis diagrams.

**Inputs expected:** Site/city/street/topic plus time periods, key changes, and whether labels should be exact.

**Prompt skeleton:**
```text
Create a horizontal timeline site-analysis diagram about [site/city/street/topic]. Arrange [number] time periods from left to right along a clear central timeline. For each period, show a representative image-like vignette, concise label, and key urban or architectural change. Use a clean collage style, muted monochrome or low-saturation palette, fine lines, and professional presentation-board composition.
```

**Preserve list (defaults):**
- Chronological order, period count, and key change per period
- Site topic, visual hierarchy, and timeline structure

**Common failure modes:**
- Time periods merge or reorder -> list every period explicitly.
- Typography becomes unreliable -> keep labels concise and expect a second editing round.

**Recommended keywords:**
- Lighting: clean collage light, muted monochrome, low-saturation palette
- View: horizontal timeline, representative vignette, site-analysis diagram
- Style: professional presentation-board composition, fine lines, clean collage
- Materials: maps, diagrams, vignettes, labels, arrows, timeline marks

**Output settings hint:** landscape 3:2 or wide board composition / API size `1536x1024`

# presentation-board

**When to use:** Compose an A1, competition, portfolio, or final presentation board from project visuals and diagrams.

**Inputs expected:** Project brief plus final images, plans, diagrams, sections, title, and required board content.

**Prompt skeleton:**
```text
Create a vertical A1 [architecture/landscape/urban design] presentation board for [project]. Use a clean white background, strong visual hierarchy, modern sans-serif typography, restrained linework, and a professional competition-board layout. Include a project title, concept statement area, main rendering, plan or masterplan, analysis diagrams, sections or details, callouts, and a coherent color system. Keep the board visually clear, not overcrowded.
```

For ChatGPT, prefer generating boards in stages:

1. Generate the main rendering or main diagram first.
2. Generate supporting diagrams separately.
3. Ask for a board composition using uploaded final images.
4. Expect to refine labels and text manually if precision matters.

**Preserve list (defaults):**
- Provided final visuals, diagrams, plan hierarchy, and project identity
- Board orientation, content hierarchy, and visual clarity

**Common failure modes:**
- Text is inaccurate or overcrowded -> generate visuals first and labels separately.
- Board lacks hierarchy -> specify main rendering, supporting diagrams, and title areas.

**Recommended keywords:**
- Lighting: clean white background, no dramatic lighting
- View: vertical A1 board, competition panel, portfolio board
- Style: modern sans-serif typography, restrained linework, professional competition-board layout
- Materials: main rendering, plan, masterplan, analysis diagrams, sections, callouts, color system

**Output settings hint:** vertical poster composition / API size `1024x1536`

# workflow-architecture

**When to use:** Break an architecture project brief into a multi-step image-generation workflow.

**Inputs expected:** Architecture project brief, available source images/models, desired deliverables, and presentation goal.

**Prompt skeleton:**
```text
Create a multi-step GPT Image 2 workflow for an architecture project. Start from [model/sketch/brief], generate the main architectural rendering, then create atmosphere variants, alternate views, diagrams, technical drawings, and a final board. Preserve the original design intent, massing, proportions, and project identity across all steps.
```

Existing workflow sequence:

1. Model or sketch to photorealistic rendering.
2. Atmosphere variant: day, night, rain, winter, warm interior glow.
3. Alternate views: bird's-eye, street view, courtyard view, interior lobby.
4. Diagrams: function zoning, exploded axonometric, section, linework.
5. Board: compose renderings, plans, diagrams, sections, and concept text.

**Preserve list (defaults):**
- Project concept, massing, facade proportions, material direction, and site context
- Consistent camera logic and visual identity across rounds

**Common failure modes:**
- Steps drift into unrelated designs -> restate protected elements in every round.
- Board is attempted too early -> generate main visuals and diagrams before board composition.

**Recommended keywords:**
- Lighting: day, night, rain, winter, warm interior glow
- View: bird's-eye, street view, courtyard view, lobby, section, exploded axonometric
- Style: photorealistic architectural visualization, competition board, CAD-like linework
- Materials: facade system, landscape context, interior glow, diagram overlays

**Output settings hint:** use `1536x1024` for renderings and `1024x1536` for final boards

# workflow-landscape

**When to use:** Break a landscape architecture brief into plan, axon, strategy diagram, sustainability, and perspective outputs.

**Inputs expected:** Landscape brief, plan/sketch/site image, planting and material direction, and final deliverables.

**Prompt skeleton:**
```text
Create a multi-step GPT Image 2 workflow for a landscape architecture project. Start from [hand sketch/site plan/site photo], generate a colored landscape plan, then create CAD-like linework or a 60-degree isometric view, strategy diagrams, sustainability diagrams, and final human-scale perspectives. Preserve layout, paths, tree positions, planting zones, water features, and spatial hierarchy across all steps.
```

Existing workflow sequence:

1. Hand sketch to colored landscape plan.
2. Colored plan to CAD-like linework or 60-degree isometric view.
3. Isometric view to strategy diagram with callouts and arrows.
4. Sustainability set: stormwater, biodiversity, food production, microclimate, community use.
5. Final perspective from a specific garden, pavilion, pool, street, or plaza viewpoint.

**Preserve list (defaults):**
- Layout, paths, tree positions, planting zones, water features, and spatial hierarchy
- Sustainability concept and site circulation logic

**Common failure modes:**
- Plan geometry changes between steps -> repeat the preserve list in every prompt.
- Strategy diagrams become decorative -> specify functions, flows, and sustainability strategies.

**Recommended keywords:**
- Lighting: flat plan light, natural lighting, ambient occlusion, soft shadows
- View: colored plan, CAD-like linework, 60-degree isometric, human-eye-height perspective
- Style: landscape architecture presentation, restrained pastel diagram, professional plan
- Materials: planting textures, paving, water, seating, terrain, stormwater, biodiversity

**Output settings hint:** `1024x1024` for plans/axons, `1536x1024` for perspectives, `1024x1536` for boards

# workflow-urban

**When to use:** Break an urban design project into rendering, masterplan diagram, analysis diagrams, and final board outputs.

**Inputs expected:** Urban design brief, model/plan/site context, diagram topics, public-space strategy, and board requirements.

**Prompt skeleton:**
```text
Create a multi-step GPT Image 2 workflow for an urban design project. Start from [model/plan/brief], generate a realistic urban rendering, then create an axonometric masterplan diagram, program and movement diagrams, public-space and green-infrastructure analysis, and a vertical A1 board. Preserve the masterplan structure, block layout, circulation network, public-space hierarchy, and green infrastructure across all steps.
```

Existing workflow sequence:

1. Model or plan to realistic urban rendering.
2. Model to axonometric masterplan diagram.
3. Add callout labels, program zones, pedestrian flows, public-space network, green infrastructure.
4. Create analysis diagrams with flat pastel colors and minimal texture.
5. Create vertical A1 board with diagrams above and main rendering as visual anchor.

**Preserve list (defaults):**
- Masterplan structure, block layout, circulation, public spaces, and green infrastructure
- Urban scale, site context, and hierarchy of diagrams

**Common failure modes:**
- Urban plan loses block/circulation logic -> explicitly protect block layout and movement network.
- Analysis labels become dense -> generate diagram visuals first, then refine labels separately.

**Recommended keywords:**
- Lighting: soft daylight, clean diagram light, low-saturation palette
- View: realistic urban rendering, axonometric masterplan, analysis diagram, vertical A1 board
- Style: urban design presentation, flat pastel diagram, professional competition board
- Materials: blocks, public space, pedestrian flows, program zones, green infrastructure

**Output settings hint:** `1536x1024` for urban renderings, `1024x1024` for diagrams, `1024x1536` for boards
