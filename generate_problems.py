#!/usr/bin/env python3
"""
Generate 25 geometry problem files based on Problem-Pack-Plan.md
"""
import os
import re

plan_path = "ATOM-SG Pilot/02-Geometry/Problem-Pack-Plan.md"
output_dir = "ATOM-SG Pilot/02-Geometry/problems"
template = """---
problem: {problem}
subpathway: {subpathway}
shadow: {shadow}
notes: {notes}
---
"""

# Mapping from ID to problem statement (simplified)
problem_statements = {
    "G001": "Measure the angles ∠A, ∠B, and ∠C in the diagram using a protractor.",
    "G002": "Two angles on a straight line are given. If one angle is 75°, find the other angle.",
    "G003": "Three angles meet at a point. Two angles are 120° and 85°. Find the third angle.",
    "G004": "In the diagram, two straight lines intersect. If one angle is 40°, find the other three angles.",
    "G005": "In triangle ABC, ∠A = 50° and ∠B = 70°. Find ∠C.",
    "G006": "Mark all pairs of perpendicular lines and parallel lines in the diagram.",
    "G007": "∠A and ∠B are on a straight line. ∠B and ∠C are complementary (sum to 90°). If ∠A = 110°, find ∠C.",
    "G008": "Measure the reflex angle ∠R in the diagram (angle greater than 180°).",
    "G009": "Find the perimeter of a rectangle with length 8 cm and breadth 5 cm.",
    "G010": "A rectilinear figure consists of two rectangles joined together. Find its perimeter, given some side lengths.",
    "G011": "Find the area of an L‑shape figure formed by two rectangles.",
    "G012": "A rectangular sheet has a smaller rectangle cut out from one corner. Find the remaining area.",
    "G013": "Convert 3.5 m to cm, and 250 cm to m.",
    "G014": "Convert 2.5 m² to cm².",
    "G015": "Draw all lines of symmetry for a regular hexagon.",
    "G016": "Complete the symmetrical figure given the mirror line (vertical).",
    "G017": "Find the volume of a cuboid with length 6 cm, breadth 4 cm, height 3 cm.",
    "G018": "Find the volume of a box with dimensions 0.5 m × 30 cm × 200 mm. Give answer in cm³.",
    "G019": "Which of the following nets can be folded to form a cube?",
    "G020": "Draw the net of a cuboid with dimensions 4 cm × 2 cm × 1 cm.",
    "G021": "Classify the triangle with side lengths 5 cm, 5 cm, 5 cm.",
    "G022": "Classify the triangle with angles 45°, 45°, 90°.",
    "G023": "Identify the quadrilateral: It has two pairs of parallel sides, all sides equal, and angles are not 90°.",
    "G024": "A circle has radius 7 cm. Find its circumference (take π = 22/7).",
    "G025": "A pie chart shows a sector with angle 90°. What fraction of the whole does this sector represent?",
}

# Mapping from ID to nano-node (subpathway) and shadow (from plan, we could parse but hardcode for now)
# We'll parse the plan file
def parse_plan():
    mapping = {}
    with open(plan_path, 'r') as f:
        lines = f.readlines()
    in_section = None
    for line in lines:
        line = line.strip()
        if line.startswith('### G'):
            in_section = line.replace('### ', '').split()[0]
        if line.startswith('| G'):
            # parse table row
            cols = [c.strip() for c in line.split('|') if c.strip()]
            if len(cols) >= 5 and cols[0].startswith('G'):
                id = cols[0]
                nano = cols[1]
                shadow = cols[2]
                diff = cols[3]
                notes = cols[4] if len(cols) > 4 else ''
                mapping[id] = (nano, shadow, diff, notes)
    return mapping

def main():
    os.makedirs(output_dir, exist_ok=True)
    mapping = parse_plan()
    print(f"Parsed {len(mapping)} items")
    for id, (nano, shadow, diff, notes) in mapping.items():
        problem = problem_statements.get(id, f"Geometry problem for {nano}")
        # Clean up shadow: remove backticks if present
        shadow_clean = shadow.replace('`', '')
        notes_with_diff = f"Difficulty zone: {diff}. {notes}"
        content = template.format(
            problem=problem,
            subpathway=nano,
            shadow=shadow_clean,
            notes=notes_with_diff
        )
        filename = os.path.join(output_dir, f"{id}.md")
        with open(filename, 'w') as f:
            f.write(content)
        print(f"Created {filename}")
    print("Done.")

if __name__ == '__main__':
    main()