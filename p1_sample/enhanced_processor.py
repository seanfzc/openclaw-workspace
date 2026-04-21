#!/usr/bin/env python3
"""
PROJECT ATOM-SG ENHANCED PROCESSOR
Vision + Dynamic Node ID System
"""

import json
import re
import os
import base64
from pathlib import Path
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass, asdict
from enum import Enum

import pdfplumber
from PIL import Image
import io

# Try to import Anthropic, but allow fallback
try:
    import anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False
    print("Warning: anthropic package not available. Vision analysis will be mocked.")

# ============================================================================
# NODE REGISTRY SYSTEM
# ============================================================================

class NodeType(Enum):
    PRIMARY = "primary"
    SECONDARY = "secondary"

@dataclass
class Node:
    id: str
    name: str
    node_type: NodeType
    description: str
    category: str = ""
    keywords: List[str] = None
    source: str = ""
    created_at: str = ""
    
    def __post_init__(self):
        if self.keywords is None:
            self.keywords = []

class NodeRegistry:
    """Dynamic registry for Primary and Secondary nodes."""
    
    def __init__(self, registry_path: Path):
        self.registry_path = registry_path
        self.nodes: Dict[str, Node] = {}
        self.next_id = {'primary': 1, 'secondary': 1}
        
        # Load existing registry
        if registry_path.exists():
            self.load()
        else:
            self.initialize_from_syllabus()
    
    def initialize_from_syllabus(self):
        """Initialize with P1 math syllabus as primary nodes."""
        from build_syllabus import skills as syllabus_skills
        
        for skill in syllabus_skills:
            node_id = f"P{self.next_id['primary']:03d}"
            self.next_id['primary'] += 1
            
            # Extract keywords from skill name
            skill_text = skill['skill'].lower()
            keywords = list(set(re.findall(r'\b\w+\b', skill_text)))
            keywords = [k for k in keywords if len(k) > 3]
            
            node = Node(
                id=node_id,
                name=skill['skill'],
                node_type=NodeType.PRIMARY,
                description=f"Syllabus skill: {skill['skill']}",
                category=skill['category'],
                keywords=keywords,
                source="MOE P1 Math Syllabus",
                created_at=Path(__file__).parent.name
            )
            self.nodes[node_id] = node
        
        # Add common secondary nodes
        secondary_nodes = [
            ("Reading Comprehension", "Ability to read and understand question text"),
            ("Counting Objects", "Basic counting of discrete items"),
            ("Pattern Recognition", "Identifying sequences and patterns"),
            ("Visual-Spatial Reasoning", "Understanding shapes and spatial relationships"),
            ("Logical Deduction", "Applying logical steps to solve problems"),
            ("Memory Recall", "Remembering number facts or procedures"),
            ("Fine Motor Skills", "Writing numbers or drawing shapes"),
            ("Attention to Detail", "Noticing small differences or changes"),
        ]
        
        for name, desc in secondary_nodes:
            node_id = f"S{self.next_id['secondary']:03d}"
            self.next_id['secondary'] += 1
            
            node = Node(
                id=node_id,
                name=name,
                node_type=NodeType.SECONDARY,
                description=desc,
                category="Cognitive Skill",
                keywords=name.lower().split(),
                source="Project ATOM-SG",
                created_at=Path(__file__).parent.name
            )
            self.nodes[node_id] = node
        
        self.save()
    
    def load(self):
        """Load registry from JSON file."""
        with open(self.registry_path) as f:
            data = json.load(f)
        
        self.nodes.clear()
        for node_data in data['nodes']:
            node = Node(
                id=node_data['id'],
                name=node_data['name'],
                node_type=NodeType(node_data['node_type']),
                description=node_data['description'],
                category=node_data.get('category', ''),
                keywords=node_data.get('keywords', []),
                source=node_data.get('source', ''),
                created_at=node_data.get('created_at', '')
            )
            self.nodes[node.id] = node
            
            # Update next_id counters
            if node.id.startswith('P'):
                num = int(node.id[1:])
                self.next_id['primary'] = max(self.next_id['primary'], num + 1)
            elif node.id.startswith('S'):
                num = int(node.id[1:])
                self.next_id['secondary'] = max(self.next_id['secondary'], num + 1)
    
    def save(self):
        """Save registry to JSON file."""
        data = {
            'nodes': [asdict(node) for node in self.nodes.values()],
            'metadata': {
                'next_primary_id': self.next_id['primary'],
                'next_secondary_id': self.next_id['secondary'],
                'total_nodes': len(self.nodes)
            }
        }
        
        with open(self.registry_path, 'w') as f:
            json.dump(data, f, indent=2)
    
    def find_best_match(self, text: str, node_type: NodeType = None) -> List[Tuple[str, float]]:
        """
        Find best matching nodes for given text.
        Returns list of (node_id, confidence_score) tuples.
        """
        text_lower = text.lower()
        words = set(re.findall(r'\b\w+\b', text_lower))
        
        matches = []
        for node_id, node in self.nodes.items():
            if node_type and node.node_type != node_type:
                continue
            
            # Score based on keyword matches
            keyword_matches = 0
            for keyword in node.keywords:
                if keyword in words:
                    keyword_matches += 1
            
            if keyword_matches > 0:
                score = keyword_matches / max(len(node.keywords), 1)
                matches.append((node_id, score))
        
        # Sort by score descending
        matches.sort(key=lambda x: x[1], reverse=True)
        return matches[:3]  # Top 3 matches
    
    def create_node(self, name: str, node_type: NodeType, description: str, 
                   category: str = "", keywords: List[str] = None) -> str:
        """Dynamically create a new node."""
        if node_type == NodeType.PRIMARY:
            node_id = f"P{self.next_id['primary']:03d}"
            self.next_id['primary'] += 1
        else:
            node_id = f"S{self.next_id['secondary']:03d}"
            self.next_id['secondary'] += 1
        
        if keywords is None:
            keywords = list(set(re.findall(r'\b\w+\b', name.lower())))
            keywords = [k for k in keywords if len(k) > 3]
        
        node = Node(
            id=node_id,
            name=name,
            node_type=node_type,
            description=description,
            category=category,
            keywords=keywords,
            source="Dynamic creation",
            created_at=Path(__file__).parent.name
        )
        
        self.nodes[node_id] = node
        self.save()
        
        return node_id

# ============================================================================
# VISION ANALYSIS WITH CLAUDE
# ============================================================================

class VisionAnalyzer:
    """Analyze PDF images using Claude 3.5 Sonnet."""
    
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.environ.get('CLAUDE_API_KEY')
        self.client = None
        
        if ANTHROPIC_AVAILABLE and self.api_key:
            self.client = anthropic.Anthropic(api_key=self.api_key)
        else:
            print("Warning: Claude API not available. Using mock responses.")
    
    def analyze_question_image(self, image_bytes: bytes, question_text: str, 
                              question_num: str, paper_name: str) -> Dict:
        """
        Send image to Claude for visual type classification.
        """
        if not self.client:
            # Mock response for testing
            return {
                "visual_type": "unknown",
                "role": "Mock analysis - Claude API not configured",
                "confidence": 0.0
            }
        
        # Convert bytes to base64
        image_base64 = base64.b64encode(image_bytes).decode('utf-8')
        
        prompt = f"""You are analyzing Primary 1 math exam questions from Singapore.

IMAGE: Shows question {question_num} from {paper_name}.
QUESTION TEXT: "{question_text}"

CLASSIFY the VISUAL_TYPE from these categories:
- number_bond (ten frames, part-whole diagrams)
- picture_graph (bar charts with pictures, tally charts)
- analog_clock (clock face with hands)
- digital_clock (digital time display)
- shapes (2D/3D geometric shapes)
- money_coins (Singapore coins/notes)
- length_measurement (rulers, comparing lengths)
- counting_objects (objects to count)
- pattern_sequence (repeating patterns)
- other (anything else)

Also describe the visual's ROLE in the question logic (1-2 sentences).
What does the student need to extract from the visual to solve the problem?

Return ONLY valid JSON with this structure:
{{
  "visual_type": "category_name",
  "role": "description of visual's role",
  "confidence": 0.95
}}"""
        
        try:
            message = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=300,
                messages=[{
                    "role": "user",
                    "content": [
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": "image/png",
                                "data": image_base64
                            }
                        },
                        {
                            "type": "text",
                            "text": prompt
                        }
                    ]
                }]
            )
            
            # Extract JSON from response
            response_text = message.content[0].text
            json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
            
            if json_match:
                return json.loads(json_match.group())
            else:
                return {
                    "visual_type": "unknown",
                    "role": "Could not parse Claude response",
                    "confidence": 0.0
                }
                
        except Exception as e:
            print(f"Claude API error: {e}")
            return {
                "visual_type": "error",
                "role": f"API error: {str(e)[:100]}",
                "confidence": 0.0
            }

# ============================================================================
# QUESTION PROCESSOR
# ============================================================================

@dataclass
class ExtractedQuestion:
    question_number: str
    text: str
    page: int
    image_bytes: Optional[bytes] = None
    options: List[Dict] = None
    
    def __post_init__(self):
        if self.options is None:
            self.options = []

class QuestionProcessor:
    """Process PDFs and extract questions with vision analysis."""
    
    def __init__(self, node_registry: NodeRegistry, vision_analyzer: VisionAnalyzer):
        self.registry = node_registry
        self.vision = vision_analyzer
    
    def extract_questions_from_pdf(self, pdf_path: Path) -> List[ExtractedQuestion]:
        """Extract questions from PDF, including images."""
        questions = []
        
        with pdfplumber.open(pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages, 1):
                # Extract text
                text = page.extract_text()
                if not text:
                    continue
                
                # Extract images from page
                images = page.images
                page_image = page.to_image(resolution=150)
                image_bytes = None
                
                if page_image:
                    # Convert to bytes
                    img_buffer = io.BytesIO()
                    page_image.save(img_buffer, format='PNG')
                    image_bytes = img_buffer.getvalue()
                
                # Simple question extraction (improve this)
                lines = text.split('\n')
                current_q = None
                current_text = []
                
                for line in lines:
                    line = line.strip()
                    if not line:
                        continue
                    
                    # Check for question number
                    match = re.match(r'^(?:Q)?(\d+)[\.\)]\s*(.*)', line)
                    if match:
                        if current_q is not None:
                            questions.append(ExtractedQuestion(
                                question_number=current_q,
                                text=' '.join(current_text).strip(),
                                page=page_num,
                                image_bytes=image_bytes
                            ))
                        
                        current_q = match.group(1)
                        current_text = [match.group(2)] if match.group(2) else []
                    else:
                        if current_q is not None:
                            current_text.append(line)
                
                # Add last question
                if current_q is not None:
                    questions.append(ExtractedQuestion(
                        question_number=current_q,
                        text=' '.join(current_text).strip(),
                        page=page_num,
                        image_bytes=image_bytes
                    ))
        
        return questions
    
    def process_question(self, question: ExtractedQuestion, pdf_name: str) -> Dict:
        """Process a single question with node mapping and vision analysis."""
        # 1. Find primary node (core concept)
        primary_matches = self.registry.find_best_match(
            question.text, node_type=NodeType.PRIMARY
        )
        primary_node = primary_matches[0][0] if primary_matches else None
        
        # 2. Find secondary nodes (supporting skills)
        secondary_matches = self.registry.find_best_match(
            question.text, node_type=NodeType.SECONDARY
        )
        secondary_nodes = [match[0] for match in secondary_matches[:2]]  # Top 2
        
        # 3. Vision analysis if image available
        visual_analysis = {"visual_type": "unknown", "role": "", "confidence": 0.0}
        if question.image_bytes:
            visual_analysis = self.vision.analyze_question_image(
                question.image_bytes,
                question.text,
                question.question_number,
                pdf_name
            )
        
        # 4. Extract context variables (nouns from question)
        nouns = re.findall(r'\b([A-Z][a-z]+)\b', question.text)  # Capitalized words
        context_vars = list(set(nouns))[:5]  # Unique, limit 5
        
        # 5. Build result
        return {
            'question_number': question.question_number,
            'text': question.text,
            'page': question.page,
            'primary_node': primary_node or "[Nano-Node ID]",
            'secondary_nodes': secondary_nodes or ["[Dependency Node ID]"],
            'visual_type': visual_analysis['visual_type'],
            'visual_role': visual_analysis['role'],
            'context_variables': context_vars,
            'syllabus_matches': [match[0] for match in primary_matches[:3]]
        }

# ============================================================================
# MAIN PIPELINE
# ============================================================================

def main():
    """Enhanced processing pipeline with vision and dynamic nodes."""
    print("=== PROJECT ATOM-SG ENHANCED PROCESSOR ===")
    
    # Configuration
    EXAM_PAPERS_ROOT = Path('/Users/zcaeth/Desktop/sg_exam_papers/Maths/P1')
    OUTPUT_DIR = Path('/Users/zcaeth/.openclaw/workspace/second-brain-simple/raw/exam-questions')
    REGISTRY_PATH = Path('/Users/zcaeth/.openclaw/workspace/p1_sample/node_registry.json')
    
    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Initialize systems
    print("1. Initializing Node Registry...")
    registry = NodeRegistry(REGISTRY_PATH)
    print(f"   Loaded {len(registry.nodes)} nodes ({registry.next_id['primary']-1} primary, {registry.next_id['secondary']-1} secondary)")
    
    print("2. Initializing Vision Analyzer...")
    api_key = os.environ.get('CLAUDE_API_KEY')
    if not api_key:
        print("   WARNING: CLAUDE_API_KEY environment variable not set.")
        print("   Set it with: export CLAUDE_API_KEY='your_key_here'")
        print("   Using mock vision analysis for now.")
    
    vision = VisionAnalyzer(api_key)
    processor = QuestionProcessor(registry, vision)
    
    # Find PDFs
    print("3. Finding PDF files...")
    pdf_files = []
    for year in ['2020', '2021', '2022', '2023', '2024', '2025']:
        year_path = EXAM_PAPERS_ROOT / year
        if year_path.exists():
            for pdf in year_path.rglob('*.pdf'):
                pdf_files.append(pdf)
    
    print(f"   Found {len(pdf_files)} PDF files")
    
    if not pdf_files:
        print("No PDF files found. Exiting.")
        return
    
    # Process first few PDFs for testing
    print("\n4. Processing PDFs (sample mode)...")
    total_questions = 0
    sample_limit = 10
    
    for pdf_path in pdf_files[:5]:  # First 5 PDFs
        print(f"\n   Processing: {pdf_path.name}")
        
        try:
            # Extract questions
            questions = processor.extract_questions_from_pdf(pdf_path)
            print(f"   Found {len(questions)} potential questions")
            
            for q in questions[:5]:  # First 5 questions per PDF
                # Process with vision and nodes
                result = processor.process_question(q, pdf_path.stem)
                
                # Generate markdown
                content = generate_markdown(result, pdf_path.stem, registry)
                
                # Save file
                filename = f"{pdf_path.stem}_Q{q.question_number}.md"
                filepath = OUTPUT_DIR / filename
                filepath.write_text(content)
                
                total_questions += 1
                print(f"     ✓ Question {q.question_number}: {result['primary_node']} | {result['visual_type']}")
                
                if total_questions >= sample_limit:
                    print(f"\n   Re