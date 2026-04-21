#!/usr/bin/env python3
"""
Extract text from PDF using PyMuPDF (often better for difficult PDFs).
"""

import fitz  # PyMuPDF
import re
from pathlib import Path

def extract_text_pymupdf(pdf_path, start_page=1, end_page=10):
    """Extract text using PyMuPDF."""
    text_by_page = []
    
    try:
        doc = fitz.open(pdf_path)
        
        for page_num in range(start_page - 1, min(end_page, len(doc))):
            page = doc[page_num]
            
            # Method 1: Get text using PyMuPDF's text extraction
            text = page.get_text()
            
            # Method 2: Get text with different parameters (sometimes works better)
            if not text or len(text.strip()) < 50:
                text = page.get_text("text")
            
            # Method 3: Get text with blocks
            if not text or len(text.strip()) < 50:
                blocks = page.get_text("blocks")
                text = "\n".join([block[4] for block in blocks if block[4]])
            
            if text:
                lines = [line.strip() for line in text.split('\n') if line.strip()]
                text_by_page.append({
                    'page': page_num + 1,
                    'lines': lines,
                    'line_count': len(lines),
                    'text': text
                })
            else:
                text_by_page.append({
                    'page': page_num + 1,
                    'lines': [],
                    'line_count': 0,
                    'text': ''
                })
        
        doc.close()
        
    except Exception as e:
        print(f"Error with PyMuPDF: {e}")
    
    return text_by_page

def find_questions_in_text(text_data):
    """Find potential questions in extracted text."""
    questions = []
    
    for page_data in text_data:
        if not page_data['lines']:
            continue
        
        lines = page_data['lines']
        current_question = []
        in_question = False
        question_num = 0
        
        for line in lines:
            # Check for question number patterns
            question_start_patterns = [
                r'^\d+[\.\)]\s',  # "1. ", "2) "
                r'^\(\d+\)\s',    # "(1) ", "(2) "
                r'^[A-D][\.\)]\s', # "A. ", "B) "
                r'^Q\d+[\.\)]?\s', # "Q1. ", "Q2) "
                r'^Question\s+\d+', # "Question 1"
            ]
            
            is_question_start = any(re.match(pattern, line) for pattern in question_start_patterns)
            
            if is_question_start:
                if current_question and in_question:
                    questions.append({
                        'page': page_data['page'],
                        'number': question_num,
                        'text': '\n'.join(current_question),
                        'lines': len(current_question)
                    })
                    current_question = []
                
                # Extract question number
                match = re.match(r'(\d+)', line.replace('(', '').replace(')', '').replace('.', ''))
                if match:
                    question_num = int(match.group(1))
                
                in_question = True
                current_question.append(line)
            elif in_question:
                # Continue question until we hit certain patterns
                if re.match(r'^\s*$', line) and len(current_question) > 3:
                    # End on blank line if we have content
                    questions.append({
                        'page': page_data['page'],
                        'number': question_num,
                        'text': '\n'.join(current_question),
                        'lines': len(current_question)
                    })
                    current_question = []
                    in_question = False
                elif len(current_question) > 15:  # Arbitrary limit
                    questions.append({
                        'page': page_data['page'],
                        'number': question_num,
                        'text': '\n'.join(current_question),
                        'lines': len(current_question)
                    })
                    current_question = []
                    in_question = False
                else:
                    current_question.append(line)
        
        # Catch any remaining question
        if current_question and in_question:
            questions.append({
                'page': page_data['page'],
                'number': question_num,
                'text': '\n'.join(current_question),
                'lines': len(current_question)
            })
    
    return questions

def main():
    pdf_path = Path('/Users/zcaeth/Desktop/sg_exam_papers/Maths/P6/2025/Other/2025 P6 Maths Weighted Assessment 1 Rosyth.pdf')
    
    if not pdf_path.exists():
        print(f"PDF not found: {pdf_path}")
        return
    
    print(f"Extracting from: {pdf_path.name}")
    print("=" * 80)
    
    # Extract text with PyMuPDF
    print("\nUsing PyMuPDF for text extraction...")
    text_data = extract_text_pymupdf(pdf_path, start_page=1, end_page=10)
    
    # Show page statistics
    total_lines = sum(page['line_count'] for page in text_data)
    print(f"\nExtracted {total_lines} total lines from {len(text_data)} pages")
    
    for page in text_data:
        if page['line_count'] > 0:
            print(f"Page {page['page']}: {page['line_count']} lines")
            if page['line_count'] > 5:
                print("  Sample:")
                for line in page['lines'][:5]:
                    print(f"    {line[:80]}")
    
    # Find questions
    print("\n" + "="*80)
    print("SEARCHING FOR QUESTIONS...")
    print("="*80)
    
    questions = find_questions_in_text(text_data)
    
    print(f"\nFound {len(questions)} potential questions")
    
    # Show questions with Algebra/Ratio analysis
    algebra_count = 0
    ratio_count = 0
    
    for i, q in enumerate(questions[:20], 1):
        print(f"\n{'='*60}")
        print(f"POTENTIAL QUESTION {i} (Page {q['page']}, Q{q.get('number', '?')}):")
        print(f"{'='*60}")
        
        # Show first 10 lines or full question if shorter
        lines_to_show = min(10, len(q['text'].split('\n')))
        question_lines = q['text'].split('\n')[:lines_to_show]
        
        for j, line in enumerate(question_lines, 1):
            print(f"{j:3}: {line[:100]}")
        
        text_lines = q['text'].split('\n')
        if len(text_lines) > lines_to_show:
            more_lines = len(text_lines) - lines_to_show
            print(f"     ... [{more_lines} more lines]")
        
        # Analyze content
        text_lower = q['text'].lower()
        
        # Algebra indicators
        algebra_indicators = []
        if 'x' in text_lower and ('=' in text_lower or 'find' in text_lower):
            algebra_indicators.append('variable x')
        if 'y' in text_lower and ('=' in text_lower or 'find' in text_lower):
            algebra_indicators.append('variable y')
        if 'algebra' in text_lower:
            algebra_indicators.append('algebra keyword')
        if 'expression' in text_lower:
            algebra_indicators.append('expression')
        if 'equation' in text_lower:
            algebra_indicators.append('equation')
        if 'solve' in text_lower:
            algebra_indicators.append('solve')
        
        # Ratio indicators
        ratio_indicators = []
        if ':' in text_lower and ('ratio' in text_lower or 'share' in text_lower):
            ratio_indicators.append('colon notation')
        if 'ratio' in text_lower:
            ratio_indicators.append('ratio keyword')
        if 'share' in text_lower and ('ratio' in text_lower or ':' in text_lower):
            ratio_indicators.append('share in ratio')
        if 'proportion' in text_lower:
            ratio_indicators.append('proportion')
        
        if algebra_indicators:
            print(f"\n  ALGEBRA INDICATORS: {', '.join(algebra_indicators)}")
            algebra_count += 1
        
        if ratio_indicators:
            print(f"\n  RATIO INDICATORS: {', '.join(ratio_indicators)}")
            ratio_count += 1
        
        if not algebra_indicators and not ratio_indicators:
            print("\n  No clear Algebra/Ratio indicators")
    
    print(f"\n{'='*80}")
    print(f"SUMMARY: {algebra_count} Algebra questions, {ratio_count} Ratio questions found")
    print(f"Total questions extracted: {len(questions)}")

if __name__ == "__main__":
    main()