#!/usr/bin/env python3
"""Validate synthetic OOXML fixtures against their versioned manifest.

F00-E04 structural verification only; this is NOT the CronoCheck importer or audit engine.
Only Python's standard library is required. No formula is evaluated.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from datetime import date
import json
from pathlib import Path
import sys
import xml.etree.ElementTree as ET
from zipfile import ZipFile, BadZipFile

ROOT = Path(__file__).resolve().parent
SP = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
REQUIRED_PARTS = {
    "[Content_Types].xml",
    "_rels/.rels",
    "xl/workbook.xml",
    "xl/_rels/workbook.xml.rels",
    "xl/worksheets/sheet1.xml",
}
HEADERS = [
    "activity_id", "name", "start_date", "finish_date",
    "duration_calendar_days", "predecessors_fs", "parent_activity_id",
]


class FixtureError(AssertionError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise FixtureError(message)


def read_cell(node: ET.Element) -> tuple[str, bool]:
    formula = node.find(f"{SP}f")
    inline = node.find(f"{SP}is/{SP}t")
    numeric = node.find(f"{SP}v")
    if inline is not None:
        return inline.text or "", formula is not None
    if numeric is not None:
        return numeric.text or "", formula is not None
    return "", formula is not None


def load_fixture(path: Path) -> tuple[list[dict[str, str]], list[str], list[str]]:
    try:
        with ZipFile(path, "r") as z:
            members = set(z.namelist())
            require(REQUIRED_PARTS.issubset(members), f"{path.name}: OOXML parts missing")
            require(members == REQUIRED_PARTS, f"{path.name}: unexpected OOXML parts: {members ^ REQUIRED_PARTS}")
            require(z.testzip() is None, f"{path.name}: bad ZIP CRC")
            for part in REQUIRED_PARTS:
                # Enforce well-formed XML throughout the OOXML package.
                ET.fromstring(z.read(part))
            document = ET.fromstring(z.read("xl/worksheets/sheet1.xml"))
            wb = ET.fromstring(z.read("xl/workbook.xml"))
    except (BadZipFile, ET.ParseError) as exc:
        raise FixtureError(f"{path.name}: invalid OOXML: {exc}") from exc

    sheets = wb.find(f"{SP}sheets")
    require(sheets is not None and len(list(sheets)) == 1, f"{path.name}: expected one sheet")
    require(list(sheets)[0].attrib.get("name") == "Activities", f"{path.name}: wrong sheet name")

    data = document.find(f"{SP}sheetData")
    require(data is not None, f"{path.name}: missing sheetData")
    rows = list(data.findall(f"{SP}row"))
    require(len(rows) > 1 and rows[0].attrib.get("r") == "1", f"{path.name}: missing header row")

    columns = []
    for cell in rows[0].findall(f"{SP}c"):
        value, is_formula = read_cell(cell)
        require(not is_formula, f"{path.name}: formula in header")
        columns.append(value)
    require(columns == HEADERS, f"{path.name}: header mismatch: {columns!r}")

    records: list[dict[str, str]] = []
    formula_cells: list[str] = []
    invalid_dates: list[str] = []
    for i, node in enumerate(rows[1:], start=2):
        require(node.attrib.get("r") == str(i), f"{path.name}: nonsequential row at {i}")
        cells = {c.attrib.get("r", ""): c for c in node.findall(f"{SP}c")}
        values = {}
        for j, key in enumerate(HEADERS):
            coord = chr(65 + j) + str(i)
            val, is_formula = read_cell(cells[coord]) if coord in cells else ("", False)
            values[key] = val
            if is_formula:
                formula_cells.append(coord)
        records.append(values)
        for key, col in (("start_date", "C"), ("finish_date", "D")):
            try:
                require(len(values[key]) == 10, "invalid ISO length")
                date.fromisoformat(values[key])
            except (ValueError, FixtureError):
                invalid_dates.append(col + str(i))
        try:
            duration = int(values["duration_calendar_days"])
            require(duration >= 1, "nonpositive duration")
        except (ValueError, FixtureError):
            raise FixtureError(f"{path.name}: invalid duration at E{i}") from None
    return records, formula_cells, invalid_dates


def structural_findings(rows: list[dict[str, str]], invalid_dates: list[str]) -> list[dict]:
    result: list[dict] = []
    ids = defaultdict(list)
    for i, x in enumerate(rows, start=2):
        ids[x["activity_id"]].append(i)
    for identifier, places in sorted(ids.items()):
        if len(places) > 1:
            result.append({"category": "duplicate_activity_id", "source_rows": places, "activity_id": identifier})

    neighbors: dict[str, list[str]] = defaultdict(list)
    for i, x in enumerate(rows, start=2):
        aid = x["activity_id"]
        for pred in (v.strip() for v in x["predecessors_fs"].split(",")):
            if not pred:
                continue
            if pred not in ids:
                result.append({"category": "missing_predecessor", "source_row": i, "activity_id": aid, "missing_id": pred})
            else:
                neighbors[pred].append(aid)

    # Tarjan strongly connected components. No dependency-type conversion is performed.
    index = 0
    stack: list[str] = []
    indices: dict[str, int] = {}
    low: dict[str, int] = {}
    on_stack = set()

    def dfs(v: str) -> None:
        nonlocal index
        indices[v] = low[v] = index
        index += 1
        stack.append(v)
        on_stack.add(v)
        for w in neighbors[v]:
            if w not in indices:
                dfs(w)
                low[v] = min(low[v], low[w])
            elif w in on_stack:
                low[v] = min(low[v], indices[w])
        if low[v] == indices[v]:
            group = []
            while True:
                u = stack.pop()
                on_stack.remove(u)
                group.append(u)
                if u == v:
                    break
            if len(group) > 1 or (len(group) == 1 and v in neighbors[v]):
                result.append({"category": "dependency_cycle", "activity_ids": sorted(group)})

    for aid in sorted(ids):
        if aid not in indices:
            dfs(aid)

    for i, x in enumerate(rows, start=2):
        if "C" + str(i) not in invalid_dates and "D" + str(i) not in invalid_dates:
            if date.fromisoformat(x["finish_date"]) < date.fromisoformat(x["start_date"]):
                result.append({"category": "reversed_date_range", "source_row": i, "activity_id": x["activity_id"]})
    return sorted(result, key=lambda item: (item["category"], json.dumps(item, sort_keys=True)))


def verify_comparison(base: list[dict[str, str]], target: list[dict[str, str]], expected: dict) -> None:
    old = {x["activity_id"]: x for x in base}
    new = {x["activity_id"]: x for x in target}
    require(len(old) == len(base) and len(new) == len(target), "ambiguous IDs in comparison")
    actual = {
        "added": sorted(new.keys() - old.keys()),
        "removed": sorted(old.keys() - new.keys()),
        "modified": sorted(k for k in old.keys() & new.keys() if old[k] != new[k]),
        "unchanged": sorted(k for k in old.keys() & new.keys() if old[k] == new[k]),
    }
    for kind, wanted in expected.items():
        require(actual[kind] == sorted(wanted), f"comparison {kind}: actual={actual[kind]}, wanted={wanted}")


def main() -> int:
    spec = json.loads((ROOT / "expected-results.json").read_text(encoding="utf-8"))
    require(spec["schema_version"] == "0.1.0", "unexpected manifest version")
    require(spec["workbook_layout"]["headers"] == HEADERS, "manifest header mismatch")
    saved: dict[str, list[dict[str, str]]] = {}
    for fx in spec["fixtures"]:
        filename = fx["file"]
        path = ROOT / filename
        require(path.is_file(), f"missing fixture: {path}")
        records, formulas, invalid = load_fixture(path)
        require(len(records) == fx["expected_data_rows"], f"{filename}: row count mismatch")
        issues = fx["import"]["issues"]
        expected_formula = sorted(i["cell"] for i in issues if i["code"] == "IMP_FORMULA_IN_MAPPED_CELL")
        expected_date = sorted(i["cell"] for i in issues if i["code"] == "IMP_INVALID_DATE")
        require(sorted(formulas) == expected_formula, f"{filename}: formula cell mismatch {formulas}")
        require(sorted(invalid) == expected_date, f"{filename}: invalid dates mismatch {invalid}")
        require(fx["import"]["status"] == ("rejected" if issues else "accepted"), f"{filename}: import status inconsistent")
        expected_findings = sorted(fx["audit"]["expected_structural_categories"], key=lambda x: (x["category"], json.dumps(x, sort_keys=True)))
        actual_findings = structural_findings(records, invalid)
        require(actual_findings == expected_findings, f"{filename}: structural findings mismatch: {actual_findings}")
        saved[filename] = records
        print(f"OK {filename:31} rows={len(records):5} import={fx['import']['status']:8} findings={len(actual_findings)}")
    for cmp in spec["comparisons"]:
        verify_comparison(saved[cmp["base_file"]], saved[cmp["target_file"]], cmp["expected"])
        print(f"OK version diff {cmp['base_file']} -> {cmp['target_file']}")
    require(len(set(saved)) == len(spec["fixtures"]), "duplicate fixture entries")
    print(f"PASS: {len(saved)} OOXML workbooks + {len(spec['comparisons'])} version comparisons (structural checks only)")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except FixtureError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
