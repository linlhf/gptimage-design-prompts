# Prompt Patterns

Use these patterns as building blocks. Replace bracketed fields with the user's project details. Keep the English prompt clear and direct.

## Core Compiler

```text
Create [output type] from the provided [input type]. Preserve [geometry/perspective/layout/proportions] exactly. Transform it into [target design result]. Apply [materials/plants/furniture/context]. Use [camera/projection/composition]. Lighting should be [lighting]. The style should be [visual style]. The final image should be suitable for [portfolio/competition board/client review/design presentation]. Do not change [protected elements].
```

## Sketch or Model to Rendering

```text
Turn the provided architectural sketch or model screenshot into a photorealistic architectural visualization. Preserve the original camera angle, massing, facade proportions, and main spatial relationships. Apply realistic facade materials including [glass/stone/wood/concrete/metal/stucco]. Add subtle landscape, street context, people, and environmental details without changing the design. Use soft natural daylight, realistic shadows, and a clean professional rendering style suitable for an architecture portfolio.
```

For MIR-like atmosphere:

```text
Use a restrained MIR-style architectural visualization: cinematic but calm composition, natural color grading, realistic material texture, soft daylight, gentle shadows, refined vegetation, and a mature atmospheric mood. Avoid exaggerated contrast or fantasy elements.
```

## Hand-Drawn Landscape Plan to Presentation Plan

```text
Convert the provided hand-drawn landscape plan into a clean professional colored landscape architecture plan. Strictly preserve the original layout, geometry, path alignment, tree locations, planting areas, water features, and spatial composition. Improve the linework and geometry, add soft green planting textures, top-view trees and shrubs, subtle paving patterns, and muted professional colors. Remove sketch noise and hand-drawn artifacts. The final plan should look polished and presentation-ready.
```

## CAD-Like Technical Linework

```text
Convert the provided plan into a clean black-and-white CAD-like technical drawing. Preserve all geometry, scale relationships, paths, boundaries, tree and shrub positions, and layout exactly. Use only black lines on a white background. Use line-weight hierarchy: thicker lines for primary boundaries and building or hardscape outlines, thinner lines for secondary details, and very fine lines for auxiliary details. Remove all labels, arrows, shadows, textures, colors, gradients, and fills.
```

## Photo Renovation

```text
Renovate the space in the original photo into [target design]. Maintain the original perspective, camera position, main massing, and site layout. Update [facade/backyard/street/interior] with [specific materials and elements]. Add [landscape/furniture/signage/lighting/people] as appropriate. Use realistic textures, soft natural daylight, and a clean contemporary design language. The final image should feel like a believable built project, not a concept collage.
```

Add detail for stronger edits:

```text
Specify paving material, plant species or plant character, furniture type, facade materials, signage style, window treatment, and lighting mood. Keep additions physically plausible and aligned with the original scale.
```

## Retexture and Reference Transfer

```text
Use Image 1 as the base scene and Image 2 as the material reference. Replace [target surface] in Image 1 with the material, texture, or graphic from Image 2. Preserve the original perspective, surface geometry, lighting direction, shadows, scale, and surrounding context. Blend the new material naturally so it appears physically attached to the surface.
```

For posters or graphics:

```text
Place the graphic from Image 1 onto [surface] in Image 2. Match the perspective, scale, lighting, surface distortion, shadows, and ambient reflections. The graphic should look printed or installed on the surface, not pasted flat on top.
```

## Plan to Bird's-Eye or Perspective

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

## Floor Plan to Interior Rendering

```text
Create a 3D interior rendering based on the provided floor plan. Use the camera angle indicated by [arrow/room/view direction]. Maintain accurate room proportions, circulation, wall positions, and spatial relationships. Design the interior in [style] with [materials/colors/furniture]. Add realistic lighting, soft textiles, plants, and lived-in details while keeping the space clean and architectural. Use a landscape interior visualization composition.
```

## Axonometric or Isometric Diagram

```text
Convert the provided plan, model, or design into a clean [axonometric/isometric] diagram. Preserve the original spatial organization and proportions. Use a white or very light background, fine consistent linework, simple volumes, muted colors, and minimal shadows. Clearly differentiate buildings, landscape, paths, water, public space, and key nodes. The result should be diagrammatic, readable, and suitable for a competition board.
```

For realistic 60-degree landscape axon:

```text
Generate a clean 60-degree isometric 3D landscape model view. Preserve the original plan geometry and layout exactly. Include buildings, trees, planting areas, paths, plaza spaces, seating, terrain, water features, and all key site elements. Use restrained realistic materials, natural lighting, ambient occlusion, and soft shadows. Keep the image clear and professional for landscape architecture presentation.
```

## Functional or Strategy Diagram

```text
Transform the provided design into a clean diagrammatic illustration. Preserve the original geometry and spatial relationships. Use flat pastel colors, thin black linework, simple icons, circular callouts, dashed arrows, and restrained labels to explain [functions/flows/sustainability strategies/program zones]. Avoid realistic textures and heavy shadows. The diagram should be clear enough for a design review or competition board.
```

## Timeline and Site Analysis

```text
Create a horizontal timeline site-analysis diagram about [site/city/street/topic]. Arrange [number] time periods from left to right along a clear central timeline. For each period, show a representative image-like vignette, concise label, and key urban or architectural change. Use a clean collage style, muted monochrome or low-saturation palette, fine lines, and professional presentation-board composition.
```

## Moodboard and Material Board

```text
Analyze the reference image and extract its main [architectural/landscape/interior] design elements. Create a clean flat-lay moodboard showing key materials, colors, textures, furniture, planting, lighting, and detail samples. Arrange elements in a balanced grid on a neutral background. Use concise labels only if needed. The board should feel curated, professional, and ready for design presentation.
```

## Moodboard to Scene

```text
Use the moodboard as the design direction for a new [interior/architecture/landscape] scene. Translate the materials, color palette, lighting mood, and design language into a coherent spatial rendering. Do not copy the moodboard layout. Create a believable finished design with realistic materials, consistent style, and soft natural lighting.
```

## Presentation Board

```text
Create a vertical A1 [architecture/landscape/urban design] presentation board for [project]. Use a clean white background, strong visual hierarchy, modern sans-serif typography, restrained linework, and a professional competition-board layout. Include a project title, concept statement area, main rendering, plan or masterplan, analysis diagrams, sections or details, callouts, and a coherent color system. Keep the board visually clear, not overcrowded.
```

For ChatGPT, prefer generating boards in stages:

1. Generate the main rendering or main diagram first.
2. Generate supporting diagrams separately.
3. Ask for a board composition using uploaded final images.
4. Expect to refine labels and text manually if precision matters.

## Architecture Workflow

1. Model or sketch to photorealistic rendering.
2. Atmosphere variant: day, night, rain, winter, warm interior glow.
3. Alternate views: bird's-eye, street view, courtyard view, interior lobby.
4. Diagrams: function zoning, exploded axonometric, section, linework.
5. Board: compose renderings, plans, diagrams, sections, and concept text.

## Landscape Workflow

1. Hand sketch to colored landscape plan.
2. Colored plan to CAD-like linework or 60-degree isometric view.
3. Isometric view to strategy diagram with callouts and arrows.
4. Sustainability set: stormwater, biodiversity, food production, microclimate, community use.
5. Final perspective from a specific garden, pavilion, pool, street, or plaza viewpoint.

## Urban Design Workflow

1. Model or plan to realistic urban rendering.
2. Model to axonometric masterplan diagram.
3. Add callout labels, program zones, pedestrian flows, public-space network, green infrastructure.
4. Create analysis diagrams with flat pastel colors and minimal texture.
5. Create vertical A1 board with diagrams above and main rendering as visual anchor.
