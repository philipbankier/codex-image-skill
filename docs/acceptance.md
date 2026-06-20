# Acceptance Checks

Run these checks in a Codex session that has built-in `gpt-image-2` image generation.

Generated output folders such as `codex-image-output-*` and `acceptance-runs/` are not committed.

## Static Checks

```bash
script/test
```

Expected:

```text
15 static checks passed
```

## Install Smoke

Run the README install command against a temporary home directory:

```bash
set -e
tmp_home="$(mktemp -d)"
trap 'rm -rf "$tmp_home"' EXIT
mkdir -p "$tmp_home/.agents/skills"
cp -R .agents/skills/codex-image "$tmp_home/.agents/skills/codex-image"
grep -q "Social Asset Director" "$tmp_home/.agents/skills/codex-image/SKILL.md"
grep -q "Infographic Director" "$tmp_home/.agents/skills/codex-image/SKILL.md"
grep -q "Prompt Preflight" "$tmp_home/.agents/skills/codex-image/SKILL.md"
```

Expected: all `grep` commands exit 0.

## Acceptance Evidence

For each generated target, record:

- lane chosen
- crop/platform
- actual output dimensions
- text budget
- P0/P1/P2 label counts
- inspection note
- Retry Delta, only when a regeneration occurred

Use `file <path-to-final.png>` or another local image metadata tool to capture dimensions.

## Public Repo URL

Invoke:

```text
Use codex-image on https://github.com/openai/openai-python
```

Pass criteria:

- `research-brief.md` captures the repo's real story.
- `image-prompt.md` is specific and source-grounded.
- `final.png` exists.
- The image is readable.
- Required labels are present.
- Unsupported claims are not introduced.

## Pasted Concept Brief

Invoke:

```text
Use codex-image on this concept:

Edge inference routers choose between local, private-cloud, and frontier-model inference paths. The explainer should show how request sensitivity, latency, cost, and quality needs affect routing.
```

Pass criteria:

- The research brief treats the pasted text as the source.
- The prompt explains the concept without inventing metrics.
- `final.png` exists and is readable.

## Local Folder Or Repo

Invoke:

```text
Use codex-image on ./sample-project
```

Pass criteria:

- The agent prioritizes README, docs, package metadata, config examples, and key source entrypoints.
- Generated folders, caches, lockfiles unless needed, and secrets are skipped.
- No secrets appear in `research-brief.md`, `image-prompt.md`, or `final.png`.

## Pack Mode

Invoke:

```text
Use codex-image pack on https://github.com/openai/openai-python
```

For repeatable live acceptance, use the fixture source:

```text
Use codex-image pack on docs/fixtures/quality-source.md
```

Pass criteria:

- One shared `research-brief.md` exists.
- `pack/dense-linkedin/image-prompt.md` and `final.png` exist.
- `pack/social-teaser/image-prompt.md` and `final.png` exist.
- `pack/blog-hero/image-prompt.md` and `final.png` exist.
- `dense-linkedin` uses Infographic Director.
- `social-teaser` and `blog-hero` use Social Asset Director.
- each target records lane chosen, crop/platform, text budget, P0/P1/P2 label counts, actual output dimensions, and inspection note.
- social targets are platform-aware and not dense diagrams.
- dense target has message spine, ranked sections, reading order, visual hierarchy, and legible P0 labels.

## Art-Director Mode

Invoke:

```text
Use codex-image art-director on https://github.com/openai/openai-python
```

Pass criteria:

- The agent asks for audience, density, tone, format, must-include items, and must-avoid items.
- The final prompt incorporates the user's answers.
- `final.png` exists and reflects the chosen direction.

## Sensitivity Gate

Use `docs/fixtures/sensitive-local-repo-layout.md` to build a temporary local repo.

Pass criteria:

- Secrets, `.env` files, generated caches, and unrelated output folders are skipped.
- The agent asks before using sensitive non-secret material: customer names, emails, hostnames, internal service names, ticket IDs, incident names, production commands, private repo paths, unreleased product names, and internal topology.
- `research-brief.md`, `image-prompt.md`, and `final.png` do not include skipped secrets.
- If sensitive material is needed to explain the source, the agent pauses and asks before using it.

## Failure Cases

Pass criteria:

- If Codex image generation is unavailable, the skill fails clearly.
- If a URL cannot be fetched, the skill asks for pasted source material.
- If the source is unsafe or contains necessary sensitive material, the skill asks before using it.
- Prompt-only mode writes prompt artifacts and does not claim an image was generated.
