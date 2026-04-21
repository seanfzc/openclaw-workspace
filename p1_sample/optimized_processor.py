#!/usr/bin/env python3
"""
PROJECT ATOM-SG OPTIMIZED PROCESSOR
Cost-optimized with hybrid vision + answer key extraction
"""

import json
import re
import os
import base64
import hashlib
from pathlib import Path
from typing import List, Dict, Optional, Tuple, Set
from dataclasses import dataclass, asdict
from enum import Enum
from collections import defaultdict

import pdfplumber
from PIL import Image
import io
import anthropic

# ============================================================================
# COST OPTIMIZATION: HEURISTIC VISUAL DETECTION
# ============================================================================

class HeuristicVisualDetector:
    """Free visual type detection using text and image metadata."""
    
    @staticmethod
    def detect_from_text(question_text: str) -> Tuple[str, float]:
        """Detect visual type from question text alone."""
        text_lower = question_text.lower()
        
        # Keyword mapping with confidence scores
        keyword_map = {
            'number_bond': ['number bond', 'ten frame', 'part whole', 'bond'],
            'picture_graph': ['picture graph', 'graph', 'chart', 'bar', 'tally'],
            'analog_clock': ['clock', 'time', 'analog', 'o\'clock', 'half past', 'minute'],
            'digital_clock': ['digital', ':', 'pm', 'am'],
            'shapes': ['shape', 'circle', 'square', 'triangle', 'rectangle', 'cube'],
            'money_coins': ['coin', 'dollar', 'cent', 'money', 'currency', 'note'],
            'length_measurement': ['longer', 'shorter', 'measure', 'cm', 'centimeter', 'ruler'],
            'counting_objects': ['count', 'how many', 'objects', 'pencils', 'sweets'],
            'pattern_sequence': ['pattern', 'next', 'sequence', 'repeat']
        }
        
        scores = {}
        for vtype, keywords in keyword_map.items():
            matches = sum(1 for kw in keywords if kw in text_lower)
            if matches > 0:
                scores[vtype] = min(0.3 + (matches * 0.1), 0.7)  # Max 0.7 confidence
        
        if scores:
            best = max(scores.items(), key=lambda x: x[1])
            return best
        
        return ("unknown", 0.1)
    
    @staticmethod
    def detect_from_image_metadata(image_bytes: bytes = None) -> Tuple[str, float]:
        """Crude image analysis without API calls."""
        if not image_bytes:
            return ("no_image", 0.0)
        
        try:
            img = Image.open(io.BytesIO(image_bytes))
            width, height = img.size
            
            # Aspect ratio hints
            aspect = width / height
            
            # Color analysis (simplified)
            colors = img.getcolors(maxcolors=100)
            if colors:
                num_colors = len(colors)
                
                # Many distinct colors → likely picture graph
                if num_colors > 20:
                    return ("picture_graph", 0.4)
                
                # Very tall image → likely number bond/vertical layout
                if aspect < 0.5:
                    return ("number_bond", 0.3)
                
                # Very wide → likely comparison (length)
                if aspect > 2.0:
                    return ("length_measurement", 0.3)
            
            return ("unknown", 0.2)
            
        except Exception:
            return ("unknown", 0.1)

# ============================================================================
# ANSWER KEY EXTRACTION
# ============================================================================

class AnswerKeyExtractor:
    """Extract and parse answer keys from PDFs."""
    
    @staticmethod
    def find_answer_key_section(text: str) -> Optional[str]:
        """Find answer key section in text."""
        patterns = [
            r'ANSWER\s*KEY.*?(?=\n\n|\Z)',
            r'ANSWERS.*?(?=\n\n|\Z)',
            r'KEY.*?(?=\n\n|\Z)',
            r'Q\d+\s*[A-D1-4].*?(?=\n\n|\Z)'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
            if match:
                return match.group()
        
        return None
    
    @staticmethod
    def parse_answer_key(key_text: str) -> Dict[str, str]:
        """Parse answer key into question→answer mapping."""
        answers = {}
        
        # Pattern: Q1 A, Q2 B, etc.
        matches = re.findall(r'Q(\d+)\s*[:\-]?\s*([A-D1-4])', key_text, re.IGNORECASE)
        for q_num, ans in matches:
            answers[q_num] = ans
        
        # Pattern: 1. A, 2. B, etc.
        matches = re.findall(r'(\d+)[\.\)]\s*([A-D1-4])', key_text, re.IGNORECASE)
        for q_num, ans in matches:
            answers[q_num] = ans
        
        return answers
    
    @staticmethod
    def infer_answer_logic(question_text: str, answer: str = None) -> str:
        """Infer answer logic from question type and answer."""
        text_lower = question_text.lower()
        
        logic_templates = {
            'mcq': "Choose correct option ({answer}), write number in brackets",
            'counting': "Count objects, write numeral {answer}",
            'comparison': "Compare, circle/cross correct option",
            'time': "Read clock, write time {answer}",
            'money': "Count coins, write amount ${answer}",
            'shapes': "Identify shape, write name/count",
            'addition': "Add numbers, write sum {answer}",
            'subtraction': "Subtract numbers, write difference {answer}"
        }
        
        # Determine question type
        if any(x in text_lower for x in ['(1)', '(2)', '(3)', '(4)', 'choose']):
            q_type = 'mcq'
        elif 'how many' in text_lower or 'count' in text_lower:
            q_type = 'counting'
        elif 'longer' in text_lower or 'shorter' in text_lower:
            q_type = 'comparison'
        elif 'clock' in text_lower or 'time' in text_lower:
            q_type = 'time'
        elif 'coin' in text_lower or 'dollar' in text_lower:
            q_type = 'money'
        elif 'shape' in text_lower:
            q_type = 'shapes'
        elif '+' in question_text or 'add' in text_lower:
            q_type = 'addition'
        elif '-' in question_text or 'subtract' in text_lower:
            q_type = 'subtraction'
        else:
            q_type = 'mcq'  # Default
        
        template = logic_templates.get(q_type, "Solve problem, write answer")
        return template.format(answer=answer or "[answer]")

# ============================================================================
# IMPROVED QUESTION DETECTION
# ============================================================================

class QuestionBoundaryDetector:
    """Better question detection using layout and semantic analysis."""
    
    @staticmethod
    def detect_questions(page_text: str, page_num: int) -> List[Dict]:
        """
        Extract questions with improved boundary detection.
        Returns list of {'number': str, 'text': str, 'options': List[str]}
        """
        lines = page_text.split('\n')
        questions = []
        current_q = None
        current_text = []
        current_options = []
        in_options = False
        
        for i, line in enumerate(lines):
            line = line.strip()
            if not line:
                continue
            
            # Check for question start patterns
            q_match = re.match(r'^(?:Q)?(\d+)[\.\)]\s*(.*)', line)
            if q_match:
                # Save previous question
                if current_q is not None:
                    questions.append({
                        'number': current_q,
                        'text': ' '.join(current_text).strip(),
                        'options': current_options.copy(),
                        'page': page_num
                    })
                
                current_q = q_match.group(1)
                current_text = [q_match.group(2)] if q_match.group(2) else []
                current_options = []
                in_options = False
                continue
            
            # Check for option patterns (1) 44, A. 44, etc.
            option_match = re.match(r'^\((\d+)\)\s*(.*)$', line)
            if option_match:
                in_options = True
                current_options.append({
                    'number': option_match.group(1),
                    'text': option_match.group(2)
                })
                continue
            
            # Also detect A. B. C. D. options
            letter_option = re.match(r'^([A-D])[\.\)]\s*(.*)$', line)
            if letter_option:
                in_options = True
                current_options.append({
                    'number': letter_option.group(1),
                    'text': letter_option.group(2)
                })
                continue
            
            # If we're collecting options, continue
            if in_options and current_options:
                # Append to last option if it's continuation
                if current_options and len(current_options[-1]['text']) < 50:
                    current_options[-1]['text'] += ' ' + line
                continue
            
            # Otherwise, add to question text
            if current_q is not None:
                # Check if line looks like start of next question
                next_q_match = re.match(r'^(\d+)[\.\)]', line)
                if next_q_match and len(current_text) > 0:
                    # This might be next question on same line
                    questions.append({
                        'number': current_q,
                        'text': ' '.join(current_text).strip(),
                        'options': current_options.copy(),
                        'page': page_num
                    })
                    current_q = next_q_match.group(1)
                    current_text = [line[len(next_q_match.group(0)):].strip()]
                    current_options = []
                    in_options = False
                else:
                    current_text.append(line)
        
        # Save last question
        if current_q is not None:
            questions.append({
                'number': current_q,
                'text': ' '.join(current_text).strip(),
                'options': current_options.copy(),
                'page': page_num
            })
        
        return questions

# ============================================================================
# BATCHED CLAUDE VISION PROCESSOR
# ============================================================================

class BatchedVisionAnalyzer:
    """Process images in batches to minimize API calls."""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.client = anthropic.Anthropic(api_key=api_key)
        self.cache = {}
        self.batch_size = 5  # Process 5 images per call
    
    def _hash_image(self, image_bytes: bytes) -> str:
        """Create hash for caching."""
        return hashlib.md5(image_bytes).hexdigest()
    
    def _batch_analyze(self, batch: List[Dict]) -> List[Dict]:
        """Analyze batch of images in single API call."""
        images_content = []
        text_content = "Classify the VISUAL_TYPE for each image:\n\n"
        
        for i, item in enumerate(batch):
            image_base64 = base64.b64encode(item['image_bytes']).decode('utf-8')
            images_content.append({
                "type": "image",
                "source": {
                    "type": "base64",
                    "media_type": "image/png",
                    "data": image_base64
                }
            })
            
            text_content += f"Image {i+1}: Question {item['q_num']} - \"{item['text'][:100]}...\"\n"
        
        text_content += """
For each image, classify VISUAL_TYPE from:
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

Also briefly describe the visual's ROLE in the question logic.

Return JSON array: [
  {"image": 1, "visual_type": "...", "role": "..."},
  {"image": 2, "visual_type": "...", "role": "..."},
  ...
]"""
        
        try:
            message = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=800,
                messages=[{
                    "role": "user",
                    "content": images_content + [{"type": "text", "text": text_content}]
                }]
            )
            
            # Parse JSON response
            response_text = message.content[0].text
            json_match = re.search(r'\[.*\]', response_text, re.DOTALL)
            
            if json_match:
                results = json.loads(json_match.group())
                return results
            else:
                # Fallback to individual analysis
                return self._fallback_analyze(batch)
                
        except Exception as e:
            print(f"Batch Claude API error: {e}")
            return self._fallback_analyze(batch)
    
    def _fallback_analyze(self, batch: List[Dict]) -> List[Dict]:
        """Fallback analysis when batch fails."""
        return [{"image": i+1, "visual_type": "unknown", "role": "API error"} for i in range(len(batch))]
    
    def analyze_images(self, questions_with_images: List[Dict]) -> List[Dict]:
        """Analyze images with caching and batching."""
        results = []
        batch = []
        
        for q in questions_with_images:
            img_hash = self._hash_image(q['image_bytes'])
            
            # Check cache
            if img_hash in self.cache:
                results.append({
                    'question_number': q['question_number'],
                    'visual_type': self.cache[img_hash]['visual_type'],
                    'role': self.cache[img_hash]['role'],
                    'source': 'cache'
                })
                continue
            
            # Add to batch
            batch.append({
                'image_bytes': q['image_bytes'],
                'q_num': q['question_number'],
                'text': q['text']
            })
            
            # Process batch when full
            if len(batch) >= self.batch_size:
                batch_results = self._batch_analyze(batch)
                
                for i, result in enumerate(batch_results):
                    img_hash_i = self._hash_image(batch[i]['image_bytes'])
                    
                    # Cache result
                    self.cache[img_hash_i] = {
                        'visual_type': result.get('visual_type', 'unknown'),
                        'role': result.get('role', '')
                    }
                    
                    results.append({
                        'question_number': batch[i]['q_num'],
                        'visual_type': result.get('visual_type', 'unknown'),
                        'role': result.get('role', ''),
                        'source': 'claude_batch'
                    })
                
                batch = []
        
        # Process remaining items
        if batch:
            batch_results = self._batch_analyze(batch)
            for i, result in enumerate(batch_results):
                img_hash_i = self._hash_image(batch[i]['image_bytes'])
                
                self.cache[img_hash_i] = {
                    'visual_type': result.get('visual_type', 'unknown'),
                    'role': result.get('role', '')
                }
                
                results.append({
                    'question_number': batch[i]['q_num'],
                    'visual_type': result.get('visual_type', 'unknown'),
                    'role': result.get('role', ''),
                    'source': 'claude_batch'
                })
        
        return results

# ============================================================================
# MAIN OPTIMIZED PROCESSOR
# ============================================================================

class OptimizedProcessor:
    """Main processor with all optimizations."""
    
    def __init__(self, claude_api_key: str = None):
        self.claude_key = claude_api_key or os.environ.get('CLAUDE_API_KEY')
        self.heuristic_detector = HeuristicVisualDetector()
        self.answer_extractor = AnswerKeyExtractor()
        self.question_detector = QuestionBoundaryDetector()
        
        if self.claude_key:
            self.vision_analyzer = BatchedVisionAnalyzer(self.claude_key)
        else:
            self.vision_analyzer = None
            print("WARNING: Claude API key not set. Vision analysis disabled.")
    
    def process_pdf(self, pdf_path: Path, output_dir: Path, limit_questions: int = None) -> int:
        """Process a single PDF with all optimizations."""
        print(f"Processing: {pdf_path.name}")
        
        # Extract whole PDF text for answer key search
        full_text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    full_text += text + "\n\n"
        
        # Find answer key
        answer_key_section = self.answer_extractor.find_answer_key_section(full_text)
        answer_key = {}
        if answer_key_section:
            answer_key = self.answer_extractor.parse_answer_key(answer_key_section)
            print(f"  Found answer key for {len(answer_key)} questions")
        
        # Process questions page by page
        questions_processed = 0
        questions_with_images = []
        question_data = []
        
        with pdfplumber.open(pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages, 1):
                text = page.extract_text()
                if not text:
                    continue
                
                # Extract page image
                page_image = page.to_image(resolution=150)
                image_bytes = None
                if page_image:
                    img_buffer = io.BytesIO()
                    page_image.save(img_buffer, format='PNG')
                    image_bytes = img_buffer.getvalue()
                
                # Detect questions on this page
                questions = self.question_detector.dect_questions(text, page_num)
                
                for q in questions:
