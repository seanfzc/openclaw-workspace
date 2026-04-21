#!/usr/bin/env python3
"""
Main render script: reads a problem card and generates SVG + render note.
"""

import yaml
import sys
import os
import shutil
from pathlib import Path

# Add templates directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'templates'))

try:
    from bar_model import create_bar_model
except ImportError:
    print("Warning: Could not import bar_model template")

try:
    from jinja2 import Template
except ImportError:
    print("Warning: Jinja2 not installed; render notes will be basic.")

def load_card(yaml_path):
    """Load problem card YAML."""
    with open(yaml_path, 'r') as f:
        return yaml.safe_load(f)

def ensure_dir(path):
    """Ensure output directory exists."""
    Path(path).mkdir(parents=True, exist_ok=True)

def render_bar_model(card, output_dir):
    """Render bar model using matplotlib template."""
    data = card.get('data', {})
    labels = data.get('labels', ['A', 'B'])
    values = data.get('values', [1, 1])
    colors = data.get('colors')
    
    svg_path = Path(output_dir) / f"{card['id']}.svg"
    
    # Import and call create_bar_model
    from bar_model import create_bar_model
    create_bar_model(
        labels=labels,
        values=values,
        colors=colors,
        title=card.get('title', 'Bar Model'),
        output_path=str(svg_path)
    )
    return svg_path

def create_render_note(card, output_dir):
    """Generate a markdown render note."""
    template_path = Path(__file__).parent.parent / 'templates' / 'render_note.md.j2'
    if template_path.exists():
        with open(template_path, 'r') as f:
            template_content = f.read()
        try:
            from jinja2 import Template
            template = Template(template_content)
            rendered = template.render(**card, **card.get('data', {}))
        except:
            # Fallback simple note
            rendered = f"""# Render {card.get('id', 'unknown')}
Title: {card.get('title', '')}
Description: {card.get('description', '')}
"""
    else:
        rendered = f"# Render {card.get('id', 'unknown')}\n\nNo template found."
    
    note_path = Path(output_dir) / f"{card['id']}.md"
    with open(note_path, 'w') as f:
        f.write(rendered)
    return note_path

def main():
    if len(sys.argv) < 2:
        print("Usage: python render.py <problem_card.yaml>")
        print("Example: python render.py ../problem_cards/sample.yaml")
        sys.exit(1)
    
    yaml_path = sys.argv[1]
    if not os.path.exists(yaml_path):
        print(f"Error: File {yaml_path} not found.")
        sys.exit(1)
    
    card = load_card(yaml_path)
    card_id = card.get('id', 'Render-001')
    
    # Determine output directory
    output_dir = card.get('output_dir', f"outputs/{card_id}")
    ensure_dir(output_dir)
    
    print(f"Rendering {card_id}...")
    
    # Copy problem card to output directory for reference
    shutil.copy(yaml_path, Path(output_dir) / f"{card_id}.yaml")
    
    # Render diagram based on type
    diagram_type = card.get('diagram_type', 'bar_model')
    if diagram_type == 'bar_model':
        svg_path = render_bar_model(card, output_dir)
        print(f"  Diagram: {svg_path}")
    else:
        print(f"Unsupported diagram type: {diagram_type}")
        sys.exit(1)
    
    # Create render note
    note_path = create_render_note(card, output_dir)
    print(f"  Note:    {note_path}")
    
    print(f"Render complete. Output in {output_dir}/")

if __name__ == "__main__":
    main()