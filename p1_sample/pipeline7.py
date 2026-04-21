#!/usr/bin/env python3.10
import json
from pathlib import Path
from graphify.build import build_from_json
from graphify.cluster import cluster
from graphify.analyze import god_nodes, surprising_connections, suggest_questions
from graphify.report import generate
from graphify.export import to_json, to_html
from graphify.wiki import to_wiki

# Load extracted data
extracted = json.loads(Path('.graphify_extracted_fixed2.json').read_text())
detection_result = json.loads(Path('.graphify_detect.json').read_text())

# Build graph
print("Building graph...")
graph = build_from_json(extracted)

# Cluster
print("Clustering...")
communities = cluster(graph)
print(f"Found {len(communities)} communities")

# Generate community labels
community_labels = {i: f"Community {i}" for i in range(len(communities))}

# Analyze
print("Analyzing...")
god = god_nodes(graph, top_n=10)
surprising = surprising_connections(graph, communities, top_n=5)
questions = suggest_questions(graph, communities, community_labels, top_n=5)
print(f"God nodes: {len(god)}")
print(f"Surprising connections: {len(surprising)}")
print(f"Suggested questions: {len(questions)}")

# Generate report
print("Generating report...")
root = Path('.')
token_cost = extracted.get('input_tokens', 0) + extracted.get('output_tokens', 0)
report = generate(graph, communities, god, surprising, questions,
                  detection_result, token_cost, root)
out_dir = Path('graphify-out')
out_dir.mkdir(exist_ok=True)
report_path = out_dir / 'GRAPH_REPORT.md'
report_path.write_text(report)
print(f"Report saved to {report_path}")

# Export JSON
print("Exporting JSON...")
to_json(graph, communities, str(out_dir / 'graph.json'))

# Export HTML visualization
print("Exporting HTML...")
to_html(graph, communities, str(out_dir / 'graph.html'))

# Export to Obsidian wiki
print("Exporting Obsidian wiki...")
wiki_dir = out_dir / 'obsidian'
to_wiki(graph, communities, wiki_dir)
print(f"Obsidian wiki saved to {wiki_dir}")

print("Pipeline complete.")