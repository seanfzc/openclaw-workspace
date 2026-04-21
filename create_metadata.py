#!/usr/bin/env python3
"""
Create metadata JSON files for each rendered PDF.
"""
import os
import json
import yaml
from datetime import datetime

BASE = "/Users/zcaeth/.openclaw/workspace/ATOM-SG Pilot"
PROBLEMS_DIR = os.path.join(BASE, "02-Geometry/problems")
RENDERS_DIR = os.path.join(BASE, "05-Backend/artifacts/renders")
METADATA_DIR = os.path.join(BASE, "05-Backend/artifacts/metadata")

os.makedirs(METADATA_DIR, exist_ok=True)

def load_problem(md_path):
    """Load YAML frontmatter from markdown file."""
    with open(md_path, 'r') as f:
        content = f.read()
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            frontmatter = parts[1]
            try:
                data = yaml.safe_load(frontmatter)
                return data
            except yaml.YAMLError:
                # fallback: extract problem line
                lines = content.split('\n')
                problem = ''
                for line in lines:
                    if line.startswith('problem:'):
                        problem = line[8:].strip()
                return {'problem': problem}
    return {}

def parse_filename(filename):
    """Parse PDF filename to extract pid, geometry_type, timestamp."""
    # format: G001_G1_20260413_143401.pdf
    basename = filename[:-4]  # remove .pdf
    parts = basename.split('_')
    if len(parts) >= 4:
        pid = parts[0]
        geo = parts[1]
        timestamp = '_'.join(parts[2:])
        return pid, geo, timestamp
    return None, None, None

def main():
    manifest = []
    for filename in sorted(os.listdir(RENDERS_DIR)):
        if not filename.endswith('.pdf'):
            continue
        pid, geo, timestamp = parse_filename(filename)
        if pid is None:
            continue
        # Load problem data
        md_path = os.path.join(PROBLEMS_DIR, f"{pid}.md")
        problem_data = load_problem(md_path)
        
        metadata = {
            "problem_id": pid,
            "geometry_type": geo,
            "timestamp": timestamp,
            "pdf_filename": filename,
            "problem": problem_data.get('problem', ''),
            "subpathway": problem_data.get('subpathway', ''),
            "shadow": problem_data.get('shadow', ''),
            "notes": problem_data.get('notes', ''),
            "render_tool": "matplotlib",
            "render_version": "1.0"
        }
        
        # Write metadata JSON
        json_filename = filename.replace('.pdf', '.json')
        json_path = os.path.join(METADATA_DIR, json_filename)
        with open(json_path, 'w') as f:
            json.dump(metadata, f, indent=2)
        print(f"Created {json_filename}")
        
        # Add to manifest
        manifest.append({
            "problem_id": pid,
            "pdf": filename,
            "metadata": json_filename,
            "geometry_type": geo
        })
    
    # Write manifest
    manifest_path = os.path.join(RENDERS_DIR, 'manifest.json')
    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=2)
    print(f"Created manifest with {len(manifest)} entries at {manifest_path}")
    
    # Also create a simple README for renders
    readme_path = os.path.join(RENDERS_DIR, 'README.md')
    with open(readme_path, 'w') as f:
        f.write("# Rendered Diagrams\n\n")
        f.write(f"Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("| Problem ID | Geometry Type | PDF | Metadata |\n")
        f.write("|------------|---------------|-----|----------|\n")
        for entry in manifest:
            f.write(f"| {entry['problem_id']} | {entry['geometry_type']} | [{entry['pdf']}]({entry['pdf']}) | [{entry['metadata']}](../metadata/{entry['metadata']}) |\n")
    print(f"Created README.md")

if __name__ == '__main__':
    main()