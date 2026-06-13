#!/usr/bin/env python3
"""
scan_for_pii.py — Personal Health Wiki PII Scanner

Scans wiki files for patterns that may indicate personally identifying
information was not fully stripped during import.

Reports file locations, line numbers, and pattern types only.
Does NOT echo the potentially-identifying content itself.

Usage:
  python scan_for_pii.py                     Scan transcribed/ folder (default)
  python scan_for_pii.py --all               Scan all .md files in the wiki
  python scan_for_pii.py --path /path/to/wiki
  python scan_for_pii.py --path /path/to/wiki --all

No dependencies beyond the Python standard library.
"""

import re
import sys
import argparse
from pathlib import Path


# ── Pattern definitions ────────────────────────────────────────────────────────
#
# HIGH_CONFIDENCE: field labels that should never appear in PII-stripped wiki
# files. A match here almost certainly means stripping failed.
#
# LOWER_CONFIDENCE: format-based patterns. More likely to produce false
# positives from lab reference numbers, clinical values, or dates. Flag as
# "possible" — require manual review before acting.

HIGH_CONFIDENCE = [
    (
        "Patient name field",
        re.compile(r"(?mi)^\s*(patient\s*name|patient)\s*:"),
    ),
    (
        "Date of birth field",
        re.compile(r"(?i)\b(dob|d\.o\.b\.?|date\s+of\s+birth|born)\s*:"),
    ),
    (
        "Medicare / patient ID field",
        re.compile(
            r"(?i)\b(medicare(\s+no\.?|\s+number)?|mrn\.?|"
            r"ur\s*(no\.?|number)?|patient\s+id)\s*:\s*\d"
        ),
    ),
    (
        "Address field",
        re.compile(r"(?mi)^\s*(address|street|suburb|postcode|state)\s*:"),
    ),
    (
        "Phone / contact field",
        re.compile(
            r"(?mi)^\s*(phone|telephone|tel\.?|mobile|mob\.?|"
            r"contact(\s+no\.?)?)\s*:"
        ),
    ),
]

LOWER_CONFIDENCE = [
    (
        "Possible Medicare number (10 consecutive digits)",
        re.compile(r"\b\d{10}\b"),
    ),
    (
        "Possible Australian mobile number (04XX format)",
        re.compile(r"\b04\d{8}\b"),
    ),
    (
        "Possible Australian landline",
        re.compile(r"\b0[2-9]\d{8}\b"),
    ),
    (
        "Salutation adjacent to name (Mr/Mrs/Ms + title case word)",
        re.compile(r"\b(Mr|Mrs|Ms|Miss|Mx)\.?\s+[A-Z][a-z]{1,25}\b"),
    ),
]

# Lines beginning with these characters are likely template placeholders,
# code blocks, or markdown structure — skip lower-confidence checks on them.
SKIP_PREFIXES = ("#", ">", "```", "|", "-", "*", "[", "<!--")


def scan_file(filepath: Path) -> dict:
    """
    Scan a single file for PII patterns.
    Returns {'high': [(lineno, pattern_name), ...],
             'low':  [(lineno, pattern_name), ...]}
    or {'error': str} on read failure.
    """
    try:
        text = filepath.read_text(encoding="utf-8", errors="ignore")
    except OSError as exc:
        return {"error": str(exc)}

    lines = text.splitlines()
    findings = {"high": [], "low": []}

    for lineno, line in enumerate(lines, start=1):
        stripped = line.strip()

        # High-confidence checks — run on every line
        for pattern_name, pattern in HIGH_CONFIDENCE:
            if pattern.search(line):
                findings["high"].append((lineno, pattern_name))
                break  # one high finding per line is enough

        # Lower-confidence checks — skip structural/template lines
        if any(stripped.startswith(p) for p in SKIP_PREFIXES):
            continue
        if not stripped:
            continue

        for pattern_name, pattern in LOWER_CONFIDENCE:
            if pattern.search(line):
                findings["low"].append((lineno, pattern_name))
                break  # one low finding per line is enough

    return findings


def scan_directory(scan_path: Path) -> tuple:
    """
    Scan all .md files under scan_path.
    Returns (results, total_file_count) where results is a list of
    (Path, findings_dict) for files that had any findings.
    """
    md_files = sorted(scan_path.rglob("*.md"))
    results = []

    for filepath in md_files:
        findings = scan_file(filepath)
        if findings.get("high") or findings.get("low") or findings.get("error"):
            results.append((filepath, findings))

    return results, len(md_files)


def relative_or_abs(filepath: Path, base: Path) -> str:
    try:
        return str(filepath.relative_to(base))
    except ValueError:
        return str(filepath)


def print_report(results: list, scan_path: Path, total_files: int) -> int:
    """
    Print the scan report. Returns exit code (0 = clean, 1 = findings).
    Content of flagged lines is never printed.
    """
    high_total = sum(len(f[1].get("high", [])) for f in results)
    low_total = sum(len(f[1].get("low", [])) for f in results)
    affected = len([f for f in results if f[1].get("high") or f[1].get("low")])

    print()
    print("PII Scan Report")
    print("=" * 60)
    print(f"Scanned:          {scan_path}")
    print(f"Files checked:    {total_files}")
    print(f"Files with findings: {affected}")
    print()

    if not results or (high_total == 0 and low_total == 0):
        print("✅  No PII patterns detected.")
        print()
        return 0

    if high_total > 0:
        print("HIGH CONFIDENCE FINDINGS")
        print("Field labels that should not appear in PII-stripped wiki files.")
        print()
        for filepath, findings in results:
            highs = findings.get("high", [])
            if highs:
                rel = relative_or_abs(filepath, scan_path)
                for lineno, pattern_name in highs:
                    print(f"  ⚠️  {rel}")
                    print(f"      Line {lineno}: {pattern_name}")
        print()

    if low_total > 0:
        print("POSSIBLE FINDINGS  (lower confidence — verify manually)")
        print("May include false positives from lab reference numbers or dates.")
        print()
        for filepath, findings in results:
            lows = findings.get("low", [])
            if lows:
                rel = relative_or_abs(filepath, scan_path)
                for lineno, pattern_name in lows:
                    print(f"  ?   {rel}")
                    print(f"      Line {lineno}: {pattern_name}")
        print()

    print("-" * 60)
    print(
        f"Summary: {high_total} high-confidence finding(s), "
        f"{low_total} possible finding(s)"
    )
    print()
    print("This report shows locations and pattern types only.")
    print("Open flagged files directly to inspect the actual content.")

    if high_total > 0:
        print()
        print("⚠️  Resolve high-confidence findings before continuing analysis")
        print("   or sharing wiki files. Re-import affected files with")
        print("   corrected input (Option 2 — manual copy-paste of results")
        print("   table only — is the safest fallback).")

    return 1 if high_total > 0 else 0


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Scan Personal Health Wiki files for possible PII patterns. "
            "Reports locations only — does not echo flagged content."
        )
    )
    parser.add_argument(
        "--path",
        type=Path,
        default=Path("."),
        metavar="WIKI_ROOT",
        help="Path to wiki root folder (default: current directory)",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Scan all .md files in the wiki (default: 03_Patient_Records/transcribed/ only)",
    )
    args = parser.parse_args()

    wiki_root = args.path.resolve()

    if not wiki_root.exists():
        print(f"Error: path not found — {wiki_root}")
        sys.exit(2)

    if args.all:
        scan_path = wiki_root
        print(f"Scanning all .md files under: {scan_path}")
    else:
        scan_path = wiki_root / "03_Patient_Records" / "transcribed"
        if not scan_path.exists():
            print(f"Transcribed folder not found at:\n  {scan_path}")
            print()
            print(
                "Tip: run from your wiki root, or use --path to point at it.\n"
                "     Use --all to scan all .md files in the folder instead."
            )
            sys.exit(2)
        print(f"Scanning: {scan_path}")

    results, total_files = scan_directory(scan_path)

    if total_files == 0:
        print("No .md files found.")
        sys.exit(0)

    exit_code = print_report(results, scan_path, total_files)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
