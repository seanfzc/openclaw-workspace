#!/usr/bin/env python3
"""
Extract sample text from P6 PDFs to understand question formats.
"""

import pdfplumber
from pathlib import Path

def extract_pdf_sample(pdf_path, num_pages=3):
    """Extract text sample from first few pages of PDF."""
    samples = []
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page_num in range(min(num_pages, len(pdf.pages))):
                page = pdf.pages[page_num]
                text = page.extract_text()
                if text:
                    # Clean up text
                    lines = [line.strip() for line in text.split('\n') if line.strip()]
                    samples.extend(lines[:20])  # First 20 lines per page
    except Exception as e:
        print(f"Error extracting from {pdf_path.name}: {e}")
    
    return samples

def main():
    pdfs_to_check = [
        Path('/Users/zcaeth/Desktop/sg_exam_papers/Maths/P6/2025/Other/2025 P6 Maths Weighted Assessment 2 St Nicholas.pdf'),
        Path('/Users/zcaeth/Desktop/sg_exam_papers/Maths/P6/2025/Other/2025 P6 Maths Weighted Assessment 1 Raffles Girls.pdf'),
        Path('/Users/zcaeth/Desktop/sg_exam_papers/Maths/P6/2025/Other/2025 P6 Maths Weighted Assessment 1 Rosyth.pdf')
    ]
    
    for pdf_path in pdfs_to_check:
        if not pdf_path.exists():
            print(f"PDF not found: {pdf_path}")
            continue
        
        print(f"\n{'='*80}")
        print(f"EXTRACTING FROM: {pdf_path.name}")
        print(f"{'='*80}")
        
        samples = extract_pdf_sample(pdf_path, num_pages=2)
        
        if not samples:
            print("No text extracted - may be scanned/image PDF")
            continue
        
        print(f"First {len(samples)} lines of text:")
        for i, line in enumerate(samples[:30], 1):
            print(f"{i:3}: {line}")
        
        # Check for Algebra/Ratio indicators
        print(f"\nAnalysis:")
        algebra_indicators = ['x', 'y', '=', 'algebra', 'expression', 'equation', 'simplify']
        ratio_indicators = [':', 'ratio', 'share', 'proportion', 'fraction']
        
        text_lower = ' '.join(samples).lower()
        
        algebra_found = [ind for ind in algebra_indicators if ind in text_lower]
        ratio_found = [ind for ind in ratio_indicators if ind in text_lower]
        
        if algebra_found:
            print(f"  Algebra indicators found: {algebra_found}")
        if ratio_found:
            print(f"  Ratio indicators found: {ratio_found}")
        
        if not algebra_found and not ratio_found:
            print("  No clear Algebra/Ratio indicators in sample")

if __name__ == "__main__":
    main()