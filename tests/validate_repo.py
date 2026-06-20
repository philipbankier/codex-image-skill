#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FORBIDDEN_FRAGMENTS = [
    "T" + "BD",
    "TO" + "DO",
    "FIX" + "ME",
    "lorem" + " ipsum",
    "{" + "{",
    "}" + "}",
]


def read(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def require_file(relative_path: str) -> None:
    path = ROOT / relative_path
    assert path.is_file(), f"Missing required file: {relative_path}"


def require_contains(relative_path: str, expected: str) -> None:
    text = read(relative_path)
    assert expected in text, f"{relative_path} must contain: {expected}"


def require_all_contains(relative_path: str, expected_values: list[str]) -> None:
    for expected in expected_values:
        require_contains(relative_path, expected)


def require_not_contains(relative_path: str, forbidden: str) -> None:
    text = read(relative_path)
    assert forbidden not in text, f"{relative_path} must not contain: {forbidden}"


def require_any_contains(relative_path: str, expected_values: list[str]) -> None:
    text = read(relative_path)
    assert any(expected in text for expected in expected_values), (
        f"{relative_path} must contain one of: {expected_values}"
    )


def require_markdown_sections(relative_path: str, expected_sections: list[str]) -> None:
    sections = [
        line.removeprefix("## ").strip()
        for line in read(relative_path).splitlines()
        if line.startswith("## ")
    ]
    assert sections == expected_sections, (
        f"{relative_path} sections mismatch. "
        f"Expected sections: {expected_sections}. Actual sections: {sections}"
    )


def require_no_draft_markers(relative_path: str) -> None:
    text = read(relative_path)
    for fragment in FORBIDDEN_FRAGMENTS:
        assert fragment not in text, f"{relative_path} contains draft marker: {fragment}"


def test_core_repo_files() -> None:
    required_files = [
        ".gitignore",
        "AGENTS.md",
        "LICENSE",
        "README.md",
        "SECURITY.md",
        "docs/acceptance.md",
        "script/test",
        ".agents/skills/codex-image/SKILL.md",
        "templates/research-brief.md",
        "templates/image-prompt.md",
        "templates/pack-target.md",
        "examples/repo-infographic.md",
        "examples/concept-explainer.md",
        "examples/pack-output.md",
        "tests/validate_repo.py",
    ]
    for relative_path in required_files:
        require_file(relative_path)


def test_core_repo_docs_have_required_rules() -> None:
    require_contains("AGENTS.md", "Treat this directory as the standalone repo root")
    require_contains("AGENTS.md", "Do not add a Go CLI")
    require_contains("AGENTS.md", "Use `script/test` before committing")
    require_contains("LICENSE", "MIT License")
    require_contains("SECURITY.md", "Do not include secrets")


def test_readme_documents_product_contract() -> None:
    require_all_contains(
        "README.md",
        [
            "# codex-image-skill",
            "Codex built-in `gpt-image-2` image generation",
            "Default Mode",
            "Art-Director Mode",
            "Pack Mode",
            "Prompt-Only Mode",
            "Local Installation",
            "Privacy",
            "Output Rights And Policy",
            "unofficial community project",
            "not affiliated with, endorsed by, or supported by OpenAI",
            "This is a slim agent skill",
        ],
    )


def test_readme_matches_installed_runtime_contract() -> None:
    require_all_contains(
        "README.md",
        [
            "Canonical runtime guidance lives in `.agents/skills/codex-image/SKILL.md`",
            "$HOME/.agents/skills/codex-image",
            "rm -rf \"$HOME/.agents/skills/codex-image\"",
            "codex-image-output-<source-slug>-<yyyymmdd-hhmmss>/",
            "Social Asset Director",
            "Infographic Director",
            "Prompt Preflight",
            "Creative Quality Gate",
            "P0",
            "P1",
            "P2",
        ],
    )
    require_not_contains("README.md", "$HOME/.codex/skills")
    require_not_contains("README.md", "codex-image-output/\n  research-brief.md")
    require_not_contains("README.md", "codex-image-output/pack/")
    require_not_contains("README.md", "https://github.com/example/project")


def test_skill_contract() -> None:
    require_all_contains(
        ".agents/skills/codex-image/SKILL.md",
        [
            "name: codex-image",
            "Codex built-in `gpt-image-2` image generation",
            "Default mode",
            "Art-director mode",
            "Pack mode",
            "Prompt-only mode",
            "research-brief.md",
            "image-prompt.md",
            "final.png",
            "Do not call the OpenAI API directly",
            "Image Quality Gate",
        ],
    )


def test_skill_defines_installed_runtime_directors() -> None:
    require_all_contains(
        ".agents/skills/codex-image/SKILL.md",
        [
            "Canonical Runtime Contract",
            "Social Asset Director",
            "Infographic Director",
            "Lane Routing Rules",
            "social",
            "infographic",
            "mixed-pack",
            "Prompt Preflight",
            "Creative Quality Gate",
            "P0",
            "P1",
            "P2",
            "Retry Delta",
            "Sensitivity Gate",
        ],
    )
    require_all_contains(
        ".agents/skills/codex-image/SKILL.md",
        [
            "`dense-linkedin`: Infographic Director",
            "`social-teaser`: Social Asset Director",
            "`blog-hero`: Social Asset Director",
        ],
    )


def test_skill_defines_text_budget_policy_and_director_schemas() -> None:
    require_not_contains(
        ".agents/skills/codex-image/SKILL.md",
        "The prompt must end with a short `## Final Generation Prompt`",
    )
    require_all_contains(
        ".agents/skills/codex-image/SKILL.md",
        [
            "Text Budget Policy",
            "Social assets should use a copy-light budget",
            "Blog hero assets should use title plus optional subtitle",
            "Dense infographic targets should default to 6-12 exact labels",
            "Overflow labels must be merged, paraphrased, moved to P2, or omitted",
            "Director Decision",
            "Final Generation Prompt",
            "Source Summary",
            "Viewer Takeaway",
            "Audience",
            "Source-Backed Claims",
            "Visualizable Relationships",
            "Best-Fit Output Lane",
            "Suggested Visual Grammar",
            "Required Labels",
            "Text Budget Risks",
            "Sensitivity Notes",
            "Risks, Caveats, Assumptions, And Unknowns",
            "Source Notes",
            "Initial prompts include a short `## Final Generation Prompt`",
            "Retry prompts append `## Retry Delta`",
        ],
    )
    require_not_contains("templates/image-prompt.md", "Use premium modern technical infographic design")


def test_public_release_hardening() -> None:
    require_all_contains(
        ".gitignore",
        [
            ".env",
            ".env.*",
            "*.pem",
            "*.key",
            "*.p12",
            "*.pfx",
            "id_rsa",
            "id_ed25519",
        ],
    )
    require_all_contains(
        "README.md",
        [
            "https://github.com/philipbankier/codex-image-skill.git",
            "You are responsible for having the rights to use the source material",
            "following applicable OpenAI/Codex terms and policies",
            "For bugs and security concerns",
        ],
    )
    require_all_contains(
        "SECURITY.md",
        [
            "# Security",
            "Do not include secrets",
            "private source material",
        ],
    )
    for relative_path in ["README.md", "docs/acceptance.md", "examples/repo-infographic.md", "examples/pack-output.md"]:
        require_not_contains(relative_path, "https://github.com/example/project")


def test_privacy_contract_covers_sensitive_non_secret_material() -> None:
    require_file("docs/fixtures/sensitive-local-repo-layout.md")
    sensitive_terms = [
        "customer names",
        "emails",
        "hostnames",
        "internal service names",
        "ticket IDs",
        "incident names",
        "production commands",
        "private repo paths",
        "unreleased product names",
        "internal topology",
    ]
    for relative_path in [".agents/skills/codex-image/SKILL.md", "README.md", "docs/acceptance.md"]:
        require_all_contains(relative_path, sensitive_terms)
    require_contains(
        ".agents/skills/codex-image/SKILL.md",
        "Ask before using sensitive-but-relevant material in `research-brief.md`, `image-prompt.md`, or generated images.",
    )
    require_all_contains(
        "docs/fixtures/sensitive-local-repo-layout.md",
        [
            "Create the temporary local repo outside this repository, or under ignored `acceptance-runs/`, and do not commit it.",
            "The skill asks before using sensitive-but-relevant material in `research-brief.md`, `image-prompt.md`, or generated images:",
        ],
    )


def test_quality_gate_retry_and_acceptance_evidence_contract() -> None:
    require_all_contains(
        ".agents/skills/codex-image/SKILL.md",
        [
            "Image Quality Gate or Creative Quality Gate",
            "Image Quality Gate and Creative Quality Gate share one retry budget per generated image",
            "In pack mode, retry only failing targets once",
            "A retry must change the prompt",
            "Retry Delta",
            "If the retry still fails, keep the best image",
        ],
    )
    require_contains(
        "templates/image-prompt.md",
        "If no regeneration occurred, omit this section.",
    )
    require_all_contains(
        "docs/acceptance.md",
        [
            "actual output dimensions",
            "lane chosen",
            "crop/platform",
            "text budget",
            "P0/P1/P2",
            "inspection note",
            "Retry Delta",
        ],
    )


def test_templates_cover_required_structures() -> None:
    require_contains("templates/research-brief.md", "# Research Brief")
    require_markdown_sections(
        "templates/research-brief.md",
        [
            "Source Summary",
            "Viewer Takeaway",
            "Audience",
            "Source-Backed Claims",
            "Visualizable Relationships",
            "Best-Fit Output Lane",
            "Suggested Visual Grammar",
            "Required Labels",
            "Text Budget Risks",
            "Sensitivity Notes",
            "Risks, Caveats, Assumptions, And Unknowns",
            "Source Notes",
        ],
    )
    require_contains("templates/image-prompt.md", "# Image Prompt")
    require_markdown_sections(
        "templates/image-prompt.md",
        [
            "Artifact And Lane",
            "Audience And Viewer Takeaway",
            "Crop, Platform, And Reading Context",
            "Director Decision",
            "Message Hierarchy",
            "Composition Plan",
            "Required Text With Priority",
            "Style, Medium, And Art Direction",
            "Negative Constraints",
            "Prompt Preflight",
            "Final Generation Prompt",
            "Retry Delta",
        ],
    )
    require_contains("templates/pack-target.md", "# Pack Target Prompt")
    require_markdown_sections(
        "templates/pack-target.md",
        [
            "Director Lane",
            "Target Role",
            "Crop And Platform",
            "Text Budget",
            "Shared Source Story",
            "Composition Archetype",
            "Difference From Other Pack Assets",
            "Required Text With Priority",
            "Negative Constraints",
            "Target-Specific Quality Gate",
            "Output Check",
        ],
    )
    require_all_contains(
        "templates/pack-target.md",
        [
            "not a complete `image-prompt.md`",
            "feeds a normal `image-prompt.md`",
        ],
    )


def test_examples_cover_supported_modes() -> None:
    require_all_contains(
        "examples/repo-infographic.md",
        [
            "# Repo Infographic Example",
            "Use codex-image on https://github.com/openai/openai-python",
            "infographic",
            "Prompt Preflight",
            "P0",
            "P1",
            "P2",
            "codex-image-output-project-",
            "research-brief.md",
            "final.png",
        ],
    )
    require_all_contains(
        "examples/concept-explainer.md",
        [
            "# Concept Explainer Example",
            "Use codex-image on this concept:",
            "prompt-only",
            "Prompt Preflight",
            "Final Generation Prompt",
            "does not claim to generate an image.",
        ],
    )
    require_all_contains(
        "examples/pack-output.md",
        [
            "# Pack Output Example",
            "Use codex-image pack on https://github.com/openai/openai-python",
            "`dense-linkedin`: Infographic Director",
            "`social-teaser`: Social Asset Director",
            "`blog-hero`: Social Asset Director",
            "Difference From Other Pack Assets",
            "Director Lane: infographic",
            "Director Decision: Infographic Director",
            "Director Lane: social",
            "Prompt Preflight",
            "Final Generation Prompt",
            "not dense diagrams",
        ],
    )


def test_acceptance_guide_covers_live_checks() -> None:
    require_all_contains(
        "docs/acceptance.md",
        [
            "# Acceptance Checks",
            "Public Repo URL",
            "Pasted Concept Brief",
            "Local Folder Or Repo",
            "Pack Mode",
            "Art-Director Mode",
            "final.png",
            "No secrets",
            "docs/fixtures/quality-source.md",
            "One shared `research-brief.md` exists.",
            "`pack/dense-linkedin/image-prompt.md` and `final.png` exist.",
            "`pack/social-teaser/image-prompt.md` and `final.png` exist.",
            "`pack/blog-hero/image-prompt.md` and `final.png` exist.",
            "`dense-linkedin` uses Infographic Director.",
            "`social-teaser` and `blog-hero` use Social Asset Director.",
            "each target records lane chosen, crop/platform, text budget, P0/P1/P2 label counts, actual output dimensions, and inspection note.",
            "social targets are platform-aware and not dense diagrams.",
            "dense target has message spine, ranked sections, reading order, visual hierarchy, and legible P0 labels.",
        ],
    )


def test_acceptance_fixtures_exist() -> None:
    require_file("docs/fixtures/quality-source.md")
    require_file("docs/fixtures/sensitive-local-repo-layout.md")
    require_all_contains(
        "docs/fixtures/quality-source.md",
        [
            "# Quality Source Fixture",
            "Core Claim",
            "Timeline",
            "Architecture",
            "Open Questions",
        ],
    )


def test_no_draft_markers_in_checked_files() -> None:
    for relative_path in [
        ".gitignore",
        "AGENTS.md",
        "LICENSE",
        "README.md",
        "docs/acceptance.md",
        "script/test",
        ".agents/skills/codex-image/SKILL.md",
        "templates/research-brief.md",
        "templates/image-prompt.md",
        "templates/pack-target.md",
        "examples/repo-infographic.md",
        "examples/concept-explainer.md",
        "examples/pack-output.md",
        "docs/fixtures/quality-source.md",
        "tests/validate_repo.py",
    ]:
        require_no_draft_markers(relative_path)


def main() -> None:
    tests = [
        test_core_repo_files,
        test_core_repo_docs_have_required_rules,
        test_readme_documents_product_contract,
        test_readme_matches_installed_runtime_contract,
        test_skill_contract,
        test_skill_defines_installed_runtime_directors,
        test_skill_defines_text_budget_policy_and_director_schemas,
        test_public_release_hardening,
        test_privacy_contract_covers_sensitive_non_secret_material,
        test_quality_gate_retry_and_acceptance_evidence_contract,
        test_templates_cover_required_structures,
        test_examples_cover_supported_modes,
        test_acceptance_guide_covers_live_checks,
        test_acceptance_fixtures_exist,
        test_no_draft_markers_in_checked_files,
    ]
    for test in tests:
        test()
    print(f"{len(tests)} static checks passed")


if __name__ == "__main__":
    main()
