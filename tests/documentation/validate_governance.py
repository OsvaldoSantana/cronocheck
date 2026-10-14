#!/usr/bin/env python3
"""CRONO-007: check repository governance artifacts and documentation.

This checks only committed policies/templates; it does not verify GitHub account
settings, actual branch protection, vulnerability reporting, or product security.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
GITHUB = ROOT / ".github"
TEMPLATES = GITHUB / "ISSUE_TEMPLATE"
ISSUE_FORMS = ("bug_report.yml", "feature_request.yml", "engineering_task.yml")
NEEDED = [
    ROOT / "CONTRIBUTING.md",
    ROOT / "SECURITY.md",
    GITHUB / "PULL_REQUEST_TEMPLATE.md",
    GITHUB / "CODEOWNERS",
    TEMPLATES / "config.yml",
    ROOT / "docs" / "engineering" / "repository-governance.md",
    ROOT / ".github" / "workflows" / "repository-quality-gate.yml",
    ROOT / "docs" / "PROJECT_STATE.md",
]

def check(value: bool, message: str) -> None:
    if not value:
        raise AssertionError(message)

def read(path: Path) -> str:
    check(path.is_file(), "Missing file: " + str(path.relative_to(ROOT)))
    return path.read_text(encoding="utf-8")

def links_ok(path: Path, content: str) -> None:
    for link in re.findall(r"\]\(([^)]+)\)", content):
        if link.startswith(("https://", "http://", "#", "mailto:")):
            continue
        target = link.split("#", 1)[0]
        if target:
            check((path.parent / target).exists(),
                  f"{path.relative_to(ROOT)}: broken local link: {link}")

def main() -> int:
    contents = {str(path.relative_to(ROOT)): read(path) for path in NEEDED}
    for filename in ISSUE_FORMS:
        content = read(TEMPLATES / filename)
        check(re.search(r"^name: .+", content, re.M) is not None,
              f"{filename}: missing name")
        check(re.search(r"^description: .+", content, re.M) is not None,
              f"{filename}: missing description")
        check(re.search(r"^title: .+", content, re.M) is not None,
              f"{filename}: missing title")
        check(re.search(r"^body:\s*$", content, re.M) is not None,
              f"{filename}: missing issue form body")
        check("validations:" in content and "required: true" in content,
              f"{filename}: no mandatory user field")
        check("type: textarea" in content, f"{filename}: description input missing")

    config = contents[".github/ISSUE_TEMPLATE/config.yml"]
    check("blank_issues_enabled: false" in config, "public blank issues unexpectedly enabled")
    check("SECURITY.md" in config, "missing security channel instructions")

    pr = contents[".github/PULL_REQUEST_TEMPLATE.md"]
    for name in ("RF/RNF", "Evidências", "riscos", "Gate G0"):
        check(name.lower() in pr.lower(), f"PR template lacks {name}")

    owners = contents[".github/CODEOWNERS"]
    check(re.search(r"(?m)^\* @OsvaldoSantana\s*$", owners) is not None,
          "default CODEOWNER not specified")

    contrib = contents["CONTRIBUTING.md"]
    for item in ("Definition of Ready", "Definition of Done", "Conventional Commits",
                 "SECURITY.md", "Repository quality gate"):
        check(item in contrib, f"CONTRIBUTING lacks {item}")

    sec = contents["SECURITY.md"]
    check("Security" not in sec or "privad" in sec.lower(),
          "private reporting policy missing")
    for needed in ("vulnerabil", "repositório", "público", "credencia"):
        check(needed in sec.lower(), f"SECURITY.md lacks {needed}")

    policy = contents["docs/engineering/repository-governance.md"]
    for item in ("GOV-01", "GOV-02", "Rulesets", "CODEOWNERS",
                 "mantenedor único", "403", "não foi alterada", "não aprovam"):
        check(item.lower() in policy.lower(), f"governance policy lacks {item}")

    state = contents["docs/PROJECT_STATE.md"]
    check("**Gate G0:** **não aprovado**" in state, "G0 approval assumed")
    check("**Fase 01:** não iniciada" in state, "F01 started without gate")
    check("GOV-01" in state and "GOV-02" in state, "administrative questions not tracked")

    workflow = contents[".github/workflows/repository-quality-gate.yml"]
    check("pull_request:" in workflow, "CI does not run on all PRs")
    check("contents: read" in workflow, "workflow permissions should be read-only")
    check("pull_request_target:" not in workflow, "unsafe pull_request_target introduced")
    for name in ("validate_requirements.py", "validate_ux_flows.py",
                 "validate_architecture.py", "validate_fixtures.py",
                 "validate_governance.py"):
        check(name in workflow, f"missing quality check {name}")

    for path in NEEDED:
        if path.suffix == ".md":
            links_ok(path, contents[str(path.relative_to(ROOT))])
    print("PASS CRONO-007: 3 issue forms, PR template, CODEOWNERS and security policy")
    print("PASS governance rules, relative links, administrative decisions and G0 status")
    print("PASS unified read-only PR CI includes 5 documentation/fixture validators")
    print("NOTE: No GitHub ruleset, branch protection or visibility change was applied.")
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except (AssertionError, ValueError, TypeError) as exc:
        print(f"FAIL CRONO-007: {exc}", file=sys.stderr)
        sys.exit(1)
