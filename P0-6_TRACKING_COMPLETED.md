# P0-6 Visual-Text Mismatches Tracking Template

**Created:** 2026-04-16 14:35 GMT+8
**Updated:** 2026-04-16 15:27 GMT+8
**For:** Manual review of 25 geometry problems (G001-G025)
**Based on:** `P0-6_Visual-Text-Mismatches-Review.md`
**Reviewer:** P0-6 ReviewBot
**Status:** Review completed, 11 issues identified (8 P0, 3 P1, 0 P2)

---

## 📝 Tracking Spreadsheet

| Problem ID | Subpathway | Issue Type | Severity | Description | Text Correction | Diagram Update | Priority | Notes |
|------------|------------|------------|----------|-------------|-----------------|----------------|----------|-------|
| G001 | Identify and measure angles using a protractor | Missing Angle Rays | 🔴 P0 | Diagram shows arcs but missing the two rays that form each angle, making it impossible to measure angles with a protractor (angle = intersection of two lines) | None | Add radial lines for each angle (rays from vertex) | High | CRITICAL - blocks angle measurement |
| G002 | Use angle properties to find unknown angles (angles on straight line) | Missing Angle Rays, Proportional Error | 🔴 P0 | Diagram shows arcs but missing the two rays that form each angle (angle = intersection of two lines); also angle proportion may not match 75° label | None | Add radial lines; ensure angle matches 75° | High | CRITICAL - blocks angle measurement |
| G003 | Use angle properties to find unknown angles (angles around a point) | Missing Angle Rays | 🔴 P0 | Diagram shows arcs but missing the rays that form each angle (angles around a point need radial lines) | None | Add radial lines separating each angle | High | CRITICAL - blocks angle measurement |
| G004 | Use angle properties to find unknown angles (vertically opposite angles) | - | - | No visual-text mismatch found | - | - | - | ✅ Pass |
| G005 | Apply angle sum of triangle (180°) to find missing angles | Proportional Error | 🟡 P1 | 70° angle may not appear visually larger than 50° (Ivy finding #2) | None | Make 70° angle clearly larger than 50° | Medium | Quick win |
| G006 | Identify perpendicular and parallel lines in diagrams | - | - | No visual-text mismatch found | - | - | - | ✅ Pass |
| G007 | Combined angle properties (multi‑step) | Missing Angle Rays, Proportional Error | 🔴 P0 | Diagram shows arcs but missing the two rays that form each angle; also angle proportion may not match label | None | Add radial lines; ensure angle matches label | High | CRITICAL - blocks angle measurement |
| G008 | Measure reflex angles (protractor) | Missing Angle Rays | 🔴 P0 | Diagram shows arcs and one line but missing the second ray that forms the reflex angle | None | Add second ray to complete the angle | High | CRITICAL - blocks angle measurement |
| G009 | Calculate perimeter of rectilinear figures | - | - | No visual-text mismatch found | - | - | - | ✅ Pass |
| G010 | Calculate perimeter of rectilinear figures with missing lengths | Shape Mismatch | 🔴 P0 | Diagram shows half-circle attached to middle, text implies quarter-circle (UX test) | Clarify shape description | Update diagram: quarter-circle (90°) attached to corner | High | CRITICAL - blocks learning |
| G011 | Calculate area of composite rectangular figures | - | - | No visual-text mismatch found | - | - | - | ✅ Pass |
| G012 | Calculate area of composite rectangular figures with missing sections | - | - | No visual-text mismatch found | - | - | - | ✅ Pass |
| G013 | Convert between units of measurement (length) | - | - | No visual-text mismatch found | - | - | - | ✅ Pass |
| G014 | Convert between units of measurement (area) | - | - | No visual-text mismatch found | - | - | - | ✅ Pass |
| G015 | Identify line(s) of symmetry in 2D shapes | - | - | No visual-text mismatch found | - | - | - | ✅ Pass |
| G016 | Complete symmetrical figures given mirror line | - | - | No visual-text mismatch found | - | - | - | ✅ Pass |
| G017 | Calculate volume of cubes and cuboids | - | - | No visual-text mismatch found | - | - | - | ✅ Pass |
| G018 | Calculate volume of cubes and cuboids with unit conversion | Label Clarity | 🔴 P0 | Missing unit labels: diagram shows 0.5, 30, 200 without cm/m/mm | None | Add unit labels: '0.5 m', '30 cm', '200 mm' | High | Quick win |
| G019 | Visualize nets of cubes/cuboids and identify 3D shapes from nets | - | - | No visual-text mismatch found | - | - | - | ✅ Pass |
| G020 | Visualize nets of cubes/cuboids (draw net given 3D shape) | - | - | No visual-text mismatch found | - | - | - | ✅ Pass |
| G021 | Classify triangles by sides (equilateral, isosceles, scalene) | - | - | No visual-text mismatch found | - | - | - | ✅ Pass |
| G022 | Classify triangles by angles (acute, right, obtuse) | Missing Measurements | 🟡 P1 | Right angle symbol missing on 90° corner | None | Add right angle symbol (square in corner) | Medium | - |
| G023 | Classify quadrilaterals (square, rectangle, parallelogram, rhombus, trapezium) | - | - | No visual-text mismatch found | - | - | - | ✅ Pass |
| G024 | Calculate circumference/area of circle using π | Label Clarity | 🟡 P1 | Radius label '7' may be ambiguous (radius vs diameter) | None | Add 'r = 7 cm' with arrow | Medium | - |
| G025 | Interpret pie charts as fractions of a circle | Proportional Error | 🔴 P0 | Sector labeled 90° but visually larger; sectors may not sum to 100% (Ivy findings #3, #11) | Ensure text matches diagram | Adjust sector to exactly 90°; verify total 360° | High | CRITICAL - visual misrepresentation |

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

**Last Updated:** 2026-04-16 15:27 GMT+8
**Status:** Review completed, 11 issues identified (8 P0, 3 P1, 0 P2)
