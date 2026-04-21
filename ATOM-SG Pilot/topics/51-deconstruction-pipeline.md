---
title: Topic #51 — Deconstruction Pipeline
description: Vision LLM 3-layer pipeline (OCR + VLM + OpenCV) → YAML
status: active
owner: Vision LLM Bot
last_updated: 2026-04-21 11:25 SGT
---

# Topic #51 — Deconstruction Pipeline

## Purpose

Coordinate the Vision LLM 3-layer extraction pipeline for converting 4 exam questions from PDF to structured YAML with confidence scores.

## Scope

- **Layer 1: OCR (RapidOCR)** — Extract text, labels, numeric values
- **Layer 2: Vision LLM (Qwen/Ollama/Moondream)** — Extract structure, relationships, pathway classification
- **Layer 3: OpenCV** — Pixel-precise measurements, angles, dimensions, line styles
- **Merge:** Combine all three layers into tagged YAML with confidence scores

## Tasks (Assigned from SOR v4.5)

| ID | Task | Owner | Target | Success Criteria |
|----|------|-------|--------|--------------|
| D1 | Install and configure Vision LLM model | Vision LLM Bot | 2026-04-23 | Model selected and operational |
| D2 | Install and configure OpenCV | OpenCV Bot | 2026-04-23 | OpenCV functions working |
| D3 | Implement 3-layer merge logic | Vision LLM Bot | 2026-04-24 | Source priority, confidence tagging, conflict detection |
| D4 | Create YAML schemas for problem types | Vision LLM Bot | 2026-04-23 | Schema defined for all 4 question types |
| D5 | Deconstruct 4 exam questions to YAML | Vision LLM Bot | 2026-04-26 | All 4 questions output as tagged YAML |

## Reporting

- **Progress Updates:** Report daily to this topic only (not directly to Sean)
- **Task Completion:** Report when each D-task completes
- **Blocking Issues:** Report immediately if any task blocks

## Success Criteria

- All 4 exam questions converted to YAML with confidence scores ≥0.7
- All YAML files validated for structural integrity
- Vision LLM model selected and operational

---

*Created for SOR v4.5 Deconstruction Pipeline coordination*
