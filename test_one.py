#!/usr/bin/env python3
import sys
sys.path.insert(0, './ATOM-SG Pilot/05-Backend/scripts')
import ocr_pipeline
from pathlib import Path

pdf_path = Path("./ATOM-SG Pilot/05-Backend/artifacts/renders/G001_G1_20260413_143401.pdf")
print("Processing", pdf_path)
results = ocr_pipeline.extract_text_from_pdf(pdf_path, dpi=200)
for pg, data in results.items():
    print(f"Page {pg}: confidence {data['confidence']:.2f}")
    print("Text:", data['text'][:200])
    print()