#!/usr/bin/env python3
"""
Test Qwen Vision LLM API
"""
import base64
import json
import requests

# Qwen VL API endpoint
API_KEY = "sk-1b2bfd0294e74d919cc33fe17ef86f45"
URL = "https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation"

def encode_image(image_path):
    """Encode image to base64"""
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode('utf-8')

def test_qwen_vision(image_path, prompt):
    """Test Qwen Vision API"""
    # Encode image
    image_base64 = encode_image(image_path)

    # Prepare request
    payload = {
        "model": "qwen-vl-max",
        "input": {
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "image": f"data:image/png;base64,{image_base64}"
                        },
                        {
                            "text": prompt
                        }
                    ]
                }
            ]
        },
        "parameters": {}
    }

    # Make request
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        result = response.json()
        return result
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    # Test with Q7
    print("Testing Qwen VL with Q7...")
    result = test_qwen_vision(
        "Q7_candidate.png",
        "What does this image show? Describe the question, any diagrams, and what the student needs to solve."
    )
    print(json.dumps(result, indent=2, ensure_ascii=False)[:1000])
