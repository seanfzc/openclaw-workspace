# Rendering Stack

Simple pipeline to turn problem descriptions into SVG diagrams (bar models, flowcharts, etc.) using Matplotlib (with pastel colors) and TikZ (optional).

## Quick Start

1. **Install Python dependencies** (if not already installed):
   ```bash
   pip install matplotlib pyyaml jinja2
   ```

2. **Write a problem card** (see `problem_cards/sample.yaml`):
   ```yaml
   id: Render-001
   title: "Parts A and B (2:1 ratio)"
   diagram_type: bar_model
   data:
     labels: ["Part A", "Part B"]
     values: [40, 20]
     colors: ["#FFB6C1", "#98FB98"]
   ```

3. **Render it**:
   ```bash
   python scripts/render.py problem_cards/sample.yaml
   ```

4. **Check the output** in `rendering-stack/outputs/Render-001/`:
   - `Render-001.svg` – the diagram (pastel bar chart)
   - `Render-001.md` – a descriptive note about the render
   - `Render-001.yaml` – copy of the problem card

## Structure

```
rendering-stack/
├── problem_cards/          # YAML or JSON files describing the diagram
├── templates/              # Matplotlib & TikZ templates
│   ├── bar_model.py        # Pastel bar charts (SVG)
│   ├── tikz_template.tex   # TikZ template (requires LaTeX)
│   └── render_note.md.j2   # Jinja2 template for render notes
├── scripts/
│   └── render.py           # Main render script
├── outputs/                # Generated diagrams and notes
└── README.md
```

## Templates

### Matplotlib (`bar_model.py`)
- Creates pastel-colored bar charts
- Saves directly as SVG (ideal for web)
- Customizable colors, labels, values

### TikZ (`tikz_template.tex`)
- For precise vector diagrams (flowcharts, graphs, geometric shapes)
- **Requires LaTeX installation** (e.g., `brew install basictex`)
- Can be compiled to PDF or SVG via `pdflatex` or `latexmk`

## Adding a New Diagram Type

1. Add a new template in `templates/` (e.g., `flowchart.py` or `flowchart.tex`)
2. Extend `scripts/render.py` to support the new `diagram_type`
3. Update the problem card YAML with the new type

## Integration with ATOM‑SG

Problem cards can be generated from ATOM‑SG schema (e.g., P6 math problems). The rendering stack can be called as a micro‑service to produce diagram assets.

## Next Steps

- [ ] Add TikZ compilation script (requires LaTeX)
- [ ] Support more diagram types (flowcharts, graphs, geometric shapes)
- [ ] Automate rendering in CI/CD (GitHub Actions)
- [ ] Integrate with ATOM‑SG problem card generation

## Notes

- **Pastel colors** are defined in `templates/bar_model.py` (PASTEL_COLORS list).
- **SVG is the default output format** for web compatibility.
- **LaTeX/TikZ** is optional; the stack works with Matplotlib alone.

## Troubleshooting

- **"ModuleNotFoundError: No module named 'matplotlib'"** → Run `pip install matplotlib`
- **TikZ compilation fails** → Ensure LaTeX is installed (`pdflatex --version`)
- **SVG looks blurry in browser** → SVG is vector; ensure it's not being rasterized by CSS.

---

*Built for the Rendering Stack pilot – macOS, Python 3.9, Matplotlib 3.9.4*