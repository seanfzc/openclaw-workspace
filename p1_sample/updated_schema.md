# Question Metadata Schema (ATOM‑SG)
# Version: 2.0 - Pedagogical Pattern + Complexity Scoring
# Purpose: Extract game‑design templates, not instance data

## Design Principles
1. **Pattern over instance**: Capture design parameters, not specific answers
2. **Extensible across levels**: Core fields for P1‑P6, extension fields for advanced concepts
3. **Complexity‑aware**: Score questions based on multi‑dimensional difficulty
4. **Game‑ready**: Every field should inform game design decisions

## Core Fields (All Primary Levels)

### Pedagogical Pattern
| Field | Values | Description |
|-------|--------|-------------|
| `skill_type` | `counting_discrete_objects`, `number_sequence`, `addition_concept`, `subtraction_concept`, `multiplication_concept`, `division_concept`, `comparison`, `pattern_recognition`, `time_reading`, `shape_identification`, `measurement`, `data_interpretation`, `money`, `fractions`, `geometry`, `word_problem` | Core learning objective |
| `visual_arrangement` | `single_row`, `two_rows`, `scattered`, `grid`, `array`, `cluster`, `paired_items`, `sequence`, `none` | Layout pattern for game variation |
| `cognitive_demand` | `direct_recall`, `systematic_enumeration`, `pattern_extraction`, `comparison`, `transformation`, `multi_step`, `abstract_reasoning`, `justification` | Mental processes required |
| `answer_format` | `write_numeral`, `circle_option`, `choose_letter`, `draw_line`, `fill_blank`, `complete_sentence`, `explain_reasoning` | How answer must be presented |

### Complexity Scoring (1‑5)
| Score | Description | Game Design Implication |
|-------|-------------|-------------------------|
| **1** | Single skill, direct visual/text, simple answer | Tutorial level, confidence‑building |
| **2** | 2 skills, some visual‑text integration | Early progression, gentle challenge |
| **3** | 2‑3 skills, moderate integration, multi‑step | Core gameplay, skill combination |
| **4** | 3‑4 skills, complex integration, transformation | Advanced levels, strategic thinking |
| **5** | 4+ skills, abstract reasoning, explanation | Mastery challenges, puzzle‑solving |

**Complexity dimensions:**
1. **Skill connectivity** – number of linked primary/secondary nodes (1 point per node beyond first)
2. **Visual‑linguistic integration** – both visual and text parsing required (1 point)
3. **Cognitive operations** – transformation or multi‑step (1‑2 points)
4. **Answer format complexity** – write numeral=0, choose=1, draw/explain=2

### Quality & Validation
| Field | Purpose |
|-------|---------|
| `answer_key_confidence` | `high`/`medium`/`low` – trustworthiness of extracted answer |
| `visual_analysis_quality` | `high`/`medium`/`low` – Claude's description usefulness |
| `needs_review` | String flag if suspicious (e.g., "Answer key mismatch") |
| `processing_notes` | Technical notes (method, confidence, cache hits) |

## Extension Fields (Level‑Specific, Nullable)

### Difficulty Calibration
| Field | P1 Typical | P6 Typical | Purpose |
|-------|------------|------------|---------|
| `count_range` | `within_20` | `within_1000` | Numeric scope for counting/operations |
| `operation_type` | `addition` | `mixed_operations` | Specific arithmetic operation |
| `concept_complexity` | `low` | `high` | Abstractness of concept |
| `number_type` | `whole_numbers` | `fractions_decimals` | Number system involved |
| `context_realism` | `abstract` | `real_world` | Connection to practical situations |

### Game Design Prompts
| Field | Example |
|-------|---------|
| `game_hook` | "Vary object count & arrangement in treasure hunt" |
| `age_6_adaptation` | "Simple counting with clear visuals, immediate feedback" |
| `age_11_adaptation` | "Add time pressure, distractions, multi‑step challenges" |
| `progression_idea` | "Start with single row, advance to scattered items" |
| `common_misconceptions` | `["double_counting", "skip_errors"]` |

## Schema Implementation (YAML Front‑Matter)

### Example – P1 Counting Question
```yaml
---
# Core pattern
skill_type: counting_discrete_objects
visual_arrangement: two_rows
cognitive_demand: systematic_enumeration
answer_format: write_numeral
complexity_score: 2

# Extension (P1‑appropriate)
count_range: within_20
operation_type: null
concept_complexity: low

# Quality
answer_key_confidence: low
visual_analysis_quality: high
needs_review: "Answer key 'C' mismatched counting question"

# Game design
game_hook: "Vary object count (5‑20) and arrangement (rows, circle, scatter)"
age_6_adaptation: "Treasure hunt – count gems in pirate chest"
age_11_adaptation: "Factory line – count items on conveyor with distractions"
progression_idea: "Start with single row of 5, advance to scattered items up to 20"
common_misconceptions: ["double_counting", "skip_errors"]
---
```

### Example – P2 Multiplication Array
```yaml
---
# Core pattern
skill_type: multiplication_concept
visual_arrangement: array
cognitive_demand: pattern_recognition
answer_format: write_numeral
complexity_score: 3

# Extension (P2‑specific)
count_range: within_100
operation_type: multiplication
concept_complexity: medium

# Quality
answer_key_confidence: high
visual_analysis_quality: high
needs_review: null

# Game design
game_hook: "Create array games with varying dimensions (2×3, 4×5, etc.)"
age_6_adaptation: null  # Too advanced
age_11_adaptation: "Grid‑based strategy game – claim array areas"
progression_idea: "Start with visual arrays, advance to numeric only"
common_misconceptions: ["counting_all_dots", "confusing_rows_columns"]
---
```

## Complexity Scoring Algorithm

```python
def compute_complexity(question_metadata):
    score = 1  # Base
    
    # 1. Skill connectivity
    primary_nodes = question_metadata.get('primary_nodes', [])
    secondary_nodes = question_metadata.get('secondary_nodes', [])
    total_nodes = len(primary_nodes) + len(secondary_nodes)
    if total_nodes >= 3:
        score += 1
    if total_nodes >= 4:
        score += 1
    
    # 2. Visual‑linguistic integration
    visual_arrangement = question_metadata.get('visual_arrangement')
    requires_text_parsing = question_metadata.get('requires_text_parsing', False)
    if visual_arrangement != 'none' and requires_text_parsing:
        score += 1
    
    # 3. Cognitive operations
    cognitive_demand = question_metadata.get('cognitive_demand')
    if cognitive_demand in ['transformation', 'multi_step']:
        score += 1
    elif cognitive_demand in ['abstract_reasoning', 'justification']:
        score += 2
    
    # 4. Answer format
    answer_format = question_metadata.get('answer_format')
    if answer_format in ['draw_line', 'complete_sentence']:
        score += 1
    elif answer_format == 'explain_reasoning':
        score += 2
    
    # Clamp to 1‑5
    return min(max(score, 1), 5)
```

## P2 Pilot Validation Checklist

### Success Criteria
- [ ] All P2 questions fit core schema without forcing
- [ ] Complexity scores distribute appropriately (mostly 2‑4, few 1 or 5)
- [ ] Extension fields used meaningfully for P2‑specific concepts
- [ ] Game hooks are concrete and actionable
- [ ] Answer‑key confidence flags real issues
- [ ] Schema can be applied back to P1 questions seamlessly

### Exit Criteria
- Schema passes P1 and P2 validation
- Complexity scoring reflects intuitive difficulty
- Game design hooks inspire actual game mechanics
- Quality flags catch ≥90% of real problems

---

## Next Steps
1. **Implement updated schema** in pipeline
2. **Run P2 pilot** (5‑10 PDFs, ~50‑100 questions)
3. **Validate** against checklist
4. **Scale** to all Primary levels if successful
5. **Build Obsidian graph** with complexity‑colored nodes