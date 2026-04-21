---
title: "AI Agent Stack Everyone Must Use in 2026 (Builder’s Guide)"
source: "https://x.com/Av1dlive/status/2044453102703841645"
author:
  - "[[@Av1dlive]]"
published: 2026-04-12
created: 2026-04-16
description: "here is the truth nobody tells ai builders. you do not need to build your own model.all you need to build is TLDR; if you don't wanna re..."
tags:
  - "clippings"
---
![Image](https://pbs.twimg.com/media/HF8__sTbcAA6MPo?format=jpg&name=large)

## here is the truth nobody tells ai builders. you do not need to build your own model.

## all you need to build is

> TLDR; if you don't wanna read it , then give this link to your agent and ask it questions to understand ➡️[github.com/codejunkie99/agentic-stack](https://github.com/codejunkie99/agentic-stack)

the infrastructure around the model.

1. The memory that persists across sessions.
2. The skills that encode how tasks should be done.
3. The protocols that govern what the agent can and cannot do. Garry Tan posted on April 13 that nailed this point perfectly.

> Apr 12
> 
> If your memory dies when your harness dies, you built the harness too thick. Memory is markdown. Skills are markdown. Brain is a git repo. The harness is a thin conductor — it reads the files, it doesn't own them.

I spent the last three months building exactly this.

1. Four-layer memory.
2. Fat skills with self-rewrite hooks.
3. Protocol enforcement.
4. A nightly dream cycle that compresses everything the agent learned that day.

This article is 4,000 words of how I built it and why every piece exists. If you do not want to read all that, you can just install the whole thing here:⬇️

> **If you just want to install it:** [github.com/codejunkie99/agentic-stack](https://github.com/codejunkie99/agentic-stack)

Works with Claude Code, Cursor, OpenClaw, or any agent that reads markdown.

If you want to understand what you are installing and why each piece exists, keep reading.⬇️

![Image](https://pbs.twimg.com/media/HF9EqvLbAAEQ5_j?format=jpg&name=large)

## The shape of the full stack

Here is the folder structure. I will explain each part in detail, but I want you to see the whole thing first because the shape matters more than any individual piece.

This mirrors patterns from Gstack and Claude Code's own memory hooks. I did not design it from scratch.

I arrived at it by trying other layouts that did not work and gradually converging on this one.

The key insight, and the thing Garry's post crystallized for me, is the separation.

**The harness does not think.** It reads files, calls tools, writes logs, runs hooks. All the intelligence lives in the skill files and the memory files. The protocols enforce boundaries.

This means:

- You can swap the harness for a different one tomorrow and lose nothing
- You can swap the model and lose nothing
- The only things that accumulate value are the skills, the memory, and the protocols
- Those are plain markdown and JSON in a git repo

## The files nobody shows you (and the prompts to generate them)

Every guide shows you the folder structure. Nobody shows you what actually goes inside the four files that make or break the system. Here they are.

**AGENTS.md**

This is the first file the harness reads. It is the table of contents for your agent's brain. Without it, the agent does not know where anything lives.

**Prompt to generate yours:**

> Read the folder structure at .agent/ and write an AGENTS.md that serves as the root config file. It should tell the agent where memory, skills, and protocols live, what to read first, and what rules to always follow. Keep it under 30 lines. It is a map, not an encyclopedia.

**DECISIONS.md**

This is the file that saves you from re-debating the same architectural choice three months later. Without it, the agent (and you) will revisit settled questions endlessly.

**Prompt to generate yours:**

> Read memory/semantic/LESSONS.md and memory/episodic/AGENT\_LEARNINGS.jsonl. Identify the 3-5 most significant architectural or workflow decisions that have been made. For each one, write an entry in DECISIONS.md with: the decision, the rationale, alternatives that were considered, and whether it is still active. Format as markdown. Only include decisions that would be costly to revisit or re-debate.

**on\_failure.py**

This is the hook that turns failures into learning instead of just errors. Without it, failures get logged with generic pain scores and no reflection.

**What it does that post\_execution.py does not:**

- Automatically assigns high pain scores (8) so failures surface during retrieval
- Counts recent failures per skill
- Flags skills for rewrite after 3+ failures in 14 days
- Includes error type and context so the reflection is actionable

**The cron line**

That is it. The dream cycle runs at 3am, compresses memory, promotes lessons, archives stale entries, and git commits the result.

Check the log:

Check the history:

That is the agent's autobiography. Every line is a night of learning.

## The harness: thin conductor

I spent about 30 minutes on the first version of this. You can skip it entirely if you use Claude Code or Cursor as your harness, because they already have the loop, the tool calling, and the file watching built in. Point them at your .agent/folder and you are done.

I wanted full ownership, so I wrote the conductor myself. The entire thing is under 200 lines.

The critical function is build\_context, and it deserves a mental model before you look at the priority list.

**The context window is a computation box.** The model only reasons over what is inside it. Everything outside it, your memory files, your skill library, your tool schemas, your entire git history, does not exist to the model unless the harness retrieves it, shapes it, and injects it.

Each piece that enters the context window is a context fragment. Each fragment is an explicit decision about what the model needs to do its work right now.

The harness is a system of blocks that control and inject context.

- **Targeted fragments are signal.** They steer the model toward better computation.
- **Conflicting or stale fragments are noise.** They make the model confused, not smarter.

This is why build\_context is the most important function in the system, not the model call.

The conductor allocates based on priority:

1. Personal preferences and workspace always load first
2. Semantic lessons second
3. Recent episodic entries third
4. Matched skills fourth
5. Permissions last

If the budget runs out, skills that did not trigger do not load. **Every fragment that enters must earn its place.** If it is not making the current decision more legible, it is making it worse.

One rule I have enforced on myself: the harness stays under 200 lines. The moment it starts doing reasoning or making decisions about which skills to load, I have put intelligence in the wrong place. That logic belongs in a skill file, not in the conductor.

## The salience scoring function

This deserves a closer look because it is doing more work than it appears to. Each log entry has:

- A **pain score** (how badly did the mistake hurt, 1-10)
- An **importance score** (how often does this type of situation come up)
- A **recurrence count** (how many times has this pattern appeared)

The formula multiplies those against a recency decay. Recent painful important recurring things float to the top. Old minor one-off things sink.

I tried vector search before this. It was slower, more complex to set up, and did not produce noticeably better results for a single-user system.

**The simple weighted formula won.**

## Memory: four layers, not one

The single biggest mistake in my original setup was treating memory as one undifferentiated pile.

DECISIONS.md, LESSONS.md, and AGENT\_LEARNINGS.jsonl all lived in the same flat folder and the agent read them the same way.

This works for about six weeks.

Then it breaks because **different kinds of memory need different retention policies, different retrieval strategies, and different update frequencies.**

**Here are the four layers and why they need to be separate.**

**Layer 1 : Working context** is the live state of whatever task is happening right now. Open files, partial plans, active hypotheses, execution checkpoints. This is the most volatile layer. It changes every few minutes and becomes worthless the moment the task is done.

- **The point of externalizing this is resumption.** When the context window resets or you come back tomorrow, the agent reads WORKSPACE.md and picks up exactly where it left off instead of reconstructing everything from scratch.
- Update this file constantly. It is disposable. When the task finishes, archive it to episodic and start fresh.

**Layer 2: Episodic memory** records what happened in prior runs. Decision points, tool calls, failures, outcomes, and reflections.

This is not just a log. Retrieved episodes serve as concrete precedents that help the agent avoid repeating known mistakes.

The fields that matter most:

- **pain\_score**: how much damage the mistake caused
- **importance**: how likely this lesson is to be relevant again

The salience scoring function uses both to determine what surfaces during retrieval.

**Layer 3 :Semantic memory** stores abstractions that outlive any single episode. These are the patterns and heuristics that tend to hold across tasks. Not tied to a specific time or place.

The difference between episodic and semantic is not just granularity. It is function.

- **Episodic memory** says "this specific thing happened on this date."
- **Semantic memory** says "this tends to hold across cases."

The dream cycle is the mechanism that promotes episodic entries into semantic lessons when they recur or score high enough.

**Layer 4: Personal memory** tracks stable information about you specifically . Your preferences, your conventions, your recurring constraints.

This layer exists because user-specific information needs different retention rules than general task knowledge.

- This is the layer that lets the agent adapt to you over time without confusing your personal conventions with general best practices.
- It should never be merged into LESSONS.md because what works for you might be terrible advice in general.

## The upgraded dream cycle

The original dream cycle was a simple compression script.

This version handles all four memory layers with different policies.

The upgraded dream cycle does three things the old one did not:

- It **detects recurring patterns** across episodes and boosts their salience
- It **automatically promotes** high-salience patterns from episodic into semantic memory. Lessons that keep mattering get hardened into permanent knowledge without you manually curating them.
- It **archives decayed entries** instead of deleting them, so you can always git log memory/ to recover something that was compressed away too aggressively

I call it the dream cycle because it runs overnight and compresses the day's raw logs into clean distilled lessons, the same way sleep consolidates memories.

Run this on a nightly cron job. Or trigger it manually after intense sessions.

git log --oneline memory/ is still the agent's autobiography. I did not expect to find that useful. I use it constantly.

## The skills

This is where I spent most of my time, and where I think most of the value lives.

Each skill is a markdown file with YAML frontmatter and a self-rewrite section at the bottom. But after running 30+ skills for three months, I learned that **the skill files themselves are only half the problem.** The other half is finding and loading the right skill at the right time without flooding the context window.

**Skill registry and progressive disclosure**

This is the progressive disclosure layer. The agent reads \_index.md on every session start. It is short. Just names, one-line descriptions, and trigger phrases.

When a trigger matches, the agent loads the full SKILL.md for that specific skill. When nothing matches, the full skill files stay on disk unloaded.

**This matters because of context budget.** Your model has a fixed number of tokens it can process. Memory retrieval, skill loading, tool schemas, and the model's own reasoning all compete for that budget.

- If you dump every skill file into context on every run, you waste tokens on irrelevant instructions and the model performs worse, not better.
- Models attend unevenly across long inputs. Information in the middle of a big context gets missed.
- Progressive disclosure solves this by keeping the context lean.

For machine-readable discovery, add a structured manifest alongside the human-readable index:

The fields beyond name and triggers that matter:

- **preconditions**: what must be true before this skill can run
- **constraints**: hard boundaries on what the skill is allowed to do, normative not procedural
- **category**: used for composition when multiple skills need to coordinate

At around 50 skills the keyword trigger matching starts to miss. At 500 you will want semantic matching with embeddings. But keyword triggers work fine for the first year of solo usage.

**The skill loader**

**The core skills**

- **skillforge** is the one I built first and the one that changed the trajectory of everything else. It teaches the agent how to create new skills.
- Without it, I was writing every SKILL.md by hand.
- With it, the agent encounters a new domain, recognizes it does not have a skill for it, and drafts one.

I want to be honest about what this does and does not do. It does not produce perfect skills on the first try. The skills it generates are rough drafts.

But rough drafts that follow a consistent format and that include self-rewrite hooks from day one.

After a few iterations the agent-generated skills start getting noticeably better, because **the self-rewrite hook on skillforge itself is updating the template** based on what worked and what did not in previous attempts.

**memory-manager is the skill I wish I had written first.**

For the first three weeks of running this system I had all the memory files but the agent was not reading them consistently.

It would write a lesson after a failure and then repeat the exact same mistake three days later because nothing told it to check.

- The difference before and after adding this skill was immediate. Before, memory was a filing cabinet nobody opened.
- After, the agent was checking its past mistakes before making decisions and updating its own skills when it noticed patterns. **T**
- **the filing cabinet became a feedback loop.**

**Self-rewrite hook template**

Every skill, no matter how small, ends with a self-rewrite hook. This is the part that makes the system compound instead of staying static.

The important addition versus my original is step 5.

- Constraint violations get escalated from the skill's local KNOWLEDGE.md into the global LESSONS.md.
- **This is how a single skill's failure becomes system-wide knowledge.** The git-proxy skill discovering that force pushes are dangerous should not stay local to git-proxy. It should become a global constraint.

## Protocols: the layer most builders skip

This is the part almost nobody builds. And it is the part that determines whether your agent stays a toy or becomes something you can actually trust with real work.

Protocols are the contracts that govern how your agent talks to external systems.

- Without them, the model improvises message formats, argument structures, and permissions for every tool call.
- **That improvisation is where most production failures come from.**
- It's not that the model cannot call the tool, but because it guesses the wrong format, sends the wrong arguments, or does something it should not have permission to do.

**Tool schemas**

For every tool your agent can call, write a typed schema. This converts the model's task from "guess how to call this tool" to "fill in these fields."

Notice the fields beyond basic argument types:

- **preconditions**: what must be true before calling
- **side\_effects**: what will happen downstream
- **requires\_approval**: operations that need human sign-off
- **blocked\_targets**: hard constraints the harness enforces regardless of what the model decides

This does not serve as documentation. The harness reads these schemas and enforces them at runtime through the pre\_tool\_call hook.

## Permissions

- **The permissions file is the single most important file in the protocol layer.**
- It is the difference between an agent you can leave running and an agent you have to babysit.
- The rule is simple: if you would not let a new hire do it unsupervised, the agent needs approval too.

## Lifecycle hooks

Hooks are the enforcement mechanism. T

hey run before and after agent actions and implement the constraints defined in permissions and tool schemas.

**The post\_execution hook is what makes the memory system compound automatically.**

- Every action, success or failure, gets logged to episodic memory with a pain score
- Failures get higher pain scores
- Higher pain scores surface more often during retrieval
- The agent is more likely to remember and avoid them

You do not have to manually teach the agent anything. The hooks do it.

## The six flows that make it compound

The reason this system gets better over time instead of staying static is six feedback loops between the three modules. None of them require you to do anything manually after initial setup.

1. **Memory feeds skill creation.** When the memory-manager detects a recurring pattern in episodic memory, the same type of task handled the same way three or more times, it triggers skillforge to create a new skill from that pattern.
2. **Skills feed memory.** Every skill execution gets logged to episodic memory via the post\_execution hook. Success or failure, the result is recorded with a pain score. The memory system always has fresh data about which skills work and which do not.
3. **Skills run through protocols.** When a skill needs to call an external tool, the call goes through the pre\_tool\_call hook. The skill describes what to do. The protocol governs how it is done and whether it is allowed.
4. **Protocols generate skills.** Once you have a typed tool schema, it becomes easy to write a skill that uses it correctly. The schema tells the agent exactly what arguments are needed, what preconditions must be met, and what constraints apply. **This is why writing schemas first and skills second produces better skills than the reverse.**
5. **Memory influences which protocols get used.** If past episodic entries show that a particular API endpoint fails frequently, the agent can learn to prefer an alternative path.
6. **Protocol results become memory.** Tool outputs, approval events, error payloads. All of these get logged to episodic memory via the post\_execution hook. The protocol layer produces the evidence that memory stores, which later feeds skill updates and protocol routing.

This cycle is self-reinforcing. Better memory leads to better skill creation leads to richer execution traces leads to better memory.

But it can also amplify errors. A bad lesson in semantic memory can lead to a flawed skill, whose failures generate more bad entries. The dream cycle's decay mechanism and the self-rewrite hooks' conservative update policy are the circuit breakers that prevent this.

## What happened over 90 days

- **Weeks 1–2: frustrating.** The agent still forgot things. The memory files were there but the agent wasn't reading them reliably. I hadn't written memory-manager yet, so nothing was pulling the files into the loop.
- **Weeks 2–4: it started clicking.** Once memory-manager was in, the agent began checking LESSONS.md before making calls . I'd corrected before.
- **Weeks 4–5: it started editing itself.** I opened git-proxy's KNOWLEDGE.md one morning and there was a line in it I hadn't written. The agent had hit a rate limit, logged it, and during a reflection cycle memory-manager patched the skill.
- **Week 8: things started compounding.** I kept running into skills I'd forgotten I had, written by skillforge in response to problems I only half-remembered. The agent wasn't just remembering corrections anymore. It was generalizing from them.
- A lesson about API timeouts in one project ended up shaping how it scaffolded error handling in a completely different one. .
- **Week 10: I hit the wall.** Thirty skills, a fat LESSONS.md, tool schemas for everything. Over 90K tokens in context before the agent had even started thinking. The model started getting worse, not better, and it took me anembarrassing couple of days to figure out why.
- Progressive disclosure and the skill registry pulled it back under control, and performance snapped back basically overnight.

**I do not want to overstate this.**

- The agent is not sentient (not yet atleast lol) . It is not even particularly smart. **What it is, is consistent.** It checks its own notes.
- It updates its own instructions.
- It does not have bad days where it forgets what it learned last week.

That consistency, compounded over months, produces something that feels qualitatively different from a stateless agent, even though the underlying model is the same.

## The bitter lesson while building skills

> Apr 15

I wrote this after reading this tweet from Daniel.

If you're building skills yourself, one thing worth internalizing early: don't write driving directions. Write destinations and fences.

My first api-scaffold was twelve numbered steps. First check this, then run that, then validate this field.

> The rewrite is a paragraph: "I build APIs in FastAPI, REST conventions, explicit error types, typed request bodies, rate limiting at the middleware layer. Here are three endpoints I think are well-built. Here's one that failed and why. Build something that looks like the good ones."

The rewrite produces better output now, and it keeps getting better as the models improve.

## 3 Important Things while building skills

1. **Procedures** so the agent has a skeleton and doesn't skip a phase
2. **Heuristics** so it has a default at forks and doesn't freeze
3. **Constraints** so there's a fence around the yard

The line between that and micromanagement is easy in practice:

- Structure: "verify tests pass before committing"
- Micromanagement: "run npm test, grep for 'passed', then git add -A, then git commit -m..."

**Same rule applies to the memory layer.**

- Preferences are context, not instructions. "I prefer functional patterns over classes" tells the agent who you are, not how to write code.
- Keep those in personal memory as context.
- Don't promote them into procedural skill steps, or your memory layer ossifies into a style guide that stops adapting.
- The audit question I run on every skill: is this line telling the agent how, or telling it what good looks like? If it's a how, it usually doesn't need to be

## What to watch out for

**Context budget bloat**

- **Problem:** 90K tokens loaded before the model thinks. Performance drops.
- **Solution:** Progressive disclosure. Load only matched skills. Truncate LESSONS.md. Top-k on episodic entries.

**Stale skills**

- **Problem:** API or dependency changes, skill keeps running old instructions confidently.
- **Solution:** Version-date every manifest entry. Flag anything untouched 60+ days for review.

**Unsafe composition**

- **Problem:** Two safe skills combine into something destructive (e.g., merge-to-main + auto-push = accidental deploy).
- **Solution:** Put constraints in pre\_tool\_call, not inside skills. Skills don't know about each other; the hook does.

**Literal execution**

- **Problem**: Agent follows procedural skills step-by-step even when steps don't make sense (runs commit/push even after failing tests).
- **Solution:** Write destinations and fences, not driving directions.

**Stale workspace**

- **Problem:** WORKSPACE.md isn't cleared after a task, agent wakes up thinking it's still mid-task.
- Solution: Dream cycle archives workspaces older than 2 days. Also add a reset step to every task-completion skill.

**Error amplification loops**

- **Problem:** Bad lesson → flawed skill → more failures → lesson reinforced. Becomes load-bearing.
- **Solution:** Dream cycle decay handles most of it. Also manually read LESSONS.md every few weeks and git revert anything wrong. Don't automate this part.

## Things I would do differently

- **Write memory-manager on day one, not week three.**
- **Build the four-layer memory separation from the start.**
- **Keep the brain repo separate from code repos.** I
- **Start with fewer skills.**
- **Create context-rich skills rather than procedure-based skills.**
- **Build the protocol layer on day one, not week six.**

For personal coding agents the thin heartbeat plus a permissions file is enough.

If you are running agents against production systems you will eventually want full tool schemas and approval hooks.

My advice is to run the thin version for a few weeks first.

It will show you exactly where the guardrails need to go because the agent will try to do something it should not, and you will know.

## Conclusion

Right now this system accumulates memory from one person using one agent. But agents can be forked and duplicated in ways humans cannot. A lesson one agent learns can be shared across every agent in a team.

The model you can swap whenever something better ships. The skills and memory you cannot replace. They encode your specific mistakes, your specific decisions, your specific way of working.

Own your memory. Own your skills. Keep them in plain files and git where no one can take them from you. The thesis is inspired by Harrison Chase ( The CEO of Langchain)

> Apr 11

I built the first version in an afternoon. The complete stack took a weekend. It has been getting better every day since, without me touching it

Disclaimers and Disclosures This article was researched and written by the author, and it was edited by an AI model, Minimax M2.7. The thumbnail was taken off Pinterest. **Harrison Chase** — "Your Harness, Your Memory" [https://blog.langchain.com/your-harness-your-memory/](https://blog.langchain.com/your-harness-your-memory/)

**Vivek Trivedi** — "The Anatomy of an Agent Harness" [https://blog.langchain.com/the-anatomy-of-an-agent-harness/](https://blog.langchain.com/the-anatomy-of-an-agent-harness/)

**Zhou et al.** — "Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering" [https://arxiv.org/abs/2604.08224](https://arxiv.org/abs/2604.08224)