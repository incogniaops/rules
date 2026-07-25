# Style rules

This document defines the style conventions for Markdown documents in different contexts.

## Document structure

### Section order

1. **Metadata and header** — tags, logos, and main titles
2. **Main content** — development of the topic
3. **Footer** — licence and contact information
4. **CSS styles** — appearance definitions (if applicable)

## HedgeDoc

Markdown documents for HedgeDoc (no licence, corporate signature only).

### Standard header

Every HedgeDoc document must include the following header:

```markdown
---
tags: tag-1, tag-2, tag-3, tag-opcional
---

<img src="https://hedgedoc.promad.com.mx:31418/uploads/9217e5d8-2a84-4e41-9634-ea3b5a6bd45a.png" class="logo-light" alt="Kabat One logo">

<img src="https://hedgedoc.promad.com.mx:31418/uploads/e0f5ef2b-4519-48ee-bd2d-16013c7f44c4.png" class="logo-dark" alt="Kabat One logo">

# First level-one heading

<div style="text-align: right;"><em>Última modificación: 31 de julio de 2025, 11:59 (CST)</em></div><br>

```

**Important notes:**
- Tags must be descriptive and relevant to the content
- The Kabat One logo is mandatory in corporate documents
- The `<div style="text-align: right;">` block works **only in HedgeDoc**; GitLab and GitHub strip `style` attributes
- The first heading must be clear and concise
- The "Última modificación" date must be updated with the real date and time when editing the document (format: DD de mes de AAAA, HH:MM (CST))
- **Single-date rule:** before inserting/updating "Última modificación", remove any date field already present (`Fecha:`, `Fecha de reporte:`, `[time=...]`, or another "Última modificación") so that only one remains
- **Mandatory timezone:** always use CST from México City (UTC-6), never UTC or any other timezone

⚠️ **CRITICAL WARNING:** To generate correct CST timestamps, adding "CST" to a UTC date is not sufficient. You must subtract 6 hours from UTC to obtain the correct CST time. For example, if UTC is 22:21, CST must be 16:21 (22:21 − 6 hours = 16:21). Using `TZ="America/Mexico_City" date` guarantees automatic conversion.

**Timestamp generation examples (CST, 24-hour):**

```bash
# Short format (ISO-like): 2025-07-31 11:59 CST
TZ=America/Mexico_City date '+%F %H:%M %Z'

# Long format in Spanish: 31 de julio de 2025, 11:59 (CST)
LC_TIME=es_MX.UTF-8 TZ=America/Mexico_City date '+%d de %B de %Y, %H:%M (%Z)'
```

### Standard footer

Every HedgeDoc document must conclude with the following footer (no licence):

```markdown
---

![FIRMA](https://hedgedoc.promad.com.mx:31418/uploads/010e09ff-5e2d-4ba8-828b-850a1424eafa.png)

[//]: # (CSS Corporativo)

<style>
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&family=Space+Grotesk:wght@300;400;500;600;700&display=swap');
  :root {
    --midday: #00A1FF;
    --midnight: #24326A;
    --ice: #C3D8F3;
    --connect: #31D8FF;
    --code: #007EB5;
    --deep: #060E40;
    --video: #7252D8;
  }
  a {
    color: var(--midday);
  }
  a:visited {
    color: var(--video);
  }
  a:hover {
    color: var(--connect);
    text-decoration: none;
  }
  .markdown-body {
    font-family: 'Space Grotesk', sans-serif;
  }
  .markdown-body h1,
  .markdown-body h2,
  .markdown-body h3,
  .markdown-body h4 {
    font-family: 'Montserrat', sans-serif;
  }
  .markdown-body h1 {
    border-bottom: 1px solid var(--midday);
  }
  .markdown-body p {
    text-align: justify;
  }
  .markdown-body hr {
    height: 1px;
    background-color: var(--midday);
  }
  .logo-dark {
    display: none;
  }
  .night .logo-light {
    display: none;
  }
  .night .logo-dark {
    display: block;
  }
</style>
```

**Footer components:**

1. **Separator** — horizontal rule
2. **Corporate signature** — official signature image
3. **Corporate CSS** — brand colour and style definitions

### Corporate colour palette

| Variable | Colour | Hexadecimal | Use |
|----------|--------|-------------|-----|
| `--midday` | Kabat One blue | `#00A1FF` | Primary brand colour |
| `--midnight` | Navy | `#24326A` | Links (light mode) |
| `--ice` | Ice | `#C3D8F3` | Hover in dark mode |
| `--connect` | Connect | `#31D8FF` | Complementary accent |
| `--code` | Code | `#007EB5` | Secondary accent |
| `--deep` | Deep | `#060E40` | Very dark blue |
| `--video` | Video | `#7252D8` | Visited links |

### Format rules

#### Headings

- H1 headings have a bottom border in the PROMAD colour
- Use clear hierarchy: H1 → H2 → H3 → H4
- Avoid skipping heading levels

#### Text

- Paragraphs are justified by default
- Links change colour on hover
- Automatic support for light and dark mode

#### Separators

- Horizontal rules (`---`) use the PROMAD colour
- Fixed height of 1px for visual consistency

## Platform syntax differences

HedgeDoc supports extensions that **do not work** in GitLab or GitHub:

| Feature | HedgeDoc | GitLab | GitHub |
|---------|----------|--------|--------|
| `[TOC]` table of contents | ✅ | ❌ | ❌ |
| `:::` admonition blocks (`:::info`, `:::warning`, etc.) | ✅ | ❌ | ❌ |
| `[name=Author]` author metadata | ✅ | ❌ | ❌ |
| `[time=date]` date metadata | ✅ | ❌ | ❌ |
| `[color=#hex]` text colour | ✅ | ❌ | ❌ |
| Native `mermaid` blocks | ✅ | ✅ | ✅ |
| Inline CSS (`<style>`) | ✅ | ❌ (ignored) | ❌ (ignored) |
| Arbitrary HTML | ✅ | partial | partial |
| Badges (`shields.io`) | ✅ | ✅ | ✅ |
| YAML frontmatter (`---`) | ✅ (`tags:`) | ✅ (`title:`, `description:`) | ✅ (horizontal table) |

**Critical rule:** when applying styling in GitLab or GitHub, remove or adapt any HedgeDoc-exclusive syntax.

## Templates

Use the templates in `templates/` as a starting point:

- `templates/hedgedoc.md` — generic document for HedgeDoc
- `templates/gitlab-readme.md` — README.md for GitLab (with licence and badges)
- `templates/github-readme.md` — README.md for GitHub (with licence and badges)

## GitLab

Markdown documents for GitLab (README.md with licence, other documents without licence).

**README.md header:** with YAML frontmatter (`title` + `description`) + H1 + timestamp in plain Markdown.

GitHub renders frontmatter as a horizontal table. GitLab renders it as a formatted code block. Both display it at the start of the document.

**Other document header:** no frontmatter. H1 + timestamp in plain Markdown only.

```markdown
---
title: "Project name"
description: "Brief project description"
---

# Project name

*Última modificación: DD de mes de AAAA, HH:MM (CST)*
```

> ⚠️ Do not use `<div style="...">` — GitLab and GitHub strip `style` attributes.
> The `title` and `description` fields are the standard for both platforms; do not use `tags` (HedgeDoc-exclusive).
> Single-date rule: keep only one `*Última modificación: ...*`; remove any redundant prior dates.

**README.md footer:**

Copyright only. No signature, no CSS:

```markdown
---

*Este proyecto fue elaborado por Rodrigo Álvarez (@incognia) y se distribuye bajo la licencia GPLv3. Para más detalles, consulta el archivo LICENSE.*

*Copyright © AAAA, Rodrigo Ernesto Álvarez Aguilera. Este es software libre bajo los términos de la GNU General Public License v3.*
```

For MIT:

```markdown
---

*Este proyecto fue elaborado por Rodrigo Álvarez para Promad Business Solutions y se distribuye bajo la licencia MIT. Para más detalles, consulta el archivo LICENSE.*

*Copyright © AAAA, Rodrigo Ernesto Álvarez Aguilera (@incogniadev).*
```

**Footer for other documents:** no footer.

### Badges in README.md

When README.md includes a licence, badges must be included at the start of the content (after the timestamp and before the first paragraph). If badges already exist, verify they are correct and up to date.

**MIT licence badge:**
```markdown
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
```

**GPLv3 licence badge:**
```markdown
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
```

**Additional recommended badges by platform:**

GitLab:
```markdown
[![pipeline status](https://gitlab.com/<namespace>/<repo>/badges/<branch>/pipeline.svg)](https://gitlab.com/<namespace>/<repo>/-/pipelines)
[![coverage](https://gitlab.com/<namespace>/<repo>/badges/<branch>/coverage.svg)](https://gitlab.com/<namespace>/<repo>/-/commits/<branch>)
```

GitHub:
```markdown
[![CI](https://github.com/<owner>/<repo>/actions/workflows/<workflow>.yml/badge.svg)](https://github.com/<owner>/<repo>/actions)
```

**Badge rules:**
- The licence badge is mandatory when `mit` or `gpl` is specified
- Badges go after the timestamp and before the first content paragraph
- If the README already has badges, verify they match the licence and current project state
- Only include CI/coverage badges if the project has them configured

## GitHub

Markdown documents for GitHub (README.md with licence, other documents without licence).

**Header:** identical to GitLab: H1 + timestamp in plain Markdown (`*Última modificación: ...*`). No `<div style>`, no logo, no YAML frontmatter.
Apply the same single-date rule: remove existing reported dates before inserting the final timestamp.

**Footer:** identical to GitLab (copyright only in README.md, no signature or CSS).

## Best practices

### Content structure

1. **Appropriate metadata**: use descriptive and relevant tags
2. **Optimised images**: prefer stable links for logos
3. **Accessibility**: include alternative text on images
4. **Responsive**: CSS must work at different screen sizes

### Maintenance

- **Update links**: periodically verify that image URLs work
- **Consistency**: maintain the same format across all documents
- **Versioning**: document significant style changes

### Context adaptations

- **Technical documents**: include Mermaid diagrams when needed
- **Internal documents**: use the full footer
- **Public documents**: evaluate which contact information to include

## Validation

Before publishing a document, verify:

- [ ] Header with Kabat One logo and appropriate tags
- [ ] Correct heading hierarchy
- [ ] Footer with corporate signature
- [ ] Corporate CSS included and functional (if applicable)
- [ ] Links and images working correctly
- [ ] Format consistent with other project documents
- [ ] Only one visible date field (`Última modificación`), no redundant dates
- [ ] Licence only in README.md (MIT or GPLv3)
- [ ] Correct platform (HedgeDoc/GitLab/GitHub)

## Editing with `edit_files`

**Critical anchor rule:** when using `search_start_line_number`, the `search` field must begin at the first character of that line. Anchors that start mid-line always fail, regardless of the line number or file encoding.

- **Correct**: start the `search` from the beginning of the target line, including enough unique content to cover the fragment to replace.
- **Incorrect**: use as anchor a fragment that appears after the first character of the line.

When the fragment to replace is in the middle of a line, include in `search` everything from the beginning of that line, and in `replace` reproduce the full line with the correction applied.

---

*Written by Rodrigo Álvarez (@incognia)*
