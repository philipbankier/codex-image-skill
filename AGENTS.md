# Agent Notes

- Treat this directory as the standalone repo root for `codex-image-skill`.
- The product is the Codex skill at `.agents/skills/codex-image/SKILL.md`.
- Do not add a Go CLI, Node app, API server, or browser automation layer.
- Keep v1 runtime behavior inside the skill instructions and markdown templates.
- Use `script/test` before committing.
- Do not commit generated image outputs, acceptance run folders, local caches, or secrets.
- Update this file when project-specific scripts, release steps, or safety defaults change.
