#!/usr/bin/env python3
import pytesseract
from PIL import Image, ImageDraw, ImageFont
import sys
import os

# First, test with a simple generated image
print("=== Generating test image with text ===")
img = Image.new('RGB', (400, 200), color='white')
draw = ImageDraw.Draw(img)
# Use default font
try:
    font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 24)
except:
    font = ImageFont.load_default()
draw.text((50, 80), "Hello World! This is a test.", fill='black', font=font)
test_path = "./test_generated.png"
img.save(test_path)
print(f"Saved generated image to {test_path}")

# OCR on generated image
text = pytesseract.image_to_string(img)
print(f"Extracted text from generated image: '{text.strip()}'")
if "Hello World" in text:
    print("SUCCESS: Tesseract works!")
else:
    print("WARNING: Tesseract may have issues.")

# Now test on the screenshot with different PSM modes
print("\n=== Testing on screenshot ===")
screenshot_path = "./openclaw-dashboard-UI/screenshots/01-overview.png"
if not os.path.exists(screenshot_path):
    print(f"Screenshot not found: {screenshot_path}")
    sys.exit(1)

img2 = Image.open(screenshot_path)
psm_modes = {
    3: "Auto",
    6: "Uniform block",
    11: "Sparse text",
    12: "Sparse text with OSD",
}
for psm, desc in psm_modes.items():
    config = f'--psm {psm}'
    text = pytesseract.image_to_string(img2, config=config)
    print(f"\nPSM {psm} ({desc}):")
    print("---")
    print(text[:200] + ("..." if len(text) > 200 else ""))
    print("---")

# Also try with image preprocessing: convert to grayscale, increase contrast
print("\n=== Preprocessing: grayscale, threshold ===")
gray = img2.convert('L')
# Apply simple threshold
threshold = 128
bw = gray.point(lambda p: p > threshold and 255)
text = pytesseract.image_to_string(bw)
print("After threshold:")
print(text[:200])
print("---")

# Save extracted text to artifacts directory
output_dir = "./ATOM-SG Pilot/05-Backend/artifacts/ocr"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "test_ocr_screenshot.txt")
with open(output_path, 'w') as f:
    f.write(text)
print(f"\nSaved extracted text to {output_path}")

# Clean up generated image
os.remove(test_path)
print("Cleaned up generated image.")