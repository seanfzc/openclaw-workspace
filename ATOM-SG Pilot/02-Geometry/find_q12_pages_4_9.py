#!/usr/bin/env python3
"""Find Q12 in pages 4-9"""

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
        return 0
    
    # Run OCR
    results = reader.readtext(img)
    
    print(f"Found {len(results)} text regions")
    
    # Look for Q12 indicators
    matches = []
    for (bbox, text, conf) in results:
        text_lower = text.lower()
        if any(kw in text_lower for kw in ['12', 'square', '4cm', '4 cm', 'five', '5', 'x =', 'x=']):
            print(f"  '{text}' (conf: {conf:.2f})")
            matches.append(text)
    
    if not matches:
        print("  (No Q12 indicators)")
    
    return len(matches)

def main():
    base_path = Path(__file__).parent
    
    print("Initializing EasyOCR...")
    reader = easyocr.Reader(['en'], gpu=False, verbose=False)
    print("✅ Ready\n")
    
    # Test pages 4-9
    pages = [f"acs_page0{i}.png" for i in range(4, 10)]
    
    best_page = None
    best_matches = 0
    
    for page in pages:
        path = base_path / page
        if path.exists():
            matches = analyze_page(path, reader)
            if matches > best_matches:
                best_matches = matches
                best_page = page
        else:
            print(f"❌ Not found: {page}")
    
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    if best_page:
        print(f"Best candidate: {best_page} with {best_matches} matches")
    else:
        print("No Q12 candidates found in pages 4-9")

if __name__ == "__main__":
    main()
