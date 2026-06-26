# Image Prompt

Use this structure for one generated image.

## Artifact And Lane

Name the artifact and the lane: `social` or `infographic`.

## Audience And Viewer Takeaway

Name the audience and the one sentence they should understand at a glance.

## Crop, Platform, And Reading Context

State the intended crop, platform, and reading distance. Examples: square social image for phone feed, 4:5 LinkedIn feed image, 16:9 open graph image, or landscape dense infographic for desktop review.

## Director Decision

State the selected director and one grammar or archetype. Explain why it fits the source in one sentence.

## Message Hierarchy

Rank the content from primary message to supporting detail.

## Composition Plan

Place the focal point on a dynamic-symmetry or thirds intersection, not dead center. Build a depth ladder: sharp foreground, soft midground, receding background. Choose one named relationship mechanism, such as grid alignment, leader lines with tick terminators, numbered reading-stations, ink channels, or a physical bridge, instead of a field of arrows. State the negative-space budget, about 30% in poster and hero lanes. Name the house look that replaces generic SaaS diagram output.

## Required Text With Priority

- P0: Exact labels that must appear.
- P1: Exact labels that may appear if space allows.
- P2: Labels to represent with icons, structure, paraphrases, or omit.

## Style, Medium, And Art Direction

Name and commit to one house look from the library in `SKILL.md`: Swiss Editorial Knockout, Blueprint Cyanotype, Riso Two-Tone Editorial, Studio Hero Render, or Cinematic Macro Still-Life. State its medium and render language, palette as named hues with hex and meaning, type character with hierarchy, light setup, and material or finish. Treat the hexes and typefaces as adaptable defaults tuned to the subject, not vague quality tokens. Carry a compact, about 40-word craft block into the Final Generation Prompt. Do not strip it.

## Negative Constraints

List up to five things to omit. Prioritize unsupported claims, fake metrics, fake UI, secrets, and composition traps.

## Prompt Preflight

- Lane:
- Crop/platform:
- Viewer takeaway:
- Grammar or archetype:
- Generic-risk callout:
- Chosen house look:
- Label budget accounting:
- Levers (quality/size):
- Unsupported claims to block:

## Final Generation Prompt

Write the prompt sent to `gpt-image-2` in this order, leading with the subject so the model prioritizes it:

1. Subject-first sentence: the subject noun, then the medium as a trailing modifier of the same sentence.
2. House-look block: the compact, about 40-word craft spec, including palette with hex and meaning, light or material, and type character.
3. Hero type: the headline set verbatim in quotation marks, with `render verbatim, exactly once, no extra characters, no duplicate text`.
4. Supporting P0 text: the exact labels, kept tight.
5. Composition: focal placement and the one named relationship mechanism.
6. Guardrails: a short hard-exclude line, such as no invented metrics, no fake UI, no watermark.
7. Technical tail: `quality high` when text is present, native crop with max edge 2048px.

On retry, use the active built-in image surface's edit or image-to-image revision only when it supports that capability. Otherwise, use the same wording as a focused fresh-generation retry prompt: `Change:` the single flaw; `Preserve:` layout, headline glyphs, palette, lighting, and all other labels.

## Retry Delta

Include this section only after a regeneration. Name what was cut, clarified, or changed from the failed prompt. If no regeneration occurred, omit this section.
