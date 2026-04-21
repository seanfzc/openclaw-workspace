# Geometry Reconstruction Framework
## Root Cause Analysis & Solution Design

**Date:** 2026-04-19  
**Problem:** Current deconstructed data insufficient for accurate reconstruction

---

## The Core Problem

### What I Have Now (Insufficient)
```
Source: "Two overlapping quarter circles with radius 10 cm. 
         Shaded area OBC is 30 cm². Find area of OABCD."
         
Deconstructed: {
  "shape": "two overlapping quarter circles",
  "radius": 10,
  "shaded_area": "OBC = 30",
  "find": ["area of OABCD", "perimeter of OABCD"]
}

Reconstruction: AMBIGUOUS - multiple valid interpretations
```

### Why This Fails
1. **No coordinate system** - Where are O, A, B, C, D exactly?
2. **No geometric relationships** - How do the shapes overlap?
3. **No visual topology** - What is the boundary path of OABCD?
4. **No constraint verification** - Is the geometry mathematically consistent?

---

## Required Deconstruction Schema

### Level 1: Coordinate Geometry (Exact Positions)
```yaml
coordinate_system:
  origin: [0, 0]
  scale: 1cm per unit
  bounds: [0, 10] x [0, 10]

points:
  O: [0, 0]
  A: [10, 0]  # center of Q2
  B: [10, 0]  # same as A, vertex of triangle
  C: [8, 6]   # on Q1 arc, forms triangle OBC with area 30
  D: [10, 10] # top of Q2

verification:
  |OC|: 10.0  # on Q1
  |AC|: 10.0  # on Q2  
  area_OBC: 30.0  # triangle area
```

### Level 2: Geometric Primitives
```yaml
primitives:
  - type: quarter_circle
    center: O [0,0]
    radius: 10
    arc: from [0,10] to [10,0]
    
  - type: quarter_circle
    center: A [10,0]
    radius: 10
    arc: from [10,10] to [0,0]
    
  - type: triangle
    vertices: [O, B, C]
    area: 30
    shading: solid_fill
```

### Level 3: Visual Topology (What Student Sees)
```yaml
visual_elements:
  arcs:
    - Q1: thick_black_line
    - Q2: thick_black_line
    
  lines:
    - OA: thick_black_line (base)
    - AD: thick_black_line (side of Q2)
    - OC: implicit (radius)
    
  shaded_regions:
    - OBC: light_blue_fill, dark_blue_border
    
  labels:
    - O: bottom_left, bold
    - A=B: bottom_right, bold_red
    - C: on_arc, bold_red
    - D: top_right, bold
    
  dimensions:
    - OA: "10 cm" with double_arrow
```

### Level 4: Solution Path (Verification)
```yaml
solution:
  part_a:
    question: "Area of OABCD"
    interpretation: "Union of Q1 and Q2 minus triangle OBC"
    formula: "(1/4)πr² + (1/4)πr² - 30"
    answer: 127.08
    
  part_b:
    question: "Perimeter of OABCD"
    interpretation: "Arc Q1 + Arc Q2 + line from (0,10) to D"
    # OR: "Arc OC + Arc CD + DA + AO"
    # Need to specify which path!
```

---

## The Bigger Picture: Two Use Cases

### Use Case 1: Baseline Test (Exact Reconstruction)
**Requirement:** Reproduce the exact same question

**Input needed:**
- Complete coordinate geometry
- Exact visual layout
- Precise labeling positions
- Verified solution path

**Process:**
```
Deconstructed Data → Render Engine → Exact Visual → Student
```

### Use Case 2: Transfer Test (Creative Variation)
**Requirement:** Create similar but different question

**Input needed:**
- Problem type template (composite overlap)
- Constraint rules (area relationships, geometric properties)
- Variation parameters (radius, positions, shaded region)
- Solution verification method

**Process:**
```
Template + Constraints → Variation Engine → New Valid Problem → Student
```

---

## Proposed Solution: Three-Tier Data Model

### Tier 1: Canonical Template (Reusable)
```yaml
template_id: composite_overlap_two_quarter_circles
parameters:
  - radius: float
  - center_distance: float  # distance between centers
  - shaded_region_type: enum [triangle, sector, lens]
  - shaded_area: float
  
constraints:
  - centers must be distance d apart where 0 < d < 2r
  - shaded_region must be calculable from given info
  - resulting figure must have solvable area/perimeter
  
variants:
  - centers_touching: d = r
  - centers_separate: d > r
  - centers_overlapping: d < r
```

### Tier 2: Instance Specification (Specific Question)
```yaml
instance_id: Q21_baseline
inherits: composite_overlap_two_quarter_circles

parameter_values:
  radius: 10
  center_distance: 10  # A at (10,0), O at (0,0)
  shaded_region_type: triangle
  shaded_area: 30
  
computed_geometry:
  O: [0, 0]
  A: [10, 0]
  C: [8, 6]  # calculated to give area 30
  D: [10, 10]
  
visual_rendering:
  coordinate_system: [0,0] to [12, 11]
  label_positions: {...}
  shading: {...}
```

### Tier 3: Transfer Variation (Creative Generation)
```yaml
variation_rules:
  radius:
    range: [5, 15]
    step: 1
    
  center_distance:
    expression: "radius * k"
    k_range: [0.5, 1.5]
    
  shaded_area:
    constraint: "must_be_solvable_with_given_radius"
    
verification:
  - all_points_must_have_integer_or_simple_fraction_coordinates
  - area_must_be_calculable_without_calculator
  - diagram_must_fit_standard_page_size
```

---

## Implementation Questions for You

### 1. Data Source
**Where does deconstructed data come from?**
- A) Manual extraction from exam papers (current)
- B) OCR + AI parsing of exam papers
- C) Structured database of canonical problems
- D) Hybrid approach

### 2. Baseline Test Generation
**For exact reconstruction, what data do you have?**
- Just the text description?
- Marking scheme with answers?
- Original exam paper PDF?
- All of the above?

### 3. Transfer Test Creativity
**How similar should transfer questions be?**
- Same structure, different numbers only?
- Same concept, different configuration?
- Same difficulty, potentially different approach?

### 4. Quality Verification
**Who verifies the generated questions?**
- Automated mathematical checking only?
- Human review before use?
- Student pilot testing?

---

## Immediate Next Steps

### Option A: Improve Deconstruction Process
1. Create structured template for geometry questions
2. Extract complete coordinate data from source
3. Verify solvability before reconstruction
4. Then regenerate all diagrams

### Option B: Use Reference Images
1. You provide 2-3 "perfect" exam diagrams
2. I analyze and extract the visual language
3. Create rendering rules based on examples
4. Apply to all questions

### Option C: Manual Coordinate Specification
1. For each geometry question, you specify exact coordinates
2. I render exactly to specification
3. Verify together before finalizing

**Which approach do you prefer?**

---

## My Recommendation

Given the iteration cycles we've had, I recommend **Option A + B hybrid:**

1. **Short term:** You provide 2-3 reference diagrams you consider "perfect"
2. **I analyze:** Extract the visual language, labeling conventions, coordinate patterns
3. **Create template:** Structured deconstruction schema
4. **Apply to all:** Use template for remaining questions
5. **Verify:** You review final output

This gives us:
- Clear visual standard (from your examples)
- Structured data model (for consistency)
- Efficient regeneration (template-based)
- Quality verification (your final review)

**What do you think?**
