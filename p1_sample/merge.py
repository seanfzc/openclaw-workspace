#!/usr/bin/env python3.10
import json
from pathlib import Path

def load_or_empty(path, default):
    if Path(path).exists():
        try:
            return json.loads(Path(path).read_text())
        except:
            pass
    return default

ast = load_or_empty('.graphify_ast.json', {'nodes':[], 'edges':[], 'hyperedges':[]})
cached = load_or_empty('.graphify_cached.json', {'nodes':[], 'edges':[], 'hyperedges':[]})
semantic = load_or_empty('.graphify_semantic.json', {'nodes':[], 'edges':[], 'hyperedges':[]})

# Merge: semantic overwrites AST for same IDs
nodes_by_id = {}
edges_by_key = {}
hyperedges_by_id = {}

for node in ast.get('nodes', []) + cached.get('nodes', []) + semantic.get('nodes', []):
    nodes_by_id[node['id']] = node

for edge in ast.get('edges', []) + cached.get('edges', []) + semantic.get('edges', []):
    key = (edge['source'], edge['target'], edge.get('relation', ''))
    edges_by_key[key] = edge

for hyper in ast.get('hyperedges', []) + cached.get('hyperedges', []) + semantic.get('hyperedges', []):
    hyperedges_by_id[hyper['id']] = hyper

merged = {
    'nodes': list(nodes_by_id.values()),
    'edges': list(edges_by_key.values()),
    'hyperedges': list(hyperedges_by_id.values()),
    'input_tokens': (ast.get('input_tokens', 0) + 
                     cached.get('input_tokens', 0) + 
                     semantic.get('input_tokens', 0)),
    'output_tokens': (ast.get('output_tokens', 0) + 
                      cached.get('output_tokens', 0) + 
                      semantic.get('output_tokens', 0))
}

Path('.graphify_extracted.json').write_text(json.dumps(merged, indent=2))
print(f"Merged: {len(merged['nodes'])} nodes, {len(merged['edges'])} edges, {len(merged['hyperedges'])} hyperedges")