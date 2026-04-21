#!/usr/bin/env python3
"""Quick test to verify matplotlib can generate SVG with pastel colors."""

import matplotlib.pyplot as plt
import os

# Create a simple pastel bar chart
colors = ["#FFB6C1", "#98FB98", "#87CEEB"]
labels = ["Test A", "Test B", "Test C"]
values = [30, 50, 20]

plt.figure(figsize=(6, 4))
plt.bar(labels, values, color=colors, edgecolor='black')
plt.title("Matplotlib Test (Pastel Colors)")
plt.ylabel("Value")

# Save as SVG
output_path = "test_output.svg"
plt.savefig(output_path, format='svg')
plt.close()

if os.path.exists(output_path):
    print(f"✓ SVG created: {output_path}")
    print(f"  File size: {os.path.getsize(output_path)} bytes")
else:
    print("✗ Failed to create SVG")

# Also test PNG
plt.bar(labels, values, color=colors)
plt.savefig("test_output.png", format='png')
plt.close()
if os.path.exists("test_output.png"):
    print(f"✓ PNG created: test_output.png")