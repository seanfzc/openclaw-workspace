#!/usr/bin/env python3
"""
Extract questions from Rosyth P6 PDF.
"""

import pdfplumber
import re
from pathlib import Path

def extract_questions_from_pdf(pdf_path, start_page=2, end_page=10):
    """Extract potential questions from PDF pages."""
    questions = []
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page_num in range(start_page - 1, min(end_page, len(pdf.pages))):
                page = pdf.pages[page_num]
                text = page.extract_text()
                
                if not text:
                    continue
                
                # Split by potential question markers
                lines = text.split('\n')
                
                # Look for question patterns
                question_patterns = [
                    r'^\d+[\.\)]',  # "1.", "2)", etc.
                    r'^\([a-d]\)',  # MCQ options
                    r'^[A-D]\.',    # MCQ options
                    r'^\(\d+\)',    # "(1)", "(2)", etc.
                ]
                
                current_question = []
                in_question = False
                
                for line in lines:
                    line = line.strip()
                    if not line:
                        continue
                    
                    # Check if line starts a new question
                    is_question_start = any(re.match(pattern, line) for pattern in question_patterns)
                    
                    if is_question_start:
                        if current_question and in_question:
                            # Save previous question
                            questions.append({
                                'page': page_num + 1,
                                'text': '\n'.join(current_question),
                                'lines': len(current_question)
                            })
                            current_question = []
                        
                        in_question = True
                        current_question.append(line)
                    elif in_question:
                        # Continue current question
                        current_question.append(line)
                        # Check if question might be ending (MCQ options, answer line, etc.)
                        if len(current_question) > 10:  # Arbitrary limit
                            # Save and start new
                            questions.append({
                                'page': page_num + 1,
                                'text': '\n'.join(current_question),
                                'lines': len(current_question)
                            })
                            current_question = []
                            in_question = False
                
                # Save last question on page
                if current_question and in_question:
                    questions.append({
                        'page': page_num + 1,
                        'text': '\n'.join(current_question),
                        'lines': len(current_question)
                    })
    
    except Exception as e:
        print(f"Error processing PDF: {e}")
    
    return questions

def main():
    pdf_path = Path('/Users/zcaeth/Desktop/sg_exam_papers/Maths/P6/2025/Other/2025 P6 Maths Weighted Assessment 1 Rosyth.pdf')
    
    if not pdf_path.exists():
        print(f"PDF not found: {pdf_path}")
        return
    
    print(f"Extracting questions from: {pdf_path.name}")
    print("=" * 80)
    
    questions = extract_questions_from_pdf(pdf_path, start_page=2, end_page=6)
    
    print(f"Found {len(questions)} potential questions")
    print("=" * 80)
    
    for i, q in enumerate(questions[:15], 1):  # Show first 15
        print(f"\nQUESTION {i} (Page {q['page']}, {q['lines']} lines):")
        print("-" * 40)
        print(q['text'][:500])  # First 500 chars
        if len(q['text']) > 500:
            print("... [truncated]")
        
        # Analyze for Algebra/Ratio
        text_lower = q['text'].lower()
        has_algebra = any(ind in text_lower for ind in ['x', 'y', '=', 'algebra', 'expression'])
        has_ratio = any(ind in text_lower for ind in [':', 'ratio', 'share', 'proportion'])
        
        if has_algebra or has_ratio:
            print("\n  CONTENT TYPE:", end=" ")
            if has_algebra:
                print("ALGEBRA", end=" ")
            if has_ratio:
                print("RATIO", end=" ")
            print()

if __name__ == "__main__":
    main()