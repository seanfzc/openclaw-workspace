# Second Brain System
# Education-Focused Implementation
# Based on Nick Spisak's System

## 🎯 Purpose
Transform Sean Foo's professional knowledge (energy, fintech, blockchain, AI) into **game-based learning experiences** that prepare his sons (11 & 6) for their future.

**Ultimate Goal:** Create learning apps, systems, and content where children learn without realizing they're learning.

## 📁 Structure

```
second-brain-simple/
├── raw/                    # Raw sources
│   ├── articles/          # Web articles, PDFs
│   ├── notes/             # Meeting notes, ideas
│   ├── conversations/     # Chat logs, transcripts
│   └── assets/            # Images, charts
├── wiki/                  # Organized knowledge
│   ├── sources/           # One page per ingested source
│   ├── entities/          # People, organizations, tools
│   ├── concepts/          # Ideas, frameworks, theories
│   ├── synthesis/         # Comparisons, analyses
│   ├── index.md           # Master catalog
│   └── log.md             # Operation history
├── output/                # Query results, reports
├── operations/            # Automation scripts
├── schema.md             # Master schema (templates, categories)
├── LIBRARIAN.md          # AI librarian rules
├── SKILL.md              # OpenClaw skill commands
└── README.md             # This file
```

## 🚀 Quick Start

### 1. Add Your First Source
Save an article to `raw/articles/`:
```bash
# Example: Save a web article about Squirrel AI or game-based learning
cp ~/Downloads/article.md raw/articles/
```

Or use **Obsidian Web Clipper** (Chrome extension) to save web articles directly.

### 2. Ingest the Source
Ask your OpenClaw assistant:
```
"Please ingest the files in my second brain raw folder"
```
or
```
"/second-brain-ingest"
```

The AI librarian will:
- Read and analyze the source
- Create a source page in `wiki/sources/`
- Extract entities and concepts
- Apply **education lens**: how this transforms into learning games
- Update index and log

### 3. Explore the Wiki
Open `wiki/` in **Obsidian** (free markdown editor) to see:
- Visual graph of connections
- Backlinks between pages
- Fast search across all knowledge

### 4. Query Your Knowledge
Ask questions:
```
"Query my second brain: How can I explain blockchain to my 6-year-old?"
```
or
```
"/second-brain-query What are the key principles of game-based learning?"
```

## 🎮 Education-First Philosophy

**Every analysis includes:**

1. **Game-Based Learning Application** - Specific game mechanics inspired by the content
2. **Critical Thinking Development** - How this builds problem-solving skills
3. **Future Skills Connection** - Skills needed for 2030+ that this develops
4. **Psychology & Engagement** - Using child psychology to make learning engaging

**Age-Specific Design:**
- **6-year-old:** Concrete thinking, short attention span, play-based
- **11-year-old:** Abstract thinking emerging, peer influence, projects

## 🔄 Four Operations (Nick Spisak Pattern)

### 1. **Onboarding** - Done
- Folder structure created
- Schema and librarian rules established
- Index and log initialized

### 2. **Ingest** - Ready
- Process raw files into wiki pages
- Each source touches 10-15 wiki pages
- Education lens applied to everything

### 3. **Query** - Ready
- Ask questions against your knowledge
- Good answers become synthesis pages
- Your curiosity makes the system smarter

### 4. **Lint** - Ready
- Monthly health checks
- Find broken links, contradictions, stale content
- Maintain knowledge quality

## 🧠 Compounding Knowledge

The system gets smarter two ways:

1. **New sources refine existing pages** - The 50th article updates 49 previous pages
2. **Queries generate synthesis** - Good answers become permanent wiki pages

**Result:** Each new piece of knowledge is exponentially more valuable than the last.

## 📞 Using OpenClaw

### Natural Language Commands
- "Ingest the new files in my second brain"
- "Query my second brain about [topic]"
- "Run a health check on my second brain"
- "Show status of my second brain"

### Skill Commands (if skill loaded)
- `/second-brain-ingest`
- `/second-brain-query "your question"`
- `/second-brain-lint`
- `/second-brain-status`

## 🛠️ Technical Details

### AI Librarian Rules
- Full rules in `LIBRARIAN.md`
- Follows schema.md templates
- Prioritizes education transformation
- Maintains cross-references and metadata

### Schema
- Comprehensive category system
- Page templates with education lens
- Metadata standards
- Quality checklists

### Automation
- Basic `ingest.py` script in `operations/`
- Can be extended with cron jobs
- Web clipping integration possible

## 🏁 Next Steps

1. **First ingestion** - Process an article about Squirrel AI or game-based learning
2. **Build entity network** - Add key educational researchers, tools, platforms
3. **Create concept framework** - Establish learning science foundations
4. **Regular queries** - Use the system to answer real questions
5. **Monthly linting** - Keep knowledge healthy

## 📚 Example Sources to Add

1. **Squirrel AI articles** - AI-driven learning gap diagnosis
2. **Game-based learning research** - What makes educational games effective
3. **Child psychology studies** - Motivation, attention, development
4. **Future skills reports** - What skills will be needed in 2030+
5. **Your professional content** - Energy, fintech, blockchain articles (with education lens)

## ⚠️ Troubleshooting

### Files not appearing in wiki?
- Check `raw/` folder permissions
- Ensure files are plain text (`.md`, `.txt`, `.pdf` requires extraction)
- Ask OpenClaw to manually process specific file

### Obsidian not showing graph?
- Open `second-brain-simple/` as vault in Obsidian
- Enable "Graph view" in left sidebar
- May need to wait for indexing

### Questions not getting good answers?
- More sources = better answers
- Try more specific queries
- Check that relevant entities/concepts exist

---

**Remember:** This isn't just a knowledge base. It's a compounding machine that transforms your professional expertise into your sons' educational future.

*System initialized: 2026-04-07*