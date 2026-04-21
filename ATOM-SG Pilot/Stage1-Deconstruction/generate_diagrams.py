#!/usr/bin/env python3
"""
Generate exam-quality diagrams from parametric YAML specifications
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import yaml
import os

def load_yaml(yaml_path):
    """Load YAML specification"""
    with open(yaml_path, 'r') as f:
        return yaml.safe_load(f)

def generate_pie_chart(spec, output_path):
    """Generate pie chart for Q7"""
    segments = spec['diagram_requirements']['segments']
    labels = [s['label'] for s in segments]
    percentages = [s['percentage'] for s in segments]
    colors = [s['color'] for s in segments]
    
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.pie(percentages, labels=labels, colors=colors, autopct='%1.0f%%', startangle=90)
    ax.set_title(spec['title'], fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Generated: {output_path}")

def generate_container(spec, output_path):
    """Generate container diagram for Q9"""
    water_level = spec['visual_elements']['annotations'][2].split()[0]
    water_fraction = 0.75 if '¾' in water_level else 0.5
    
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12)
    ax.set_aspect('equal')
    
    # Tank outline
    tank = patches.Rectangle((2, 1), 6, 10, linewidth=3, edgecolor='#333333', facecolor='none')
    ax.add_patch(tank)
    
    # Water
    water_height = 10 * water_fraction
    water = patches.Rectangle((2, 1), 6, water_height, alpha=0.5, color=spec['diagram_requirements']['colors']['water'])
    ax.add_patch(water)
    
    # Tap
    ax.plot([5, 5], [11, 13], 'k-', linewidth=3)
    ax.plot([5, 5], [13, 13], 'k-o', markersize=10)
    
    # Labels
    ax.text(5, 14, 'Tap A', ha='center', fontsize=12, fontweight='bold')
    ax.text(5, 6, f'¾ full', ha='center', fontsize=12, color='blue')
    ax.text(5, 0.5, '8 min to fill', ha='center', fontsize=11)
    
    ax.axis('off')
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Generated: {output_path}")

def generate_line_graph(spec, output_path):
    """Generate line graph for Q10"""
    data = spec['visual_elements']['data_points']
    days = [d['day'] for d in data]
    sales = [d['sales'] for d in data]
    
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.plot(days, sales, 'o-', linewidth=2, markersize=8, color='#4169E1')
    
    # Mark highest
    max_idx = sales.index(max(sales))
    ax.plot(days[max_idx], sales[max_idx], '*', markersize=20, color='#FF6B6B')
    
    # Annotations
    ax.annotate('Day 3: 16 discounted', xy=(3, 76), xytext=(4, 85),
                arrowprops=dict(arrowstyle='->'), fontsize=10)
    ax.annotate('Highest', xy=(4, 95), xytext=(4.5, 90),
                fontsize=10, ha='center', fontweight='bold')
    
    ax.set_xlabel('Day', fontsize=12)
    ax.set_ylabel('Number of T-shirts', fontsize=12)
    ax.set_title(spec['title'], fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Generated: {output_path}")

def generate_complex_polygon(spec, output_path):
    """Generate complex polygon for Q13"""
    # Define vertices (approximate based on typical pentagon)
    A = np.array([2, 8])
    B = np.array([5, 9])
    C = np.array([7, 7])
    D = np.array([6, 4])
    E = np.array([3, 3])
    F = np.array([6, 6])  # On line DF
    H = np.array([4.5, 6.5])  # Intersection of AF and BD
    
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 11)
    ax.set_aspect('equal')
    
    # Polygon
    polygon = patches.Polygon([A, B, C, D, E], fill=False, linewidth=2, edgecolor='#333333')
    ax.add_patch(polygon)
    
    # Diagonals and extensions
    ax.plot([B[0], D[0]], [B[1], D[1]], 'r-', linewidth=1.5, alpha=0.7)  # BD
    ax.plot([A[0], D[0]], [A[1], D[1]], 'b-', linewidth=1.5, alpha=0.7)  # AD
    ax.plot([D[0], F[0]], [D[1], F[1]], 'b-', linewidth=1.5, alpha=0.7)  # DF
    ax.plot([F[0], E[0]], [F[1], E[1]], 'b-', linewidth=1.5, alpha=0.7)  # FE
    
    # Vertices
    for label, point in [('A', A), ('B', B), ('C', C), ('D', D), ('E', E)]:
        ax.plot(point[0], point[1], 'ko', markersize=6)
        ax.text(point[0]+0.3, point[1]+0.3, label, fontsize=11, fontweight='bold')
    
    # F and H
    ax.plot(F[0], F[1], 'ko', markersize=6)
    ax.text(F[0]+0.3, F[1], 'F', fontsize=11)
    ax.plot(H[0], H[1], 'ko', markersize=6)
    ax.text(H[0]+0.3, H[1]+0.3, 'H', fontsize=11, color='#45B7D1', fontweight='bold')
    
    # Angle arcs (simplified)
    # ∠AFB = 33°
    arc1 = patches.Arc(F, 0.5, 0.5, theta1=0, theta2=33, color='#FF6B6B', linewidth=1.5)
    ax.add_patch(arc1)
    ax.text(F[0]+0.7, F[1]+0.3, '33°', fontsize=9, color='#FF6B6B')
    
    # ∠DFE = 21°
    arc2 = patches.Arc(F, 0.5, 0.5, theta1=200, theta2=221, color='#4E79A7', linewidth=1.5)
    ax.add_patch(arc2)
    ax.text(F[0]-1, F[1]-0.5, '21°', fontsize=9, color='#4E79A7')
    
    # ∠BDE = 108°
    arc3 = patches.Arc(D, 0.8, 0.8, theta1=200, theta2=308, color='#FF6B6B', linewidth=1.5)
    ax.add_patch(arc3)
    ax.text(D[0]-1.2, D[1]+1, '108°', fontsize=9, color='#FF6B6B')
    
    # Target angles
    ax.text(H[0]-0.3, H[1]+0.5, 'x', fontsize=12, color='#45B7D1', fontweight='bold')
    ax.text(E[0]-0.5, E[1]+0.5, 'y', fontsize=12, color='#45B7D1', fontweight='bold')
    
    ax.axis('off')
    ax.set_title(spec['title'], fontsize=14, fontweight='bold', pad=20)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Generated: {output_path}")

def generate_all_diagrams():
    """Generate all 4 diagrams"""
    os.makedirs('output', exist_ok=True)
    
    # Q7 - Pie Chart
    print("\nGenerating Q7 diagram (Pie Chart)...")
    spec7 = load_yaml('Q7.yaml')
    generate_pie_chart(spec7, 'output/Q7_diagram.png')
    
    # Q9 - Container
    print("\nGenerating Q9 diagram (Container)...")
    spec9 = load_yaml('Q9.yaml')
    generate_container(spec9, 'output/Q9_diagram.png')
    
    # Q10 - Line Graph
    print("\nGenerating Q10 diagram (Line Graph)...")
    spec10 = load_yaml('Q10.yaml')
    generate_line_graph(spec10, 'output/Q10_diagram.png')
    
    # Q13 - Complex Polygon
    print("\nGenerating Q13 diagram (Complex Polygon)...")
    spec13 = load_yaml('Q13.yaml')
    generate_complex_polygon(spec13, 'output/Q13_diagram.png')
    
    print("\n" + "="*50)
    print("All diagrams generated in 'output/' folder")
    print("="*50)

if __name__ == "__main__":
    generate_all_diagrams()
