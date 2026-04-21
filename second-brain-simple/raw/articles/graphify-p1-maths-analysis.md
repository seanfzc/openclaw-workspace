# Graphify Analysis: Primary 1 Maths Exam Papers
*Knowledge graph extraction of 10 representative Primary 1 Maths exam papers (2021-2025) from Singapore schools.*

## Overview
Graphify was used to analyze 10 Primary 1 Maths exam papers from schools including Henry Park, Raffles Girls, SCGS, Ai Tong, Maha Bodhi, and MGS. The pipeline extracted text from PDFs, identified topics and concepts, built a knowledge graph with 49 nodes and 385 edges, clustered into 10 communities, and identified god nodes (most-connected concepts).

## Key Findings

### 1. Core Concepts (God Nodes)
The most connected concepts across all papers:
- **School** – Appears in every paper's metadata
- **Term** – Term indicators (Term 2, etc.)
- **Level** – Grade level references
- **Subject** – Mathematics subject designation
- **Mathematics** – The subject itself
- **Addition And Subtraction Within** – Found in multiple papers
- **Numbers To** – Numbers to 100, etc.

### 2. Topic Clusters (10 Communities)
- **Community 0**: School metadata, administrative labels
- **Community 1**: Basic arithmetic (addition, subtraction)
- **Community 2**: Number sense (numbers to 100, place value)
- **Community 3**: Assessment formats (quiz, test, review)
- **Community 4**: Year groupings (2021, 2022, etc.)
- **Community 5**: Answer key patterns
- **Community 6**: Measurement concepts
- **Community 7**: Word problem structures
- **Community 8**: Visual/spatial concepts
- **Community 9**: Time/money concepts

### 3. Surprising Connections
- **Math ↔ Addition And Subtraction Within** – The term "Math" (abbreviation) strongly connects to specific arithmetic operations
- **Math ↔ Numbers To** – Number range concepts tightly linked to subject abbreviation
- **Mathematics ↔ Math** – Formal vs informal subject naming co-occur

### 4. Structural Insights
- **School-specific patterns**: Henry Park papers show consistent "Quiz" terminology; Raffles Girls uses "Review Assessment"
- **Year progression**: 2024-2025 papers include more visual/spatial concepts than earlier years
- **Assessment types**: "Quiz" vs "Test" vs "Review" form distinct clusters
- **Concept granularity**: Topics extracted are relatively coarse (e.g., "Addition And Subtraction Within" rather than "addition within 10" vs "addition within 20")

## Limitations of This Analysis
- **Text extraction quality**: Some PDFs had low-quality OCR, resulting in sparse text
- **Topic granularity**: Without semantic LLM extraction, topics are filename/heading-based
- **No prerequisite mapping**: Graph doesn't show which concepts build on others
- **Missing answer patterns**: Student answer patterns not analyzed

## Source Files Analyzed
1. 2021 P1 Maths Quiz1 Henry Park
2. 2021 P1 Maths Revisions Mgs
3. 2022 P1 Maths Review Assessment 2 Raffles Girls
4. 2022 P1 Maths Test 6 Scgs
5. 2023 P1 Maths Term 2 Mini Test Ai Tong
6. 2023 P1 Maths Topical Quiz 2 Henry Park
7. 2024 P1 Maths Quiz 1 Henry Park
8. 2024 P1 Maths Review 1 Maha Bodhi
9. 2025 P1 Maths Quiz 2 Henry Park
10. 2025 P1 Maths Quiz 3 Henry Park

## Graphify Output Files
- `graph.json` – Complete knowledge graph (GraphRAG-ready)
- `graph.html` – Interactive visualization
- `obsidian/` – Obsidian vault with one note per node
- Generated: 2026-04-07

---
*Analysis performed using Graphify v3 (Python 3.10).*