---
title: "Obsidian + ByteRover: Your Personal Knowledge Base Now Lives Inside Every AI Coding Agent"
source: "https://x.com/kevinnguyendn/status/2043567698253427144"
author:
  - "[[@kevinnguyendn]]"
published: 2026-04-13
created: 2026-04-16
description: "You’ve spent months, maybe years building a second brain in Obsidian. It’s packed with architecture decisions, design sketches, and deep-div..."
tags:
  - "clippings"
---
![Image](https://pbs.twimg.com/media/HFw4a-EacAAWS5j?format=jpg&name=large)

You’ve spent months, maybe years building a second brain in **Obsidian**. It’s packed with architecture decisions, design sketches, and deep-dive research on things like authentication patterns.

But there’s a problem: The moment you open a coding agent like **Claude Code, Cursor or Codex**, that knowledge vanishes. When you ask your agent to refactor a module, it has no idea you’ve already documented the exact trade-offs and strategies required. Your personal notes and your codebase live in two completely different worlds.

**ByteRover finally bridges that gap.**

## The Structural Accident That Makes It Work

ByteRover doesn't need a complex bridge because it shares the same DNA as Obsidian. Both systems are built on a simple, zero-infra philosophy:

- **Directories of Markdown files** with **YAML frontmatter, organized into folders, with no database**.
- No proprietary format, no binary blobs, no encoding layer. Just .md files on disk.

Because your vault is structurally identical to a ByteRover Context Tree, ByteRover can treat your notes as a native knowledge source.

## Why This Changes Your Workflow

Using the ByteRover’s **source feature** (released in [ByteRover CLI v3.2.0](https://github.com/campfirein/byterover-cli/releases/tag/v3.2.0)), you can now link your Obsidian vault as a read-only knowledge source:

- **Federated Search:** Search across your vault knowledge and your project code in a single query.
- **Scale with Every Project**: You can link the same curated vault to every project you own. Curate once and search from everywhere.
- **Universal Support (by connecting to 22+ coding agents):** Your vault becomes available to **22+ coding agents** (including Claude Code, Cursor, Windsurf and more) with zero extra configuration.
- **Read-Only Safety:** Agents can read and learn from your notes to give better suggestions, but they can **never modify or delete** your vault content.
- **Zero Friction:** You don’t need Obsidian running. No plugins, no REST APIs, and no API keys are required. It’s just Markdown on disk.

## Setup: 4 steps, 5 minutes

**Step 1 - Initialize ByteRover in your vault**

```text
cd ~/Documents/MyVault
brv
```

Running brv starts the TUI for initial setup. Use /providers to set up your LLM and /connectors to link your favorite coding agent. Once done, run /exit.

Note: ByteRover creates a .brv/ directory. If you want it invisible in Obsidian, just add .brv to your .obsidianignore file.

**Step 2 - Curate your vault knowledge**

Instruct your coding agent (while inside your vault directory:

```text
> curate the knowledge from ./Architecture/ to context tree
> curate all notes from ./Decisions/ to context tree
> curate the knowledge from ./Design/api-design.md to context tree
```

The agent extracts the knowledge and writes it into .brv/context-tree/making it structured, indexed, and searchable.

**Step 3 - Link the vault to your project**

Switch to any project where you want vault knowledge available:

```text
cd ~/code/my-project
brv source add ~/Documents/MyVault
```

ByteRover validates the link and registers it as a read-only source. You can verify this with brv source list.

You can verify the link with /brv source list

```text
Knowledge Sources:
   MyVault → /Users/you/Documents/MyVault (valid)
```

**Step 4 - Search across everything**

Now, from your dev project, you can run:

```text
brv search "authentication flow"
```

Results will show both project code and vault notes (tagged with a \[MyVault\] prefix). Even better, ask a question:

```text
brv query "What did we decide about the auth refresh token strategy?"
```

## Practical tips

- **Start Small:** Don't curate your whole vault at once. Pick the 3 folders most relevant to your current work (e.g., /Architecture, /Design).
- **Re-curate when notes change:** The context-tree is a snapshot. If you make a major update to a note, tell your agent: "re-curate ./Architecture/auth-decisions.md."
- **Check health:** Run brv source list to ensure your links are active and healthy.
- **Use aliases for clarity:** When linking from multiple projects, give your vault a clear alias:

```text
brv source add ~/Documents/MyVault --alias vault
```

## Get Started in Seconds

Check the repo: [https://github.com/campfirein/byterover-cli.git](https://github.com/campfirein/byterover-cli.git)

Install the CLI: curl -fsSL <[https://byterover.dev/install.sh](https://byterover.dev/install.sh)\> | sh

Make your Obsidian native to every coding agents:

```text
brv source add ~/Documents/YourVault
```