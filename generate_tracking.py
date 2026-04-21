#!/usr/bin/env python3
import re

# Template header
header = """# P0-6 Visual-Text Mismatches Tracking Template

**Created:** 2026-04-16 14:35 GMT+8
**For:** Manual review of 25 geometry problems (G001-G025)
**Based on:** `P0-6_Visual-Text-Mismatches-Review.md`

---

## 📝 Tracking Spreadsheet

| Problem ID | Subpathway | Issue Type | Severity | Description | Text Correction | Diagram Update | Priority | Notes |
|------------|------------|------------|----------|-------------|-----------------|----------------|----------|-------|
"""

# Data from our review
issues = [
    ("G001", "Identify and measure angles using a protractor", "", "", "", "", "", "", ""),
    ("G002", "Use angle properties to find unknown angles (angles on straight line)", "Proportional Error", "🟡 P1", "Angle labeled 75° but visually may appear different (Ivy finding #5)", "None", "Ensure drawn angle matches 75° within ±2°", "Medium", "Quick win"),
    ("G003", "Use angle properties to find unknown angles (angles around a point)", "", "", "", "", "", "", ""),
    ("G004", "Use angle properties to find unknown angles (vertically opposite angles)", "", "", "", "", "", "", ""),
    ("G005", "Apply angle sum of triangle (180°) to find missing angles", "Proportional Error", "🟡 P1", "70° angle may not appear visually larger than 50° (Ivy finding #2)", "None", "Make 70° angle clearly larger than 50°", "Medium", "Quick win"),
    ("G006", "Identify perpendicular and parallel lines in diagrams", "", "", "", "", "", "", ""),
    ("G007", "Combined angle properties (multi‑step)", "Proportional Error", "🟡 P1", "Angle labeled 110° but visually may appear different", "None", "Ensure drawn angle matches label", "Low", ""),
    ("G008", "Measure reflex angles (protractor)", "", "", "", "", "", "", ""),
    ("G009", "Calculate perimeter of rectilinear figures", "", "", "", "", "", "", ""),
    ("G010", "Calculate perimeter of rectilinear figures with missing lengths", "Shape Mismatch", "🔴 P0", "Diagram shows half-circle attached to middle, text implies quarter-circle (UX test)", "Clarify shape description", "Update diagram: quarter-circle (90°) attached to corner", "High", "CRITICAL - blocks learning"),
    ("G011", "Calculate area of composite rectangular figures", "", "", "", "", "", "", ""),
    ("G012", "Calculate area of composite rectangular figures with missing sections", "", "", "", "", "", "", ""),
    ("G013", "Convert between units of measurement (length)", "", "", "", "", "", "", ""),
    ("G014", "Convert between units of measurement (area)", "", "", "", "", "", "", ""),
    ("G015", "Identify line(s) of symmetry in 2D shapes", "", "", "", "", "", "", ""),
    ("G016", "Complete symmetrical figures given mirror line", "", "", "", "", "", ""),
    ("G017", "Calculate volume of cubes and cuboids", "", "", "", "", "", "", ""),
    ("G018", "Calculate volume of cubes and cuboids with unit conversion", "Label Clarity", "🔴 P0", "Missing unit labels: diagram shows 0.5, 30, 200 without cm/m/mm", "None", "Add unit labels: '0.5 m', '30 cm', '200 mm'", "High", "Quick win"),
    ("G019", "Visualize nets of cubes/cuboids and identify 3D shapes from nets", "", "", "", "", "", "", ""),
    ("G020", "Visualize nets of cubes/cuboids (draw net given 3D shape)", "", "", "", "", "", "", ""),
    ("G021", "Classify triangles by sides (equilateral, isosceles, scalene)", "", "", "", "", "", "", ""),
    ("G022", "Classify triangles by angles (acute, right, obtuse)", "Missing Measurements", "🟡 P1", "Right angle symbol missing on 90° corner", "None", "Add right angle symbol (square in corner)", "Medium", ""),
    ("G023", "Classify quadrilaterals (square, rectangle, parallelogram, rhombus, trapezium)", "", "", "", "", "", "", ""),
    ("G024", "Calculate circumference/area of circle using π", "Label Clarity", "🟡 P1", "Radius label '7' may be ambiguous (radius vs diameter)", "None", "Add 'r = 7 cm' with arrow", "Medium", ""),
    ("G025", "Interpret pie charts as fractions of a circle", "Proportional Error", "🔴 P0", "Sector labeled 90° but visually larger; sectors may not sum to 100% (Ivy findings #3, #11)", "Ensure text matches diagram", "Adjust sector to exactly 90°; verify total 360°", "High", "CRITICAL - visual misrepresentation"),
]

# Generate table rows
rows = []
for issue in issues:
    row = f"| {issue[0]} | {issue[1]} | {issue[2]} | {issue[3]} | {issue[4]} | {issue[5]} | {issue[6]} | {issue[7]} | {issue[8]} |"
    rows.append(row)

table = "\n".join(rows)

# Rest of template
footer = """

---

## 🎯 Issue Types (Use Exactly)

- Shape Mismatch
- Quantity Consistency
- Proportional Error
- Label Clarity
- Before-After Arrows
- Bar Model Error
- Text Contradiction
- Missing Measurements
- Rendering Quality

---

## 🚨 Severity Codes

- 🔴 P0 - Blocks learning, causes disengagement (CRITICAL)
- 🟡 P1 - Annoying but workable (MEDIUM)
- 🟢 P2 - Minor, can defer (LOW)

---

## 🔍 Review Checklist Per Problem

### A. Shape Consistency
- [ ] Diagram shape matches question description
- [ ] Example: Question says "circle" → Diagram is circular (not rectangular)
- [ ] Example: Question says "triangle" → Diagram is triangular (3 sides)

### B. Quantity Consistency
- [ ] All measurements in question appear in diagram
- [ ] No extra measurements in diagram not mentioned in question
- [ ] No missing measurements mentioned in question

### C. Proportional Accuracy
- [ ] Angles visually proportional to their values
- [ ] Side lengths visually proportional to their ratios

### D. Label Clarity
- [ ] All geometric elements are labeled (sides, angles, vertices)
- [ ] Labels are readable and not obscured
- [ ] Font size is appropriate for 11-year-olds

### E. Before-After Arrows (if applicable)
- [ ] Arrows show what changed
- [ ] Arrow direction is clear
- [ ] Arrows don't conflict with question description
- [ ] Quantities on arrows match question text

### F. Bar Models (if applicable)
- [ ] Bar segments are clearly labeled (e.g., "1/2", "3/4")
- [ ] Total is clearly shown
- [ ] Fractions are visually represented
- [ ] Colors are consistent with question (if colors mentioned)

### G. Text-Diagram Correspondence
- [ ] Question text describes diagram accurately
- [ ] No contradictions between text and diagram
- [ ] Diagram doesn't show elements not mentioned in question
- [ ] Diagram shows elements that contradict question text

### H. Rendering Quality
- [ ] Lines are crisp and clear (not blurry or pixelated)
- [ ] Colors have good contrast
- [ ] Font is legible
- [ ] Diagram fits within problem card layout

---

## 📊 Quick Wins Priority

1. **Add explicit side labels** to geometry problems (P0)
2. **Fix obvious proportion errors** (P0)
3. **Add arrow labels** for before-after problems (P0)

**Time estimates:**
- Side labels: 5-10 min per problem
- Proportion errors: 15 min per fix
- Arrow labels: 10 min per fix

---

**Last Updated:** 2026-04-16 15:45 GMT+8
**Status:** Review completed, 8 issues identified (3 P0, 4 P1, 1 P2)
"""

output = header + table + footer

with open("P0-6_TRACKING_COMPLETED.md", "w") as f:
    f.write(output)

print("Generated P0-6_TRACKING_COMPLETED.md")