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

Avoid architecture maps, tiny labels, fake product UI, generic dark SaaS dashboards, more than one arrow unless essential, and reuse of the dense infographic layout. Default look: Studio Hero Render for tactile key art, or Cinematic Macro Still-Life for one dramatic metaphor object.

## Infographic Director

Use Infographic Director for technical infographics, dense one-pagers, codebase maps, architecture visuals, research summaries, timelines, layered stacks, taxonomies, command maps, dependency graphs, and comparisons.

The prompt must define the message spine, ranked source-backed claims, visual grammar, reading order, label hierarchy, annotation plan, callout plan, evidence guardrails, and what must be omitted. Prefer one commanding headline plus a tight ring of essential P0 labels, and reserve the dense grid for genuine matrices, taxonomies, and comparisons. Dense infographic targets should default to 6-12 exact labels unless the user explicitly accepts higher text risk. Default look: Swiss Editorial Knockout, or Blueprint Cyanotype for structural systems and codebase maps.

Avoid treating all facts as equal, tiny label soup, fake metrics, decorative charts, and generic neon cards connected by arrows as the default answer.

## Text Budget Policy

Use priority tiers for exact text:

- `P0`: labels that must appear. Keep this list small.
- `P1`: labels that are useful if space allows.
- `P2`: labels that should become icons, visual structure, paraphrases, or omitted.

Overflow labels must be merged, paraphrased, moved to P2, or omitted. Do not ask image generation to render every source detail when the target size cannot support it.

## Prompt Preflight

Every `image-prompt.md` must contain a `## Prompt Preflight` section with short answers for lane, crop/platform, viewer takeaway, grammar or archetype, generic-risk callout, P0/P1/P2 label counts, and unsupported claims to block. Do not create a separate preflight artifact.

Initial prompts include a short `## Final Generation Prompt` that can be passed to `gpt-image-2`. This final prompt must lead with the subject, then carry the chosen house look — medium, palette with hex and meaning, type character, light, material, and the one composition mechanism — as a compact craft block, with P0 text quoted and protected; compress the research brief, never the craft. Retry prompts append `## Retry Delta` after regeneration, naming what was cut, clarified, or changed.

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
- Uses a flat vector or default-software look instead of a committed house medium (offset litho, risograph, cyanotype, clay render, or cinematic chiaroscuro).
- Spreads an undirected rainbow palette instead of a restricted 2-3 hue system with the accent reserved for the focal element.
- Falls back to default-sans label soup instead of one commanding headline with a real size jump.
- Garbles, duplicates, or misspells any P0 string.

Image Quality Gate and Creative Quality Gate share one retry budget per generated image. In pack mode, retry only failing targets once. A retry must change the prompt and add `## Retry Delta` to that target's `image-prompt.md`, naming what was cut, clarified, or changed.

If the retry still fails, keep the best image for that target and report the remaining issue in the final response.

## Visual Craft System

`gpt-image-2` renders exactly one thing: the literal text of the `## Final Generation Prompt`. It never sees the research brief, the Composition Plan, or the Style section. Any art direction that does not reach that final string changes zero pixels. `gpt-image-2` also has best-in-class large-type rendering and built-in layout reasoning, so this system leans on its strengths instead of fighting them.

A style-silent prompt is not neutral. For this model the bare word `infographic` with no look attached lands on its default attractor: flat neon-on-charcoal vector cards, evenly weighted boxes, and arrows — the exact look this skill is trying to escape. You beat that attractor by committing to a strong positive look, never by listing what to avoid.

Three rules:

1. Craft survives into the Final Generation Prompt. The final prompt is the deliverable, not a summary. Compress the research brief, never the craft.
2. Every negative becomes a positive move. Replace "not dark SaaS" with "commit to one named house look and carry its core spec." Keep only a short hard-exclude line for true contaminants: invented metrics, fake UI, duplicate text, watermark.
3. Subject leads, craft modifies, text is protected. The subject noun comes first; the medium is a trailing modifier of that same sentence; the exact P0 text is quoted and capped so a long style preamble can never crowd it out.

### Commit To One House Look

After choosing the lane, pick exactly one named look from the House Aesthetic Library and adapt it to the subject. Do not invent a look from a category list, and do not blend two full recipes — borrowing a single secondary element (a title block, an accent rule) from another look is fine when it serves the subject.

Treat hex values, angles, and typeface names as adaptable defaults ("e.g." starting points), not verbatim mandates. Tune the values to the actual subject so every image varies, while keeping each look's load-bearing identity: its medium, its palette logic (one dominant, one neutral, one focal accent), its light and material, and its type character.

Default look per lane, so no image is ever generated style-free:

- `infographic` -> Swiss Editorial Knockout (dense type), or Blueprint Cyanotype (structural systems, codebase and architecture maps).
- concept explainer -> Riso Two-Tone Editorial (single bold idea), or Blueprint Cyanotype (systems).
- `social` -> Studio Hero Render (tactile key art), or Cinematic Macro Still-Life (one dramatic metaphor object).

Record the chosen look by name in `## Style, Medium, And Art Direction`, then carry a compact craft block (about 35-45 words) into the `## Final Generation Prompt`: medium and render language, the two or three named hues with their meaning, one light or material cue, and one typeface character. Long signature details (registration marks, title blocks, fold creases, hand-lettered legends) go in an optional tail clause placed after the P0 text, and are dropped first when the label count is high.

### House Aesthetic Library

Five maximally distinct anchors cover every lane. Each ships a paste-ready fragment; keep it near 40 words when carried into the final prompt, and treat the hexes and typefaces as tunable defaults.

**1. Swiss Editorial Knockout** — default for dense infographics, comparisons, taxonomies, timelines, research summaries, and single-thesis posters. International-Typographic rigor so density reads as authoritative, not cluttered.

- Palette logic: warm off-white paper ground (e.g. #FAF8F3, dominant), near-black ink (e.g. #16181D) for type and hairline rules, exactly one saturated signal accent (e.g. Signal Red #E5322B or Ultramarine #1B3CCB) on the focal data and section numbers only.
- Type: grotesque-only (Helvetica-Now / Akzidenz character), three sizes maximum, ranged-left on a strict baseline grid; giant section numerals in the accent; one enormous headline carrying most of the message.
- Medium and light: flat offset-litho on uncoated stock, matte, high-contrast, deliberately shadowless reproduction light; drama is structural (figure/ground, rule weight, white space); faint paper tooth in quiet areas; no cards, no arrows.
- Fragment: `A Swiss International-Typographic infographic as a flat offset-litho print on warm uncoated off-white stock (e.g. #FAF8F3); near-black grotesk type on a strict left-aligned baseline grid, hairline rules instead of cards, giant section numerals and one focal element in a single signal accent (e.g. Signal Red #E5322B); generous structural white space, flat shadowless print light, faint paper tooth.`

**2. Blueprint Cyanotype** — architecture visuals, codebase maps, system and dependency diagrams, layered stacks. The strongest replacement for the dark-SaaS card grid because it reads as draftsmanship, not a dashboard.

- Palette logic: deep Prussian/cyanotype blue ground (e.g. #0E2A47-#1E466E, dominant), chalk-white drafting linework (e.g. #EAF2FA), pale-cyan annotation (e.g. #7FB7E8), exactly one warm accent (e.g. oxidized-copper #E2662F) on the single most important node.
- Type: condensed engineering-stencil uppercase for labels plus true monospace for code strings and coordinates, so verbatim P0 reads as machine text; hierarchy by line weight.
- Medium and light: cyanotype contact print on cold-press cotton — paper-fiber tooth, faint chemical mottle, edge vignette; flat orthographic projection; the focal node lit a half-stop brighter; primary flow is the brightest, thickest line.
- Optional tail (drop first): corner registration marks, a lower-right drafting title block, dimension ticks, leader lines with tick terminators.
- Fragment: `A technical cyanotype blueprint contact print on cold-press cotton, deep Prussian-blue ground (e.g. #0E2A47-#1E466E) with fine chalk-white drafting linework and pale-cyan annotation; flat orthographic projection, primary flow the brightest thickest line, one oxidized-copper accent (e.g. #E2662F) on the critical node lit half a stop brighter; condensed engineering-stencil labels and monospace code strings, paper-fiber tooth and faint chemical mottle.`

**3. Riso Two-Tone Editorial** — concept explainers (especially three-step or three-path), single-metaphor big-idea frames, social teasers, blog heroes. Warm, hand-printed, unmistakably designed boldness.

- Palette logic: two true riso spot inks over warm stock (e.g. Fluorescent Pink #FF4870 + Federal Blue #2A3C8F) overprinting to muddy aubergine (e.g. #5B2E63) only where the two ideas collide or converge, on warm newsprint cream (e.g. #F4EFE1). The overprint zone is the third color and marks the conceptual meeting point.
- Type: bold condensed grotesque (Druk / Founders character) for a three-to-five-word hook set large; monospace caption for one to three supporting labels; one ink per text channel; scale contrast of at least 4x.
- Medium and light: authentic risograph — visible halftone dot screens, deliberate 1-2mm misregistration so the pink fringe glows, grainy soy-ink texture, paper showing through the fills; "light" is the cream paper glowing through semi-transparent ink; depth comes from overprint density, not z-layers.
- Optional tail (drop first): a small printed registration mark in one corner; halftone dots coarsening toward the edges.
- Fragment: `An authentic two-color risograph print on warm cream newsprint (e.g. #F4EFE1): Fluorescent Pink (e.g. #FF4870) and Federal Blue (e.g. #2A3C8F) overprinting to aubergine only where the ideas converge; visible halftone dot screens, ~1.5mm misregistration so the pink fringe glows, grainy soy-ink texture, paper through the fills; one bold condensed-grotesque hook, monospace captions, depth from overprint not arrows.`

**4. Studio Hero Render** — blog heroes, launch and social key art, single-concept explainers where one idea should read as a tactile, beautifully-lit physical object. The keynote "hero object on seamless" treatment, with real directional light.

- Palette logic: warm off-white seamless sweep (e.g. #F4F1EB, dominant), hero object in a single desaturated clay hue (e.g. cobalt #3A5CCC / shadow #28408F), one warm rim accent (e.g. amber #F2A83B, under about 8% of frame); deepest shadow is ink-blue (e.g. #1A2238), never pure black.
- Type: humanist grotesque (GT-America / Soehne character), tight all-caps hook on the seamless (never on the object), one size jump of at least 3x to the label.
- Medium and light: matte 3D clay render, soft global illumination, one large soft key from upper-left around 35 degrees with a cool lower-right fill and a single warm rim; subtle subsurface, soft contact shadow and ambient occlusion, shallow depth of field; faint film grain over the whole frame to kill plastic cleanliness.
- Fragment: `A matte 3D clay-render hero object on the left third of a warm off-white seamless sweep (e.g. #F4F1EB), lit by one large soft key from upper-left ~35 degrees with a cool fill and a single warm amber rim (e.g. #F2A83B); fine matte micro-surface, soft contact shadow and ambient occlusion, shallow depth of field, deepest shadow ink-blue not black; a tight all-caps humanist-grotesque hook in the right negative space, faint film grain.`

**5. Cinematic Macro Still-Life** — high-drama hero key art for a launch or one big idea embodied as a single physical metaphor object (a router as a railway switch, a cache as a vault). The Economist / photographic-cover register: monumental, copy-light.

- Palette logic: near-black warm void (e.g. #14110D, dominant), hero object in burnished bronze/brass (e.g. #B5853A / shadow #4A2E14), one cold cyan practical accent (e.g. #2FB6B0) marking the "active" element; highlight rolloff to warm cream (e.g. #EDE0C4).
- Type: minimal high-contrast serif (Canela / Tiempos character) or sparse engraved caps set small in the dark negative space, like a gallery placard; the light shouts, the type whispers.
- Medium and light: photoreal macro render, 100mm-lens look, f/4 slim focus; single hard key spotlight raking from camera-left, almost no fill so the shadow side falls into the void; the cold practical kicks the opposite rim; physically-based brushed-metal surface, gentle filmic halation, fine sensor grain.
- Optional tail (drop first): dust motes in a visible light shaft; anisotropic streak highlights; embossed labels etched into the metal.
- Fragment: `A photoreal cinematic macro render of a single burnished-bronze object (e.g. #B5853A) embodying the concept, emerging from a near-black warm void (e.g. #14110D), lit by one hard focused key raking from camera-left with almost no fill; a small cold cyan practical (e.g. #2FB6B0) kicks the opposite rim; brushed-metal surface, filmic halation, fine grain, warm deep blacks, sparse serif title small in the dark negative space.`

### Make Typography The Hero, Then Protect The Labels

`gpt-image-2`'s superpower is large type; its weakness is many small text blocks, each of which raises garble risk. So:

- Lead with one commanding headline (3-7 words), set verbatim, in quotation marks, in ALL CAPS or a named weight.
- The hero-headline rule is a social/hero default, not an infographic default. On dense infographic crops a giant headline fights legibility: cap the headline near 10-12% of canvas height with about a 2x jump so P0 labels stay large enough to render. The big-hero rule and the dense-label rule are mutually exclusive within one in-model render.
- Show relationships through one named mechanism — grid position, ink-channel assignment, leader lines with tick terminators, numbered reading-stations, or a physical bridge. Pick one and name it; never default to a field of identical arrows.
- Couple craft verbosity and label count in one shared budget: when the supporting-label count exceeds about five, drop the long signature-detail tail and use only the ~40-word craft block (or route to the optional hybrid lane). A maximal look and a 12-label matrix must never co-occur in one in-model render.

### gpt-image-2 Lever Policy

Express every lever as text inside the Final Generation Prompt and as the built-in generation request — never as direct OpenAI API calls or keys. Use only knobs the active built-in generation surface accepts; if it does not accept a knob, fold the intent into prompt text (the model honors the intent regardless of surface).

- quality: request `quality high` for any infographic-lane asset and any text-bearing image — the single biggest legibility lever for small, dense, or multi-font copy. `medium` is acceptable only for sparse, large-type hero work.
- size and aspect: native to the crop, edges multiples of 16, max edge 2048px (this skill's conservative reliable high-detail policy; treat larger and 4K outputs as experimental when the active surface supports them). Match the aspect so the model composes in-frame: e.g. 1024x1536 portrait poster, ~1080x1350 4:5 LinkedIn, 1536x1024 landscape hero, 1024x1024 square feed.
- Do not request `input_fidelity` (a no-op on this model; rely on explicit "Preserve:" prompt text instead). Do not request a transparent background (rejected on `gpt-image-2`; generate on a flat solid color and key out downstream if needed).
- Reference and style images, only if the built-in surface accepts them: reference each by index and role ("Image 1: subject; Image 2: style reference — apply Image 2's look to the layout") and state preserve-vs-change. A shared style reference can lock a pack's house look across targets; if references are unavailable, carry the look in prompt text.
- Bake the failure-mode guards into every prompt: lead with the subject; quote exact strings with "render verbatim, exactly once, no extra characters, no duplicate text"; add material and micro-detail cues to escape plasticky photoreal; keep on-image copy as tight as the design allows.

Generating several candidates and selecting the best is available only when the user opts in (for example in art-director mode); default and pack modes keep the one-image, one-shared-retry contract.

### Refinement: Edit The Best Frame, Don't Re-Roll

Stay inside the one shared retry budget. When the single allowed regeneration fires, prefer an edit pass only when the active built-in image surface supports image editing or image-to-image revision, so the good composition survives. If no edit capability is confirmed, reuse the same wording as a focused fresh-generation retry prompt instead of claiming an edit operation:

- `Change:` the single flaw, with the exact corrected string if it is text. `Preserve:` layout, headline glyphs, palette, lighting, material and texture, and all other labels.
- Restate the full Preserve list every iteration, and keep the change small and single — over-constrained edits drift.

### Optional Hybrid Lane

For the hardest dense-infographic case, the highest-legibility move is a hybrid: `gpt-image-2` renders the art layer in the chosen look, leaving a defined quiet zone, then the small body labels are composited as crisp vector text in that zone so they stay razor-sharp.

This lane is off by default. Before reserving any negative space, confirm that an image-text compositing tool actually exists in the active environment; saving `final.png` is not the same capability as rasterizing typeset text onto an image.

- If no compositing tool is confirmed: do not reserve negative space. Fall back to a single in-model render with `quality high`, a tight P0 cap, and the hero-typography default. This fallback is the default behavior.
- If compositing is confirmed: keep the headline and P0 hero text in-model (the model's strength), overlay only the small supporting labels, match the overlaid typeface character to the chosen look, and run the reserve-and-overlay as one atomic step so the image never ships with a blank gap.

The positive craft checks for this system are enforced inside the existing Creative Quality Gate, within the same single shared retry budget — no third gate and no second retry budget. Most are prompt-time presence checks, verifiable before generation when fixes are free: did the prompt commit to a library medium, state a palette logic with named hues and meaning, name one light or material cue, name one relationship mechanism, and request `quality high` at a native size of 2048px or less?

## Privacy And Sensitivity Gate

Treat all source-derived content as potentially sensitive. Image generation may send source-derived prompts and content through the active Codex image-generation environment. Do not use private or confidential material unless the user has made it clear that this is acceptable.

Before writing `research-brief.md`, check local and private sources for sensitive non-secret material: customer names, emails, hostnames, internal service names, ticket IDs, incident names, production commands, private repo paths, unreleased product names, and internal topology.

Skip obvious secrets automatically, including credentials, private keys, tokens, passwords, `.env` files, generated caches, and unrelated output folders. Ask before using sensitive-but-relevant material in `research-brief.md`, `image-prompt.md`, or generated images.

If sensitive content is necessary to explain the subject, ask before using it.
