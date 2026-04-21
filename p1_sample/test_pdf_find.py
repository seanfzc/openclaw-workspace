#!/usr/bin/env python3
from pathlib import Path

pdf_files = list(Path('.').glob('*.pdf'))
print(f"Found {len(pdf_files)} PDF files")
for f in pdf_files:
    print(f"  {f.name} -> {f.resolve()}")