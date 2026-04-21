#!/usr/bin/env python3
import sys
import os
import xml.etree.ElementTree as ET
from pathlib import Path

def extract_svg_text(svg_path):
    """Extract text elements from SVG."""
    try:
        tree = ET.parse(svg_path)
        root = tree.getroot()
        # SVG namespace
        ns = {'svg': 'http://www.w3.org/2000/svg'}
        texts = []
        for text_elem in root.findall('.//svg:text', ns):
            # Get text content
            txt = ''.join(text_elem.itertext()).strip()
            if txt:
                texts.append(txt)
        return texts
    except ET.ParseError as e:
        return [f"Parse error: {e}"]
    except Exception as e:
        return [f"Error: {e}"]

def main():
    render_dir = Path("./ATOM-SG Pilot/05-Backend/artifacts/renders")
    svg_files = sorted(list(render_dir.glob("G*.svg")))
    for svg in svg_files:
        print(f"\n=== {svg.name} ===")
        texts = extract_svg_text(svg)
        if texts:
            print("Text labels:", texts)
        else:
            print("No text labels found")

if __name__ == "__main__":
    main()