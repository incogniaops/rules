---
domain: writing
task: correctly apply LINGUISTICS.md rules to a Markdown document
dificultad: media
longitud_objetivo: media
validacion: findings list + proposed corrections aligned with es_MX and typographic rules
---
<!-- markdownlint-disable MD041 -->
Reasoning:

- Main rule: content in Mexican Spanish must avoid English calques and non-Mexican regionalisms (see `~/rules/rulesets/LINGUISTICS.md` and `~/rules/PROMPTS.md`).
- Review from general to specific: dialect/es_MX → calques → terminology → technical verbs → italics for loanwords → typography (titles and post-colon casing) → quotes (text vs code) → writing subtleties → acronyms → tense usage → dates/times (CST) → file naming → explicit anti-patterns → idiomatic expressions (usage/moderation) → International English spelling where applicable.
- Produce concrete findings and minimal corrected wording where needed.

Steps:

1) Action: verify dialect and regionalisms.
   Result: flag peninsular forms (`ordenador`, `fichero`, `vale`), Argentinian forms (`piola`), Colombian forms (`bacano`), and other regionalisms (`chévere`), then replace with es_MX equivalents (`computadora`, `archivo`, `está bien`, `excelente`, etc.).
2) Action: avoid common English calques.
   Result: prefer `hacer/ejecutar` (instead of calqued `realizar`), `aplicar/poner en práctica` (instead of `implementar` when used as calque), `admitir/permitir` (instead of `soportar`), `cambios incompatibles` (instead of `cambios rompedores`), and other native alternatives.
3) Action: normalise priority technical terminology.
   Result: use `IA`, `TI`, `computadora`, `archivo`, `carpeta`, `aplicación`, `almacenamiento`, `predeterminado`, `clúster`, `métricas`, `nodo`.
4) Action: review technical verbs.
   Result: use `desplegar`, `respaldar`, `compilar`, `depurar`, `probar/poner a prueba`, `confirmar cambios`, `reflejar`, `hacer clic`, `descargar`; avoid -ear Spanglish forms (`commitear`, `deployear`, `buildear`, etc.).
5) Action: apply italics to technical loanwords.
   Result: use italics for *commit*, *pull request*, *pipeline*, *container*, *render*, *stack*, *bare-metal*.
6) Action: review title and heading typography.
   Mandatory command: `grep -n "^#" archivo.md` to list all H1-H6 headings.
   Validation: review every heading line individually and correct Title Case misuse.
   Result: sentence case only (first word and proper nouns capitalised), no trailing full stop; after colons, lowercase unless proper noun.
   Critical: do not mark this step complete without documenting each heading and applied correction.
7) Action: validate quotes (text vs code).
   Result: use «» in prose and "" only in code/script comments; confirm code examples keep double quotes where needed.
8) Action: review writing subtleties.
   Result: avoid starting sentences with numerals where possible; avoid ending paragraphs with symbols/abbreviations when a full term is clearer; rewrite when needed.
9) Action: review acronyms.
   Result: keep acronyms invariable (e.g. VM, not VMs); use numerals or phrasing such as `instancias de VM` for clarity.
10) Action: validate tense usage.
    Result: reports in first-person past tense; guides in second person (imperative/present/future); avoid impersonal third person (`se configuró...`).
11) Action: validate dates and times (México City CST).
    Result: use 24-hour format and `TZ=America/Mexico_City`; never label UTC time as CST. In CHANGELOG: date only `[YYYY-MM-DD]`.
12) Action: validate file naming.
    Result: filenames in International English; Markdown files in `UPPERCASE_NAMES.md` (lowercase extension).
13) Action: apply explicit anti-pattern filters.
    Result: reject `librería` (for `biblioteca`), `IT`, peninsularisms, -ear verbs, Every-Word-Capitalised headings, uppercase after colons, pluralised acronyms, and impersonal third person.
14) Action: assess Mexican idioms.
    Result: allow in internal informal contexts; moderate in formal/corporate documents; keep es_MX consistency.
15) Action: validate International English (UK) spelling in English segments.
    Result: replace American spellings in English text (`color`→`colour`, `organization`→`organisation`, `virtualization`→`virtualisation`).

Mandatory verification (before completion):

- Run `grep -n "^#" archivo.md` and document every heading found.
- Confirm no heading remains in Every-Word-Capitalised style.
- List all capitalisation fixes applied.
- Validate proper italics for technical loanwords (*stack*, *commit*, etc.).
- Verify all identified English calques were corrected.
- Verify all English content uses International English (UK) spelling.

Conclusion:

- Deliver: (a) findings list and proposed replacements; (b) corrected fragments with proper quotes and capitalisation; (c) if timestamps appear, provide correct TZ examples; (d) note whether idiomatic expressions were kept or moderated.
- References: `~/rules/LINGUISTICS.md`, `~/rules/README.md`, and `~/rules/PROMPTS.md`.
