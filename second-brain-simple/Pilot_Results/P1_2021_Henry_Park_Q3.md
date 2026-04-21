---
# Core Identification (2026-Aligned)
question_id: "P1_2021_Henry_Park_Q3"
source_file: "2021 P1 Maths Quiz1 Henry Park.txt"
logic_family: "part_whole_operations"  # Subtraction within 20
grade_level: "P1"
2026_syllabus_check: "Confirmed - Subtraction within 20"
paper_type: "Paper 1"  # 50% weight
date_extracted: "2026-04-08"
pilot_phase: "Phase 1 - P1 Subtraction Foundation"

# Enhanced Complexity Scoring (2026-Prioritized)
complexity_scores:
  cognitive_load: 3  # Context understanding + calculation
  visual_linguistic_integration: 4  # Must interpret scenario from text/visual
  conceptual_abstraction: 2  # Representational (real-world to math)
  contextual_load: 3  # Family relationship understanding required
  paper_1_fluency_target: 3  # MODERATE - word problem takes more time
  weighted_score: 3.1  # Grade-adjusted with fluency weight

# MOE-Standard Node Mapping
nodes:
  primary: ["P1-N2-Add-Sub"]  # MOE: Addition and subtraction within 20
  secondary: ["S-PART-WHOLE", "S-CONTEXT-INTERP"]  # Part-whole decomposition, Context interpretation
  tertiary: ["T-OPERATION-CONF"]  # Operation confusion (addition vs subtraction)
  vertical_evolution: "P6-ALG-EQ"  # Links to P6 Algebraic equations (15 - x = 9)

# Logic Trap Detection (2026-Relevant)
logic_traps:
  - type: "cultural_assumption"
    description: "Assumes understanding of 'father gave her' as subtraction context (giving reduces quantity)"
    confidence: 0.7
    intervention: "Prompt: 'If father GIVES cupcakes, does he have more or less?'"
    game_design_hook: "'Context Detective' mechanic - identify operation from real-world scenario"

# Context Analysis (Singapore-Specific)
context_analysis:
  real_world_context: "family"
  cultural_assumptions: 
    - "Nuclear family structure (father-child)"
    - "Cupcakes as desirable treat in Singapore"
    - "Gifting reduces giver's quantity (cultural norm)"
  vocabulary_demand: "medium"
  prior_knowledge_required: ["subtraction concepts", "family relationship terms", "gifting context"]

# Game Design Template (Speed-Focused)
game_design_template:
  mechanic: "Context_Solver"
  logic: "Player must interpret word problem, identify operation (subtraction), then calculate missing value"
  progression_hook: "Vary scenarios (giving, losing, sharing), object types, relationship contexts"
  level_config: 
    starting_total: 15
    amount_given: 6
    remaining: 9
    time_limit: 25  # Seconds (word problem takes longer)
  age_6_adaptation: "Visual removal animation, audio narration, simple family terms"
  age_11_adaptation: "Multiple steps, mixed operations, generate own word problems"
  boss_level_design: "Include ambiguous scenarios where operation isn't explicitly stated"

# Original Question Content
original_question: |
  15-6=9
  Her father gave her 9 cupcakes.

question_type: "Word problem with visual"
answer_key: "9"
visual_description: "Likely shows 15 cupcakes initially, with 6 being given away/removed"

# Logical Decomposition
logical_steps:
  - "Step 1: Understand scenario - father giving cupcakes to child"
  - "Step 2: Identify starting quantity (15 cupcakes)"
  - "Step 3: Identify quantity given (6 cupcakes)"
  - "Step 4: Calculate remaining: 15 - 6 = 9"
  - "Step 5: Verify answer matches statement 'Her father gave her 9 cupcakes'"

# Part-Whole Analysis
part_whole_structure:
  whole: "15 cupcakes (initial total)"
  part_removed: "6 cupcakes (given away)"
  part_remaining: "9 cupcakes (with father/remaining)"
  operation: "subtraction"
  context_cue: "gave her" indicates removal/reduction

# Validation & 2026 Compliance
validation:
  manual_review_required: true
  confidence_score: 0.85
  syllabus_2026_alignment: 
    - "Subtraction within 20: CONFIRMED (P1-N2-Add-Sub)"
    - "Paper 1 weight: 50% - word problem fluency training"
    - "No deprecated topics: CONFIRMED (not Speed/Cells)"
  cost_tracking:
    vision_api_calls: 0  # Heuristic preferred
    llm_tokens: 160
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

# Critical Analysis Notes
analysis_notes: |
  This question tests both mathematical computation (15-6=9) AND contextual understanding.
  Key skill: Translating real-world scenario ("gave her") to mathematical operation (subtraction).
  Common error: Students may interpret "gave her" as addition (receiving increases).
  Cultural note: Assumes understanding of family relationships and gifting norms.

# Pedagogical Insights

## Cognitive Demand Profile
- **Working Memory:** Moderate (hold scenario details while calculating)
- **Linguistic Processing:** Interpret "gave her" as subtraction cue
- **Executive Function:** Parse word problem, identify operation, execute calculation
- **Contextual Understanding:** Family relationships and gifting norms

## Common Misconceptions
1. **Operation confusion:** "Gave" interpreted as addition (child receives = increase)
2. **Quantity reversal:** Thinking 15-9=6 instead of 15-6=9
3. **Context misreading:** Missing that father is giver, not receiver
4. **Visual miscount:** Incorrect initial count of cupcakes

## Adaptive Learning Pathway
1. **Prerequisite:** Counting to 20, basic subtraction facts
2. **Current:** Contextual subtraction with familiar objects
3. **Next:** Subtraction with larger numbers, multiple steps
4. **Advanced:** Missing subtrahend problems (15 - ? = 9)

## Game Mechanics Translation
- **Core loop:** Read scenario → Identify operation → Calculate → Verify
- **Reward:** Points for accuracy + bonus for identifying contextual cues
- **Progression:** Increase scenario complexity, add distractors, reduce explicit cues
- **Power-ups:** "Context hint", "Operation checker", "Visual removal animation"

## Vertical Evolution to P6
- **P1 foundation:** Concrete subtraction with real-world context
- **P3 development:** Multi-step word problems, mixed operations
- **P6 evolution:** Algebraic equations (15 - x = 9, solve for x)
- **Real-world link:** Percentage decrease, profit/loss scenarios

---

*Generated as part of ATOM-SG Operation Vertical Thread Pilot*
*Schema Version: 4.0 (Post-QA/QC Brutal Feedback)*
*Processing Date: 2026-04-08*
*Correction: Updated with MOE codes, vertical evolution, and 2026 compliance*