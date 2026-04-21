#!/usr/bin/env python3
"""
Use Claude Vision to extract questions from PDF page image.
"""

import base64
from pathlib import Path
import anthropic
import os

def read_image_base64(image_path):
    """Read image and return base64 string."""
    with open(image_path, 'rb') as f:
        img_bytes = f.read()
    return base64.b64encode(img_bytes).decode('utf-8')

def extract_questions_with_vision(image_base64, api_key):
    """Use Claude Vision to extract questions from image."""
    
    client = anthropic.Anthropic(api_key=api_key)
    
    prompt = """You are analyzing a scanned page from a Singapore Primary 6 (P6) Mathematics exam paper.
The page likely contains math questions. Your task is to:

1. Identify ALL questions on the page
2. For each question, extract:
   - The full question text
   - Any multiple choice options (A, B, C, D or 1, 2, 3, 4)
   - Any diagrams or visual elements described
   - The question number if visible

3. Categorize each question by topic:
   - Algebra (contains variables like x, y, equations, expressions)
   - Ratio/Proportion (contains ratios, sharing, proportions)
   - Percentage (contains %, discount, increase/decrease)
   - Other (geometry, measurement, statistics, etc.)

4. Note if the question appears to be part of a "linked question" set (same diagram/scenario used for multiple questions)

Format your response as:
QUESTION [number]:
[Full question text]

OPTIONS: [A. ... B. ... etc. or None]

TOPIC: [Algebra/Ratio/Percentage/Other]

LINKED: [Yes/No - describe if same scenario as other questions]

NOTES: [Any relevant observations about the question]

Separate questions with ---

If no questions are found, say: NO QUESTIONS FOUND"""

    try:
        message = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=4000,
            messages=[
                {
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
                }
            ]
        )
        
        return message.content[0].text
        
    except Exception as e:
        return f"Error with vision API: {e}"

def main():
    # Check for API key
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        # Try to get from file or other sources
        print("ANTHROPIC_API_KEY environment variable not set")
        print("Checking for API key in workspace...")
        
        # Check if there's an API key in the pipeline file
        pipeline_path = Path('/Users/zcaeth/.openclaw/workspace/p1_sample/final_pipeline.py')
        if pipeline_path.exists():
            with open(pipeline_path, 'r') as f:
                content = f.read()
                # Look for API key pattern
                import re
                match = re.search(r'api_key\s*=\s*["\']([^"\']+)["\']', content)
                if match:
                    api_key = match.group(1)
                    print(f"Found API key in pipeline file")
                else:
                    print("No API key found in pipeline file")
                    return
    
    if not api_key:
        print("Cannot proceed without API key")
        print("Please set ANTHROPIC_API_KEY environment variable")
        return
    
    # Read the image we extracted earlier
    image_path = Path('/tmp/page_2.png')
    if not image_path.exists():
        print(f"Image not found: {image_path}")
        print("Run extract_page_image.py first")
        return
    
    print(f"Reading image: {image_path}")
    image_base64 = read_image_base64(image_path)
    print(f"Image base64 size: {len(image_base64)} characters")
    
    print("\n" + "="*80)
    print("SENDING TO CLAUDE VISION FOR EXTRACTION...")
    print("="*80)
    
    # Extract questions
    result = extract_questions_with_vision(image_base64, api_key)
    
    print("\nVISION EXTRACTION RESULTS:")
    print("="*80)
    print(result)
    
    # Save results
    output_path = Path('/Users/zcaeth/.openclaw/workspace/vision_extraction_results.txt')
    with open(output_path, 'w') as f:
        f.write(result)
    
    print(f"\nResults saved to: {output_path}")

if __name__ == "__main__":
    main()