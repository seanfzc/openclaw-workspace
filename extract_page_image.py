#!/usr/bin/env python3
"""
Extract a page from PDF as image to see content.
"""

import fitz  # PyMuPDF
from pathlib import Path
import base64

def extract_page_as_image(pdf_path, page_num=2, zoom=2):
    """Extract a PDF page as image and return base64."""
    try:
        doc = fitz.open(pdf_path)
        if page_num - 1 >= len(doc):
            print(f"Page {page_num} not available, PDF has {len(doc)} pages")
            return None
        
        page = doc[page_num - 1]
        
        # Render page to image
        mat = fitz.Matrix(zoom, zoom)  # Zoom factor for better resolution
        pix = page.get_pixmap(matrix=mat)
        
        # Convert to bytes
        img_bytes = pix.tobytes("png")
        
        # Convert to base64 for potential API use
        img_base64 = base64.b64encode(img_bytes).decode('utf-8')
        
        doc.close()
        
        # Save locally for inspection
        output_path = Path(f"/tmp/page_{page_num}.png")
        pix.save(output_path)
        print(f"Saved page {page_num} image to: {output_path}")
        print(f"Image size: {pix.width} x {pix.height}")
        print(f"Base64 size: {len(img_base64)} characters")
        
        return img_base64
        
    except Exception as e:
        print(f"Error extracting image: {e}")
        return None

def check_multiple_pages(pdf_path):
    """Check what's on first few pages."""
    try:
        doc = fitz.open(pdf_path)
        print(f"PDF has {len(doc)} pages")
        
        for i in range(min(5, len(doc))):
            page = doc[i]
            text = page.get_text()
            images = page.get_images()
            
            print(f"\nPage {i+1}:")
            print(f"  Text characters: {len(text)}")
            print(f"  Images: {len(images)}")
            
            if len(text) > 0:
                lines = [l.strip() for l in text.split('\n') if l.strip()]
                print(f"  Text lines: {len(lines)}")
                if lines:
                    print(f"  First line: {lines[0][:80]}")
            
            if images:
                print(f"  Image details:")
                for img in images[:2]:  # First 2 images
                    print(f"    - Size: {img}")
        
        doc.close()
        
    except Exception as e:
        print(f"Error checking pages: {e}")

def main():
    pdf_path = Path('/Users/zcaeth/Desktop/sg_exam_papers/Maths/P6/2025/Other/2025 P6 Maths Weighted Assessment 1 Rosyth.pdf')
    
    if not pdf_path.exists():
        print(f"PDF not found: {pdf_path}")
        return
    
    print(f"Analyzing: {pdf_path.name}")
    print("="*80)
    
    # Check what's on pages
    check_multiple_pages(pdf_path)
    
    print("\n" + "="*80)
    print("Extracting page 2 as image (likely first question page)...")
    
    # Extract page 2 as image
    img_base64 = extract_page_as_image(pdf_path, page_num=2)
    
    if img_base64:
        print(f"\nImage extracted successfully")
        print(f"To use with vision API: data:image/png;base64,{img_base64[:100]}...")
    else:
        print("Failed to extract image")

if __name__ == "__main__":
    main()