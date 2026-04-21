# P0 Critical Issues Requiring Immediate Attention

**Generated:** 2026-04-16 15:45 GMT+8
**Updated:** 2026-04-16 15:27 GMT+8 (added G001)
**From Review:** P0-6 Visual-Text Mismatches Review + Manual Spot Check
**Total P0 Issues:** 4

---

## 🔴 P0 Issues (Block Learning, Must Fix Before Launch)

### 1. G010: Shape Mismatch – Quarter-Circle vs Half-Circle
- **Problem:** Composite shape perimeter
- **Issue:** Diagram shows half-circle attached to middle of square side, but question text describes quarter-circle (UX test finding)
- **Impact:** Students lose trust in system; contradictory visual vs text information
- **Fix:** Update diagram to show quarter-circle (90° sector) attached to corner
- **Priority:** HIGH
- **Estimated Fix Time:** 15 minutes

### 2. G025: Proportional Error – Pie Chart Sector Misrepresentation
- **Problem:** Interpret pie charts as fractions of a circle
- **Issue:** Sector labeled 90° (¼ of circle) but visually appears larger; sectors may not sum to 100% (Ivy findings #3, #11)
- **Impact:** Students misjudge fractions from visual estimation, leading to wrong answers
- **Fix:** Adjust sector to exactly 90°; ensure visual proportion matches label; verify total 360°
- **Priority:** HIGH
- **Estimated Fix Time:** 10 minutes

### 3. G018: Label Clarity – Missing Unit Labels
- **Problem:** Calculate volume with unit conversion (0.5 m × 30 cm × 200 mm)
- **Issue:** Diagram shows dimensions 0.5, 30, 200 without unit labels (only "m" appears). Missing "cm" and "mm".
- **Impact:** Ambiguous which unit applies to which dimension; conversion problem unsolvable
- **Fix:** Add explicit unit labels: "0.5 m", "30 cm", "200 mm"
- **Priority:** HIGH
- **Estimated Fix Time:** 5 minutes

### 4. G001 (and G002, G003, G004, G007, G008): Missing Angle Rays
- **Problem:** Measure angles using a protractor
- **Issue:** Diagram shows arcs but missing the two rays that form each angle, making it impossible to measure angles with a protractor (angle = intersection of two lines)
- **Impact:** Students cannot identify what angle is being measured; contradicts definition of angle
- **Fix:** Add radial lines for each angle in all angle diagrams
- **Priority:** HIGH
- **Estimated Fix Time:** 20 minutes (update draw_angle_diagram function)

---

## 🚨 Action Required

1. **Immediate Diagram Updates** – RenderBot needs to regenerate SVGs for G010, G025, G018
2. **Visual QA** – Human review of updated diagrams before deployment
3. **Cross-Check** – Ensure no similar issues exist in other geometry problems

---

## 📋 Verification Checklist

- [ ] G010 diagram now shows quarter-circle (90°) attached to corner
- [ ] G025 pie chart sector exactly 90°, total 360°
- [ ] G018 cuboid has clear unit labels (m, cm, mm)
- [ ] All other geometry problems reviewed for similar issues

---

**Next Review:** After fixes applied, conduct spot-check of 5 random geometry problems for visual-text consistency.

**Owner:** Diagram Rendering Team
**Deadline:** Before MVP launch (ASAP)