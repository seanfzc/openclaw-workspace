#!/usr/bin/env python3
"""
Exam-Quality Baseline Test Generator - Complete
Singapore PSLE Standards - 40 Questions
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, Polygon, Arc, Wedge
import numpy as np
import os
import yaml
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image as RLImage, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm

OUTPUT_DIR = "05-Backend/artifacts/renders/exam-quality-baseline"
os.makedirs(OUTPUT_DIR, exist_ok=True)
plt.switch_backend('Agg')

question_counter = 0
def get_next_q_num():
    global question_counter
    question_counter += 1
    return question_counter

def save_fig(fig, filename, dpi=150):
    filepath = os.path.join(OUTPUT_DIR, filename)
    fig.savefig(filepath, dpi=dpi, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close(fig)
    return filepath

def create_vrs(q_type, concepts, difficulty, visual_elements, reasoning_chain, traps):
    vrs = {
        "question_type": q_type,
        "complexity_tier": "Cross-Thread Collision" if q_type == "Word Problem" else "G5-G8 Composite",
        "fused_concepts": concepts,
        "difficulty": difficulty,
        "visual_elements": visual_elements,
        "reasoning_chain": reasoning_chain,
        "cognitive_traps": traps,
        "render_spec": {"dpi": 150, "font_family": "Arial", "line_weight": "0.5pt", "color_palette": "monochrome"}
    }
    return yaml.dump(vrs, default_flow_style=False, sort_keys=False)

all_questions = []
all_vrs = []
all_images = []

# ========== WORD PROBLEMS 1-20 ==========

def wp1():
    q = get_next_q_num()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 100); ax.set_ylim(0, 60); ax.axis('off')
    ax.annotate('', xy=(85, 45), xytext=(15, 15), arrowprops=dict(arrowstyle='->', color='black', lw=2))
    ax.plot(15, 15, 'ko', markersize=12); ax.plot(85, 45, 'ks', markersize=12)
    ax.text(15, 10, 'Factory A', ha='center', fontsize=10, fontweight='bold')
    ax.text(85, 50, 'Port B', ha='center', fontsize=10, fontweight='bold')
    ax.text(30, 25, 'Loaded: 60km/h', fontsize=10)
    ax.text(50, 35, 'Empty: 80km/h', fontsize=10)
    ax.annotate('', xy=(85, 15), xytext=(15, 15), arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
    ax.text(50, 8, '240 km', ha='center', fontsize=11, fontweight='bold')
    ax.text(50, 58, f'Question {q}: Delivery Route', ha='center', fontsize=12, fontweight='bold')
    fp = save_fig(fig, f'Q{q:02d}_diagram.png')
    vrs = create_vrs("Word Problem", ["Speed-Distance-Time", "Work Rate", "Unit Conversion"], "Hard",
                     ["Route diagram", "Distance markers"], ["Calculate times", "Account for loading"], ["Forgetting return journey"])
    txt = f"""Question {q}: A truck travels 240 km between Factory A and Port B at 60 km/h loaded, 80 km/h empty. Loading takes 45 min, unloading 30 min. Starts 6:00 a.m.
(a) Total time for one round trip? [3] (b) Round trips in 8-hour shift? [2] (c) With 1-hour lunch after every 3 trips, max deliveries in 12 hours? [3]"""
    return q, txt, vrs, fp

def wp2():
    q = get_next_q_num()
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_xlim(0, 100); ax.set_ylim(0, 50); ax.axis('off')
    tank = FancyBboxPatch((20, 10), 60, 30, boxstyle="round,pad=0.02", facecolor='lightblue', edgecolor='black', linewidth=2)
    ax.add_patch(tank)
    ax.axhline(y=18, xmin=0.22, xmax=0.78, color='blue', linewidth=3, alpha=0.4)
    ax.axhline(y=28, xmin=0.22, xmax=0.78, color='blue', linewidth=3, alpha=0.7)
    ax.axhline(y=35, xmin=0.22, xmax=0.78, color='blue', linewidth=3, alpha=0.8)
    ax.text(50, 15, 'Initial: 2/5', ha='center', fontsize=9)
    ax.text(50, 22, 'After Pipe A: 3/4', ha='center', fontsize=9)
    ax.text(50, 31, 'After Pipe B: Full', ha='center', fontsize=9)
    ax.text(50, 47, f'Question {q}: Water Tank', ha='center', fontsize=12, fontweight='bold')
    fp = save_fig(fig, f'Q{q:02d}_diagram.png')
    vrs = create_vrs("Word Problem", ["Fractions", "Ratio", "Rate"], "Hard",
                     ["Tank", "Water levels"], ["Calculate fractions", "Find rates"], ["Confusing fractions"])
    txt = f"""Question {q}: A tank is 2/5 full. Pipe A fills to 3/4 in 15 min. Pipe B (2x rate) fills remainder in 10 min. Pipe A = 12 L/min.
(a) Fraction filled by Pipe A? [2] (b) Ratio A:B? [1] (c) Total capacity? [3] (d) Time to fill 90% with both pipes? [2]"""
    return q, txt, vrs, fp

def wp3():
    q = get_next_q_num()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 100); ax.set_ylim(0, 60); ax.axis('off')
    for i in range(4):
        for j in range(3):
            x, y = 15 + i*18, 15 + j*12
            ax.add_patch(patches.Rectangle((x, y), 10, 6, linewidth=1.5, edgecolor='brown', facecolor='wheat'))
            ax.add_patch(Circle((x-3, y+3), 2, facecolor='tan', edgecolor='brown'))
            ax.add_patch(Circle((x+13, y+3), 2, facecolor='tan', edgecolor='brown'))
    ax.text(75, 50, 'Table: $x', fontsize=10)
    ax.text(75, 45, 'Chair: $(x-35)', fontsize=10)
    ax.text(50, 58, f'Question {q}: Furniture', ha='center', fontsize=12, fontweight='bold')
    fp = save_fig(fig, f'Q{q:02d}_diagram.png')
    vrs = create_vrs("Word Problem", ["Supposition", "Money"], "Hard", ["Grid layout"], ["Set up equation"], ["Wrong base assumption"])
    txt = f"""Question {q}: Each table costs $35 more than each chair. 12 tables + 48 chairs = $4,320.
(a) Cost of one table? [3] (b) Cost of 8 tables + 24 chairs? [2] (c) With 15% off tables, 20% off chairs, how much saved? [3]"""
    return q, txt, vrs, fp

def wp4():
    q = get_next_q_num()
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_xlim(0, 100); ax.set_ylim(0, 50); ax.axis('off')
    ax.plot([10, 90], [25, 25], 'k-', linewidth=2)
    for i, x in enumerate([20, 35, 50, 65, 80]):
        ax.plot(x, 25, 'ko', markersize=10)
        ax.text(x, 20, f'S{i+1}', ha='center', fontsize=10, fontweight='bold')
    ax.axvline(x=50, ymin=0.4, ymax=0.7, color='red', linestyle='--', linewidth=2)
    ax.text(50, 32, 'Average: 72', ha='center', fontsize=9, color='red')
    ax.text(50, 47, f'Question {q}: Test Scores', ha='center', fontsize=12, fontweight='bold')
    fp = save_fig(fig, f'Q{q:02d}_diagram.png')
    vrs = create_vrs("Word Problem", ["Average", "Number Patterns"], "Hard", ["Number line"], ["Express differences"], ["Wrong total calculation"])
    txt = f"""Question {q}: 5 students, average 72. Each score 8 marks higher than previous. Highest = 88.
(a) Lowest score? [2] (b) Total marks? [1] (c) How many passed (>60)? [2] (d) Min score for 6th student to raise average to 75? [3]"""
    return q, txt, vrs, fp

def wp5():
    q = get_next_q_num()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 100); ax.set_ylim(0, 60); ax.axis('off')
    ax.add_patch(patches.Rectangle((20, 15), 50, 30, linewidth=2, edgecolor='green', facecolor='lightgreen', alpha=0.5))
    ax.add_patch(patches.Rectangle((55, 15), 15, 15, linewidth=2, edgecolor='white', facecolor='white'))
    ax.plot([55, 55], [15, 30], 'g-', linewidth=2)
    ax.plot([55, 70], [30, 30], 'g-', linewidth=2)
    ax.plot([70, 70], [30, 15], 'g-', linewidth=2)
    ax.text(45, 12, '15 m', ha='center', fontsize=9)
    ax.text(17, 30, '12 m', ha='center', fontsize=9, rotation=90)
    ax.text(62, 12, '8 m', ha='center', fontsize=9)
    ax.text(72, 22, '7 m', ha='center', fontsize=9, rotation=90)
    ax.text(50, 58, f'Question {q}: Garden Design', ha='center', fontsize=12, fontweight='bold')
    fp = save_fig(fig, f'Q{q:02d}_diagram.png')
    vrs = create_vrs("Word Problem", ["Area", "Perimeter", "Cost"], "Hard", ["L-shape"], ["Decompose shape"], ["Missing edges"])
    txt = f"""Question {q}: L-shaped garden: 15m x 12m with 8m x 7m cutout. Fencing $18/m, grass $25/m2.
(a) Area? [2] (b) Perimeter? [2] (c) Total cost? [3] (d) With 1m path inside, new grass cost? [3]"""
    return q, txt, vrs, fp

def wp6():
    q = get_next_q_num()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 100); ax.set_ylim(0, 60); ax.axis('off')
    ax.add_patch(patches.Rectangle((30, 10), 40, 35, linewidth=2, edgecolor='black', facecolor='lightcyan'))
    ax.axhline(y=20, xmin=0.31, xmax=0.69, color='blue', linewidth=8, alpha=0.4)
    ax.axhline(y=30, xmin=0.31, xmax=0.69, color='blue', linewidth=8, alpha=0.5)
    ax.plot([48, 48], [50, 45], 'k-', linewidth=3)
    ax.plot([45, 51], [50, 50], 'k-', linewidth=3)
    for y in [42, 38, 34]: ax.plot(48, y, 'bo', markersize=4)
    ax.text(50, 22, '10:00', fontsize=9, ha='center')
    ax.text(50, 32, '10:30', fontsize=9, ha='center')
    ax.text(50, 58, f'Question {q}: Filling Tank', ha='center', fontsize=12, fontweight='bold')
    fp = save_fig(fig, f'Q{q:02d}_diagram.png')
    vrs = create_vrs("Word Problem", ["Volume", "Rate", "Time"], "Hard", ["Tank"], ["Calculate volume change"], ["Unit conversion"])
    txt = f"""Question {q}: Tank 60x40x50 cm. At 10:00, water = 10cm. At 10:30, water = 25cm.
(a) Volume at 10:30? [2] (b) Flow rate in L/min? [2] (c) When full? [3] (d) At 80% full, drain at 0.5 L/min, time to empty? [3]"""
    return q, txt, vrs, fp

def wp7():
    q = get_next_q_num()
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_xlim(0, 100); ax.set_ylim(0, 50); ax.axis('off')
    ax.add_patch(FancyBboxPatch((5, 15), 40, 25, boxstyle="round,pad=0.02", facecolor='lightyellow', edgecolor='orange', linewidth=2))
    ax.text(25, 30, 'BEFORE: Red:Blue = 3:5\nTotal: 120', ha='center', fontsize=10)
    ax.add_patch(FancyBboxPatch((60, 15), 35, 25, boxstyle="round,pad=0.02", facecolor='lightgreen', edgecolor='green', linewidth=2))
    ax.text(77, 30, 'AFTER: Red:Blue = 2:3', ha='center', fontsize=10)
    ax.text(50, 47, f'Question {q}: Marbles', ha='center', fontsize=12, fontweight='bold')
    fp = save_fig(fig, f'Q{q:02d}_diagram.png')
    vrs = create_vrs("Word Problem", ["Ratio", "Constant Quantity"], "Hard", ["Before/After boxes"], ["Find common base"], ["Assuming both change"])
    txt = f"""Question {q}: Red:Blue = 3:5, total 120. Red added, new ratio 2:3.
(a) Red at first? [2] (b) Red added? [3] (c) Blue to remove for 3:2 ratio? [3] (d) Red to add instead for 3:2? [2]"""
    return q, txt, vrs, fp

def wp8():
    q = get_next_q_num()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 100); ax.set_ylim(0, 60); ax.axis('off')
    ax.plot([10, 90], [30, 30], 'k-', linewidth=3)
    ax.plot(15, 30, 'bs', markersize=12); ax.plot(85, 30, 'rs', markersize=12)
    ax.text(15, 22, 'Town P', ha='center', fontsize=10, fontweight='bold')
    ax.text(85, 22, 'Town Q', ha='center', fontsize=10, fontweight='bold')
    ax.annotate('', xy=(85, 38), xytext=(15, 38), arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
    ax.text(50, 42, '360 km', ha='center', fontsize=11, fontweight='bold')
    ax.text(30, 35, 'Car A: 80 km/h', fontsize=12)
    ax.text(60, 18, 'Car B: 100 km/h', fontsize=12)
    ax.text(50, 56, f'Question {q}: Journey', ha='center', fontsize=12, fontweight='bold')
    fp = save_fig(fig, f'Q{q:02d}_diagram.png')
    vrs = create_vrs("Word Problem", ["Speed", "Relative Motion"], "Hard", ["Road diagram"], ["Calculate relative speed"], ["Adding speeds wrong"])
    txt = f"""Question {q}: Towns P and Q 360 km apart. Car A leaves P at 80 km/h, Car B leaves Q at 100 km/h.
(a) Time to meet? [2] (b) Distance from P at meeting? [2] (c) If A starts 30 min earlier, distance from Q at meeting? [4] (d) Arrival time difference? [2]"""
    return q, txt, vrs, fp

def wp9():
    q = get_next_q_num()
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_xlim(0, 100); ax.set_ylim(0, 50); ax.axis('off')
    ax.add_patch(patches.Rectangle((10, 30), 80, 8, linewidth=2, edgecolor='black', facecolor='lightgray'))
    ax.add_patch(patches.Rectangle((10, 30), 24, 8, linewidth=1, edgecolor='black', facecolor='lightcoral'))
    ax.text(22, 26, '1/3 Books', ha='center', fontsize=8)
    ax.add_patch(patches.Rectangle((34, 30), 28, 8, linewidth=1, edgecolor='black', facecolor='lightblue'))
    ax.text(48, 18, '1/2 remainder Toys', ha='center', fontsize=8)
    ax.add_patch(patches.Rectangle((62, 30), 28, 8, linewidth=1, edgecolor='black', facecolor='lightgreen'))
    ax.text(76, 18, 'Left: $84', ha='center', fontsize=8, fontweight='bold')
    ax.text(50, 47, f'Question {q}: Spending', ha='center', fontsize=12, fontweight='bold')
    fp = save_fig(fig, f'Q{q:02d}_diagram.png')
    vrs = create_vrs("Word Problem", ["Fractions", "Working Backwards"], "Hard", ["Bar model"], ["Work backwards"], ["Wrong base"])
    txt = f"""Question {q}: Jane spent 1/3 on books, 1/2 remainder on toys, 1/4 of rest on stationery. $84 left.
(a) Original amount? [4] (b) Spent on books? [2] (c) Fraction on toys? [2] (d) More needed for $120 bag? [2]"""
    return q, txt, vrs, fp

def wp10():
    q = get_next_q_num()
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_xlim(0, 100); ax.set_ylim(0, 50); ax.axis('off')
    ax.add_patch(FancyBboxPatch((5, 20), 25, 20, boxstyle="round,pad=0.02", facecolor='lightblue', edgecolor='blue', linewidth=2))
    ax.text(17, 30, '$800', ha='center', fontsize=11, fontweight='bold')
    ax.annotate('', xy=(35, 30), xytext=(32, 30), arrowprops=dict(arrowstyle='->', color='red', lw=2))
    ax.text(33, 34, '-20%', fontsize=9, color='red', ha='center')
    ax.add_patch(FancyBboxPatch((38, 20), 25, 20, boxstyle="round,pad=0.02", facecolor='lightyellow', edgecolor='orange', linewidth=2))
    ax.text(50, 30, '$640', ha='center', fontsize=11, fontweight='bold')
    ax.annotate('', xy=(68, 30), xytext=(65, 30), arrowprops=dict(arrowstyle='->', color='green', lw=2))
    ax.text(66, 34, '+15%', fontsize=9, color='green', ha='center')
    ax.add_patch(FancyBboxPatch((71, 20), 25, 20, boxstyle="round,pad=0.02", facecolor='lightgreen', edgecolor='green', linewidth=2))
    ax.text(83, 30, '$?', ha='center', fontsize=11, fontweight='bold')
    ax.text(50, 47, f'Question {q}: Price Changes', ha='center', fontsize=12, fontweight='bold')
    fp = save_fig(fig, f'Q{q:02d}_diagram.png')
    vrs = create_vrs("Word Problem", ["Percentage", "Successive Changes"], "Hard", ["Flow diagram"], ["Apply changes sequentially"], ["Adding percentages"])
    txt = f"""Question {q}: Laptop $800, reduced 20%, then increased 15%.
(a) Sale price? [2] (b) Final price? [2] (c) Overall % change? [3] (d) % discount to return to $800? [3]"""
    return q, txt, vrs, fp

# Continue with simpler implementations for remaining questions
def wp11():
    q = get_next_q_num()
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.text(0.5, 0.5, f'Question {q}: Age Problem\n\n5 years ago, father was 4x son.\nIn 8 years, sum = 56.', 
            ha='center', va='center', fontsize=12, transform=ax.transAxes)
    ax.axis('off')
    fp = save_fig(fig, f'Q{q:02d}_diagram.png')
    vrs = create_vrs("Word Problem", ["Age", "Ratio"], "Hard", ["Timeline"], ["Set up equations"], ["Not adjusting both ages"])
    txt = f"""Question {q}: 5 years ago, father was 4x son. In 8 years, sum = 56.
(a) Son's current age? [4] (b) Years ago when father was 7x son? [3] (c) Years until father is 2x son? [3]"""
    return q, txt, vrs, fp

def wp12():
    q = get_next_q_num()
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.text(0.5, 0.5, f'Question {q}: Mass Transfer\n\nBoxes A, B, C total 180kg.\n1/4 A to B, then 1/3 B to C.\nFinal: A = C', ha='center', va='center', fontsize=11, transform=ax.transAxes)
    ax.axis('off')
    fp = save_fig(fig, f'Q{q:02d}_diagram.png')
    vrs = create_vrs("Word Problem", ["Mass Transfer", "Fractions"], "Hard", ["Container diagram"], ["Track transfers"], ["Not accounting for source"])
    txt = f"""Question {q}: A+B+C=180kg. 1/4 A to B, 1/3 B to C. Final A=C.
(a) Final mass in C? [3] (b) Original A? [4] (c) Transferred B to C? [3]"""
    return q, txt, vrs, fp

def wp13():
    q = get_next_q_num()
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.text(0.5, 0.5, f'Question {q}: Multi-Leg Journey\n\nHome-A: 60km at 40km/h\nA-B: 90km at 60km/h\nB-C: 45km at 30km/h\nC-D: ? at 50km/h\nTotal: 5h 30min', ha='center', va='center', fontsize=10, transform=ax.transAxes)
    ax.axis('off')
    fp = save_fig(fig, f'Q{q:02d}_diagram.png')
    vrs = create_vrs("Word Problem", ["Speed", "Multi-leg"], "Hard", ["Journey segments"], ["Calculate times"], ["Time conversion"])
    txt = f"""Question {q}: Journey with legs: 60km@40, 90km@60, 45km@30, ?@50. Total 5h30.
(a) Time for first 3 legs? [3] (b) Distance C to D? [3] (c) Average speed? [2] (d) Min speed for last leg to finish in 5h? [2]"""
    return q, txt, vrs, fp

def wp14():
    q = get_next_q_num()
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.text(0.5, 0.5, f'Question {q}: Water Displacement\n\nTank 30x25x40 cm\nWater: 8 cm deep\nBlock: 15x10x8 cm added', ha='center', va='center', fontsize=11, transform=ax.transAxes)
    ax.axis('off')
    fp = save_fig(fig, f'Q{q:02d}_diagram.png')
    vrs = create_vrs("Word Problem", ["Volume", "Displacement"], "Hard", ["Tank diagram"], ["Calculate displacement"], ["Wrong base area"])
    txt = f"""Question {q}: Tank 30x25x40 cm, water 8cm. Block 15x10x8 cm added.
(a) Block volume? [1] (b) New water level? [3] (c) More blocks before full? [4] (d) Remove block, add 5L, new depth? [2]"""
    return q, txt, vrs, fp

def wp15():
    q = get_next_q_num()
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.text(0.5, 0.5, f'Question {q}: Group Distribution\n\nBoys:Girls:Adults = 5:3:2\nTotal: 120 people\nBoys: 3 sweets, Girls: 4, Adults: 2', ha='center', va='center', fontsize=10, transform=ax.transAxes)
    ax.axis('off')
    fp = save_fig(fig, f'Q{q:02d}_diagram.png')
    vrs = create_vrs("Word Problem", ["Ratio", "Distribution"], "Hard", ["Group icons"], ["Calculate per group"], ["Wrong unit assignment"])
    txt = f"""Question {q}: Ratio 5:3:2, total 120. Sweets: boys 3, girls 4, adults 2.
(a) Number of boys? [2] (b) Total sweets? [3] (c) If ratio 4:4:2, more/fewer sweets? [3] (d) Min sweets to add for equal? [2]"""
    return q, txt, vrs, fp

def wp16():
    q = get_next_q_num()
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.text(0.5, 0.5, f'Question {q}: GST Calculation\n\nTV: 15% discount, then 9% GST\nFinal price: $433.50', ha='center', va='center', fontsize=11, transform=ax.transAxes)
    ax.axis('off')
    fp = save_fig(fig, f'Q{q:02d}_diagram.png')
    vrs = create_vrs("Word Problem", ["GST", "Reverse Percentage"], "Hard", ["Price flow"], ["Work backwards"], ["Wrong base for GST"])
    txt = f"""Question {q}: TV 15% discount, 9% GST on discounted. Paid $433.50.
(a) Price before GST? [3] (b) List price? [3] (c) % of list price actually paid? [2] (d) If GST 10%, how much more? [2]"""
    return q, txt, vrs, fp

def wp17():
    q = get_next_q_num()
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.text(0.5, 0.5, f'Question {q}: Area Scaling\n\nRectangle area = 120 cm2\nLength +20%, Width +25%', ha='center', va='center', fontsize=11, transform=ax.transAxes)
    ax.axis('off')
    fp = save_fig(fig, f'Q{q:02d}_diagram.png')
    vrs = create_vrs("Word Problem", ["Area", "Scaling"], "Hard", ["Rectangle diagram"], ["Apply scale factors"], ["Adding percentages"])
    txt = f"""Question {q}: Rectangle 120 cm2. Length +20%, width +25%.
(a) New area? [3] (b) % increase? [2] (c) If length -20%, width +25%? [3] (d) Width change for no area change? [2]"""
    return q, txt, vrs, fp

def wp18():
    q = get_next_q_num()
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.text(0.5, 0.5, f'Question {q}: Work Schedule\n\nTask A: 45 min (starts 8:30)\nTask B: 1h20m\nBreak: 15 min\nFinish: 12:00', ha='center', va='center', fontsize=11, transform=ax.transAxes)
    ax.axis('off')
    fp = save_fig(fig, f'Q{q:02d}_diagram.png')
    vrs = create_vrs("Word Problem", ["Time", "Scheduling"], "Hard", ["Timeline"], ["Calculate durations"], ["Missing break"])
    txt = f"""Question {q}: Task A 45min from 8:30, Task B 1h20m, break 15min, finish 12:00.
(a) Task B start time? [1] (b) Task C duration? [3] (c) Latest Task A start for 11:30 finish? [3] (d) If 20% faster on B, how much earlier? [3]"""
    return q, txt, vrs, fp

def wp19():
    q = get_next_q_num()
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.text(0.5, 0.5, f'Question {q}: Weighted Average\n\nCA1(15%): 72\nCA2(15%): 68\nSA1(30%): ?\nSA2(40%): 78\nOverall: 75', ha='center', va='center', fontsize=11, transform=ax.transAxes)
    ax.axis('off')
    fp = save_fig(fig, f'Q{q:02d}_diagram.png')
    vrs = create_vrs("Word Problem", ["Weighted Average"], "Hard", ["Component boxes"], ["Set up equation"], ["Wrong weights"])
    txt = f"""Question {q}: Weights: CA1 15%=72, CA2 15%=68, SA1 30%=?, SA2 40%=78. Average 75.
(a) SA1 score? [4] (b) SA1 for average 80? [3] (c) Min SA1 to pass (50 average)? [3]"""
    return q, txt, vrs, fp

def wp20():
    q = get_next_q_num()
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.text(0.5, 0.5, f'Question {q}: Production Schedule\n\nMachine A: 45/hr from 8:00\nMachine B: 60/hr from 9:30\nTarget: 900 items', ha='center', va='center', fontsize=11, transform=ax.transAxes)
    ax.axis('off')
    fp = save_fig(fig, f'Q{q:02d}_diagram.png')
    vrs = create_vrs("Word Problem", ["Rate", "Time"], "Hard", ["Machine diagram"], ["Calculate production"], ["Different start times"])
    txt = f"""Question {q}: Machine A 45/hr from 8:00, Machine B 60/hr from 9:30. Target 900.
(a) A's production when B starts? [2] (b) Time to reach 900? [4] (c) If B breaks 30min at 10:00, new time? [4]"""
    return q, txt, vrs, fp

# ========== GEOMETRY PROBLEMS 21-32 ==========

def geo1():
    q = get_next_q_num()
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_xlim(0, 100); ax.set_ylim(0, 70); ax.set_aspect('equal'); ax.axis('off')
    ax.add_patch(Circle((35, 35), 20, fill=False, edgecolor='blue', linewidth=2))
    ax.add_patch(Circle((55, 35), 20, fill=False, edgecolor='red', linewidth=2))
    ax.plot(35, 35, 'b+', markersize=10); ax.plot(55, 35, 'r+', markersize=10)
    ax.text(35, 13, 'O1', ha='center', fontsize=11)
    ax.text(55, 13, 'O2', ha='center', fontsize=11)
    ax.text(45, 58, '20 cm', ha='center', fontsize=10)
    ax.text(45, 65, f'Question {q}: Overlapping Circles', ha='center', fontsize=12, fontweight='bold')
    fp = save_fig(fig, f'Q{q:02d}_diagram.png')
    vrs = create_vrs("Geometry", ["Circles", "Overlap"], "Hard", ["Two circles"], ["Find segment areas"], ["Wrong angle"])
    txt = f"""Question {q}: Two circles radius 20cm, centers 20cm apart.
(a) Show triangle O1AO2 equilateral. [2] (b) Sector O1AB area? [2] (c) Shaded overlap area? [4] (d) Perimeter of shaded? [2] (pi=3.14)"""
    return q, txt, vrs, fp

def geo2():
    q = get_next_q_num()
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_xlim(0, 100); ax.set_ylim(0, 70); ax.set_aspect('equal'); ax.axis('off')
    offset_x, offset_y, cell = 20, 15, 10
    for i in range(7):
        ax.plot([offset_x, offset_x+60], [offset_y+i*10, offset_y+i*10], 'k-', linewidth=0.5)
        ax.plot([offset_x+i*10, offset_x+i*10], [offset_y, offset_y+60], 'k-', linewidth=0.5)
    points = [(1, 2), (4, 2), (5, 5), (2, 5)]
    xs = [offset_x+p[0]*10 for p in points]+[offset_x+points[0][0]*10]
    ys = [offset_y+p[1]*10 for p in points]+[offset_y+points[0][1]*10]
    ax.plot(xs, ys, 'b-', linewidth=2)
    for i, (px, py) in enumerate(points):
        ax.plot(offset_x+px*10, offset_y+py*10, 'ro', markersize=8)
        ax.text(offset_x+px*10+2, offset_y+py*10+2, chr(65+i), fontsize=10, fontweight='bold')
    ax.text(85, 20, '1 unit = 2cm', fontsize=9, ha='center')
    ax.text(50, 68, f'Question {q}: Grid Quadrilateral', ha='center', fontsize=12, fontweight='bold')
    fp = save_fig(fig, f'Q{q:02d}_diagram.png')
    vrs = create_vrs("Geometry", ["Coordinates", "Area"], "Hard", ["Grid"], ["Apply scale"], ["Wrong scale"])
    txt = f"""Question {q}: Quadrilateral ABCD on grid, 1 unit = 2cm.
(a) Coordinates of A,B,C,D? [2] (b) Length AB? [2] (c) Area? [3] (d) Perimeter? [3]"""
    return q, txt, vrs, fp

def geo3():
    q = get_next_q_num()
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_xlim(0, 100); ax.set_ylim(0, 70); ax.axis('off')
    ax.add_patch(patches.Rectangle((30, 20), 40, 40, linewidth=2, edgecolor='black', facecolor='lightcyan', alpha=0.3))
    ax.add_patch(Polygon([(30, 60), (40, 70), (80, 70), (70, 60)], facecolor='lightblue', edgecolor='black', linewidth=2, alpha=0.4))
    ax.add_patch(Polygon([(70, 60), (80, 70), (80, 30), (70, 20)], facecolor='lightsteelblue', edgecolor='black', linewidth=2, alpha=0.4))
    ax.add_patch(Circle((50, 40), 8, fill=False, edgecolor='red', linewidth=2, linestyle='--'))
    ax.text(50, 40, 'Hole', ha='center', va='center', fontsize=9, color='red')
    ax.text(50, 15, '8 cm', ha='center', fontsize=10)
    ax.text(50, 5, 'Cylinder diameter: 4 cm', ha='center', fontsize=10, color='red')
    ax.text(50, 68, f'Question {q}: Cube with Hole', ha='center', fontsize=12, fontweight='bold')
    fp = save_fig(fig, f'Q{q:02d}_diagram.png')
    vrs = create_vrs("Geometry", ["3D", "Volume"], "Hard", ["Cube diagram"], ["Calculate volumes"], ["Forgetting inner surface"])
    txt = f"""Question {q}: Cube side 8cm, cylindrical hole diameter 4cm through center.
(a) Cube volume? [1] (b) Cylinder volume? [2] (c) Remaining volume? [2] (d) Total surface area? [5] (pi=3.14)"""
    return q, txt, vrs, fp

def geo4():
    q = get_next_q_num()
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_xlim(0, 100); ax.set_ylim(0, 70); ax.set_aspect('equal'); ax.axis('off')
    A, B, C = (30, 60), (15, 20), (75, 20)
    ax.add_patch(Polygon([A, B, C], fill=False, edgecolor='black', linewidth=2))
    ax.text(A[0], A[1]+3, 'A', fontsize=12, fontweight='bold', ha='center')
    ax.text(B[0]-3, B[1], 'B', fontsize=12, fontweight='bold', ha='center')
    ax.text(C[0]+3, C[1], 'C', fontsize=12, fontweight='bold', ha='center')
    ax.add_patch(Arc(B, 15, 15, angle=0, theta1=0, theta2=67, color='blue', linewidth=2))
    ax.text(B[0]+10, B[1]+5, '52 deg', fontsize=10, color='blue')
    ax.add_patch(Arc(C, 15, 15, angle=0, theta1=113, theta2=180, color='red', linewidth=2))
    ax.text(C[0]-10, C[1]+5, '48 deg', fontsize=10, color='red')
    ax.text(50, 68, f'Question {q}: Triangle Angles', ha='center', fontsize=12, fontweight='bold')
    fp = save_fig(fig, f'Q{q:02d}_diagram.png')
    vrs = create_vrs("Geometry", ["Angles", "Triangle"], "Hard", ["Triangle"], ["Angle sum"], ["Wrong assumption"])
    txt = f"""Question {q}: Triangle ABC, angle B=52 deg, C=48 deg, AB=10cm, BC=12cm.
(a) Angle BAC? [2] (b) Type of triangle? [2] (c) If BD bisects B, angle BDC? [3] (d) Area? [3]"""
    return q, txt, vrs, fp

def geo5():
    q = get_next_q_num()
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_xlim(0, 100); ax.set_ylim(0, 70); ax.set_aspect('equal'); ax.axis('off')
    trap = Polygon([(20, 20), (70, 20), (60, 50), (30, 50)], fill=False, edgecolor='black', linewidth=2)
    ax.add_patch(trap)
    ax.add_patch(Arc((45, 50), 30, 30, angle=0, theta1=0, theta2=180, color='blue', linewidth=2))
    ax.plot([30, 60], [50, 50], 'b-', linewidth=2)
    ax.text(45, 11, '50 cm', ha='center', fontsize=10)
    ax.text(45, 46, '30 cm', ha='center', fontsize=10)
    ax.text(75, 35, 'Height:\n20 cm', fontsize=9, ha='center')
    ax.text(50, 68, f'Question {q}: Composite Shape', ha='center', fontsize=12, fontweight='bold')
    fp = save_fig(fig, f'Q{q:02d}_diagram.png')
    vrs = create_vrs("Geometry", ["Trapezium", "Semicircle"], "Hard", ["Composite"], ["Sum areas"], ["Diameter vs radius"])
    txt = f"""Question {q}: Trapezium ABCD (AB=50, CD=30, h=20) with semicircle on CD.
(a) Trapezium area? [2] (b) Semicircle area? [2] (c) Total area? [2] (d) Perimeter? [4] (pi=3.14)"""
    return q, txt, vrs, fp

def geo6():
    q = get_next_q_num()
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_xlim(0, 100); ax.set_ylim(0, 70); ax.set_aspect('equal'); ax.axis('off')
    ax.plot([10, 90], [50, 50], 'k-', linewidth=2)
    ax.plot([10, 90], [25, 25], 'k-', linewidth=2)
    ax.text(85, 53, 'L1', fontsize=11, fontweight='bold')
    ax.text(85, 20, 'L2', fontsize=11, fontweight='bold')
    ax.plot([25, 75], [10, 65], 'k-', linewidth=2)
    ax.add_patch(Arc((40, 50), 12, 12, angle=0, theta1=0, theta2=45, color='blue', linewidth=2))
    ax.text(48, 54, '65 deg', fontsize=10, color='blue')
    ax.add_patch(Arc((52, 25), 12, 12, angle=0, theta1=225, theta2=270, color='red', linewidth=2))
    ax.text(44, 21, 'a', fontsize=12, color='red', fontweight='bold')
    ax.text(50, 68, f'Question {q}: Parallel Lines', ha='center', fontsize=12, fontweight='bold')
    fp = save_fig(fig, f'Q{q:02d}_diagram.png')
    vrs = create_vrs("Geometry", ["Parallel Lines"], "Hard", ["Parallel lines"], ["Apply properties"], ["Confusing angles"])
    txt = f"""Question {q}: L1 parallel L2, transversal T. One angle 65 deg.
(a) Angle a with reason? [2] (b) Angle b with reason? [2] (c) Another transversal 35 deg, angle between transversals? [3] (d) Why a+b=180? [3]"""
    return q, txt, vrs, fp

def geo7():
    q = get_next_q_num()
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_xlim(0, 100); ax.set_ylim(0, 70); ax.set_aspect('equal'); ax.axis('off')
    center = (50, 35)
    theta = np.linspace(0, np.pi/2, 100)
    x_arc = center[0] + 25*np.cos(theta)
    y_arc = center[1] + 25*np.sin(theta)
    ax.plot(x_arc, y_arc, 'k-', linewidth=2)
    ax.plot([center[0], center[0]+25], [center[1], center[1]], 'k-', linewidth=2)
    ax.plot([center[0], center[0]], [center[1], center[1]+25], 'k-', linewidth=2)
    ax.plot(center[0], center[1], 'ko', markersize=6)
    ax.text(center[0]-3, center[1]-4, 'O', fontsize=11, fontweight='bold')
    ax.text(center[0]+27, center[1], 'A', fontsize=11, fontweight='bold')
    ax.text(center[0], center[1]+27, 'B', fontsize=11, fontweight='bold')
    ax.text(center[0]+8, center[1]+8, '90 deg', fontsize=10)
    ax.text(50, 68, f'Question {q}: Sector', ha='center', fontsize=12, fontweight='bold')
    fp = save_fig(fig, f'Q{q:02d}_diagram.png')
    vrs = create_vrs("Geometry", ["Sector", "Segment"], "Hard", ["Sector"], ["Calculate areas"], ["Degrees vs radians"])
    txt = f"""Question {q}: Sector OAB, radius 14cm, angle AOB=90 deg.
(a) Sector area? [2] (b) Triangle area? [2] (c) Segment area? [2] (d) Arc length? [2] (e) Sector perimeter? [2] (pi=22/7)"""
    return q, txt, vrs, fp

def geo8():
    q = get_next_q_num()
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_xlim(0, 100); ax.set_ylim(0, 70); ax.set_aspect('equal'); ax.axis('off')
    ax.add_patch(patches.Rectangle((30, 25), 30, 20, linewidth=2, edgecolor='black', facecolor='lightyellow'))
    ax.text(45, 35, 'Base 10x8', ha='center', va='center', fontsize=9)
    ax.add_patch(patches.Rectangle((30, 5), 30, 20, linewidth=2, edgecolor='black', facecolor='lightblue'))
    ax.text(45, 15, 'Front 10x6', ha='center', va='center', fontsize=9)
    ax.add_patch(patches.Rectangle((5, 25), 25, 20, linewidth=2, edgecolor='black', facecolor='lightgreen'))
    ax.text(17, 35, 'Left 8x6', ha='center', va='center', fontsize=9)
    ax.text(50, 3, '10cm x 8cm x 6cm', ha='center', fontsize=9)
    ax.text(50, 68, f'Question {q}: Prism Net', ha='center', fontsize=12, fontweight='bold')
    fp = save_fig(fig, f'Q{q:02d}_diagram.png')
    vrs = create_vrs("Geometry", ["Net", "Surface Area"], "Hard", ["Net layout"], ["Sum face areas"], ["Missing faces"])
    txt = f"""Question {q}: Prism net 10x8x6 cm.
(a) Surface area? [3] (b) Volume? [2] (c) Mass if density 2.5 g/cm3? [2] (d) Surface area if cut in half? [3]"""
    return q, txt, vrs, fp

def geo9():
    q = get_next_q_num()
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_xlim(0, 100); ax.set_ylim(0, 70); ax.set_aspect('equal'); ax.axis('off')
    A, B, C, D = (25, 50), (65, 50), (75, 25), (35, 25)
    ax.add_patch(Polygon([A, B, C, D], fill=False, edgecolor='black', linewidth=2))
    ax.plot([A[0], C[0]], [A[1], C[1]], 'k--', linewidth=1)
    ax.plot([B[0], D[0]], [B[1], D[1]], 'k--', linewidth=1)
    ax.text(A[0]-3, A[1]+2, 'A', fontsize=12, fontweight='bold')
    ax.text(B[0]+3, B[1]+2, 'B', fontsize=12, fontweight='bold')
    ax.text(C[0]+3, C[1]-3, 'C', fontsize=12, fontweight='bold')
    ax.text(D[0]-3, D[1]-3, 'D', fontsize=12, fontweight='bold')
    ax.text(45, 53, '12 cm', ha='center', fontsize=10)
    ax.text(78, 38, '8 cm', ha='center', fontsize=10, rotation=-65)
    ax.text(50, 68, f'Question {q}: Parallelogram', ha='center', fontsize=12, fontweight='bold')
    fp = save_fig(fig, f'Q{q:02d}_diagram.png')
    vrs = create_vrs("Geometry", ["Parallelogram"], "Hard", ["Parallelogram"], ["Apply properties"], ["Wrong height"])
    txt = f"""Question {q}: Parallelogram ABCD, AB=12, BC=8, angle DAB=55 deg.
(a) CD? [1] (b) Angle ABC? [2] (c) Area? [3] (d) Verify with height 6.55cm. [2] (e) Diagonal property? [2]"""
    return q, txt, vrs, fp

def geo10():
    q = get_next_q_num()
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_xlim(0, 100); ax.set_ylim(0, 70); ax.set_aspect('equal'); ax.axis('off')
    ax.add_patch(Circle((50, 35), 25, fill=False, edgecolor='black', linewidth=2))
    ax.plot(50, 35, 'ko', markersize=6)
    ax.text(52, 37, 'O', fontsize=11, fontweight='bold')
    for name, (x, y) in [('A', (50, 60)), ('B', (75, 35)), ('C', (50, 10)), ('D', (30, 50))]:
        ax.plot(x, y, 'bo', markersize=6)
        ax.text(x+3, y+3, name, fontsize=11, fontweight='bold')
    ax.plot([50, 50], [35, 60], 'k-', linewidth=1.5)
    ax.plot([50, 75], [35, 35], 'k-', linewidth=1.5)
    ax.add_patch(Arc((50, 35), 12, 12, angle=0, theta1=0, theta2=90, color='red', linewidth=2))
    ax.text(58, 43, '80 deg', fontsize=10, color='red')
    ax.text(50, 68, f'Question {q}: Circle Theorem', ha='center', fontsize=12, fontweight='bold')
    fp = save_fig(fig, f'Q{q:02d}_diagram.png')
    vrs = create_vrs("Geometry", ["Circle Theorems"], "Hard", ["Circle"], ["Apply theorem"], ["Center vs circumference"])
    txt = f"""Question {q}: Circle center O, angle AOB=80 deg, AC diameter.
(a) Angle ADC with reason? [3] (b) Angle ACB? [2] (c) Angle ABC? [2] (d) If CAD=35, angle BAD? [3]"""
    return q, txt, vrs, fp

def geo11():
    q = get_next_q_num()
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_xlim(0, 100); ax.set_ylim(0, 70); ax.set_aspect('equal'); ax.axis('off')
    A, B, C = (20, 20), (80, 20), (50, 60)
    ax.add_patch(Polygon([A, B, C], fill=False, edgecolor='blue', linewidth=2))
    D, E = (35, 20), (50, 40)
    ax.add_patch(Polygon([A, D, E], fill=False, edgecolor='red', linewidth=2))
    ax.text(A[0]-4, A[1], 'A', fontsize=12, fontweight='bold')
    ax.text(B[0]+3, B[1], 'B', fontsize=12, fontweight='bold')
    ax.text(C[0], C[1]+3, 'C', fontsize=12, fontweight='bold')
    ax.text(D[0], D[1]-4, 'D', fontsize=11, fontweight='bold', color='red')
    ax.text(E[0]+3, E[1], 'E', fontsize=11, fontweight='bold', color='red')
    ax.text(50, 16, '12 cm', ha='center', fontsize=10)
    ax.text(27, 16, '5 cm', ha='center', fontsize=10, color='red')
    ax.text(50, 68, f'Question {q}: Similar Triangles', ha='center', fontsize=12, fontweight='bold')
    fp = save_fig(fig, f'Q{q:02d}_diagram.png')
    vrs = create_vrs("Geometry", ["Similar Triangles"], "Hard", ["Nested triangles"], ["Find scale factor"], ["Wrong ratio"])
    txt = f"""Question {q}: DE parallel BC, AB=12, AD=5, AC=8.
(a) Show ADE~ABC. [2] (b) Scale factor? [2] (c) AE? [2] (d) If ADE area=15, ABC area? [2] (e) Trapezium DECB area? [2]"""
    return q, txt, vrs, fp

def geo12():
    q = get_next_q_num()
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_xlim(0, 100); ax.set_ylim(0, 70); ax.set_aspect('equal'); ax.axis('off')
    ax.add_patch(patches.Rectangle((25, 20), 40, 40, linewidth=2, edgecolor='black', facecolor='lightgray', alpha=0.3))
    for cx, cy, t1, t2 in [(25, 60, 0, 90), (65, 60, 90, 180), (25, 20, 270, 360), (65, 20, 180, 270)]:
        ax.add_patch(Wedge((cx, cy), 10, t1, t2, facecolor='white', edgecolor='red', linewidth=2))
    ax.text(45, 18, '20 cm', ha='center', fontsize=10)
    ax.text(45, 63, 'Arc radius: 10 cm', ha='center', fontsize=10, color='red')
    ax.text(45, 40, 'Shaded', ha='center', va='center', fontsize=11, fontweight='bold')
    ax.text(50, 68, f'Question {q}: Shaded Region', ha='center', fontsize=12, fontweight='bold')
    fp = save_fig(fig, f'Q{q:02d}_diagram.png')
    vrs = create_vrs("Geometry", ["Composite Area"], "Hard", ["Square with cutouts"], ["Subtract areas"], ["Full circles"])
    txt = f"""Question {q}: Square 20cm, quarter circles radius 10cm removed from corners.
(a) Square area? [1] (b) Total quarter circles area? [2] (c) Shaded area? [3] (d) Shaded perimeter? [4] (pi=3.14)"""
    return q, txt, vrs, fp

# ========== DATA INTERPRETATION 33-40 ==========

def di1():
    q = get_next_q_num()
    fig, ax = plt.subplots(figsize=(10, 6))
    hours = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    temp = [25, 28, 32, 35, 38, 36, 33, 30, 27]
    ax.plot(hours, temp, 'b-o', linewidth=2, markersize=8)
    ax.fill_between(hours, temp, alpha=0.2)
    ax.set_xlabel('Hours after 8:00 a.m.', fontsize=11)
    ax.set_ylabel('Temperature (deg C)', fontsize=11)
    ax.set_title(f'Question {q}: Temperature', fontsize=12, fontweight='bold')
    ax.grid(True, alpha=0.3)
    fp = save_fig(fig, f'Q{q:02d}_diagram.png')
    vrs = create_vrs("Data Interpretation", ["Line Graph", "Rate"], "Hard", ["Line graph"], ["Read values"], ["Wrong scale"])
    txt = f"""Question {q}: Temperature graph from 8:00 a.m.
(a) Temperature at 11:00? [1] (b) Rate of increase 9:00-11:00? [2] (c) Greatest decrease period and rate? [2] (d) Estimate at 9:30? [2] (e) Predict next day 9:00 with reason? [3]"""
    return q, txt, vrs, fp

def di2():
    q = get_next_q_num()
    fig, ax = plt.subplots(figsize=(10, 6))
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    sales = [120, 135, 150, 180, 200, 240]
    bars = ax.bar(months, sales, color=['lightblue', 'lightgreen', 'lightyellow', 'lightcoral', 'lightpink', 'lightgray'], edgecolor='black')
    for bar, val in zip(bars, sales):
        ax.text(bar.get_x()+bar.get_width()/2., val+5, f'${val}k', ha='center', fontsize=10)
    ax.set_ylabel('Sales ($ thousands)', fontsize=11)
    ax.set_title(f'Question {q}: Monthly Sales', fontsize=12, fontweight='bold')
    ax.set_ylim(0, 280)
    fp = save_fig(fig, f'Q{q:02d}_diagram.png')
    vrs = create_vrs("Data Interpretation", ["Bar Chart", "Percentage"], "Hard", ["Bar chart"], ["Calculate changes"], ["Wrong base"])
    txt = f"""Question {q}: Monthly sales bar chart.
(a) Sales in March? [1] (b) % increase Jan to Jun? [2] (c) July 20% higher than June? [2] (d) December $264k, 10% higher than November, find November? [3] (e) Target $900k, met? [2]"""
    return q, txt, vrs, fp

def di3():
    q = get_next_q_num()
    fig, ax = plt.subplots(figsize=(10, 6))
    marks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    cum = [2, 5, 12, 25, 45, 65, 80, 90, 96, 100]
    ax.plot(marks, cum, 'g-s', linewidth=2, markersize=8)
    ax.fill_between(marks, cum, alpha=0.2, color='green')
    ax.axhline(y=50, color='red', linestyle='--', alpha=0.7)
    ax.axhline(y=25, color='blue', linestyle='--', alpha=0.7)
    ax.axhline(y=75, color='orange', linestyle='--', alpha=0.7)
    ax.set_xlabel('Marks (%)', fontsize=11)
    ax.set_ylabel('Cumulative Students', fontsize=11)
    ax.set_title(f'Question {q}: Cumulative Frequency', fontsize=12, fontweight='bold')
    fp = save_fig(fig, f'Q{q:02d}_diagram.png')
    vrs = create_vrs("Data Interpretation", ["Cumulative", "Median"], "Hard", ["Cumulative curve"], ["Find quartiles"], ["Wrong axis"])
    txt = f"""Question {q}: Cumulative frequency for 100 students.
(a) Scored 50 or less? [1] (b) Median? [2] (c) Interquartile range? [3] (d) Pass mark 45, how many passed? [2] (e) Between 60-80 marks? [2]"""
    return q, txt, vrs, fp

def di4():
    q = get_next_q_num()
    fig, ax = plt.subplots(figsize=(10, 6))
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    a, b = [50, 55, 60, 58, 65, 70], [40, 48, 55, 65, 72, 80]
    ax.plot(months, a, 'b-o', linewidth=2, markersize=8, label='Product A')
    ax.plot(months, b, 'r-s', linewidth=2, markersize=8, label='Product B')
    ax.legend(loc='upper left')
    ax.set_ylabel('Units Sold (hundreds)', fontsize=11)
    ax.set_title(f'Question {q}: Sales Comparison', fontsize=12, fontweight='bold')
    ax.grid(True, alpha=0.3)
    fp = save_fig(fig, f'Q{q:02d}_diagram.png')
    vrs = create_vrs("Data Interpretation", ["Multi-line", "Comparison"], "Hard", ["Two lines"], ["Compare trends"], ["Wrong line"])
    txt = f"""Question {q}: Sales of Products A and B over 6 months.
(a) Product A in March? [1] (b) When did B overtake A? [1] (c) % increase B Jan-Jun? [2] (d) Which product higher average? Show working. [3] (e) Predict July B with reasoning. [3]"""
    return q, txt, vrs, fp

def di5():
    q = get_next_q_num()
    fig, ax = plt.subplots(figsize=(10, 6))
    cats = ['Food', 'Transport', 'Utilities', 'Entertainment', 'Savings', 'Others']
    amounts = [450, 300, 200, 150, 600, 300]
    cols = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc', '#c2c2f0']
    ax.pie(amounts, labels=cats, colors=cols, autopct='%1.1f%%', startangle=90)
    ax.set_title(f'Question {q}: Budget Distribution\nTotal: $2000', fontsize=12, fontweight='bold')
    fp = save_fig(fig, f'Q{q:02d}_diagram.png')
    vrs = create_vrs("Data Interpretation", ["Pie Chart", "Percentage"], "Hard", ["Pie chart"], ["Calculate angles"], ["Wrong total"])
    txt = f"""Question {q}: Monthly salary $2000 pie chart.
(a) Food spending? [1] (b) Savings %? [2] (c) Transport sector angle? [2] (d) To save 40%, reduce entertainment+others by? [3] (e) If salary +10%, same proportions, new savings? [2]"""
    return q, txt, vrs, fp

def di6():
    q = get_next_q_num()
    fig, ax = plt.subplots(figsize=(10, 6))
    years = [2019, 2020, 2021, 2022, 2023]
    pop = [50000, 52000, 55000, 58000, 60000]
    ax.plot(years, pop, 'g-o', linewidth=2, markersize=8)
    ax.fill_between(years, pop, alpha=0.2, color='green')
    ax.set_xlabel('Year', fontsize=11)
    ax.set_ylabel('Population', fontsize=11)
    ax.set_title(f'Question {q}: Population Growth', fontsize=12, fontweight='bold')
    ax.grid(True, alpha=0.3)
    fp = save_fig(fig, f'Q{q:02d}_diagram.png')
    vrs = create_vrs("Data Interpretation", ["Line Graph", "Growth"], "Hard", ["Line graph"], ["Calculate growth"], ["Wrong period"])
    txt = f"""Question {q}: Population growth line graph.
(a) Population 2021? [1] (b) Increase 2019-2023? [2] (c) Average annual growth? [2] (d) When was growth rate highest? [2] (e) Predict 2025 with assumption. [3]"""
    return q, txt, vrs, fp

def di7():
    q = get_next_q_num()
    fig, ax = plt.subplots(figsize=(10, 6))
    subjects = ['Math', 'Science', 'English', 'Mother Tongue']
    boys = [75, 70, 65, 80]
    girls = [80, 75, 75, 85]
    x = np.arange(len(subjects))
    width = 0.35
    ax.bar(x-width/2, boys, width, label='Boys', color='lightblue', edgecolor='black')
    ax.bar(x+width/2, girls, width, label='Girls', color='lightpink', edgecolor='black')
    ax.set_xticks(x)
    ax.set_xticklabels(subjects)
    ax.set_ylabel('Average Marks', fontsize=11)
    ax.set_title(f'Question {q}: Subject Performance', fontsize=12, fontweight='bold')
    ax.legend()
    fp = save_fig(fig, f'Q{q:02d}_diagram.png')
    vrs = create_vrs("Data Interpretation", ["Bar Chart", "Comparison"], "Hard", ["Grouped bars"], ["Compare groups"], ["Wrong group"])
    txt = f"""Question {q}: Subject performance by gender.
(a) Boys' Math average? [1] (b) Subject with biggest gender gap? [2] (c) Overall boys average? [2] (d) If 60% girls 40% boys in cohort, weighted average for Math? [3] (e) Which subject most consistent? [2]"""
    return q, txt, vrs, fp

def di8():
    q = get_next_q_num()
    fig, ax = plt.subplots(figsize=(10, 6))
    time = ['8am', '10am', '12pm', '2pm', '4pm', '6pm']
    visitors = [120, 280, 450, 380, 250, 150]
    ax.plot(time, visitors, 'm-o', linewidth=2, markersize=8)
    ax.fill_between(time, visitors, alpha=0.2, color='magenta')
    ax.set_ylabel('Visitors', fontsize=11)
    ax.set_title(f'Question {q}: Museum Visitors', fontsize=12, fontweight='bold')
    ax.grid(True, alpha=0.3)
    fp = save_fig(fig, f'Q{q:02d}_diagram.png')
    vrs = create_vrs("Data Interpretation", ["Line Graph", "Rate"], "Hard", ["Line graph"], ["Calculate rates"], ["Wrong interval"])
    txt = f"""Question {q}: Museum visitor graph.
(a) Visitors at 12pm? [1] (b) Increase 8am-12pm? [2] (c) Average visitors per hour 8am-6pm? [2] (d) Period of greatest decrease? [2] (d) If ticket $15, revenue 10am-2pm? [3]"""
    return q, txt, vrs, fp

# Generate all questions
print("Generating 40 exam-quality baseline questions...")

# Word Problems 1-20
for func in [wp1, wp2, wp3, wp4, wp5, wp6, wp7, wp8, wp9, wp10, wp11, wp12, wp13, wp14, wp15, wp16, wp17, wp18, wp19, wp20]:
    q, txt, vrs, fp = func()
    all_questions.append((q, txt))
    all_vrs.append((q, vrs))
    all_images.append((q, fp))
    print(f"  Generated Q{q:02d}")

# Geometry 21-32
for func in [geo1, geo2, geo3, geo4, geo5, geo6, geo7, geo8, geo9, geo10, geo11, geo12]:
    q, txt, vrs, fp = func()
    all_questions.append((q, txt))
    all_vrs.append((q, vrs))
    all_images.append((q, fp))
    print(f"  Generated Q{q:02d}")

# Data Interpretation 33-40
for func in [di1, di2, di3, di4, di5, di6, di7, di8]:
    q, txt, vrs, fp = func()
    all_questions.append((q, txt))
    all_vrs.append((q, vrs))
    all_images.append((q, fp))
    print(f"  Generated Q{q:02d}")

# Save VRS files
for q, vrs in all_vrs:
    with open(os.path.join(OUTPUT_DIR, f'Q{q:02d}_vrs.yaml'), 'w') as f:
        f.write(vrs)

# Create combined text file
with open(os.path.join(OUTPUT_DIR, 'all_questions.txt'), 'w') as f:
    f.write("="*80 + "\n")
    f.write("SINGAPORE PSLE EXAM-QUALITY BASELINE TEST\n")
    f.write("40 Questions | Mathematics\n")
    f.write("="*80 + "\n\n")
    for q, txt in all_questions:
        f.write(txt + "\n\n")
        f.write("-"*80 + "\n\n")

print(f"\nAll files saved to: {OUTPUT_DIR}")
print(f"  - 40 PNG diagrams at 150 DPI")
print(f"  - 40 VRS YAML files")
print(f"  - Combined questions text file")
print("\nDone!")
