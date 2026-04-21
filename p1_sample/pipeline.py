#!/usr/bin/env python3.10
import json
from pathlib import Path
from graphify.build import build_from_json
from graphify.cluster import cluster
from graphify.analyze import god_nodes, surprising_connections, suggest_questions
from graphify.report import generate
from graphify.export import to_json, to_html, to_wiki
from graphify.export import to_svg, to_canvas  # optional

# Load extracted data
extracted = json.loads(Path('.graphify_extracted_fixed.json').read_text())

# Build graph
print("Building graph...")
graph = build_from_json(extracted)

# Cluster
print("Clustering...")
communities = cluster(graph)
print(f"Found {len(communities)} communities")

# Analyze
print("Analyzing...")
god = god_nodes(graph, communities)
surprising = surprising_connections(graph, communities)
questions = suggest_questions(graph, communities)
print(f"God nodes: {len(god)}")
print(f"Surprising connections: {len(surprising)}")
print(f"Suggested questions: {len(questions)}")

# Generate report
print("Generating report...")
report = generate(graph, communities, god, surprising, questions)
out_dir = Path('graphify-out')
out_dir.mkdir(exist_ok=True)
report_path = out_dir / 'GRAPH_REPORT.md'
report_path.write_text(report)
print(f"Report saved to {report_path}")

# Export JSON
print("Exporting JSON...")
json_dict = to_json(graph, communities, out_dir / 'graph.json')
print(f"JSON saved to {out_dir / 'graph.json'}")

# Export HTML visualization
print("Exporting HTML...")
html = to_html(graph, communities, out_dir / 'graph.html')
print(f"HTML saved to {out_dir / 'graph.html'}")

# Optional: Export to Obsidian wiki
print("Exporting Obsidian wiki...")
wiki_dir = out_dir / 'obsidian'
to_wiki(graph, communities, wiki_dir)
print(f"Obsidian wiki saved to {wiki_dir}")

print("Pipeline complete.")