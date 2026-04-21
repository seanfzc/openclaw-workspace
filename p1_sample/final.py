#!/usr/bin/env python3.10
import json
from pathlib import Path
from graphify.build import build_from_json
from graphify.cluster import cluster
from graphify.analyze import god_nodes, surprising_connections, suggest_questions
from graphify.export import to_json, to_html
from graphify.wiki import to_wiki

# Load extracted data
extracted = json.loads(Path('.graphify_extracted_fixed2.json').read_text())

print("=== Graphify Pipeline (Simplified) ===")
print("Building graph...")
graph = build_from_json(extracted)

print("Clustering...")
communities = cluster(graph)
print(f"Found {len(communities)} communities")

# Generate community labels
community_labels = {i: f"Community {i}" for i in range(len(communities))}

print("Analyzing...")
god = god_nodes(graph, top_n=10)
surprising = surprising_connections(graph, communities, top_n=5)
questions = suggest_questions(graph, communities, community_labels, top_n=5)

print("\n=== Analysis Results ===")
print(f"God nodes ({len(god)}):")
for node in god[:5]:
    print(f"  • {node.get('label', node.get('id'))}")
if len(god) > 5:
    print(f"  ... and {len(god)-5} more")

print(f"\nSurprising connections ({len(surprising)}):")
for conn in surprising[:3]:
    print(f"  • {conn.get('source', '')} ↔ {conn.get('target', '')} ({conn.get('reason', '')})")

print(f"\nSuggested questions ({len(questions)}):")
for q in questions[:3]:
    print(f"  • {q.get('question', '')}")

out_dir = Path('graphify-out')
out_dir.mkdir(exist_ok=True)

print(f"\n=== Exporting Outputs ===")
print("Exporting JSON...")
to_json(graph, communities, str(out_dir / 'graph.json'))

print("Exporting HTML visualization...")
to_html(graph, communities, str(out_dir / 'graph.html'))

print("Exporting Obsidian wiki...")
wiki_dir = out_dir / 'obsidian'
to_wiki(graph, communities, wiki_dir)

print(f"\n=== Output Files ===")
print(f"Graph JSON: {out_dir / 'graph.json'}")
print(f"Interactive HTML: {out_dir / 'graph.html'}")
print(f"Obsidian wiki: {wiki_dir}")
print(f"To view the graph, open {out_dir / 'graph.html'} in your browser.")
print(f"To explore the wiki, open {wiki_dir} in Obsidian.")

print("\nPipeline complete.")