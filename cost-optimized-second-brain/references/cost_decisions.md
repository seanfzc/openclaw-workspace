# Cost Decision Framework

## Karpathy's Core Insight
**Context length drives token cost** because every new token re-processes all prior tokens in the Transformer forward pass. Cost scales linearly with total context.

## Conversation Cost Management

### Running Summary Strategy
- **Target:** 200-300 tokens per summary
- **Update frequency:** Every 4-6 user turns or significant milestones
- **Structure:**
  1. Current project status (1-2 sentences)
  2. Key decisions & progress (bullet points)
  3. Active tasks (bullet points)
  4. Critical learnings (bullet points)
  5. Next immediate actions (bullet points)
  6. Cost management strategy (API decisions)
  7. Second Brain integration (what's been added)
  8. Open questions

### Context Window Management
- **Full history mode:** Only when explicitly requested
- **Normal mode:** Summary + last 1-2 messages
- **Proactive suggestion:** When context exceeds ~8k tokens, suggest summarization

## API Cost-Benefit Analysis

### Decision Tree for Processing Tasks

```
Is the task validation-critical?
├── Yes → Manual processing first (ensure quality)
│   └── Then automate for scale
└── No → Proceed to automation options

Automation options (ordered by cost-effectiveness):
1. **Local OCR (Tesseract)** - Free, for scanned PDFs
2. **Local scripts** - Free, for structured data
3. **LLM Text API** - Moderate cost, for analysis/classification
4. **Vision API** - High cost, for complex image understanding
5. **Manual review** - Time cost, for final validation
```

### Cost Categories

| Method | Cost Type | Best For | When to Use |
|--------|-----------|----------|-------------|
| **Manual Processing** | Time investment | Validation, small batches, schema development | Initial validation, critical quality checks |
| **Tesseract OCR** | Free (local) | Scanned PDFs, image text extraction | Bulk PDF processing, when installation possible |
| **Claude Text API** | Token-based | Analysis, classification, summarization | Logic detection, complexity scoring, pattern analysis |
| **Vision API** | High token cost | Complex diagrams, handwritten text, multi-modal | When OCR fails and manual is infeasible |
| **Gemini/Other APIs** | Varies | Alternative when primary unavailable | Fallback options, specific capabilities |

### Heuristic Rules
1. **Validation First:** Manual processing for initial schema validation
2. **Scale Second:** Automation for production processing
3. **Cost Tracking:** Record API calls, token usage, processing time
4. **Fallback Planning:** Have manual fallback for API failures

## Project ATOM-SG Cost Decisions

### Current Implementation (2026-04-08)
1. **Vision API:** Not available (404 errors) → manual extraction for validation
2. **OCR:** Tesseract pending installation approval → automated extraction for scale
3. **Claude API:** Using `claude-sonnet-4-6` for text analysis (not vision)
4. **Heuristic:** Manual validation first, automation for production

### Cost Tracking Metrics
- **Questions processed:** Track per question cost
- **API calls:** Count and estimate token usage
- **Processing time:** Manual vs automated comparison
- **Accuracy rate:** Schema compliance validation

### Optimization Opportunities
1. **Batch processing:** Group similar operations
2. **Caching:** Store analysis results for similar questions
3. **Template reuse:** Apply validated schemas to similar logic families
4. **Progressive disclosure:** Load reference material only when needed

## Second Brain Cost Efficiency

### Knowledge Compounding Benefits
- **Reduced repetition:** Information stored once in wiki, referenced multiple times
- **Context reduction:** Wiki serves as external memory, reducing conversation history
- **Decision tracking:** Cost decisions documented for future reference

### Implementation Efficiency
1. **Route once, reference many:** Add knowledge to wiki, then reference by link
2. **Schema evolution:** Track changes in wiki, not re-explain in conversation
3. **Script repository:** Store processing scripts in wiki for reuse

## Conversation Token Estimation

### Rough Estimates
- **System prompt:** ~2000 tokens
- **Skill metadata:** ~100 tokens per active skill
- **Conversation history:** ~150 tokens per exchange
- **Summary:** ~300 tokens (replaces full history)
- **Tool outputs:** Variable

### Optimization Strategies
1. **Summary early:** Create first summary after 4-6 exchanges
2. **Reference wiki:** Use `[[page]]` links instead of re-explaining
3. **Concise responses:** Bullet points over paragraphs when possible
4. **Tool output filtering:** Read only needed portions of files

## Emergency Cost Controls

### When Costs Spike
1. **Switch to manual:** Fall back to human processing
2. **Reduce context:** Aggressive summarization
3. **Pause automation:** Stop API-intensive operations
4. **Review decisions:** Audit cost-benefit analysis

### Monitoring Indicators
- **API error rates:** 404s, rate limits
- **Processing time:** Sudden increases
- **Token usage:** Per operation spikes
- **Quality degradation:** Accuracy drops requiring rework

## Template for Cost Decisions Log

```markdown
# Cost Decision: [Task Name]
## Date: [YYYY-MM-DD]
## Project: [Project Name]

## Decision Context
[Why this decision needed]

## Options Considered
1. **Option A:** [Description] - [Cost estimate]
2. **Option B:** [Description] - [Cost estimate]
3. **Option C:** [Description] - [Cost estimate]

## Decision Rationale
- [Factor 1]
- [Factor 2]
- [Factor 3]

## Expected Costs
- **Time:** [Estimate]
- **Tokens:** [Estimate]
- **Money:** [If applicable]

## Fallback Plan
[If this fails, what's the backup]

## Success Metrics
- [Metric 1]
- [Metric 2]
- [Metric 3]

## Actual Results (To be filled post-execution)
- **Actual time:** 
- **Actual tokens:**
- **Accuracy rate:**
- **Lessons learned:**
```

## Integration with Memory System

### memory.md Updates
Add cost-related principles to memory.md:
```
## Cost Optimization Principles
1. [Principle 1]
2. [Principle 2]
3. [Principle 3]
```

### soul.md Updates
Add identity statements to soul.md:
```
## Cost-Optimized Identity
"I am a token-efficient, knowledge-compounding agent..."
```

## Continuous Improvement

### Review Cycle
1. **Weekly:** Review cost decisions, identify patterns
2. **Monthly:** Update cost framework based on experience
3. **Per project:** Document lessons learned in wiki

### Metrics to Track
- **Conversation length reduction** after summarization
- **Wiki reference frequency** increasing over time
- **API cost per operation** trending downward
- **Processing accuracy** maintaining or improving

---

*This framework evolves based on actual usage patterns and cost data.*