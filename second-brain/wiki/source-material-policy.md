# Source Material Policy

The source set currently defines `raw/` as an unprocessed input area and explicitly states that AI systems must not modify files there. This establishes a strict separation between immutable source inputs and generated knowledge outputs.

## Summary
- `raw/.gitkeep` labels `raw/` as storage for unprocessed source material.
- The same source states that AI should never edit those raw files directly.
- This implies all transformed, structured, or summarized content must live outside `raw/`, such as in `wiki/`.

## Related Topics
- [[INDEX]]
- [[prompt-optimization-patterns]]
- [[x-virality-playbook]]
- [[agentic-parenting-systems]]
