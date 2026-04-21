#!/usr/bin/env python3
"""Quick test of EasyOCR functionality"""

import easyocr
from pathlib import Path
import cv2

def test_easyocr():
    print("Initializing EasyOCR...")
    reader = easyocr.Reader(['en'], gpu=False, verbose=False)
    print("✅ EasyOCR initialized successfully\n")
    
    # Test on one page
    test_image = Path(__file__).parent / "acs_pdf_page012.png"
    
    if not test_image.exists():
        print(f"❌ Test image not found: {test_image}")
        return False
    
    print(f"Testing on: {test_image.name}")
    
    # Read image
    img = cv2.imread(str(test_image))
    if img is None:
        print("❌ Could not load image")
        return False
    
    # Run OCR
    print("Running OCR...")
    results = reader.readtext(img)
    
    print(f"\n✅ OCR complete! Found {len(results)} text regions\n")
    
    # Look for Q12 indicators
    print("Looking for Q12 indicators:")
    found_q12 = False
    for (bbox, text, conf) in results:
        text_lower = text.lower()
        if any(kw in text_lower for kw in ['12', 'square', '4cm', 'five', '5']):
            print(f"  '{text}' (conf: {conf:.2f})")
            found_q12 = True
    
    if not found_q12:
        print("  No Q12 indicators found on this page")
    
    return True

if __name__ == "__main__":
    success = test_easyocr()
    exit(0 if success else 1)
