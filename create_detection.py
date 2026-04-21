#!/usr/bin/env python3
import json
from pathlib import Path

# Read selected paths
selected_paths = []
with open('/Users/zcaeth/.openclaw/workspace/selected_pdfs.txt') as f:
    selected_paths = [line.strip() for line in f if line.strip()]

print(f"Selected {len(selected_paths)} PDFs")

# Create detection structure
detection = {
    "files": {
        "code": [],
        "document": [],
        "paper": selected_paths,
        "image": []
    },
    "total_files": len(selected_paths),
    "total_words": 0,  # Will be updated after extraction
    "needs_graph": True,
    "warning": None,
    "skipped_sensitive": [],
    "graphifyignore_patterns": 0
}

# Save to file
output_path = '/Users/zcaeth/.openclaw/workspace/graphify-pilot/.graphify_detect.json'
Path(output_path).parent.mkdir(parents=True, exist_ok=True)
with open(output_path, 'w') as f:
    json.dump(detection, f, indent=2)

print(f"Detection saved to {output_path}")