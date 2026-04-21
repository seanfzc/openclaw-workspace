# AGENTS.md

## Project: ATOM-SG (v6.2)
## CEO: ATOM
## Pipeline: DUAL-PASS "NEO" PIPELINE

This file defines the agentic army structure, their primary models, and core responsibilities for Project ATOM-SG.

---

### 1. DEPARTMENTS & MODELS

#### Department: LOGISTICS (The Ingestor)
*   **Primary Model:** DUAL-PASS "NEO" PIPELINE Execution
*   **Core Tasks:**
    *   **Pass 1 (OpenDataLoader - Hybrid):** Uses `opendataloader` library. Performs a structural scan, local formula extraction, routes complex tables to the Docling-fast backend, and processes simple text locally for speed.
    *   **Pass 2 (PyMuPDF4LLM):** Uses `pymupdf4llm` library for high-speed Markdown conversion of raw text.
    *   **Pass 3 (The "Clean-Up"):** Raw Markdown is saved to a file (e.g., `raw_extraction.md` in `Raw_Text/` directory) and then processed by DeepSeek-V3.2 with the system instruction: "I am providing a Markdown file from a lightweight parser. Please identify any mathematical formulas and convert them to standard LaTeX $...$ format."

**Example Execution:**
The pipeline is demonstrated with the command: `initialize_neo("Exam_Papers/Rosyth_P6_Algebra.pdf", "Raw_Text/")`

**Priority Thread Logging:**
Metadata related to "Vertical Continuity: $10x+y$" should be logged as the priority thread.

#### Department: PEDAGOGY (The Architect)
*   **Primary Model:** DeepSeek R2 / V4
*   **Core Tasks:**
    *   Atomic Task Analysis.
    *   Vertical Threading (P1→P6): Map every P6 question to P1–P3 "Seed" nodes. Prioritize "Algebraic Continuity" thread.
    *   **System Prompt Update:** "Identify the Visual Template. If the diagram is a 'Comparison Model' but the problem involves 'Internal Transfer', flag as a Logic Conflict for the Auditor."

#### Department: INTEGRITY (Auditor)
*   **Primary Model:** Claude 3.5 / 4.6 Sonnet
*   **Core Tasks:**
    *   Adversarial Audit against official MOE lists.
    *   2026 Compliance Check.
    *   **Topic Filtering (Death List Update):**
        *   DELETE: Speed (Distance, Time, Speed) – Fully moved to Secondary 1.
        *   DELETE: 8-Point Compass (Turns and Compass directions) – Removed from primary assessment.
        *   DELETE: Cells (Science) – Removed from examinable PSLE scope.
        *   SHIFT: Pie Charts & Nets – Now P4 topics. If found in P6 papers, categorize as "Foundational Review," not "Mastery Content."
    *   High-level "Heuristic Reasoning" and "Pedagogical Mapping" (reserved).
    *   **Mandatory Validation:** The Auditor, agent for Integrity, cross-verifies all nodes, ensuring they define all three axes (Linguistic, Visual, Logic). Nodes lacking any of these three axes will be rejected by the Auditor. The Auditor must also reference `linguistic_triggers.md` for keyword detection and seed node mapping, flagging 'Double-Helix Fragmentation' if P1-P3 Seed Node linkage is missing for detected triggers.

#### Department: CREATIVE (The Game Smith)
*   **Primary Model:** DeepSeek V4
*   **Core Tasks:**
    *   Generate Level_Config_JSON.
    *   Generate age-appropriate context (Age 6 vs. Age 11) for logic patterns.

---

### 2. DATA STEWARDSHIP

*   **Folder:** `/Second_Brain/`
*   **Sync Task:** Run Graphify after batches to maintain bidirectional links between P1 seeds and P6 mastery.
*   **Metadata Output:** Store all metadata in Obsidian-ready Markdown with YAML frontmatter.

---

### 4. QUALITY ASSURANCE (QA) & VERIFICATION STANDARD

To ensure high-fidelity output from the NEO Pipeline, all agents must audit processed nodes against the following "Gold Standard" criteria:

A. Logistics (Ingestor) Verification
*   **Structural Integrity:** Markdown must clearly separate "Exam Headers" from "Question Zones."
*   **LaTeX Fidelity:** All mathematical variables (e.g., $x, y$), ratios (e.g., $1:x$), and equations (e.g., $10x + y = 132$) must be enclosed in standard LaTeX inline $...$ or display$$...$$blocks.
*   **Formula Accuracy:** The "Clean-Up" pass by DeepSeek-V3.2 must ensure that multi-variable expressions are not "flattened" into plain text during LaTeX conversion.

B. Pedagogy (Architect) Verification
*   **Vertical Continuity:** Every P6 "Boss" question must explicitly identify its P1-P3 "Seed" node (e.g., mapping Algebraic Units back to Part-Whole Number Bonds).
*   **Triad Axis Mapping:**
    *   **Linguistic:** Must identify at least one of the 12 Heuristics (e.g., Supposition, Repeated Identity, Equal Stage). See `linguistic_triggers.md` for definitions.
    *   **Visual:** Must assign a Visual Stress Score (1-5) based on diagram complexity AND identify one of the 8 Core Templates (Part-Whole, Comparison, Equal Units, Fractional, Common Identity, Constant Difference, Constant Sum, or Gap & Difference). See `visual_templates.md` for definitions.
    *   **Logic:** Must provide the specific MOE 2026 Syllabus code AND ensure linkage to relevant P1-P3 Seed Node as defined in `linguistic_triggers.md`. This includes identifying and flagging 'Logic Conflicts' if a 'Comparison Model' diagram is associated with 'Internal Transfer' problems, as per the Architect's system prompt.

C. Integrity (Auditor) Verification
*   **Bimodal Calibration:** Every node must be tagged as Mode A (Paper 1: Fluency) or Mode B (Paper 2: Heuristic).
*   **Zero-Tolerance Purge:** Any node containing "Speed," "8-Point Compass," or "Cells" must be flagged for immediate deletion to maintain 2026 PSLE compliance.
*   **Auditor Logic Traps:** Must flag "High-Stress" patterns for manual review, adhering to protocols in `linguistic_triggers.md`.
*   **Rule 6: The Inter-Thread Check:** If a node contains triggers from multiple threads (e.g., 'Ratio' AND 'Remainder'), the Auditor must verify that the node has a dual-parentage link covering BOTH threads. If it only links to one thread, the node is REJECTED for 'Structural Blindness.'