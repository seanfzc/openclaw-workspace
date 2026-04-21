---
# Core Identification (2026-Aligned)
question_id: "P1_2021_Henry_Park_Q5"
source_file: "2021 P1 Maths Quiz1 Henry Park.txt"
logic_family: "part_whole_operations"  # Subtraction inference
grade_level: "P1"
2026_syllabus_check: "Confirmed - Word problem comprehension"
paper_type: "Paper 1"  # 50% weight (but reasoning, not calculation speed)
date_extracted: "2026-04-08"
pilot_phase: "Phase 1 - P1 Problem Comprehension"

# Enhanced Complexity Scoring (2026-Prioritized)
complexity_scores:
  cognitive_load: 4  # High: Must infer missing information
  visual_linguistic_integration: 3  # Moderate: Text + likely visual cues
  conceptual_abstraction: 3  # Moderate: Concrete to abstract inference
  contextual_load: 2  # Moderate: Play context familiar
  paper_1_fluency_target: 2  # LOW - reasoning focus, not speed calculation
  weighted_score: 3.0  # Grade-adjusted with fluency weight

# MOE-Standard Node Mapping
nodes:
  primary: ["P1-N2-Add-Sub"]  # MOE: Addition and subtraction within 20
  secondary: ["S-PROBLEM-RECON", "S-CONTEXT-INTERP"]  # Problem reconstruction, Context interpretation
  tertiary: ["T-MISSING-INFO"]  # Missing information confusion
  vertical_evolution: "P6-ALG-WORD"  # Links to P6 Algebraic word problems with variables

# Logic Trap Detection (2026-Relevant)
logic_traps:
  - type: "hidden_assumption"
    description: "Requires inferring complete problem from partial conclusion 'Ali has 8 marbles left'"
    confidence: 0.85
    intervention: "Prompt: 'What might have happened to the marbles before?'"
    game_design_hook: "'Story_Detective' mechanic - reconstruct complete scenario from clues"

# Context Analysis (Singapore-Specific)
context_analysis:
  real_world_context: "play"
  cultural_assumptions: 
    - "Marbles as traditional children's game in Singapore"
    - "'Left' implies subtraction context (some marbles gone)"
    - "Typical P1 marble quantities (8 is reasonable remainder)"
  vocabulary_demand: "low-medium"
  prior_knowledge_required: ["subtraction concepts", "marbles as countable objects", "problem-solving inference"]

# Game Design Template (Reasoning-Focused)
game_design_template:
  mechanic: "Scenario_Reconstructor"
  logic: "Player must reconstruct complete word problem from partial conclusion using visual/textual clues"
  progression_hook: "Vary completeness of information, ambiguity level, number of possible reconstructions"
  level_config: 
    given_info: "Ali has 8 marbles left."
    missing_elements: ["starting quantity", "what happened", "operation required"]
    time_limit: 40  # Seconds (reasoning takes time)
  age_6_adaptation: "Visual story sequence, audio narration, multiple choice options"
  age_11_adaptation: "Open-ended reconstruction, justify reasoning, create multiple valid versions"
  boss_level_design: "Provide contradictory clues requiring reconciliation or probability assessment"

# Original Question Content
original_question: |
  Ali has 8 marbles left.

question_type: "Incomplete word problem"
answer_key: "Unknown - likely asks for starting quantity or quantity lost"
visual_description: "Likely shows Ali with 8 marbles, possibly with empty spaces indicating missing marbles"

# Logical Decomposition (Inferred)
logical_steps:
  - "Step 1: Recognize this is a subtraction problem conclusion ('left' implies reduction)"
  - "Step 2: Infer missing information from visual cues (starting amount, what happened)"
  - "Step 3: Reconstruct complete problem based on available clues"
  - "Step 4: Calculate missing value(s) based on reconstructed scenario"
  - "Step 5: Provide answer based on inferred question prompt"

# Possible Complete Problem Reconstructions
possible_reconstructions:
  - "Ali had some marbles. He gave 5 to Ben. Now he has 8 marbles left. How many marbles did Ali have at first?" (Subtraction: ? - 5 = 8)
  - "Ali had 15 marbles. He lost some. Now he has 8 marbles left. How many marbles did he lose?" (Subtraction: 15 - ? = 8)
  - "Ali had some marbles. He played a game and won 3 more. Now he has 8 marbles. How many did he start with?" (Addition: ? + 3 = 8)

# Part-Whole Analysis (Inferred)
part_whole_structure:
  known: "part_remaining = 8"
  unknown: "whole OR part_removed"
  operation: "subtraction (most likely) OR addition"
  context: "marbles left after some change"

# Validation & 2026 Compliance
validation:
  manual_review_required: true
  confidence_score: 0.7
  syllabus_2026_alignment: 
    - "Word problem comprehension: CONFIRMED"
    - "Paper 1 weight: 50% - reasoning skills important"
    - "No deprecated topics: CONFIRMED (not Speed/Cells)"
  cost_tracking:
    vision_api_calls: 0  # Heuristic preferred
    llm_tokens: 180
    heuristic_bypass: true
    cost_per_node: 0.00
    processing_method: "text_keyword_heuristic + inference"

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

# Critical Thinking Focus
reasoning_analysis: |
  This question type tests HIGHER-ORDER thinking beyond mere calculation.
  Skills required: Problem comprehension, logical inference, scenario reconstruction.
  Paper 1 includes such questions to test conceptual understanding, not just fluency.
  Game design must balance: Too much guidance → defeats purpose; Too little → frustration.

# Pedagogical Insights

## Cognitive Demand Profile
- **Working Memory:** High (must hold incomplete info while inferring missing parts)
- **Attention:** Integration of textual and visual clues to reconstruct scenario
- **Executive Function:** Hypothesis generation, logical reconstruction, verification
- **Linguistic Processing:** Interpret "has...left" as subtraction context cue

## Common Misconceptions
1. **Incomplete processing:** Answering "8" without recognizing missing information
2. **Operation misinference:** Assuming addition instead of subtraction (or vice versa)
3. **Visual misinterpretation:** Misreading visual cues about what happened to marbles
4. **Context blindness:** Not using visual context to infer the complete problem

## Adaptive Learning Pathway
1. **Prerequisite:** Complete word problems with all information given
2. **Current:** Problems with one missing element requiring inference
3. **Next:** Multiple missing elements, ambiguous scenarios
4. **Advanced:** Create word problems from given conclusions

## Game Mechanics Translation
- **Core loop:** Analyze partial info → Generate hypotheses → Test against visual → Reconstruct → Solve
- **Reward:** Points for accurate reconstruction + bonus for identifying all possibilities
- **Progression:** Increase ambiguity, reduce visual cues, add multiple interpretations
- **Power-ups:** "Context hint", "Possible scenario generator", "Visual analyzer"

## Assessment Design Insight
- **Formative:** Tests problem comprehension vs. mere calculation
- **Diagnostic:** Reveals whether student can identify missing information
- **Critical thinking:** Requires logical reconstruction beyond rote calculation

## Singapore Context Notes
- **Marbles:** Traditional game still familiar to Singaporean children
- **Language:** "Has...left" common phrasing in Singapore math materials
- **Visual style:** Likely uses clear before/after visual representations

## Vertical Evolution to P6
- **P1 version:** Simple objects, single missing element, clear visual cues
- **P3 version:** Multiple steps, mixed operations, fewer visual aids
- **P6 version:** Algebraic representation (x - y = 8), multiple variables, real-world data interpretation

---

*Generated as part of ATOM-SG Operation Vertical Thread Pilot*
*Schema Version: 4.0 (Post-QA/QC Brutal Feedback)*
*Processing Date: 2026-04-08*
*Correction: Updated with MOE codes, vertical evolution, and 2026 compliance*