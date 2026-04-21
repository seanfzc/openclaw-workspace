#!/usr/bin/env python3.10
import json
from graphify.detect import detect
from pathlib import Path

target = Path('/Users/zcaeth/Desktop/sg_exam_papers/Maths/P1')
result = detect(target)
print(json.dumps(result, indent=2))