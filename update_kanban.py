#!/usr/bin/env python3
import sys
import re

path = "ATOM-SG Pilot/01-Projects/KANBAN.md"
with open(path, 'r') as f:
    lines = f.readlines()

# Find DONE section
in_done = False
done_start = None
for i, line in enumerate(lines):
    if line.strip() == '## 🟢 DONE':
        in_done = True
        done_start = i
        break

if done_start is None:
    print("DONE section not found")
    sys.exit(1)

# Find the table start (two lines after header)
table_start = done_start + 2  # skip blank line and header line? Actually need to scan
for i in range(done_start, len(lines)):
    if lines[i].strip().startswith('| # |'):
        table_start = i
        break

# Find the line after the table (empty line)
table_end = table_start
while table_end < len(lines) and (lines[table_end].strip().startswith('|') or lines[table_end].strip().startswith('|---')):
    table_end += 1
# include the empty line after table
if table_end < len(lines) and lines[table_end].strip() == '':
    table_end += 1

print(f"Replacing lines {table_start+1} to {table_end}")

# New table rows
new_rows = [
    "| # | Task | Owner | Completed | Notes |\n",
    "|---|------|-------|-----------|-------|\n",
    "| T1 | Build baseline problem pack (20–25 geometry items) | GeoBot | 2026‑04‑13 10:30 SGT | 25 geometry problems created in `02‑Geometry/problems/`; mapping plan in `Problem‑Pack‑Plan.md` |\n",
    "| T2 | Map items → geometry sub-pathways + equation shadows | GeoBot | 2026‑04‑13 10:30 SGT | Mapping file `Geometry-Subpathway-Mapping.md` created with sub‑pathway and equation shadow mapping |\n"
]

lines[table_start:table_end] = new_rows

with open(path, 'w') as f:
    f.writelines(lines)
print("Updated DONE table.")