#!/usr/bin/env python3.10
import json
from pathlib import Path
from graphify.build import build_from_json
from graphify.export import to_json

extracted = json.loads(Path('.graphify_extracted.json').read_text())
graph = build_from_json(extracted)

# Ensure output directory
out_dir = Path('graphify-out')
out_dir.mkdir(exist_ok=True)

graph_dict = to_json(graph)
graph_path = out_dir / 'graph.json'
graph_path.write_text(json.dumps(graph_dict, indent=2))
print(f"Graph built: {len(graph_dict.get('nodes', []))} nodes, {len(graph_dict.get('edges', []))} edges")
print(f"Saved to {graph_path}")