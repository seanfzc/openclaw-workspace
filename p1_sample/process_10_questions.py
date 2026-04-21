#!/usr/bin/env python3
"""
Process PDFs until we have 10 sample questions for review.
"""

import json
import re
from pathlib import Path
import pdfplumber

# Configuration
EXAM_PAPERS_ROOT = Path('/Users/zcaeth/Desktop/sg_exam_papers/Maths/P1')
OUTPUT_DIR = Path('/Users/zcaeth/.openclaw/workspace/second-brain-simple/raw/exam-questions')
YEARS = ['2020', '2021', '2022', '2023', '2024', '2025']

def load_skills():
    skills_path = Path('moe_skills.json')
    if skills_path.exists():
        with open(skills_path) as f:
            return json.load(f)
    from build_syllabus import skills
    return skills

def extract_questions_from_page(text, page_num):
    questions = []
    lines = text.split('\n')
    current_q = None
    current_text = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        match = re.match(r'^(?:Q)?(\d+)[\.\)]\s*(.*)', line)
        if match:
            if current_q is not None:
                questions.append({
                    'question_number': current_q,
                    'text': ' '.join(current_text).strip(),
                    'page': page_num
                })
            current_q = match.group(1)
            current_text = [match.group(2)] if match.group(2) else []
        else:
            if current_q is not None:
                current_text.append(line)
    if current_q is not None:
        questions.append({
            'question_number': current_q,
            'text': ' '.join(current_text).strip(),
            'page': page_num
        })
    return questions

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    skills = load_skills()
    print(f"Loaded {len(skills)} syllabus skills")
    
    # Find PDFs
    pdf_files = []
    for year in YEARS:
        year_path = EXAM_PAPERS_ROOT / year
        if year_path.exists():
            for pdf in year_path.rglob('*.pdf'):
                pdf_files.append(pdf)
    
    print(f"Found {len(pdf_files)} PDF files")
    
    total_questions = 0
    processed_pdfs = 0
    
    for pdf_path in pdf_files:
        processed_pdfs += 1
        print(f"\nProcessing {pdf_path.name} ({processed_pdfs}/{len(pdf_files)})")
        
        try:
            with pdfplumber.open(pdf_path) as pdf:
                for page_num, page in enumerate(pdf.pages, 1):
                    text = page.extract_text()
                    if not text:
                        continue
                    questions = extract_questions_from_page(text, page_num)
                    
                    for q in questions:
                        # Generate simple markdown
                        content = f"""---
Question_ID: {pdf_path.stem}-Q{q['question_number']}
Topic: S001
Primary_Node: [Nano-Node ID]
Secondary_Node: [Dependency Node ID]
Visual_Type: [Type]
Context_Variables: [Key objects/nouns in the question]
Misconception_Risk: [Common P1 error for this specific logic]
Answer_Logic: [Specific rubric requirements]
---

### Original Question
{q['text']}

### Logical Steps
1. [Logic Step 1]
2. [Logic Step 2]

### Metadata
- Source: {pdf_path.name}
- Page: {page_num}
"""
                        filename = f"{pdf_path.stem}_Q{q['question_number']}.md"
                        filepath = OUTPUT_DIR / filename
                        filepath.write_text(content)
                        
                        total_questions += 1
                        print(f"  Saved question {total_questions}: {filename}")
                        
                        if total_questions >= 10:
                            print(f"\nReached target of 10 questions.")
                            print(f"Output directory: {OUTPUT_DIR}")
                            return
        except Exception as e:
            print(f"  Error: {e}")
            continue
    
    print(f"\nProcessed all PDFs. Total questions: {total_questions}")

if __name__ == '__main__':
    main()