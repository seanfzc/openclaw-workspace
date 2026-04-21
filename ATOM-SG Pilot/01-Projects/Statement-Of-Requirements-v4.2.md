---
title: Statement of Requirements (C0) – Pilot v4.2 (Vision LLM Integration)
objective: Define requirements for Vision LLM integration to achieve exam-quality question reconstruction.
status: draft — incorporating Vision LLM pipeline and lessons learned
owner: Zcaethbot → Sean Foo (approval pending)
last_updated: 2026-04-21 05:50 SGT
directive_source: OPENCLAW DIRECTIVE – PILOT v4.1 (Recognition-First Integrated Training)
data_source: 94 questions across 5 elite-school prelim papers (ACS Junior, Nanyang, Henry Park, Nan Hua, RGPS)
quality_standard: Reconstruction of questions and visuals based on deconstructed data to original question standard
---

# Statement of Requirements – ATOM‑SG Pilot v4.2

## v4.2 Changes from v4.1

### Critical Additions
1. **Vision LLM Integration** — Now a BLOCKING REQUIREMENT (not enhancement)
2. **Quality Standard Defined** — Reconstruction fidelity to original exam question standard
3. **3-Layer Extraction Pipeline** — OCR + Vision LLM + OpenCV (mandatory)
4. **Exam-Quality Rendering** — Isometric 3D, grid precision, composite overlap, reflex angles
5. **Automated Validation** — Confidence thresholds, re-extraction strategies
6. **Launch Timeline Extended** — May 10, 2026 (2 weeks from today)

### Lessons Learned Incorporated
1. **Basic rendering is insufficient** — v2.0 baseline test (+83% word count) still not exam-quality
2. **Framework gaps identified** — Only 40% of exam content covered without Vision LLM
3. **Missing visual capabilities** — No isometric 3D, no grid precision, no composite overlap
4. **Quality verification is critical** — Independent QA revealed issues automation missed
5. **Deconstruction → Reconstruction loop** — Must verify reconstructed output ≈ original

---

## 1. Why We Are Here

After analysing **94 questions across 5 elite‑school prelim papers** (ACS Junior, Nanyang, Henry Park, Nan Hua, RGPS), the data revealed:

| Track | Coverage | Key Pathways |
|-------|----------|-------------|
| **Word Problems** | 35.1% | Cross‑Thread Collision (12.8%), Part‑Whole with Comparison (10.6%), Data Interpretation (6.4%), Before‑After Change (5.3%) |
| **Geometry** | 31.9% | Angles, Area & Perimeter, Volume & 3D, Properties & Classification |
| **Combined** | 67% | Rising to 71.3% with Constant‑Total + Supposition variants |

The original 5‑pathway plan was too fragmented. The **real novelty** of ATOM‑SG is teaching student to **identify pathway type and articulate equation shadow as very first step of every problem**, then immediately apply it to solve. This meta‑skill is what creates tipping point.

### 🚨 Critical Quality Crisis (2026-04-21)

**Issue:** Current rendering cannot achieve exam-quality standard.

**Evidence:**
- Baseline test v2.0: Basic matplotlib plots, no geometric precision
- Missing diagrams: Q35, Q37 had no visuals
- Visual quality: No isometric 3D, no grid precision, no composite overlap
- Linguistic complexity: 5.2/10 (exams require 10-12/10)
- Framework coverage: Only 40% of exam content

**Root Cause:** Basic rendering (matplotlib + TikZ) cannot reconstruct exam-quality diagrams from deconstructed data.

**Solution:** Vision LLM 3-layer extraction pipeline (OCR + Vision LLM + OpenCV) with exam-quality rendering rules.

---

## 2. Primary Objective

**Measure how fast a student can ramp up with targeted intervention training following a baseline diagnostic test.**

**CRITICAL:** To measure this accurately, we must be able to **reconstruct questions and visuals from deconstructed data to original question standard**. This is now a BLOCKING REQUIREMENT.

The key is understanding how we can make intervention training **as powerful as possible** with ATOM‑G's unique methodology **without compromising over‑execution** — this is a pilot, not a production build. The methodology drives what we need from tech stack, not the other way around.

---

## 3. Pilot Structure (5 Weeks) — Updated Timeline

### Week 1 — Baseline (Offline Paper Test) — **COMPLETE**

The student takes a printed test covering **all 3 tracks**:

| Track | # Questions | Notes |
|-------|-------------|-------|
| Word Problems | 20 | Drawn from 4 main pathways identified across 5 prelim papers |
| Geometry | 12 | Angles, area, volume, properties — aligned to existing nano‑nodes |
| Data Interpretation | 8 | Bar graphs, pie charts, tables with red‑herring data |
| **Total** | **40** | |

**Process:**
1. Student completes test on paper.
2. Parent scans working (handwritten answers + working).
3. OpenClaw analyses scan and returns a **gap map** showing **3 weakest pathways** (across any track).

**Important:** Baseline has **no forced articulation** — we are measuring raw performance first.

### Weeks 2–4 — Integrated Intervention (Online MVP)

**🚨 BLOCKER:** Requires Vision LLM integration for exam-quality visual rendering.

Train **3 weakest pathways** identified from baseline (one per week).

Every problem follows this **exact loop**:

```
Student reads question
        ↓
Forced Articulation (must type/write before solving):
  Pathway type: ________________
  Equation shadow (in your own words): ________________
        ↓
Student solves problem (with exam-quality visual reconstruction)
        ↓
Instant Triad‑based feedback on BOTH identification and solution
```

**Daily 5‑minute Pathway Radar warm‑up** (identification only, 10 mixed questions) builds pure recognition muscle.

### Week 5 — Transfer Test — **EXTENDED to Week 6**

- **40 new unseen problems** (trained + held‑back pathways) + geometry/DI transfer tests.
- Measures whether recognition skill transfers to pathways student was *not* explicitly trained on.

---

## 4. Success Criteria

| Criterion | Target |
|-----------|--------|
| **🆕 Reconstruction Fidelity** | ≥ 90% match to original exam question standard |
| Pathway identification accuracy on trained pathways | ≥ 90% |
| Articulation quality reaches Level 2+ on | ≥ 90% of problems |
| Solving accuracy improvement from baseline on trained pathways | ≥ 80% |
| Transfer: identification accuracy on trained pathways | ≥ 80% (for first 3 items), ≥ 50% for held‑back pathways |

---

## 5. Storylines — From Wrong Answer to Mastery

### Storyline A: Word Problem — Cross‑Thread Collision

1. **The Question:** "A shop sold 3/5 of its pens on Monday and 1/4 of the remainder on Tuesday. It had 150 pens left. How many pens did it have at first?"
2. **Wrong Answer:** Student treats it as a simple fraction problem, ignoring the two‑stage change. Writes 150 ÷ (1 − 3/5 − 1/4) = wrong.
3. **Diagnosis (after baseline scan):** System maps this to **Before‑After Change** pathway. Error pattern: student did not recognise the sequential "remainder" structure — classic Cross‑Thread Collision trap (fraction language disguising a change pathway).
4. **Targeted Training UI/Flow:**
   - Student opens the day's intervention module.
   - **Forced articulation first:** "What pathway type is this?" → Student must type "Before‑After Change" before seeing any solving interface.
   - "Write the equation shadow in your own words" → Student types: "After first change, then after second change, find the original."
   - **Solving phase:** Student works through the problem with the articulated framework visible.
   - **Instant Triad feedback:** Green (correct ID + correct solution), Yellow (correct ID but wrong solution), Red (wrong ID — re‑route to Pathway Radar).
5. **Retest (Week 6):** A new unseen Before‑After Change problem with different surface features. Student articulates the pathway correctly and solves → ramp‑up measured.

### Storyline B: Geometry — Composite Shape Area

1. **The Question:** A composite figure made of a square and a ¾‑circle. Find the total area.
2. **Wrong Answer:** Student calculates the full circle area instead of ¾, or misidentifies the square's side length as the diameter.
3. **Diagnosis:** System maps to **Area & Perimeter (Composite Shapes)** sub‑pathway. Gap: visual decomposition of overlapping regions.
4. **Targeted Training UI/Flow:**
   - Forced articulation: "Part‑Whole (Composite Shapes)" + "Total area = area of square + area of ¾ circle."
   - Interactive diagram where student shades each component before calculating (**🆕 Vision LLM reconstructed diagram**).
   - Triad feedback on both the decomposition logic and the numerical answer.
5. **Retest:** New composite shape (different configuration) — student decomposes correctly → mastery confirmed.

### Storyline C: Data Interpretation — Red Herring

1. **The Question:** A bar graph shows sales for 5 products. The question asks about the difference between Product A and Product C, but Product D's bar is visually prominent and close to C.
2. **Wrong Answer:** Student reads Product D's value instead of C.
3. **Diagnosis:** System maps to **Data Interpretation — Red Herring** sub‑pathway. Gap: filtering irrelevant visual data.
4. **Targeted Training UI/Flow:**
   - Forced articulation: "Data Interpretation — comparison of two specific data points, ignore others."
   - "Data Filter" mini‑game: student must highlight only the relevant bars before answering.
   - Triad feedback on filter accuracy + numerical answer (**🆕 Vision LLM reconstructed chart**).
5. **Retest:** New chart with a different red herring — student filters correctly → transfer confirmed.

---

## 6. What This Drives for Tech Stack & Software Build

### 6.1 What We Need (Minimum Viable) — UPDATED

| Component | Purpose | Priority | Status |
|-----------|---------|----------|--------|
| **Baseline test PDF generator** | Print 40‑question test with diagrams | Week 1 | ✅ Complete |
| **Scan upload & OCR pipeline** | Ingest scanned student answers | Week 1 end | ✅ Complete |
| **Gap map analyser** | Identify 3 weakest pathways from baseline | Week 1 end | ✅ Complete |
| **🆕 Vision LLM 3-Layer Extraction** | Extract structure (Vision LLM) + measurements (OpenCV) + text (OCR) | **BLOCKING** | ❌ Required |
| **🆕 Exam-Quality Rendering Pipeline** | Render diagrams from YAML with pixel precision | **BLOCKING** | ❌ Required |
| **🆕 Automated Validation** | Confidence thresholds, re-extraction strategies | **BLOCKING** | ❌ Required |
| **MVP online question display** | Show problems with forced articulation boxes + embedded visual diagrams (rendered from exam-quality Vision LLM data) | Week 2 | 🟡 Ready (needs Vision LLM) |
| **Forced articulation UI** | Pathway type + equation shadow input fields (must complete before solving) | Week 2 | 🟡 Ready |
| **Triad feedback engine** | Instant feedback on identification + solution. **ENHANCEMENT: Include model articulations in response so students can compare their articulations against ideal ones (Priority 2 recommendation).** | Week 2 | 🟡 Ready |
| **Pathway Radar warm‑up** | 5‑min, 10‑question identification‑only drill | Week 2 | 🟡 Ready |
| **Radar chart visualization** | Visual radar chart showing pathway identification accuracy and trends over time (frontend-only enhancement using Chart.js/D3.js). **Recommendation from MVP-Backend Alignment (Priority 1, Low severity).** | Week 2+ | 🟡 Ready |
| **Progress & milestone tracker** | Visual pathway mastery dashboard | Week 2 | 🟡 Ready |
| **Transfer test generator** | 40 unseen problems (20 new + 20 held‑back) + geometry/DI transfer tests. | Week 6 | 🟡 Ready |
| **Ramp‑up analytics** | Compare baseline → retest speed & accuracy | Week 6 | 🟡 Ready |

### 6.2 What We Do NOT Need for Pilot — UPDATED

- Production‑grade infrastructure (cloud hosting, auth, multi‑user)
- Gamification engine beyond simple mini‑games
- Automated problem generation (we curate manually from prelim papers)
- Mobile app (web interface is sufficient)
- Student management system
- ~~MVP online question display with embedded visual diagrams~~ → **🆕 MUST be exam-quality (Vision LLM reconstruction)**
- ~~Student drawing capability during training~~ → **🆕 Keep as-is (canvas tool)**
- ~~Multi‑LLM support~~ → **🆕 Required: RapidOCR (OCR) + Vision LLM (structure) + OpenCV (measurements)**

### 6.3 Technical Constraints — UPDATED

- **Local‑first:** File storage on machine, not cloud. Simple Flask/FastAPI backend.
- **Static frontend:** HTML5 + JavaScript. No framework overhead.
- **🆕 Rendering:** Vision LLM 3-layer pipeline:
  - **OCR:** RapidOCR for text extraction
  - **Vision LLM:** Structure identification, spatial relationships
  - **OpenCV:** Pixel-precise measurements (angles, coordinates, line styles)
  - **Output:** YAML with confidence scores → Validate → Render to exam-quality
- **🆕 Validation:** Confidence thresholds (≥0.9 trust, <0.7 flag MAJOR, <0.5 block CRITICAL)
- **🆕 Rendering Rules:** Isometric 3D (30°), grid precision (1cm squares), composite overlap (clipping paths), reflex angles (proper arcs)
- **Rapid iteration:** Must allow quick changes based on what student's data tells us.

### 6.4 Bureau Organisation (per v4.1 Directive) — UPDATED

| Bureau | LLM | Responsibility | Status |
|--------|-----|---------------|--------|
| **Pedagogy** | GLM 4.7 (pedagogical bureau) | Generate all questions + diagrams. Auto‑classify every question. Generate equation shadow + recognition cues + 3‑level articulation rubric. | 🟡 Ready |
| **Integrity** | GLM 5.1 | Review every question for accuracy. Generate Triad feedback for every possible student articulation. | 🟡 Ready |
| **🆕 Vision LLM** | **Vision LLM (Qwen/Ollama/Moondream)** | Extract diagram structure, identify shapes, spatial relationships, semantic meaning. | ❌ Required |
| **🆕 Geometric Analysis** | **OpenCV** | Pixel-precise measurements: angles, coordinates, line styles, fill patterns, hatching angles. | ❌ Required |
| **🆕 Text Extraction** | **RapidOCR** | Extract handwritten text, numeric labels, units with confidence scores. | ❌ Required |
| **Logistics** | Tesseract + TikZ/Matplotlib | ~~Render all diagrams locally. Build minimal MVP web interface.~~ → **🆕 Validate YAML + render from exam-quality YAML with pixel precision.** | 🟡 Ready (needs Vision LLM input) |
| **Creative** | — | Create daily Pathway Radar warm‑up. Design simple student reflection sheet. | 🟡 Ready |

---

## 7. Data Foundation

The pilot is grounded in **real exam data**, not hypotheticals:

- **5 elite‑school prelim papers** (2025): ACS Junior, Nanyang, Henry Park, Nan Hua, RGPS
- **94 questions** analysed and classified by pathway type
- **Coverage:** 67–71.3% of P6 exam content captured by targeted pathways
- **Source files:** `neo_output/` directory containing corrected, ATOM‑SG‑analysed versions of all 5 papers
- **🆕 Deconstruction Target:** Every exam question must be deconstructed to YAML and reconstructed to exam-quality standard (≥90% fidelity)

This data will be used to:
1. Select the 40 baseline questions (20 WP + 12 Geo + 8 DI)
2. **🆕 Deconstruct each question to YAML** using Vision LLM 3-layer pipeline
3. **🆕 Validate reconstruction fidelity** (≥90% match to original)
4. Generate intervention training problems for the 3 weakest pathways
5. Create Pathway Radar warm‑up items
6. Build Week 6 transfer test (20 WP + 12 Geo + 8 DI)

---

## 8. Deliverables & Timeline — UPDATED

| Deliverable | Owner | Target | Status |
|-------------|-------|--------|--------|
| **SOR v4.2 (this document)** | Zcaethbot | 2026‑04‑21 | 🟡 Draft |
| **🆕 Vision LLM 3-Layer Pipeline** | Vision LLM + OpenCV + OCR Bureaus | Week 2 | ❌ Required |
| **🆕 Exam-Quality Rendering Rules** | Logistics Bureau | Week 2 | ❌ Required |
| **🆕 Automated Validation System** | Integrity Bureau | Week 2 | ❌ Required |
| **🆕 Deconstruction of 94 Exam Questions** | Vision LLM Bureau | Week 2 | ❌ Required |
| **🆕 Reconstruction Fidelity Verification** | Integrity Bureau | Week 2 | ❌ Required |
| **Baseline Test Pack (40 questions, printable PDFs)** | Pedagogy Bureau | Week 1 | ✅ Complete |
| **Gap Map Analyser** | Pedagogy + Logistics | Week 1 end | ✅ Complete |
| **MVP Web Interface** (question display + forced articulation + feedback) | Logistics Bureau | Week 2 | 🟡 Ready (needs Vision LLM) |
| **Pathway Radar Warm‑up** | Creative Bureau | Week 2 | 🟡 Ready |
| **Triad Feedback Engine** | Integrity Bureau | Week 2 | 🟡 Ready |
| **Transfer Test** | Pedagogy Bureau | Week 6 | 🟡 Ready |
| **Ramp‑up Analytics Report** | Zcaethbot | Week 6 end | 🟡 Ready |

---

## 9. Vision LLM Architecture — NEW SECTION

### 9.1 3-Layer Extraction Pipeline

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Exam Image   │────▶│ Vision LLM    │────▶│ OpenCV       │──▶│ Validate    │
│  (student scan)  ├─────┤   ├───────┤   ├─────┤   │
└─────────────────┘     └─────────────────┘     └─────────────────┘     └─────────────────┘
```

**Layer 1: OCR (RapidOCR)**
- Extract handwritten text, numeric labels, units
- High confidence on text (LLMs misread characters)
- Output: `{text: "12 cm", confidence: 0.95}`

**Layer 2: Vision LLM (Qwen/Ollama/Moondream)**
- Identify diagram structure, shapes, spatial relationships
- Medium confidence on semantics (context understanding)
- Output: `{type: "triangle", vertices: [A,B,C], relationships: {...}, confidence: 0.8}`

**Layer 3: OpenCV**
- Pixel-precise measurements: angles, coordinates, line styles
- High confidence on geometry (LLMs approximate)
- Output: `{angle_A: 35.7°, edge_AB_length: 120px, style: "solid", confidence: 0.99}`

**Merge Logic:**
1. Start with Vision LLM's structural output (the "skeleton")
2. Override label text with OCR readings (higher accuracy)
3. Override positions/angles with OpenCV measurements (pixel-precise)
4. Tag every field with `source` and `confidence`
5. Detect conflicts (OCR vs LLM disagree) and flag them
6. Pass to `validate_yaml` before rendering

### 9.2 Source Priority (When Sources Disagree)

| Data Type | Best Source | Why Others Fail |
|-----------|------------|-----------------|
| Label text ("12 cm", "35°") | OCR | LLMs misread characters |
| Diagram structure | Vision LLM | OCR and OpenCV can't infer meaning |
| Spatial relationships | OpenCV | LLMs approximate positions |
| Line styles (solid/dashed) | OpenCV | LLMs frequently misidentify |
| Fill patterns | OpenCV | Precise angle/density measurement |
| Angles between lines | OpenCV | LLMs round or guess |

### 9.3 Validation Rules

**Confidence Thresholds:**
| Confidence | Action |
|-----------|--------|
| ≥ 0.9 | Trust. No review needed. |
| 0.7–0.9 | Accept. Flag if other sources disagree. |
| 0.5–0.7 | Flag MAJOR. Needs manual review before rendering. |
| < 0.5 | Flag CRITICAL. Block rendering. Re-extract from indicated source. |

**Structural Checks (CRITICAL if failed):**
- Every label `anchor` references a shape/edge that exists in `shapes`
- Triangle interior angles sum to 180° (±2°)
- Quadrilateral interior angles sum to 360° (±2°)
- Bar model segments sum to their stated whole
- Pie chart percentages sum to 100%

### 9.4 Re-Extraction Strategy

When validation fails, don't re-run the entire pipeline. Target the specific source:

| Issue Type | Re-Query |
|-----------|-----------|
| Label misread | Re-run OCR with different preprocessing |
| Wrong spatial relationship | Re-prompt Vision LLM with specific question |
| Angle measurement off | Check OpenCV preprocessing |
| Shape misidentified | Re-prompt Vision LLM with cropped region |

---

## 10. Exam-Quality Rendering Rules — NEW SECTION

### 10.1 Universal Gates (Load Before Rendering Any Diagram)

**Gate 0 — Solve First**
Solve the problem to completion before choosing a visual. If you cannot solve it, you cannot draw it.

**Gate 1 — Validate Extraction**
Skip this gate if the YAML was authored by hand.
Apply source priority, block on CRITICAL confidence (<0.5), flag MAJOR (<0.7).

**Gate 2 — Audience Constraint Check**
| Level | Cannot Use | Use Instead |
|-------|-----------|-------------|
| P1–P2 | Multiplication, division, variables | Counting, grouping, concrete objects |
| P3–P4 | Algebra, ratios, negative numbers | Bar models, suppose heuristic, guess-and-check |
| P5–P6 | Simultaneous equations, formal algebra | Unitary method, suppose heuristic, bar models |

**Gate 3 — Map the Reasoning Chain**
Write the step-by-step reasoning a student at the target level would use. Your diagram must make **each step** visible.

**Gate 4 — Plan Scale**
Choose a pixels-per-unit scale for all elements that will be compared. Write it down. If two quantities use different scales, they must appear in visually separated panels.

### 10.2 Label & Arrow Rules (Universal)

**Label Placement:**
- Anchored, not fixed — every label has anchor + offset
- Collision detection mandatory — 2px minimum clearance
- Stay within canvas — clamp all labels with padding
- Never cross unrelated lines
- Minimum proximity — smallest distance that avoids collision
- Contrast on fills — ≥4.5:1 contrast ratio or opaque background
- Font hierarchy — 14px bold (title), 12px bold (labels), 11px (data)

**Arrow Types:**
- Leader line: 0.5px, dashed, no arrowhead
- Callout: 1px, solid, single arrowhead
- Dimension: 1px, solid, double arrowheads + perpendicular ticks
- Flow: 1.5px, solid, single arrowhead

**Precision Rules (All Arrows):**
- Arrow tip touches target boundary (compute intersection)
- Arrow tail starts at source boundary
- All arrowheads identical dimensions (6px long, 4px wide)
- No arrow extends past its arrowhead

**Dimension Lines:**
- Endpoint precision — both arrow tips touch extension lines to the pixel
- Length accuracy — arrow span equals visual length of measured edge
- Parallelism — dimension line slope = measured edge slope exactly
- Extension lines exactly perpendicular
- Label centred on dimension line

### 10.3 Geometry Rendering Rules

**2D Geometry (Composite/Overlapping Shapes):**
- Z-order: Background fills → Pattern fills → Outlines → Construction lines → Markers → Labels
- Labels: Side lengths at midpoint (8px offset), angles inside (20% of shorter arm), vertices outside
- "Not to scale" label: Bottom-right, italic, 10px
- Overlap regions: Compute intersection as clipped path, apply fill only to clipped region

**3D Solids (Cuboid, Prism, Cylinder):**
- Isometric projection (30°): `screen_x = origin_x + (x - y) × cos(30°) × scale`
- Visible faces: Top, front, right always visible. Back edges dashed or omitted
- Parallel edges stay parallel — no perspective convergence
- Water level: Fill visible faces below water line
- Dimension lines: Along front-facing edges only

**Isometric Stacked Cubes:**
- Visible face computation: `top_visible = (x, y, z+1) not in cube_set`
- Edge classification: Solid meets air = 1.5px outline; between cubes = 0.5px internal
- Rendering order: Sort cubes by (y descending, x ascending, z ascending)
- Face shading: All tops same shade (lightest), all fronts same, all sides same

**Cube Nets:**
- 2D diagrams, not 3D renders
- Every face identical square, snapped to unit grid
- Adjacent faces share exactly one full edge
- Internal shared edges: 0.5px. External outline: 1.5px

### 10.4 Data Visualization Rules

**Bar Charts:**
- Y-axis starts at zero (CRITICAL)
- Bar height = value (compute (value/max) × plot_height, flag >3% deviation)
- Equal bar widths, equal gaps
- Gridlines behind bars, not on top

**Pie Charts:**
- Slice angles: Expected = (value/total) × 360°, flag >2° deviation
- Percentages sum to 100%, flag 99% or 101%+
- Inside labels if sweep > 40°, outside with leader line otherwise
- Leader lines: Edge → elbow → horizontal to label
- Collision resolution: Sort by angle, push lower one down if too close

**Line Graphs:**
- Point positions match (value × scale + origin)
- Line equation fidelity (verify 3 points lie on line)
- Grid scale consistent (each square = same step)
- Data labels not overlapping at close-valued points

**Number Lines:**
- Uniform tick spacing (measure 3+ intervals, flag >1px variation)
- Fraction/decimal placement (e.g., "2.5" exactly halfway between 2 and 3)
- Open vs closed circles match inequality symbols

**Timelines:**
- Chronological order (left-to-right = earliest-to-latest)
- Proportional spacing (9:30 exactly halfway between 9:00 and 10:00)
- Labels not piling up when events are close

---

## 11. Quality Verification — NEW SECTION

### 11.1 Reconstruction Fidelity Target

**Standard:** ≥90% match between reconstructed output and original exam question.

**Measurement Criteria:**
- Visual fidelity: Pixel-precise match of shapes, angles, positions
- Semantic fidelity: Correct interpretation of problem structure
- Linguistic fidelity: Exact match of question text, labels, units
- Completeness: No missing elements (diagrams, labels, annotations)

### 11.2 Audit Protocol

**Audit Stages (Run in Order):**
1. Stage 0 — Establish Intent: "This diagram claims to show ____."
2. Stage 1 — Pre-Render YAML Validation: Check confidence thresholds, structural integrity
3. Stage 2 — Audience Appropriateness: Flag concepts above target level
4. Stage 3 — Universal Visual Checks: Label binding, legibility, numeric consistency
5. Stage 4 — Type-Specific Checks: Load relevant `types/*.md` file
6. Stage 5 — Label Forensics: Leader lines, occlusion, orphan labels
7. Stage 6 — Pedagogical Sanity: Does it teach or just depict?

**Severity Classification:**
- CRITICAL — Teaches a falsehood or uses concepts above the audience
- MAJOR — Correct and age-appropriate but confusing
- MINOR — Polish issues that don't impair learning
- ADVISORY — Pedagogical improvement suggestion

### 11.3 Tester Procedures

- **T1 — Numeric Recomputation:** List every number. Recompute every arithmetic claim.
- **T2 — Pixel Ratio Measurement:** Measure pixel sizes, compute actual vs expected ratio (flag >3% deviation).
- **T3 — Label Binding Trace:** For every label, verify anchor is unambiguous.
- **T4 — Reasoning Chain Walk-Through:** Solve at target level. Point to visual element for each step.
- **T5 — Audience Simulation:** Cover text outside the diagram. Can a target-level student follow it?
- **T6 — Scale Audit:** Same scale within panels, different scales separated visually.
- **T7 — Bracket Span Verification:** Endpoints on boundaries, content sums to label.

---

## 12. Open Decisions — v4.2 Updates

1. **🆕 Vision LLM Model Selection:** Which Vision LLM to use? Options: Qwen, Ollama, Moondream. **Pending decision.**
2. **🆕 Validation Threshold Adjustments:** Are confidence thresholds (≥0.9 trust, <0.5 block) appropriate? **Pending decision.**
3. **Baseline question selection:** Which 40 questions from 94 analysed? **Sean's decision: Balanced** — Select questions proportionally across pathways based on exam coverage. (✅ Resolved in v4.1)
4. **Student reflection sheet format:** Paper‑based or digital? **Sean's decision: Digital** — Create a digital reflection sheet interface in the MVP. (✅ Resolved in v4.1)
5. **Scan ingestion workflow:** Parent emails scan → OpenClaw processes? Or upload through MVP interface? **Sean's decision: Upload through MVP interface** — Implement scan upload directly in the MVP web interface. (✅ Resolved in v4.1)

---

## 13. Lessons Learned — NEW SECTION

### 13.1 Quality Crisis Lessons (2026-04-21)

**Lesson 1: Basic Rendering Is Insufficient**
- Evidence: v2.0 baseline test (+83% word count) still not exam-quality
- Issue: matplotlib + TikZ cannot achieve pixel precision for exam diagrams
- Fix: Vision LLM 3-layer pipeline (OCR + Vision LLM + OpenCV)

**Lesson 2: Framework Gaps Identified**
- Evidence: Only 40% of exam content covered without Vision LLM
- Issue: Missing G5-G8 (composite overlap, grid construction, 3D viz, angle chasing)
- Fix: Expand taxonomy, add composite overlap rendering rules

**Lesson 3: Independent QA is Critical**
- Evidence: Manual review revealed issues automation missed
- Issue: 90 tests passing but START HERE broken (structure-only tests)
- Fix: Action verification tests + manual quality gate

**Lesson 4: Deconstruction → Reconstruction Loop Required**
- Evidence: Cannot verify quality without reconstructing from deconstructed data
- Issue: No validation loop between extraction and rendering
- Fix: Validate YAML → Render → Audit → Reconstruction fidelity check

**Lesson 5: Quality Standard Must Be Explicit**
- Evidence: Implicit quality assumption led to v2.0 "good enough" fallacy
- Issue: No clear definition of "exam-quality" or "reconstruction fidelity"
- Fix: Define quality standard (≥90% reconstruction fidelity), audit protocol

### 13.2 Process Lessons

**Lesson 6: Always Ask the Right Questions Early**
- Should have asked: "Is current quality acceptable for launch?" before proceeding
- Should have asked: "What is blocking launch?" before treating Vision LLM as enhancement
- Should have asked: "Does MVP meet your quality standard?" before recommending launch

**Lesson 7: User Feedback About Quality Must Be Taken Seriously**
- "Rendering is very bad" = Current rendering cannot achieve required quality
- "Cannot launch when I cannot get the quality to where I want" = Quality standard is blocking
- "Pilot will fail if I listened to your recommendation" = Deferring quality = failure

**Lesson 8: Timeline Should Follow Quality, Not Vice Versa**
- Artificial deadlines (Week 2 launch) cannot override quality requirements
- Better to extend timeline than to launch with broken features
- Launch when quality is achieved, not when calendar says

---

## 14. Launch Timeline — UPDATED

| Milestone | Target Date | Status |
|------------|-------------|--------|
| **SOR v4.2 Approval** | 2026‑04‑21 | 🟡 Pending |
| **Vision LLM 3-Layer Pipeline** | 2026‑04‑23 | ❌ Required |
| **Exam-Quality Rendering Rules** | 2026‑04‑24 | ❌ Required |
| **Automated Validation System** | 2026‑04‑25 | ❌ Required |
| **Deconstruction of 94 Exam Questions** | 2026‑04‑26 | ❌ Required |
| **Reconstruction Fidelity Verification** | 2026‑04‑27 | ❌ Required |
| **Baseline Test Pack (Revised)** | 2026‑04‑28 | 🟡 Pending |
| **Weeks 2-4 Intervention MVP** | 2026‑05‑01 | 🟡 Pending |
| **Week 6 Transfer Test** | 2026‑05‑05 | 🟡 Pending |
| **🎯 PILOT LAUNCH** | **2026‑05‑10** | 🟡 Target |

**Total Timeline Extension:** 14 days from April 26 → May 10, 2026

---

## 15. Appendices

### Appendix A: Vision LLM Documentation References

The following documentation has been incorporated into v4.2:

| File | Purpose |
|------|---------|
| `00-overview.md` | File index + architecture |
| `01-rendering-gates.md` | 5 gates before rendering |
| `02-label-arrow-rules.md` | Universal label & arrow rules |
| `03-audit-protocol.md` | Audit protocol, severity, output format |
| `architecture.md` | 3-layer pipeline, source priority |
| `ocr-setup.md` | RapidOCR, EasyOCR, Tesseract comparison |
| `opencv-analysis.md` | OpenCV geometric analysis |
| `validation.md` | Pre-render validation, confidence thresholds |
| `types/*.md` | Diagram-specific rules (11 types) |

**Total:** 20 files covering extraction, validation, rendering, audit

### Appendix B: v4.1 → v4.2 Migration Guide

| v4.1 Element | v4.2 Update |
|---------------|--------------|
| Basic rendering (matplotlib + TikZ) | Vision LLM 3-layer pipeline + exam-quality rendering |
| No deconstruction → reconstruction loop | Deconstruct (YAML) → Validate → Render → Verify (≥90% fidelity) |
| Implicit quality standard | Explicit quality standard (reconstruction fidelity) |
| Week 2 launch (2026-04-26) | Week 6 launch (2026-05-10) |
| Vision LLM as enhancement | Vision LLM as BLOCKING REQUIREMENT |

---

*This document supersedes SOR v4.1. Approval pending from Sean Foo.*
