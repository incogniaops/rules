---
domain: writing
task: generate a clean, compilable corporate LaTeX document with XeLaTeX
dificultad: medium
longitud_objetivo: medium
validacion: PDF generated without errors, full-width tables, solid code blocks with rounded borders
---
<!-- markdownlint-disable MD041 -->

Reasoning:

- Use XeLaTeX as the engine (native Unicode, fontspec, emoji); never pdflatex for corporate documents.
- CRITICAL: do NOT use pandoc for direct Markdown→PDF conversion. The result is mediocre: tables without consistent width, broken-background code blocks, headers/footers impossible to control cleanly. Use the Markdown only as a content reference and write the .tex from scratch.
- The flow is: read the Markdown → download images → write .tex → compile → fix missing packages → compile again.
- Full rules reference: «~/rules/rulesets/LATEX.md» and «~/rules/rulesets/STYLING.md».
- Apply language rules from LINGUISTICS.md to document content as appropriate.

Steps:

1) Action: download images locally before writing the .tex.
   CRITICAL: XeLaTeX cannot load URLs in `\includegraphics`. Always `curl -sL URL -o file.png` and verify with `file file.png`.
   Result: images available in the same directory as the .tex.

2) Action: write the complete preamble with mandatory packages.
   Result: include in order — fontspec, geometry, parskip, microtype, xcolor (corporate palette), booktabs, tabularx, colortbl, array, tcolorbox, graphicx, hyperref, xurl, newunicodechar, titlesec, caption.
   Configure: `\arrayrulecolor{promad}` once in the preamble for all table borders.

3) Action: write the standard header.
   Result:
   - Logo with `\includegraphics[height=1.8cm]{promad-logo.png}\\`
   - Timestamp below, right-aligned: `\makebox[\linewidth][r]{\footnotesize\textit{...}}`
   - Do NOT use `\hfill` at the start of a line (it does not work).
   - Title in `\LARGE\bfseries`; subtitle in `\large` with initial capital.
   - Metadata with the `\meta{key}{value}` command.

4) Action: write sections with `\section{N. Title}` and tables with `tabularx`.
   Result: every table uses `\begin{tabularx}{\linewidth}{...}` with at least one `X` column.
   Table header with `\rowcolor{rowhead}`.
   Borders with `\toprule`, `\midrule`, `\bottomrule` — NEVER `\hline`.
   No decorative lines in section titles.

5) Action: write code blocks with the `codebox` tcolorbox environment.
   CRITICAL: do NOT use `lstlisting` directly — it leaves white lines between text and background.
   Result: `\begin{codebox}...\end{codebox}` generates a solid dark background (#2d2d2d) with rounded borders (arc=5pt).

6) Action: write the footer.
   Result: `\vfill` + `\noindent\rule{\linewidth}{0.4pt}` (thin grey line) + contact details as plain text.
   No avatar — it does not render well in LaTeX.

7) Action: compile and resolve missing packages.
   COMMAND: `xelatex -interaction=nonstopmode file.tex 2>&1 | grep -iE 'error|missing|not found'`
   CRITICAL: use single quotes in the grep pattern (zsh interprets `!` inside double quotes).
   If a package is missing: `sudo dnf install -y 'tex(name.sty)'`
   Repeat until the grep output is empty.
   Note: grep with no matches returns exit 1 — that is success, not an error.

8) Action: verify the generated PDF.
   Result: `ls -lh file.pdf` confirms a reasonable size (> 50 KB for documents with tables).
   Compile twice if the document contains internal references or a table of contents.

Conclusion:

- Deliver: clean .tex file + generated PDF + locally downloaded images.
- Verify: full-width tables, solid-background code blocks, right-aligned timestamp, no «Figure 1» on the logo.
- If a missing package is detected during compilation, install it with `dnf` and recompile — never try to omit the package.
- References: «~/rules/rulesets/LATEX.md» ([../rulesets/LATEX.md](../rulesets/LATEX.md)), «~/rules/rulesets/STYLING.md» ([../rulesets/STYLING.md](../rulesets/STYLING.md)) and «~/rules/rulesets/LINGUISTICS.md» ([../rulesets/LINGUISTICS.md](../rulesets/LINGUISTICS.md)).
