#!/usr/bin/env python3
"""
Generate CORRECT Q21 diagram based on ACTUAL ACS Junior exam paper
Key insight: Both quarter circles share center O!
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Wedge, Arc
import numpy as np
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent / "artifacts" / "renders" / "exam-quality-baseline-v3"

def create_q21_final():
    """
    CORRECT Q21 geometry (from ACS Junior exam paper):
    - Center O with two overlapping quarter circles
    - Quarter circle OAC: from OA to OC
    - Quarter circle OBD: from OB to OD
    - Shaded sector OBC: the overlap
    - All radii = 10 cm
    """
    
    fig, ax = plt.subplots(figsize=(6.5, 5.5), dpi=150)
    ax.set_xlim(-2, 12)
    ax.set_ylim(-2, 11)
    ax.set_aspect('equal')
    ax.axis('off')
    
    r = 10
    O = (0, 0)
    
    # The two quarter circles both have center O
    # Quarter circle OAC: spans from A to C
    # Quarter circle OBD: spans from B to D
    # They overlap in sector OBC
    
    # From the diagram in exam paper:
    # - A is at bottom left (angle ~225° or -135° from positive x)
    # - D is at bottom right (angle ~315° or -45° from positive x)
    # - B and C are between them, creating the overlap
    
    # Actually, looking at the exam diagram:
    # O is at the bottom
    # A is left, D is right (forming a semi-circle shape)
    # B and C are between A and D on the arc
    
    # The two quarter circles are:
    # Q1: OAC - from OA to OC (going counter-clockwise)
    # Q2: OBD - from OB to OD (going clockwise)
    
    # Let me place them:
    # O at origin
    # A at angle 180° (left)
    # D at angle 0° (right) 
    # B and C somewhere between
    
    # Actually, looking more carefully at the exam image:
    # It's like a semi-circle with center O at bottom
    # A ----arc---- B -shaded- C ----arc---- D
    #          \            /
    #           \    O    /
    #            \      /
    
    # So:
    # - A is at one end of the semi-circle
    # - D is at the other end
    # - B and C are points on the arc between A and D
    # - Sector OBC is shaded (the pie slice from O to B to C)
    
    # Two quarter circles means 90° each
    # If they overlap, the total span is less than 180°
    
    # Let me define:
    # Quarter circle 1: from angle θ1 to θ1+90°
    # Quarter circle 2: from angle θ2 to θ2+90°
    # They overlap between max(θ1, θ2) and min(θ1+90°, θ2+90°)
    
    # From exam diagram, looks like:
    # Q1 spans from ~150° to ~240° (left side)
    # Q2 spans from ~300° to ~30° (right side, wrapping)
    # Wait, that doesn't overlap...
    
    # Let me reconsider. Looking at exam image again:
    # The shaded region OBC is a SECTOR (pie slice)
    # It's bounded by radii OB, OC and arc BC
    
    # The figure shows:
    # - Point O at bottom
    # - Arc from A to D forming a semi-circle shape
    # - B and C are on this arc
    # - Shaded region is sector OBC
    
    # Two quarter circles:
    # - Q1: OAC (from OA to OC) - this is one quarter circle
    # - Q2: OBD (from OB to OD) - this is another quarter circle
    # - They overlap at sector OBC
    
    # So the angles must be:
    # A at some angle, C at A+90°
    # B at some angle, D at B+90°
    # B is between A and C, so sectors overlap
    
    # Let's say:
    # A at 180° (pointing left)
    # C at 270° (pointing down) - this makes Q1 a quarter circle
    # B at 225° (between A and C)
    # D at 315° (between C and... wait)
    
    # Actually if Q2 is OBD and B is at 225°, D would be at 225+90=315°
    # But then C is at 270°, D at 315°, so C is between B and D
    # This works!
    
    # Let me calculate angles:
    angle_A = 180  # π radians
    angle_C = 270  # 3π/2 radians (A + 90°)
    angle_B = 225  # 5π/4 radians (between A and C)
    angle_D = 315  # 7π/4 radians (B + 90°)
    
    # Verify Q2 is quarter circle: B to D = 315 - 225 = 90° ✓
    # Overlap is from B (225°) to C (270°) = 45° sector
    
    # Draw quarter circle OAC (from A to C)
    theta1 = np.linspace(np.radians(angle_A), np.radians(angle_C), 100)
    x1 = r * np.cos(theta1)
    y1 = r * np.sin(theta1)
    ax.plot(x1, y1, 'k-', linewidth=2.5)
    
    # Draw quarter circle OBD (from B to D)
    theta2 = np.linspace(np.radians(angle_B), np.radians(angle_D), 100)
    x2 = r * np.cos(theta2)
    y2 = r * np.sin(theta2)
    ax.plot(x2, y2, 'k-', linewidth=2.5)
    
    # Draw radii
    # OA
    ax.plot([0, r*np.cos(np.radians(angle_A))], 
            [0, r*np.sin(np.radians(angle_A))], 'k-', linewidth=2.5)
    # OC
    ax.plot([0, r*np.cos(np.radians(angle_C))], 
            [0, r*np.sin(np.radians(angle_C))], 'k-', linewidth=2.5)
    # OB
    ax.plot([0, r*np.cos(np.radians(angle_B))], 
            [0, r*np.sin(np.radians(angle_B))], 'k-', linewidth=2.5)
    # OD
    ax.plot([0, r*np.cos(np.radians(angle_D))], 
            [0, r*np.sin(np.radians(angle_D))], 'k-', linewidth=2.5)
    
    # Shade sector OBC (the overlap)
    theta_shade = np.linspace(np.radians(angle_B), np.radians(angle_C), 50)
    x_shade = [0] + list(r * np.cos(theta_shade)) + [0]
    y_shade = [0] + list(r * np.sin(theta_shade)) + [0]
    
    shade = patches.Polygon(list(zip(x_shade, y_shade)), 
                           facecolor='#5B9BD5', edgecolor='darkblue', 
                           linewidth=2, alpha=0.5)
    ax.add_patch(shade)
    
    # Add diagonal hatching to shaded region only
    for angle in np.linspace(angle_B + 5, angle_C - 5, 5):
        rad = np.radians(angle)
        x_line = [0.5 * r * np.cos(rad), 0.9 * r * np.cos(rad)]
        y_line = [0.5 * r * np.sin(rad), 0.9 * r * np.sin(rad)]
        ax.plot(x_line, y_line, 'b--', linewidth=1, alpha=0.6)
    
    # Mark and label points
    points = {
        'A': (r*np.cos(np.radians(angle_A)), r*np.sin(np.radians(angle_A))),
        'B': (r*np.cos(np.radians(angle_B)), r*np.sin(np.radians(angle_B))),
        'C': (r*np.cos(np.radians(angle_C)), r*np.sin(np.radians(angle_C))),
        'D': (r*np.cos(np.radians(angle_D)), r*np.sin(np.radians(angle_D))),
        'O': (0, 0)
    }
    
    for label, (x, y) in points.items():
        ax.plot(x, y, 'ko', markersize=10, zorder=5)
    
    # Labels with offsets
    ax.text(points['A'][0]-0.8, points['A'][1], 'A', fontsize=14, 
            ha='center', fontweight='bold')
    ax.text(points['B'][0]-0.6, points['B'][1]+0.5, 'B', fontsize=14, 
            ha='center', fontweight='bold', color='darkred')
    ax.text(points['C'][0]+0.6, points['C'][1]+0.5, 'C', fontsize=14, 
            ha='center', fontweight='bold', color='darkred')
    ax.text(points['D'][0]+0.8, points['D'][1], 'D', fontsize=14, 
            ha='center', fontweight='bold')
    ax.text(points['O'][0], points['O'][1]-0.8, 'O', fontsize=14, 
            ha='center', fontweight='bold')
    
    # Label shaded region
    ax.text(-3, -3, 'Shaded OBC', fontsize=11, ha='center', 
            fontweight='bold', color='darkblue',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.9))
    ax.text(-3, -3.8, '30 cm²', fontsize=10, ha='center', color='darkblue')
    
    # Radius label
    ax.annotate('', xy=(r*np.cos(np.radians(angle_A))-0.3, 
                       r*np.sin(np.radians(angle_A))+0.3), 
                xytext=(0.3, -0.3),
                arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
    ax.text(-2.5, -1, '10 cm', fontsize=11, ha='center', fontweight='bold')
    
    ax.set_title('Q21: Overlapping Quarter Circles (ACS Junior)', 
                fontsize=13, pad=15, fontweight='bold')
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'Q21_final_correct.png', dpi=150, 
                bbox_inches='tight', facecolor='white')
    plt.close()
    
    print("✅ Q21 FINAL correct diagram generated")
    print("   Both quarter circles share center O")
    print("   Shaded OBC is a sector (pie slice)")
    print("   All points A, B, C, D on the outer arc")

if __name__ == "__main__":
    create_q21_final()
