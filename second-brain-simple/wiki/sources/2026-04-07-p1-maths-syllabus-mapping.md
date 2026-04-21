---
title: Primary 1 Maths Syllabus Mapping Analysis
created: 2026-04-07
last_updated: 2026-04-07
source_count: 3
status: draft
---
# Primary 1 Maths Syllabus Mapping Analysis
*Knowledge graph mapping of 10 Singapore Primary 1 Maths exam papers to the MOE syllabus, identifying most-tested skills, prerequisite chains, and gaps for game‑based learning design.*

## Executive Summary
This analysis maps 10 representative Primary 1 Maths exam papers (2021‑2025 from schools including Henry Park, Raffles Girls, SCGS, Ai Tong, Maha Bodhi, and MGS) against the official MOE Primary 1 Mathematics syllabus. Using text extraction and keyword matching, 83 granular syllabus skills were identified and matched to papers, creating a knowledge graph with **93 nodes** (83 skills + 10 papers) and **210 edges** (46 test‑relationships, 88 prerequisite relationships). Key findings: (1) **71% of syllabus skills** (59 of 83) appear in at least one paper, with "Counting objects to 10", "Reading and writing numerals 0‑10", and "Addition with pictures" being most frequently tested; (2) **24 skills were untested** in the sample, including "Division as sharing equally", "Measuring length using standard units (cm)", and "Interpreting tally charts"; (3) Papers show clear **topic clustering**—Henry Park's quizzes focus on Numbers to 10/20, while Raffles Girls' reviews cover broader ranges including Addition/Subtraction within 100; (4) The **prerequisite graph** reveals a clear learning progression from number sense to basic operations to measurement/geometry. For Sean's education‑first mission, this map identifies **high‑impact game targets** (most‑tested skills), **learning‑path design** (prerequisite chains), and **gap‑filling opportunities** (untested skills that still matter for holistic understanding).

## Key Insights
- **Syllabus coverage is broad but uneven** – 59 of 83 skills (71%) appear in at least one paper, but frequency varies widely from 1 to 7 papers per skill. [Source: syllabus_analysis_report.md]
- **Foundation skills dominate** – "Counting objects to 10", "Reading and writing numerals 0‑10", and "Adding with pictures" are tested by 6‑7 papers each, confirming their role as **gateway competencies**. [Source: knowledge_graph.json]
- **School‑specific emphases exist** – Henry Park papers consistently test **Numbers to 10/20**; Raffles Girls includes **Addition/Subtraction within 100**; SCGS emphasizes **word problems**. This suggests **different pedagogical approaches** across schools. [Source: paper_topic_analysis.json]
- **Prerequisite chains are mostly linear** – The syllabus implies a clear progression: Numbers → Addition/Subtraction → Multiplication/Division → Measurement → Geometry → Data Analysis. Games can **make this progression visible and engaging**. [Source: knowledge_graph.json]
- **Untested skills reveal assessment gaps** – 24 skills not appearing in any paper include practical applications like "Measuring with standard units", "Division as sharing", and "Interpreting tally charts". These may be **under‑assessed but still educationally valuable**. [Source: syllabus_analysis_report.md]

## Strategic Implications
**PRIMARY LENS: How this transforms your sons' education (11 & 6)**
- **Game‑Based Learning Application:** Create a "Skill‑Tree Explorer" game where players (your boys) unlock syllabus skills like video‑game abilities. The knowledge graph becomes the **game map**—nodes are unlockable skills, edges are prerequisite gates, papers are "boss levels" testing skill clusters. Visual progression shows how "Counting objects to 10" unlocks "Adding with pictures".
- **Critical Thinking Development:** Design games that teach **metacognitive mapping**—kids learn to identify which skills they've mastered vs. which need work, using the same graph structure. A "Learning GPS" game could plot routes from current skill to target skill, showing required prerequisite steps.
- **Future Skills Connection:** This analysis models **system thinking**—seeing connections between concepts rather than isolated facts. Games that make these connections explicit (e.g., "How does telling time connect to counting by fives?") build **integrative cognitive skills** valuable for complex problem‑solving.
- **Psychology & Engagement:** Use the **prerequisite chain as a progression system** with frequent small wins (each skill mastered). For a 6‑year‑old, represent skills as "learning LEGO blocks" that snap together; for an 11‑year‑old, frame it as a "tech‑skill tree" with branching specializations.

**For Aurora Energy Research:** The mapping methodology (documents → skills → graph) can be adapted for **energy competency frameworks**. New hires could use a game that maps their existing knowledge against required energy‑sector skills, identifying gaps and personalized learning paths.
**For Two Alpha Group:** Quantitative skill trees (statistics, programming, financial modeling) could be mapped similarly. An adaptive learning game could diagnose team members' quantitative foundations and prescribe targeted upskilling, **accelerating time‑to‑productivity**.
**Personal Development:** Demonstrating **explicit skill mapping** to your boys shows that learning is not random—it's a **structured journey** with clear milestones. This reduces anxiety ("I don't know where to start") and builds confidence ("I know exactly what to learn next").

## Detailed Analysis
### Methodology
1. **Syllabus Decomposition:** MOE Primary 1 Mathematics syllabus was broken into 83 granular skills across 6 categories (Whole Numbers, Addition/Subtraction, Multiplication/Division, Measurement, Geometry, Data Analysis).
2. **Paper Processing:** 10 PDF exam papers were converted to text, section headers extracted, and content analyzed.
3. **Skill‑Paper Mapping:** Keyword matching linked paper content to syllabus skills; headers like "NUMBERS TO 100" directly mapped to subcategories.
4. **Graph Construction:** Created nodes (skills, papers), edges (paper‑tests‑skill, skill‑prerequisite‑skill), with weights based on frequency and confidence.
5. **Visualization:** Interactive D3.js graph allows exploration of connections.

### Key Findings
#### Most Tested Skills (≥4 papers)
1. **S001: Counting objects to 10** (7 papers)
2. **S002: Reading and writing numerals 0‑10** (6 papers)  
3. **S021: Adding with pictures** (6 papers)
4. **S004: Comparing numbers within 10** (5 papers)
5. **S022: Adding using number bonds** (5 papers)

#### School‑Level Patterns
- **Henry Park:** Focused on foundational skills (Numbers to 10/20, basic addition), frequent "Quiz" format suggests **formative assessment** approach.
- **Raffles Girls:** Broader coverage including Addition/Subtraction within 100, "Review Assessment" format suggests **cumulative testing**.
- **SCGS:** Emphasis on **word problems** and application, not just computation.
- **Ai Tong/Maha Bodhi:** Mix of foundation and application, with visual/spatial concepts in later years.

#### Prerequisite Structure
The graph reveals **three main learning paths**:
1. **Number Sense Path:** Counting → Numeral recognition → Comparing → Ordering → Place value
2. **Operations Path:** Addition (pictures → facts → word problems) → Subtraction → Mixed operations
3. **Application Path:** Measurement (length → time → money) → Geometry (2D → 3D shapes) → Data (graphs → charts)

#### Gaps & Opportunities
- **Untested practical skills:** Measuring with cm, money transactions, tally charts—these are **life‑ready competencies** that could be emphasized in game design.
- **Limited multiplicative reasoning:** Multiplication/Division appear in only 2 papers—a potential **enrichment area** for advanced 6‑year‑olds or 11‑year‑olds.
- **Visual‑spatial under‑represented:** Shape composition and patterns appear sparsely—**game‑friendly topics** with high engagement potential.

## Connections
**Related Entities:** [[Graphify]], [[knowledge‑graph‑tools]], [[MOE Singapore]]
**Related Concepts:** [[syllabus‑mapping]], [[prerequisite‑learning]], [[adaptive‑assessment]], [[game‑based‑learning‑design]]
**Source Materials:** `raw/articles/syllabus_analysis_report.md`, `p1_sample/knowledge_graph.json`, `p1_sample/syllabus_graph.html`

## Metadata
- **Source:** `p1_sample/syllabus_analysis_report.md`, `p1_sample/knowledge_graph.json`
- **Ingested:** 2026-04-07
- **Category:** education
- **Confidence:** high
- **Tags:** #primary‑maths #syllabus‑mapping #knowledge‑graph #game‑based‑learning #prerequisite‑analysis
- **Project:** Education
- **Priority:** high
- **Review Date:** 2026-10-07