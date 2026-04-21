---
# Core Identification (2026-Aligned)
question_id: "P1_2021_Henry_Park_Q4"
source_file: "2021 P1 Maths Quiz1 Henry Park.txt"
logic_family: "part_whole_operations"  # Subtraction fact
grade_level: "P1"
2026_syllabus_check: "Confirmed - Subtraction within 20"
paper_type: "Paper 1"  # 50% weight - high fluency required
date_extracted: "2026-04-08"
pilot_phase: "Phase 1 - P1 Subtraction Fluency"

# Enhanced Complexity Scoring (2026-Prioritized)
complexity_scores:
  cognitive_load: 2  # Simple fact recall or quick calculation
  visual_linguistic_integration: 1  # Pure symbolic (no visual)
  conceptual_abstraction: 3  # Abstract symbolic manipulation
  contextual_load: 1  # No real-world context
  paper_1_fluency_target: 5  # VERY HIGH - basic facts must be automatic
  weighted_score: 2.4  # Grade-adjusted with heavy fluency weight

# MOE-Standard Node Mapping
nodes:
  primary: ["P1-N2-Add-Sub"]  # MOE: Addition and subtraction within 20
  secondary: ["S-MENTAL-CALC", "S-OPERATION-RECOG"]  # Mental calculation, Operation recognition
  tertiary: ["T-FACT-ERROR"]  # Fact retrieval error (confusing with 17-8=9)
  vertical_evolution: "P6-ALG-EQ"  # Links to P6 Algebraic equations (solving for variables)

# Logic Trap Detection (2026-Relevant)
logic_traps:
  - type: "procedural_overload"
    description: "For students using counting-back strategy, high working memory demand leads to errors"
    confidence: 0.8
    intervention: "Strategy guidance: 'Try make-ten method: 17-7=10, then 10-2=8'"
    game_design_hook: "'Math Gym' mechanic - practice mental strategies under time pressure"

# Context Analysis (Singapore-Specific)
context_analysis:
  real_world_context: "mathematical_abstract"
  cultural_assumptions: 
    - "Arabic numeral system understanding"
    - "Subtraction symbol recognition ('-' means take away)"
  vocabulary_demand: "low"
  prior_knowledge_required: ["subtraction symbol meaning", "number recognition 1-20"]

# Game Design Template (Speed-Focused)
game_design_template:
  mechanic: "Flash_Math"
  logic: "Player must solve basic subtraction facts as quickly as possible"
  progression_hook: "Increase number size, reduce time limit, add visual/auditory distractions"
  level_config: 
    equation: "17 - 9 = ?"
    time_limit: 5  # Seconds (Paper 1 fluency: <5s per basic fact)
    allowed_strategies: ["recall", "make-ten", "counting-back"]
  age_6_adaptation: "Number line visualization, counting aids, immediate feedback"
  age_11_adaptation: "Multiple operations, negative numbers, algebraic thinking"
  boss_level_design: "Combine with visual distractions or require showing work strategy"

# Original Question Content
original_question: |
  17-9=8

question_type: "Pure equation"
answer_key: "8"
visual_description: "None - pure symbolic representation"

# Logical Decomposition
logical_steps:
  - "Step 1: Recognize subtraction operation"
  - "Step 2: Recall subtraction fact 17-9=8 or calculate using preferred strategy"
  - "Step 3: Verify calculation"
  - "Step 4: Provide answer"

# Part-Whole Analysis
part_whole_structure:
  whole: "17"
  part_removed: "9"
  part_remaining: "8"
  operation: "subtraction"
  representation: "symbolic_only"

# Strategy Analysis
solution_strategies:
  - "Recall: Memory of subtraction fact (optimal for fluency)"
  - "Counting back: Count 9 backwards from 17 (working memory intensive)"
  - "Make ten: 17-7=10, then 10-2=8 (efficient strategy)"
  - "Addition reversal: 9+8=17, so 17-9=8 (fact family understanding)"
  - "Number line: Visualize movement on number line (visual strategy)"

# Validation & 2026 Compliance
validation:
  manual_review_required: false
  confidence_score: 0.95
  syllabus_2026_alignment: 
    - "Subtraction within 20: CONFIRMED (P1-N2-Add-Sub)"
    - "Paper 1 weight: 50% - AUTOMATICITY required (<5s per fact)"
    - "No deprecated topics: CONFIRMED (not Speed/Cells)"
  cost_tracking:
    vision_api_calls: 0  # Heuristic preferred
    llm_tokens: 100
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

# Fluency Training Criticality
fluency_analysis: |
  This question type represents the CORE of Paper 1 fluency requirements.
  With Paper 1 now 50% of PSLE, students must achieve automaticity (<5 seconds) on basic facts.
  Game design MUST prioritize speed while maintaining accuracy.
  Progression: Accuracy → Accuracy+Speed → Speed under pressure → Speed with distractions.

# Pedagogical Insights

## Cognitive Demand Profile
- **Working Memory:** Low (if fact recall) to Moderate (if counting strategy)
- **Attention:** Focused on symbolic manipulation
- **Executive Function:** Strategy selection and execution
- **Mathematical Processing:** Arithmetic fact retrieval or calculation efficiency

## Common Misconceptions
1. **Fact confusion:** Mistaking 17-9 for 17-8=9 or 18-9=9
2. **Operation confusion:** Misreading '-' as '+' (17+9=26)
3. **Place value error:** Treating 17 as 1+7=8 then 8-9=? (impossible)
4. **Counting errors:** Miscounting when using counting-back strategy

## Adaptive Learning Pathway
1. **Prerequisite:** Number recognition, counting skills
2. **Current:** Subtraction facts within 20 with strategy development
3. **Next:** Subtraction with regrouping, larger numbers
4. **Advanced:** Algebraic thinking, missing variable problems

## Game Mechanics Translation
- **Core loop:** See equation → Calculate → Input answer → Feedback
- **Reward:** Points for accuracy + bonus for speed + super bonus for strategy efficiency
- **Progression:** Increase number size, reduce time, add multiple operations, add distractions
- **Power-ups:** "Strategy hint", "Number line", "Fact checker", "Time freeze"

## Strategy Development Focus
- **Early P1:** Counting-based strategies with visual aids
- **Mid P1:** Make-ten strategies and fact families
- **Late P1:** Automaticity and fact recall (Paper 1 ready)
- **P6:** Algebraic reasoning and mental math efficiency

## Vertical Evolution to P6
- **P1 foundation:** Basic subtraction facts (17-9=8)
- **P3 development:** Subtraction with regrouping, 3-digit numbers
- **P6 evolution:** Algebraic equations (solve for x: 17 - x = 8)
- **Real-world link:** Negative numbers, decimal subtraction

---

*Generated as part of ATOM-SG Operation Vertical Thread Pilot*
*Schema Version: 4.0 (Post-QA/QC Brutal Feedback)*
*Processing Date: 2026-04-08*
*Correction: Updated with MOE codes, vertical evolution, and 2026 compliance*