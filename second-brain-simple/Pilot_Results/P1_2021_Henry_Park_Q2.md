---
# Core Identification (2026-Aligned)
question_id: "P1_2021_Henry_Park_Q2"
source_file: "2021 P1 Maths Quiz1 Henry Park.txt"
logic_family: "part_whole_operations"  # Addition within 20
grade_level: "P1"
2026_syllabus_check: "Confirmed - Addition within 20"
paper_type: "Paper 1"  # 50% weight
date_extracted: "2026-04-08"
pilot_phase: "Phase 1 - P1 Addition Foundation"

# Enhanced Complexity Scoring (2026-Prioritized)
complexity_scores:
  cognitive_load: 3  # Two groups to count then add
  visual_linguistic_integration: 4  # Must differentiate fruit types/groups
  conceptual_abstraction: 2  # Representational (pictures to numbers)
  contextual_load: 2  # Simple daily context (fruits in box)
  paper_1_fluency_target: 4  # MEDIUM-HIGH - addition facts should be quick
  weighted_score: 3.0  # Grade-adjusted with fluency weight

# MOE-Standard Node Mapping
nodes:
  primary: ["P1-N2-Add-Sub"]  # MOE: Addition and subtraction within 20
  secondary: ["S-PART-WHOLE", "S-VIS-GROUP"]  # Part-whole composition, Visual grouping
  tertiary: ["T-COUNT-ERR"]  # Counting error (double-counting or skipping)
  vertical_evolution: "P6-RATIO-PROP"  # Links to P6 Ratio (parts to whole relationships)

# Logic Trap Detection (2026-Relevant)
logic_traps:
  - type: "hidden_assumption"
    description: "Assumes all fruits are fully visible; image might show partially hidden fruits"
    confidence: 0.6
    intervention: "Prompt: 'Check if any fruits are hiding behind others'"
    game_design_hook: "'Reveal Hidden' mechanic - drag to reveal obscured objects"

# Context Analysis (Singapore-Specific)
context_analysis:
  real_world_context: "daily_life"
  cultural_assumptions: 
    - "Common Singapore fruits (apples, oranges, bananas)"
    - "Box as standard container for storage/transport"
  vocabulary_demand: "low"
  prior_knowledge_required: ["addition facts to 20", "counting objects"]

# Game Design Template (Speed-Focused)
game_design_template:
  mechanic: "Part_Combiner"
  logic: "Player must count two groups of fruits, then combine them to match target total"
  progression_hook: "Increase group sizes, mix similar-looking fruits, reduce counting time"
  level_config: 
    target: 15
    group_a: 8
    group_b: 7
    time_limit: 20  # Seconds
  age_6_adaptation: "Color differentiation (red apples, green apples), audio counting, sum display"
  age_11_adaptation: "Three groups, missing addend problems, algebraic representation (8 + x = 15)"
  boss_level_design: "Include moving fruits or fruits that change groups when tapped"

# Original Question Content
original_question: |
  8+7=15
  There are 15 fruits in the box.

question_type: "Word problem with visual"
answer_key: "15"
visual_description: "Likely shows a box with 8 fruits of one type and 7 of another (from answer key inference)"

# Logical Decomposition
logical_steps:
  - "Step 1: Identify two groups of fruits in the image"
  - "Step 2: Count fruits in first group (8)"
  - "Step 3: Count fruits in second group (7)"
  - "Step 4: Add 8 + 7 = 15"
  - "Step 5: Verify total matches statement 'There are 15 fruits in the box'"

# Part-Whole Analysis
part_whole_structure:
  part_a: "8 fruits (visible group)"
  part_b: "7 fruits (visible group)"
  whole: "15 fruits (total in box)"
  operation: "addition"
  missing_element: "none"  # Complete part-whole representation

# Validation & 2026 Compliance
validation:
  manual_review_required: true
  confidence_score: 0.8
  syllabus_2026_alignment: 
    - "Addition within 20: CONFIRMED (P1-N2-Add-Sub)"
    - "Paper 1 weight: 50% - fluency training REQUIRED"
    - "No deprecated topics: CONFIRMED (not Speed/Cells)"
  cost_tracking:
    vision_api_calls: 0  # Heuristic preferred
    llm_tokens: 135
    heuristic_bypass: true
    cost_per_node: 0.00
    processing_method: "text_keyword_heuristic"

# Linked Questions Detection (2026 Feature)
linked_questions:
  is_linked: false
  scenario_cluster_id: null
  linked_count: 0

# Deprecated Topics Check (2026 Purge)
deprecated_check:
  contains_speed: false
  contains_cells: false
  deprecated_2026: false
  replacement_topic: null

# Pedagogical Analysis

## Cognitive Demand Profile
- **Working Memory:** Moderate (hold two counts while adding)
- **Attention:** Split attention between groups
- **Executive Function:** Systematic counting and addition sequence
- **Visual Processing:** Group differentiation and boundary recognition

## Common Misconceptions
1. **Group boundary confusion:** Miscounting due to unclear group separation
2. **Addition error:** Mistaking 8+7 for other sums (e.g., 8+8=16)
3. **Part-whole reversal:** Thinking subtraction instead of addition
4. **Visual miscount:** Double-counting or skipping objects

## Adaptive Learning Pathway
1. **Prerequisite:** Counting to 20, basic addition facts
2. **Current:** Visual part-whole addition with concrete objects
3. **Next:** Abstract addition without visuals
4. **Advanced:** Missing addend problems (8 + ? = 15)

## Game Mechanics Translation
- **Core loop:** Identify groups → Count → Add → Verify
- **Reward:** Points for accuracy + bonus for speed
- **Progression:** Increase group count, add similar-looking distractors, reduce time
- **Power-ups:** "Group highlighter", "Auto-count", "Time freeze"

## Vertical Evolution to P6
- **P1 foundation:** Concrete addition with visual groups (8 + 7 = 15)
- **P3 development:** Abstract addition, missing addends
- **P6 evolution:** Ratio problems (If 8:7 ratio, total 15, find parts)
- **Algebraic link:** 8x + 7y = 15 (coefficients as group sizes)

---

*Generated as part of ATOM-SG Operation Vertical Thread Pilot*
*Schema Version: 4.0 (Post-QA/QC Brutal Feedback)*
*Processing Date: 2026-04-08*
*Correction: Updated with MOE codes, vertical evolution, and 2026 compliance*