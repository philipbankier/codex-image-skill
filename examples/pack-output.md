# Pack Output Example

Invoke the skill:

```text
Use codex-image pack on https://github.com/openai/openai-python
```

Expected behavior:

1. Build one shared `research-brief.md`.
2. Generate a distinct prompt for each target.
3. Generate one image per target.
4. Record target-specific inspection evidence.

Expected artifact shape:

```text
codex-image-output-project-20260619-153000/
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

Target roles:

- `dense-linkedin`: Infographic Director, default look Swiss Editorial Knockout, or Blueprint Cyanotype for structural systems.
- `social-teaser`: Social Asset Director, default look Studio Hero Render.
- `blog-hero`: Social Asset Director, default look Cinematic Macro Still-Life, or Studio Hero Render.

Each target requests `quality high` at its native crop, max edge 2048px. When the built-in generation surface accepts a reference image, a shared style reference can lock the chosen house look across all three targets so the pack feels like one family. If references are unavailable, each prompt carries the house look in text.

Target-differentiation excerpt:

```markdown
## dense-linkedin

Director Lane: infographic
Director Decision: Infographic Director

Target Role: dense technical map with the most source detail.

## social-teaser

Director Lane: social
Director Decision: Social Asset Director

Target Role: lighter platform-aware social image with one clear idea.

## blog-hero

Director Lane: social
Director Decision: Social Asset Director

Target Role: wide hero or open graph image that introduces the subject.

## Difference From Other Pack Assets

Each target differs in purpose, composition, crop/platform, and text budget.
```

This is only the target-differentiation excerpt. Each actual pack `image-prompt.md` still includes the normal Prompt Preflight and Final Generation Prompt sections.

Quality check:

- The targets are not the same prompt or crop.
- Each target has a distinct purpose, composition, and text budget.
- `dense-linkedin` carries the dense technical message spine with ranked sections and legible P0 labels.
- `social-teaser` and `blog-hero` are platform-aware social assets, not dense diagrams.
- Every generated image stays source-grounded.
