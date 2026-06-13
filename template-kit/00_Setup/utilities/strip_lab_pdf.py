#!/usr/bin/env python3
"""
strip_lab_pdf.py
Extracts clinical results from a lab PDF, stripping the patient header
(name, date of birth, address, Medicare number).

Usage:
    python strip_lab_pdf.py <path_to_pdf>
    python strip_lab_pdf.py <path_to_pdf> --header-lines 25

Output:
    <basename>-clean.txt in the same folder as the input PDF.

Requirements:
    pip install pdfplumber

Notes:
    Auto-detection works for most digitally-generated Australian lab PDFs.
    If the patient header is still visible in the output, use --header-lines
    with a higher number (e.g. --header-lines 25 or --header-lines 30).
    Scanned (image-only) PDFs are not supported — use manual copy-paste instead.
"""

import sys
import argparse
from pathlib import Path

try:
    import pdfplumber
except ImportError:
    print("ERROR: pdfplumber is not installed.")
    print("Install it with:  pip install pdfplumber")
    sys.exit(1)

RESULT_SECTION_MARKERS = [
    "clinical chemistry", "haematology", "full blood count",
    "biochemistry", "iron studies", "thyroid function", "lipids",
    "liver function", "immunology", "vitamins", "pathology report",
    "your results", "test results", "analyte", "reference interval",
    "coagulation", "urinalysis", "microbiology", "serology",
    "result", "reference range"
]


def find_results_start(lines):
    for i, line in enumerate(lines):
        lower = line.lower().strip()
        if any(marker in lower for marker in RESULT_SECTION_MARKERS):
            return max(0, i - 1)
    return min(20, len(lines))


def extract_clean_text(pdf_path, header_lines=None):
    text_pages = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                text_pages.append(text)

    if not text_pages:
        return None, 0

    full_text = "\n".join(text_pages)
    lines = full_text.split("\n")

    if header_lines is not None:
        start = header_lines
    else:
        start = find_results_start(lines)

    return "\n".join(lines[start:]), start


def main():
    parser = argparse.ArgumentParser(
        description="Strip patient header from lab PDF and extract clinical results."
    )
    parser.add_argument("pdf_path", help="Path to the lab result PDF")
    parser.add_argument(
        "--header-lines", type=int, default=None,
        help="Manually specify how many header lines to skip (overrides auto-detection)"
    )
    args = parser.parse_args()

    pdf_path = Path(args.pdf_path)

    if not pdf_path.exists():
        print(f"ERROR: File not found: {pdf_path}")
        sys.exit(1)

    if pdf_path.suffix.lower() != ".pdf":
        print(f"ERROR: Expected a PDF file, got: {pdf_path.suffix}")
        sys.exit(1)

    print(f"Processing: {pdf_path.name}")

    clean_text, lines_skipped = extract_clean_text(pdf_path, args.header_lines)

    if clean_text is None:
        print("ERROR: Could not extract text from this PDF.")
        print("The file may be a scanned image rather than a digital PDF.")
        print("For scanned documents, use the manual copy-paste method instead.")
        sys.exit(1)

    output_path = pdf_path.parent / (pdf_path.stem + "-clean.txt")
    output_path.write_text(clean_text, encoding="utf-8")

    print(f"Done. Header lines removed: {lines_skipped}")
    print(f"Clean output saved to: {output_path.name}")
    print()
    print("Review the output file before importing into Cowork.")
    print("If patient details are still visible, re-run with --header-lines 30")


if __name__ == "__main__":
    main()
