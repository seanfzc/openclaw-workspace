#!/usr/bin/env python3
"""
Get basic info about PDFs.
"""

import pdfplumber
from pathlib import Path

def check_pdf(pdf_path):
    print(f"\nChecking: {pdf_path.name}")
    print("-" * 40)
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            print(f"Pages: {len(pdf.pages)}")
            
            # Check first few pages for text
            for i in range(min(3, len(pdf.pages))):
                page = pdf.pages[i]
                text = page.extract_text()
                print(f"\nPage {i+1}:")
                if text:
                    # Count lines and chars
                    lines = [l.strip() for l in text.split('\n') if l.strip()]
                    print(f"  Text lines: {len(lines)}")
                    print(f"  Sample lines:")
                    for line in lines[:5]:
                        print(f"    - {line[:80]}")
                else:
                    print("  No text extracted (may be scanned/image)")
                
                # Check for images
                if page.images:
                    print(f"  Images: {len(page.images)}")
    
    except Exception as e:
        print(f"Error: {e}")

def main():
    pdfs = [
        Path('/Users/zcaeth/Desktop/sg_exam_papers/Maths/P6/2025/Other/2025 P6 Maths Weighted Assessment 1 Rosyth.pdf'),
        Path('/Users/zcaeth/Desktop/sg_exam_papers/Maths/P6/2025/Other/2025 P6 Maths Weighted Assessment 2 St Nicholas.pdf'),
    ]
    
    for pdf_path in pdfs:
        if pdf_path.exists():
            check_pdf(pdf_path)
        else:
            print(f"\nPDF not found: {pdf_path}")

if __name__ == "__main__":
    main()