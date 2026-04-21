#!/usr/bin/env python3
"""
FINAL PIPELINE: Cost-optimized processing with second brain mapping.
Processes P1 math PDFs, extracts questions with answer keys and visual types,
and saves to second brain with education lens.
"""

import json
import re
import os
import base64
import hashlib
from pathlib import Path
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass
from enum import Enum

import pdfplumber
from PIL import Image
import io
import anthropic

# ============================================================================
# FREE HEURISTICS (from cost_optimized_pipeline.py)
# ============================================================================

class HeuristicVisualDetector:
    """Free visual type detection - avoids API calls."""
    
    VISUAL_KEYWORDS = {
        'number_bond': ['number bond', 'ten frame', 'part whole', 'bond', 'frame'],
        'picture_graph': ['picture graph', 'graph', 'chart', 'bar', 'tally', 'most', 'least'],
        'analog_clock': ['clock', 'time', 'analog', 'o\'clock', 'half past', 'minute', 'hour'],
        'digital_clock': ['digital', ':', 'pm', 'am', 'digital clock'],
        'shapes': ['shape', 'circle', 'square', 'triangle', 'rectangle', 'cube', '3d'],
        'money_coins': ['coin', 'dollar', 'cent', 'money', 'currency', 'note', 'singapore'],
        'length_measurement': ['longer', 'shorter', 'measure', 'cm', 'centimeter', 'ruler', 'length'],
        'counting_objects': ['count', 'how many', 'objects', 'pencils', 'sweets', 'balls', 'apples'],
        'pattern_sequence': ['pattern', 'next', 'sequence', 'repeat', 'comes next']
    }
    
    @staticmethod
    def detect(question_text: str, image_bytes: bytes = None) -> Tuple[str, float, str]:
        """
        Detect visual type with confidence score.
        Returns: (visual_type, confidence, method)
        """
        text_lower = question_text.lower()
        
        # Method 1: Text keywords (fastest)
        text_scores = {}
        for vtype, keywords in HeuristicVisualDetector.VISUAL_KEYWORDS.items():
            matches = sum(1 for kw in keywords if kw in text_lower)
            if matches > 0:
                text_scores[vtype] = min(0.3 + (matches * 0.1), 0.8)
        
        if text_scores:
            best_type, best_score = max(text_scores.items(), key=lambda x: x[1])
            if best_score >= 0.5:
                return best_type, best_score, "text_keyword"
        
        # Method 2: Image metadata (free)
        if image_bytes:
            img_type, img_score = HeuristicVisualDetector._analyze_image_metadata(image_bytes)
            if img_score >= 0.4:
                return img_type, img_score, "image_metadata"
        
        # Method 3: Question structure hints
        if any(x in question_text for x in ['(1)', '(2)', '(3)', '(4)']):
            # Multiple choice often has diagrams
            return "unknown_mcq", 0.3, "question_structure"
        
        return "unknown", 0.1, "default"
    
    @staticmethod
    def _analyze_image_metadata(image_bytes: bytes) -> Tuple[str, float]:
        """Simple image analysis without API."""
        try:
            img = Image.open(io.BytesIO(image_bytes))
            width, height = img.size
            aspect = width / height
            
            # Color analysis
            colors = img.getcolors(maxcolors=100)
            if colors:
                num_colors = len(colors)
                
                # Many colors → likely picture graph
                if num_colors > 25:
                    return ("picture_graph", 0.5)
                
                # Very tall → number bond
                if aspect < 0.4:
                    return ("number_bond", 0.4)
                
                # Very wide → comparison
                if aspect > 2.5:
                    return ("length_measurement", 0.4)
            
            # Check for common patterns
            if width > 800 and height > 600:
                return ("complex_diagram", 0.3)
            
            return ("unknown", 0.2)
        except:
            return ("unknown", 0.1)

# ============================================================================
# BATCHED CLAUDE FOR OUTLIERS
# ============================================================================

class BatchedClaudeAnalyzer:
    """Only for complex/ambiguous visuals (confidence < 0.7)."""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.client = anthropic.Anthropic(api_key=api_key)
        self.cache = {}
        self.batch_size = 8
        self.model = "claude-sonnet-4-6"
    
    def _hash_image(self, image_bytes: bytes) -> str:
        return hashlib.md5(image_bytes).hexdigest()
    
    def analyze_complex_images(self, complex_questions: List[Dict]) -> List[Dict]:
        """
        Analyze ONLY complex questions (heuristic confidence < 0.7).
        Returns list of {'question_number': str, 'visual_type': str, 'role': str}
        """
        if not complex_questions:
            return []
        
        print(f"  Sending {len(complex_questions)} complex images to Claude...")
        
        # Group into batches
        batches = []
        for i in range(0, len(complex_questions), self.batch_size):
            batches.append(complex_questions[i:i + self.batch_size])
        
        results = []
        
        for batch_idx, batch in enumerate(batches):
            print(f"    Batch {batch_idx + 1}/{len(batches)} ({len(batch)} images)")
            
            try:
                batch_result = self._process_batch(batch)
                results.extend(batch_result)
                
                # Cache results
                for i, item in enumerate(batch):
                    img_hash = self._hash_image(item['image_bytes'])
                    self.cache[img_hash] = {
                        'visual_type': batch_result[i]['visual_type'],
                        'role': batch_result[i]['role']
                    }
                    
            except Exception as e:
                print(f"    Batch failed: {e}")
                # Fallback to unknown
                for item in batch:
                    results.append({
                        'question_number': item['question_number'],
                        'visual_type': 'unknown',
                        'role': f'Claude error: {str(e)[:50]}'
                    })
        
        return results
    
    def _process_batch(self, batch: List[Dict]) -> List[Dict]:
        """Process one batch of images."""
        images_content = []
        text_content = "Analyze these Primary 1 math questions:\n\n"
        
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
            
            text_content += f"Image {i+1}: Q{item['question_number']} - \"{item['text'][:80]}...\"\n"
        
        text_content += """
For EACH image, classify VISUAL_TYPE from:
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

Briefly describe the visual's ROLE (1 sentence).

Return JSON array exactly:
[
  {"image": 1, "visual_type": "...", "role": "..."},
  {"image": 2, "visual_type": "...", "role": "..."},
  ...
]"""
        
        message = self.client.messages.create(
            model=self.model,
            max_tokens=600,
            messages=[{
                "role": "user",
                "content": images_content + [{"type": "text", "text": text_content}]
            }]
        )
        
        response_text = message.content[0].text
        json_match = re.search(r'\[.*\]', response_text, re.DOTALL)
        
        if json_match:
            return json.loads(json_match.group())
        else:
            # Fallback
            return [{"image": i+1, "visual_type": "unknown", "role": "Parse error"} for i in range(len(batch))]

# ============================================================================
# ANSWER KEY EXTRACTION
# ============================================================================

class AnswerKeyExtractor:
    """Extract answer keys from PDFs."""
    
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

# ============================================================================
# ANSWER LOGIC INFERENCE
# ============================================================================

class AnswerLogicExtractor:
    """Infer answer logic from question patterns."""
    
    @staticmethod
    def extract(question_text: str, answer: str = None) -> str:
        """Infer answer logic from question patterns."""
        text_lower = question_text.lower()
        
        # MCQ patterns
        if any(x in question_text for x in ['(1)', '(2)', '(3)', '(4)']):
            if answer:
                return f"Choose option ({answer}), write number in brackets"
            return "Choose correct option, write number in brackets"
        
        # Counting
        if 'how many' in text_lower or 'count' in text_lower:
            if answer:
                return f"Count objects, write {answer}"
            return "Count objects, write numeral"
        
        # Time
        if 'clock' in text_lower or 'time' in text_lower:
            if answer:
                return f"Read clock, write {answer}"
            return "Read analog/digital clock, write time"
        
        # Money
        if any(word in text_lower for word in ['coin', 'dollar', 'cent', 'money']):
            if answer:
                return f"Count coins, write ${answer}"
            return "Count coins/notes, write amount"
        
        # Comparison
        if 'longer' in text_lower or 'shorter' in text_lower:
            return "Compare lengths, circle/cross correct option"
        
        # Addition/Subtraction
        if '+' in question_text or 'add' in text_lower:
            if answer:
                return f"Add numbers, write sum {answer}"
            return "Add numbers, write sum"
        
        if '-' in question_text or 'subtract' in text_lower:
            if answer:
                return f"Subtract numbers, write difference {answer}"
            return "Subtract numbers, write difference"
        
        # Default
        return "Solve problem, write answer in box"

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
# MAIN PROCESSOR WITH SECOND BRAIN MAPPING
# ============================================================================

class SecondBrainPipeline:
    """
    Complete pipeline:
    1. Extract questions from PDF with answer keys
    2. Cost-optimized visual classification
    3. Map to second brain schema with education lens
    """
    
    def __init__(self, claude_api_key: str = None):
        self.api_key = claude_api_key or os.environ.get('CLAUDE_API_KEY')
        self.heuristic_detector = HeuristicVisualDetector()
        self.answer_extractor = AnswerKeyExtractor()
        self.question_detector = QuestionBoundaryDetector()
        self.logic_extractor = AnswerLogicExtractor()
        
        if self.api_key:
            self.claude_analyzer = BatchedClaudeAnalyzer(self.api_key)
        else:
            self.claude_analyzer = None
            print("WARNING: Claude API disabled. Using heuristics only.")
        
        # Second brain paths
        self.workspace_root = Path('/Users/zcaeth/.openclaw/workspace')
        self.second_brain_raw = self.workspace_root / 'second-brain-simple' / 'raw'
        self.second_brain_wiki = self.workspace_root / 'second-brain-simple' / 'wiki'
        
        # Create directories
        (self.second_brain_raw / 'exam-questions').mkdir(parents=True, exist_ok=True)
        (self.second_brain_wiki / 'entities' / 'education-learning').mkdir(parents=True, exist_ok=True)
        (self.second_brain_wiki / 'concepts' / 'education-development').mkdir(parents=True, exist_ok=True)
    
    def process_pdf(self, pdf_path: Path, sample_limit: int = 10) -> Dict:
        """
        Process a single PDF and return results.
        Returns dict with metadata and questions.
        """
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
            answer_key = self.answer_extractor.parse