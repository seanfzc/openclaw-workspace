#!/usr/bin/env python3
"""Test PDF text extraction from different years."""

import fitz
from pathlib import Path

def test_pdf_text(pdf_path):
    print(f"\nTesting: {pdf_path.name}")
    if not pdf_path.exists():
        print("  File not found")
        return
    
    try:
        doc = fitz.open(pdf_path)
        print(f"  Pages: {len(doc)}")
        
        # Test first 5 pages
        text_lines = []
        for i in range(min(5, len(doc))):
            page = doc[i]
            text = page.get_text()
            lines = [l.strip() for l in text.split('\n') if l.strip()]
            text_lines.extend(lines)
            
            print(f"  Page {i+1}: {len(lines)} text lines")
            if lines:
                print(f"    Sample: {lines[0][:80]}")
        
        doc.close()
        
        # Check if it's likely scanned (minimal text)
        if len(text_lines) < 10:
            print("  STATUS: LIKELY SCANNED IMAGE (minimal OCR text)")
        else:
            print("  STATUS: MAY HAVE SELECTABLE TEXT")
            
    except Exception as e:
        print(f"  Error: {e}")

def main():
    pdfs = [
        # 2025 Rosyth (already tested - scanned)
        Path('/Users/zcaeth/Desktop/sg_exam_papers/Maths/P6/2025/Other/2025 P6 Maths Weighted Assessment 1 Rosyth.pdf'),
        # 2022 Rosyth (maybe different)
        Path('/Users/zcaeth/Desktop/sg_exam_papers/Maths/P6/2022/Other/2022 P6 Maths Prelim Rosyth.pdf'),
        # 2022 St Nicholas (maybe different format)
        Path('/Users/zcaeth/Desktop/sg_exam_papers/Maths/P6/2022/Other/2022 P6 Maths Prelim Scgs.pdf'),
    ]
    
    print("PDF Text Extraction Test")
    print("="*80)
    
    for pdf in pdfs:
        test_pdf_text(pdf)

if __name__ == "__main__":
    main()