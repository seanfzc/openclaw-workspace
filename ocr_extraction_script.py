#!/usr/bin/env python3
"""
OCR extraction script for P6 PDFs (to be used after Tesseract installation).
"""

import fitz  # PyMuPDF
import tempfile
import os
from pathlib import Path

def check_tesseract_installation():
    """Check if Tesseract is installed."""
    try:
        import pytesseract
        # Check if tesseract command is available
        pytesseract.get_tesseract_version()
        print("✅ Tesseract is installed and accessible")
        return True
    except ImportError:
        print("❌ pytesseract not installed. Install with: pip install pytesseract")
        return False
    except Exception as e:
        print(f"❌ Tesseract error: {e}")
        print("Install Tesseract: brew install tesseract")
        return False

def extract_text_with_ocr(pdf_path, page_range=(2, 10)):
    """
    Extract text from PDF pages using OCR.
    Pages are converted to images first, then OCR applied.
    """
    if not check_tesseract_installation():
        return None
    
    try:
        import pytesseract
        from PIL import Image
    except ImportError:
        print("Required libraries not installed.")
        print("Install: pip install pytesseract Pillow")
        return None
    
    doc = fitz.open(pdf_path)
    extracted_text = {}
    
    start_page, end_page = page_range
    start_page = max(1, start_page)
    end_page = min(len(doc), end_page)
    
    print(f"Processing pages {start_page} to {end_page} of {pdf_path.name}")
    
    for page_num in range(start_page - 1, end_page):
        page = doc[page_num]
        
        # Convert page to image
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # 2x zoom for better OCR
        img_path = tempfile.mktemp(suffix='.png')
        pix.save(img_path)
        
        # Apply OCR
        try:
            text = pytesseract.image_to_string(Image.open(img_path))
            extracted_text[page_num + 1] = text
            
            # Clean up
            os.remove(img_path)
            
            # Show sample if text found
            if text.strip():
                lines = [l.strip() for l in text.split('\n') if l.strip()]
                print(f"\nPage {page_num + 1}: {len(lines)} lines extracted")
                if lines:
                    print(f"  Sample: {lines[0][:80]}")
            else:
                print(f"Page {page_num + 1}: No text detected")
                
        except Exception as e:
            print(f"Page {page_num + 1}: OCR error - {e}")
            extracted_text[page_num + 1] = ""
    
    doc.close()
    return extracted_text

def find_questions_in_ocr_text(ocr_text):
    """Find potential questions in OCR-extracted text."""
    questions = []
    
    for page_num, text in ocr_text.items():
        if not text.strip():
            continue
        
        lines = text.split('\n')
        current_question = []
        in_question = False
        
        for line in lines:
            line = line.strip()
            if not line:
                if current_question and in_question:
                    questions.append({
                        'page': page_num,
                        'text': '\n'.join(current_question),
                        'lines': len(current_question)
                    })
                    current_question = []
                    in_question = False
                continue
            
            # Check for question patterns
            import re
            question_patterns = [
                r'^\d+[\.\)]\s*',  # "1. ", "2) "
                r'^\(\d+\)\s*',    # "(1) ", "(2) "
                r'^[A-D][\.\)]\s*', # "A. ", "B) "
                r'^Q\d+[\.\)]?\s*', # "Q1. ", "Q2) "
                r'^Question\s+\d+', # "Question 1"
            ]
            
            is_question = any(re.match(pattern, line) for pattern in question_patterns)
            
            if is_question:
                if current_question and in_question:
                    questions.append({
                        'page': page_num,
                        'text': '\n'.join(current_question),
                        'lines': len(current_question)
                    })
                current_question = [line]
                in_question = True
            elif in_question:
                current_question.append(line)
                # Limit question length
                if len(current_question) > 15:
                    questions.append({
                        'page': page_num,
                        'text': '\n'.join(current_question),
                        'lines': len(current_question)
                    })
                    current_question = []
                    in_question = False
        
        # Catch last question
        if current_question and in_question:
            questions.append({
                'page': page_num,
                'text': '\n'.join(current_question),
                'lines': len(current_question)
            })
    
    return questions

def main():
    """Main function to demonstrate OCR extraction."""
    pdf_path = Path('/Users/zcaeth/Desktop/sg_exam_papers/Maths/P6/2025/Other/2025 P6 Maths Weighted Assessment 1 Rosyth.pdf')
    
    if not pdf_path.exists():
        print(f"PDF not found: {pdf_path}")
        return
    
    print("="*80)
    print("P6 PDF OCR EXTRACTION SCRIPT")
    print("="*80)
    print("\nPREREQUISITES:")
    print("1. Install Tesseract: brew install tesseract")
    print("2. Install Python packages: pip install pytesseract Pillow")
    print("3. This script uses existing PyMuPDF (fitz) installation")
    print("="*80)
    
    # Check installation
    if not check_tesseract_installation():
        print("\n❌ Cannot proceed without Tesseract installation.")
        print("Please run: brew install tesseract")
        print("Then: pip install pytesseract Pillow")
        return
    
    print("\n✅ All prerequisites met. Starting OCR extraction...")
    
    # Extract text with OCR
    ocr_text = extract_text_with_ocr(pdf_path, page_range=(2, 6))
    
    if not ocr_text:
        print("No text extracted.")
        return
    
    # Find questions
    questions = find_questions_in_ocr_text(ocr_text)
    
    print(f"\n{'='*80}")
    print(f"OCR EXTRACTION RESULTS: {len(questions)} potential questions found")
    print(f"{'='*80}")
    
    for i, q in enumerate(questions[:10], 1):
        print(f"\nQUESTION {i} (Page {q['page']}):")
        print("-"*40)
        # Show first 5 lines or full question if shorter
        lines = q['text'].split('\n')
        for j, line in enumerate(lines[:8], 1):
            print(f"{j:2}: {line[:80]}")
        if len(lines) > 8:
            print(f"   ... [{len(lines) - 8} more lines]")
        
        # Check for Algebra/Ratio keywords
        text_lower = q['text'].lower()
        algebra_keywords = ['x', 'y', '=', 'algebra', 'equation', 'solve']
        ratio_keywords = [':', 'ratio', 'share', 'proportion']
        
        has_algebra = any(kw in text_lower for kw in algebra_keywords)
        has_ratio = any(kw in text_lower for kw in ratio_keywords)
        
        if has_algebra or has_ratio:
            print("  Content: ", end="")
            if has_algebra:
                print("ALGEBRA ", end="")
            if has_ratio:
                print("RATIO ", end="")
            print()
    
    # Save extracted text for review
    output_dir = Path("/Users/zcaeth/.openclaw/workspace/OCR_Results")
    output_dir.mkdir(exist_ok=True)
    
    output_file = output_dir / "rosyth_ocr_extraction.txt"
    with open(output_file, 'w') as f:
        for page_num, text in ocr_text.items():
            f.write(f"\n{'='*80}\n")
            f.write(f"PAGE {page_num}\n")
            f.write(f"{'='*80}\n")
            f.write(text)
    
    print(f"\n✅ Full OCR text saved to: {output_file}")
    print(f"Total pages processed: {len(ocr_text)}")

if __name__ == "__main__":
    main()