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

Create a source-grounded concept explainer that shows how an edge inference router chooses between local, private-cloud, and frontier-model inference paths. Make the routing criteria visible without adding unsupported numbers.
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
