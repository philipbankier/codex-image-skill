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

Describe the layout, focal point, reading order, and how the design avoids generic SaaS diagram output.

## Required Text With Priority

- P0: Exact labels that must appear.
- P1: Exact labels that may appear if space allows.
- P2: Labels to represent with icons, structure, paraphrases, or omit.

## Style, Medium, And Art Direction

Specify medium, typography, visual tone, color behavior, lighting, depth, and visual references. Do not rely on vague quality tokens by themselves.

## Negative Constraints

List up to five things to omit. Prioritize unsupported claims, fake metrics, fake UI, secrets, and composition traps.

## Prompt Preflight

- Lane:
- Crop/platform:
- Viewer takeaway:
- Grammar or archetype:
- Generic-risk callout:
- Label budget accounting:
- Unsupported claims to block:

## Final Generation Prompt

Write the concise prompt that should be sent to `gpt-image-2`. Emphasize the composition, P0 text, crop, and source guardrails.

## Retry Delta

Include this section only after a regeneration. Name what was cut, clarified, or changed from the failed prompt. If no regeneration occurred, omit this section.
