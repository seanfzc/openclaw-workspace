#!/usr/bin/env python3
"""
Quick scan of P6 PDFs to identify Algebra and Ratio content.
"""

import pdfplumber
import re
from pathlib import Path

# Algebra and Ratio keywords
ALGEBRA_KEYWORDS = [
    'algebra', 'algebraic', 'expression', 'equation', 'variable',
    'solve for', 'find x', 'find y', 'simplify', 'expand', 'factor',
    'coefficient', 'term', 'like terms', 'substitute', 'formula'
]

RATIO_KEYWORDS = [
    'ratio', 'proportion', 'share in the ratio', 'in the ratio',
    'simplify the ratio', 'equivalent ratio', 'ratio of', 'proportional',
    'direct proportion', 'inverse proportion'
]

PERCENTAGE_KEYWORDS = [
    'percentage', 'percent', '%', 'discount', 'increase', 'decrease',
    'profit', 'loss', 'interest', 'gst', 'tax'
]

def scan_pdf_for_keywords(pdf_path, max_pages=5):
    """Scan first few pages of PDF for Algebra/Ratio keywords."""
    results = {
        'algebra_count': 0,
        'ratio_count': 0,
        'percentage_count': 0,
        'algebra_examples': [],
        'ratio_examples': [],
        'percentage_examples': [],
        'total_pages': 0
    }
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            results['total_pages'] = len(pdf.pages)
            pages_to_scan = min(max_pages, len(pdf.pages))
            
            for page_num in range(pages_to_scan):
                page = pdf.pages[page_num]
                text = page.extract_text()
                if not text:
                    continue
                
                text_lower = text.lower()
                
                # Check for Algebra keywords
                for keyword in ALGEBRA_KEYWORDS:
                    if keyword in text_lower:
                        results['algebra_count'] += 1
                        # Extract context around keyword
                        lines = text.split('\n')
                        for line in lines:
                            if keyword in line.lower():
                                if len(results['algebra_examples']) < 3:
                                    results['algebra_examples'].append(line[:100])
                                break
                
                # Check for Ratio keywords
                for keyword in RATIO_KEYWORDS:
                    if keyword in text_lower:
                        results['ratio_count'] += 1
                        lines = text.split('\n')
                        for line in lines:
                            if keyword in line.lower():
                                if len(results['ratio_examples']) < 3:
                                    results['ratio_examples'].append(line[:100])
                                break
                
                # Check for Percentage keywords
                for keyword in PERCENTAGE_KEYWORDS:
                    if keyword in text_lower:
                        results['percentage_count'] += 1
                        lines = text.split('\n')
                        for line in lines:
                            if keyword in line.lower():
                                if len(results['percentage_examples']) < 3:
                                    results['percentage_examples'].append(line[:100])
                                break
                
    except Exception as e:
        print(f"Error scanning {pdf_path.name}: {e}")
        return None
    
    return results

def main():
    p6_dir = Path('/Users/zcaeth/Desktop/sg_exam_papers/Maths/P6/2025')
    pdf_files = list(p6_dir.rglob('*.pdf'))
    
    print(f"Found {len(pdf_files)} PDF files in {p6_dir}")
    print("=" * 80)
    
    # Scan each PDF
    pdf_results = []
    for pdf_path in pdf_files[:10]:  # Limit to first 10 for speed
        print(f"\nScanning: {pdf_path.name}")
        results = scan_pdf_for_keywords(pdf_path)
        
        if results:
            total_keywords = (results['algebra_count'] + 
                            results['ratio_count'] + 
                            results['percentage_count'])
            
            if total_keywords > 0:
                print(f"  Algebra keywords: {results['algebra_count']}")
                print(f"  Ratio keywords: {results['ratio_count']}")
                print(f"  Percentage keywords: {results['percentage_count']}")
                print(f"  Total pages: {results['total_pages']}")
                
                pdf_results.append({
                    'path': pdf_path,
                    'name': pdf_path.name,
                    'algebra': results['algebra_count'],
                    'ratio': results['ratio_count'],
                    'percentage': results['percentage_count'],
                    'total': total_keywords
                })
            else:
                print("  No Algebra/Ratio/Percentage keywords found")
    
    # Sort by total keyword count
    pdf_results.sort(key=lambda x: x['total'], reverse=True)
    
    print("\n" + "=" * 80)
    print("TOP PDFS FOR ALGEBRA/RATIO CONTENT:")
    print("=" * 80)
    
    for i, result in enumerate(pdf_results[:5], 1):
        print(f"{i}. {result['name']}")
        print(f"   Algebra: {result['algebra']}, Ratio: {result['ratio']}, Percentage: {result['percentage']}")
        print(f"   Total keywords: {result['total']}")
        print()

if __name__ == "__main__":
    main()