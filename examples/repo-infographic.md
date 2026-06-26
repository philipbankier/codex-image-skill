# Repo Infographic Example

Invoke the skill with a public repository:

```text
Use codex-image on https://github.com/openai/openai-python
```

Expected default behavior:

1. Treat the input as a repo source.
2. Read README, docs, command references, config examples, package metadata, and key entrypoints.
3. Skip generated files, caches, unrelated outputs, and secrets.
4. Choose the `infographic` lane because the repo needs a dense technical map.
5. Write `research-brief.md`.
6. Write `image-prompt.md`.
7. Generate `final.png`.

Expected prompt shape:

```markdown
## Artifact And Lane

Best-Fit Output Lane: `infographic`
Director Decision: Infographic Director

## Required Text With Priority

- P0: Project name, main promise, and primary workflow labels.
- P1: Architecture sections, setup commands, and supported integrations.
- P2: Secondary caveats, file names, and supporting notes that can be omitted if space is tight.

## Prompt Preflight

- Source-backed claims only.
- Text budget fits the output size.
- P0 labels are legible before any P1 or P2 text is added.
- Sensitive or unsupported repo details are excluded.

## Final Generation Prompt

A source-grounded technical repo infographic of the openai-python library, what it does, how it is structured, and how a developer would use it, rendered as a cyanotype blueprint contact print on cold-press cotton paper. HOUSE LOOK: deep Prussian-blue ground (e.g. #0E2A47-#1E466E), chalk-white drafting linework (e.g. #EAF2FA), pale-cyan annotation (e.g. #7FB7E8), one oxidized-copper accent (e.g. #E2662F) on the single most important node lit a half-stop brighter; flat orthographic projection, paper-fiber tooth and faint chemical mottle, condensed engineering-stencil uppercase labels with true monospace for code strings, hierarchy by line weight. HERO TYPE: the project name set large in stencil caps as the title, render verbatim, exactly once, no extra characters, no duplicate text. SUPPORTING TEXT (P0): the section and primary-workflow labels taken exactly from the source brief, kept tight, each placed on a leader line with a tick terminator. COMPOSITION: a clear section hierarchy with visible reading order, the focal node on a dynamic-symmetry intersection, the primary install-to-call workflow drawn as the brightest thickest line, numbered station bubbles enforcing reading order, generous ruled margins. GUARDRAILS: only labels from the source brief, no invented metrics, no fake UI, no fabricated architecture, no neon-on-charcoal, no watermark. quality high, native landscape crop, max edge 2048px. On retry, use an edit pass only when the active built-in image surface supports editing or image-to-image revision; otherwise use this as a focused fresh-generation retry: Change only the single flaw, with the corrected string if text; Preserve layout, title glyphs, palette, linework, and all other labels.
```

Expected artifact shape:

```text
codex-image-output-project-20260619-153000/
  research-brief.md
  image-prompt.md
  final.png
```

Quality check:

- `research-brief.md` names the repo, source files reviewed, supported claims, and unknowns.
- `image-prompt.md` includes Prompt Preflight, P0/P1/P2 priorities, and Final Generation Prompt.
- `final.png` exists and is readable.
- The image names the repo or product clearly.
- The image explains what it does, how it is organized, and the main workflow.
- Unsupported claims, fake metrics, and invented architecture are not introduced.
