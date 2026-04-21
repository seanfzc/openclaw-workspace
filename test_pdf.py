#!/usr/bin/env python3
import fitz
import sys

pdf_path = '/Users/zcaeth/.openclaw/workspace/p1_sample/2021 P1 Maths Revisions Mgs.pdf'
try:
    doc = fitz.open(pdf_path)
    text = ''
    for page in doc:
        text += page.get_text()
    print(f"Pages: {len(doc)}")
    print(f"First 500 chars:\n{text[:500]}")
    doc.close()
except Exception as e:
    print(f"Error: {e}")