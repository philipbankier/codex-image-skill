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

Create a source-grounded technical repo infographic that explains what the project does, how it is structured, and how a developer would use it. Use clear section hierarchy, visible reading order, and exact labels from the source brief.
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
