#!/usr/bin/env python3
"""
Create conversation summary for token-efficient context management.

Usage:
  python create_conversation_summary.py --project "Project Name" --status "Current status" --decisions "Decision 1\nDecision 2" --tasks "Task 1\nTask 2" --learnings "Learning 1\nLearning 2" --actions "Action 1\nAction 2" --output summary.md
"""

import argparse
import datetime
import os

def create_summary(project, status, decisions, tasks, learnings, actions, cost_strategy="", wiki_integration="", open_questions=""):
    """Create conversation summary template."""
    
    # Get current timestamp
    now = datetime.datetime.now()
    timezone = "SGT"  # Default, could be made configurable
    timestamp = now.strftime(f"%Y-%m-%d %H:%M {timezone}")
    
    # Format bullet points if provided as strings
    def format_bullets(text):
        if not text:
            return "*No items*"
        lines = text.strip().split('\n')
        return '\n'.join([f"- {line.strip()}" for line in lines if line.strip()])
    
    summary = f"""# Conversation Summary: {project}
## Last Updated: {timestamp}
## Token-Efficient Context Management

## Current Project Status
{status if status else "[Brief status]"}

## Key Decisions & Progress
{format_bullets(decisions) if decisions else "- [Decision 1: What was decided and why]\n- [Decision 2: What was decided and why]"}

## Active Tasks
{format_bullets(tasks) if tasks else "- [Task 1: Status (pending/in progress/blocked)]\n- [Task 2: Status (pending/in progress/blocked)]"}

## Critical Learnings
{format_bullets(learnings) if learnings else "- [Learning 1: What we discovered]\n- [Learning 2: What we discovered]"}

## Next Immediate Actions
{format_bullets(actions) if actions else "1. [Action 1: Who/what/when]\n2. [Action 2: Who/what/when]"}

## Cost Management Strategy
{cost_strategy if cost_strategy else "- **API Decisions:** [Which APIs being used and why]\n- **Cost Tradeoffs:** [Manual vs automated decisions]\n- **Heuristic Rules:** [Applied cost-saving rules]"}

## Second Brain Integration
{wiki_integration if wiki_integration else "- **Wiki Updates:** [What's been added to Second Brain]\n- **Knowledge Compounding:** [How information is being preserved]\n- **Reference Links:** [[Page1]], [[Page2]]"}

## Open Questions
{format_bullets(open_questions) if open_questions else "1. [Question 1 needing answer]\n2. [Question 2 needing answer]"}

---
**Summary Purpose:** Token-efficient context management per Karpathy's cost insight + Second Brain architecture
**Update Frequency:** Every 4-6 conversation turns or significant progress milestones
**Max Tokens:** ~300 (concise, actionable)
"""
    
    return summary

def main():
    parser = argparse.ArgumentParser(description="Create conversation summary for token-efficient context management")
    parser.add_argument("--project", required=True, help="Project or topic name")
    parser.add_argument("--status", help="Current project status (1-2 sentences)")
    parser.add_argument("--decisions", help="Key decisions and progress (bullet points, one per line)")
    parser.add_argument("--tasks", help="Active tasks (bullet points, one per line)")
    parser.add_argument("--learnings", help="Critical learnings (bullet points, one per line)")
    parser.add_argument("--actions", help="Next immediate actions (numbered or bullet points)")
    parser.add_argument("--cost", help="Cost management strategy")
    parser.add_argument("--wiki", help="Second Brain integration updates")
    parser.add_argument("--questions", help="Open questions")
    parser.add_argument("--output", default="conversation_summary.md", help="Output file path")
    
    args = parser.parse_args()
    
    summary = create_summary(
        project=args.project,
        status=args.status,
        decisions=args.decisions,
        tasks=args.tasks,
        learnings=args.learnings,
        actions=args.actions,
        cost_strategy=args.cost,
        wiki_integration=args.wiki,
        open_questions=args.questions
    )
    
    # Write to file
    with open(args.output, 'w') as f:
        f.write(summary)
    
    print(f"Summary written to {args.output}")
    print(f"Estimated tokens: {len(summary.split()) * 1.3:.0f}")  # Rough estimate

if __name__ == "__main__":
    main()