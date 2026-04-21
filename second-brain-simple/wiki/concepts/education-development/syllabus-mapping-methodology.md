---
title: Syllabus Mapping Methodology
created: 2026-04-08
last_updated: 2026-04-08
source_count: 3
status: draft
---
# Syllabus Mapping Methodology
*Framework for mapping assessment items to granular syllabus skills to create knowledge graphs for personalized learning*

## Core Idea
Syllabus mapping is the systematic process of decomposing official curriculum documents into granular skills, then linking assessment items (exam questions, quizzes, exercises) to those skills to create a prerequisite graph that reveals learning pathways, identifies high-frequency test areas, and surfaces untested but important competencies. [Source: 2026-04-07-p1-maths-syllabus-mapping.md]

## Key Components
1. **Syllabus Decomposition:** Breaking curriculum statements into atomic, assessable skills with unique identifiers (e.g., S001: "Counting objects to 10"). [Source: 2026-04-07-p1-maths-syllabus-mapping.md]
2. **Assessment Processing:** Extracting questions from PDFs, identifying visual types, parsing answer keys, and normalizing question text through OCR and layout analysis. [Source: raw/exam-questions/sample_summary.json]
3. **Skill–Question Mapping:** Using keyword matching, LLM semantic analysis, or manual tagging to link each question to one or more syllabus skills. [Source: 2026-04-07-p1-maths-syllabus-mapping.md]
4. **Graph Construction:** Building nodes (skills, questions, papers) and edges (tests, prerequisites, co-occurrence) to visualize the assessment ecosystem. [Source: 2026-04-07-p1-maths-syllabus-mapping.md]
5. **Gap Analysis:** Identifying skills that are over-tested, under-tested, or missing from assessments, informing curriculum design and game-based learning priorities. [Source: 2026-04-07-p1-maths-syllabus-mapping.md]

## Applications - With Education as Primary Lens
**PRIMARY: Game-Based Learning Design**
- **Age 6 Adaptation:** Turn the syllabus map into a "learning treasure map" where each skill is a treasure island. Children sail between islands (skills) by completing mini-games, with the map showing their progress. [Source: 2026-04-07-p1-maths-syllabus-mapping.md]
- **Age 11 Adaptation:** Frame as a "tech skill tree" (like video‑game ability trees) where players unlock advanced skills by mastering prerequisites. Show statistical data (how many peers have unlocked each skill) to add social motivation. [Source: 2026-04-07-p1-maths-syllabus-mapping.md]
- **Game Mechanics:** Use the prerequisite graph as the core progression system: players cannot attempt "Addition word problems" until they've unlocked "Adding with pictures" and "Reading number words". Visual feedback shows skill connections. [Source: 2026-04-07-p1-maths-syllabus-mapping.md]
- **Psychology & Engagement:** Make learning progression **visible and celebrate‑able**. Children see exactly how today's practice ("Counting objects") leads to tomorrow's goal ("Adding numbers"). This reduces ambiguity and builds growth mindset. [Source: 2026-04-07-p1-maths-syllabus-mapping.md]

**Energy Sector Use:** Map energy competency frameworks (technical, regulatory, commercial) to training materials and real‑world projects. New hires see a personalized "energy skill tree" showing which competencies they need for their role, with recommended learning resources linked to each node. [Source: 2026-04-07-p1-maths-syllabus-mapping.md]
**Fintech/AI Use:** Create quantitative finance skill trees connecting statistics, programming, and financial modeling. Team members diagnose their own knowledge gaps and follow personalized upskilling paths, accelerating time‑to‑productivity in fast‑moving quantitative environments. [Source: 2026-04-07-p1-maths-syllabus-mapping.md]
**Personal Development:** Demonstrate **explicit skill mapping** to your boys: show them that learning is not random but a structured journey with clear milestones. This metacognitive awareness ("knowing what you need to learn") is itself a critical future skill. [Source: 2026-04-07-p1-maths-syllabus-mapping.md]

## Limitations & Criticisms
- **Granularity Trade‑off:** Over‑decomposition creates hundreds of micro‑skills that may be impractical to assess individually; under‑decomposition misses nuance.
- **Mapping Subjectivity:** Different raters may assign the same question to different skills, requiring consensus protocols or LLM‑assisted standardization.
- **Static vs. Dynamic:** Syllabi evolve, but mapped graphs become outdated without continuous updating.
- **Cultural Bias:** Official syllabi reflect national educational priorities that may not align with future‑focused skills (creativity, systems thinking).

## Implementation Guide
**Step 1: Syllabus Decomposition**
- Obtain official curriculum documents (MOE, national standards)
- Break into atomic skills (one learning objective per skill)
- Assign unique IDs and categorize (number sense, operations, measurement, etc.)
- Identify prerequisite relationships (which skills must come before others)

**Step 2: Assessment Corpus Collection**
- Gather exam papers, quizzes, worksheets (PDF preferred)
- Extract text and images using OCR/pdf‑plumber
- Parse answer keys and scoring rubrics
- Normalize question formatting

**Step 3: Automated Mapping**
- Build keyword library for each skill
- Use LLM semantic matching for ambiguous cases
- Apply confidence scores (high/medium/low) to each question–skill link
- Handle multi‑skill questions (one question tests multiple skills)

**Step 4: Graph Construction & Analysis**
- Create nodes: skills, questions, papers
- Create edges: question‑tests‑skill, skill‑prerequisite‑skill, paper‑contains‑question
- Calculate metrics: skill frequency, prerequisite chains, school‑level patterns
- Visualize with D3.js, Graphviz, or Obsidian graph view

**Step 5: Game‑Based Learning Design**
- Translate skill graph into game progression system
- Design mini‑games for each skill category
- Implement adaptive difficulty based on player performance
- Add social features (skill mastery sharing, peer comparisons)

**Success Metrics:**
- **Coverage:** Percentage of syllabus skills represented in assessments
- **Accuracy:** Question‑skill mapping precision (human‑validated)
- **Utility:** Teachers/students report the map helps identify learning gaps
- **Engagement:** Children spend more time on skill‑practice games when progression is visible

## Connections
**Related Concepts:** [[prerequisite‑learning]], [[adaptive‑assessment]], [[knowledge‑graph‑construction]], [[game‑based‑learning‑design]]
**Supporting Entities:** [[Graphify]], [[knowledge‑graph‑tools]], [[MOE Singapore]]
**Source References:** [[2026-04-07-p1-maths-syllabus-mapping]], [[raw/exam-questions/sample_summary.json]]

## Metadata
- **Concept Type:** methodology
- **Domain:** education
- **Maturity:** established
- **Confidence:** high
- **Last Reviewed:** 2026-04-08