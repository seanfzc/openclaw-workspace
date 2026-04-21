# VERTICAL THREADING RULES (v2.0) — Post-Mortem Update

## Root Cause Analysis

**Gap:** P4-M3-OffsetRemoval was missing from Thread B.
**Why:** The Architect's original rule was "Link P6 Boss to a P1-P3 Seed." This only checks for EXISTENCE of a connection, not LEARNABILITY of the progression.
**Classification:** Cognitive Leap Error — a bridge that teaches a CONCEPT was present, but a bridge that teaches the ACTION was absent.

---

## Updated Threading Rules

### Rule 1: The Verb Test (NEW)
Every node in a vertical thread must teach an ACTION, not just a CONCEPT.

**Check:** Can you complete this sentence for each node?
- "At this level, the student learns to ________."

If the blank is a noun ("the difference"), it's a concept node.
If the blank is a verb ("remove the difference"), it's an action node.

**Mandate:** Every thread MUST contain at least one action node between any concept node and its Boss. A concept without a corresponding action is an incomplete bridge.

| ❌ FAILS Verb Test | ✅ PASSES Verb Test |
| :--- | :--- |
| "The difference is constant" (concept only) | "Remove the difference to create equal groups" (action) |
| "Ratios exist" (concept only) | "Find the value of 1 unit" (action) |
| "Fractions represent parts" (concept only) | "Calculate a fraction OF a quantity" (action) |

### Rule 2: The Cognitive Leap Score (NEW)
Between any two adjacent nodes in a thread, calculate the Cognitive Leap Score (CLS):

$$CLS = |C_{boss} - C_{bridge}|$$

Where $C$ = complexity_score from the node's bimodal_calibration.

**Thresholds:**
- $CLS \leq 1.5$: ✅ Smooth progression
- $1.5 < CLS \leq 2.5$: ⚠️ Review — may need an intermediate node
- $CLS > 2.5$: ❌ REJECT — mandatory bridge insertion

**Example (Thread B before fix):**
- P3-N3 complexity: 1.8
- ROSYTH-P6-ALG-02 complexity: 3.8
- CLS = $|3.8 - 1.8| = 2.0$ ⚠️ — should have triggered a review

**Example (Thread B after fix):**
- P3-N3 complexity: 1.8
- P4-M3 complexity: 2.5 → CLS = 0.7 ✅
- P4-M3 complexity: 2.5
- ROSYTH-P6-ALG-02 complexity: 3.8 → CLS = 1.3 ✅

### Rule 3: The Three-Part Bridge Test (NEW)
Every vertical thread from Seed to Boss must pass three checks:

1. **KNOW** — Does a node exist that teaches the student the underlying concept? (Concept Node)
2. **DO** — Does a node exist that teaches the student to APPLY the concept as a procedure? (Action Node)  
3. **ABSTRACT** — Does a node exist that teaches the student to GENERALISE the procedure to new contexts? (Transfer Node)

For Thread B:
- **KNOW:** P3-N3 (Difference is constant) ✅
- **DO:** P4-M3 (Remove the difference, then divide equally) ✅ ← THIS WAS MISSING
- **ABSTRACT:** ROSYTH-P6-ALG-02 (Substitute $b+y$, solve algebraically) ✅

### Rule 4: Auditor Pre-Flight (UPDATED)
Before ANY Boss node is marked as "EXTRACTED," the Auditor MUST run the following checks on its vertical thread:

1. ☐ Verb Test passes for every bridge node
2. ☐ Cognitive Leap Score between ALL adjacent pairs is ≤ 1.5 (or flagged)
3. ☐ Three-Part Bridge Test (KNOW / DO / ABSTRACT) is satisfied
4. ☐ No bridge node is a "concept orphan" (concept without a paired action)
5. ☐ Death List compliance verified at every level

**If any check fails, the Boss node status must be set to "THREAD INCOMPLETE" and the Ingestor is tasked with forging the missing bridge.**

### Rule 5: Forge-Before-Extract (NEW)
**Mandate:** No new P6 Boss node may be extracted from exam papers UNTIL its full vertical thread (Seed → Bridge(s) → Boss) has been pre-mapped and verified.

**Workflow change:**
1. Architect maps the expected thread FIRST (top-down)
2. Auditor validates the thread using Rules 1-4
3. ONLY THEN does the Ingestor extract the Boss node from the PDF

This prevents "orphan Boss" nodes that lack proper pedagogical scaffolding.

---

## Summary of Process Changes

| Before (v1.0) | After (v2.0) |
| :--- | :--- |
| "Link Boss to a Seed" | "Build a KNOW → DO → ABSTRACT chain" |
| No leap measurement | Cognitive Leap Score with thresholds |
| Concepts accepted as bridges | Verb Test: actions required |
| Extract first, thread later | Forge-Before-Extract: thread first |
| Auditor checks axes only | Auditor Pre-Flight: 5-point thread validation |

---

*These rules are retroactive. All existing threads must be re-validated against v2.0 before Batch 02 proceeds.*
