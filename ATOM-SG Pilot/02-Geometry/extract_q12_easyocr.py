#!/usr/bin/env python3
"""
Extract Q12 using EasyOCR for text + OpenCV for geometry
Fast and reliable approach
"""

import cv2
import numpy as np
from pathlib import Path
import json

# EasyOCR imports
try:
    import easyocr
    EASYOCR_AVAILABLE = True
except ImportError:
    EASYOCR_AVAILABLE = False
    print("EasyOCR not available")

# pytesseract as fallback
try:
    import pytesseract
    from pytesseract import Output
    PYTESSERACT_AVAILABLE = True
except ImportError:
    PYTESSERACT_AVAILABLE = False


def extract_text_easyocr(image_path, reader):
    """Use EasyOCR to extract text with bounding boxes."""
    img = cv2.imread(str(image_path))
    if img is None:
        return []
    
    # Convert BGR to RGB for EasyOCR
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Detect text
    results = reader.readtext(img_rgb)
    
    detections = []
    for (bbox, text, conf) in results:
        detections.append({
            'text': text,
            'confidence': float(conf),
            'bbox': bbox
        })
    
    return detections


def extract_text_pytesseract(image_path):
    """Fallback: Use pytesseract to extract text."""
    img = cv2.imread(str(image_path))
    if img is None:
        return []
    
    # OCR with bounding boxes
    data = pytesseract.image_to_data(img, output_type=Output.DICT)
    
    detections = []
    n_boxes = len(data['text'])
    for i in range(n_boxes):
        if int(data['conf'][i]) > 30:  # Confidence threshold
            text = data['text'][i].strip()
            if text:
                x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
                detections.append({
                    'text': text,
                    'confidence': data['conf'][i] / 100.0,
                    'bbox': [[x, y], [x+w, y], [x+w, y+h], [x, y+h]]
                })
    
    return detections


def detect_squares_hough(image_path):
    """Detect squares using Hough Line Transform - better for thin lines."""
    img = cv2.imread(str(image_path))
    if img is None:
        return None, None
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Edge detection with Canny
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    
    # Dilate to connect nearby edges
    kernel = np.ones((2, 2), np.uint8)
    edges = cv2.dilate(edges, kernel, iterations=1)
    
    # Find lines using Hough Transform
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=50, 
                            minLineLength=30, maxLineGap=10)
    
    # Find contours on the edge image
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    squares = []
    rectangles = []
    
    for contour in contours:
        area = cv2.contourArea(contour)
        if area < 1000:  # Filter small noise
            continue
        
        # Approximate polygon
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
            
            # More lenient square detection for exam diagrams
            if 0.7 <= aspect_ratio <= 1.3:
                squares.append(shape_info)
            else:
                rectangles.append(shape_info)
    
    return squares, rectangles, img, lines


def analyze_page(image_path, reader=None):
    """Analyze a page for Q12 content."""
    print(f"\n{'='*60}")
    print(f"Analyzing: {image_path.name}")
    print(f"{'='*60}")
    
    # Extract text
    print("\n--- Text Detection ---")
    if EASYOCR_AVAILABLE and reader:
        text_results = extract_text_easyocr(image_path, reader)
        print("Using: EasyOCR")
    elif PYTESSERACT_AVAILABLE:
        text_results = extract_text_pytesseract(image_path)
        print("Using: pytesseract")
    else:
        text_results = []
        print("No OCR available")
    
    q12_indicators = []
    for item in text_results:
        text = item['text'].lower()
        if any(kw in text for kw in ['12', 'square', '4cm', '4 cm', 'five', '5', 'x=', 'y=']):
            print(f"  '{item['text']}' (conf: {item['confidence']:.2f})")
            q12_indicators.append(item)
    
    # Find shapes
    print("\n--- Geometry Detection ---")
    squares, rectangles, img, lines = detect_squares_hough(image_path)
    
    if squares:
        print(f"  Found {len(squares)} potential squares")
        # Sort by area and show top 5
        sorted_squares = sorted(squares, key=lambda x: x['area'], reverse=True)
        for i, sq in enumerate(sorted_squares[:5]):
            print(f"    {i+1}. {sq['width']}x{sq['height']} px at ({sq['x']}, {sq['y']})")
    else:
        print("  No squares detected")
    
    if rectangles:
        print(f"  Found {len(rectangles)} rectangles")
    
    if lines is not None:
        print(f"  Found {len(lines)} lines (Hough)")
    
    # Determine if Q12 candidate
    has_q12_text = len(q12_indicators) > 0
    has_multiple_squares = len(squares) >= 4 if squares else False
    is_candidate = has_q12_text or has_multiple_squares
    
    if is_candidate:
        print("\n*** Q12 CANDIDATE ***")
    
    return {
        'image': image_path.name,
        'q12_text_found': has_q12_text,
        'text_matches': [t['text'] for t in q12_indicators],
        'squares': len(squares) if squares else 0,
        'rectangles': len(rectangles) if rectangles else 0,
        'lines': len(lines) if lines is not None else 0,
        'is_candidate': is_candidate
    }


def main():
    base_path = Path(__file__).parent
    
    # Initialize EasyOCR reader
    reader = None
    if EASYOCR_AVAILABLE:
        print("Initializing EasyOCR (this may take a moment)...")
        reader = easyocr.Reader(['en'], gpu=False)
        print("EasyOCR ready\n")
    else:
        print("Using pytesseract as fallback\n")
    
    # Analyze all candidate pages
    candidates = sorted(base_path.glob("acs_pdf_page*.png"))
    
    if not candidates:
        print("No candidate images found!")
        return
    
    print(f"Found {len(candidates)} candidate pages to analyze")
    
    results = []
    for candidate in candidates:
        result = analyze_page(candidate, reader)
        results.append(result)
    
    # Summary
    print(f"\n{'='*60}")
    print("SUMMARY - Q12 CANDIDATES")
    print(f"{'='*60}")
    
    candidates_found = [r for r in results if r['is_candidate']]
    if candidates_found:
        print(f"\nFound {len(candidates_found)} Q12 candidates:")
        for r in candidates_found:
            print(f"  - {r['image']}: {r['squares']} squares, text matches: {r['text_matches']}")
    else:
        print("\nNo Q12 candidates found.")
        print("Top candidates by square count:")
        sorted_results = sorted(results, key=lambda x: x['squares'], reverse=True)
        for r in sorted_results[:3]:
            print(f"  - {r['image']}: {r['squares']} squares, {r['lines']} lines")
    
    # Save results
    output_file = base_path / "easyocr_analysis_results.json"
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to: {output_file}")


if __name__ == "__main__":
    main()
