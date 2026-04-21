#!/usr/bin/env python3
"""
Exam-Quality Baseline Test Generator
Singapore PSLE Standards - 40 Questions
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, Polygon, Arc, Wedge
import numpy as np
import os
import yaml
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image as RLImage, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas

# Ensure output directory exists
OUTPUT_DIR = "05-Backend/artifacts/renders/exam-quality-baseline"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Set matplotlib to use a non-interactive backend
plt.switch_backend('Agg')

# Global question counter
question_counter = 0

def get_next_q_num():
    global question_counter
    question_counter += 1
    return question_counter

def save_fig(fig, filename, dpi=150):
    """Save figure with proper settings"""
    filepath = os.path.join(OUTPUT_DIR, filename)
    fig.savefig(filepath, dpi=dpi, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close(fig)
    return filepath

def create_vrs(q_type, concepts, difficulty, visual_elements, reasoning_chain, traps):
    """Create Visual Reconstruction Specification in YAML"""
    vrs = {
        "question_type": q_type,
        "complexity_tier": "Cross-Thread Collision" if q_type == "Word Problem" else "G5-G8 Composite",
        "fused_concepts": concepts,
        "difficulty": difficulty,
        "visual_elements": visual_elements,
        "reasoning_chain": reasoning_chain,
        "cognitive_traps": traps,
        "render_spec": {
            "dpi": 150,
            "font_family": "Arial",
            "line_weight": "0.5pt",
            "color_palette": "monochrome"
        }
    }
    return yaml.dump(vrs, default_flow_style=False, sort_keys=False)

# ==================== WORD PROBLEMS (20) ====================

def generate_wp1():
    """Word Problem 1: Speed-Distance-Time with Work Rate"""
    q_num = get_next_q_num()
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 60)
    ax.axis('off')
    
    # Draw route diagram
    ax.annotate('', xy=(85, 45), xytext=(15, 15),
                arrowprops=dict(arrowstyle='->', color='black', lw=2))
    ax.plot([15, 85], [15, 45], 'k--', alpha=0.3, lw=1)
    
    # Locations
    ax.plot(15, 15, 'ko', markersize=12)
    ax.plot(85, 45, 'ks', markersize=12)
    ax.text(15, 10, 'Factory A', ha='center', fontsize=10, fontweight='bold')
    ax.text(85, 50, 'Port B', ha='center', fontsize=10, fontweight='bold')
    
    # Truck icons
    ax.text(30, 25, 'Loaded: 60km/h', fontsize=10)
    ax.text(50, 35, 'Empty: 80km/h', fontsize=10)
    
    # Distance marker
    ax.annotate('', xy=(85, 15), xytext=(15, 15),
                arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
    ax.text(50, 8, '240 km', ha='center', fontsize=11, fontweight='bold')
    
    # Speed info box
    box = FancyBboxPatch((5, 38), 35, 18, boxstyle="round,pad=0.02", 
                          facecolor='lightyellow', edgecolor='black', linewidth=1)
    ax.add_patch(box)
    ax.text(22, 52, 'Truck Information', ha='center', fontsize=9, fontweight='bold')
    ax.text(22, 46, '• Speed: 60 km/h (loaded)', ha='center', fontsize=8)
    ax.text(22, 41, '• Speed: 80 km/h (empty)', ha='center', fontsize=8)
    ax.text(22, 36, '• Loading: 45 min', ha='center', fontsize=8)
    
    # Title
    ax.text(50, 58, f'Question {q_num}: Delivery Route', ha='center', fontsize=12, fontweight='bold')
    
    filepath = save_fig(fig, f'Q{q_num:02d}_diagram.png')
    
    vrs = create_vrs(
        "Word Problem",
        ["Speed-Distance-Time", "Work Rate", "Unit Conversion", "Optimization"],
        "Hard",
        ["Route diagram", "Distance markers", "Speed annotations"],
        ["Calculate one-way time", "Account for loading time", "Determine round-trip cycle", "Scale to 8-hour shift"],
        ["Forgetting return journey", "Ignoring loading time", "Unit conversion error (min vs hr)"]
    )
    
    question_text = f"""Question {q_num}:
A logistics company operates between Factory A and Port B, 240 km apart. 
A truck travels at 60 km/h when loaded and 80 km/h when empty. Loading 
at the factory takes 45 minutes, while unloading at the port takes 
30 minutes. The truck starts at 6:00 a.m. from Factory A.

(a) Calculate the total time for one complete round trip. [3 marks]

(b) How many complete round trips can the truck make in an 8-hour shift? [2 marks]

(c) If the driver takes a 1-hour lunch break after every 3 round trips, 
    what is the maximum number of deliveries to Port B possible in a 
    12-hour working day? [3 marks]
"""
    
    return q_num, question_text, vrs, filepath

def generate_wp2():
    """Word Problem 2: Fractions with Ratio and Percentage"""
    q_num = get_next_q_num()
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 50)
    ax.axis('off')
    
    # Draw tank/container representation
    tank = FancyBboxPatch((20, 10), 60, 30, boxstyle="round,pad=0.02",
                          facecolor='lightblue', edgecolor='black', linewidth=2)
    ax.add_patch(tank)
    
    # Water levels
    ax.axhline(y=18, xmin=0.22, xmax=0.78, color='blue', linewidth=3, alpha=0.4)
    ax.axhline(y=28, xmin=0.22, xmax=0.78, color='blue', linewidth=3, alpha=0.7)
    ax.axhline(y=35, xmin=0.22, xmax=0.78, color='blue', linewidth=3, alpha=0.8)
    
    # Labels
    ax.text(50, 15, 'Initial: 2/5', ha='center', fontsize=9, color='darkblue')
    ax.text(50, 22, 'After Pipe A: 3/4', ha='center', fontsize=9, color='darkblue')
    ax.text(50, 31, 'After Pipe B: Full', ha='center', fontsize=9, color='darkblue')
    ax.text(50, 38, 'Full Tank', ha='center', fontsize=9, color='darkblue')
    
    # Pipe indicators
    ax.annotate('', xy=(15, 25), xytext=(5, 35),
                arrowprops=dict(arrowstyle='->', color='green', lw=2))
    ax.text(5, 38, 'Inlet A', fontsize=9, color='green')
    
    ax.annotate('', xy=(85, 20), xytext=(95, 30),
                arrowprops=dict(arrowstyle='->', color='red', lw=2))
    ax.text(90, 33, 'Inlet B', fontsize=9, color='red')
    
    ax.text(50, 47, f'Question {q_num}: Water Tank Problem', ha='center', fontsize=12, fontweight='bold')
    
    filepath = save_fig(fig, f'Q{q_num:02d}_diagram.png')
    
    vrs = create_vrs(
        "Word Problem",
        ["Fractions", "Ratio", "Percentage", "Working Backwards"],
        "Hard",
        ["Tank container", "Water level indicators", "Pipe flow arrows"],
        ["Express initial as fraction", "Calculate first addition", "Determine second addition", "Find full capacity"],
        ["Confusing which fraction refers to what", "Adding instead of finding base"]
    )
    
    question_text = f"""Question {q_num}:
A rectangular tank is partially filled with water. Initially, the water 
occupies 2/5 of the tank's capacity. When Pipe A is turned on for 
15 minutes, the tank becomes 3/4 full. Pipe B, which fills at twice 
the rate of Pipe A, is then used to fill the remaining space.

(a) What fraction of the tank is filled by Pipe A alone? [2 marks]

(b) Express the ratio of Pipe A's rate to Pipe B's rate in simplest form. [1 mark]

(c) If Pipe B takes 10 minutes to fill the remainder, what is the 
    total capacity of the tank in litres, given that Pipe A delivers 
    12 litres per minute? [3 marks]

(d) If both pipes are used together from the start with an empty tank, 
    how long will it take to fill 90% of the tank? [2 marks]
"""
    
    return q_num, question_text, vrs, filepath

def generate_wp3():
    """Word Problem 3: Money with Supposition Method"""
    q_num = get_next_q_num()
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 60)
    ax.axis('off')
    
    # Draw tables/chairs arrangement
    for i in range(4):
        for j in range(3):
            x = 15 + i * 18
            y = 15 + j * 12
            # Table
            rect = patches.Rectangle((x, y), 10, 6, linewidth=1.5, edgecolor='brown', facecolor='wheat')
            ax.add_patch(rect)
            # Chairs
            chair1 = patches.Circle((x-3, y+3), 2, facecolor='tan', edgecolor='brown')
            chair2 = patches.Circle((x+13, y+3), 2, facecolor='tan', edgecolor='brown')
            ax.add_patch(chair1)
            ax.add_patch(chair2)
    
    # Legend
    ax.text(75, 50, 'Furniture Prices:', fontsize=10, fontweight='bold')
    ax.text(75, 45, '• Table: $x', fontsize=9)
    ax.text(75, 41, '• Chair: $(x-35)', fontsize=9)
    
    ax.text(50, 58, f'Question {q_num}: Furniture Purchase', ha='center', fontsize=12, fontweight='bold')
    
    filepath = save_fig(fig, f'Q{q_num:02d}_diagram.png')
    
    vrs = create_vrs(
        "Word Problem",
        ["Supposition Method", "Simultaneous Equations", "Money Calculations", "Pattern Recognition"],
        "Hard",
        ["Furniture arrangement grid", "Price legend", "Visual count aid"],
        ["Set up supposition assumption", "Calculate total difference", "Find unit price", "Verify with constraints"],
        ["Assuming wrong base unit", "Not accounting for price relationship"]
    )
    
    question_text = f"""Question {q_num}:
A restaurant owner purchased tables and chairs for the dining area. 
Each table costs $35 more than each chair. He bought 12 tables and 
48 chairs for a total of $4,320.

(a) Using the supposition method, find the cost of one table. [3 marks]

(b) How much would 8 tables and 24 chairs cost? [2 marks]

(c) During a sale, tables are discounted by 15% and chairs by 20%. 
    If the owner had waited for the sale, how much would he have saved 
    on his purchase of 12 tables and 48 chairs? [3 marks]
"""
    
    return q_num, question_text, vrs, filepath

def generate_wp4():
    """Word Problem 4: Average with Number Patterns"""
    q_num = get_next_q_num()
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 50)
    ax.axis('off')
    
    # Number line representation
    ax.plot([10, 90], [25, 25], 'k-', linewidth=2)
    for i, x in enumerate([20, 35, 50, 65, 80]):
        ax.plot(x, 25, 'ko', markersize=10)
        ax.text(x, 20, f'S{i+1}', ha='center', fontsize=10, fontweight='bold')
    
    # Average markers
    ax.axvline(x=50, ymin=0.4, ymax=0.7, color='red', linestyle='--', linewidth=2)
    ax.text(50, 32, 'Overall Average: 72', ha='center', fontsize=9, color='red')
    
    # Arrows showing differences
    ax.annotate('', xy=(35, 30), xytext=(50, 30),
                arrowprops=dict(arrowstyle='->', color='blue', lw=1.5))
    ax.text(42, 33, '-8', fontsize=9, color='blue')
    
    ax.text(50, 47, f'Question {q_num}: Test Score Analysis', ha='center', fontsize=12, fontweight='bold')
    
    filepath = save_fig(fig, f'Q{q_num:02d}_diagram.png')
    
    vrs = create_vrs(
        "Word Problem",
        ["Average", "Number Patterns", "Algebraic Thinking", "Data Analysis"],
        "Hard",
        ["Number line", "Score points", "Average marker", "Difference arrows"],
        ["Express all scores relative to average", "Set up total equation", "Solve for unknown", "Verify pattern"],
        ["Treating average as a score itself", "Forgetting total = average × count"]
    )
    
    question_text = f"""Question {q_num}:
Five students took a mathematics test. The average score was 72 marks. 
When arranged in order, each student's score was 8 marks higher than 
the previous student. The highest score was 88 marks.

(a) Find the lowest score. [2 marks]

(b) Calculate the total marks scored by all five students. [1 mark]

(c) If the passing mark is 60, how many students passed the test? [2 marks]

(d) A sixth student takes the test. What is the minimum score needed 
    to raise the class average to 75 marks? [3 marks]
"""
    
    return q_num, question_text, vrs, filepath

def generate_wp5():
    """Word Problem 5: Area/Perimeter with Cost Optimization"""
    q_num = get_next_q_num()
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 60)
    ax.axis('off')
    
    # Draw L-shaped garden
    # Main rectangle
    rect1 = patches.Rectangle((20, 15), 50, 30, linewidth=2, edgecolor='green', facecolor='lightgreen', alpha=0.5)
    ax.add_patch(rect1)
    # Cutout
    rect2 = patches.Rectangle((55, 15), 15, 15, linewidth=2, edgecolor='white', facecolor='white')
    ax.add_patch(rect2)
    # Re-add border for cutout
    ax.plot([55, 55], [15, 30], 'g-', linewidth=2)
    ax.plot([55, 70], [30, 30], 'g-', linewidth=2)
    ax.plot([70, 70], [30, 15], 'g-', linewidth=2)
    
    # Dimensions
    ax.text(45, 12, '15 m', ha='center', fontsize=9)
    ax.text(17, 30, '12 m', ha='center', fontsize=9, rotation=90)
    ax.text(62, 12, '8 m', ha='center', fontsize=9)
    ax.text(72, 22, '7 m', ha='center', fontsize=9, rotation=90)
    
    # Fencing cost info
    box = FancyBboxPatch((5, 42), 40, 15, boxstyle="round,pad=0.02",
                          facecolor='lightyellow', edgecolor='black')
    ax.add_patch(box)
    ax.text(25, 54, 'Fencing: $18/m', ha='center', fontsize=9, fontweight='bold')
    ax.text(25, 48, 'Grass: $25/m²', ha='center', fontsize=9, fontweight='bold')
    
    ax.text(50, 58, f'Question {q_num}: Garden Design', ha='center', fontsize=12, fontweight='bold')
    
    filepath = save_fig(fig, f'Q{q_num:02d}_diagram.png')
    
    vrs = create_vrs(
        "Word Problem",
        ["Area", "Perimeter", "Cost Calculation", "Composite Shapes"],
        "Hard",
        ["L-shaped polygon", "Dimension labels", "Cost information box"],
        ["Decompose shape", "Calculate individual areas", "Sum for total area", "Calculate perimeter", "Apply unit costs"],
        ["Missing internal edges in perimeter", "Double-counting overlap areas"]
    )
    
    question_text = f"""Question {q_num}:
Mr. Tan is designing a garden in the shape shown below. The garden 
has an L-shape with the following dimensions: overall length 15 m, 
overall width 12 m, with a rectangular cutout of 8 m by 7 m from 
one corner.

(a) Calculate the area of the garden. [2 marks]

(b) Find the perimeter of the garden. [2 marks]

(c) Mr. Tan wants to fence the garden and plant grass on the entire 
    area. Fencing costs $18 per metre and grass costs $25 per m². 
    Calculate the total cost. [3 marks]

(d) If Mr. Tan decides to leave a 1-metre wide path around the entire 
    inside perimeter (reducing the grass area), what is the new cost 
    of the grass only? [3 marks]
"""
    
    return q_num, question_text, vrs, filepath

def generate_wp6():
    """Word Problem 6: Volume with Rate and Time"""
    q_num = get_next_q_num()
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 60)
    ax.axis('off')
    
    # Draw tank with tap
    # Tank
    tank = patches.Rectangle((30, 10), 40, 35, linewidth=2, edgecolor='black', facecolor='lightcyan')
    ax.add_patch(tank)
    
    # Water levels at different times
    ax.axhline(y=20, xmin=0.31, xmax=0.69, color='blue', linewidth=8, alpha=0.4)
    ax.axhline(y=30, xmin=0.31, xmax=0.69, color='blue', linewidth=8, alpha=0.5)
    
    # Tap
    ax.plot([48, 48], [50, 45], 'k-', linewidth=3)
    ax.plot([45, 51], [50, 50], 'k-', linewidth=3)
    ax.plot([46, 50], [47, 47], 'k-', linewidth=2)
    
    # Water drops
    for y in [42, 38, 34]:
        ax.plot(48, y, 'bo', markersize=4)
    
    # Time labels
    ax.text(50, 22, '10:00 a.m.', fontsize=9, ha='center')
    ax.text(50, 32, '10:30 a.m.', fontsize=9, ha='center')
    ax.text(75, 35, 'Base: 60 cm × 40 cm', fontsize=9)
    ax.text(75, 30, 'Height: 50 cm', fontsize=9)
    
    ax.text(50, 58, f'Question {q_num}: Filling Tank', ha='center', fontsize=12, fontweight='bold')
    
    filepath = save_fig(fig, f'Q{q_num:02d}_diagram.png')
    
    vrs = create_vrs(
        "Word Problem",
        ["Volume", "Rate", "Time", "Unit Conversion"],
        "Hard",
        ["Tank container", "Water level indicators", "Tap with drops", "Time stamps"],
        ["Calculate volume difference", "Determine time elapsed", "Find flow rate", "Predict completion time"],
        ["Mixing cm and m", "Not converting minutes to hours consistently"]
    )
    
    question_text = f"""Question {q_num}:
A rectangular tank measures 60 cm long, 40 cm wide and 50 cm high. 
A tap is turned on to fill the empty tank at a constant rate. At 
10:00 a.m., the water level is 10 cm. At 10:30 a.m., the water 
level is 25 cm.

(a) Calculate the volume of water in the tank at 10:30 a.m. [2 marks]

(b) Find the rate of water flow in litres per minute. [2 marks]

(c) At what time will the tank be completely filled? [3 marks]

(d) If the tap is turned off when the tank is 80% full, and then 
    a drain hole that empties at 0.5 litres per minute is opened, 
    how long will it take to empty the tank completely? [3 marks]
"""
    
    return q_num, question_text, vrs, filepath

def generate_wp7():
    """Word Problem 7: Ratio with Changing Scenarios"""
    q_num = get_next_q_num()
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 50)
    ax.axis('off')
    
    # Before and After boxes
    # Before
    box1 = FancyBboxPatch((5, 15), 40, 25, boxstyle="round,pad=0.02",
                          facecolor='lightyellow', edgecolor='orange', linewidth=2)
    ax.add_patch(box1)
    ax.text(25, 37, 'BEFORE', ha='center', fontsize=10, fontweight='bold', color='orange')
    ax.text(25, 30, 'Red : Blue = 3 : 5', ha='center', fontsize=10)
    ax.text(25, 23, 'Total: 120 marbles', ha='center', fontsize=9)
    
    # Arrow
    ax.annotate('', xy=(55, 27), xytext=(50, 27),
                arrowprops=dict(arrowstyle='->', color='black', lw=2))
    ax.text(52, 31, 'Add', fontsize=9, ha='center')
    
    # After
    box2 = FancyBboxPatch((60, 15), 35, 25, boxstyle="round,pad=0.02",
                          facecolor='lightgreen', edgecolor='green', linewidth=2)
    ax.add_patch(box2)
    ax.text(77, 37, 'AFTER', ha='center', fontsize=10, fontweight='bold', color='green')
    ax.text(77, 30, 'Red : Blue = 2 : 3', ha='center', fontsize=10)
    ax.text(77, 23, 'Total: ?', ha='center', fontsize=9)
    
    ax.text(50, 47, f'Question {q_num}: Marble Collection', ha='center', fontsize=12, fontweight='bold')
    
    filepath = save_fig(fig, f'Q{q_num:02d}_diagram.png')
    
    vrs = create_vrs(
        "Word Problem",
        ["Ratio", "Constant Quantity", "Proportion", "Problem Solving"],
        "Hard",
        ["Before/After boxes", "Ratio displays", "Arrow transition", "Total indicators"],
        ["Identify constant quantity", "Express ratios with common parts", "Calculate unit value", "Find new total"],
        ["Assuming both quantities change", "Not finding common base for ratios"]
    )
    
    question_text = f"""Question {q_num}:
A bag contains red and blue marbles in the ratio 3:5. There are 
120 marbles altogether. Some red marbles are added to the bag, 
changing the ratio of red to blue marbles to 2:3.

(a) How many red marbles were in the bag at first? [2 marks]

(b) How many red marbles were added? [3 marks]

(c) How many blue marbles must be removed so that the ratio of 
    red to blue becomes 3:2? [3 marks]

(d) If instead of removing blue marbles, more red marbles are added 
    to achieve the 3:2 ratio, how many red marbles must be added? [2 marks]
"""
    
    return q_num, question_text, vrs, filepath

def generate_wp8():
    """Word Problem 8: Speed with Overtaking/Meeting"""
    q_num = get_next_q_num()
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 60)
    ax.axis('off')
    
    # Track/Road
    ax.plot([10, 90], [30, 30], 'k-', linewidth=3)
    ax.plot([10, 90], [25, 25], 'k-', linewidth=1, linestyle='--')
    
    # Town markers
    ax.plot(15, 30, 'bs', markersize=12)
    ax.plot(85, 30, 'rs', markersize=12)
    ax.text(15, 22, 'Town P', ha='center', fontsize=10, fontweight='bold')
    ax.text(85, 22, 'Town Q', ha='center', fontsize=10, fontweight='bold')
    
    # Distance
    ax.annotate('', xy=(85, 38), xytext=(15, 38),
                arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
    ax.text(50, 42, '360 km', ha='center', fontsize=11, fontweight='bold')
    
    # Cars
    ax.text(30, 35, 'Car A: 80 km/h', fontsize=12)
    ax.text(60, 18, 'Car B: 100 km/h', fontsize=12)
    
    # Meeting point indicator
    ax.plot(50, 30, 'g*', markersize=15)
    ax.text(50, 48, 'Meeting Point', ha='center', fontsize=9, color='green')
    
    ax.text(50, 56, f'Question {q_num}: Journey Between Towns', ha='center', fontsize=12, fontweight='bold')
    
    filepath = save_fig(fig, f'Q{q_num:02d}_diagram.png')
    
    vrs = create_vrs(
        "Word Problem",
        ["Speed", "Distance", "Time", "Relative Motion"],
        "Hard",
        ["Road track", "Town markers", "Distance annotation", "Vehicle positions", "Meeting point"],
        ["Calculate relative speed", "Determine meeting time", "Find distances traveled", "Calculate arrival times"],
        ["Adding speeds instead of using relative", "Forgetting they start at different times"]
    )
    
    question_text = f"""Question {q_num}:
Town P and Town Q are 360 km apart. Car A leaves Town P for Town Q 
at 80 km/h. At the same time, Car B leaves Town Q for Town P at 
100 km/h.

(a) How long will it take for the two cars to meet? [2 marks]

(b) How far from Town P will they meet? [2 marks]

(c) If Car A had started 30 minutes earlier than Car B, how far 
    from Town Q would they meet? [4 marks]

(d) After meeting, both cars continue to their destinations. How 
    long after Car A arrives at Town Q will Car B arrive at Town P? [2 marks]
"""
    
    return q_num, question_text, vrs, filepath

def generate_wp9():
    """Word Problem 9: Fractions with Remainder Concept"""
    q_num = get_next_q_num()
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 50)
    ax.axis('off')
    
    # Bar model representation
    # Total bar
    total_bar = patches.Rectangle((10, 30), 80, 8, linewidth=2, edgecolor='black', facecolor='lightgray')
    ax.add_patch(total_bar)
    ax.text(50, 42, 'Total Money', ha='center', fontsize=10, fontweight='bold')
    
    # Segments
    # Spent on books
    seg1 = patches.Rectangle((10, 30), 24, 8, linewidth=1, edgecolor='black', facecolor='lightcoral')
    ax.add_patch(seg1)
    ax.text(22, 26, '1/3 (Books)', ha='center', fontsize=8)
    
    # Remainder
    seg2 = patches.Rectangle((34, 30), 56, 8, linewidth=1, edgecolor='black', facecolor='lightyellow')
    ax.add_patch(seg2)
    ax.text(62, 26, 'Remainder', ha='center', fontsize=8)
    
    # Of remainder
    seg3 = patches.Rectangle((34, 30), 28, 8, linewidth=1, edgecolor='black', facecolor='lightblue')
    ax.add_patch(seg3)
    ax.text(48, 18, '1/2 of remainder (Toys)', ha='center', fontsize=8)
    
    # Final remainder
    seg4 = patches.Rectangle((62, 30), 28, 8, linewidth=1, edgecolor='black', facecolor='lightgreen')
    ax.add_patch(seg4)
    ax.text(76, 18, 'Left: $84', ha='center', fontsize=8, fontweight='bold')
    
    ax.text(50, 47, f'Question {q_num}: Spending Pattern', ha='center', fontsize=12, fontweight='bold')
    
    filepath = save_fig(fig, f'Q{q_num:02d}_diagram.png')
    
    vrs = create_vrs(
        "Word Problem",
        ["Fractions", "Remainder Concept", "Working Backwards", "Bar Model"],
        "Hard",
        ["Bar model segments", "Fraction labels", "Color coding", "Final amount"],
        ["Identify final remainder", "Work backwards through fractions", "Calculate original amount", "Verify forward"],
        ["Applying fraction to original instead of remainder", "Arithmetic errors in working backwards"]
    )
    
    question_text = f"""Question {q_num}:
Jane had some money. She spent 1/3 of her money on books. Then she 
spent 1/2 of the remainder on toys. Finally, she spent 1/4 of what 
was left on stationery. She had $84 left.

(a) How much money did Jane have at first? [4 marks]

(b) How much did she spend on books? [2 marks]

(c) What fraction of her original money was spent on toys? [2 marks]

(d) If Jane wants to buy a $120 bag with the money she has left, 
    how much more money does she need? [2 marks]
"""
    
    return q_num, question_text, vrs, filepath

def generate_wp10():
    """Word Problem 10: Percentage with Successive Changes"""
    q_num = get_next_q_num()
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 50)
    ax.axis('off')
    
    # Price change diagram
    # Original
    box1 = FancyBboxPatch((5, 20), 25, 20, boxstyle="round,pad=0.02",
                          facecolor='lightblue', edgecolor='blue', linewidth=2)
    ax.add_patch(box1)
    ax.text(17, 35, 'Original', ha='center', fontsize=9, fontweight='bold')
    ax.text(17, 28, '$800', ha='center', fontsize=11, fontweight='bold')
    
    # Arrow 1
    ax.annotate('', xy=(35, 30), xytext=(32, 30),
                arrowprops=dict(arrowstyle='->', color='red', lw=2))
    ax.text(33, 34, '-20%', fontsize=9, color='red', ha='center')
    
    # After discount
    box2 = FancyBboxPatch((38, 20), 25, 20, boxstyle="round,pad=0.02",
                          facecolor='lightyellow', edgecolor='orange', linewidth=2)
    ax.add_patch(box2)
    ax.text(50, 35, 'Discounted', ha='center', fontsize=9, fontweight='bold')
    ax.text(50, 28, '$640', ha='center', fontsize=11, fontweight='bold')
    
    # Arrow 2
    ax.annotate('', xy=(68, 30), xytext=(65, 30),
                arrowprops=dict(arrowstyle='->', color='green', lw=2))
    ax.text(66, 34, '+15%', fontsize=9, color='green', ha='center')
    
    # Final
    box3 = FancyBboxPatch((71, 20), 25, 20, boxstyle="round,pad=0.02",
                          facecolor='lightgreen', edgecolor='green', linewidth=2)
    ax.add_patch(box3)
    ax.text(83, 35, 'Final', ha='center', fontsize=9, fontweight='bold')
    ax.text(83, 28, '$?', ha='center', fontsize=11, fontweight='bold')
    
    ax.text(50, 47, f'Question {q_num}: Price Adjustments', ha='center', fontsize=12, fontweight='bold')
    
    filepath = save_fig(fig, f'Q{q_num:02d}_diagram.png')
    
    vrs = create_vrs(
        "Word Problem",
        ["Percentage", "Successive Changes", "Multiplicative Reasoning", "Comparison"],
        "Hard",
        ["Price boxes", "Percentage arrows", "Value displays", "Color-coded stages"],
        ["Apply first percentage change", "Calculate intermediate value", "Apply second change", "Compare to original"],
        ["Adding/subtracting percentages directly", "Using wrong base for second percentage"]
    )
    
    question_text = f"""Question {q_num}:
A laptop was priced at $800. During a sale, its price was reduced 
by 20%. After the sale, the price was increased by 15%.

(a) What was the sale price of the laptop? [2 marks]

(b) What is the final price after the increase? [2 marks]

(c) What is the overall percentage change from the original price 
    to the final price? [3 marks]

(d) If the shop wants to return to the original price of $800 from 
    the final price, what percentage discount should be applied? [3 marks]
"""
    
    return q_num, question_text, vrs, filepath

def generate_wp11():
    """Word Problem 11: Age with Future/Past Scenarios"""
    q_num = get_next_q_num()
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 50)
    ax.axis('off')
    
    # Timeline
    ax.plot([10, 90], [25, 25], 'k-', linewidth=2)
    
    # Time markers
    times = [15, 40, 65, 85]
    labels = ['Now', '5 years ago', 'In 8 years', 'In 15 years']
    for i, (x, label) in enumerate(zip(times, labels)):
        ax.plot(x, 25, 'ko', markersize=8)
        ax.text(x, 20, label, ha='center', fontsize=8, rotation=15)
    
    # Age brackets
    ax.plot([15, 40], [32, 32], 'b-', linewidth=2)
    ax.text(27, 35, 'Father 4x Son', ha='center', fontsize=9, color='blue')
    
    ax.plot([40, 65], [38, 38], 'r-', linewidth=2)
    ax.text(52, 41, 'Sum = 56', ha='center', fontsize=9, color='red')
    
    ax.text(50, 47, f'Question {q_num}: Age Relationship', ha='center', fontsize=12, fontweight='bold')
    
    filepath = save_fig(fig, f'Q{q_num:02d}_diagram.png')
    
    vrs = create_vrs(
        "Word Problem",
        ["Age Problems", "Ratio", "Sum/Difference", "Temporal Reasoning"],
        "Hard",
        ["Timeline", "Time markers", "Relationship brackets", "Age indicators"],
        ["Define variables for current ages", "Express past relationship", "Express future sum", "Solve system"],
        ["Not adjusting both ages equally", "Confusing whose age is being referenced"]
    )
    
    question_text = f"""Question {q_num}:
Five years ago, a father was 4 times as old as his son. In 8 years' 
time, the sum of their ages will be 56 years.

(a) Find the son's current age. [4 marks]

(b) How many years ago was the father 7 times as old as his son? [3 marks]

(c) In how many years will the father be twice as old as his son? [3 marks]
"""
    
    return q_num, question_text, vrs, filepath

def generate_wp12():
    """Word Problem 12: Mass with Transfer Between Containers"""
    q_num = get_next_q_num()
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 60)
    ax.axis('off')
    
    # Three containers
    # Container A
    box_a = patches.Rectangle((10, 15), 20, 30, linewidth=2, edgecolor='blue', facecolor='lightblue', alpha=0.5)
    ax.add_patch(box_a)
    ax.text(20, 12, 'Box A', ha='center', fontsize=10, fontweight='bold')
    ax.text(20, 25, '? kg', ha='center', fontsize=11)
    
    # Container B
    box_b = patches.Rectangle((40, 15), 20, 25, linewidth=2, edgecolor='green', facecolor='lightgreen', alpha=0.5)
    ax.add_patch(box_b)
    ax.text(50, 12, 'Box B', ha='center', fontsize=10, fontweight='bold')
    ax.text(50, 22, '? kg', ha='center', fontsize=11)
    
    # Container C
    box_c = patches.Rectangle((70, 15), 20, 20, linewidth=2, edgecolor='red', facecolor='lightcoral', alpha=0.5)
    ax.add_patch(box_c)
    ax.text(80, 12, 'Box C', ha='center', fontsize=10, fontweight='bold')
    ax.text(80, 20, '? kg', ha='center', fontsize=11)
    
    # Transfer arrows
    ax.annotate('', xy=(38, 35), xytext=(32, 35),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
    ax.text(35, 38, '1/4 to B', fontsize=8, ha='center')
    
    ax.annotate('', xy=(68, 30), xytext=(62, 30),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
    ax.text(65, 33, '1/3 to C', fontsize=8, ha='center')
    
    # Final info
    ax.text(50, 50, 'Final: A = C, and A + B + C = 180 kg', ha='center', fontsize=10, fontweight='bold')
    
    ax.text(50, 57, f'Question {q_num}: Mass Transfer', ha='center', fontsize=12, fontweight='bold')
    
    filepath = save_fig(fig, f'Q{q_num:02d}_diagram.png')
    
    vrs = create_vrs(
        "Word Problem",
        ["Mass Transfer", "Fractions", "Simultaneous Equations", "Conservation"],
        "Hard",
        ["Container boxes", "Transfer arrows", "Fraction labels", "Final condition"],
        ["Track transfers step by step", "Express all in terms of original", "Apply final conditions", "Solve for original"],
        ["Not accounting for mass leaving source", "Arithmetic errors in fraction operations"]
    )
    
    question_text = f"""Question {q_num}:
Three boxes A, B and C contain a total of 180 kg of rice. 1/4 of 
the rice from Box A is transferred to Box B. Then 1/3 of the rice 
in Box B is transferred to Box C. In the end, Box A and Box C 
contain the same mass of rice.

(a) Find the final mass of rice in Box C. [3 marks]

(b) Find the original mass of rice in Box A. [4 marks]

(c) How much rice was transferred from Box B to Box C? [3 marks]
"""
    
    return q_num, question_text, vrs, filepath

def generate_wp13():
    """Word Problem 13: Distance with Multiple Legs"""
    q_num = get_next_q_num()
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 50)
    ax.axis('off')
    
    # Journey segments
    segments = [
        (15, 30, 'Home to A', '60 km', '40 km/h'),
        (35, 30, 'A to B', '90 km', '60 km/h'),
        (55, 30, 'B to C', '45 km', '30 km/h'),
        (80, 30, 'C to D', '? km', '50 km/h'),
    ]
    
    for i, (x, y, label, dist, speed) in enumerate(segments):
        # Segment box
        box = FancyBboxPatch((x-10, y-10), 22, 20, boxstyle="round,pad=0.01",
                             facecolor='lightyellow', edgecolor='black', linewidth=1)
        ax.add_patch(box)
        ax.text(x+1, y+4, label, ha='center', fontsize=7, fontweight='bold')
        ax.text(x+1, y-1, dist, ha='center', fontsize=8)
        ax.text(x+1, y-6, speed, ha='center', fontsize=7, color='blue')
        
        # Arrow to next
        if i < 3:
            ax.annotate('', xy=(x+16, y), xytext=(x+13, y),
                        arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
    
    # Total info
    ax.text(50, 45, 'Total journey time: 5 hours 30 minutes', ha='center', fontsize=10, fontweight='bold')
    ax.text(50, 5, f'Question {q_num}: Multi-Leg Journey', ha='center', fontsize=12, fontweight='bold')
    
    filepath = save_fig(fig, f'Q{q_num:02d}_diagram.png')
    
    vrs = create_vrs(
        "Word Problem",
        ["Speed", "Distance", "Time", "Multi-Leg Journey"],
        "Hard",
        ["Journey segments", "Distance labels", "Speed annotations", "Direction arrows"],
        ["Calculate time for each known leg", "Sum known times", "Find remaining time", "Calculate unknown distance"],
        ["Not converting time properly", "Using wrong speed for wrong leg"]
    )
    
    question_text = f"""Question {q_num}:
A cyclist travels from Home to Town D through Towns A, B and C. 
The distances and speeds for each leg are shown below. The total 
journey takes 5 hours 30 minutes.

Leg 1: Home to A - 60 km at 40 km/h
Leg 2: A to B - 90 km at 60 km/h  
Leg 3: B to C - 45 km at 30 km/h
Leg 4: C to D - unknown distance at 50 km/h

(a) Calculate the time taken for the first three legs. [3 marks]

(b) Find the distance from C to D. [3 marks]

(c) What is the average speed for the entire journey? [2 marks]

(d) If the cyclist wants to complete the journey in 5 hours, what 
    minimum speed is required for the last leg? [2 marks]
"""
    
    return q_num, question_text, vrs, filepath

def generate_wp14():
    """Word Problem 14: Volume with Displacement"""
    q_num = get_next_q_num()
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 60)
    ax.axis('off')
    
    # Tank
    tank = patches.Rectangle((25, 10), 50, 40, linewidth=2, edgecolor='black', facecolor='lightcyan', alpha=0.3)
    ax.add_patch(tank)
    
    # Water levels
    ax.axhline(y=20, xmin=0.26, xmax=0.74, color='blue', linewidth=12, alpha=0.4)
    ax.text(82, 20, 'Initial: 8 cm', fontsize=9)
    
    # Metal block
    block = patches.Rectangle((40, 20), 20, 15, linewidth=2, edgecolor='gray', facecolor='silver')
    ax.add_patch(block)
    ax.text(50, 27, 'Metal\nBlock', ha='center', va='center', fontsize=9)
    ax.text(50, 15, '15 cm x 10 cm x 8 cm', ha='center', fontsize=8)
    
    # New water level
    ax.axhline(y=32, xmin=0.26, xmax=0.74, color='blue', linewidth=12, alpha=0.4)
    ax.text(82, 32, 'Final: 20 cm', fontsize=9)
    
    # Tank dimensions
    ax.text(50, 5, 'Tank base: 30 cm x 25 cm', ha='center', fontsize=9)
    
    ax.text(50, 57, f'Question {q_num}: Water Displacement', ha='center', fontsize=12, fontweight='bold')
    
    filepath = save_fig(fig, f'Q{q_num:02d}_diagram.png')
    
    vrs = create_vrs(
        "Word Problem",
        ["Volume", "Displacement", "Water Level Change", "3D Geometry"],
        "Hard",
        ["Tank container", "Water levels", "Submerged object", "Dimension labels"],
        ["Calculate block volume", "Calculate base area", "Find height change", "Verify final level"],
        ["Using wrong base area", "Not checking if block is fully submerged"]
    )
    
    question_text = f"""Question {q_num}:
A rectangular tank measures 30 cm long, 25 cm wide and 40 cm high. 
It contains water to a depth of 8 cm. A metal block measuring 
15 cm x 10 cm x 8 cm is placed into the tank, resting flat on 
the bottom.

(a) Calculate the volume of the metal block. [1 mark]

(b) Find the new water level after the block is placed in the tank. [3 marks]

(c) How many more identical blocks can be added before the water 
    reaches the top of the tank? [4 marks]

(d) If the block is removed and 5 litres of water are added, what 
    is the new water depth? [2 marks]
"""
    
    return q_num, question_text, vrs, filepath

def generate_wp15():
    """Word Problem 15: Ratio with Grouping"""
    q_num = get_next_q_num()
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 60)
    ax.axis('off')
    
    # Group representation
    # Boys
    for i in range(5):
        circle = patches.Circle((15 + i*8, 40), 3, facecolor='lightblue', edgecolor='blue', linewidth=1.5)
        ax.add_patch(circle)
        ax.text(15 + i*8, 40, 'B', ha='center', va='center', fontsize=8)
    ax.text(35, 47, 'Boys: 5 units', ha='center', fontsize=10, fontweight='bold')
    
    # Girls
    for i in range(3):
        circle = patches.Circle((15 + i*8, 25), 3, facecolor='lightpink', edgecolor='red', linewidth=1.5)
        ax.add_patch(circle)
        ax.text(15 + i*8, 25, 'G', ha='center', va='center', fontsize=8)
    ax.text(23, 18, 'Girls: 3 units', ha='center', fontsize=10, fontweight='bold')
    
    # Adults
    for i in range(2):
        circle = patches.Circle((65 + i*10, 32), 4, facecolor='lightgreen', edgecolor='green', linewidth=1.5)
        ax.add_patch(circle)
        ax.text(65 + i*10, 32, 'A', ha='center', va='center', fontsize=8)
    ax.text(70, 42, 'Adults: 2 units', ha='center', fontsize=10, fontweight='bold')
    
    # Info box
    box = FancyBboxPatch((5, 5), 90, 8, boxstyle="round,pad=0.01",
                          facecolor='lightyellow', edgecolor='black')
    ax.add_patch(box)
    ax.text(50, 9, 'Total people: 120 | Each boy gets 3 sweets, each girl gets 4 sweets, each adult gets 2 sweets', 
            ha='center', fontsize=8)
    
    ax.text(50, 56, f'Question {q_num}: Group Distribution', ha='center', fontsize=12, fontweight='bold')
    
    filepath = save_fig(fig, f'Q{q_num:02d}_diagram.png')
    
    vrs = create_vrs(
        "Word Problem",
        ["Ratio", "Distribution", "Unit Method", "Multi-Group"],
        "Hard",
        ["Group icons", "Unit labels", "Visual representation", "Distribution info"],
        ["Express ratio in units", "Calculate total units", "Find value per unit", "Calculate per-group totals"],
        ["Confusing which unit applies to which group", "Arithmetic errors in distribution"]
    )
    
    question_text = f"""Question {q_num}:
At a party, the ratio of boys to girls to adults is 5:3:2. There 
are 120 people at the party altogether. Each boy receives 3 sweets, 
each girl receives 4 sweets, and each adult receives 2 sweets.

(a) How many boys are at the party? [2 marks]

(b) Calculate the total number of sweets distributed. [3 marks]

(c) If the ratio of boys to girls to adults was instead 4:4:2 with 
    the same total number of people, how many more or fewer sweets 
    would be needed? [3 marks]

(d) What is the minimum number of sweets that must be added so that 
    everyone receives the same number of sweets? [2 marks]
"""
    
    return q_num, question_text, vrs, filepath

def generate_wp16():
    """Word Problem 16: Money with GST and Discount"""
    q_num = get_next_q_num()
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 50)
    ax.axis('off')
    
    # Price breakdown
    # Base price
    box1 = FancyBboxPatch((5, 25), 25, 15, boxstyle="round,pad=0.02",
                          facecolor='lightblue', edgecolor='blue', linewidth=2)
    ax.add_patch(box1)
    ax.text(17, 35, 'List Price', ha='center', fontsize=9, fontweight='bold')
    ax.text(17, 29, '$x', ha='center', fontsize=11)
    
    # Arrow
    ax.annotate('', xy=(35, 32), xytext=(32, 32),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
    ax.text(33, 36, '-15%', fontsize=9, ha='center')
    
    # After discount
    box2 = FancyBboxPatch((38, 25), 25, 15, boxstyle="round,pad=0.02",
                          facecolor='lightyellow', edgecolor='orange', linewidth=2)
    ax.add_patch(box2)
    ax.text(50, 35, 'Discounted', ha='center', fontsize=9, fontweight='bold')
    ax.text(50, 29, '0.85x', ha='center', fontsize=11)
    
    # Arrow
    ax.annotate('', xy=(68, 32), xytext=(65, 32),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
    ax.text(66, 36, '+9% GST', fontsize=9, ha='center')
    
    # Final
    box3 = FancyBboxPatch((71, 25), 25, 15, boxstyle="round,pad=0.02",
                          facecolor='lightgreen', edgecolor='green', linewidth=2)
    ax.add_patch(box3)
    ax.text(83, 35, 'Final', ha='center', fontsize=9, fontweight='bold')
    ax.text(83, 29, '$433.50', ha='center', fontsize=11, fontweight='bold')
    
    ax.text(50, 47, f'Question {q_num}: Price with GST', ha='center', fontsize=12, fontweight='bold')
    
    filepath = save_fig(fig, f'Q{q_num:02d}_diagram.png')
    
    vrs = create_vrs(
        "Word Problem",
        ["Money", "Percentage", "GST Calculation", "Reverse Percentage"],
        "Hard",
        ["Price boxes", "Percentage arrows", "Value labels", "Calculation flow"],
        ["Work backwards from final price", "Remove GST to get discounted price", "Remove discount to get list price", "Verify forward"],
        ["Applying GST to wrong base", "Adding/subtracting percentages directly"]
    )
    
    question_text = f"""Question {q_num}:
A television set was sold at a 15% discount from its list price. 
A 9% Goods and Services Tax (GST) was then applied to the discounted 
price. Mrs. Lim paid $433.50 for the television set.

(a) Find the price of the television set before GST was added. [3 marks]

(b) Find the list price of the television set. [3 marks]

(c) What percentage of the list price did Mrs. Lim actually pay 
    (including GST)? [2 marks]

(d) If the GST rate increases to 10% but the discount remains 15%, 
    how much more would Mrs. Lim have to pay? [2 marks]
"""
    
    return q_num, question_text, vrs, filepath

def generate_wp17():
    """Word Problem 17: Area with Scaling"""
    q_num = get_next_q_num()
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 60)
    ax.axis('off')
    
    # Original rectangle
    rect1 = patches.Rectangle((10, 35), 30, 15, linewidth=2, edgecolor='blue', facecolor='lightblue', alpha=0.5)
    ax.add_patch(rect1)
    ax.text(25, 48, 'Original', ha='center', fontsize=9, fontweight='bold')
    ax.text(25, 42, 'L x W', ha='center', fontsize=9)
    ax.text(25, 31, 'Area = 120 cm²', ha='center', fontsize=9)
    
    # Arrow
    ax.annotate('', xy=(50, 42), xytext=(43, 42),
                arrowprops=dict(arrowstyle='->', color='black', lw=2))
    ax.text(46, 47, 'L + 20%\nW + 25%', fontsize=8, ha='center')
    
    # New rectangle
    rect2 = patches.Rectangle((55, 30), 37, 20, linewidth=2, edgecolor='green', facecolor='lightgreen', alpha=0.5)
    ax.add_patch(rect2)
    ax.text(73, 53, 'New', ha='center', fontsize=9, fontweight='bold')
    ax.text(73, 47, '1.2L x 1.25W', ha='center', fontsize=9)
    ax.text(73, 25, 'New Area = ?', ha='center', fontsize=9, fontweight='bold')
    
    ax.text(50, 57, f'Question {q_num}: Area Scaling', ha='center', fontsize=12, fontweight='bold')
    
    filepath = save_fig(fig, f'Q{q_num:02d}_diagram.png')
    
    vrs = create_vrs(
        "Word Problem",
        ["Area", "Scaling", "Percentage", "Dimensional Analysis"],
        "Hard",
        ["Original rectangle", "New rectangle", "Dimension arrows", "Area labels"],
        ["Understand scaling factors", "Calculate new dimensions", "Find new area", "Calculate percentage change"],
        ["Adding percentages instead of multiplying", "Not squaring scale factor for area"]
    )
    
    question_text = f"""Question {q_num}:
A rectangle has an area of 120 cm². Its length is increased by 20% 
and its width is increased by 25%.

(a) Find the new area of the rectangle. [3 marks]

(b) By what percentage has the area increased? [2 marks]

(c) If instead the length was decreased by 20% and the width 
    increased by 25%, what would be the new area? [3 marks]

(d) What percentage change in width would result in no change to 
    the area when the length increases by 20%? [2 marks]
"""
    
    return q_num, question_text, vrs, filepath

def generate_wp18():
    """Word Problem 18: Time with Scheduling"""
    q_num = get_next_q_num()
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 60)
    ax.axis('off')
    
    # Timeline
    ax.plot([10, 90], [30, 30], 'k-', linewidth=2)
    
    # Events
    events = [
        (15, '8:30 a.m.', 'Start Task A\n(45 min)'),
        (35, '9:15 a.m.', 'Start Task B\n(1 hr 20 min)'),
        (55, '10:35 a.m.', 'Break\n(15 min)'),
        (75, '10:50 a.m.', 'Start Task C\n(?)'),
    ]
    
    for x, time, label in events:
        ax.plot(x, 30, 'ko', markersize=8)
        ax.text(x, 22, time, ha='center', fontsize=8, rotation=15)
        ax.text(x, 40, label, ha='center', fontsize=8)
    
    # Completion
    ax.plot(88, 30, 'g*', markersize=12)
    ax.text(88, 22, '12:00 p.m.', ha='center', fontsize=8, color='green', fontweight='bold')
    ax.text(88, 40, 'Finish', ha='center', fontsize=9, color='green', fontweight='bold')
    
    ax.text(50, 55, f'Question {q_num}: Work Schedule', ha='center', fontsize=12, fontweight='bold')
    
    filepath = save_fig(fig, f'Q{q_num:02d}_diagram.png')
    
    vrs = create_vrs(
        "Word Problem",
        ["Time", "Scheduling", "Duration Calculation", "Working Backwards"],
        "Hard",
        ["Timeline", "Event markers", "Time labels", "Duration annotations"],
        ["Calculate end times sequentially", "Account for breaks", "Work backwards from finish", "Find unknown duration"],
        ["Not accounting for break time", "Confusing start and end times"]
    )
    
    question_text = f"""Question {q_num}:
A worker has three tasks to complete. Task A takes 45 minutes. 
Task B takes 1 hour 20 minutes. The worker starts Task A at 8:30 a.m. 
and begins Task B immediately after completing Task A. After 
completing Task B, the worker takes a 15-minute break before 
starting Task C. All work is completed by 12:00 p.m.

(a) At what time does Task B start? [1 mark]

(b) How long does Task C take? [3 marks]

(c) If Task C must be completed by 11:30 a.m., what is the latest 
    time the worker can start Task A? [3 marks]

(d) If the worker could work 20% faster on Task B, how much earlier 
    would all tasks be completed? [3 marks]
"""
    
    return q_num, question_text, vrs, filepath

def generate_wp19():
    """Word Problem 19: Average with Weighted Components"""
    q_num = get_next_q_num()
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 50)
    ax.axis('off')
    
    # Test components
    components = [
        (15, 'CA1', '15%', '72'),
        (35, 'CA2', '15%', '68'),
        (55, 'SA1', '30%', '?'),
        (75, 'SA2', '40%', '78'),
    ]
    
    for x, name, weight, score in components:
        box = FancyBboxPatch((x-8, 20), 16, 20, boxstyle="round,pad=0.02",
                             facecolor='lightyellow', edgecolor='black', linewidth=1.5)
        ax.add_patch(box)
        ax.text(x, 37, name, ha='center', fontsize=10, fontweight='bold')
        ax.text(x, 30, f'Weight: {weight}', ha='center', fontsize=9)
        ax.text(x, 24, f'Score: {score}', ha='center', fontsize=10, color='blue' if score != '?' else 'red')
    
    # Overall
    ax.text(50, 10, 'Overall Average: 75 marks', ha='center', fontsize=11, fontweight='bold')
    
    ax.text(50, 47, f'Question {q_num}: Weighted Average', ha='center', fontsize=12, fontweight='bold')
    
    filepath = save_fig(fig, f'Q{q_num:02d}_diagram.png')
    
    vrs = create_vrs(
        "Word Problem",
        ["Average", "Weighted Average", "Percentage", "Reverse Calculation"],
        "Hard",
        ["Component boxes", "Weight labels", "Score displays", "Overall indicator"],
        ["Calculate weighted contribution of known scores", "Set up equation for unknown", "Solve for missing score", "Verify average"],
        ["Not applying weights correctly", "Dividing by wrong number of components"]
    )
    
    question_text = f"""Question {q_num}:
A student's final grade is calculated from four assessments with 
different weightings:
- CA1: 15% weight, scored 72 marks
- CA2: 15% weight, scored 68 marks  
- SA1: 30% weight, score unknown
- SA2: 40% weight, scored 78 marks

The student's overall average is 75 marks.

(a) Find the student's score for SA1. [4 marks]

(b) If the student wants an overall average of 80 marks, what score 
    is needed for SA1 (assuming other scores remain the same)? [3 marks]

(c) What is the minimum score needed on SA1 to achieve at least 
    an overall pass (50 marks)? [3 marks]
"""
    
    return q_num, question_text, vrs, filepath

def generate_wp20():
    """Word Problem 20: Complex Multi-Concept"""
    q_num = get_next_q_num()
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 60)
    ax.axis('off')
    
    # Factory production diagram
    # Machine A
    box_a = FancyBboxPatch((5, 30), 25, 20, boxstyle="round,pad=0.02",
                           facecolor='lightblue', edgecolor='blue', linewidth=2)
    ax.add_patch(box_a)
    ax.text(17, 47, 'Machine A', ha='center', fontsize=10, fontweight='bold')
    ax.text(17, 40, 'Rate: 45/hr', ha='center', fontsize=9)
    ax.text(17, 34, 'Start: 8:00 a.m.', ha='center', fontsize=8)
    
    # Arrow
    ax.annotate('', xy=(38, 40), xytext=(32, 40),
                arrowprops=dict(arrowstyle='->', color='black', lw=2))
    
    # Machine B
    box_b = FancyBboxPatch((40, 30), 25, 20, boxstyle="round,pad=0.02",
                           facecolor='lightgreen', edgecolor='green', linewidth=2)
    ax.add_patch(box_b)
    ax.text(52, 47, 'Machine B', ha='center', fontsize=10, fontweight='bold')
    ax.text(52, 40, 'Rate: 60/hr', ha='center', fontsize=9)
    ax.text(52, 34, 'Start: 9:30 a.m.', ha='center', fontsize=8)
    
    # Output
    ax.annotate('', xy=(90, 40), xytext=(67, 40),
                arrowprops=dict(arrowstyle='->', color='black', lw=2))
    ax.text(78, 45, 'Total: 900', fontsize=9, ha='center')
    
    # Target box
    target = FancyBboxPatch((75, 30), 20, 15, boxstyle="round,pad=0.02",
                            facecolor='gold', edgecolor='orange', linewidth=2)
    ax.add_patch(target)
    ax.text(85, 37, 'Target', ha='center', fontsize=10, fontweight='bold')
    
    ax.text(50, 57, f'Question {q_num}: Production Schedule', ha='center', fontsize=12, fontweight='bold')
    
    filepath = save_fig(fig, f'Q{q_num:02d}_diagram.png')
    
    vrs = create_vrs(
        "Word Problem",
        ["Rate", "Time", "Work Done", "Simultaneous Start Times", "Optimization"],
        "Hard",
        ["Machine boxes", "Rate labels", "Time annotations", "Output flow", "Target indicator"],
        ["Calculate head start production", "Set up combined rate equation", "Solve for time", "Verify total production"],
        ["Not accounting for different start times", "Adding rates without considering overlap"]
    )
    
    question_text = f"""Question {q_num}:
A factory has two machines producing identical items. Machine A 
produces 45 items per hour and starts at 8:00 a.m. Machine B 
produces 60 items per hour and starts at 9:30 a.m. The target 
production is 900 items.

(a) How many items has Machine A produced by the time Machine B starts? [2 marks]

(b) At what time will the total production reach 900 items? [4 marks]

(c) If Machine B breaks down for 30 minutes at 10:00 a.m., at what 
    time will the target be reached? [4 marks]
"""
    
    return q_num, question_text, vrs, filepath

# ==================== GEOMETRY PROBLEMS (12) ====================

def generate_geo1():
    """Geometry 1: Composite Overlap - Two Circles"""
    q_num = get_next_q_num()
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 8))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 80)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Two overlapping circles
    circle1 = Circle((35, 40), 20, fill=False, edgecolor='blue', linewidth=2)
    circle2 = Circle((55, 40), 20, fill=False, edgecolor='red', linewidth=2)
    ax.add_patch(circle1)
    ax.add_patch(circle2)
    
    # Centers
    ax.plot(35, 40, 'b+', markersize=10)
    ax.plot(55, 40, 'r+', markersize=10)
    ax.text(35, 18, 'O1', ha='center', fontsize=11)
    ax.text(55, 18, 'O2', ha='center', fontsize=11)
    
    # Radius labels
    ax.annotate('', xy=(55, 60), xytext=(35, 60),
                arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
    ax.text(45, 63, '20 cm', ha='center', fontsize=10)
    
    # Intersection points
    ax.plot(45, 40 + np.sqrt(300), 'ko', markersize=6)
    ax.plot(45, 40 - np.sqrt(300), 'ko', markersize=6)
    ax.text(45, 40 + np.sqrt(300) + 3, 'A', ha='center', fontsize=10)
    ax.text(45, 40 - np.sqrt(300) - 5, 'B', ha='center', fontsize=10)
    
    # Distance between centers
    ax.annotate('', xy=(55, 25), xytext=(35, 25),
                arrowprops=dict(arrowstyle='<->', color='green', lw=1.5))
    ax.text(45, 22, '20 cm', ha='center', fontsize=10, color='green')
    
    # Shaded region indicator
    ax.text(45, 75, f'Question {q_num}: Overlapping Circles', ha='center', fontsize=12, fontweight='bold')
    ax.text(45, 5, 'Each circle has radius 20 cm. Distance between centers is 20 cm.', 
            ha='center', fontsize=9, style='italic')
    
    filepath = save_fig(fig, f'Q{q_num:02d}_diagram.png')
    
    vrs = create_vrs(
        "Geometry",
        ["Circle Properties", "Overlapping Areas", "Sector Areas", "Triangle Areas"],
        "Hard",
        ["Two circles", "Intersection points", "Center markers", "Dimension labels"],
        ["Identify equilateral triangles formed", "Calculate sector angles", "Find segment areas", "Calculate overlap region"],
        ["Using wrong angle for sector", "Forgetting to subtract triangle from sector"]
    )
    
    question_text = f"""Question {q_num}:
Two circles with radius 20 cm each have their centers 20 cm apart. 
The circles intersect at points A and B.

(a) Show that triangle O1AO2 is equilateral, where O1 and O2 are 
    the centers of the circles. [2 marks]

(b) Find the area of the sector O1AB in the first circle. [2 marks]

(c) Find the area of the shaded region common to both circles. [4 marks]

(d) Find the perimeter of the shaded region. [2 marks]

(Take pi = 3.14)
"""
    
    return q_num, question_text, vrs, filepath

def generate_geo2():
    """Geometry 2: Grid Construction"""
    q_num = get_next_q_num()
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 8))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 80)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Grid coordinates
    grid_size = 6
    cell_size = 10
    offset_x = 20
    offset_y = 15
    
    # Draw grid
    for i in range(grid_size + 1):
        ax.plot([offset_x, offset_x + grid_size * cell_size], 
                [offset_y + i * cell_size, offset_y + i * cell_size], 'k-', linewidth=0.5)
        ax.plot([offset_x + i * cell_size, offset_x + i * cell_size], 
                [offset_y, offset_y + grid_size * cell_size], 'k-', linewidth=0.5)
    
    # Label axes
    for i in range(grid_size + 1):
        ax.text(offset_x + i * cell_size, offset_y - 3, str(i), ha='center', fontsize=8)
        ax.text(offset_x - 3, offset_y + i * cell_size, str(i), ha='center', fontsize=8, va='center')
    
    # Plot points and shape
    points = [(1, 2), (4, 2), (5, 5), (2, 5)]
    xs = [offset_x + p[0] * cell_size for p in points] + [offset_x + points[0][0] * cell_size]
    ys = [offset_y + p[1] * cell_size for p in points] + [offset_y + points[0][1] * cell_size]
    ax.plot(xs, ys, 'b-', linewidth=2)
    
    for i, (px, py) in enumerate(points):
        ax.plot(offset_x + px * cell_size, offset_y + py * cell_size, 'ro', markersize=8)
        ax.text(offset_x + px * cell_size + 3, offset_y + py * cell_size + 3, chr(65+i), fontsize=10, fontweight='bold')
    
    # Scale
    ax.text(85, 20, 'Scale:\n1 unit = 2 cm', fontsize=9, ha='center')
    
    ax.text(50, 78, f'Question {q_num}: Grid Quadrilateral', ha='center', fontsize=12, fontweight='bold')
    
    filepath = save_fig(fig, f'Q{q_num:02d}_diagram.png')
    
    vrs = create_vrs(
        "Geometry",
        ["Coordinate Geometry", "Area by Shoelace", "Perimeter", "Scale Conversion"],
        "Hard",
        ["Coordinate grid", "Plotted points", "Connected shape", "Scale indicator"],
        ["Read coordinates", "Apply scale factor", "Calculate side lengths", "Find area using grid method"],
        ["Forgetting to apply scale factor", "Counting grid squares incorrectly"]
    )
    
    question_text = f"""Question {q_num}:
The diagram shows quadrilateral ABCD drawn on a grid where each 
unit represents 2 cm.

(a) Write down the coordinates of points A, B, C, and D. [2 marks]

(b) Calculate the actual length of side AB. [2 marks]

(c) Find the area of quadrilateral ABCD in cm2 using the grid method. [3 marks]

(d) Calculate the perimeter of quadrilateral ABCD. [3 marks]
"""
    
    return q_num, question_text, vrs, filepath

def generate_geo3():
    """Geometry 3: 3D Visualization - Cube with Hole"""
    q_num = get_next_q_num()
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 8))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 80)
    ax.axis('off')
    
    # Draw cube as 2D representation (isometric-style)
    # Front face
    front = patches.Rectangle((30, 20), 40, 40, linewidth=2, edgecolor='black', facecolor='lightcyan', alpha=0.3)
    ax.add_patch(front)
    
    # Top face (parallelogram)
    top = Polygon([(30, 60), (40, 70), (80, 70), (70, 60)], fill=True, 
                  facecolor='lightblue', edgecolor='black', linewidth=2, alpha=0.4)
    ax.add_patch(top)
    
    # Side face
    side = Polygon([(70, 60), (80, 70), (80, 30), (70, 20)], fill=True,
                   facecolor='lightsteelblue', edgecolor='black', linewidth=2, alpha=0.4)
    ax.add_patch(side)
    
    # Cylindrical hole (circle on front face)
    hole = Circle((50, 40), 8, fill=False, edgecolor='red', linewidth=2, linestyle='--')
    ax.add_patch(hole)
    ax.text(50, 40, 'Hole', ha='center', va='center', fontsize=9, color='red')
    
    # Dimension labels
    ax.text(50, 15, '8 cm', ha='center', fontsize=10)
    ax.text(25, 40, '8 cm', ha='center', fontsize=10, rotation=90)
    ax.text(85, 50, '8 cm', ha='center', fontsize=10, rotation=90)
    ax.text(50, 5, 'Cylinder diameter: 4 cm', ha='center', fontsize=10, color='red')
    
    ax.text(50, 77, f'Question {q_num}: Cube with Cylindrical Hole', ha='center', fontsize=12, fontweight='bold')
    
    filepath = save_fig(fig, f'Q{q_num:02d}_diagram.png')
    
    vrs = create_vrs(
        "Geometry",
        ["3D Visualization", "Volume", "Surface Area", "Composite Solid"],
        "Hard",
        ["3D cube representation", "Cylindrical hole", "Dimension labels", "Perspective view"],
        ["Calculate cube volume", "Calculate cylinder volume", "Subtract for remaining volume", "Calculate surface area adjustments"],
        ["Forgetting to add inner cylinder surface area", "Using diameter instead of radius"]
    )
    
    question_text = f"""Question {q_num}:
A cube with side 8 cm has a cylindrical hole drilled through its 
center from top to bottom. The cylinder has diameter 4 cm.

(a) Calculate the volume of the cube. [1 mark]

(b) Calculate the volume of the cylindrical hole. [2 marks]

(c) Find the volume of the remaining solid. [2 marks]

(d) Calculate the total surface area of the remaining solid. [5 marks]

(Take pi = 3.14)
"""
    
    return q_num, question_text, vrs, filepath

def generate_geo4():
    """Geometry 4: Angle Chasing in Triangle"""
    q_num = get_next_q_num()
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 8))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 80)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Triangle ABC
    A = (30, 60)
    B = (15, 20)
    C = (75, 20)
    
    triangle = Polygon([A, B, C], fill=False, edgecolor='black', linewidth=2)
    ax.add_patch(triangle)
    
    # Labels
    ax.text(A[0], A[1] + 3, 'A', fontsize=12, fontweight='bold', ha='center')
    ax.text(B[0] - 3, B[1], 'B', fontsize=12, fontweight='bold', ha='center')
    ax.text(C[0] + 3, C[1], 'C', fontsize=12, fontweight='bold', ha='center')
    
    # Angle marks
    # Angle at B
    arc_B = Arc(B, 15, 15, angle=0, theta1=0, theta2=67, color='blue', linewidth=2)
    ax.add_patch(arc_B)
    ax.text(B[0] + 10, B[1] + 5, '52 deg', fontsize=10, color='blue')
    
    # Angle at C
    arc_C = Arc(C, 15, 15, angle=0, theta1=113, theta2=180, color='red', linewidth=2)
    ax.add_patch(arc_C)
    ax.text(C[0] - 10, C[1] + 5, '48 deg', fontsize=10, color='red')
    
    # Angle at A (to find)
    arc_A = Arc(A, 15, 15, angle=0, theta1=247, theta2=293, color='green', linewidth=2)
    ax.add_patch(arc_A)
    ax.text(A[0], A[1] - 10, '?', fontsize=12, color='green', fontweight='bold')
    
    # Side labels
    ax.text(45, 18, '12 cm', fontsize=10, ha='center')
    ax.text(22, 42, '10 cm', fontsize=10, ha='center', rotation=65)
    
    ax.text(50, 75, f'Question {q_num}: Triangle Angles', ha='center', fontsize=12, fontweight='bold')
    
    filepath = save_fig(fig, f'Q{q_num:02d}_diagram.png')
    
    vrs = create_vrs(
        "Geometry",
        ["Angle Sum", "Triangle Properties", "Angle Chasing", "Isosceles Triangle"],
        "Hard",
        ["Triangle shape", "Angle arc marks", "Side labels", "Vertex labels"],
        ["Apply angle sum property", "Calculate unknown angle", "Identify triangle type", "Find remaining angles"],
        ["Assuming triangle is isosceles without proof", "Forgetting angle sum is 180 deg"]
    )
    
    question_text = f"""Question {q_num}:
In triangle ABC, angle ABC = 52 deg and angle ACB = 48 deg. Side AB = 10 cm 
and side BC = 12 cm.

(a) Find angle BAC. [2 marks]

(b) What type of triangle is ABC? Give a reason for your answer. [2 marks]

(c) If D is a point on AC such that BD bisects angle ABC, find 
    angle BDC. [3 marks]

(d) Calculate the area of triangle ABC using the formula 
    Area = 1/2 x base x height. [3 marks]
"""
    
    return q_num, question_text, vrs, filepath

def generate_geo5():
    """Geometry 5: Composite Shape - Trapezium and Semicircle"""
    q_num = get_next_q_num()
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 7))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 70)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Trapezium
    trap_points = [(20, 20), (70, 20), (60, 50), (30, 50)]
    trapezium = Polygon(trap_points, fill=False, edgecolor='black', linewidth=2)
    ax.add_patch(trapezium)
    
    # Semicircle on top
    semicircle = Arc((45, 50), 30, 30, angle=0, theta1=0, theta2=180, color='blue', linewidth=2)
    ax.add_patch(semicircle)
    ax.plot([30, 60], [50, 50], 'b-', linewidth=2)
    
    # Labels
    ax.text(20, 16, 'A', fontsize=11, fontweight='bold')
    ax.text(70, 16, 'B', fontsize=11, fontweight='bold')
    ax.text(60, 54, 'C', fontsize=11, fontweight='bold')
    ax.text(30, 54, 'D', fontsize=11, fontweight='bold')
    
    # Dimensions
    ax.annotate('', xy=(70, 15), xytext=(20, 15),
                arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
    ax.text(45, 11, '50 cm', ha='center', fontsize=10)
    
    ax.annotate('', xy=(65, 50), xytext=(25, 50),
                arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
    ax.text(45, 46, '30 cm', ha='center', fontsize=10)
    
    ax.text(75, 35, 'Height:\n20 cm', fontsize=9, ha='center')
    
    ax.text(50, 67, f'Question {q_num}: Composite Shape', ha='center', fontsize=12, fontweight='bold')
    
    filepath = save_fig(fig, f'Q{q_num:02d}_diagram.png')
    
    vrs = create_vrs(
        "Geometry",
        ["Trapezium Area", "Semicircle Area", "Perimeter", "Composite Shape"],
        "Hard",
        ["Trapezium shape", "Semicircle on top", "Dimension labels", "Vertex labels"],
        ["Calculate trapezium area", "Calculate semicircle area", "Sum for total area", "Calculate perimeter components"],
        ["Using diameter as radius", "Forgetting semicircle is half circle"]
    )
    
    question_text = f"""Question {q_num}:
The diagram shows a composite shape consisting of a trapezium ABCD 
and a semicircle on top of side CD. AB = 50 cm, CD = 30 cm, and 
the height of the trapezium is 20 cm.

(a) Calculate the area of the trapezium. [2 marks]

(b) Calculate the area of the semicircle. [2 marks]

(c) Find the total area of the composite shape. [2 marks]

(d) Calculate the perimeter of the entire shape. [4 marks]

(Take pi = 3.14)
"""
    
    return q_num, question_text, vrs, filepath

def generate_geo6():
    """Geometry 6: Angles in Parallel Lines"""
    q_num = get_next_q_num()
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 7))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 70)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Parallel lines
    ax.plot([10, 90], [50, 50], 'k-', linewidth=2)
    ax.plot([10, 90], [25, 25], 'k-', linewidth=2)
    ax.text(85, 53, 'L1', fontsize=11, fontweight='bold')
    ax.text(85, 20, 'L2', fontsize=11, fontweight='bold')
    
    # Transversal
    ax.plot([25, 75], [10, 65], 'k-', linewidth=2)
    ax.text(78, 63, 'T', fontsize=11, fontweight='bold')
    
    # Intersection points
    ax.plot(40, 50, 'ko', markersize=6)
    ax.plot(52, 25, 'ko', markersize=6)
    
    # Angle marks
    # Angle at top intersection (alternate)
    arc1 = Arc((40, 50), 12, 12, angle=0, theta1=0, theta2=45, color='blue', linewidth=2)
    ax.add_patch(arc1)
    ax.text(48, 54, '65 deg', fontsize=10, color='blue')
    
    # Angle to find at bottom
    arc2 = Arc((52, 25), 12, 12, angle=0, theta1=225, theta2=270, color='red', linewidth=2)
    ax.add_patch(arc2)
    ax.text(44, 21, 'a deg', fontsize=12, color='red', fontweight='bold')
    
    # Another angle
    arc3 = Arc((52, 25), 12, 12, angle=0, theta1=45, theta2=90, color='green', linewidth=2)
    ax.add_patch(arc3)
    ax.text(60, 29, 'b deg', fontsize=12, color='green', fontweight='bold')
    
    ax.text(50, 68, f'Question {q_num}: Parallel Lines', ha='center', fontsize=12, fontweight='bold')
    ax.text(50, 5, 'L1 is parallel to L2. T is a transversal.', ha='center', fontsize=10, style='italic')
    
    filepath = save_fig(fig, f'Q{q_num:02d}_diagram.png')
    
    vrs = create_vrs(
        "Geometry",
        ["Parallel Lines", "Transversal", "Angle Properties", "Angle Relationships"],
        "Hard",
        ["Parallel lines", "Transversal line", "Intersection points", "Angle arc marks"],
        ["Identify angle relationship type", "Apply corresponding/alternate angle properties", "Use angle sum on straight line", "Find unknown angles"],
        ["Confusing corresponding with alternate angles", "Not using properties of parallel lines"]
    )
    
    question_text = f"""Question {q_num}:
In the diagram, line L1 is parallel to line L2. T is a transversal 
that intersects L1 and L2. One angle is marked as 65 deg.

(a) Find the value of angle a, giving a reason for your answer. [2 marks]

(b) Find the value of angle b, giving a reason for your answer. [2 marks]

(c) If another transversal creates an angle of 35 deg with L1 on the 
    opposite side, what is the angle between the two transversals 
    at their intersection point? [3 marks]

(d) Explain why the sum of angles a and b is 180 deg. [3 marks]
"""
    
    return q_num, question_text, vrs, filepath

def generate_geo7():
    """Geometry 7: Sector and Segment"""
    q_num = get_next_q_num()
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 8))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 80)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Sector
    center = (50, 35)
    radius = 25
    
    # Draw sector (90 degree)
    theta = np.linspace(0, np.pi/2, 100)
    x_arc = center[0] + radius * np.cos(theta)
    y_arc = center[1] + radius * np.sin(theta)
    ax.plot(x_arc, y_arc, 'k-', linewidth=2)
    ax.plot([center[0], center[0] + radius], [center[1], center[1]], 'k-', linewidth=2)
    ax.plot([center[0], center[0]], [center[1], center[1] + radius], 'k-', linewidth=2)
    
    # Center and arc point
    ax.plot(center[0], center[1], 'ko', markersize=6)
    ax.text(center[0] - 3, center[1] - 4, 'O', fontsize=11, fontweight='bold')
    
    # Labels on arc
    ax.text(center[0] + radius + 2, center[1], 'A', fontsize=11, fontweight='bold')
    ax.text(center[0], center[1] + radius + 2, 'B', fontsize=11, fontweight='bold')
    
    # Radius label
    ax.annotate('', xy=(center[0] + radius/2, center[1] - 5), xytext=(center[0], center[1] - 5),
                arrowprops=dict(arrowstyle='<->', color='blue', lw=1.5))
    ax.text(center[0] + radius/4, center[1] - 9, '14 cm', fontsize=10, color='blue')
    
    # Right angle mark
    ax.plot([center[0] + 3, center[0] + 3, center[0]], [center[1], center[1] + 3, center[1] + 3], 'k-', linewidth=1.5)
    
    # Angle label
    ax.text(center[0] + 8, center[1] + 8, '90 deg', fontsize=10)
    
    ax.text(50, 75, f'Question {q_num}: Sector Area', ha='center', fontsize=12, fontweight='bold')
    
    filepath = save_fig(fig, f'Q{q_num:02d}_diagram.png')
    
    vrs = create_vrs(
        "Geometry",
        ["Sector Area", "Segment Area", "Arc Length", "Circle Properties"],
        "Hard",
        ["Sector shape", "Radius lines", "Arc curve", "Right angle mark"],
        ["Calculate sector area using angle", "Calculate triangle area", "Subtract for segment area", "Calculate arc length"],
        ["Using wrong angle (degrees vs radians)", "Forgetting segment = sector - triangle"]
    )
    
    question_text = f"""Question {q_num}:
The diagram shows a sector OAB of a circle with center O and radius 
14 cm. Angle AOB = 90 deg.

(a) Calculate the area of sector OAB. [2 marks]

(b) Calculate the area of triangle OAB. [2 marks]

(c) Find the area of the shaded segment (region between arc AB and 
    chord AB). [2 marks]

(d) Calculate the length of arc AB. [2 marks]

(e) Find the perimeter of sector OAB. [2 marks]

(Take pi = 22/7)
"""
    
    return q_num, question_text, vrs, filepath

def generate_geo8():
    """Geometry 8: Rectangular Prism Net"""
    q_num = get_next_q_num()
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 7))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 70)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Draw net of rectangular prism
    # Central rectangle (base)
    base = patches.Rectangle((30, 25), 30, 20, linewidth=2, edgecolor='black', facecolor='lightyellow')
    ax.add_patch(base)
    ax.text(45, 35, 'Base\n10x8', ha='center', va='center', fontsize=9)
    
    # Front face
    front = patches.Rectangle((30, 5), 30, 20, linewidth=2, edgecolor='black', facecolor='lightblue')
    ax.add_patch(front)
    ax.text(45, 15, 'Front\n10x6', ha='center', va='center', fontsize=9)
    
    # Back face
    back = patches.Rectangle((30, 45), 30, 20, linewidth=2, edgecolor='black', facecolor='lightblue')
    ax.add_patch(back)
    ax.text(45, 55, 'Back\n10x6', ha='center', va='center', fontsize=9)
    
    # Left face
    left = patches.Rectangle((5, 25), 25, 20, linewidth=2, edgecolor='black', facecolor='lightgreen')
    ax.add_patch(left)
    ax.text(17, 35, 'Left\n8x6', ha='center', va='center', fontsize=9)
    
    # Right face
    right = patches.Rectangle((60, 25), 25, 20, linewidth=2, edgecolor='black', facecolor='lightgreen')
    ax.add_patch(right)
    ax.text(72, 35, 'Right\n8x6', ha='center', va='center', fontsize=9)
    
    # Top
    top = patches.Rectangle((30, 65), 30, 4, linewidth=2, edgecolor='black', facecolor='lightcoral')
    ax.add_patch(top)
    
    ax.text(50, 3, 'Dimensions: Length = 10 cm, Width = 8 cm, Height = 6 cm', 
            ha='center', fontsize=9, style='italic')
    ax.text(50, 75, f'Question {q_num}: Prism Net', ha='center', fontsize=12, fontweight='bold')
    
    filepath = save_fig(fig, f'Q{q_num:02d}_diagram.png')
    
    vrs = create_vrs(
        "Geometry",
        ["3D Nets", "Surface Area", "Volume", "Rectangular Prism"],
        "Hard",
        ["Net layout", "Face labels", "Dimension annotations", "Fold lines"],
        ["Identify each face dimensions", "Calculate each face area", "Sum for total surface area", "Calculate volume"],
        ["Missing faces in surface area calculation", "Confusing which dimension is which"]
    )
    
    question_text = f"""Question {q_num}:
The diagram shows the net of a rectangular prism with dimensions 
10 cm x 8 cm x 6 cm.

(a) Calculate the surface area of the prism. [3 marks]

(b) Calculate the volume of the prism. [2 marks]

(c) If the prism is made of material with density 2.5 g/cm3, 
    what is its mass? [2 marks]

(d) If the prism is cut in half along its longest dimension, what 
    is the surface area of each half? [3 marks]
"""
    
    return q_num, question_text, vrs, filepath

def generate_geo9():
    """Geometry 9: Quadrilateral Properties"""
    q_num = get_next_q_num()
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 7))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 70)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Parallelogram ABCD
    A = (25, 50)
    B = (65, 50)
    C = (75, 25)
    D = (35, 25)
    
    parallelogram = Polygon([A, B, C, D], fill=False, edgecolor='black', linewidth=2)
    ax.add_patch(parallelogram)
    
    # Diagonals
    ax.plot([A[0], C[0]], [A[1], C[1]], 'k--', linewidth=1)
    ax.plot([B[0], D[0]], [B[1], D[1]], 'k--', linewidth=1)
    
    # Labels
    ax.text(A[0] - 3, A[1] + 2, 'A', fontsize=12, fontweight='bold')
    ax.text(B[0] + 3, B[1] + 2, 'B', fontsize=12, fontweight='bold')
    ax.text(C[0] + 3, C[1] - 3, 'C', fontsize=12, fontweight='bold')
    ax.text(D[0] - 3, D[1] - 3, 'D', fontsize=12, fontweight='bold')
    
    # Intersection
    ax.plot(50, 37.5, 'ro', markersize=6)
    ax.text(53, 40, 'O', fontsize=11, fontweight='bold', color='red')
    
    # Side lengths
    ax.text(45, 53, '12 cm', fontsize=10, ha='center')
    ax.text(78, 38, '8 cm', fontsize=10, ha='center', rotation=-65)
    
    # Angle
    arc_A = Arc(A, 12, 12, angle=0, theta1=270, theta2=315, color='blue', linewidth=2)
    ax.add_patch(arc_A)
    ax.text(A[0] + 5, A[1] - 6, '55 deg', fontsize=10, color='blue')
    
    ax.text(50, 67, f'Question {q_num}: Parallelogram', ha='center', fontsize=12, fontweight='bold')
    
    filepath = save_fig(fig, f'Q{q_num:02d}_diagram.png')
    
    vrs = create_vrs(
        "Geometry",
        ["Parallelogram Properties", "Area", "Diagonals", "Angle Properties"],
        "Hard",
        ["Parallelogram shape", "Diagonals", "Vertex labels", "Angle marks", "Side labels"],
        ["Apply parallelogram properties", "Calculate area using base x height", "Find diagonal properties", "Determine angles"],
        ["Using wrong height (slant instead of perpendicular)", "Confusing properties with other quadrilaterals"]
    )
    
    question_text = f"""Question {q_num}:
ABCD is a parallelogram with AB = 12 cm, BC = 8 cm, and angle DAB = 55 deg. 
The diagonals AC and BD intersect at point O.

(a) Find the length of CD. [1 mark]

(b) Find angle ABC. [2 marks]

(c) Calculate the area of parallelogram ABCD. [3 marks]

(d) Given that the height from D to AB is approximately 6.55 cm, 
    verify your area calculation. [2 marks]

(e) Name one property of the diagonals of a parallelogram. [2 marks]
"""
    
    return q_num, question_text, vrs, filepath

def generate_geo10():
    """Geometry 10: Circle Theorems"""
    q_num = get_next_q_num()
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 8))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 80)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Circle
    circle = Circle((50, 40), 25, fill=False, edgecolor='black', linewidth=2)
    ax.add_patch(circle)
    
    # Center
    ax.plot(50, 40, 'ko', markersize=6)
    ax.text(52, 42, 'O', fontsize=11, fontweight='bold')
    
    # Points on circumference
    points = {
        'A': (50, 65),
        'B': (75, 40),
        'C': (50, 15),
        'D': (30, 55)
    }
    
    for name, (x, y) in points.items():
        ax.plot(x, y, 'bo', markersize=6)
        offset_x = 3 if x > 50 else -3
        offset_y = 3 if y > 40 else -3
        ax.text(x + offset_x, y + offset_y, name, fontsize=11, fontweight='bold')
    
    # Draw angles
    # Angle at center
    ax.plot([50, 50], [40, 65], 'k-', linewidth=1.5)
    ax.plot([50, 75], [40, 40], 'k-', linewidth=1.5)
    arc_center = Arc((50, 40), 12, 12, angle=0, theta1=0, theta2=90, color='red', linewidth=2)
    ax.add_patch(arc_center)
    ax.text(58, 48, '80 deg', fontsize=10, color='red')
    
    # Angle at circumference
    ax.plot([50, 30], [65, 55], 'k-', linewidth=1.5)
    ax.plot([50, 50], [65, 15], 'k-', linewidth=1.5)
    arc_circ = Arc((50, 65), 12, 12, angle=0, theta1=270, theta2=315, color='blue', linewidth=2)
    ax.add_patch(arc_circ)
    ax.text(43, 58, 'x deg', fontsize=11, color='blue', fontweight='bold')
    
    ax.text(50, 77, f'Question {q_num}: Circle Theorem', ha='center', fontsize=12, fontweight='bold')
    
    filepath = save_fig(fig, f'Q{q_num:02d}_diagram.png')
    
    vrs = create_vrs(
        "Geometry",
        ["Circle Theorems", "Angle at Center", "Angle at Circumference", "Arc Properties"],
        "Hard",
        ["Circle", "Center point", "Circumference points", "Angle arcs", "Chord lines"],
        ["Identify angle relationship", "Apply angle at center theorem", "Calculate angle at circumference", "Verify relationship"],
        ["Confusing angle at center with circumference", "Not recognizing same arc subtends both angles"]
    )
    
    question_text = f"""Question {q_num}:
In the diagram, A, B, C, and D are points on the circumference of 
a circle with center O. Angle AOB = 80 deg. AC is a diameter of the circle.

(a) Find angle x (angle ADC), giving a reason for your answer. [3 marks]

(b) Find angle ACB. [2 marks]

(c) Find angle ABC. [2 marks]

(d) If angle CAD = 35 deg, find angle BAD. [3 marks]
"""
    
    return q_num, question_text, vrs, filepath

def generate_geo11():
    """Geometry 11: Similar Triangles"""
    q_num = get_next_q_num()
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 8))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 80)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Two similar triangles (nested)
    # Large triangle
    A = (20, 20)
    B = (80, 20)
    C = (50, 70)
    
    large = Polygon([A, B, C], fill=False, edgecolor='blue', linewidth=2)
    ax.add_patch(large)
    
    # Small triangle (similar, sharing vertex A)
    D = (35, 20)
    E = (50, 45)
    
    small = Polygon([A, D, E], fill=False, edgecolor='red', linewidth=2)
    ax.add_patch(small)
    
    # Labels
    ax.text(A[0] - 4, A[1], 'A', fontsize=12, fontweight='bold')
    ax.text(B[0] + 3, B[1], 'B', fontsize=12, fontweight='bold')
    ax.text(C[0], C[1] + 3, 'C', fontsize=12, fontweight='bold')
    ax.text(D[0], D[1] - 4, 'D', fontsize=11, fontweight='bold', color='red')
    ax.text(E[0] + 3, E[1], 'E', fontsize=11, fontweight='bold', color='red')
    
    # Side labels
    ax.text(50, 16, '12 cm', fontsize=10, ha='center')
    ax.text(27, 32, '8 cm', fontsize=10, ha='center', rotation=65)
    ax.text(27, 16, '5 cm', fontsize=10, ha='center', color='red')
    
    # Parallel indicator
    ax.plot([35, 50], [48, 73], 'k--', linewidth=1, alpha=0.5)
    ax.text(55, 60, 'DE || BC', fontsize=10, style='italic')
    
    ax.text(50, 77, f'Question {q_num}: Similar Triangles', ha='center', fontsize=12, fontweight='bold')
    
    filepath = save_fig(fig, f'Q{q_num:02d}_diagram.png')
    
    vrs = create_vrs(
        "Geometry",
        ["Similar Triangles", "Scale Factor", "Proportion", "Parallel Lines"],
        "Hard",
        ["Two triangles", "Shared vertex", "Parallel indicator", "Side labels"],
        ["Identify similarity criterion", "Find scale factor", "Apply proportion to find unknown sides", "Calculate areas"],
        ["Using wrong ratio (not matching corresponding sides)", "Squaring scale factor for area incorrectly"]
    )
    
    question_text = f"""Question {q_num}:
In triangle ABC, D is a point on AB and E is a point on AC such 
that DE is parallel to BC. AB = 12 cm, AD = 5 cm, and AC = 8 cm.

(a) Show that triangle ADE is similar to triangle ABC. [2 marks]

(b) Find the scale factor of enlargement from triangle ADE to 
    triangle ABC. [2 marks]

(c) Calculate the length of AE. [2 marks]

(d) If the area of triangle ADE is 15 cm2, find the area of 
    triangle ABC. [2 marks]

(e) Find the area of trapezium DECB. [2 marks]
"""
    
    return q_num, question_text, vrs, filepath

def generate_geo12():
    """Geometry 12: Complex Composite with Shaded Region"""
    q_num = get_next_q_num()
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 8))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 80)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Square with quarter circles removed from corners
    square = patches.Rectangle((25, 20), 40, 40, linewidth=2, edgecolor='black', facecolor='lightgray', alpha=0.3)
    ax.add_patch(square)
    
    # Quarter circles at corners (removed/shaded differently)
    # Top-left quarter circle (removed)
    arc1 = Arc((25, 60), 20, 20, angle=0, theta1=0, theta2=90, color='red', linewidth=2)
    ax.add_patch(arc1)
    
    # Top-right quarter circle (removed)
    arc2 = Arc((65, 60), 20, 20, angle=0, theta1=90, theta2=180, color='red', linewidth=2)
    ax.add_patch(arc2)
    
    # Bottom-left quarter circle (removed)
    arc3 = Arc((25, 20), 20, 20, angle=0, theta1=270, theta2=360, color='red', linewidth=2)
    ax.add_patch(arc3)
    
    # Bottom-right quarter circle (removed)
    arc4 = Arc((65, 20), 20, 20, angle=0, theta1=180, theta2=270, color='red', linewidth=2)
    ax.add_patch(arc4)
    
    # Fill the quarter circle regions
    # Use wedge patches for the quarter circles
    wedge1 = Wedge((25, 60), 10, 0, 90, facecolor='white', edgecolor='red', linewidth=2)
    wedge2 = Wedge((65, 60), 10, 90, 180, facecolor='white', edgecolor='red', linewidth=2)
    wedge3 = Wedge((25, 20), 10, 270, 360, facecolor='white', edgecolor='red', linewidth=2)
    wedge4 = Wedge((65, 20), 10, 180, 270, facecolor='white', edgecolor='red', linewidth=2)
    ax.add_patch(wedge1)
    ax.add_patch(wedge2)
    ax.add_patch(wedge3)
    ax.add_patch(wedge4)
    
    # Labels
    ax.text(45, 18, '20 cm', fontsize=10, ha='center')
    ax.text(20, 40, '20 cm', fontsize=10, ha='center', rotation=90)
    ax.text(45, 63, 'Arc radius: 10 cm', fontsize=10, ha='center', color='red')
    
    # Shaded region label
    ax.text(45, 40, 'Shaded\nRegion', ha='center', va='center', fontsize=11, fontweight='bold')
    
    ax.text(50, 77, f'Question {q_num}: Shaded Region', ha='center', fontsize=12, fontweight='bold')
    
    filepath = save_fig(fig, f'Q{q_num:02d}_diagram.png')
    
    vrs = create_vrs(
        "Geometry",
        ["Composite Area", "Square Area", "Quarter Circle", "Subtraction Method"],
        "Hard",
        ["Square shape", "Quarter circle arcs", "Radius labels", "Shaded region"],
        ["Calculate square area", "Calculate total quarter circle area", "Subtract from square", "Find shaded region"],
        ["Calculating full circles instead of quarters", "Not subtracting all four corners"]
    )
    
    question_text = f"""Question {q_num}:
The diagram shows a square of side 20 cm with quarter circles of 
radius 10 cm removed from each corner.

(a) Calculate the area of the square. [1 mark]

(b) Calculate the total area of the four quarter circles. [2 marks]

(c) Find the area of the shaded region. [3 marks]

(d) Find the perimeter of the shaded region. [4 marks]

(Take pi = 3.14)
"""
    
    return q_num, question_text, vrs, filepath

# ==================== DATA INTERPRETATION PROBLEMS (8) ====================

def generate_di1():
    """DI 1: Line Graph with Rate of Change"""
    q_num = get_next_q_num()
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    
    # Data points
    hours = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    temperature = [25, 28, 32, 35, 38, 36, 33, 30, 27]
    
    ax.plot(hours, temperature, 'b-o', linewidth=2, markersize=8)
    ax.fill_between(hours, temperature, alpha=0.2)
    
    # Labels
    ax.set_xlabel('Time (hours after 8:00 a.m.)', fontsize=11)
    ax.set_ylabel('Temperature (deg C)', fontsize=11)
    ax.set_title(f'Question {q_num}: Temperature Change Throughout the Day', fontsize=12, fontweight='bold')
    
    # Grid
    ax.grid(True, alpha=0.3)
    ax.set_xticks(hours)
    ax.set_yticks(range(20, 45, 5))
    
    # Annotations
    ax.annotate('Peak', xy=(4, 38), xytext=(5, 41),
                arrowprops=dict(arrowstyle='->', color='red'),
                fontsize=10, color='red')
    
    filepath = save_fig(fig, f'Q{q_num:02d}_diagram.png')
    
    vrs = create_vrs(
        "Data Interpretation",
        ["Line Graph", "Rate of Change", "Interpolation", "Trend Analysis"],
        "Hard",
        ["Line graph", "Data points", "Axes labels", "Grid lines", "Peak annotation"],
        ["Read values from graph", "Calculate rate of change", "Identify trends", "Interpolate between points"],
        ["Reading wrong scale", "Confusing increasing/decreasing rates"]
    )
    
    question_text = f"""Question {q_num}:
The line graph shows the temperature recorded at hourly intervals 
starting from 8:00 a.m.

(a) What was the temperature at 11:00 a.m.? [1 mark]

(b) Calculate the rate of temperature increase between 9:00 a.m. 
    and 11:00 a.m. [2 marks]

(c) During which 1-hour period was the temperature decrease the 
    greatest? What was the rate of decrease? [2 marks]

(d) Estimate the temperature at 9:30 a.m. [2 marks]

(e) If the pattern continued, predict the temperature at 9:00 a.m. 
    the next day, giving a reason for your answer. [3 marks]
"""
    
    return q_num, question_text, vrs, filepath

def generate_di2():
    """DI 2: Reverse Percentage from Data"""
    q_num = get_next_q_num()
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    
    # Bar chart data
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    sales = [120, 135, 150, 180, 200, 240]
    
    bars = ax.bar(months, sales, color=['lightblue', 'lightgreen', 'lightyellow', 'lightcoral', 'lightpink', 'lightgray'],
                  edgecolor='black', linewidth=1.5)
    
    # Add value labels on bars
    for bar, value in zip(bars, sales):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 5,
                f'${value}k', ha='center', va='bottom', fontsize=10)
    
    ax.set_xlabel('Month', fontsize=11)
    ax.set_ylabel('Sales ($ thousands)', fontsize=11)
    ax.set_title(f'Question {q_num}: Monthly Sales Figures', fontsize=12, fontweight='bold')
    ax.set_ylim(0, 280)
    ax.grid(True, axis='y', alpha=0.3)
    
    filepath = save_fig(fig, f'Q{q_num:02d}_diagram.png')
    
    vrs = create_vrs(
        "Data Interpretation",
        ["Bar Chart", "Percentage Change", "Reverse Percentage", "Trend Analysis"],
        "Hard",
        ["Bar chart", "Month labels", "Value labels", "Y-axis scale", "Grid lines"],
        ["Read bar values", "Calculate percentage changes", "Apply reverse percentage", "Identify trends"],
        ["Using wrong base for percentage", "Confusing increase and decrease percentages"]
    )
    
    question_text = f"""Question {q_num}:
The bar chart shows the monthly sales figures for a company in the 
first half of the year.

(a) What were the sales in March? [1 mark]

(b) Calculate the percentage increase in sales from January to June. [2 marks]

(c) Sales in July were 20% higher than in June. Calculate the sales 
    in July. [2 marks]

(d) Sales in December were $264,000, which was 10% higher than in 
    November. What were the sales in November? [3 marks]

(e) The sales target for the first half of the year was $900,000. 
    Did the company meet its target? Show your working. [2 marks]
"""
    
    return q_num, question_text, vrs, filepath

def generate_di3():
    """DI 3: Cumulative Data"""
    q_num = get_next_q_num()
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    
    # Cumulative frequency data
    marks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    cumulative = [2, 5, 12, 25, 45, 65, 80, 90, 96, 100]
    
    ax.plot(marks, cumulative, 'g-s', linewidth=2, markersize=8)
    ax.fill_between(marks, cumulative, alpha=0.2, color='green')
    
    # Reference lines
    ax.axhline(y=50, color='red', linestyle='--', linewidth=1, alpha=0.7)
    ax.axhline(y=25, color='blue', linestyle='--', linewidth=1, alpha=0.7)
    ax.axhline(y=75, color='orange', linestyle='--', linewidth=1, alpha=0.7)
    
    ax.set_xlabel('Marks (%)', fontsize=11)
    ax.set_ylabel('Cumulative Number of Students', fontsize=11)
    ax.set_title(f'Question {q_num}: Cumulative Frequency of Test Marks', fontsize=12, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 110)
    
    # Legend
    ax.text(5, 52, 'Median', fontsize=9, color='red')
    ax.text(5, 27, 'Q1', fontsize=9, color='blue')
    ax.text(5, 77, 'Q3', fontsize=9, color='orange')
    
    filepath = save_fig(fig, f'Q{q_num:02d}_diagram.png')
    
    vrs = create_vrs(
        "Data Interpretation",
        ["Cumulative Frequency", "Median", "Quartiles", "Percentiles"],
        "Hard",
        ["Cumulative curve", "Grid lines", "Quartile markers", "Axes labels"],
        ["Read cumulative values", "Find median from 50% point", "Find quartiles", "Calculate interquartile range"],
        ["Reading from wrong axis", "Confusing cumulative with actual frequency"]
    )
    
    question_text = f"""Question {q_num}:
The cumulative frequency graph shows the distribution of marks for 
100 students in a mathematics test.

(a) How many students scored 50 marks or less? [1 mark]

(b) Find the median mark. [2 marks]

(c) Find the interquartile range. [3 marks]

(d) If the pass mark is 45, estimate how many students passed. [2 marks]

(e) How many students scored between 60 and 80 marks? [2 marks]
"""
    
    return q_num, question_text, vrs, filepath

def generate_di4():
    """DI 4: Multi-Line Graph Comparison"""
    q_num = get_next_q_num()
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    
    # Data for two products
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    product_a = [50, 55, 60, 58, 65, 70]
    product_b = [40, 48, 55, 65, 72, 80]
    
    ax.plot(months, product_a, 'b-o', linewidth=2, markersize=8, label='Product A')
    ax.plot(months, product_b, 'r-s', linewidth=2, markersize=8, label='Product B')
    
    ax.set_xlabel('Month', fontsize=11)
    ax.set_ylabel('Units Sold (hundreds)', fontsize=11)
    ax.set_title(f'Question {q_num}: Sales Comparison - Two Products', fontsize=12, fontweight='bold')
    ax.legend(loc='upper left', fontsize=10)
    ax.grid(True, alpha=0.3)
    
    # Annotation for intersection
    ax.annotate('Crossover', xy=('Apr', 65), xytext=('Mar', 75),
                arrowprops=dict(arrowstyle='->', color='green'),
                fontsize=10, color='green')
    
    filepath = save_fig(fig, f'Q{q_num:02d}_diagram.png')
    
    vrs = create_vrs(
        "Data Interpretation",
        ["Multi-Line Graph", "Comparison", "Rate of Change", "Trend Analysis"],
        "Hard",
        ["Two line graphs", "Legend", "Data points", "Grid lines", "Trend arrows"],
        ["Read values for each series", "Compare trends", "Calculate rates of change", "Identify crossover points"],
        ["Confusing which line is which", "Not reading values accurately"]
    )
    
    question_text = f"""Question {q_num}:
The line graph shows the sales of two products (A and B) over six 
months.

(a) How many units of Product A were sold in March? [1 mark]

(b) In which month did Product B overtake Product A in sales? [1 mark]

(c) Calculate the percentage increase in sales of Product B from 
    January to June. [2 marks]

(d) For which product was the average monthly sales higher? Show 
    your working. [3 marks]

(e) If the trend continues, predict the sales of Product B in July 
    and explain your reasoning. [3 marks]
"""
    
    return q_num, question_text, vrs, filepath

def generate_di5():
    """DI 5: Pie Chart with Calculations"""
    q_num = get_next_q_num()
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 7))
    
    # Pie chart data
    categories = ['Food', 'Transport', 'Utilities', 'Entertainment', 'Savings', 'Others']
    amounts = [450, 300, 200, 150, 600, 300]
    colors_pie = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc', '#c2c2f0']
    
    wedges, texts, autotexts = ax.pie(amounts, labels=categories, colors=colors_pie, autopct='%1.1f%%',
                                       startangle=90, textprops={'fontsize': 10})
    
    # Make percentage text bold
    for autotext in autotexts:
        autotext.set_fontweight('bold')
    
    ax.set_title(f'Question {q_num}: Monthly Budget Distribution\n(Total: $2000)', fontsize=12, fontweight='bold')
    
    filepath = save_fig(fig, f'Q{q_num:02d}_diagram.png')
    
    vrs = create_vrs(
        "Data Interpretation",
        ["Pie Chart", "Percentage", "Angle Calculation", "Proportion"],
        "Hard",
        ["Pie chart segments", "Category labels", "Percentage labels", "Color coding"],
        ["Read segment values", "Calculate percentages", "Find angles", "Compare proportions"],
        ["Confusing actual values with percentages", "Not using correct total"]
    )
    
    question_text = f"""Question {q_num}:
The pie chart shows how Mr. Lim allocates his monthly salary of $2000.

(a) How much does Mr. Lim spend on food? [1 mark]

(b) What percentage of his salary does Mr. Lim save? [2 marks]

(c) Calculate the angle of the sector representing transport. [2 marks]

(d) If Mr. Lim wants to increase his savings to 40% of his salary 
    while keeping other expenses the same, how much must he reduce 
    his spending on entertainment and others combined? [3 marks]

(e) If Mr. Lim's salary increases by 10% and he maintains the same 