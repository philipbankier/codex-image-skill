# codex-image-skill

`codex-image-skill` is a lightweight Codex skill for turning a URL, pasted brief, local file, or local repo into a high quality technical infographic or explainer image.

The skill researches the source, writes a focused research brief, crafts a strong `gpt-image-2` prompt, generates the image through Codex built-in `gpt-image-2` image generation, and saves a small artifact folder.

This is a slim agent skill, not a Go CLI, API service, or auditable visualization bundle system. It is an unofficial community project and is not affiliated with, endorsed by, or supported by OpenAI.

## Requirements

- Codex with built-in `gpt-image-2` image generation.
- A source to explain: public URL, pasted text, local file, or local repo.
- A workspace where the agent can write output artifacts.

The skill does not manage OpenAI API keys, billing, browser login, or ChatGPT account automation.

## Local Installation

Clone and install:

```bash
git clone https://github.com/philipbankier/codex-image-skill.git
cd codex-image-skill
mkdir -p "$HOME/.agents/skills"
rm -rf "$HOME/.agents/skills/codex-image"
cp -R .agents/skills/codex-image "$HOME/.agents/skills/codex-image"
```

Canonical runtime guidance lives in `.agents/skills/codex-image/SKILL.md`, which is exactly what the local install command copies. Repo-root templates are development references and examples; installed users do not need repo-root files for correct behavior.

Then start a new Codex session so the skill list refreshes.

## Default Mode

Ask Codex to use the skill with a source:

```text
Use codex-image on https://github.com/openai/openai-python
```

Default mode is one-shot. The agent researches the source, chooses a visual strategy, writes the prompt, generates one image, and saves:

```text
codex-image-output-<source-slug>-<yyyymmdd-hhmmss>/
  research-brief.md
  image-prompt.md
  final.png
```

The agent should only pause when the input is missing, inaccessible, unsafe, or impossible to interpret.

## Art-Director Mode

Use art-director mode when you want control before generation:

```text
Use codex-image art-director on ./my-project
```

The agent asks a short set of questions about audience, density, tone, format, must-include items, and must-avoid items before generating the image.

## Pack Mode

Use pack mode when you want related images from one shared research brief:

```text
Use codex-image pack on https://github.com/openai/openai-python
```

Default pack targets:

- `dense-linkedin`: high-density technical infographic.
- `social-teaser`: lighter social image with fewer claims.
- `blog-hero`: wider hero or open graph explainer image.

Pack mode writes prompts and images under `codex-image-output-<source-slug>-<yyyymmdd-hhmmss>/pack/`.

## Prompt-Only Mode

Use prompt-only mode when you want the research brief and image prompt without generation:

```text
Use codex-image prompt-only on this pasted concept:

Edge inference routers choose between local, private-cloud, and frontier-model inference paths. The explainer should show how request sensitivity, latency, cost, and quality needs affect routing.
```

Prompt-only mode does not claim to generate an image.

## Privacy

Treat all source-derived content as potentially sensitive. The skill may send source-derived prompts and content through the active Codex image-generation environment. Do not use it on private or confidential material unless that is acceptable.

For local repos and files, the skill should avoid secrets, credentials, private keys, environment files, generated caches, and unrelated output folders. It should also ask before using sensitive non-secret material such as customer names, emails, hostnames, internal service names, ticket IDs, incident names, production commands, private repo paths, unreleased product names, and internal topology.

## Output Rights And Policy

You are responsible for having the rights to use the source material you provide, for reviewing generated images before publishing them, and for following applicable OpenAI/Codex terms and policies.

## Quality Bar

The generated image should be source-specific, readable, and useful. The agent should regenerate when an image is blank, visually broken, unreadable, missing the main subject, missing required labels, or inventing unsupported claims.

The skill chooses a lane before prompting: Social Asset Director for launch, social, hero, open graph, teaser, and shareable assets; Infographic Director for dense technical maps, codebase explainers, research summaries, timelines, stacks, comparisons, and one-pagers. Prompt artifacts must include Prompt Preflight and P0/P1/P2 text priority, and generated images must pass a Creative Quality Gate.

## Development

Run static checks with:

```bash
script/test
```

Generated image outputs and acceptance runs are ignored by git.

For bugs and security concerns, open a GitHub issue with enough detail to reproduce the problem. Do not include secrets or private source material in public issues.
