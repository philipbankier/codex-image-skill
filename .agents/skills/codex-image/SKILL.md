---
name: codex-image
description: "Generate high-quality gpt-image-2 technical infographics and explainers from URLs, pasted briefs, local files, or repos."
---

# Codex Image

Use this skill when the user asks for a technical infographic, explainer image, visual one-pager, codebase map, architecture visual, concept visual, or content pack from a URL, pasted brief, local file, or local repo.

## Canonical Runtime Contract

Canonical runtime guidance lives in this file because local installation copies `.agents/skills/codex-image` into `$HOME/.agents/skills/codex-image`. Repo-root templates are development references that mirror this contract, but installed users must not need repo-root files for correct behavior.

This skill assumes the active Codex environment has Codex built-in `gpt-image-2` image generation. If image generation is unavailable and the user did not ask for prompt-only mode, stop and say: `codex-image requires Codex built-in gpt-image-2 image generation in the active session.`

Do not call the OpenAI API directly. Do not ask for API keys. Do not automate browser login or account state.

## Modes

Default mode is one-shot. Research the source, choose a lane, write the brief, write the prompt, generate one image, inspect it, and save artifacts without asking questions unless the input is missing, inaccessible, unsafe, or impossible to interpret.

Art-director mode is selected when the user says `art-director`, `art director`, `ask me first`, or asks to choose style before generation. Ask only these questions, then proceed:

1. Audience.
2. Visual density.
3. Tone.
4. Format or platform.
5. Must-include items.
6. Must-avoid items.
7. Preferred lane, only when their answers conflict between social and infographic behavior.

Prompt-only mode is selected when the user says `prompt-only`, `prompt only`, or asks for prompts without images. Write `research-brief.md` and `image-prompt.md`, including Prompt Preflight, then stop before image generation. Do not claim an image was generated.

Pack mode is selected when the user says `pack`, `content pack`, `variants`, or asks for multiple related images. Generate these targets from one shared research brief:

- `dense-linkedin`: Infographic Director.
- `social-teaser`: Social Asset Director.
- `blog-hero`: Social Asset Director.

Pack mode is a `mixed-pack`: classify each target independently using the target map above.

## Lane Routing Rules

Choose `social` when the user asks for a social post, launch asset, hero image, open graph image, teaser, poster, campaign asset, banner, shareable visual, or platform-native asset.

Choose `infographic` when the user asks for a technical infographic, visual one-pager, codebase map, architecture visual, research summary, timeline, layered stack, matrix, comparison, taxonomy, command map, dependency graph, or dense explainer.

Choose `mixed-pack` only for pack mode or when the user explicitly asks for multiple related assets with different roles.

If the user asks for an ambiguous one-shot asset, prefer `infographic` with a reduced text budget. Ask one clarification only when the user requests mutually conflicting behavior, such as a phone-readable social post with maximum-density architecture labels.

## Input Handling

Supported inputs:

- Public URL.
- Pasted brief or raw text.
- Local file.
- Local repo or folder.

For repos and folders, prioritize README, docs, architecture notes, command references, config examples, package metadata, and key source entrypoints. Skip generated directories, caches, lockfiles unless needed, binary files, secrets, environment files, and unrelated output folders.

For URLs, gather enough source context to understand the object being explained. If the URL cannot be fetched or read, ask for pasted source material instead of guessing.

## Workflow

1. Create an output folder named `codex-image-output-<source-slug>-<yyyymmdd-hhmmss>` in the current workspace.
2. Gather source context with a bias toward meaning, structure, and visualizable relationships.
3. Write `research-brief.md`.
4. Write `image-prompt.md`, or one prompt per pack target.
5. Generate image output through Codex built-in `gpt-image-2` image generation.
6. Save the image as `final.png` for default mode or as each target's `final.png` in pack mode.
7. Inspect the generated image before final response.
8. Regenerate once when the image fails the Image Quality Gate or Creative Quality Gate.
9. Return the artifact paths and show the image when the environment supports inline image display.

Default artifact shape:

```text
codex-image-output-<source-slug>-<yyyymmdd-hhmmss>/
  research-brief.md
  image-prompt.md
  final.png
```

Pack artifact shape:

```text
codex-image-output-<source-slug>-<yyyymmdd-hhmmss>/
  research-brief.md
  pack/
    dense-linkedin/
      image-prompt.md
      final.png
    social-teaser/
      image-prompt.md
      final.png
    blog-hero/
      image-prompt.md
      final.png
```

## Research Brief

`research-brief.md` must include:

- Source Summary.
- Viewer Takeaway.
- Audience.
- Source-Backed Claims.
- Visualizable Relationships.
- Best-Fit Output Lane.
- Suggested Visual Grammar.
- Required Labels.
- Text Budget Risks.
- Sensitivity Notes.
- Risks, Caveats, Assumptions, And Unknowns.
- Source Notes.

Write the brief for image generation. Keep it concise and source-grounded.

## Prompt Rules

`image-prompt.md` must include these sections:

1. Artifact And Lane.
2. Audience And Viewer Takeaway.
3. Crop, Platform, And Reading Context.
4. Director Decision.
5. Message Hierarchy.
6. Composition Plan.
7. Required Text With Priority.
8. Style, Medium, And Art Direction.
9. Negative Constraints.
10. Prompt Preflight.
11. Final Generation Prompt.
12. Retry Delta, only after a regeneration.

## Social Asset Director

Use Social Asset Director for social posts, launch visuals, blog heroes, open graph images, teasers, posters, banners, campaign assets, and shareable visuals.

The prompt must define the crop, platform context, dominant hook, phone-readable text budget, hero composition, safe margins, mood, medium, typography, and what must not appear. Social assets should use a copy-light budget: title or hook plus 1-3 short supporting labels. Blog hero assets should use title plus optional subtitle and minimal supporting labels.

Avoid architecture maps, tiny labels, fake product UI, generic dark SaaS dashboards, more than one arrow unless essential, and reuse of the dense infographic layout.

## Infographic Director

Use Infographic Director for technical infographics, dense one-pagers, codebase maps, architecture visuals, research summaries, timelines, layered stacks, taxonomies, command maps, dependency graphs, and comparisons.

The prompt must define the message spine, ranked source-backed claims, visual grammar, reading order, label hierarchy, annotation plan, callout plan, evidence guardrails, and what must be omitted. Dense infographic targets should default to 6-12 exact labels unless the user explicitly accepts higher text risk.

Avoid treating all facts as equal, tiny label soup, fake metrics, decorative charts, and generic neon cards connected by arrows as the default answer.

## Text Budget Policy

Use priority tiers for exact text:

- `P0`: labels that must appear. Keep this list small.
- `P1`: labels that are useful if space allows.
- `P2`: labels that should become icons, visual structure, paraphrases, or omitted.

Overflow labels must be merged, paraphrased, moved to P2, or omitted. Do not ask image generation to render every source detail when the target size cannot support it.

## Prompt Preflight

Every `image-prompt.md` must contain a `## Prompt Preflight` section with short answers for lane, crop/platform, viewer takeaway, grammar or archetype, generic-risk callout, P0/P1/P2 label counts, and unsupported claims to block. Do not create a separate preflight artifact.

Initial prompts include a short `## Final Generation Prompt` that can be passed to `gpt-image-2`. This final prompt should emphasize the chosen composition and P0 text instead of repeating the full research brief. Retry prompts append `## Retry Delta` after regeneration, naming what was cut, clarified, or changed.

## Image Quality Gate

Reject and regenerate once when the image:

- Is blank or visually broken.
- Has unreadable P0 text.
- Omits the main subject.
- Invents unsupported claims or labels.
- Misses required P0 labels.
- Looks like a generic stock graphic instead of a source-specific explainer.
- Uses a layout that cannot support the requested density.

## Creative Quality Gate

Reject and regenerate once when the image:

- Does not match the selected lane.
- Does not match the requested crop or platform context.
- Has no clear focal idea within 2 seconds.
- Uses too many equally weighted boxes.
- Looks like generic dark SaaS diagram output.
- Turns a social asset into a dense diagram.
- Turns an infographic into tiny label soup.
- Reuses a sibling pack target composition without a clear reason.

Image Quality Gate and Creative Quality Gate share one retry budget per generated image. In pack mode, retry only failing targets once. A retry must change the prompt and add `## Retry Delta` to that target's `image-prompt.md`, naming what was cut, clarified, or changed.

If the retry still fails, keep the best image for that target and report the remaining issue in the final response.

## Privacy And Sensitivity Gate

Treat all source-derived content as potentially sensitive. Image generation may send source-derived prompts and content through the active Codex image-generation environment. Do not use private or confidential material unless the user has made it clear that this is acceptable.

Before writing `research-brief.md`, check local and private sources for sensitive non-secret material: customer names, emails, hostnames, internal service names, ticket IDs, incident names, production commands, private repo paths, unreleased product names, and internal topology.

Skip obvious secrets automatically, including credentials, private keys, tokens, passwords, `.env` files, generated caches, and unrelated output folders. Ask before using sensitive-but-relevant material in `research-brief.md`, `image-prompt.md`, or generated images.

If sensitive content is necessary to explain the subject, ask before using it.
