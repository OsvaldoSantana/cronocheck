#!/usr/bin/env python3
"""Verify explicit OQ decisions from 15 October without inventing PRD/G0 approval.

This tests document consistency only; never infers approval from a merged PR.
"""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
PRODUCT = ROOT / "docs" / "product"


def require(valid: bool, message: str) -> None:
    if not valid:
        raise AssertionError(message)


def content(path: Path) -> str:
    require(path.is_file(), f"missing file: {path}")
    return path.read_text(encoding="utf-8")


def parse_oqs(text: str) -> dict[str, str]:
    result = {}
    for line in text.splitlines():
        if re.match(r"^\| OQ-\d\d \|", line):
            cells = [part.strip().replace("**", "") for part in line.split("|")[1:-1]]
            require(len(cells) == 9, "invalid OQ decision row: " + line[:80])
            require(cells[0] not in result, "duplicate OQ row " + cells[0])
            result[cells[0]] = cells[-1]
    return result


def main() -> int:
    source = content(PRODUCT / "open-questions.md")
    decisions = parse_oqs(source)
    expected = {f"OQ-{x:02d}" for x in range(1, 10)}
    require(set(decisions) == expected, "require exactly OQ-01 to OQ-09")
    for i in (1, 2, 3, 6, 7, 8, 9):
        key = f"OQ-{i:02d}"
        require("aprovad" in decisions[key].lower(), f"{key} approval not recorded")
    for i in (4, 5):
        key = f"OQ-{i:02d}"
        require("pendente" in decisions[key].lower(), f"{key} must remain pending")

    record = content(PRODUCT / "decisions-2026-10-15.md")
    require("rejeitar" in record.lower() and "FS simples" in record,
            "OQ-03 rejection of FS-only not traceable")
    for key in ("OQ-03", "OQ-06", "OQ-07", "OQ-08", "OQ-09"):
        require(key in record, f"{key}: decision not in signed-off narrative")
    require("NÃO DECIDIDA" in record, "OQ-04/05 limitations missing")
    for path in ("architecture-options-oq04.md", "performance-options-oq05.md",
                 "dependency-domain-requirements.md"):
        require((PRODUCT / path).is_file(), f"decision attachment missing: {path}")

    model = content(PRODUCT / "dependency-domain-requirements.md")
    for rel in ("FS", "SS", "FF", "SF", "lag/lead", "Calendários", "SourceLocator"):
        require(rel.lower() in model.lower(), f"domain model scope missing: {rel}")
    require("não" in model.lower() and "fixture" in model.lower(),
            "do not mistake synthetic fixtures for final domain")
    require("OQ-04" in content(PRODUCT / "architecture-options-oq04.md"), "OQ-04 study absent")
    perf = content(PRODUCT / "performance-options-oq05.md")
    for nonfunctional in ("RNF-03", "RNF-04", "RNF-08"):
        require(nonfunctional in perf, f"performance comparison lacks {nonfunctional}")

    prd = content(PRODUCT / "prd.md")
    state = content(ROOT / "docs" / "PROJECT_STATE.md")
    require("Não aprovado" in prd and "v1.2" in prd, "PRD approval prematurely implied")
    require("**Gate G0:** **não aprovado**" in state, "Gate G0 approval prematurely implied")
    require("**Fase 01:** não iniciada" in state, "F01 started before approved gate")
    require("OQ-04 e OQ-05" in state and "Pendentes" in state,
            "project state not updated for open choices")

    print("PASS OQ decision register: OQ-01/02/03/06/07/08/09 approved as scoped")
    print("PASS OQ-04/05 pending, decision briefs present, FS-only model rejected")
    print("PASS PRD v1.2 not approved; G0 not approved; F01 not started")
    print("NOTE: Documentary assertions only, not tests of a working product.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (AssertionError, ValueError, TypeError, KeyError) as exc:
        print(f"FAIL OQ decisions: {exc}", file=sys.stderr)
        sys.exit(1)
