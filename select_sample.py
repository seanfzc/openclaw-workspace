#!/usr/bin/env python3
import os
import random
from pathlib import Path

# Get all PDFs
pdfs = list(Path('/Users/zcaeth/Desktop/sg_exam_papers/Maths/P1').rglob('*.pdf'))
print(f"Total PDFs: {len(pdfs)}")

# Extract metadata from filename
def parse_filename(path):
    name = path.name
    # Example: "2022 P1 Maths Review Assessment 2 Raffles Girls.pdf"
    parts = name.split()
    year = parts[0] if parts[0].isdigit() else None
    # School is usually the last word before .pdf
    school = parts[-1].replace('.pdf', '')
    # Test type: combine words after "Maths"
    try:
        maths_idx = parts.index('Maths')
        test_type = ' '.join(parts[maths_idx+1:-1])
    except:
        test_type = 'Unknown'
    return {'year': year, 'school': school, 'test_type': test_type, 'path': str(path)}

parsed = [parse_filename(p) for p in pdfs]

# Group by year
from collections import defaultdict
by_year = defaultdict(list)
for p in parsed:
    by_year[p['year']].append(p)

print("\nDistribution by year:")
for year in sorted(by_year.keys()):
    print(f"  {year}: {len(by_year[year])}")

# Group by school
by_school = defaultdict(list)
for p in parsed:
    by_school[p['school']].append(p)

print("\nTop schools by file count:")
for school in sorted(by_school.keys(), key=lambda s: len(by_school[s]), reverse=True)[:10]:
    print(f"  {school}: {len(by_school[school])}")

# Select 10 samples: 2 from each year 2021-2025 (if available)
selected = []
years = ['2021', '2022', '2023', '2024', '2025']
for year in years:
    if year in by_year:
        candidates = by_year[year]
        # Pick up to 2, trying to diversify schools
        picked = []
        schools_seen = set()
        for p in candidates:
            if p['school'] not in schools_seen:
                picked.append(p)
                schools_seen.add(p['school'])
                if len(picked) >= 2:
                    break
        # If not enough diverse schools, add more
        if len(picked) < 2:
            for p in candidates:
                if p not in picked:
                    picked.append(p)
                    if len(picked) >= 2:
                        break
        selected.extend(picked[:2])

# If still less than 10, add random ones
if len(selected) < 10:
    remaining = [p for p in parsed if p not in selected]
    random.shuffle(remaining)
    selected.extend(remaining[:10 - len(selected)])

print(f"\nSelected {len(selected)} samples:")
for i, p in enumerate(selected):
    print(f"{i+1:2}. {p['year']} {p['school']:20} {p['test_type'][:40]}...")

# Write selected paths to file
with open('/Users/zcaeth/.openclaw/workspace/selected_pdfs.txt', 'w') as f:
    for p in selected:
        f.write(p['path'] + '\n')

print(f"\nPaths saved to selected_pdfs.txt")