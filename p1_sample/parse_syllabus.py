#!/usr/bin/env python3
import json
import sys

skills = []
with open('syllabus_structure.txt', 'r') as f:
    lines = f.read().strip().split('\n')
    
for i, line in enumerate(lines):
    if not line.strip():
        continue
    parts = line.split(' > ')
    if len(parts) != 3:
        print(f"Skipping malformed line: {line}")
        continue
    
    category, subcategory, skill = parts
    skills.append({
        'id': f'S{i+1:03d}',
        'skill': skill.strip(),
        'category': category.strip(),
        'subcategory': subcategory.strip(),
        'full_path': line.strip()
    })

print(f"Parsed {len(skills)} skills")

# Save to JSON
with open('moe_syllabus_complete.json', 'w') as f:
    json.dump(skills, f, indent=2)

print("Saved to moe_syllabus_complete.json")

# Print sample
print("\nFirst 10 skills:")
for s in skills[:10]:
    print(f"{s['id']}: {s['skill']}")