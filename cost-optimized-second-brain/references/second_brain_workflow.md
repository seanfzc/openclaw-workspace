# Second Brain Integration Workflow

## Core Principle
**Knowledge compounding:** Instead of repeating information in conversation history, store it once in the Second Brain wiki and reference it multiple times. This reduces token usage while creating a self-improving knowledge repository.

## Workflow Overview

```
Raw Input → Conversation → Summary → Wiki Integration → Memory Distillation
```

### 1. Raw Input Processing
- **Sources:** Articles, documents, notes, transcripts
- **Location:** `raw/` directory (organized by type)
- **Processing:** Read, analyze with education lens, extract key insights

### 2. Conversation Context
- **Live discussion:** Immediate questions, decisions, clarifications
- **Summary maintenance:** Running conversation summary (200-300 tokens)
- **Knowledge identification:** Flag content worth preserving

### 3. Wiki Integration
- **Route to appropriate location:** sources/entities/concepts/synthesis
- **Create/update pages:** With YAML frontmatter and cross-references
- **Update index:** Maintain master catalog and statistics
- **Log operation:** Record in wiki/log.md for audit trail

### 4. Memory Distillation
- **memory.md:** Curated long-term facts, patterns, preferences
- **soul.md:** Core identity and cost-optimization principles
- **Daily logs:** `memory/YYYY-MM-DD.md` for detailed activity

## Wiki Structure Guide

### Sources (`wiki/sources/`)
**For:** Raw materials that have been analyzed
**Examples:** Articles, research papers, document analyses, transcript summaries
**Template:**
```markdown
---
title: [Descriptive Title]
created: [YYYY-MM-DD]
last_updated: [YYYY-MM-DD]
source_count: [Number]
status: [draft/active/archived]
---
# [Title]
*[Brief descriptor]*

## Executive Summary
[2-3 paragraph summary of key insights]

## Key Takeaways
- [Takeaway 1]
- [Takeaway 2]
- [Takeaway 3]

## Strategic Implications - Through Education Lens
**PRIMARY: Education Transformation Value**
- **Learning Game Potential:** [How this inspires games for 6yo/11yo]
- **Concept Simplification:** [How to explain to different ages]
- **Role Modeling:** [What this demonstrates about learning/thinking]
- **Future Connection:** [How this prepares for future skills]

**For [Professional Context 1]:** [Application]
**For [Professional Context 2]:** [Application]
**Personal Development:** [Personal application]

## Connections
**Related Concepts:** [[concept1]], [[concept2]]
**Related Entities:** [[entity1]], [[entity2]]
**Source References:** [[source1]], [[source2]]

## Metadata
- **Source Type:** [article/research/document/conversation]
- **Domain:** [education/energy/fintech/etc.]
- **Maturity:** [emerging/established/legacy]
- **Confidence:** [low/medium/high]
- **Next Review:** [YYYY-MM-DD]
```

### Entities (`wiki/entities/`)
**For:** People, organizations, projects, tools, systems
**Categories:** education-learning, energy-sector, fintech-ai, blockchain-web3, professional-network, tools-platforms
**Template:**
```markdown
---
title: [Entity Name]
created: [YYYY-MM-DD]
last_updated: [YYYY-MM-DD]
source_count: [Number]
status: [draft/active/monitoring/archived]
---
# [Entity Name]
*Type: [organization/person/project/tool]*

## Overview
[Brief description]

## Key Details
- **Domain:** [primary domain]
- **Relationship:** [tool/inspiration/partner/competitor]
- **First Contact:** [YYYY-MM-DD]
- **Last Updated:** [YYYY-MM-DD]

## Strategic Value - Through Education Lens
**PRIMARY: Education Transformation Value**
- **Learning Game Potential:** [Game inspiration for 6yo/11yo]
- **Concept Simplification:** [Age-appropriate explanations]
- **Role Modeling:** [What this demonstrates]
- **Future Connection:** [Future skills preparation]

**For [Professional Context 1]:** [Application]
**For [Professional Context 2]:** [Application]
**Personal Network:** [Network implications]

## Interactions
[Direct interactions, meetings, collaborations]

## Connections
**Related Entities:** [[entity1]], [[entity2]]
**Related Concepts:** [[concept1]], [[concept2]]
**Source References:** [[source1]], [[source2]]

## Metadata
- **Entity Type:** [organization/person/project/tool]
- **Domain:** [primary domain]
- **Status:** [monitoring/active/inactive]
- **Priority:** [low/medium/high]
- **Next Action:** [What to do next]
```

### Concepts (`wiki/concepts/`)
**For:** Frameworks, methodologies, patterns, theories
**Categories:** operational-excellence, education-development, leadership-frameworks
**Template:**
```markdown
---
title: [Concept Name]
created: [YYYY-MM-DD]
last_updated: [YYYY-MM-DD]
source_count: [Number]
status: [draft/active/established]
---
# [Concept Name]
*[Brief descriptor]*

## Core Idea
[1-2 paragraph explanation]

## Key Components
1. **[Component 1]:** [Description]
2. **[Component 2]:** [Description]
3. **[Component 3]:** [Description]

## Applications - With Education as Primary Lens
**PRIMARY: Game-Based Learning Design**
- **Age 6 Adaptation:** [How to adapt for 6yo]
- **Age 11 Adaptation:** [How to adapt for 11yo]
- **Game Mechanics:** [Specific game applications]
- **Psychology & Engagement:** [Psychological principles]

**For [Professional Context 1]:** [Application]
**For [Professional Context 2]:** [Application]
**Personal Development:** [Personal application]

## Limitations & Criticisms
- [Limitation 1]
- [Limitation 2]
- [Limitation 3]

## Implementation Guide
**Step 1:** [First step]
**Step 2:** [Second step]
**Step 3:** [Third step]

**Success Metrics:**
- [Metric 1]
- [Metric 2]
- [Metric 3]

## Connections
**Related Concepts:** [[concept1]], [[concept2]]
**Supporting Entities:** [[entity1]], [[entity2]]
**Source References:** [[source1]], [[source2]]

## Metadata
- **Concept Type:** [methodology/framework/pattern/theory]
- **Domain:** [primary domain]
- **Maturity:** [emerging/established/legacy]
- **Confidence:** [low/medium/high]
- **Last Reviewed:** [YYYY-MM-DD]
```

### Synthesis (`wiki/synthesis/`)
**For:** Cross-referenced insights, comparison pages, integrated analyses
**Created when:** Multiple sources/concepts need synthesis for deeper insight
**Template:** Flexible based on synthesis type

## Integration with Conversation Summary

### What Gets Added When
| Conversation Element | Wiki Location | Timing |
|----------------------|---------------|--------|
| **Project started** | Entities (project page) | After initial definition |
| **Schema created** | Concepts (methodology) | After validation |
| **Script developed** | Entities (tools) or References | After testing |
| **Key decision** | Project entity page | After decision finalized |
| **Learning discovered** | Concepts or Synthesis | After verification |
| **Cost decision** | References (cost framework) | After implementation |

### Cross-Reference Patterns
- **From conversation summary:** `[[wiki-page]]` links
- **From wiki pages:** Link to related pages
- **From memory.md:** Reference key wiki pages
- **From soul.md:** Core principles that guide wiki use

## Education Lens Implementation

### Age-Specific Design
**6-year-old (Concrete thinking):**
- Play-based learning
- Short attention span (5-10 minute activities)
- Concrete examples (objects, pictures, stories)
- Immediate feedback
- Physical interaction

**11-year-old (Abstract thinking emerging):**
- Project-based learning
- Peer influence and collaboration
- Longer focus (15-30 minute activities)
- Abstract concepts with concrete anchors
- Choice and autonomy

### Game Design Heuristics
1. **Invisible Learning:** Teach without them realizing they're learning
2. **Progressive Challenge:** Start easy, gradually increase complexity
3. **Meaningful Choice:** Let decisions affect outcomes
4. **Immediate Feedback:** Show consequences of actions
5. **Story Integration:** Wrap learning in narrative
6. **Social Connection:** Peer comparison, collaboration
7. **Mastery Display:** Show progress visually

### Squirrel AI Inspiration
- **Knowledge space theory:** Decompose subjects into granular points
- **Diagnostic assessment:** Identify specific gaps before teaching
- **Personalized paths:** Adapt sequence based on performance
- **Continuous adaptation:** Adjust based on ongoing performance

## Cost-Efficiency Benefits

### Token Reduction
- **Wiki as external memory:** Reduces need to repeat information in conversation
- **Reference by link:** `[[page]]` uses fewer tokens than re-explaining
- **Structured retrieval:** Load only needed reference sections

### Knowledge Compounding
- **Builds over time:** Each addition makes the wiki more valuable
- **Cross-references create network:** Insights emerge from connections
- **Reduces rework:** Lessons learned are preserved for future use

### Decision Quality
- **Documented rationale:** Cost decisions preserved for review
- **Pattern recognition:** Repeated decisions reveal optimization opportunities
- **Continuous improvement:** Framework evolves based on experience

## Implementation Checklist

### For Each Conversation
- [ ] Maintain running summary (update every 4-6 turns)
- [ ] Identify knowledge worth preserving
- [ ] Route to appropriate wiki location
- [ ] Update index and log
- [ ] Reference wiki naturally in conversation

### For Each Project
- [ ] Create project entity page
- [ ] Document schemas/methodologies as concepts
- [ ] Store scripts/tools as entities or references
- [ ] Track decisions and learnings on project page
- [ ] Update cost decisions in framework

### Weekly Maintenance
- [ ] Review wiki index for gaps
- [ ] Check for broken links
- [ ] Update stale pages
- [ ] Review cost decisions
- [ ] Prune memory.md of outdated entries

## Example: ATOM-SG Integration

### What Was Added
1. **Entity:** `atom-sg-pedagogical-engine.md` (project/system)
2. **Concept:** `syllabus-mapping-methodology.md` (enhanced)
3. **References:** Cost decision framework, summary template
4. **Log entry:** Operation recorded in wiki/log.md

### Conversation Integration
- **Summary created:** `conversation_summary_atom_sg.md`
- **References used:** `[[atom-sg-pedagogical-engine]]`, `[[syllabus-mapping-methodology]]`
- **Cost decisions:** Documented in framework
- **Next actions:** Linked to project page

### Education Lens Application
- **Age 6 adaptation:** "Logic Traps" as "Boss Levels"
- **Age 11 adaptation:** "Red Herring Data" as "Data Filter" games
- **Game mechanics:** Vertical progression as evolving game world
- **Psychology:** Cognitive dissonance traps as metacognitive training

## Scripts and Automation

### Available Scripts
- `update_second_brain.py`: Route content to wiki
- `create_conversation_summary.py`: Generate summary from recent messages
- `wiki_lint.py`: Check wiki health (broken links, orphans)
- `cost_tracker.py`: Track API usage and estimate costs

### Integration Points
- **Post-conversation:** Auto-suggest wiki updates
- **Project milestones:** Auto-create summary
- **Cost decisions:** Auto-log to framework
- **Education lens:** Auto-apply age adaptations

## Quality Metrics

### Wiki Health
- **Page count growth:** Steady increase over time
- **Cross-reference density:** Average links per page
- **Update frequency:** Regular updates to key pages
- **Education lens coverage:** Percentage of pages with age adaptations

### Cost Efficiency
- **Conversation length reduction:** Tokens per exchange trending down
- **Wiki reference frequency:** Increasing use of `[[page]]` links
- **API cost per operation:** Trending downward
- **Processing accuracy:** Maintaining or improving with cost optimization

### Knowledge Compounding
- **Insight emergence:** New connections discovered through cross-references
- **Decision quality:** Better decisions with documented rationale
- **Learning velocity:** Faster onboarding to new topics via wiki
- **Error reduction:** Fewer repeated mistakes with documented learnings

## Troubleshooting

### Common Issues
1. **Wiki not being referenced:** Remind to use `[[page]]` notation
2. **Summary too long:** Enforce 300-token limit, focus on key points
3. **Education lens missing:** Always include age adaptations
4. **Cost decisions not documented:** Log in framework immediately
5. **Links broken:** Run wiki_lint.py regularly

### Solutions
- **Training reminder:** Include wiki reference examples in responses
- **Template enforcement:** Use provided templates consistently
- **Quality checklist:** Review before finalizing wiki pages
- **Regular maintenance:** Weekly wiki review session

## Evolution Path

### Phase 1: Foundation (Current)
- Basic wiki structure
- Conversation summaries
- Cost decision framework
- Education lens application

### Phase 2: Automation
- Scripts for common operations
- Auto-suggestions for wiki updates
- Cost tracking integration
- Quality metrics dashboard

### Phase 3: Optimization
- Predictive cost modeling
- Intelligent routing to wiki
- Adaptive education lens
- Advanced knowledge compounding

---

*This workflow evolves based on usage patterns and emerging best practices. Update regularly as the system matures.*