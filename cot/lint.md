---
domain: workflow
task: fix Markdown lint errors (markdownlint-cli2) in this repository
dificultad: medium
longitud_objetivo: medium
validacion: errors significantly reduced after applying corrections and re-running the linter
---
<!-- markdownlint-disable MD041 -->

Reasoning:

- Prioritise high-impact mechanical fixes (blank lines around headings/lists: MD022/MD032; fences and languages: MD031/MD040; ordered list prefixes: MD029).
- Maintain consistency with the current configuration (.markdownlint.yaml with MD013 disabled and exceptions in CHANGELOG).
- Avoid semantic changes to content; limit changes to Markdown formatting.
- Use non-interactive execution to measure progress between iterations.

Steps:

1) Action: run the linter to establish the baseline.
   Result:
   - `npx markdownlint-cli2 "**/*.md" "#node_modules"`
   - Save a summary (total errors and predominant rules) for comparison.

2) Action: fix MD022/MD032 (blank lines) in priority files.
   Result:
   - Targets: rulesets/LINGUISTICS.md, rulesets/GIT.md, rulesets/TEACHING.md, ROADMAP.md, README.md.
   - Practical rule: add a blank line after each heading and before/after lists.

3) Action: fix MD031/MD040 (code fences and language).
   Result:
   - Add a blank line before and after each ``` block.
   - Specify language (bash, text, yaml) where applicable.

4) Action: normalise ordered lists (MD029) to the 1/1/1 style.
   Result:
   - Rewrite numbered list prefixes as consistent `1.` in steps and procedures.

5) Action: convert problematic bare URLs (MD034) to links with text.
   Result:
   - Examples: DOI/arXiv → `[arXiv:2201.11903](https://arxiv.org/abs/2201.11903)`; emails → `mailto:` where applicable.

6) Action (bounded): handle special cases.
   Result:
   - CHANGELOG.md already ignores MD022/MD032/MD013/MD024 (do not change content, only maintain the exception header).
   - systemd/backups/README.md: resolve multiple H1 (MD025) by merging into one H1 and the rest as H2/H3; for literals like `backup@.service`, present them inside inline code or lists with context to avoid MD034.
   - "Developed by …" (MD036): either convert to a "Credits" subtitle or disable MD036 at the end with a local comment if the style is intentional.

7) Action: re-run the linter and measure improvements.
   Result:
   - `npx markdownlint-cli2 "**/*.md" "#node_modules"`
   - Compare errors: expect a notable reduction in MD022/MD032, MD031/MD040, MD029, MD034.

8) Action (optional): run the link checker.
   Result:
   - `npx markdown-link-check -q -c .markdownlinkcheck.json "**/*.md"`
   - Review broken links and update internal references as needed.

Conclusion:

- The set of mechanical fixes should substantially reduce linter errors and leave minimal pending items.
- If specific warnings persist (e.g. MD036 in footers), decide whether to adjust the content or document a local per-file exception.
- References: «~/rules/.markdownlint.yaml», «~/rules/CHANGELOG.md», «~/rules/README.md».
