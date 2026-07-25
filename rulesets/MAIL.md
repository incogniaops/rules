# HTML email composition rules for Outlook Web (OWA)

## Purpose

This document defines the rules for composing HTML emails that are copied from the browser and pasted into Outlook Web App (OWA). The restrictions exist because OWA strips most CSS on paste.

## Available templates

Templates live in `templates/mail/` of this repository:

- **`delivery_template.html`** — microservice delivery (Java/Spring Boot). Has 7 *placeholders* to replace.
- **`generic_template.html`** — any other type: configuration changes, technical decisions, reports, corrections.

## Workflow

1. Copy the template with the name `YYYY-MM-DD-{short-name}.html`
2. Replace the *placeholders*
3. Deliver according to the chosen mode:
   - **`owa`**: open in browser → `Ctrl+A` → `Ctrl+C` → paste into OWA. Outlook adds the signature on send.
   - **`mac`**: open a draft in Outlook via AppleScript. Outlook injects the "Kabat One" signature. Send with ⌘+Enter.
   - **`graph`**: send via Microsoft Graph API with signature as an inline CID image. Authenticate with `~/rules/scripts/graph_auth.py`.

> Skill invocation: `/mail <owa|mac|graph> <delivery|generic> <subject>`

## Critical HTML rules

### Colour backgrounds: `bgcolor` on `<td>`, never on `<table>` alone

OWA only captures the `background-color` of the `<td>` containing the text. Also duplicate it as the HTML attribute `bgcolor`.

```html
<!-- CORRECT -->
<td bgcolor="#d4edda" style="background-color:#d4edda; padding:15px;">Content</td>

<!-- INCORRECT — background is not copied -->
<table style="background-color:#d4edda;"><tr><td>Content</td></tr></table>
```

### Container structure

Outer table (grey background `#f0f0f0`) → inner table (white background `#ffffff`, max 800px). Backgrounds go on the `<td>` elements.

### Colour boxes

The left border goes on `<table>` (`border-left:4px solid`), the background on `<td>` (`bgcolor` + `background-color`).

### Code blocks

Do not use `<pre>` (loses background on copy). Use `<td>` with `white-space:pre-wrap`.

### Inline code

`<code>` with inline styles works: `background-color:#f4f4f4; padding:2px 5px; font-family:'Courier New',monospace;`

### Data tables

Alternating rows: add `style="background-color:#f9f9f9;"` manually to each even `<tr>`. CSS `nth-child` does not work on copy.

### Images

`<img>` with `style="max-width:100%; display:block;"`.

## What OWA strips or ignores

- Full `<style>` blocks
- CSS classes
- `background-color` on `<table>` (not on `<td>`)
- `border-radius`
- `overflow-x:auto`
- `tr:nth-child(even)`
- Flexbox, Grid
- `position:absolute`
- *Media queries*

## Colour palette

### Accent colours (H1 bottom border)

- Delivery / OK status → `#00A1FF` Midday
- Correction / change → `#7252D8` Video
- Critical alert → `#E10613` Dispatch
- Technical decision → `#007EB5` Code

### Boxes

- *Success* (green): border `#8DCB3E` Safety, background `#E8F5D6`
- *Info* (blue): border `#00A1FF` Midday, background `#C3D8F3` Ice
- *Warning* (yellow): border `#FFDA00` Traffic, background `#FFF8D6`
- *Danger* (red): border `#E10613` Dispatch, background `#FCE4E5`
- Decision (dark blue): border `#007EB5` Code, background `#E0F0F5`

### Other

- Code: background `#f4f4f4`
- Table header: background `#00A1FF` Midday, white text
- Even table row: `#f9f9f9`

## Delivery template *placeholders*

- `{NOMBRE_SERVICIO}` — full microservice name
- `{PREFIJO}` — path prefix without leading slash
- `{VERSION}` — deployed version
- `{DESTINATARIO}` — developer name
- `{FECHA}` — date in long format (e.g. 21 de marzo de 2026)
- `{RAMA_BASE}` — source branch (main, DEV-1.1, etc.)
- `{DESCRIPCION}` — one sentence about what the service does

## Adjustments for Angular/Node.js

- Remove the "Análisis de código (SonarQube)" section
- *Pipeline*: 5 *stages* (no compile or SonarQube stage)
- Docker: switch to *multi-stage* Node 22 + Nginx
- Remove the Swagger UI row from the access table
- Estimated time: 5–8 min *build* + 3 min ArgoCD

## Sending via Microsoft Graph API

- Authentication: `~/rules/scripts/graph_auth.py` (cache → *refresh* → *device code flow*)
- Credentials: `~/.secrets.yaml` (key `GRAPH_API`)
- Inline signature: `~/rules/templates/mail/assets/ralvarez_firma_740.png` as a CID attachment
- Detailed documentation for the Entra registration and OAuth2 flow: `~/rules/docs/MAIL.md`

---

*Written by Rodrigo Álvarez (@incogniadev)*
