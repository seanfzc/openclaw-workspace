#!/usr/bin/env python3.10
import json
from pathlib import Path

extracted = json.loads(Path('.graphify_extracted_fixed.json').read_text())
valid_conf = {'AMBIGUOUS', 'EXTRACTED', 'INFERRED'}

for node in extracted['nodes']:
    if node.get('confidence') not in valid_conf:
        node['confidence'] = 'EXTRACTED'

for edge in extracted['edges']:
    if edge.get('confidence') not in valid_conf:
        edge['confidence'] = 'EXTRACTED'

for hyper in extracted['hyperedges']:
    if hyper.get('confidence') not in valid_conf:
        hyper['confidence'] = 'EXTRACTED'

Path('.graphify_extracted_fixed2.json').write_text(json.dumps(extracted, indent=2))
print("Fixed confidence values")