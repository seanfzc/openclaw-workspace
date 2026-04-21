#!/usr/bin/env python3.10
import json
from pathlib import Path

extracted = json.loads(Path('.graphify_extracted.json').read_text())
for node in extracted['nodes']:
    if node.get('type') == 'file':
        node['file_type'] = 'pdf'
    if 'file_type' not in node:
        node['file_type'] = 'unknown'

Path('.graphify_extracted_fixed.json').write_text(json.dumps(extracted, indent=2))
print("Fixed file_type fields")