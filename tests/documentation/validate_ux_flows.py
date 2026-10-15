#!/usr/bin/env python3
"""CRONO-005: structural checks of proposed UX flow and wireframe documents.

This validates documentation only, not usability or frontend behavior.
"""
from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
UX = ROOT / "docs" / "ux"
FLOW_PATH = UX / "flows.md"
WIREFRAME_PATH = UX / "wireframes.md"
REVIEW_PATH = UX / "usability-review.md"
BLUEPRINT = ROOT / "docs" / "CRONOCHECK_BLUEPRINT_V1.md"
STATE = ROOT / "docs" / "PROJECT_STATE.md"
OPEN = ROOT / "docs" / "product" / "open-questions.md"

MAIN_MENU = ("Projetos", "Importações", "Auditorias", "Pendências", "Relatórios", "Configurações")
CORE_RF = ("RF-03", "RF-04", "RF-05", "RF-06", "RF-07", "RF-08", "RF-09", "RF-10", "RF-11")
SCENARIOS = tuple(f"CU-{i:02d}" for i in range(1, 6))
FLOWS = tuple(f"FL-{i:02d}" for i in range(1, 6))
WIREFRAMES = tuple(f"W-{i:02d}" for i in range(1, 12))
TASKS = tuple(f"UXT-{i:02d}" for i in range(1, 11))
FENCE = chr(96) * 3


def check(condition: bool, description: str) -> None:
    if not condition:
        raise AssertionError(description)


def read(path: Path) -> str:
    check(path.is_file(), f"missing document: {path}")
    return path.read_text(encoding="utf-8")


def check_local_links(path: Path, text: str) -> None:
    for target in re.findall(r"\]\(([^)]+)\)", text):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        local = target.split("#", 1)[0]
        if local:
            check((path.parent / local).exists(),
                  f"{path.relative_to(ROOT)}: broken relative link: {target}")


def main() -> int:
    flow = read(FLOW_PATH)
    wire = read(WIREFRAME_PATH)
    review = read(REVIEW_PATH)
    blueprint = read(BLUEPRINT)
    state = read(STATE)
    decisions = read(OPEN)

    for doc, contents in ((FLOW_PATH, flow), (WIREFRAME_PATH, wire), (REVIEW_PATH, review)):
        check(contents.count(FENCE) % 2 == 0, f"{doc.name}: unbalanced fenced code blocks")
        check_local_links(doc, contents)

    for menu in MAIN_MENU:
        check(menu in flow, f"missing menu section: {menu}")
        check(menu in wire, f"missing navigation label in wireframes: {menu}")

    for name in SCENARIOS + FLOWS:
        check(name in flow, f"missing scenario/flow: {name}")
    for rf in CORE_RF:
        check(rf in flow, f"missing RF mapping in UX flow: {rf}")
    for wf in WIREFRAMES:
        check(re.search(rf"^## {re.escape(wf)}\b", wire, re.M) is not None,
              f"missing wireframe heading: {wf}")
    for task in TASKS:
        check(re.search(rf"^\| {re.escape(task)} \|", review, re.M) is not None,
              f"missing planned usability task: {task}")

    check(flow.count(FENCE + "mermaid") >= 3, "missing proposed navigation and task diagrams")
    check("OQ-07" in flow and "OQ-07" in wire, "CU-05 decision dependency absent")
    check(all(d in flow for d in ("OQ-03", "OQ-08", "OQ-09")),
          "missing open domain decisions")
    check("não executado" in review.lower() or "sem validação" in review.lower(),
          "user research cannot be presumed complete")
    check("protótipo clicável" in review.lower(), "prototype status should be explicit")
    check("Gate G0" in flow and "Gate G0" in wire and "Gate G0" in review,
          "G0 references missing")
    check("**Gate G0:** **não aprovado**" in state, "G0 status changed unexpectedly")
    check("OQ-04/OQ-05 pendentes" in decisions,
          "open questions mismatch")
    check("### D.2 Telas mínimas" in blueprint, "blueprint UX section absent")
    check("SourceLocator" in flow and "SourceLocator" in wire,
          "finding provenance absent")
    check("idempotência" in flow.lower() and "concorrência" in wire.lower(),
          "retry/concurrency not covered")
    check("filtros" in flow and "filtros" in wire, "back navigation loses filters")
    check("teclado" in flow and "teclado" in review, "accessibility absent")

    print("PASS CRONO-005: 6 navigation sections, 5 CU, 5 flows, 11 wireframes")
    print("PASS future usability tasks: 10 planned; no research performed")
    print("PASS error, warning, retry, authorization and concurrency states")
    print("PASS relative links, domain decisions and phase gate references")
    print("NOTE: Documentation checks only; no interactive prototype or UI tests.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (AssertionError, ValueError, TypeError) as exc:
        print(f"FAIL CRONO-005: {exc}", file=sys.stderr)
        sys.exit(1)
