#!/usr/bin/env python3
"""
Extract Q12 using PaddleOCR for text + OpenCV for geometry
"""

import cv2
import numpy as np
from pathlib import Path
from paddleocr import PaddleOCR
import json


def extract_with_paddle(image_path, ocr):
    """Use PaddleOCR to extract text with bounding boxes."""
    result = ocr.predict(str(image_path))
    
    detections = []
    if result:
        for item in result:
            if 'text' in item and 'score' in item:
                detections.append({
                    'text': item['text'],
                    'confidence': float(item['score']),
                    'bbox': item.get('points', [])
                })
    
    return detections


def find_geometric_shapes(image_path):
    """Find squares and rectangles using OpenCV."""
    img = cv2.imread(str(image_path))
    if img is None:
        return None, None, None
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Adaptive thresholding for better edge detection
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                   cv2.THRESH_BINARY_INV, 11, 2)
    
    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    squares = []
    rectangles = []
    
    for contour in contours:
        area = cv2.contourArea(contour)
        if area < 500:  # Filter small noise
            continue
        
        epsilon = 0.05 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        
        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(approx)
            aspect_ratio = float(w) / h if h > 0 else 0
            
            shape_info = {
                'x': int(x),
                'y': int(y),
                'width': int(w),
                'height': int(h),
                'aspect_ratio': float(aspect_ratio),
                'area': int(area)
            }
            
            if 0.8 <= aspect_ratio <= 1.2:
                squares.append(shape_info)
            else:
                rectangles.append(shape_info)
    
    return squares, rectangles, img


def analyze_page(image_path, ocr):
    """Analyze a page for Q12 content."""
    print(f"\n{'='*60}")
    print(f"Analyzing: {image_path.name}")
    print(f"{'='*60}")
    
    # Extract text
    print("\n--- PaddleOCR Text Detection ---")
    text_results = extract_with_paddle(image_path, ocr)
    
    q12_indicators = []
    for item in text_results:
        text = item['text'].lower()
        if any(kw in text for kw in ['12', 'square', '4cm', '4 cm', 'five', '5']):
            print(f"  '{item['text']}' (conf: {item['confidence']:.2f})")
            q12_indicators.append(item)
    
    # Find shapes
    print("\n--- OpenCV Shape Detection ---")
    squares, rectangles, img = find_geometric_shapes(image_path)
    
    if squares:
        print(f"  Found {len(squares)} squares")
        for i, sq in enumerate(sorted(squares, key=lambda x: x['area'], reverse=True)[:5]):
            print(f"    {i+1}. {sq['width']}x{sq['height']} px at ({sq['x']}, {sq['y']})")
    
    if rectangles:
        print(f"  Found {len(rectangles)} rectangles")
    
    # Determine if Q12 candidate
    has_five_squares = len(squares) >= 5
    has_q12_text = len(q12_indicators) > 0
    is_candidate = has_five_squares or (has_q12_text and len(squares) >= 3)
    
    if is_candidate:
        print("\n*** Q12 CANDIDATE ***")
    
    return {
        'image': image_path.name,
        'q12_text_found': has_q12_text,
        'squares': len(squares),
        'rectangles': len(rectangles),
        'is_candidate': is_candidate,
        'text_detections': q12_indicators
    }


def main():
    base_path = Path(__file__).parent
    
    print("Initializing PaddleOCR...")
    ocr = PaddleOCR(lang='en')
    print("PaddleOCR ready\n")
    
    # Analyze all candidate pages
    candidates = sorted(base_path.glob("acs_pdf_page*.png"))
    
    results = []
    for candidate in candidates:
        result = analyze_page(candidate, ocr)
        results.append(result)
    
    # Summary
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    
    candidates_found = [r for r in results if r['is_candidate']]
    if candidates_found:
        print(f"\nFound {len(candidates_found)} Q12 candidates:")
        for r in candidates_found:
            print(f"  - {r['image']}: {r['squares']} squares, Q12 text: {r['q12_text_found']}")
    else:
        print("\nNo Q12 candidates found.")
        print("Top candidates by square count:")
        sorted_results = sorted(results, key=lambda x: x['squares'], reverse=True)
        for r in sorted_results[:3]:
            print(f"  - {r['image']}: {r['squares']} squares")
    
    # Save results
    with open(base_path / "paddle_analysis_results.json", 'w') as f:
        json.dump(results, f, indent=2)


if __name__ == "__main__":
    main()
