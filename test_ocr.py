#!/usr/bin/env python3
import pytesseract
from PIL import Image
import sys
import json

image_path = "./openclaw-dashboard-UI/screenshots/01-overview.png"
print(f"Processing {image_path}")
try:
    img = Image.open(image_path)
except Exception as e:
    print(f"Error opening image: {e}")
    sys.exit(1)

# Extract text with default config
text = pytesseract.image_to_string(img)
print("Extracted text:")
print("---")
print(text)
print("---")

# Get detailed data including confidence
data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
total_conf = 0
count = 0
for conf in data['conf']:
    if conf != -1:
        total_conf += conf
        count += 1
avg_conf = total_conf / count if count else 0
print(f"Average confidence: {avg_conf:.2f}")

# Save text to artifacts directory
output_path = "./ATOM-SG Pilot/05-Backend/artifacts/ocr/test_ocr_py.txt"
try:
    with open(output_path, 'w') as f:
        f.write(text)
    print(f"Saved to {output_path}")
except Exception as e:
    print(f"Error writing file: {e}")