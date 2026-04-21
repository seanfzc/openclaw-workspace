#!/usr/bin/env python3
"""
Render geometry diagrams for each problem in 02-Geometry/problems/
Output PDFs to 05-Backend/artifacts/renders/
"""
import os
import yaml
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from datetime import datetime
import sys

# Paths
BASE = "/Users/zcaeth/.openclaw/workspace/ATOM-SG Pilot"
PROBLEMS_DIR = os.path.join(BASE, "02-Geometry/problems")
RENDERS_DIR = os.path.join(BASE, "05-Backend/artifacts/renders")
PLAN_PATH = os.path.join(BASE, "02-Geometry/Problem-Pack-Plan.md")

# Ensure output directory exists
os.makedirs(RENDERS_DIR, exist_ok=True)

# Mapping from nano-node to geometry type (G1, G2, G3, G4)
def parse_plan():
    """Parse plan to map problem ID to geometry type (G1-G4)"""
    mapping = {}
    with open(PLAN_PATH, 'r') as f:
        lines = f.readlines()
    current_section = None
    for line in lines:
        line = line.strip()
        if line.startswith('### G'):
            # e.g., "### G1 Angle Reasoning (8 items)"
            parts = line.split()
            if parts[1].startswith('G') and parts[1][1].isdigit():
                current_section = parts[1]  # G1, G2, etc.
        if line.startswith('| G'):
            cols = [c.strip() for c in line.split('|') if c.strip()]
            if len(cols) >= 2 and cols[0].startswith('G'):
                pid = cols[0]
                mapping[pid] = current_section
    return mapping

def load_problem(md_path):
    """Load YAML frontmatter from markdown file."""
    with open(md_path, 'r') as f:
        content = f.read()
    # Split frontmatter
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            frontmatter = parts[1]
            try:
                data = yaml.safe_load(frontmatter)
                return data
            except yaml.YAMLError as e:
                print(f"YAML error in {md_path}: {e}")
    return {}

def draw_angle_diagram(ax):
    """Draw a simple angle diagram (protractor)."""
    # Draw two rays from origin
    ax.plot([0, 3], [0, 0], 'k-', lw=2)
    ax.plot([0, 2], [0, 2], 'k-', lw=2)
    # Arc
    import math
    arc = patches.Arc((0,0), 2, 2, angle=0, theta1=0, theta2=45, color='blue', lw=2)
    ax.add_patch(arc)
    ax.text(1, 0.2, '45°', fontsize=12)
    ax.set_xlim(-1, 4)
    ax.set_ylim(-1, 4)
    ax.set_aspect('equal')
    ax.axis('off')

def draw_rectangle_diagram(ax):
    """Draw a rectangle."""
    rect = patches.Rectangle((1,1), 5, 3, linewidth=2, edgecolor='black', facecolor='lightblue')
    ax.add_patch(rect)
    ax.set_xlim(0, 7)
    ax.set_ylim(0, 5)
    ax.set_aspect('equal')
    ax.axis('off')

def draw_cuboid_diagram(ax):
    """Draw a simple 3D cuboid."""
    # front face
    rect = patches.Rectangle((1,1), 4, 3, linewidth=2, edgecolor='black', facecolor='lightgreen')
    ax.add_patch(rect)
    # back face offset
    ax.plot([1,1.5], [1,0.5], 'k-', lw=2)
    ax.plot([5,5.5], [1,0.5], 'k-', lw=2)
    ax.plot([1,1.5], [4,3.5], 'k-', lw=2)
    ax.plot([5,5.5], [4,3.5], 'k-', lw=2)
    ax.set_xlim(0, 7)
    ax.set_ylim(0, 5)
    ax.set_aspect('equal')
    ax.axis('off')

def draw_circle_diagram(ax):
    """Draw a circle with radius."""
    circle = patches.Circle((3,3), 2, linewidth=2, edgecolor='black', facecolor='lightyellow')
    ax.add_patch(circle)
    # radius line
    ax.plot([3,5], [3,3], 'r-', lw=2)
    ax.text(4, 2.8, 'r', fontsize=12, color='red')
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 6)
    ax.set_aspect('equal')
    ax.axis('off')

def draw_pie_chart_diagram(ax):
    """Draw a simple pie chart sector."""
    import math
    wedge = patches.Wedge((3,3), 2, 0, 90, linewidth=2, edgecolor='black', facecolor='orange')
    ax.add_patch(wedge)
    ax.text(3, 5.5, '90° sector', fontsize=12, ha='center')
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 6)
    ax.set_aspect('equal')
    ax.axis('off')

def render_diagram(problem_id, geometry_type, problem_text):
    """Create a diagram based on geometry type."""
    fig, ax = plt.subplots(figsize=(4, 4))
    if geometry_type == 'G1':
        draw_angle_diagram(ax)
    elif geometry_type == 'G2':
        draw_rectangle_diagram(ax)
    elif geometry_type == 'G3':
        draw_cuboid_diagram(ax)
    elif geometry_type == 'G4':
        # Determine if circle or pie chart or triangle etc.
        if 'circle' in problem_text.lower() or 'circumference' in problem_text.lower():
            draw_circle_diagram(ax)
        elif 'pie chart' in problem_text.lower():
            draw_pie_chart_diagram(ax)
        else:
            # default triangle
            # draw a triangle
            ax.plot([1,4,2.5,1], [1,1,4,1], 'k-', lw=2)
            ax.set_aspect('equal')
            ax.axis('off')
    else:
        # default rectangle
        draw_rectangle_diagram(ax)
    
    # Add problem ID as title
    ax.set_title(f'{problem_id}: {geometry_type}', fontsize=10)
    plt.tight_layout()
    return fig

def main():
    # Parse plan mapping
    plan_map = parse_plan()
    print(f"Loaded mapping for {len(plan_map)} problems")
    
    # Iterate over problem files
    for filename in sorted(os.listdir(PROBLEMS_DIR)):
        if filename.startswith('G') and filename.endswith('.md'):
            pid = filename[:-3]  # remove .md
            geometry_type = plan_map.get(pid, 'G1')
            md_path = os.path.join(PROBLEMS_DIR, filename)
            data = load_problem(md_path)
            problem_text = data.get('problem', '')
            print(f"Rendering {pid} ({geometry_type})...")
            
            # Render diagram
            fig = render_diagram(pid, geometry_type, problem_text)
            
            # Generate timestamp
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            # geometry_type_simple = geometry_type.replace(' ', '_')
            pdf_filename = f"{pid}_{geometry_type}_{timestamp}.pdf"
            pdf_path = os.path.join(RENDERS_DIR, pdf_filename)
            
            # Save PDF
            fig.savefig(pdf_path, format='pdf', bbox_inches='tight')
            plt.close(fig)
            print(f"  Saved to {pdf_path}")
    
    print(f"All diagrams rendered to {RENDERS_DIR}")

if __name__ == '__main__':
    main()