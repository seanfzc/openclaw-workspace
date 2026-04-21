#!/usr/bin/env python3
"""Quick test of pages 10-11 for Q12"""

import easyocr
import cv2
from pathlib import Path

def analyze_page(image_path, reader):
    print(f"\n{'='*60}")
    print(f"Analyzing: {image_path.name}")
    print(f"{'='*60}")
    
    img = cv2.imread(str(image_path))
    if img is None:
        print("❌ Could not load image")
        return
    
    # Run OCR
    results = reader.readtext(img)
    
    print(f"Found {len(results)} text regions")
    
    # Look for Q12 indicators
    q12_indicators = []
    for (bbox, text, conf) in results:
        text_lower = text.lower()
        if any(kw in text_lower for kw in ['12', 'square', '4cm', '4 cm', 'five', '5', 'x =', 'x=']):
            print(f"  '{text}' (conf: {conf:.2f})")
            q12_indicators.append(text)
    
    if not q12_indicators:
        print("  (No Q12 indicators)")
    else:
        print(f"\n*** Q12 CANDIDATE: {len(q12_indicators)} matches ***")
    
    return len(q12_indicators) > 0

def main():
    base_path = Path(__file__).parent
    
    print("Initializing EasyOCR...")
    reader = easyocr.Reader(['en'], gpu=False, verbose=False)
    print("✅ Ready\n")
    
    # Test pages 10 and 11
    pages = ["acs_pdf_page010.png", "acs_pdf_page011.png"]
    
    for page in pages:
        path = base_path / page
        if path.exists():
            analyze_page(path, reader)
        else:
            print(f"❌ Not found: {page}")

if __name__ == "__main__":
    main()
