# Knowledge Base Schema
## Identity
This is a personal knowledge base about transforming professional knowledge (energy, fintech, blockchain, AI) into game-based learning experiences for Sean's sons (11 & 6 years old). Maintained by an LLM agent. The human curates sources and asks questions. The LLM does everything else.

**Primary Focus:** Education transformation through Squirrel AI-inspired adaptive learning, critical thinking development, leadership skills, and psychology-informed engagement design.

## Architecture
- `raw/` contains immutable source documents. NEVER modify files in raw/.
- `wiki/` contains the compiled wiki. The LLM owns this directory entirely.
- `outputs/` contains generated reports, analyses, and query answers.

## Wiki Conventions
- Every topic gets its own .md file in wiki/
- Every wiki file starts with YAML frontmatter:
  ```
  ---
  title: [Topic Name]
  created: [Date]
  last_updated: [Date]
  source_count: [Number of raw sources that informed this page]
  status: [draft | reviewed | needs_update]
  ---
  ```
- After frontmatter, a one-paragraph summary
- Use `[[topic-name]]` for internal links between wiki pages
- Every factual claim cites its source: `[Source: filename.md]`
- When new info contradicts existing content, flag explicitly:
  > CONTRADICTION: [old claim] vs [new claim] from [source]

**EDUCATION LENS REQUIRED:** Every analysis must include:
1. **Game-Based Learning Application** - Specific game mechanics inspired by content
2. **Critical Thinking Development** - How this builds problem-solving skills
3. **Future Skills Connection** - Skills needed for 2030+ that this develops
4. **Psychology & Engagement** - Using child psychology to make learning engaging
5. **Age-Specific Adaptation** - How to explain to 6yo vs 11yo

## Index and Log
- `wiki/index.md` lists every page with a one-line description, by category
- `wiki/log.md` is append-only chronological record
- Log entry format: `## [YYYY-MM-DD] action | Description` (Actions: ingest, query, lint, update)

## Ingest Workflow
When processing a new source:
1. Read the full source document
2. **Discuss key takeaways with user** before proceeding
3. Create or update a summary page in wiki/ with YAML frontmatter
4. Update wiki/index.md
5. Update ALL relevant entity and concept pages across the wiki
6. Add backlinks from existing pages to new content
7. Flag any contradictions with existing wiki content using `> CONTRADICTION:` format
8. Append entry to wiki/log.md
9. A single source should touch 10-15 wiki pages

**Education Transformation Focus:** Each ingest must apply the education lens above. Identify how professional knowledge translates into learning games for 11yo and 6yo.

## Query Workflow
When answering a question:
1. Read wiki/index.md first to find relevant pages
2. Read all relevant wiki pages
3. Synthesize answer with `[Source: page-name]` citations
4. If answer reveals new insights, offer to file it back into wiki/
5. Save valuable answers to outputs/

**Education Connection:** When answering, always consider: "How does this relate to preparing Sean's sons for their future through game-based learning?"

## Lint Workflow (Monthly)
Check for:
- Contradictions between pages
- Stale claims superseded by newer sources
- Orphan pages with no inbound links
- Concepts mentioned but never explained
- Missing cross-references
- Claims without source attribution
- Missing education lens in Strategic Implications sections
- Incomplete YAML frontmatter

Output: `wiki/lint-report-[date].md` with severity levels (🔴 errors, 🟡 warnings, 🔵 info)

## Focus Areas
1. **Game-Based Learning Systems** - Transforming content into engaging games where children learn without realizing it
2. **Adaptive Learning & Squirrel AI Approach** - Using AI to diagnose and address individual learning gaps
3. **Critical Thinking & Leadership Development** - Age-appropriate skill building for 11yo and 6yo
4. **Child Psychology & Communication** - Understanding motivation, attention, and engagement principles
5. **Future Skills Preparation** - Skills needed for 2030+ (adaptability, digital literacy, systems thinking)
6. **Domain Knowledge Translation** - Converting energy, fintech, blockchain, AI concepts into child-friendly learning experiences

## Age-Specific Considerations
- **6-year-old:** Concrete thinking, short attention span, play-based learning, simple cause-effect
- **11-year-old:** Abstract thinking emerging, peer influence, longer projects, system understanding

## Squirrel AI Inspiration
- Knowledge Space Theory: Decompose subjects into granular "knowledge points"
- Diagnostic assessment before learning begins
- AI-powered personalization of learning paths
- Continuous reassessment and gap identification

## Learning Game Design Heuristics
1. **Invisible Learning:** Teach without them realizing they're learning
2. **Progressive Challenge:** Start easy, gradually increase complexity
3. **Meaningful Choice:** Let decisions affect outcomes
4. **Immediate Feedback:** Show consequences of actions
5. **Story Integration:** Wrap learning in narrative

## Compounding Mechanism
- Each new source refines existing pages (the 50th article updates 49 previous pages)
- Queries generate permanent synthesis pages (good answers become wiki content)
- Connections reveal patterns across domains
- Knowledge compounds instead of resetting