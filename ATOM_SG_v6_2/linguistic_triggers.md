# LINGUISTIC RADAR: P6 ALGEBRA DICTIONARY (v1.0)

## CEO ATOM: Linguistic Triggers for Auditor's Memory

These keywords serve as "tripwires" to define the Logic Axis and ensure Vertical Continuity by mapping P6 "Boss" nodes to their P1-P3 "Seed" nodes.

---

### Defined Linguistic Triggers

1.  **[CONSTANT DIFFERENCE]**
    *   **Keywords:** "Years later," "Older/Younger," "Age difference."
    *   **Logic Formulation:** $(A + x) - (B + x) = A - B$
    *   **P1-P3 Seed:** `P1-N2 Comparison (More/Less than)`

2.  **[INTERNAL TRANSFER]**
    *   **Keywords:** "Gave some to," "Exchanged," "Shifted between."
    *   **Logic Formulation:** $A + B = \text{Total (Constant)}$
    *   **P1-P3 Seed:** `P1-N1 Number Bonds (Parts of a Whole)`

3.  **[VALUE OF UNITS]**
    *   **Keywords:** "Each," "Costing," "Total Value," "Denomination."
    *   **Logic Formulation:** $(\text{Quantity} \times \text{Value}) = \text{Total}$
    *   **P1-P3 Seed:** `P2-M1 Equal Groups (Multiplication)`

4.  **[REMAINDER PIVOT]**
    *   **Keywords:** "Of the remainder," "Leftover," "Remaining."
    *   **Logic Formulation:** $x - (\frac{1}{n} \times x) = \text{New Whole}$
    *   **P1-P3 Seed:** `P1-N2 Subtraction (Taking away)`

5.  **[INCLUSIVE INTERVAL]**
    *   **Keywords:** "From... to," "Inclusive," "Number of pages."
    *   **Logic Formulation:** $(\text{End} - \text{Start}) + 1 = \text{Quantity}$
    *   **P1-P3 Seed:** `P1-N1 Counting sequences`

6.  **[REMAINDER PIVOT]**
    *   **Keywords:** "Of the remainder," "Of the remaining," "Leftover," "What was left," "Rest of," "From what remained."
    *   **Logic Formulation:** $x - (\frac{1}{n} \times x) = \text{New Whole (Remainder)}$. The remainder becomes the input for the next operation.
    *   **P1-P3 Seed:** `P1-N2 Subtraction (Taking away)` → `P3-F1-FractionOfWhole`
    *   **Chaining Pattern:** Each "of the remainder" creates a NEW whole. Track: Original → Remainder₁ → Remainder₂ → Final.
    *   **Common Trap:** Students apply the second fraction to the ORIGINAL instead of the REMAINDER. Flag for Auditor review if detected.

### ⚠️ AUDITOR TRAP: "Of the remainder" vs. "Of the total"

| Keyword Detected | Architect Visual Template | Logic |
| :--- | :--- | :--- |
| "of the remaining" / "of what was left" / "of the rest" | **Pull-down Visual Template** — bar shrinks after each take-away, new fraction applies to REDUCED bar | Remainder becomes new whole: $R_1 = x - \frac{a}{b}x$, then $\frac{c}{d} \times R_1$ |
| "of the original" / "of the total" / "of all" | **Standard Part-Whole Model** — fraction always refers to the FULL original bar | Always: $\frac{a}{b} \times x$ where $x$ is the ORIGINAL total |

**MANDATORY:** If both patterns appear in the SAME problem, the Auditor must flag for manual Architect review. Mixed-reference problems are High-Stress (VSS ≥ 4).

7.  **[FRACTIONAL TRANSFER]**
    *   **Keywords:** "Gave 1/3 of," "Spent 2/5 of," "Used a fraction of."
    *   **Logic Formulation:** $\text{Given} = \frac{a}{b} \times \text{Current Total}$; $\text{Remaining} = (1 - \frac{a}{b}) \times \text{Current Total}$
    *   **P1-P3 Seed:** `P1-N2 Subtraction` → `P3-F1-FractionOfWhole`
    *   **Distinction from Remainder Pivot:** Fractional Transfer focuses on WHAT WAS GIVEN. Remainder Pivot focuses on WHAT IS LEFT. Both may appear in the same problem.

---

### ⚠️ AUDITOR "LOGIC TRAP" PROTOCOL

CEO ATOM: Command the Auditor to flag any node containing these "High-Stress" patterns for manual review by the Architect.

*   **TRAP 1 [Units vs. Parts]:** If keyword "Ratio $1:x$" is present, verify the Architect has defined the "Value of $1$ Unit."
*   **TRAP 2 [The Pivot]:** If keyword "After giving away... had $y$ left" is present, force a link to "Working Backwards" heuristics.
*   **TRAP 3 [Constant Total]:** If keywords "Ali lost 10 and Baba gained 10" are present, ensure the Logic Axis uses $A + B = C$ (Constant Total).

---

### 🛠️ SYSTEM INSTRUCTION FOR AUDITOR

"Cross-reference all Ingestor Markdown against LINGUISTIC_TRIGGERS. If a trigger is detected but the Architect has failed to map the P1-P3 Seed Node, reject the entry for 'Double-Helix Fragmentation'."
