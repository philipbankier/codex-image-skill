# Concept Explainer Example

Normal invocation:

```text
Use codex-image on this concept:

Edge inference routers choose between local, private-cloud, and frontier-model inference paths. The explainer should show how request sensitivity, latency, cost, and quality needs affect routing.
```

Expected behavior:

1. Treat the pasted concept as the full source.
2. Identify the audience, viewer takeaway, routing paths, and decision criteria.
3. Choose a visual structure such as a decision flow or layered routing diagram.
4. Write `research-brief.md`.
5. Write `image-prompt.md`.
6. Generate `final.png`.

Expected prompt shape:

```markdown
## Prompt Preflight

- The source only supports three routing paths: local, private-cloud, and frontier-model.
- The prompt explains sensitivity, latency, cost, and quality as routing criteria.
- No benchmark numbers, vendor claims, or unsupported metrics are added.
- Required labels fit the selected crop before generation.

## Final Generation Prompt

A source-grounded concept explainer that shows how an edge inference router chooses between local, private-cloud, and frontier-model inference paths, rendered as a two-color risograph print on warm cream newsprint (e.g. #F4EFE1). HOUSE LOOK: Fluorescent Pink (e.g. #FF4870) and Federal Blue (e.g. #2A3C8F) spot inks overprinting to muddy aubergine (e.g. #5B2E63) only where the three paths converge on the routing decision; visible halftone dot screens, about 1.5mm misregistration so the pink fringe glows, grainy soy-ink texture, paper showing through the fills; one bold condensed-grotesque hook, IBM-Plex-Mono captions, one ink per text channel, depth from overprint not arrows. HERO TYPE + SUPPORTING TEXT: label the three paths "local", "private-cloud", and "frontier-model" verbatim, exactly once each, no extra characters; set the four routing criteria sensitivity, latency, cost, and quality as small monospace captions feeding the decision; add no benchmark numbers, no vendor claims, no unsupported metrics. COMPOSITION: a triptych of three ink zones for the three paths converging on a central aubergine overprint block that is the routing decision; reading order by scale, the criteria captions flowing into the convergence; generous bare-paper negative space. GUARDRAILS: only the three supported paths and four criteria, no invented numbers, no logos, no watermark. quality high, native crop, max edge 2048px. On retry, use an edit pass only when the active built-in image surface supports editing or image-to-image revision; otherwise use this as a focused fresh-generation retry: Change only the single flaw; Preserve the triptych layout, the path labels, the palette, the overprint, and all captions.
```

Prompt-only invocation:

```text
Use codex-image prompt-only on this concept:

Edge inference routers choose between local, private-cloud, and frontier-model inference paths. The explainer should show how request sensitivity, latency, cost, and quality needs affect routing.
```

Prompt-only quality check:

- `research-brief.md` exists.
- `image-prompt.md` exists.
- `final.png` does not exist.
- The response does not claim to generate an image.
- The prompt names the routing paths.
- The prompt explains the decision criteria.
- The prompt avoids claiming benchmark numbers that the source did not provide.
