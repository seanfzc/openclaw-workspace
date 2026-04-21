#!/usr/bin/env python3
"""
Test OCR extraction on a geometry problem PDF.
"""
import sys
from pathlib import Path

# Import functions from existing OCR script
sys.path.insert(0, '.')
from ocr_extraction_script import extract_text_with_ocr, check_tesseract_installation

pdf_path = Path("./ATOM-SG Pilot/05-Backend/artifacts/renders/G001_G1_20260413_143401.pdf")
if not pdf_path.exists():
    print(f"PDF not found: {pdf_path}")
    sys.exit(1)

print(f"Processing {pdf_path.name}")
if not check_tesseract_installation():
    sys.exit(1)

# Extract text (pages 1 to 1)
ocr_text = extract_text_with_ocr(pdf_path, page_range=(1, 1))
if ocr_text:
    for page, text in ocr_text.items():
        print(f"Page {page}:")
        print(text)
        print("-" * 40)
else:
    print("No text extracted.")