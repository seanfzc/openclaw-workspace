#!/usr/bin/env python3
"""
Generate exam-quality diagrams using Vision LLM (zai/glm-5v-turbo)
"""
import base64
import json
import requests
import os

def encode_image(image_path):
    """Encode image to base64"""
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode('utf-8')

def call_glm_vision(image_path, prompt):
    """Call GLM-5V Turbo Vision API"""
    image_base64 = encode_image(image_path)
    
    payload = {
        "model": "glm-5v-turbo",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{image_base64}"
                        }
                    },
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }
        ],
        "max_tokens": 2000
    }
    
    # Use OpenAI-compatible endpoint for ZAI
    headers = {
        "Authorization": f"Bearer {os.environ.get('ZAI_API_KEY', '')}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(
            "https://api.z.ai/api/coding/paas/v4/chat/completions",
            headers=headers,
            json=payload,
            timeout=30
        )
        response.raise_for_status()
        result = response.json()
        return result
    except Exception as e:
        return {"error": str(e)}

def analyze_diagram(image_path, question_yaml):
    """Analyze diagram and extract specifications"""
    prompt = f"""Analyze this mathematics diagram and extract:

1. Diagram type (pie chart, container/tank, line graph, complex polygon)
2. All visible labels, measurements, and annotations
3. Colors used (if visible)
4. Exact values shown (percentages, angles, quantities)
5. Style characteristics (font, line thickness, proportions)

Return as JSON with these fields:
- diagram_type
- elements (list of all labeled elements)
- measurements (all numeric values shown)
- colors (main colors used)
- style_notes (stylistic observations)
- completeness_check (what's missing or unclear)

Question context: {question_yaml}"""
    
    result = call_glm_vision(image_path, prompt)
    return result

if __name__ == "__main__":
    # Analyze each question
    questions = {
        "Q7": {
            "image": "page-17.png",
            "type": "pie_chart"
        },
        "Q9": {
            "image": "page-19.png",
            "type": "container"
        },
        "Q10": {
            "image": "page-20.png",
            "type": "line_graph"
        },
        "Q13": {
            "image": "page-23.png",
            "type": "complex_polygon"
        }
    }
    
    for q_id, info in questions.items():
        print(f"\n{'='*50}")
        print(f"Analyzing {q_id} ({info['type']})...")
        print('='*50)
        
        result = analyze_diagram(info['image'], info['type'])
        
        if 'error' in result:
            print(f"ERROR: {result['error']}")
        else:
            print(json.dumps(result, indent=2, ensure_ascii=False)[:2000])
