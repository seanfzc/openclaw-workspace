#!/usr/bin/env python3
import pdfplumber
import re
import json
from pathlib import Path

def extract_questions_from_pdf(pdf_path):
    """Extract questions from a PDF file."""
    questions = []
    
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, 1):
            text = page.extract_text()
            if not text:
                continue
                
            # Split by question numbers (like Q1, Q2, 1., 2., etc.)
            # This is a simple heuristic; will need refinement
            lines = text.split('\n')
            
            current_question = None
            current_text = []
            
            for line in lines:
                line = line.strip()
                # Check if line starts with question pattern
                match = re.match(r'^(?:Q)?(\d+)[\.\)]?\s*(.*)', line)
                if match:
                    # Save previous question if exists
                    if current_question is not None:
                        questions.append({
                            'question_number': current_question,
                            'text': ' '.join(current_text).strip(),
                            'page': page_num
                        })
                    
                    current_question = match.group(1)
                    current_text = [match.group(2)] if match.group(2) else []
                else:
                    if current_question is not None:
                        current_text.append(line)
            
            # Add last question
            if current_question is not None:
                questions.append({
                    'question_number': current_question,
                    'text': ' '.join(current_text).strip(),
                    'page': page_num
                })
    
    return questions

def map_to_syllabus(question_text, syllabus_skills):
    """Map question text to syllabus skills using keyword matching."""
    matched_skills = []
    question_lower = question_text.lower()
    
    for skill in syllabus_skills:
        skill_text = skill['skill'].lower()
        # Simple keyword matching - could be improved
        if any(keyword in question_lower for keyword in skill_text.split() if len(keyword) > 3):
            matched_skills.append(skill['id'])
    
    return matched_skills[:3]  # Limit to top 3

def main():
    # Load syllabus skills
    skills_path = Path('moe_skills.json')
    if skills_path.exists():
        with open(skills_path) as f:
            syllabus_skills = json.load(f)
    else:
        # Fallback to built-in syllabus
        from build_syllabus import skills as syllabus_skills
    
    # Process one PDF as example
    pdf_files = list(Path('.').glob('*.pdf'))
    if not pdf_files:
        print("No PDF files found")
        return
    
    pdf_path = pdf_files[0]
    print(f"Processing {pdf_path.name}...")
    
    questions = extract_questions_from_pdf(pdf_path)
    print(f"Found {len(questions)} questions")
    
    # Create output directory
    output_dir = Path('question_extractions')
    output_dir.mkdir(exist_ok=True)
    
    for i, q in enumerate(questions[:5]):  # Limit to first 5 for testing
        # Map to syllabus
        matched_skills = map_to_syllabus(q['text'], syllabus_skills)
        
        # Generate markdown content
        content = f"""---
Question_ID: {pdf_path.stem}-Q{q['question_number']}
Topic: {matched_skills[0] if matched_skills else 'Unknown'}
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

### Syllabus Mapping
{', '.join(matched_skills) if matched_skills else 'No mapping found'}

### Notes
- Page: {q['page']}
- Question number: {q['question_number']}
- Extracted from: {pdf_path.name}
"""
        
        # Save to file
        filename = f"{pdf_path.stem}_Q{q['question_number']}.md"
        filepath = output_dir / filename
        filepath.write_text(content)
        print(f"  Saved {filename}")
    
    print(f"\nSample extraction complete. Files saved to {output_dir}/")

if __name__ == '__main__':
    main()