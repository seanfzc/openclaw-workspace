#!/usr/bin/env python3
"""
RapidOCR test script for handwritten samples.
"""

from rapidocr import RapidOCR
from pathlib import Path
import sys

def test_rapidocr(image_path=None):
    """Test RapidOCR on an image."""
    print("=" * 60)
    print("RapidOCR Test")
    print("=" * 60)
    
    # Initialize RapidOCR
    try:
        engine = RapidOCR()
        print("✅ RapidOCR initialized successfully")
    except Exception as e:
        print(f"❌ Failed to initialize RapidOCR: {e}")
        return False
    
    # If no image provided, just verify initialization
    if not image_path:
        print("\nNo image provided. RapidOCR is ready to use.")
        print("Usage: python3 test_rapidocr.py <image_path>")
        return True
    
    # Check if image exists
    img_path = Path(image_path)
    if not img_path.exists():
        print(f"❌ Image not found: {image_path}")
        return False
    
    print(f"\nProcessing image: {image_path}")
    
    # Run OCR
    try:
        result, elapse = engine(str(img_path))
        
        if result:
            print(f"\n✅ OCR completed in {elapse:.3f}s")
            print(f"\nDetected text ({len(result)} lines):")
            print("-" * 60)
            for i, (box, text, score) in enumerate(result, 1):
                print(f"{i:2d}: [{score:.2f}] {text}")
            print("-" * 60)
            return True
        else:
            print("\n⚠️ No text detected in image")
            return False
            
    except Exception as e:
        print(f"❌ OCR failed: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        test_rapidocr(sys.argv[1])
    else:
        test_rapidocr()