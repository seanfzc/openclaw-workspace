#!/usr/bin/env python3
"""
Analyze Q12 image to extract square arrangement and measurements
"""

from PIL import Image
import numpy as np
from pathlib import Path

def analyze_image(image_path):
    """Analyze image to find Q12 diagram."""
    img = Image.open(image_path)
    print(f"\n{'='*60}")
    print(f"Analyzing: {image_path.name}")
    print(f"{'='*60}")
    print(f"Size: {img.size}")
    print(f"Mode: {img.mode}")
    
    # Convert to numpy array for analysis
    img_array = np.array(img)
    print(f"Array shape: {img_array.shape}")
    
    # Look for dark lines (square edges) and text regions
    # This is a simple heuristic - look for high contrast regions
    if len(img_array.shape) == 3:
        gray = np.mean(img_array, axis=2)
    else:
        gray = img_array
    
    # Find edges using gradient
    grad_x = np.abs(np.diff(gray, axis=1, append=gray[:, -1:]))
    grad_y = np.abs(np.diff(gray, axis=0, append=gray[-1:, :]))
    edges = grad_x + grad_y
    
    # Count strong edges (potential square boundaries)
    strong_edges = np.sum(edges > np.percentile(edges, 95))
    print(f"Strong edges detected: {strong_edges}")
    
    # Look for rectangular regions (potential squares)
    # This is simplified - would need more sophisticated analysis
    print(f"Edge density: {strong_edges / edges.size:.4f}")
    
    return img, img_array

def main():
    base_path = Path(__file__).parent
    
    candidates = [
        "q12_candidate_page12.png",
        "q12_candidate_page13.jpeg", 
        "q12_candidate_page14.jpeg"
    ]
    
    for candidate in candidates:
        path = base_path / candidate
        if path.exists():
            try:
                img, arr = analyze_image(path)
            except Exception as e:
                print(f"Error analyzing {candidate}: {e}")
        else:
            print(f"Not found: {candidate}")

if __name__ == "__main__":
    main()
