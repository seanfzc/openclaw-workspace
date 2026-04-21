#!/usr/bin/env python3
"""Detailed analysis of page 10 for Q12"""

import easyocr
import cv2
from pathlib import Path

def analyze_page10():
    base_path = Path(__file__).parent
    image_path = base_path / "acs_pdf_page010.png"
    
    print("Initializing EasyOCR...")
    reader = easyocr.Reader(['en'], gpu=False, verbose=False)
    print("✅ Ready\n")
    
    img = cv2.imread(str(image_path))
    if img is None:
        print("❌ Could not load image")
        return
    
    print(f"Image size: {img.shape}")
    
    # Run OCR
    results = reader.readtext(img)
    
    print(f"\nFound {len(results)} text regions:\n")
    
    # Print all text with confidence
    for i, (bbox, text, conf) in enumerate(results):
        print(f"{i+1:2d}. '{text}' (conf: {conf:.2f})")
    
    # Look for question numbers
    print("\n" + "="*60)
    print("QUESTION NUMBER ANALYSIS")
    print("="*60)
    
    for i, (bbox, text, conf) in enumerate(results):
        text_clean = text.strip()
        # Look for standalone numbers that could be question numbers
        if text_clean.isdigit() and 1 <= int(text_clean) <= 30:
            print(f"Question {text_clean} at position {i+1}")

if __name__ == "__main__":
    analyze_page10()
