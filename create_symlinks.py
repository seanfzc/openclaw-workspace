#!/usr/bin/env python3
import os
from pathlib import Path

sample_dir = Path('/Users/zcaeth/.openclaw/workspace/p1_sample')
sample_dir.mkdir(exist_ok=True)

with open('/Users/zcaeth/.openclaw/workspace/selected_pdfs.txt') as f:
    paths = [line.strip() for line in f if line.strip()]

for src in paths:
    src_path = Path(src)
    dest = sample_dir / src_path.name
    if dest.exists():
        dest.unlink()
    os.symlink(src, dest)
    print(f"Linked {src_path.name}")

print(f"Created {len(paths)} symlinks in {sample_dir}")