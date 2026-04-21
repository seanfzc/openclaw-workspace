#!/usr/bin/env python3
"""
Test OCR pipeline on a single PDF.
"""
import sys
from pathlib import Path

# Add the backend scripts directory to path
sys.path.insert(0, str(Path(__file__).parent / "ATOM-SG Pilot" / "05-Backend" / "scripts"))

from ocr_pipeline import extract_text_from_pdf, save_ocr_results

pdf_path = Path("./ATOM-SG Pilot/05-Backend/artifacts/renders/G001_G1_20260413_143401.pdf")
if not pdf_path.exists():
    print(f"PDF not found: {pdf_path}")
    sys.exit(1)

print(f"Testing OCR on {pdf_path.name}")
results = extract_text_from_pdf(pdf_path, dpi=200)
print(f"Extracted {len(results)} pages")
for pg, data in results.items():
    print(f"Page {pg}: confidence {data['confidence']:.2f}")
    print("Text preview:", data['text'][:100])

# Save results
text_file, meta_file = save_ocr_results(pdf_path, results)
print(f"Saved text to {text_file}")
print(f"Saved metadata to {meta_file}")