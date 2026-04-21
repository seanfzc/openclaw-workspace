# Conversation Summary Template

## Purpose
Token-efficient context management per Karpathy's cost insight. Replace full conversation history with concise summary + recent messages.

## File Naming Convention
`conversation_summary_<project_or_topic>.md`

## Template Structure

```markdown
# Conversation Summary: [Project/Topic Name]
## Last Updated: [YYYY-MM-DD HH:MM Timezone]
## Token-Efficient Context Management

## Current Project Status
[1-2 sentences describing current phase, progress, and immediate focus]

## Key Decisions & Progress
- [Decision 1: What was decided and why]
- [Decision 2: What was decided and why]
- [Progress milestone 1]
- [Progress milestone 2]

## Active Tasks
- [Task 1: Status (pending/in progress/blocked)]
- [Task 2: Status (pending/in progress/blocked)]
- [Task 3: Status (pending/in progress/blocked)]

## Critical Learnings
- [Learning 1: What we discovered]
- [Learning 2: What we discovered]
- [Learning 3: What we discovered]

## Next Immediate Actions
1. [Action 1: Who/what/when]
2. [Action 2: Who/what/when]
3. [Action 3: Who/what/when]

## Cost Management Strategy
- **API Decisions:** [Which APIs being used and why]
- **Cost Tradeoffs:** [Manual vs automated decisions]
- **Heuristic Rules:** [Applied cost-saving rules]

## Second Brain Integration
- **Wiki Updates:** [What's been added to Second Brain]
- **Knowledge Compounding:** [How information is being preserved]
- **Reference Links:** [[Page1]], [[Page2]]

## Open Questions
1. [Question 1 needing answer]
2. [Question 2 needing answer]
3. [Question 3 needing answer]

---
**Summary Purpose:** Token-efficient context management per Karpathy's cost insight + Second Brain architecture
**Update Frequency:** Every 4-6 conversation turns or significant progress milestones
**Max Tokens:** ~300 (concise, actionable)
**Version:** [Optional version tracking]
```

## Usage Guidelines

### When to Create Summary
1. **After 4-6 exchanges** in a conversation
2. **At project milestones** (phase completion, major decisions)
3. **When context feels long** (estimated >8k tokens)
4. **Before breaks** (end of session, switching topics)

### When to Update Summary
1. **Significant progress** made
2. **Key decisions** finalized
3. **New learnings** discovered
4. **Blockers resolved** or new blockers identified
5. **Cost decisions** changed

### How to Use in Conversation
**Replace full history with:**
```
Previous context summary: [2-3 sentence summary of summary]

[Last 1-2 user messages]
```

**Example:**
```
Previous context summary: We're processing P6 questions for ATOM-SG pilot. 5 manual questions created for schema v4.1 validation. Tesseract OCR installation pending for automated extraction. Current focus: independent verification of manual samples.

User: Can you also implement this skill to manage costs?
```

## Content Guidelines

### Keep It Concise
- **Current Status:** 1-2 sentences max
- **Bullet Points:** 3-5 items per section
- **Total Length:** 200-300 tokens target
- **Language:** Direct, actionable, specific

### Focus on What Matters
- **Decisions:** Only include decisions that affect future work
- **Progress:** Milestones that change project trajectory
- **Learnings:** Insights that inform future decisions
- **Actions:** Concrete next steps with owners

### Omit What Doesn't Matter
- **Small talk** or social exchanges
- **Already-completed minor tasks**
- **Temporary confusion** that's been resolved
- **Redundant information** already in wiki

## Integration with Second Brain

### What Goes to Summary vs Wiki
| Content Type | Summary | Wiki |
|--------------|---------|------|
| **Project status** | ✓ Current snapshot | ✗ (Too transient) |
| **Decisions** | ✓ Key decisions | ✓ Documented in project page |
| **Progress** | ✓ Recent milestones | ✓ Added to project timeline |
| **Learnings** | ✓ Critical insights | ✓ Added to concepts/entities |
| **Actions** | ✓ Next steps | ✗ (Action tracking) |
| **Cost decisions** | ✓ Current strategy | ✓ Added to cost framework |
| **Open questions** | ✓ Unresolved issues | ✓ Added to project page |

### Cross-Referencing
- **From summary to wiki:** Use `[[page]]` notation
- **From wiki to summary:** Not needed (wiki is source of truth)
- **Version alignment:** Ensure summary references correct wiki page versions

## Examples

### Example 1: ATOM-SG Project Summary
```markdown
# Conversation Summary: Operation Vertical Thread (ATOM-SG)
## Last Updated: 2026-04-08 18:15 SGT
## Token-Efficient Context Management

## Current Project Status
Pilot execution phase: Validating schema v4.1 with P6 questions. 5 P1 questions processed, 5 P6 manual questions created for validation.

## Key Decisions & Progress
- Corrected node misclassification in P1 questions (Q1 was place_value_systems not number bonds)
- Created schema v4.1 with Paper 1 Revolution fields (time targets, red herring analysis)
- Manual extraction for P6 validation due to PDF OCR limitations

## Active Tasks
- Independent verification of 5 P6 manual questions (pending user/LLM review)
- Tesseract OCR installation approval (pending)
- Processing remaining 5 P6 questions from Rosyth PDF

## Critical Learnings
- PDF quality issue: 2025 P6 papers are scanned images with minimal OCR text
- Vision API access limited (404 errors), manual extraction as fallback
- Schema compliance: v4.1 adds Paper 1 requirements affecting game design

## Next Immediate Actions
1. User provides verification feedback on 5 P6 manual questions
2. Install Tesseract OCR for automated extraction
3. Process remaining 5 P6 questions from Rosyth PDF

## Cost Management Strategy
- Vision API: Not available → manual extraction for validation
- OCR: Tesseract pending → automated extraction for scale
- Claude API: Using text model for analysis
- Heuristic: Manual validation first, automation for production

## Second Brain Integration
- Schema v4.1: To be added to wiki/concepts/education-development/
- ATOM-SG Project: Added to wiki/entities/education-learning/
- Processing scripts: To be added to wiki/entities/tools-platforms/

## Open Questions
1. Schema v4.1 validation feedback from independent review?
2. Tesseract installation approval?
3. Target completion date for 10-question P6 pilot?
```

### Example 2: Quick Discussion Summary
```markdown
# Conversation Summary: API Cost Discussion
## Last Updated: 2026-04-08 14:30 SGT

## Current Discussion Status
Exploring cost optimization strategies for vision API usage in document processing.

## Key Decisions
- Prioritize manual validation before automated processing
- Implement cost tracking per operation
- Create fallback to OCR when vision API unavailable

## Learnings
- Vision APIs cost ~10x more than text APIs
- OCR accuracy sufficient for structured documents
- Manual validation catches schema issues early

## Next Actions
- Implement cost decision framework in skill
- Add cost tracking to processing scripts
- Document fallback procedures

## Open Questions
- What's the acceptable error rate for OCR vs manual?
- How to balance speed vs cost in production?
```

## Automation Scripts

### Sample Python Script for Summary Creation
```python
# scripts/create_summary.py
import datetime

def create_summary(project, status, decisions, tasks, learnings, actions):
    """Create conversation summary template."""
    template = f'''# Conversation Summary: {project}
## Last Updated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M %Z')}
## Token-Efficient Context Management

## Current Project Status
{status}

## Key Decisions & Progress
{decisions}

## Active Tasks
{tasks}

## Critical Learnings
{learnings}

## Next Immediate Actions
{actions}

## Cost Management Strategy
[API decisions, heuristics]

## Second Brain Integration
[What's been added to wiki]

## Open Questions
[Questions needing answers]
---
**Summary Purpose:** Token-efficient context management
**Update Frequency:** Every 4-6 conversation turns
**Max Tokens:** ~300
'''
    return template
```

## Quality Checklist
- [ ] Under 300 tokens (estimate)
- [ ] All key decisions included
- [ ] Action items specific and actionable
- [ ] Links to wiki where appropriate
- [ ] Cost decisions documented
- [ ] Open questions clearly stated
- [ ] Timestamp current
- [ ] Project name accurate

## Version History
- v1.0 (2026-04-08): Initial template created
- v1.1 (2026-04-08): Added integration guidelines, examples

---

*This template evolves based on usage patterns. Update as needed for different project types.*