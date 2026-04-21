#!/usr/bin/env python3
import json
import re
from pathlib import Path

# MOE Primary 1 Mathematics Syllabus - based on Sean's list and research
syllabus = {
    "Whole Numbers": {
        "Numbers to 10": [
            "Counting objects to 10",
            "Reading and writing numerals 0-10",
            "Reading and writing number words zero to ten",
            "Comparing numbers within 10",
            "Ordering numbers within 10",
            "Number bonds for numbers up to 10",
            "Ordinal numbers (first to tenth)"
        ],
        "Numbers to 20": [
            "Counting objects to 20",
            "Reading and writing numerals 11-20",
            "Reading and writing number words eleven to twenty",
            "Comparing numbers within 20",
            "Ordering numbers within 20",
            "Place value (tens and ones) for numbers 11-20"
        ],
        "Numbers to 100": [
            "Counting objects to 100",
            "Reading and writing numerals up to 100",
            "Place value (tens and ones) for numbers up to 100",
            "Comparing numbers up to 100",
            "Ordering numbers up to 100",
            "Number patterns (skip counting by 2s, 5s, 10s)"
        ]
    },
    "Addition and Subtraction": {
        "Addition within 10": [
            "Adding with pictures",
            "Adding using number bonds",
            "Addition facts (sums up to 10)",
            "Adding 0, 1, 2 to a number",
            "Adding three 1-digit numbers",
            "Addition word problems within 10"
        ],
        "Subtraction within 10": [
            "Subtracting with pictures",
            "Subtracting using number bonds",
            "Subtraction facts (within 10)",
            "Subtracting 0, 1, 2 from a number",
            "Subtraction word problems within 10"
        ],
        "Addition within 20": [
            "Addition without regrouping",
            "Addition facts (sums up to 20)",
            "Adding three 1-digit numbers (sums up to 20)",
            "Addition word problems within 20"
        ],
        "Subtraction within 20": [
            "Subtraction without regrouping",
            "Subtraction facts (within 20)",
            "Subtraction word problems within 20"
        ],
        "Addition and Subtraction within 100": [
            "Adding tens",
            "Subtracting tens",
            "Adding 2-digit and 1-digit numbers without regrouping",
            "Subtracting 1-digit from 2-digit numbers without regrouping",
            "Adding two 2-digit numbers without regrouping",
            "Subtracting two 2-digit numbers without regrouping",
            "Word problems within 100"
        ]
    },
    "Multiplication and Division": {
        "Basic Multiplication": [
            "Multiplication as repeated addition",
            "Multiplying by 2",
            "Multiplying by 5",
            "Multiplying by 10"
        ],
        "Basic Division": [
            "Division as sharing equally",
            "Division as grouping",
            "Dividing by 2",
            "Dividing by 5",
            "Dividing by 10"
        ]
    },
    "Measurement": {
        "Length": [
            "Comparing lengths (longer/shorter)",
            "Measuring length using non-standard units (e.g., paper clips)",
            "Measuring length using standard units (cm)",
            "Word problems involving length"
        ],
        "Time": [
            "Telling time to the hour",
            "Telling time to the half hour",
            "Reading clock faces (analogue)",
            "Reading digital clocks",
            "Days of the week",
            "Months of the year",
            "Sequence of events (before, after, next)"
        ],
        "Money": [
            "Recognising coins and notes (Singapore currency)",
            "Counting money in cents up to $1",
            "Counting money in dollars up to $10",
            "Comparing amounts of money",
            "Simple addition and subtraction with money",
            "Word problems involving money"
        ]
    },
    "Geometry": {
        "Shapes": [
            "Identifying 2D shapes (square, rectangle, circle, triangle)",
            "Describing 2D shapes (sides, corners)",
            "Identifying 3D shapes (cube, cuboid, sphere, cone)",
            "Describing 3D shapes (faces, edges, vertices)",
            "Composing shapes (making pictures with shapes)",
            "Patterns with shapes"
        ]
    },
    "Data Analysis": {
        "Picture Graphs": [
            "Reading picture graphs",
            "Making picture graphs",
            "Interpreting picture graphs (most, least, how many more)",
            "Simple questions about picture graphs"
        ],
        "Tally Charts": [
            "Reading tally marks",
            "Making tally charts",
            "Interpreting tally charts"
        ]
    }
}

# Flatten into skills with IDs
skills = []
skill_id = 1
for category, subcategories in syllabus.items():
    for subcategory, skill_list in subcategories.items():
        for skill in skill_list:
            skills.append({
                "id": f"S{skill_id:03d}",
                "skill": skill,
                "category": category,
                "subcategory": subcategory,
                "full_path": f"{category} > {subcategory} > {skill}"
            })
            skill_id += 1

print(f"Created {len(skills)} syllabus skills")

# Save to JSON
skills_path = Path('moe_syllabus_skills.json')
skills_path.write_text(json.dumps(skills, indent=2))
print(f"Saved syllabus skills to {skills_path}")

# Create a mapping for keyword matching
keyword_to_skill = {}
for skill in skills:
    # Generate keywords from skill text
    text = skill["skill"].lower()
    words = re.findall(r'\b\w+\b', text)
    for word in words:
        if len(word) > 3:  # Ignore short words
            if word not in keyword_to_skill:
                keyword_to_skill[word] = []
            keyword_to_skill[word].append(skill["id"])
    
    # Also add category and subcategory keywords
    for part in [skill["category"], skill["subcategory"]]:
        part_words = re.findall(r'\b\w+\b', part.lower())
        for word in part_words:
            if len(word) > 3:
                if word not in keyword_to_skill:
                    keyword_to_skill[word] = []
                keyword_to_skill[word].append(skill["id"])

# Save keyword mapping
keyword_path = Path('keyword_to_skill.json')
keyword_path.write_text(json.dumps(keyword_to_skill, indent=2))
print(f"Saved keyword mapping to {keyword_path}")

# Sample output
print("\nSample skills:")
for skill in skills[:15]:
    print(f"{skill['id']}: {skill['skill']}")