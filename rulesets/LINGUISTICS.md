# Mexican Spanish linguistic rules as reference standard

## Main rule

**All content must be written in Mexican Spanish, avoiding English calques and regionalisms from other Spanish variants.**

---

## Use Mexican Spanish

### Technical terms

- **«IA»** (not «AI»)
- **«Biblioteca»** (not «librería») [CRITICAL]
- **«TI»** (not «IT»)
- **«Computadora»** (not «ordenador» or «computador»)
- **«Archivo»** (not «fichero»)
- **«Carpeta»** (not «directorio»)
- **«Aplicación»** (not «app» or «aplicativo»)
- **«Almacenamiento»** (not «storage»)
- **«Predeterminado»** (not «por defecto»)
- **«Clúster»** (not «cluster») — with accent in Spanish
- **«Métricas»** for observability data

### Spelling when the text is in English

- If a section is written in English, use **International English (UK)**.
- Avoid American spelling.
- Preserve accent marks in proper nouns even in English text.
- Mandatory exceptions:
  - ✅ `México` (including `México City`)
  - ✅ `Álvarez`
- Mandatory examples:
  - ✅ `colour` / ❌ `color`
  - ✅ `organisation` / ❌ `organization`
  - ✅ `virtualisation` / ❌ `virtualization`
  - ✅ `optimisation` / ❌ `optimization`
  - ✅ `standardised` / ❌ `standardized`

### Technical verbs

- **«Desplegar»** (not «deployar»)
- **«Respaldar»** (not «backupear»)
- **«Compilar»** (not «buildear»)
- **«Depurar»** (not «debugear»)
- **«Probar / poner a prueba»** (not «testear»)
- **«Confirmar cambios»** (not «commitear»)
- **«Reflejar»** (not «mirrorear»)
- **«Hacer clic»** (not «clickear»)
- **«Descargar»** (not «bajar» in technical docs)

### Technical loanwords: use italics

- **«Hacer *commit*»**
- **«*Pull request*»**
- **«*Pipeline* de CI/CD»**
- **«*Container*»**
- **«*Render*»**
- **«*Stack* tecnológico»**
- **«*bare-metal*»**

---

## Avoid

### Common English calques

- ❌ «AI» → ✅ «IA»
- ❌ «Realizar» (as perform calque) → ✅ «Hacer / ejecutar / llevar a cabo»
- ❌ «Actualmente» (as currently calque) → ✅ «Ahora / en este momento»
- ❌ «Eventualmente» (as eventually calque) → ✅ «Finalmente / al final / en algún momento»
- ❌ «Soportar» (as support calque) → ✅ «Admitir / permitir»
- ❌ «Implementar» (as implement calque) → ✅ «Aplicar / poner en práctica»
- ❌ «Cambios rompedores» → ✅ «Cambios incompatibles»

### Peninsular Spanish

- ❌ «Ordenador» → ✅ «Computadora»
- ❌ «Fichero» → ✅ «Archivo»
- ❌ «Vale» → ✅ «Está bien / de acuerdo»

### Other regionalisms

- ❌ «Piola», «bacano», «chévere», «pana» → ✅ use natural Mexican Spanish alternatives

---

## Mexican idiomatic expressions

Use idioms only when context allows it.

### Appropriate contexts

- Internal informal conversations
- Personal project comments
- Internal team notes

### Moderate or avoid in

- Formal documentation
- International client communication
- Corporate formal presentations

---

## Typographic rules

### Titles and headings

- Use sentence case (only first word + proper nouns capitalised).
- Do not end headings with full stops.
- After a colon, use lowercase unless a proper noun follows.

Examples:
- ✅ `### Configuración de Proxmox VE`
- ❌ `### Configuración De Proxmox VE`
- ✅ **Regla:** los nombres de archivos deben estar en inglés
- ❌ **Regla:** Los nombres de archivos deben estar en inglés

### Verb tenses in documents

- Reports/postmortems: first-person past tense.
- Guides/manuals: second person (imperative/present/future).
- Avoid impersonal third person (`se configuró`, `se debe...`).

### Dates and times (CST, México City)

- Use 24-hour format and `America/Mexico_City`.
- Never label UTC as CST without conversion.
- Preferred formats:
  - `2025-07-28 14:30 CST`
  - `28 de julio de 2025, 14:30 CST (Ciudad de México)`

Shell examples:
- `TZ=America/Mexico_City date '+%F %H:%M %Z'`
- `TS=$(TZ=America/Mexico_City date '+%F %H:%M %Z'); echo "$TS"`

### Quotes

- Use angular quotes «» in Markdown prose.
- Keep double quotes "" in code and script comments.

### Writing subtleties

- Prefer not to start sentences with numerals.
- Prefer full words over symbol endings in prose (`20 por ciento`, `etcétera`).

### File naming

- Filenames and directories: International English.
- Markdown files: `UPPERCASE_NAME.md` (lowercase extension).
- Valid: `README.md`, `PHILOSOPHY.md`, `LINGUISTICS.md`
- Invalid: `readme.md`, `Philosophy.md`, `LINGUISTICS.MD`

---

## Special hard stops

The following are explicitly unacceptable:

- Using «librería» instead of «biblioteca».
- Using «IT» instead of «TI» in Spanish content.
- Using peninsular terms such as «ordenador» or «fichero».
- Invented Spanglish verbs ending in `-ear` (`commitear`, `deployear`, etc.).
- Writing `Alvarez` without accent in regular text where `Álvarez` is expected.
- Title Case in Spanish headings.
- Incorrect uppercase after colons.
- Pluralised acronyms (`VMs`, `ONGs`, etc.).
- Impersonal third-person writing in contexts requiring first/second person.

---

## Evaluation criterion

**Would this wording sound natural to a Mexican Spanish speaker with no English dependency?**

- If yes → use it.
- If no → replace with a natural Mexican Spanish alternative.

---

## Scope

These rules apply to:

- Technical documentation
- Code comments
- Scripts and tooling messages
- User-facing written communication

---

*This document was created by Rodrigo Álvarez (@incognia) and is distributed under GPLv3. For details, see LICENSE.*

**Created**: 28 July 2025 (CST, México City)
**Last updated**: 17 August 2025, 01:36 CST (México City)
**Goal**: maintain linguistic consistency with Mexican Spanish
