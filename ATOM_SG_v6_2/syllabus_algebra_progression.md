# Syllabus Algebra Progression (v1.2) — ATOM-SG

## Project: ATOM-SG (v6.2) - Vertical Thread: Algebraic Continuity
## Topic: Mathematics - Number & Algebra Strand (2026 MOE Singapore Primary Syllabus)

---

## Vertical Thread Table

| Thread | Seed Node (P1-P2) | Bridge Nodes (P3-P4) | Boss Node (P6) | Status |
| :--- | :--- | :--- | :--- | :--- |
| **A** | `P1-N1-PartWhole` | `P3-M2-ScaledComparison` → `P4-A1-UnitScaling` | **ROSYTH-P6-ALG-01** — $15(1+x)$ | ✅ Complete |
| **B** | `P2-M1-EqualGroups` | `P3-N3-DifferencePatterns` → `P4-M3-OffsetRemoval` | **ROSYTH-P6-ALG-02** — $b = \frac{32-5y}{8}$ | ✅ Complete |
| **B-alt** | `P1-N2-Comparison` | `P3-N3-DifferencePatterns` | **ROSYTH-P6-ALG-02** (secondary) | ✅ Conditional |
| **C** | `P2-N1-MissingVal` | `P3-N4-InverseOperations` → `P4-A2-BalancingEquations` | **ROSYTH-P6-ALG-03** — $3x + 5 = 20$, $x = 5$ | ✅ Complete |
| **D** | `P1-N2-Subtraction` | ⚠️ `P3-F1-FractionOfWhole` → `P4-F2-RemainderAction` | *Pending Boss (P6-A3-WordProbs)* | 🔲 Queued |

---

## Graphify Bidirectional Links (Formalized)

### Thread A Links
```
P1-N1-PartWhole ←→ P3-M2-ScaledComparison ←→ P4-A1-UnitScaling ←→ ROSYTH-P6-ALG-01
```
- CLS: 1.0 → 0.7 → 1.3 — all ≤ 1.5 ✅

### Thread B Links
```
P2-M1-EqualGroups ←→ P3-N3-DifferencePatterns ←→ P4-M3-OffsetRemoval ←→ ROSYTH-P6-ALG-02
```
- CLS: 0.8 → 0.7 → 1.3 — all ≤ 1.5 ✅
- **[High_CLS_Jump]** tag: P3-N3 (1.8) → ROSYTH-P6-ALG-02 (3.8) was CLS 2.0 BEFORE P4-M3 fix. Retained as historical warning.

### Thread C Links
```
P2-N1-MissingVal ←→ P3-N4-InverseOperations ←→ P4-A2-BalancingEquations ←→ ROSYTH-P6-ALG-03
```
- CLS: 1.0 → 0.4 → 1.1 — all ≤ 1.5 ✅
- **Hard-Link:** ROSYTH-P6-ALG-03 ↔ P4-A2-BalancingEquations (direct parent)

### Thread D Links (Planned)
```
P1-N2-Subtraction ←→ P3-F1-FractionOfWhole ←→ P4-F2-RemainderAction ←→ [PENDING BOSS]
```
- Target CLS: ~1.0 → ~0.5 → ~1.2

---

## Tier 1: Seeds (P1-P2)

| Code | Level | Concept | Threads Served |
| :--- | :--- | :--- | :--- |
| `P1-N1-PartWhole` | P1 | Number bonds within 20 | Thread A |
| `P1-N2-Comparison` | P1 | More than / Less than | Thread B-alt |
| `P1-N2-Subtraction` | P1 | Taking away from a set | Thread D |
| `P2-N1-MissingVal` | P2 | $45 + ? = 60$ | Thread C |
| `P2-M1-EqualGroups` | P2 | Repeated addition, equal sharing | Thread B |

## Tier 2: Bridges (P3-P4)

| Code | Level | Concept | Status | Thread |
| :--- | :--- | :--- | :--- | :--- |
| `P3-M2-ScaledComparison` | P3 | "3 times as many," unit model | ✅ Forged | A |
| `P4-A1-UnitScaling` | P4 | Scale units to find totals | ✅ Forged | A |
| `P3-N3-DifferencePatterns` | P3 | Constant difference, shaded box | ✅ Forged | B, B-alt |
| `P4-M3-OffsetRemoval` | P4 | Un-snap offset, create equal groups | ✅ Forged | B |
| `P3-N4-InverseOperations` | P3 | Undo Machine, reverse operations | ✅ Forged | C |
| `P4-A2-BalancingEquations` | P4 | Scale Master, balance both sides | ✅ Forged | C |
| `P3-F1-FractionOfWhole` | P3 | Fraction of a quantity | ⚠️ QUEUED | D |
| `P4-F2-RemainderAction` | P4 | Calculate remainder after fractional take-away | ⚠️ QUEUED | D |

## Tier 3: Bosses (P6)

| Code | Source | Bimodal | Triad Summary | Thread |
| :--- | :--- | :--- | :--- | :--- |
| `ROSYTH-P6-ALG-01` | Rosyth CA1 Q1 | Mode A (Fluency) | Ratio $1:x$, Comparison Bar, `P6-A1-Expressions` | A |
| `ROSYTH-P6-ALG-02` | Rosyth CA1 Q2 | Mode B (Odyssey) | Substitution offset, `P6-A2-Equations` | B |
| `ROSYTH-P6-ALG-03` | Rosyth CA1 Q3 | Mode B (Odyssey) | Solve $3x + 5 = 20$, `P6-A2-Equations` | C |

---

## Topic Changes & Filtering (Death List)

| Action | Topic | Detail |
| :--- | :--- | :--- |
| DELETE | Speed | Moved to Secondary 1 |
| DELETE | 8-Point Compass | Removed from primary |
| DELETE | Cells (Science) | Removed from PSLE scope |
| SHIFT | Pie Charts & Nets | Now P4 — "Foundational Review" only |
| SHIFT | Ratio & Average | Consolidated at P6 |

---

*Syllabus Map v1.2 — Threads A, B, C Complete. Thread D Queued. Digital Twin 0.2 Online.*
