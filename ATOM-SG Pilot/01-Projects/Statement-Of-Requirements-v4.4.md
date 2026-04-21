---
title: Statement of Requirements (C0) – Pilot v4.4 (Focused MVP with Iterative Verification)
objective: Replicate whole process working end-to-end with 4 focused questions, testing against 12 diverse personas at every stage.
status: draft — focused MVP with iterative stages
owner: Zcaethbot → Sean Foo (approval pending)
last_updated: 2026-04-21 10:15 SGT
directive_source: OPENCLAW DIRECTIVE – PILOT v4.1 (Recognition-First Integrated Training)
quality_standard: Quality of reconstruction data must match original exam questions; deconstructed data must enable improvisation during transfer testing without obvious human errors and be solvable using both visual and text information.
---

# Statement of Requirements – ATOM‑SG Pilot v4.4

## Executive Summary

**This SOR takes a focused, iterative approach to replicate the whole process working end-to-end.**

**Key Insights:**
1. **Focus on 4 questions, not 94** — Verify end-to-end quickly, not stuck at generation
2. **Test against 12 personas** — Diverse student archetypes represent target population
3. **Success criteria at every stage** — Deconstruct → Generate → Test → Intervene → Transfer
4. **Dynamic process** — Pivot, track, and deprecate old versions with version tags
5. **End-to-end verification** — Scan → Deconstruct → Generate → Test → Intervene → Transfer

**Root Cause from Sean Foo:**
> "We deconstructed exam data outside of OpenClaw and this resulted in reconstruction deficits. We have no choice but to do it internally. Consequence is we are unable to establish veracity of existing MVP."

---

## 1. Taking Stock — What Do We Have?

### 1.1 External Data (Deconstructed Outside OpenClaw)

| Asset | Location | Format | Verdict |
|-------|----------|--------|---------|
| **5 Exam Papers (PDF)** | `~/Desktop/neo_output/` | ✅ KEEP — Original source |
| **Deconstructed Questions (Markdown)** | `~/Desktop/neo_output/*.md` | ❌ REDUCE — Extract insights only (pathway classifications, equation shadows), discard structure |
| **Extracted Images (PNG/JPG)** | `~/Desktop/neo_output/extracted_images/` | ✅ KEEP — Good source for Vision LLM |

**Why Reduce/Extract-Only:**
- External deconstruction was manual, not machine-parseable
- No machine-readable visual data (coordinates, angles, dimensions)
- Cannot verify reconstruction fidelity
- Use for **reference insights only** (pathway types, shadow patterns), not as source data

### 1.2 Internal Data (Built Within OpenClaw)

| Asset | Location | Status | Verdict |
|-------|----------|--------|---------|
| **28 P5 Problem Cards** | `01-Projects/Baseline/P5-Problem-*.md` | ✅ KEEP — Good structure |
| **25 Geometry Problems (G001-G025)** | `02-Geometry/problems/G*.md` | ✅ KEEP — Good structure |
| **20 Word Problems (WP001-WP020)** | `03-WordProblems/problems/WP*.md` | ✅ KEEP — Good structure |
| **Geometry Taxonomy (18 Nano-Nodes)** | `Geometry_Taxonomy_NanoNodes.md` | ✅ KEEP — Approved by Sean |
| **Geometry Rubrics** | `02-Geometry/Geometry-Rubrics.md` | ✅ KEEP — Good framework |
| **Rubric Mapping** | `02-Geometry/Geometry-Rubric-Mapping.md` | ✅ KEEP — 25 problems mapped |
| **Baseline PDF Generator** | `05-Backend/generate_full_baseline_pdf.py` | ✅ KEEP — Functional (use with internal deconstruction) |
| **Backend API (19 Endpoints)** | `05-Backend/main.py` | ✅ KEEP — Functional, tested |
| **Frontend (Static HTML/JS)** | `05-Backend/frontend/` | ✅ KEEP — Recognition-first loop, forced articulation, triad feedback |
| **33 Bug Fixes** | Multiple files | ✅ KEEP — Verified |
| **90 Playwright Tests** | `05-Backend/playwright-tests/` | ✅ KEEP — Good coverage |
| **Action Verification Tests (15)** | `05-Backend/playwright-tests/tests/action-verification.spec.ts` | ✅ KEEP — Addresses behavioral testing |
| **OCR Pipeline (Tesseract 5.5.2)** | Tested | ✅ KEEP — Ready for Layer 1 of Vision LLM |

### 1.3 Vision LLM Documentation (Received 2026-04-21)

| Asset | Location | Purpose | Verdict |
|-------|----------|---------|---------|
| **00-overview.md** | Inbound/ | ✅ KEEP — File index, architecture |
| **01-rendering-gates.md** | Inbound/ | ✅ KEEP — 5 gates before rendering |
| **02-label-arrow-rules.md** | Inbound/ | ✅ KEEP — Universal label & arrow rules |
| **03-audit-protocol.md** | Inbound/ | ✅ KEEP — Audit stages, severity, output format |
| **architecture.md** | Inbound/ | ✅ KEEP — 3-layer pipeline, source priority |
| **ocr-setup.md** | Inbound/ | ✅ KEEP — RapidOCR, EasyOCR, Tesseract comparison |
| **opencv-analysis.md** | Inbound/ | ✅ KEEP — Geometric analysis functions |
| **validation.md** | Inbound/ | ✅ KEEP — Confidence thresholds, re-extraction |
| **types/*.md (11 files)** | Inbound/ | ✅ KEEP — Diagram-specific rules |

**Verdict:** ✅ **KEEP AND IMPLEMENT** — This is the solution to our reconstruction deficit.

### 1.4 Issues Encountered & Root Causes

| Issue | Root Cause | Impact | Status |
|-------|------------|--------|--------|
| **Baseline Test Rendering Quality Crisis** | External deconstruction (markdown, not machine-parseable) | ❌ Cannot establish veracity of existing MVP | ✅ Identified in v4.3 |
| **Testing Infrastructure Failure** | Tests checked structure only, not behavior | 3 days lost to START HERE bug | ✅ Resolved (action verification tests) |
| **Framework Coverage Gap** | External analysis only covered 40% of exam content | Missing G5-G8 pathways | 🟡 Partially resolved |
| **Missing Word Problems (20 WP)** | Directory structure inconsistency | Incomplete baseline test | ✅ Resolved |
| **Quality Verification Gap** | No deconstruction → reconstruction loop | Cannot verify reconstruction fidelity | ❌ Not resolved (blocking) |

---

## 2. Focused Scope — 4 Questions Only

### 2.1 Question Selection

| Type | Count | Subtypes |
|-------|-------|----------|
| **Complex Geometry** | 2 | Composite overlap, isometric 3D |
| **Complex Bar Model Word Problem** | 1 | Multi-stage, before-after change |
| **Data Interpretation Question** | 1 | Red herring, multi-source |
| **Total** | **4** | |

**Why 4 Questions:**
- Verify end-to-end quickly (not stuck at generation of 40 questions)
- Test against 12 personas at every stage
- Replicate whole process: Scan → Deconstruct → Generate → Test → Intervene → Transfer
- Can pivot quickly if one question type fails

### 2.2 What These 4 Questions Must Test

| Question Type | Focus Areas |
|-------------|-------------|
| **Complex Geometry (2 Qs)** | - Visual reconstruction fidelity (pixel-precise angles, coordinates, dimensions) <br> - Isometric 3D rendering (30° projection) <br> - Composite overlap (clipping paths, shaded regions) <br> - Reflex angle arcs (proper curves) |
| **Complex Bar Model WP (1 Q)** | - Multi-stage change (before-after) <br> - Bar model segmentation (proportional rendering) <br> - Visual-linguistic alignment (bar matches text) |
| **Data Interpretation (1 Q)** | - Red herring detection (filter irrelevant data) <br> - Chart accuracy (bar/pie/line graphs) <br> - Multi-source integration (tables + charts) |

---

## 3. Process Stages (Iterative with Success Criteria)

### Stage 1: Deconstruction

**Objective:** Convert 4 exam questions from external PDFs to internal, structured YAML.

**Tasks:**
1. Scan/select 4 questions from 5 exam papers
2. Run Vision LLM 3-layer pipeline (OCR + VLM + OpenCV)
3. Generate tagged YAML with confidence scores
4. Verify reconstruction fidelity (compare to original)

**Success Criteria:**
- ✅ **4 questions converted to YAML** — All 4 tagged with confidence scores
- ✅ **Visual fidelity ≤3% deviation** — Reconstructed diagram matches original pixel-precisely
- ✅ **Semantic fidelity 100% match** — Pathway classification matches external analysis
- ✅ **Linguistic fidelity 100% match** — Question text matches original exactly
- ✅ **Completeness 100% match** — No missing elements (shapes, labels, annotations)
- ✅ **Confidence scores ≥0.7 average** — All critical fields have confidence >0.5

**Exit Criteria:** All 4 success criteria met, proceed to Stage 2.

**Blocking Issue:** If any question fails reconstruction fidelity (≥3% deviation), stop and analyze root cause.

**Pivot Decision:**
- **Pass:** Proceed to Stage 2
- **Fail:** Analyze failure, adjust Vision LLM pipeline, repeat Stage 1 with corrected approach
- **Deprecate:** Old approach tagged as `v4.4-stage1-deprecate-001`

---

### Stage 2: Baseline Generation

**Objective:** Generate 4-question baseline test PDF with exam-quality visuals from internal YAML.

**Tasks:**
1. Load 4 YAML files from Stage 1
2. Apply rendering gates (solve first, validate extraction, audience constraint, reason chain, scale plan)
3. Apply label rules (anchored, collision detection, canvas bounds, contrast)
4. Apply geometry rules (isometric 3D, composite overlap, reflex angles)
5. Generate PDF with inline visuals
6. Verify rendering quality (pixel precision, semantic correctness)

**Success Criteria:**
- ✅ **4 questions in PDF** — All 4 questions rendered
- ✅ **Exam-quality visuals** — Pixel-precise angles, coordinates, dimensions
- ✅ **Isometric 3D (if applicable)** — 30° projection, parallel edges stay parallel
- ✅ **Composite overlap (if applicable)** — Clipping paths correct, shaded regions accurate
- ✅ **Label placement correct** — No overlaps, no crossings, minimum proximity achieved
- ✅ **Scale consistency** — Within-panel elements use same scale
- ✅ **PDF generation successful** — No overflow, proper margins, printable quality

**Exit Criteria:** All 4 success criteria met, proceed to Stage 3.

**Blocking Issue:** If any question fails rendering quality, stop and analyze root cause.

**Pivot Decision:**
- **Pass:** Proceed to Stage 3
- **Fail:** Analyze failure, adjust rendering pipeline, repeat Stage 2 with corrected approach
- **Deprecate:** Old approach tagged as `v4.4-stage2-deprecate-001`

---

### Stage 3: Persona Testing

**Objective:** Test baseline test against 12 diverse personas to verify UI/UX works for all student archetypes.

**Persona Definitions (12 Archetypes):**

| Persona | Age | Ability | Learning Style | Tech Savviness | Goal |
|---------|-----|---------|---------------|---------------|------|
| **P1-Early-Reader** | 11 | High average | Visual learner | Low | Test basic recognition accuracy |
| **P2-Struggling-Reader** | 11 | Below average | Text learner | Low | Test support scaffolding |
| **P3-Visual-Spatial** | 12 | High average | Spatial learner | Medium | Test diagram interpretation |
| **P4-Sequential-Thinker** | 11 | High average | Step-by-step | Low | Test reasoning chain support |
| **P5-Quick-Processor** | 12 | High average | Pattern matcher | High | Test speed of feedback |
| **P6-Detail-Oriented** | 11 | High average | Analyzer | Low | Test annotation tools |
| **P7-Social-Learner** | 11 | Average | Collaborative | Medium | Test discussion/help features |
| **P8-Anxious-Test-Taker** | 11 | Average | Test anxiety | Low | Test timer comfort |
| **P9-English-Second-Language** | 11 | Average | Visual learner | Low | Test linguistic clarity |
| **P10-Advanced-Student** | 12 | High average | Self-directed | High | Test challenge mode |
| **P11-Auditory-Kinesthetic** | 12 | Average | Multimodal | Low | Test audio/visual support |
| **P12-Inconsistent-Performer** | 11 | Variable | Mixed | Low | Test engagement features |

**Tasks:**
1. Assign each persona to complete baseline test
2. Track completion time, errors, help requests, frustration points
3. Collect qualitative feedback (interview post-test)
4. Aggregate results by persona archetype

**Success Criteria:**
- ✅ **All 12 personas complete baseline** — 100% completion rate
- ✅ **Average completion time <30 minutes** — Reasonable pacing
- ✅ **≥90% success rate** — Questions answered correctly by ≥10 personas
- ✅ **≤2 critical UX issues** — Blockers preventing completion
- ✅ **≥8 personas report "easy to use"** — Positive experience
- ✅ **No persona reports "completely unusable"** — Zero critical failures

**Exit Criteria:** All 12 personas complete baseline, success criteria met, proceed to Stage 4.

**Blocking Issue:** If ≥3 personas cannot complete or report "completely unusable", stop and analyze UX issues.

**Pivot Decision:**
- **Pass:** Proceed to Stage 4
- **Fail:** Analyze UX failures, adjust frontend, repeat Stage 3 with corrected UI
- **Deprecate:** Old UI tagged as `v4.4-stage3-deprecate-001`

---

### Stage 4: Intervention (Data Manipulation Focus)

**Objective:** Train all 12 personas on pathway types, shadow equations, geometry, and linguistic equivalents.

**Tasks:**
1. Assign each persona to weakest pathway (from baseline test)
2. Provide daily practice problems (5-minute sessions)
3. Track pathway recognition accuracy, articulation quality, solving accuracy
4. Provide triad feedback (pathway ID, articulation, solution)
5. Monitor improvement over time (day-by-day, week-by-week)

**Success Criteria:**
- ✅ **All 12 personas improve pathway recognition** — ≥80% accuracy on trained pathway
- ✅ **All 12 personas achieve Level 2+ articulation** — ≥80% at or above Level 2
- ✅ **≥70% solving accuracy improvement** — From baseline to final day of intervention
- ✅ **≥90% report "helpful feedback"** — Triad feedback useful
- ✅ **≤5 minutes per problem** — Reasonable pacing
- ✅ **No persona reports "stuck without guidance"** — Self-directed learning achieved

**Exit Criteria:** All 12 personas meet improvement criteria, proceed to Stage 5.

**Blocking Issue:** If ≥3 personas do not improve or report "stuck without guidance", stop and analyze intervention design.

**Pivot Decision:**
- **Pass:** Proceed to Stage 5
- **Fail:** Analyze intervention failures, adjust pedagogy, repeat Stage 4 with corrected approach
- **Deprecate:** Old approach tagged as `v4.4-stage4-deprecate-001`

---

### Stage 5: Transfer Test

**Objective:** Measure ramp-up by testing all 12 personas on 4 transfer questions (same types, different parameters).

**Tasks:**
1. Generate 4 transfer questions (same diagram types, different parameters)
2. Assign each persona to complete transfer test
3. Compare baseline performance vs. transfer performance
4. Calculate ramp-up metrics (recognition improvement, articulation improvement, solving improvement)

**Success Criteria:**
- ✅ **All 12 personas complete transfer test** — 100% completion rate
- ✅ **≥80% pathway recognition on trained types** — Transfer of recognition skill
- ✅ **≥70% articulation quality (Level 2+)** — Transfer of articulation skill
- ✅ **≥60% solving accuracy on transfer** — Transfer of solving skill
- ✅ **≥50% improvement on trained pathways** — Ramp-up achieved
- ✅ **≤25 minutes completion time** — Efficient transfer

**Exit Criteria:** All 12 personas complete transfer test, success criteria met, READY FOR LAUNCH.

**Blocking Issue:** If ≥3 personas show negative transfer or zero improvement, stop and analyze overall approach.

**Pivot Decision:**
- **Pass:** LAUNCH PILOT — All stages verified, ready for students
- **Fail:** Analyze transfer failures, adjust entire approach, return to Stage 1 with revised strategy
- **Deprecate:** Old approach tagged as `v4.4-stage5-deprecate-001`

---

## 4. Dynamic Process — Pivot, Track, Deprecate

### 4.1 Version Tags

All decisions tracked with version tags:

| Example Tag | Meaning |
|------------|----------|
| `v4.4-stage1-deprecate-001` | Deconstruction approach failed, replaced with new method |
| `v4.4-stage2-deprecate-001` | Rendering approach failed, replaced with new method |
| `v4.4-stage3-deprecate-001` | UX approach failed, replaced with new design |
| `v4.4-stage4-deprecate-001` | Intervention approach failed, replaced with new pedagogy |
| `v4.4-stage5-deprecate-001` | Transfer test failed, entire approach revised |

### 4.2 Decision Log

All critical decisions documented with rationale:

```yaml
v4.4-decision-001:
  stage: 1 (Deconstruction)
  decision: "Use Vision LLM 3-layer pipeline"
  rationale: "External deconstruction produced markdown, not machine-parseable"
  date: "2026-04-21"
  alternatives_considered: ["Use external markdown directly", "Manually recreate YAML"]
  outcome: "Accepted"

v4.4-decision-002:
  stage: 2 (Baseline Generation)
  decision: "Use rendering gates + label rules + geometry rules"
  rationale: "Basic matplotlib/tikZ insufficient for exam quality"
  date: "2026-04-21"
  alternatives_considered: ["Keep basic rendering", "Use external renders only"]
  outcome: "Accepted"
```

### 4.3 Deprecation Mechanism

When an approach fails:
1. **Tag deprecation** — Add version tag to old approach
2. **Document failure** — Why did it fail? What metrics didn't meet?
3. **Propose pivot** — What alternative approach should we try?
4. **Implement new approach** — Test and verify
5. **Update decision log** — Track all pivots

**Example:**

```yaml
deprecation: v4.4-stage3-deprecate-001
  failed_approach: "Generic UI design"
  failure_reason: "Persona P3-Visual-Spatial reported diagrams were too complex"
  metrics_missed: ["Average completion time >30 minutes", "3 personas reported 'completely unusable'"]
  proposed_pivot: "Add progressive disclosure (simplified diagrams → detailed diagrams)"
  status: "pending"
```

---

## 5. Quality Standard (Reinforced)

### 5.1 Definition

**Quality of reconstruction data must match original exam questions.**

This means:
1. **Visual Fidelity:** Reconstructed diagram looks identical to original (pixel-precise, ≤3% deviation)
2. **Semantic Fidelity:** Reconstructed problem has same meaning as original (100% match on pathway classification)
3. **Linguistic Fidelity:** Reconstructed text matches original exactly (100% match on question text, labels, units)
4. **Completeness:** No missing elements (100% match on shapes, labels, annotations, diagrams)

### 5.2 Improvisation During Transfer Testing

**Requirement:** Deconstructed data must allow improvisation during transfer testing without obvious human errors and be solvable using both visual and text information.

**What This Means:**
- Deconstructed YAML contains **all structural information** (shapes, relationships, coordinates)
- Deconstructed YAML contains **all measurements** (angles, dimensions, line styles)
- Deconstructed YAML contains **all semantic information** (pathway, equation shadow)
- During transfer test, can **modify parameters** (e.g., change side length from 4cm to 6cm)
- Modified YAML still produces **valid, solvable problem**
- Both visual and text information are **sufficient to solve**

**Example Improvisation:**
```yaml
# Original (Stage 1)
shapes:
  - id: square_1
    side_length: {value: 4, unit: "cm"}

# Transfer Test (Stage 5 - Improvised)
shapes:
  - id: square_1
    side_length: {value: 6, unit: "cm"}  # Changed value
    # All other structure, relationships, measurements scale proportionally
```

**Result:** Transfer test problem is valid, solvable, visually correct, semantically consistent.

---

## 6. Intervention Phase Focus (Weeks 2-4)

### 6.1 Primary Focus Areas

**Based on your clarification:**

| Focus Area | Description |
|------------|-------------|
| **Data Manipulation** | Work with deconstructed YAML data during intervention (modify parameters, explore variations) |
| **Downsizing to Nano-Nodes** | Use geometry taxonomy (18 nano-nodes) for targeted training (break problems into smaller skills) |
| **Accurate Visuals** | Render exam-quality diagrams from YAML using rendering gates/rules (pixel-precise) |
| **Teaching Content** | Create Socratic feedback, model articulations, 3-level rubrics (pathway, shadow, geometry, linguistic equivalents) |

### 6.2 Week-by-Week Focus

**Week 2 (Stage 4 - Intervention):**
- Deconstruct 4 questions (Stage 1)
- Generate baseline PDF (Stage 2)
- Test against 12 personas (Stage 3)
- Train all 12 personas on pathway types, shadow equations, geometry, linguistic equivalents
- Focus: Pathway recognition, articulation quality

**Week 3 (Continued Intervention):**
- Downsize to nano-nodes for struggling personas
- Provide targeted practice on specific skills (e.g., "identify right-angle markers", "read dimension lines")
- Track improvement across days

**Week 4 (Final Intervention):**
- Consolidate learning (pathway types mastered vs. still struggling)
- Prepare for transfer test
- Verify improvisation capability (test with modified parameters)

---

## 7. Success Criteria (Per Stage + Overall)

### 7.1 Stage 1: Deconstruction

| Criterion | Target | How to Measure |
|-----------|--------|-----------------|
| **4 questions converted to YAML** | 100% | Count YAML files = 4 |
| **Visual fidelity** | ≤3% deviation | Pixel comparison: Measure shape positions, angles, dimensions |
| **Semantic fidelity** | 100% match | Compare pathway classification to external analysis |
| **Linguistic fidelity** | 100% match | Compare question text to original exactly |
| **Completeness** | 100% match | Count elements: shapes, labels, annotations must match |
| **Confidence scores** | ≥0.7 average | Aggregate all confidence scores |

### 7.2 Stage 2: Baseline Generation

| Criterion | Target | How to Measure |
|-----------|--------|-----------------|
| **4 questions in PDF** | 100% | Count questions in PDF = 4 |
| **Exam-quality visuals** | Pass audit | Apply audit protocol (Stage 0-6) |
| **Isometric 3D (if applicable)** | Pass audit | Measure 30° projection, parallel edges |
| **Composite overlap (if applicable)** | Pass audit | Verify clipping paths, shaded regions |
| **Label placement correct** | Pass audit | No overlaps, no crossings, minimum proximity |
| **Scale consistency** | Pass audit | Within-panel elements use same scale |

### 7.3 Stage 3: Persona Testing

| Criterion | Target | How to Measure |
|-----------|--------|-----------------|
| **All 12 personas complete** | 100% | Count completions = 12 |
| **Average completion time** | <30 minutes | Aggregate timing across all personas |
| **≥90% success rate** | ≥11 personas | Count correct answers |
| **≤2 critical UX issues** | ≤2 blockers | Count blockers preventing completion |
| **≥8 personas report "easy to use"** | ≥8 personas | Qualitative feedback score |
| **No "completely unusable" reports** | 0 personas | Count zero critical failures |

### 7.4 Stage 4: Intervention

| Criterion | Target | How to Measure |
|-----------|--------|-----------------|
| **Pathway recognition improvement** | ≥80% | Compare first day to final day accuracy |
| **Level 2+ articulation** | ≥80% | Count articulations at or above Level 2 |
| **Solving accuracy improvement** | ≥70% | Compare baseline solving % to final day solving % |
| **"Helpful feedback" reports** | ≥90% | Qualitative feedback score |
| **No "stuck without guidance" reports** | 0 personas | Count zero self-reported failures |

### 7.5 Stage 5: Transfer Test

| Criterion | Target | How to Measure |
|-----------|--------|-----------------|
| **All 12 personas complete** | 100% | Count completions = 12 |
| **Pathway recognition transfer** | ≥80% | Count correct pathway IDs on trained types |
| **Level 2+ articulation transfer** | ≥70% | Count articulations at or above Level 2 |
| **Solving accuracy transfer** | ≥60% | Count correct answers on transfer test |
| **Improvement on trained pathways** | ≥50% | Compare baseline to transfer on same pathway types |
| **Completion time** | ≤25 minutes | Aggregate timing across all personas |

### 7.6 Overall Launch Criteria

| Criterion | Target | How to Measure |
|-----------|--------|-----------------|
| **All stages pass** | 100% | Stage 1 ✅ → Stage 2 ✅ → Stage 3 ✅ → Stage 4 ✅ → Stage 5 ✅ |
| **All 12 personas complete all tests** | 100% | Persona completion tracking |
| **Reconstruction fidelity** | ≤3% deviation | Pixel comparison + semantic comparison |
| **Persona diversity** | 12 archetypes | All personas represented and tested |
| **Dynamic process verified** | Pivot/deprecate mechanism tested | At least 1 pivot tested (if needed) |

---

## 8. Deliverables & Timeline

| Deliverable | Owner | Stage | Target | Dependencies |
|-------------|-------|--------|--------|------------|
| **SOR v4.4 (this document)** | Zcaethbot | — | 2026-04-21 | — |
| **Stage 1: 4 Questions to YAML** | Vision LLM + OpenCV + OCR Bureaus | 1 | 2026-04-22 | Vision LLM documentation reviewed |
| **Stage 2: Baseline PDF (4 Questions)** | Logistics Bureau | 2 | 2026-04-23 | Stage 1 complete |
| **Stage 3: Persona Testing (12 Archetypes)** | QA Team | 3 | 2026-04-25 | Stage 2 complete, personas defined |
| **Stage 4: Intervention (Weeks 2-4)** | All Bureaus | 4 | 2026-05-01 | Stage 3 complete |
| **Stage 5: Transfer Test** | QA Team | 5 | 2026-05-05 | Stage 4 complete |
| **Launch Decision** | Sean Foo | — | 2026-05-06 | All stages pass |

**Total Timeline:** 15 days from today (April 21) to launch decision (May 6)

---

## 9. Open Decisions

1. **SOR v4.4 Approach Approval:** Is this focused, iterative approach with 4 questions correct? **Pending decision.**
2. **Persona Definitions:** Are the 12 archetypes diverse and representative? **Pending decision.**
3. **Success Criteria:** Are the per-stage targets appropriate? **Pending decision.**
4. **Launch Date:** Is May 6, 2026 (15 days) appropriate? **Pending decision.**
5. **Quality Standard:** Is "quality of reconstruction must match original" sufficient? **Already confirmed.**
6. **Any Other Requirements:** What else is needed?

---

## 10. Appendices

### Appendix A: Persona Definitions (Detailed)

| Persona | Age | Ability | Learning Style | Tech Savviness | Goals | Pain Points |
|---------|-----|---------|---------------|---------------|------|------------|
| **P1-Early-Reader** | 11 | High average | Visual learner | Low | Test basic recognition, simple feedback | Needs clear visual hierarchy, avoids text-heavy explanations |
| **P2-Struggling-Reader** | 11 | Below average | Text learner | Low | Test support scaffolding | Needs reading support, audio options, simplified language |
| **P3-Visual-Spatial** | 12 | High average | Spatial learner | Medium | Test diagram interpretation | Needs 3D rotation, zoom on diagrams, drag-and-drop tools |
| **P4-Sequential-Thinker** | 11 | High average | Step-by-step | Low | Test reasoning chain support | Needs breakdown of problems, hints at each step |
| **P5-Quick-Processor** | 12 | High average | Pattern matcher | High | Test speed of feedback | Needs instant feedback, minimal waiting, progress bars |
| **P6-Detail-Oriented** | 11 | High average | Analyzer | Low | Test annotation tools | Needs text highlighting, note-taking, zoom on details |
| **P7-Social-Learner** | 11 | Average | Collaborative | Medium | Test discussion/help features | Needs chat/discussion, peer comparison, sharing options |
| **P8-Anxious-Test-Taker** | 11 | Average | Test anxiety | Low | Test timer comfort | Needs timer pause option, no countdown pressure, calming UI |
| **P9-English-Second-Language** | 11 | Average | Visual learner | Low | Test linguistic clarity | Needs simple vocabulary, glossary access, visual aids |
| **P10-Advanced-Student** | 12 | High average | Self-directed | High | Test challenge mode | Needs advanced problems, minimal handholding, exploration tools |
| **P11-Auditory-Kinesthetic** | 12 | Average | Multimodal | Low | Test audio/visual support | Needs audio descriptions, interactive elements, touch interfaces |
| **P12-Inconsistent-Performer** | 11 | Variable | Mixed | Low | Test engagement features | Needs gamification, streak tracking, rewards, reminders |

### Appendix B: v4.3 → v4.4 Migration Guide

| v4.3 Element | v4.4 Update |
|---------------|--------------|
| Scope: 94 questions | Scope: 4 questions (focused) |
| Process: Build entire pipeline, then test | Process: Iterative stages with success criteria at each stage |
| Verification: End-to-end only | Verification: Test against 12 personas at every stage |
| Timeline: 2 weeks, then launch | Timeline: 15 days, then launch decision |
| Dynamic process: Not defined | Dynamic process: Pivot, track, deprecate mechanism |
| Success criteria: Overall only | Success criteria: Per-stage + overall |

### Appendix C: External Data Usage

| External Asset | Usage in v4.4 |
|---------------|-----------------|
| **5 Exam Papers (PDF)** | Source for Vision LLM deconstruction |
| **Deconstructed Questions (Markdown)** | Reference insights only (pathway types, shadow patterns) |
| **Extracted Images (PNG/JPG)** | Input to Vision LLM pipeline |

**What's Discarded:**
- External markdown structure (not machine-parseable)
- External visual notes (text descriptions only, no precision)

### Appendix D: Internal Data Retention

| Internal Asset | Usage in v4.4 |
|---------------|-----------------|
| **Problem Card Structure** | Format for YAML output (extended with confidence scores) |
| **Backend API (19 Endpoints)** | Unchanged, functional |
| **Frontend UI** | Enhanced for persona testing (tracking, analytics) |
| **Geometry Taxonomy** | Unchanged, used for nano-node training |
| **Geometry Rubrics** | Unchanged, used for articulation quality assessment |
| **Playwright Tests** | Extended with persona test scenarios |
| **OCR Pipeline** | Layer 1 of Vision LLM pipeline |
| **Vision LLM Documentation (20 files)** | Implemented as 3-layer pipeline |

---

*This document supersedes SOR v4.3. Approval pending from Sean Foo.*
