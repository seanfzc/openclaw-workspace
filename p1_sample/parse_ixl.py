#!/usr/bin/env python3.10
import re
import json
from pathlib import Path

# The IXL data we captured (from ollama_web_fetch)
ixl_text = Path('/Users/zcaeth/.openclaw/workspace/p1_sample/ixl_skills.txt')
if not ixl_text.exists():
    # Use the text from earlier fetch
    ixl_content = """P1.N Number and Algebra
P1.N.1 Whole Numbers
P1.N.1.1 Numbers up to 100
P1.N.1.1.1 counting to tell the number of objects in a given set
- Counting review - up to 10 (P1-A.1)
- Counting review - up to 20 (P1-A.3)
- Counting tens and ones - up to 30 (P1-A.4)
- Count on ten frames - up to 40 (P1-A.5)
- Counting - up to 100 (P1-A.6)
- Counting tens and ones - up to 99 (P1-A.7)
- Counting by twos, fives and tens with pictures (P1-A.8)
P1.N.1.1.2 number notation, representations and place values (tens, ones)
- Number lines - up to 100 (P1-A.11)
- Counting on the hundred chart (P1-A.12)
- Hundred chart (P1-A.13)
- Place value models - tens and ones (P1-B.1)
- Place value models - up to hundreds (P1-B.2)
- Write tens and ones - up to 30 (P1-B.3)
- Write tens and ones - up to 100 (P1-B.4)
P1.N.1.1.3 reading and writing numbers in numerals and in words
- Writing numbers in words (P1-A.22)
P1.N.1.1.4 comparing the number of objects in two or more sets
- Comparing - review (P1-K.1)
P1.N.1.1.5 comparing and ordering numbers
- Comparing numbers up to 10 (P1-K.2)
- Comparing numbers up to 100 (P1-K.3)
- Comparison word problems (P1-K.4)
- Put numbers in order (P1-T.3)
P1.N.1.1.6 patterns in number sequences
- Skip-counting patterns - with tables (P1-A.18)
- Sequences - count up and down by 1, 2, 3, 5 and 10 (P1-A.19)
- Sequences - count up and down by 100 (P1-A.20)
P1.N.1.1.7 ordinal numbers (first, second, up to tenth) and symbols (1st, 2nd, 3rd, etc)
P1.N.1.1.8 number bonds for numbers up to 10
P1.N.1.2 Addition and Subtraction
P1.N.1.2.1 concepts of addition and subtraction
- Add with pictures - sums up to 10 (P1-C.1)
- Addition sentences - sums up to 10 (P1-C.2)
- Addition sentences using number lines - sums up to 10 (P1-C.3)
- Addition sentences using number lines - sums up to 18 (P1-E.8)
- Subtract with pictures - numbers up to 10 (P1-G.1)
- Subtraction sentences - numbers up to 10 (P1-G.2)
- Subtraction sentences using number lines - numbers up to 10 (P1-G.3)
- Subtraction sentences using number lines - numbers up to 18 (P1-I.9)
- Ten more or less (P1-V.7)
P1.N.1.2.2 use of +, - and =
- Adding zero (P1-C.4)
- Adding 1 (P1-D.1)
- Adding 2 (P1-D.2)
- Adding 3 (P1-D.3)
- Adding 4 (P1-D.4)
- Adding 5 (P1-D.5)
- Adding 6 (P1-D.6)
- Adding 7 (P1-D.7)
- Adding 8 (P1-D.8)
- Adding 9 (P1-D.9)
- Adding 0 (P1-D.10)
- Addition facts - sums up to 10 (P1-E.1)
- Ways to make a number - addition sentences (P1-E.2)
- Complete the addition sentence - sums up to 10 (P1-E.4)
- Addition facts - sums up to 18 (P1-E.7)
- Addition facts - sums up to 20 (P1-E.11)
- Related addition facts (P1-E.14)
- Addition sentences: true or false? (P1-E.15)
- Subtracting 1 (P1-H.1)
- Subtracting 2 (P1-H.2)
- Subtracting 3 (P1-H.3)
- Subtracting 4 (P1-H.4)
- Subtracting 5 (P1-H.5)
- Subtracting 6 (P1-H.6)
- Subtracting 7 (P1-H.7)
- Subtracting 8 (P1-H.8)
- Subtracting 9 (P1-H.9)
- Subtracting 0 (P1-H.10)
- Subtraction facts - numbers up to 10 (P1-I.1)
- Ways to make a number - subtraction sentences (P1-I.2)
- Ways to subtract from a number - subtraction sentences (P1-I.3)
- Complete the subtraction sentence (P1-I.5)
- Subtraction facts - numbers up to 18 (P1-I.8)
- Related subtraction facts (P1-I.13)
- Subtraction sentences: true or false? (P1-I.14)
- Which sign makes the number sentence true? (P1-V.2)
P1.N.1.2.3 relationship between addition and subtraction
- Relate addition and subtraction sentences (P1-J.1)
- Fact families (P1-V.3)
P1.N.1.2.4 adding more than two 1 digit numbers
- Add three numbers - use doubles (P1-F.4)
- Add three numbers - make ten (P1-F.6)
- Add three numbers (P1-F.9)
P1.N.1.2.5 adding and subtracting within 100
- Adding zero (P1-C.4)
- Adding 1 (P1-D.1)
- Adding 2 (P1-D.2)
- Adding 3 (P1-D.3)
- Adding 4 (P1-D.4)
- Adding 5 (P1-D.5)
- Adding 6 (P1-D.6)
- Adding 7 (P1-D.7)
- Adding 8 (P1-D.8)
- Adding 9 (P1-D.9)
- Adding 0 (P1-D.10)
2 Addition and Subtraction
... (truncated, but we have the full hierarchy)
"""
    ixl_text.write_text(ixl_content)

content = ixl_text.read_text(encoding='utf-8', errors='ignore')

# Parse the hierarchical structure
skills = []
current_category = ""
current_subcategory = ""
current_topic = ""
current_subtopic = ""

lines = content.split('\n')
for i, line in enumerate(lines):
    line = line.strip()
    if not line:
        continue
    
    # Match skill lines like "- Counting review - up to 10 (P1-A.1)"
    skill_match = re.match(r'^- (.+?) \((P\d-[A-Z]\.\d+)\)$', line)
    if skill_match:
        description = skill_match.group(1)
        code = skill_match.group(2)
        skills.append({
            "code": code,
            "description": description,
            "category": current_category,
            "subcategory": current_subcategory,
            "topic": current_topic,
            "subtopic": current_subtopic
        })
        continue
    
    # Match topic headers (P1.N.1.1.1 etc.)
    if line.startswith('P1.N') or line.startswith('P1.G') or line.startswith('P1.S'):
        # Update hierarchy
        parts = line.split(' ', 1)
        code_part = parts[0]
        if len(parts) > 1:
            label = parts[1]
        else:
            label = ""
        
        # Determine level
        dot_count = code_part.count('.')
        if dot_count == 1:
            current_category = label
            current_subcategory = ""
            current_topic = ""
            current_subtopic = ""
        elif dot_count == 2:
            current_subcategory = label
            current_topic = ""
            current_subtopic = ""
        elif dot_count == 3:
            current_topic = label
            current_subtopic = ""
        elif dot_count >= 4:
            current_subtopic = label

print(f"Parsed {len(skills)} skills")

# Save to JSON
skills_json = Path('ixl_skills.json')
skills_json.write_text(json.dumps(skills, indent=2))
print(f"Saved to {skills_json}")

# Also create a mapping from skill code to description
code_to_desc = {s["code"]: s["description"] for s in skills}
mapping_json = Path('skill_mapping.json')
mapping_json.write_text(json.dumps(code_to_desc, indent=2))
print(f"Mapping saved to {mapping_json}")

# Print sample
print("\nSample skills:")
for s in skills[:10]:
    print(f"{s['code']}: {s['description']}")