# Quality Source Fixture

This fixture gives live acceptance a dense but non-sensitive source.

## Core Claim

Codex Image Skill turns a source into a source-grounded image artifact by reading the input, writing a research brief, choosing the right director lane, writing an image prompt, and generating a final image when generation is requested.

The useful output is not just the image. The durable artifact folder lets reviewers inspect the source story, prompt choices, text priorities, generated file, and any retry notes.

## Architecture

The workflow has five parts:

1. Source intake accepts a public URL, pasted concept, local file, or local repo.
2. Source review extracts supported claims, visualizable relationships, sensitivity notes, and unknowns.
3. Director routing chooses Social Asset Director, Infographic Director, or mixed-pack behavior.
4. Prompt writing records Prompt Preflight, P0/P1/P2 labels, composition, negative constraints, and the final generation prompt.
5. Output review checks readability, source grounding, dimensions, and whether a retry changed the prompt.

Local repo inputs skip secrets, generated folders, caches, and unrelated output. Sensitive non-secret material needs approval before it appears in artifacts or images.

## Timeline

1. The user invokes `codex-image` with a source.
2. The agent gathers enough source context to avoid generic claims.
3. The agent writes `research-brief.md`.
4. The agent writes `image-prompt.md` with a director lane and text priority plan.
5. The agent generates `final.png`, unless the invocation is prompt-only.
6. The agent records inspection evidence for acceptance.

## Pack Targets

- `dense-linkedin`: Infographic Director
- `social-teaser`: Social Asset Director
- `blog-hero`: Social Asset Director

Pack mode uses one shared research brief and separate target prompts. Each target needs a distinct purpose, composition, crop/platform, text budget, and inspection note.

## Open Questions

- Which source claims are essential enough to become P0 labels?
- Which details should move to P1, P2, or be omitted for readability?
- Does the target need a dense technical map, a lighter social asset, or a wide hero image?
- Are any source details sensitive enough to require approval before use?
- Did the final image preserve the source story without adding unsupported claims?
