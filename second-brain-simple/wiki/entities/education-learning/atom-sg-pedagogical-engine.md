---
title: ATOM-SG (Pedagogical Engine)
created: 2026-04-08
last_updated: 2026-04-08
source_count: 2
status: active_development
---
# ATOM-SG (Pedagogical Engine)
*Type: project/system*

## Overview
ATOM-SG is a pedagogical engine project (codenamed "Operation Vertical Thread") that creates a "Syllabus Digital Twin" for the Singapore MOE 2026 syllabus. It uses a Logic-First approach to map primary school mathematics concepts (P1→P6) into a vertical knowledge graph with game design templates for adaptive learning.

## Core Components
1. **Vertical Knowledge Graph:** Maps P1 foundational concepts to P6 advanced concepts with prerequisite relationships
2. **Logic-First Analysis:** Focuses on cognitive logic families (part-whole, place value, ratio) rather than assessment items
3. **Game Design Templates:** Translates each logic family into age-appropriate game mechanics
4. **Schema v4.1:** Incorporates "Paper 1 Revolution" (speed-accuracy balance), red herring analysis, scenario clusters

## Current Status (2026-04-08)
- **Pilot Phase:** Validating schema with 5 P1 + 5 P6 questions
- **Schema Version:** v4.1 (Paper 1 Revolution compliance)
- **Technical Approach:** Manual extraction → OCR automation (Tesseract pending)
- **Cost Management:** Implementing Karpathy + Second Brain skill for token efficiency

## Strategic Value - Through Education Lens
**PRIMARY: Game-Based Learning Application**
- **Age 6 Adaptation:** "Logic Trap" concepts become "Boss Levels" in learning games - visual-text mismatches are puzzle challenges to solve
- **Age 11 Adaptation:** "Red Herring Data" training becomes "Data Filter" mini-games where players identify relevant information
- **Vertical Progression:** Children see their learning journey from P1 basics to P6 complexity as an evolving game world
- **Psychology Integration:** Cognitive dissonance traps mapped to game interventions that teach metacognitive skills

**For Professional Contexts:**
- **Aurora Energy:** Complex energy concepts can be mapped with similar vertical progression (basic physics → advanced grid management)
- **Two Alpha Group:** Quantitative reasoning skills can follow similar logic-family progression (basic arithmetic → statistical modeling)
- **Cross-Domain Application:** The Logic-First approach transfers to any domain requiring hierarchical skill development

## Key Innovations
1. **Paper 1 Revolution Compliance:** Accounts for PSLE Paper 1 (50% weight) with time targets and non-calculator constraints
2. **Red Herring Analysis:** Identifies intentionally misleading information in P6 questions for "careless mistake" training
3. **Scenario Cluster Tracking:** Links multiple questions sharing same diagram for "World-Based Levels" game design
4. **Cost-Per-Node Optimization:** Tracks vision/LLM API costs for sustainable scaling

## Implementation Workflow
1. **PDF Processing:** OCR extraction of exam questions (Rosyth 2025 P6 Papers)
2. **Logic Detection:** Classify questions into logic families (algebra, ratio, percentage)
3. **Schema Application:** Apply v4.1 schema with all fields (time targets, distractor density, etc.)
4. **Backward Linking:** Connect P6 concepts to P1 foundations for vertical evolution
5. **Game Design:** Map to appropriate mechanics (Algebraic_Puzzle_Solver, Ratio_Unit_Finder, etc.)

## Cost Management Strategy
*Implementing Karpathy + Second Brain Principles:*
- **Token Efficiency:** Running conversation summaries instead of full history
- **API Optimization:** Manual validation before costly vision/LLM calls
- **Second Brain Integration:** All schema, results, scripts stored in wiki for compounding knowledge
- **Heuristic Rules:** Balance between accuracy (manual) and scale (automated)

## Connections
**Related Concepts:** [[syllabus-mapping-methodology]], [[knowledge-space-theory]], [[game-based-learning-design]]
**Related Entities:** [[Graphify]], [[knowledge-graph-tools]], [[MOE Singapore]]
**Technical Tools:** Python PDF processing, Claude API, Tesseract OCR
**Source References:** Operation Vertical Thread pilot results, schema v4.1 documentation

## Next Actions
1. Complete independent verification of 5 P6 manual questions
2. Install Tesseract OCR for automated extraction
3. Process remaining 5 P6 questions to complete 10-question pilot
4. Generate vertical evolution report (P1→P6 concept mapping)
5. Integrate full results into Second Brain wiki

## Metadata
- **Entity Type:** project/system
- **Domain:** education technology
- **Status:** active_development
- **Priority:** high (operational pilot)
- **Confidence:** medium (validating schema)
- **Next Review:** 2026-04-10 (after pilot completion)