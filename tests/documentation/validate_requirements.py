#!/usr/bin/env python3
"""CRONO-004: structural consistency checks for proposed requirements and traceability.

This validates DOCUMENTATION ONLY. It does not implement or validate product features.
Uses Python standard library; safe for public GitHub Actions.
"""
from __future__ import annotations

import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
PRODUCT = ROOT / "docs" / "product"
REGISTRY = PRODUCT / "requirements-register.json"
MATRIX = PRODUCT / "traceability-matrix.md"
PRIORITY = PRODUCT / "requirements-prioritization.md"
PRD = PRODUCT / "prd.md"
BLUEPRINT = ROOT / "docs" / "CRONOCHECK_BLUEPRINT_V1.md"
GLOSSARY = PRODUCT / "domain-invariants.md"
OPEN = PRODUCT / "open-questions.md"
TEST_FIXTURES = ROOT / "tests" / "fixtures"
REQUIRED = [f"RF-{n:02d}" for n in range(1, 12)] + [f"RNF-{n:02d}" for n in range(1, 11)]
PROVISIONAL = {"RNF-03", "RNF-04", "RNF-08"}


def check(condition: bool, reason: str) -> None:
    if not condition:
        raise AssertionError(reason)


def text(path: Path) -> str:
    check(path.is_file(), f"missing document: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def validate() -> int:
    data = json.loads(text(REGISTRY))
    check(data["schema_version"] == "0.1.0", "registry schema version changed")
    check(data["state"] == "PROPOSAL_PENDING_HUMAN_ACCEPTANCE", "approval was presumed")
    reqs = data["requirements"]
    ids = [r["id"] for r in reqs]
    check(len(ids) == 21 and set(ids) == set(REQUIRED), "expected exactly RF-01..11 and RNF-01..10")
    check(len(set(ids)) == len(ids), "duplicate requirement IDs")

    matrix = text(MATRIX)
    priority = text(PRIORITY)
    prd = text(PRD)
    blueprint = text(BLUEPRINT)
    domain = text(GLOSSARY)
    decisions = text(OPEN)

    check("**Gate G0:** **não aprovado**" in text(ROOT / "docs" / "PROJECT_STATE.md"), "Gate G0 approval mismatch")
    check("aguardando validação técnica" in prd, "PRD approval status unexpectedly changed")
    check("CRONO-004" in blueprint, "CRONO-004 missing from blueprint")
    check("OQ-04/OQ-05 pendentes" in decisions, "open decisions summary changed")
    check(len(re.findall(r"\| OQ-0[12] \|[^\n]*Aprovado", decisions)) == 2,
          "prior approvals OQ-01 and OQ-02 must remain recorded")
    check(len(re.findall(r"^\| (?:RF-\d{2}|RNF-\d{2}) \|", matrix, re.M)) == 21,
          "matrix must have exactly 21 data rows")
    check("Must" in priority and "OQ-06" in priority, "prioritization notes missing")

    all_dependencies: dict[str, list[str]] = {}
    for item in reqs:
        rid = item["id"]
        prefix = "RF-" if rid.startswith("RF-") else "RNF-"
        check(item["type"] == ("functional" if prefix == "RF-" else "non_functional"),
              f"{rid}: invalid type")
        check(item["moscow_proposal"] == "Must" and item["mvp_release_required"] is True,
              f"{rid}: MvP was silently de-scoped")
        check(item["application_status"] == "not_implemented"
              and item["validation_status"] == "not_validated",
              f"{rid}: unverified completion")
        check(item["numeric_target_status"] == (
            "provisional_calibration_required" if rid in PROVISIONAL else "not_applicable"),
            f"{rid}: provisional metrics changed")
        check(item["acceptance_source"] == f"docs/product/prd.md §{'8' if prefix == 'RF-' else '9'} ({rid})",
              f"{rid}: acceptance criterion link mismatch")
        check(re.search(rf"^\| {re.escape(rid)} \|.*?\| Must\* \|", matrix, re.M),
              f"{rid}: missing Must tag in human matrix")
        check(re.search(rf"^\| {re.escape(rid)} \|", priority, re.M),
              f"{rid}: missing in prioritization")
        check(item["first_implementation_milestone"].startswith("F"),
              f"{rid}: first milestone missing")
        check(item["wbs_stages"], f"{rid}: no WBS linkage")
        for stage in item["wbs_stages"]:
            check(re.fullmatch(r"F\d\d(?:-E\d\d)?(?:\.\.F\d\d-E\d\d)?", stage) is not None,
                  f"{rid}: invalid WBS reference {stage}")
        for scenario in item["user_scenarios"]:
            check(re.fullmatch(r"CU-0[1-5]", scenario) is not None,
                  f"{rid}: invalid scenario {scenario}")
        for path in item["preparatory_fixture_references"]:
            check(path.startswith("tests/fixtures/"), f"{rid}: unexpected fixture path {path}")
            check((ROOT / path).is_file(), f"{rid}: broken fixture {path}")
            check(Path(path).name in matrix, f"{rid}: fixture missing from matrix")
        for scenario in item["proposed_test_scenarios"]:
            check(re.fullmatch(r"T-DOM-\d{2}", scenario) is not None and scenario in domain,
                  f"{rid}: undocumented test scenario {scenario}")
        for decision in item["decision_dependencies"]:
            check(re.fullmatch(r"OQ-0[3-9]", decision) is not None and decision in decisions,
                  f"{rid}: bad decision reference {decision}")
        deps = item["depends_on_proposal"]
        check(len(set(deps)) == len(deps), f"{rid}: duplicate dependency")
        check(all(x in REQUIRED and x != rid for x in deps), f"{rid}: invalid dependency")
        all_dependencies[rid] = deps

    # Proposal graph must be acyclic, including cross-functional dependencies.
    visiting: set[str] = set()
    visited: set[str] = set()

    def traverse(node: str) -> None:
        if node in visited:
            return
        check(node not in visiting, f"dependency cycle at {node}")
        visiting.add(node)
        for parent in all_dependencies[node]:
            traverse(parent)
        visiting.remove(node)
        visited.add(node)

    for name in REQUIRED:
        traverse(name)

    check("RF-08" in blueprint and "RF-11" in blueprint, "blueprint RF coverage missing")
    check("Fase 00" in prd, "PRD context missing")
    check((TEST_FIXTURES / "expected-results.json").is_file(), "fixture manifest missing")
    check(len(list(TEST_FIXTURES.glob("*.xlsx"))) == 10, "expect 10 synthetic XLSX fixtures")
    check(len([r for r in reqs if r["type"] == "functional"]) == 11, "functional count mismatch")
    check(len([r for r in reqs if r["type"] == "non_functional"]) == 10,
          "nonfunctional count mismatch")
    print("PASS CRONO-004 requirements: 11 RF + 10 RNF; all 21 Must (proposed)")
    print("PASS acceptance references, WBS, CU, fixture paths, domain test scenarios")
    print("PASS provisional RNF-03/04/08; dependency graph acyclic")
    print("PASS source alignment; PRD/Gate G0 unapproved; OQ-04/05 pending")
    print("NOTE: Documentation checks only; zero product features validated.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(validate())
    except (AssertionError, KeyError, TypeError, ValueError) as exc:
        print(f"FAIL CRONO-004: {exc}", file=sys.stderr)
        sys.exit(1)
