#!/usr/bin/env python3.10
import json
from pathlib import Path

extracted = json.loads(Path('.graphify_extracted.json').read_text())
valid_types = {'code', 'document', 'image', 'paper'}

# Filter out nodes with id containing 'uncached'
filtered_nodes = []
for node in extracted['nodes']:
    if 'uncached' in node.get('id', ''):
        continue
    filtered_nodes.append(node)
extracted['nodes'] = filtered_nodes

for node in extracted['nodes']:
    if node.get('type') == 'file':
        node['file_type'] = 'paper'
    elif node.get('type') == 'concept':
        node['file_type'] = 'document'
    else:
        node['file_type'] = 'document'
    # Ensure file_type is valid
    if node['file_type'] not in valid_types:
        node['file_type'] = 'document'

Path('.graphify_extracted_fixed.json').write_text(json.dumps(extracted, indent=2))
print(f"Fixed file_type fields, kept {len(extracted['nodes'])} nodes")