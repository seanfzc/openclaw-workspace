#!/usr/bin/env python3
"""
Generate CORRECTED Q21 diagram v4
Include point A clearly
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Polygon
import numpy as np
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent / "artifacts" / "renders" / "exam-quality-baseline-v3"

def create_q21_v4():
    """
    Q21 with all points clearly labeled:
    - O = (0, 0) - center of Q1
    - A = (10, 0) - center of Q2 (also point B)
    - B = (10, 0) - on triangle OBC
    - C = (8, 6) - on Q1 arc
    - D = (10, 10) - top of Q2
    """
    
    fig, ax = plt.subplots(figsize=(6.5, 5.5), dpi=150)
    ax.set_xlim(-1, 12)
    ax.set_ylim(-1, 11)
    ax.set_aspect('equal')
    ax.axis('off')
    
    r = 10
    
    # Points
    O = (0, 0)
    A = (10, 0)  # Center of Q2
    B = (10, 0)  # Same as A - vertex of triangle
    C = (8, 6)
    D = (10, 10)
    
    # Draw Q1: center O(0,0)
    theta1 = np.linspace(0, np.pi/2, 100)
    x1 = r * np.cos(theta1)
    y1 = r * np.sin(theta1)
    ax.plot(x1, y1, 'k-', linewidth=2.5)
    ax.plot([0, r], [0, 0], 'k-', linewidth=2.5)
    ax.plot([0, 0], [0, r], 'k-', linewidth=2.5)
    
    # Draw Q2: center A(10,0)
    theta2 = np.linspace(np.pi/2, np.pi, 100)
    x2 = 10 + r * np.cos(theta2)
    y2 = r * np.sin(theta2)
    ax.plot(x2, y2, 'k-', linewidth=2.5)
    ax.plot([10, 0], [0, 0], 'k-', linewidth=2.5)
    ax.plot([10, 10], [0, r], 'k-', linewidth=2.5)
    
    # Shade triangle OBC
    triangle = Polygon([O, B, C], facecolor='#5B9BD5', edgecolor='darkblue', 
                      linewidth=2.5, alpha=0.4)
    ax.add_patch(triangle)
    
    # Mark all points
    ax.plot(O[0], O[1], 'ko', markersize=12, zorder=5)
    ax.plot(A[0], A[1], 'ko', markersize=12, zorder=5)
    ax.plot(C[0], C[1], 'ko', markersize=12, zorder=5)
    ax.plot(D[0], D[1], 'ko', markersize=10, zorder=5)
    
    # Labels - showing A and B are the same point
    ax.text(O[0]-0.7, O[1]-0.7, 'O', fontsize=16, ha='center', fontweight='bold')
    ax.text(A[0]+0.9, A[1]-0.7, 'A=B', fontsize=16, ha='center', fontweight='bold', color='darkred')
    ax.text(C[0]+0.8, C[1]+0.4, 'C', fontsize=16, ha='center', fontweight='bold', color='darkred')
    ax.text(D[0]+0.7, D[1]+0.4, 'D', fontsize=14, ha='center', fontweight='bold')
    
    # Dimension
    ax.annotate('', xy=(10, -0.3), xytext=(0, -0.3),
                arrowprops=dict(arrowstyle='<->', color='black', lw=2))
    ax.text(5, -1.1, '10 cm', fontsize=12, ha='center', fontweight='bold')
    
    # Label the shaded region
    ax.text(6.5, 2.2, 'Shaded area', fontsize=11, ha='center', 
            fontweight='bold', color='darkblue')
    ax.text(6.5, 1.5, 'OBC = 30 cm²', fontsize=11, ha='center', 
            fontweight='bold', color='darkblue')
    
    ax.set_title('Q21: Two Overlapping Quarter Circles', fontsize=13, pad=15, fontweight='bold')
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'Q21_v4_with_A.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ Q21 v4 generated with point A labeled")

if __name__ == "__main__":
    create_q21_v4()
