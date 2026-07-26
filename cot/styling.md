---
domain: writing
task: correctly apply the rules of STYLING.md in a corporate Markdown document
dificultad: medium
longitud_objetivo: medium
validacion: correct header/footer, valid CST timestamp, structure and styles conforming to STYLING.md
---
<!-- markdownlint-disable MD041 -->

Reasoning:

- Use International English (UK) and repo CoT format (see «~/rules/rulesets/LINGUISTICS.md» ([../rulesets/LINGUISTICS.md](../rulesets/LINGUISTICS.md)), «~/rules/rulesets/STYLING.md» ([../rulesets/STYLING.md](../rulesets/STYLING.md)) and «~/rules/README.md» ([../README.md](../README.md))).
- Traverse top to bottom: standard header → content → footer → CSS → validations (timestamps, links, accessibility).
- Ensure consistency with CST (México City) and mermaid where applicable.

Steps:

1) Action: insert the standard header following «~/rules/STYLING.md» (tags + logo + H1 + right-aligned timestamp).
   Result: YAML block with tags and header block with Kabat One logo and H1 title.
2) Action: detect and remove existing date fields before inserting the new timestamp.
   Validation: locate and clean patterns such as `Last modified:`, `Date:`, `Report date:`, and `[time=...]` to avoid duplication.
   Result: the document retains a single visible date field.
2b) Action: generate and validate the «Last modified» timestamp in CST (24 h).
   Result: `TZ=America/Mexico_City date '+%d %B %Y, %H:%M (CST)'` produces, e.g., «31 July 2025, 11:59 (CST)».
3) Action: review content structure (H2→H3→H4) and avoid heading level skips.
   Result: clear hierarchy; titles in sentence case and without a trailing full stop.
4) Action: apply LINGUISTICS rules to terms and quotes.
   Result: «AI», «IT», standard quotes, loanwords in italics.
5) Action: remove unnecessary `---` separators (CRITICAL RULE — AI-generated documents tend to overuse them).
   Step 5a: run `grep -n "^---$" <file>` to locate ALL occurrences.
   Step 5b: keep only:
     - The YAML frontmatter block (lines 1 and 3)
     - The `---` immediately before the signature image in the footer
   Step 5c: remove WITHOUT EXCEPTION all other `---`. No H2, table, code block, or paragraph should be separated with `---`.
   Result: zero `---` in the body; exactly one just before the footer.
6) Action: insert the standard footer with the single separator, corporate signature, and corporate CSS.
   Result: footer with official signature image, corporate colours, and consistent styles.
7) Action: validate links and images.
   Result: URLs work; add alternative text to images.
8) Action: review accessibility and responsive behaviour.
   Result: legible styles, sufficient contrast, correct tables.
9) Action: verify mermaid where diagrams are required.
   Result: ````mermaid` blocks conforming to spec; no ASCII diagrams.
10) Action: validate consistency with linters.
    Result: markdownlint (headings/line length) and Vale (style/en_GB) pass without errors.
11) Action: when editing the file with `edit_files`, always anchor from the start of the line.
    Rule: when `search_start_line_number` is specified, the `search` field MUST begin at the first character of that line. Anchoring mid-line always fails, regardless of the line number or file encoding.
    Result: all edits apply without search errors.

Conclusion:

- Deliver the document with correct header/footer, valid CST timestamp, hierarchical content, and consistent style.
- Confirm the single-date policy: no redundant date remains after styling.
- References: «~/rules/rulesets/STYLING.md» ([../rulesets/STYLING.md](../rulesets/STYLING.md)), «~/rules/rulesets/LINGUISTICS.md» ([../rulesets/LINGUISTICS.md](../rulesets/LINGUISTICS.md)) and «~/rules/README.md» ([../README.md](../README.md)).
