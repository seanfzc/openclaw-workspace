---
name: second-brain
description: Manage Sean Foo's education-focused second brain system. Implements Nick Spisak's second brain pattern with unique focus on transforming professional knowledge into game-based learning for his sons (11 & 6).
---

# Second Brain Skill

This skill provides commands to operate Sean Foo's second brain system, adapted from Nick Spisak's pattern with education-first focus.

## System Overview

**Core Philosophy:** Transform all professional knowledge (energy, fintech, blockchain, AI) into game-based learning experiences that prepare Sean's sons (11 & 6) for their future.

**Structure:**
- `raw/` - Raw sources (articles, notes, transcripts)
- `wiki/` - Organized knowledge (sources, entities, concepts, synthesis)
- `outputs/` - Query results, reports
- `CLAUDE.md` - Primary schema following Nick Spisak's exact template
- `schema.md` - Extended schema with education-first templates
- `LIBRARIAN.md` - Rules for AI librarian behavior

## Commands

### `/second-brain-ingest`
Process raw files into wiki pages.

**Usage:**
```
/second-brain-ingest [filename]
```
- If no filename provided: process all unprocessed files in `raw/`
- Reads file, analyzes with education lens
- Creates source page in `wiki/sources/`
- Updates/creates entity and concept pages
- Establishes cross-references
- Updates index and log

**Education Lens Focus:** Each analysis must answer:
1. What learning game could this inspire for 11yo or 6yo?
2. Which future skills does this build (critical thinking, leadership, etc.)?
3. How would you explain this to a 6yo vs 11yo?
4. How can child psychology principles make learning more engaging?

### `/second-brain-query`
Ask questions against the knowledge base.

**Usage:**
```
/second-brain-query "your question"
```
- Searches across entire wiki using semantic understanding
- Synthesizes answer with citations
- If answer is valuable, creates synthesis page in `wiki/synthesis/`
- Saves query to `outputs/queries/`

**Example Questions:**
- "What are the biggest gaps in my understanding of game-based learning?"
- "Compare Squirrel AI's approach with traditional adaptive learning."
- "How can I explain blockchain concepts to my 6-year-old?"
- "What energy sector trends could become learning games?"

### `/second-brain-lint`
Run health check on the knowledge base.

**Usage:**
```
/second-brain-lint
```
- Checks for broken links
- Identifies orphan pages
- Finds contradictions between sources
- Flags stale claims (>6 months)
- Verifies metadata completeness
- Generates report in `outputs/lint/`

### `/second-brain-status`
Show system status and statistics.

**Usage:**
```
/second-brain-status
```
- Displays page counts by category
- Shows recent activity from log
- Identifies pending raw files
- Reports on education transformation progress

## Education-First Principles

### Age-Specific Design
- **6-year-old:** Concrete thinking, short attention span, play-based learning
- **11-year-old:** Abstract thinking emerging, peer influence, longer projects

### Learning Game Heuristics
1. **Invisible Learning:** Teach without them realizing they're learning
2. **Progressive Challenge:** Start easy, gradually increase complexity
3. **Meaningful Choice:** Let decisions affect outcomes
4. **Immediate Feedback:** Show consequences of actions
5. **Story Integration:** Wrap learning in narrative

### Squirrel AI Inspiration
- Use AI to identify and address individual learning gaps
- Personalize difficulty based on performance
- Adapt content to learning style

## Workflow

### Daily
1. Save interesting content to `raw/` (via Obsidian Web Clipper or manual)
2. Run `/second-brain-ingest` to process new files
3. Use `/second-brain-query` for immediate questions

### Weekly
1. Process batch of accumulated raw files
2. Review new connections in wiki
3. Check `/second-brain-status`

### Monthly
1. Run `/second-brain-lint`
2. Review and fix issues
3. Update schema based on usage patterns

## Getting Started

1. **First ingestion:** Save an article about Squirrel AI or game-based learning to `raw/`
2. **Run:** `/second-brain-ingest`
3. **Explore:** Check created pages in `wiki/`
4. **Query:** `/second-brain-query "How can I apply this to my boys' education?"`

## File Locations

- **Skill Directory:** `/Users/zcaeth/.openclaw/workspace/second-brain-simple/`
- **Raw Files:** `raw/articles/`, `raw/notes/`, `raw/conversations/`
- **Wiki:** `wiki/sources/`, `wiki/entities/`, `wiki/concepts/`, `wiki/synthesis/`
- **Output:** `outputs/queries/`, `outputs/reports/`, `outputs/lint/`

## References

- **Primary Schema:** `CLAUDE.md` - Exact implementation of Nick Spisak's system
- **Extended Schema:** `schema.md` - Education-focused templates and categories
- **Librarian Rules:** `LIBRARIAN.md` - Detailed AI librarian instructions
- **Index:** `wiki/index.md` - Master catalog
- **Log:** `wiki/log.md` - Operation history

---

**Remember:** Every piece of knowledge should ultimately connect to preparing Sean's sons for their future through engaging, game-based learning experiences.