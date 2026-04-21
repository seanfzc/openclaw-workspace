#!/usr/bin/env python3
"""
PROJECT ATOM-SG: Primary 1 Math Exam Question Processor
Processes Singapore P1 Math exam PDFs (2020-2025) and extracts individual questions
with syllabus alignment and visual type identification.
"""

import json
import re
import sys
from pathlib import Path
from typing import List, Dict, Tuple, Optional

import pdfplumber

# Configuration
EXAM_PAPERS_ROOT = Path('/Users/zcaeth/Desktop/sg_exam_papers/Maths/P1')
OUTPUT_DIR = Path('/Users/zcaeth/.openclaw/workspace/second-brain-simple/raw/exam-questions')
YEARS = ['2020', '2021', '2022', '2023', '2024', '2025']

def load_syllabus_skills() -> List[Dict]:
    """Load syllabus skills from JSON file or build from scratch."""
    skills_path = Path('moe_skills.json')
    if skills_path.exists():
        with open(skills_path) as f:
            return json.load(f)
    
    # Fallback: generate minimal skills
    from build_syllabus import skills
    return skills

def extract_questions_from_page(page_text: str, page_num: int) -> List[Dict]:
    """
    Extract individual questions from a page of text.
    Returns list of dictionaries with question_number, text, and page.
    """
    questions = []
    
    # Common question patterns:
    # 1. "Q1. Text" or "Q1) Text"
    # 2. "1. Text" or "1) Text"
    # 3. "Question 1: Text"
    # 4. MCQs with options like "(1) 44" or "A. 44"
    
    # Split by lines
    lines = page_text.split('\n')
    
    current_q = None
    current_text = []
    in_options = False
    options = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Check for question start
        match = re.match(r'^(?:Q)?(\d+)[\.\)]\s*(.*)', line)
        if match:
            # Save previous question
            if current_q is not None:
                questions.append({
                    'question_number': current_q,
                    'text': ' '.join(current_text).strip(),
                    'options': options.copy() if in_options else [],
                    'page': page_num
                })
            
            current_q = match.group(1)
            current_text = [match.group(2)] if match.group(2) else []
            in_options = False
            options = []
            continue
        
        # Check for option patterns
        option_match = re.match(r'^\((\d+)\)\s*(.*)$', line)
        if option_match:
            in_options = True
            options.append({
                'number': option_match.group(1),
                'text': option_match.group(2)
            })
            continue
        
        # If we're inside a question, add line
        if current_q is not None:
            current_text.append(line)
    
    # Add last question
    if current_q is not None:
        questions.append({
            'question_number': current_q,
            'text': ' '.join(current_text).strip(),
            'options': options.copy() if in_options else [],
            'page': page_num
        })
    
    return questions

def identify_visual_type(question_text: str, options: List[Dict]) -> str:
    """
    Identify visual type based on question content.
    Uses keyword matching; could be enhanced with vision model.
    """
    text_lower = question_text.lower()
    
    visual_keywords = {
        'picture_graph': ['picture graph', 'graph', 'chart', 'bar'],
        'number_bond': ['number bond', 'bond', 'ten frame'],
        'analog_clock': ['clock', 'time', 'analog', 'o\'clock', 'half past'],
        'shapes': ['shape', 'circle', 'square', 'triangle', 'rectangle'],
        'money': ['coin', 'dollar', 'cent', 'money', 'currency'],
        'length': ['longer', 'shorter', 'measure', 'cm', 'centimeter'],
        'counting': ['count', 'how many', 'objects'],
        'pattern': ['pattern', 'next', 'sequence']
    }
    
    for vtype, keywords in visual_keywords.items():
        if any(keyword in text_lower for keyword in keywords):
            return vtype
    
    return 'unknown'

def map_to_syllabus_skills(question_text: str, skills: List[Dict]) -> List[str]:
    """
    Map question to syllabus skills using keyword matching.
    Returns list of skill IDs.
    """
    text_lower = question_text.lower()
    matched = []
    
    for skill in skills:
        skill_text = skill['skill'].lower()
        # Split into words, check for significant matches
        words = re.findall(r'\b\w+\b', skill_text)
        significant_words = [w for w in words if len(w) > 3]
        
        # Check if any significant word appears in question
        if any(word in text_lower for word in significant_words):
            matched.append(skill['id'])
    
    return matched[:5]  # Limit to top 5

def generate_markdown(question: Dict, pdf_name: str, skills: List[Dict]) -> str:
    """Generate markdown content for a question."""
    q_num = question['question_number']
    q_text = question['text']
    options = question['options']
    page = question['page']
    
    # Identify visual type
    visual_type = identify_visual_type(q_text, options)
    
    # Map to syllabus
    skill_ids = map_to_syllabus_skills(q_text, skills)
    primary_skill = skill_ids[0] if skill_ids else 'unknown'
    
    # Build options text
    options_text = ''
    if options:
        options_text = '\n'.join([f"{opt['number']}. {opt['text']}" for opt in options])
    
    # Build syllabus mapping
    syllabus_mapping = ''
    if skill_ids:
        syllabus_mapping = '\n'.join([f"- {sid}" for sid in skill_ids])
    
    # Construct markdown
    content = f"""---
Question_ID: {pdf_name}-Q{q_num}
Topic: {primary_skill}
Primary_Node: [Nano-Node ID]
Secondary_Node: [Dependency Node ID]
Visual_Type: {visual_type}
Context_Variables: [Key objects/nouns in the question]
Misconception_Risk: [Common P1 error for this specific logic]
Answer_Logic: [Specific rubric requirements]
---

### Original Question
{q_text}

### Options
{options_text if options_text else 'No structured options found'}

### Logical Steps
1. [Logic Step 1]
2. [Logic Step 2]

### Syllabus Mapping
{syllabus_mapping if syllabus_mapping else 'No syllabus mapping found'}

### Metadata
- **Source PDF:** {pdf_name}
- **Page:** {page}
- **Question Number:** {q_num}
- **Visual Type:** {visual_type}
- **Extracted on:** {Path(__file__).parent.name}

### Notes
*This file was automatically generated by Project ATOM-SG. Fill in [bracketed] fields as needed.*

---
**Education Transformation Potential:**
- **Game-Based Learning Idea:** [How this question could become a learning game]
- **Age Adaptation (6yo):** [Simplified version]
- **Age Adaptation (11yo):** [More complex version]
- **Critical Thinking Skill:** [Which cognitive skill is exercised]
- **Future Skill Connection:** [Connection to 2030+ skills]
"""
    
    return content

def process_pdf(pdf_path: Path, skills: List[Dict]) -> int:
    """
    Process a single PDF file, extract questions, and save markdown files.
    Returns number of questions processed.
    """
    print(f"  Processing: {pdf_path.name}")
    
    questions_processed = 0
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages, 1):
                text = page.extract_text()
                if not text:
                    continue
                
                # Extract questions from page
                questions = extract_questions_from_page(text, page_num)
                
                for q in questions:
                    # Generate markdown
                    md_content = generate_markdown(q, pdf_path.stem, skills)
                    
                    # Create filename
                    filename = f"{pdf_path.stem}_Q{q['question_number']}.md"
                    filepath = OUTPUT_DIR / filename
                    
                    # Save file
                    filepath.write_text(md_content)
                    questions_processed += 1
                    
                    # Limit for testing (remove for full processing)
                    if questions_processed >= 10:
                        print(f"    Extracted 10 questions (sample limit)")
                        return questions_processed
        
        print(f"    Extracted {questions_processed} questions")
        
    except Exception as e:
        print(f"    Error processing {pdf_path.name}: {e}")
    
    return questions_processed

def main():
    """Main processing pipeline."""
    print("=== PROJECT ATOM-SG: P1 Math Exam Question Processor ===")
    print(f"Searching for PDFs in {EXAM_PAPERS_ROOT}")
    
    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Output directory: {OUTPUT_DIR.absolute()}")
    
    # Load syllabus skills
    print("\nLoading syllabus skills...")
    skills = load_syllabus_skills()
    print(f"Loaded {len(skills)} syllabus skills")
    
    # Find PDF files (2020-2025)
    pdf_files = []
    for year in YEARS:
        year_path = EXAM_PAPERS_ROOT / year
        if year_path.exists():
            # Look in all subdirectories for PDFs
            for pdf in year_path.rglob('*.pdf'):
                pdf_files.append(pdf)
    
    print(f"\nFound {len(pdf_files)} PDF files")
    
    if not pdf_files:
        print("No PDF files found. Exiting.")
        return
    
    # Process each PDF
    total_questions = 0
    processed_pdfs = 0
    
    # Process only first PDF for testing
    for pdf_path in pdf_files[:1]:
        print(f"\n[{processed_pdfs + 1}/{len(pdf_files[:3])}]")
        questions = process_pdf(pdf_path, skills)
        total_questions += questions
        processed_pdfs += 1
        
        # If we hit sample limit, break
        if total_questions >= 10:
            print("\nReached sample limit of 10 questions for review.")
            break
    
    print(f"\n=== PROCESSING COMPLETE ===")
    print(f"Processed {processed_pdfs} PDF files")
    print(f"Extracted {total_questions} questions")
    print(f"Output directory: {OUTPUT_DIR.absolute()}")
    print("\nNext steps:")
    print("1. Review extracted questions in output directory")
    print("2. Fill in bracketed fields (Primary_Node, Secondary_Node, etc.)")
    print("3. Ingest into second brain: `/second-brain-ingest`")
    print("4. Design game-based learning activities based on question patterns")

if __name__ == '__main__':
    main()