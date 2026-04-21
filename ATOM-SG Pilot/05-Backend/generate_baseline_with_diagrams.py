#!/usr/bin/env python3
"""
Generate complete baseline test PDF with embedded diagrams.
Uses existing rendered SVG/PNG diagrams from artifacts/renders/
"""

from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import inch, cm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, Frame
from datetime import datetime
import re

# Setup paths
BASE_DIR = Path(__file__).parent
RENDERS_DIR = BASE_DIR / "artifacts" / "renders"
OUTPUT_DIR = BASE_DIR / "artifacts" / "renders"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# All 25 geometry problems from G001-G025 with diagram references
GEOMETRY_PROBLEMS = [
    {
        "id": "G001",
        "question": "In the diagram, measure ∠AOB, ∠BOC, and ∠COD using a protractor. Write your answers in the boxes provided.",
        "subpathway": "G1: Identify and measure angles using a protractor",
        "difficulty": "A",
        "marks": 3,
        "diagram": "G001-angle-diagram-v1.svg",
        "answer_format": "∠AOB = _____°, ∠BOC = _____°, ∠COD = _____°"
    },
    {
        "id": "G002",
        "question": "In the diagram, AOB is a straight line. If ∠AOC = 75°, find ∠COB.",
        "subpathway": "G1: Use angle properties (angles on straight line = 180°)",
        "difficulty": "B",
        "marks": 2,
        "diagram": "G002-angle-diagram-v1.svg",
        "answer_format": "∠COB = _____°"
    },
    {
        "id": "G003",
        "question": "Three angles meet at point O. Given ∠AOB = 120° and ∠BOC = 85°, find ∠AOC.",
        "subpathway": "G1: Use angle properties (angles at a point = 360°)",
        "difficulty": "B",
        "marks": 2,
        "diagram": "G003-angle-diagram-v1.svg",
        "answer_format": "∠AOC = _____°"
    },
    {
        "id": "G004",
        "question": "In the diagram, two straight lines AB and CD intersect at O. If ∠AOC = 40°, find ∠AOD, ∠BOD, and ∠BOC.",
        "subpathway": "G1: Use angle properties (vertically opposite angles)",
        "difficulty": "B",
        "marks": 3,
        "diagram": "G004-angle-diagram-v1.svg",
        "answer_format": "∠AOD = _____°, ∠BOD = _____°, ∠BOC = _____°"
    },
    {
        "id": "G005",
        "question": "In triangle ABC, ∠A = 50° and ∠B = 70°. Find ∠C.",
        "subpathway": "G1: Apply angle sum of triangle (180°)",
        "difficulty": "C",
        "marks": 2,
        "diagram": "G005-triangle-v1.svg",
        "answer_format": "∠C = _____°"
    },
    {
        "id": "G006",
        "question": "In the diagram, identify and label all pairs of perpendicular lines and parallel lines using the symbols ⊥ and ∥.",
        "subpathway": "G1: Identify perpendicular and parallel lines",
        "difficulty": "A",
        "marks": 2,
        "diagram": "G006-parallel-perpendicular-v1.svg",
        "answer_format": "Perpendicular: _____, Parallel: _____"
    },
    {
        "id": "G007",
        "question": "In the diagram, AOB is a straight line. ∠BOD = 90° (right angle). If ∠AOC = 110°, find ∠COD.",
        "subpathway": "G1: Combined angle properties (multi-step)",
        "difficulty": "D",
        "marks": 3,
        "diagram": "G007-angle-diagram-v1.svg",
        "answer_format": "∠COD = _____°"
    },
    {
        "id": "G008",
        "question": "Measure the reflex angle ∠XOY in the diagram (the angle greater than 180°).",
        "subpathway": "G1: Measure reflex angles",
        "difficulty": "C",
        "marks": 2,
        "diagram": "G008-angle-diagram-v1.svg",
        "answer_format": "∠XOY = _____°"
    },
    {
        "id": "G009",
        "question": "Find the perimeter of rectangle ABCD with length 8 cm and breadth 5 cm.",
        "subpathway": "G2: Calculate perimeter of rectangles",
        "difficulty": "A",
        "marks": 2,
        "diagram": "G009-rectangle-v1.svg",
        "answer_format": "Perimeter = _____ cm"
    },
    {
        "id": "G010",
        "question": "The figure shows a composite shape made of two rectangles. Find its perimeter.",
        "subpathway": "G2: Calculate perimeter of composite rectilinear figures",
        "difficulty": "B",
        "marks": 3,
        "diagram": "G010-composite-shape-v1.svg",
        "answer_format": "Perimeter = _____ cm"
    },
    {
        "id": "G011",
        "question": "Find the area of the L-shaped figure shown. All dimensions are in centimetres.",
        "subpathway": "G2: Calculate area of composite rectangular figures",
        "difficulty": "B",
        "marks": 3,
        "diagram": "G011-lshape-area-v1.svg",
        "answer_format": "Area = _____ cm²"
    },
    {
        "id": "G012",
        "question": "A rectangular sheet measures 12 cm by 8 cm. A 3 cm by 3 cm square is cut from one corner. Find the remaining area.",
        "subpathway": "G2: Calculate area with missing sections",
        "difficulty": "C",
        "marks": 3,
        "diagram": "G012-cutout-rectangle-v1.svg",
        "answer_format": "Remaining area = _____ cm²"
    },
    {
        "id": "G013",
        "question": "Convert: (a) 3.5 m = _____ cm, (b) 250 cm = _____ m, (c) 4.2 km = _____ m",
        "subpathway": "G2: Convert between units of length",
        "difficulty": "A",
        "marks": 3,
        "diagram": None,
        "answer_format": "(a) _____, (b) _____, (c) _____"
    },
    {
        "id": "G014",
        "question": "Convert 2.5 m² to cm².",
        "subpathway": "G2: Convert between units of area",
        "difficulty": "B",
        "marks": 2,
        "diagram": None,
        "answer_format": "2.5 m² = _____ cm²"
    },
    {
        "id": "G015",
        "question": "Draw all lines of symmetry on the regular hexagon shown.",
        "subpathway": "G4: Identify lines of symmetry",
        "difficulty": "A",
        "marks": 2,
        "diagram": "G015-hexagon-symmetry-v1.svg",
        "answer_format": "Number of lines = _____"
    },
    {
        "id": "G016",
        "question": "The figure shows half of a symmetrical shape with the mirror line (dotted). Complete the symmetrical figure.",
        "subpathway": "G4: Complete symmetrical figures",
        "difficulty": "C",
        "marks": 3,
        "diagram": "G016-symmetry-complete-v1.svg",
        "answer_format": "(Complete the drawing on the diagram)"
    },
    {
        "id": "G017",
        "question": "Find the volume of the cuboid with length 6 cm, breadth 4 cm, and height 3 cm.",
        "subpathway": "G3: Calculate volume of cuboids",
        "difficulty": "A",
        "marks": 2,
        "diagram": "G017-cuboid-v1.svg",
        "answer_format": "Volume = _____ cm³"
    },
    {
        "id": "G018",
        "question": "Find the volume of a box with dimensions 0.5 m × 30 cm × 200 mm. Give your answer in cm³.",
        "subpathway": "G3: Calculate volume with unit conversion",
        "difficulty": "B",
        "marks": 3,
        "diagram": "G018-cuboid-v1.svg",
        "answer_format": "Volume = _____ cm³"
    },
    {
        "id": "G019",
        "question": "Which of the following nets can be folded to form a cube? Circle the correct answer(s).",
        "subpathway": "G3: Identify valid nets of cubes",
        "difficulty": "C",
        "marks": 2,
        "diagram": "G019-cube-nets-v1.svg",
        "answer_format": "Valid net(s): _____"
    },
    {
        "id": "G020",
        "question": "Draw a net of the cuboid shown on the grid. The dimensions are 4 cm × 2 cm × 1 cm.",
        "subpathway": "G3: Draw nets of cuboids",
        "difficulty": "D",
        "marks": 4,
        "diagram": "G020-cuboid-net-v1.svg",
        "answer_format": "(Draw on the grid provided)"
    },
    {
        "id": "G021",
        "question": "Classify the triangle with side lengths 5 cm, 5 cm, and 5 cm.",
        "subpathway": "G4: Classify triangles by sides",
        "difficulty": "A",
        "marks": 1,
        "diagram": "G021-triangle-classification-v1.svg",
        "answer_format": "Type: _____ triangle"
    },
    {
        "id": "G022",
        "question": "Classify the triangle with angles 45°, 45°, and 90°.",
        "subpathway": "G4: Classify triangles by angles",
        "difficulty": "A",
        "marks": 1,
        "diagram": "G022-triangle-angles-v1.svg",
        "answer_format": "Type: _____ triangle"
    },
    {
        "id": "G023",
        "question": "Identify the quadrilateral: It has two pairs of parallel sides, all sides equal, but angles are not 90°.",
        "subpathway": "G4: Classify quadrilaterals",
        "difficulty": "B",
        "marks": 2,
        "diagram": "G023-quadrilateral-v1.svg",
        "answer_format": "Quadrilateral: _____"
    },
    {
        "id": "G024",
        "question": "A circle has radius 7 cm. Find its circumference. (Take π = 22/7)",
        "subpathway": "G2: Calculate circumference of circle",
        "difficulty": "C",
        "marks": 2,
        "diagram": "G024-circle-v1.svg",
        "answer_format": "Circumference = _____ cm"
    },
    {
        "id": "G025",
        "question": "The pie chart shows how a student spends 24 hours in a day. If the 'Sleep' sector has angle 90°, what fraction of the day is spent sleeping?",
        "subpathway": "G2: Interpret pie charts as fractions",
        "difficulty": "D",
        "marks": 3,
        "diagram": "G025-pie-chart-v1.svg",
        "answer_format": "Fraction = _____"
    }
]


def draw_wrapped_text(c, text, x, y, max_width, line_height=0.2*inch, font_name="Helvetica", font_size=10):
    """Draw text with word wrapping and return new y position."""
    c.setFont(font_name, font_size)
    words = text.split()
    lines = []
    current_line = []
    
    for word in words:
        test_line = ' '.join(current_line + [word])
        if c.stringWidth(test_line, font_name, font_size) <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(' '.join(current_line))
            current_line = [word]
    if current_line:
        lines.append(' '.join(current_line))
    
    for line in lines:
        c.drawString(x, y, line)
        y -= line_height
    return y


def embed_diagram(c, diagram_filename, x, y, max_width=3*inch, max_height=2*inch):
    """Embed a diagram image (SVG, PNG, or PDF) into the PDF."""
    if not diagram_filename:
        return y
    
    # Try different extensions
    for ext in ['.svg', '.png', '.pdf']:
        diagram_path = RENDERS_DIR / (diagram_filename.replace('.svg', '').replace('.png', '').replace('.pdf', '') + ext)
        if diagram_path.exists():
            try:
                # For PNG/PDF, use drawImage
                if ext in ['.png', '.pdf']:
                    # Get aspect ratio
                    from PIL import Image
                    with Image.open(diagram_path) as img:
                        img_width, img_height = img.size
                        aspect = img_height / img_width
                        
                        # Scale to fit
                        if img_width > max_width:
                            draw_width = max_width
                            draw_height = max_width * aspect
                        else:
                            draw_width = img_width
                            draw_height = img_height
                        
                        if draw_height > max_height:
                            draw_height = max_height
                            draw_width = max_height / aspect
                    
                    c.drawImage(str(diagram_path), x, y - draw_height, width=draw_width, height=draw_height)
                    return y - draw_height - 0.1*inch
                    
                # For SVG, try to find PNG version
                elif ext == '.svg':
                    png_path = diagram_path.with_suffix('.png')
                    pdf_path = diagram_path.with_suffix('.pdf')
                    if png_path.exists():
                        # Direct PNG embedding without recursion
                        try:
                            from PIL import Image
                            with Image.open(png_path) as img:
                                img_width, img_height = img.size
                                aspect = img_height / img_width
                                
                                if img_width > max_width:
                                    draw_width = max_width
                                    draw_height = max_width * aspect
                                else:
                                    draw_width = img_width
                                    draw_height = img_height
                                
                                if draw_height > max_height:
                                    draw_height = max_height
                                    draw_width = max_height / aspect
                            
                            c.drawImage(str(png_path), x, y - draw_height, width=draw_width, height=draw_height)
                            return y - draw_height - 0.1*inch
                        except Exception as e2:
                            print(f"Warning: Could not embed PNG {png_path}: {e2}")
                    elif pdf_path.exists():
                        # Use PDF if PNG not available
                        try:
                            c.drawImage(str(pdf_path), x, y - max_height, width=max_width, height=max_height)
                            return y - max_height - 0.1*inch
                        except Exception as e2:
                            print(f"Warning: Could not embed PDF {pdf_path}: {e2}")
                    
                    # Fallback: show placeholder
                    c.setFont("Helvetica-Oblique", 8)
                    c.setFillColorRGB(0.5, 0.5, 0.5)
                    c.drawString(x, y - 0.2*inch, f"[Diagram: {diagram_filename}]")
                    c.setFillColorRGB(0, 0, 0)
                    return y - 0.3*inch
                        
            except Exception as e:
                print(f"Warning: Could not embed {diagram_path}: {e}")
                c.setFont("Helvetica-Oblique", 8)
                c.setFillColorRGB(0.8, 0.2, 0.2)
                c.drawString(x, y - 0.2*inch, f"[Diagram missing: {diagram_filename}]")
                c.setFillColorRGB(0, 0, 0)
                return y - 0.3*inch
    
    # Diagram not found
    c.setFont("Helvetica-Oblique", 8)
    c.setFillColorRGB(0.8, 0.2, 0.2)
    c.drawString(x, y - 0.2*inch, f"[Diagram not found: {diagram_filename}]")
    c.setFillColorRGB(0, 0, 0)
    return y - 0.3*inch


def generate_baseline_pdf_with_diagrams(output_path: Path = None) -> Path:
    """Generate baseline test PDF with embedded diagrams."""
    
    if output_path is None:
        output_path = OUTPUT_DIR / "ATOM-SG_Baseline_Test_25_Questions_WITH_DIAGRAMS.pdf"
    
    c = canvas.Canvas(str(output_path), pagesize=letter)
    width, height = letter
    
    # Margins
    left_margin = 0.6 * inch
    right_margin = 0.6 * inch
    top_margin = 0.6 * inch
    bottom_margin = 0.6 * inch
    content_width = width - left_margin - right_margin
    
    def draw_header():
        """Draw the test header."""
        c.setFont("Helvetica-Bold", 16)
        c.drawCentredString(width/2, height - top_margin, "ATOM-SG Baseline Assessment Test")
        
        c.setFont("Helvetica", 11)
        c.drawCentredString(width/2, height - top_margin - 0.25*inch, 
                           "Primary 6 Mathematics — Geometry Track (25 Questions)")
        
        # Student info box
        c.setFont("Helvetica-Bold", 10)
        y_info = height - top_margin - 0.6*inch
        c.drawString(left_margin, y_info, "Name: _________________________________")
        c.drawString(left_margin + 3.2*inch, y_info, "Class: _______")
        c.drawString(left_margin + 4.5*inch, y_info, "Date: ___________")
        
        # Instructions
        c.setFont("Helvetica-Bold", 10)
        y_inst = height - top_margin - 0.95*inch
        c.drawString(left_margin, y_inst, "Instructions:")
        c.setFont("Helvetica", 9)
        instructions = [
            "• This test contains 25 geometry questions. Time allowed: 45 minutes.",
            "• Show all your working in the spaces provided. Marks may be awarded for correct method.",
            "• Write your final answers clearly in the boxes provided.",
            "• Calculators are NOT allowed unless specified.",
            "• Diagrams are NOT drawn to scale unless stated otherwise."
        ]
        y = y_inst - 0.18*inch
        for instruction in instructions:
            c.drawString(left_margin + 0.1*inch, y, instruction)
            y -= 0.16*inch
        
        return y - 0.15*inch  # Return starting y for questions
    
    def draw_question(c, q_num, problem, y_start):
        """Draw a single question with diagram and working space."""
        y = y_start
        
        # Check if we need a new page
        min_space = 2.5 * inch if problem.get("diagram") else 1.5 * inch
        if y < bottom_margin + min_space:
            c.showPage()
            y = height - top_margin - 0.3*inch
            c.setFont("Helvetica-Bold", 11)
            c.drawCentredString(width/2, y, "Baseline Assessment Test — Continued")
            y -= 0.35*inch
        
        # Question number and difficulty
        c.setFont("Helvetica-Bold", 10)
        c.drawString(left_margin, y, f"Q{q_num:2d}. [{problem['difficulty']}] ")
        
        # Question text (wrapped)
        question_x = left_margin + 0.55*inch
        c.setFont("Helvetica", 10)
        y = draw_wrapped_text(c, problem['question'], question_x, y, 
                             max_width=content_width - 0.6*inch, 
                             line_height=0.16*inch, font_size=10)
        
        # Subpathway (smaller, lighter)
        y -= 0.04*inch
        c.setFont("Helvetica-Oblique", 7)
        c.setFillColorRGB(0.4, 0.4, 0.4)
        y = draw_wrapped_text(c, f"({problem['subpathway']})", 
                             question_x + 0.05*inch, y, 
                             max_width=content_width - 0.7*inch, 
                             line_height=0.13*inch, font_size=7)
        c.setFillColorRGB(0, 0, 0)
        
        # Embed diagram if available
        if problem.get("diagram"):
            y -= 0.08*inch
            diagram_y = y
            y = embed_diagram(c, problem["diagram"], 
                            left_margin + 0.3*inch, diagram_y, 
                            max_width=content_width - 0.6*inch, 
                            max_height=1.8*inch)
        
        # Working space label
        y -= 0.12*inch
        c.setFont("Helvetica-Bold", 8)
        c.drawString(question_x, y, "Working:")
        
        # Working space box
        y -= 0.14*inch
        working_height = 0.55*inch
        c.rect(question_x, y - working_height, content_width - 0.65*inch, working_height)
        
        # Answer box
        y -= working_height + 0.12*inch
        c.setFont("Helvetica-Bold", 9)
        c.drawString(question_x, y, "Answer: ")
        c.setFont("Helvetica", 10)
        answer_text = problem['answer_format']
        c.drawString(question_x + 0.55*inch, y, answer_text)
        
        # Marks
        c.setFont("Helvetica-Bold", 8)
        marks_x = width - right_margin - 0.6*inch
        c.drawString(marks_x, y, f"({problem['marks']}m)")
        
        # Separator line
        y -= 0.22*inch
        c.setStrokeColorRGB(0.7, 0.7, 0.7)
        c.line(left_margin, y, width - right_margin, y)
        c.setStrokeColorRGB(0, 0, 0)
        
        return y - 0.08*inch
    
    # Page 1: Header + Questions 1-8
    y = draw_header()
    
    for i, problem in enumerate(GEOMETRY_PROBLEMS[:8], 1):
        y = draw_question(c, i, problem, y)
    
    # Page 2: Questions 9-17
    c.showPage()
    y = height - top_margin - 0.2*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(width/2, y, "Baseline Assessment Test — Page 2")
    y -= 0.35*inch
    
    for i, problem in enumerate(GEOMETRY_PROBLEMS[8:17], 9):
        y = draw_question(c, i, problem, y)
    
    # Page 3: Questions 18-25
    c.showPage()
    y = height - top_margin - 0.2*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(width/2, y, "Baseline Assessment Test — Page 3")
    y -= 0.35*inch
    
    for i, problem in enumerate(GEOMETRY_PROBLEMS[17:25], 18):
        y = draw_question(c, i, problem, y)
    
    # Answer key page
    c.showPage()
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(width/2, height - top_margin, "Answer Key — For Markers Only")
    
    c.setFont("Helvetica", 9)
    c.drawCentredString(width/2, height - top_margin - 0.25*inch, 
                       "DO NOT DISTRIBUTE TO STUDENTS")
    
    y = height - top_margin - 0.6*inch
    c.setFont("Helvetica-Bold", 9)
    c.drawString(left_margin, y, "Q#  |  Answer  |  Subpathway  |  Marks")
    c.line(left_margin, y - 0.08*inch, width - right_margin, y - 0.08*inch)
    
    y -= 0.2*inch
    c.setFont("Courier", 8)
    
    for i, problem in enumerate(GEOMETRY_PROBLEMS, 1):
        answer_short = problem['answer_format'][:35] + "..." if len(problem['answer_format']) > 35 else problem['answer_format']
        pathway_short = problem['subpathway'][:25] + "..." if len(problem['subpathway']) > 25 else problem['subpathway']
        c.drawString(left_margin, y, f"Q{i:2d} | {answer_short:37} | {pathway_short:28} | {problem['marks']}m")
        y -= 0.14*inch
        
        if y < bottom_margin + 0.3*inch and i < 25:
            c.showPage()
            y = height - top_margin - 0.3*inch
    
    # Footer on all pages
    c.setFont("Helvetica-Oblique", 7)
    c.setFillColorRGB(0.4, 0.4, 0.4)
    c.drawCentredString(width/2, bottom_margin - 0.15*inch, 
                       f"ATOM-SG Pilot MVP • Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    c.setFillColorRGB(0, 0, 0)
    
    c.save()
    
    # Summary
    total_marks = sum(p['marks'] for p in GEOMETRY_PROBLEMS)
    diagrams_count = sum(1 for p in GEOMETRY_PROBLEMS if p.get('diagram'))
    
    print(f"\n{'='*60}")
    print("BASELINE TEST PDF WITH DIAGRAMS - GENERATION COMPLETE")
    print(f"{'='*60}")
    print(f"Output: {output_path}")
    print(f"Total questions: 25")
    print(f"Total marks: {total_marks}")
    print(f"Questions with diagrams: {diagrams_count}/25")
    print(f"Difficulty distribution:")
    print(f"  A (Easy): {sum(1 for p in GEOMETRY_PROBLEMS if p['difficulty']=='A')}")
    print(f"  B (Medium): {sum(1 for p in GEOMETRY_PROBLEMS if p['difficulty']=='B')}")
    print(f"  C (Hard): {sum(1 for p in GEOMETRY_PROBLEMS if p['difficulty']=='C')}")
    print(f"  D (Challenge): {sum(1 for p in GEOMETRY_PROBLEMS if p['difficulty']=='D')}")
    print(f"{'='*60}\n")
    
    return output_path


if __name__ == "__main__":
    output = generate_baseline_pdf_with_diagrams()
    print(f"✅ PDF ready at: {output}")