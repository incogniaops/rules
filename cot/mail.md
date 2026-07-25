---
domain: workflow
task: compose and send OWA-compatible HTML email using templates and three delivery modes
dificultad: medium
longitud_objetivo: medium
validacion: HTML file generated with inline styles, bgcolor on td, no external CSS or classes; delivered according to the chosen mode
---
<!-- markdownlint-disable MD041 -->

Reasoning:
- Emails are composed as HTML using OWA templates with *inline* styles.
- OWA strips `<style>` blocks, CSS classes, `background-color` on `<table>`, `border-radius`, flexbox, grid, and *media queries*.
- All styling must be *inline* on `<td>` elements, duplicating `bgcolor` as an HTML attribute.
- Templates are in `~/rules/templates/mail/` (`delivery_template.html` and `generic_template.html`).
- There are three delivery modes: `owa` (copy/paste), `mac` (AppleScript + Outlook), and `graph` (Microsoft Graph API).
- Composition reference: «~/rules/rulesets/MAIL.md» ([../rulesets/MAIL.md](../rulesets/MAIL.md)).
- Graph API credentials: `~/.secrets.yaml` (key `GRAPH_API`).

Steps:
1) Action: determine the email type.
   - Microservice delivery → use `templates/mail/delivery_template.html`
   - Any other (change, decision, report, correction) → use `templates/mail/generic_template.html`
   Result: template selected.

2) Action: copy the template with the correct name.
   Result: `YYYY-MM-DD-{short-name}.html` (CST date).

3) Action: gather the required information.
   For delivery: SERVICE_NAME, PREFIX, VERSION, RECIPIENT, DATE, BASE_BRANCH, DESCRIPTION.
   For generic: TITLE, RECIPIENT, DATE, and content for each section.
   Result: data ready for substitution.

4) Action: replace *placeholders* in the HTML.
   Result: HTML with real data.

5) Action: select the accent colour according to email type.
   - Delivery/OK → `#3498db` (blue)
   - Correction/change → `#e67e22` (orange)
   - Critical alert → `#e74c3c` (red)
   - Technical decision → `#0066cc` (dark blue)
   Result: H1 `border-bottom` colour adjusted.

6) Action: if using the generic template, remove unused components.
   Optional components: summary box, information box, attention box, problem box, data table, code block.
   Result: clean HTML with no empty blocks.

7) Action: if Angular/Node.js (not Java/Spring Boot), apply adjustments.
   - Remove SonarQube section
   - Change *pipeline* to 5 *stages*
   - Docker: multi-stage Node 22 + Nginx
   - Remove Swagger UI from the access table
   Result: HTML adapted to the service *stack*.

8) Action: verify critical HTML rules before finalising.
   - [ ] All coloured backgrounds use `bgcolor` on `<td>`, not on `<table>`
   - [ ] No `<style>` blocks or CSS classes
   - [ ] Code blocks use `<td>` with `white-space:pre-wrap`, not `<pre>`
   - [ ] Alternating table rows have inline `style`, not `nth-child`
   - [ ] All styles are inline
   Result: HTML validated.

9) Action: save the HTML file.
   - Name: `YYYY-MM-DD-{short-name}.html` (CST date).
   - Location: path indicated by the user, project `mail/` folder, or `~/mail/`.
   Result: file saved.

10) Action: deliver according to the chosen mode.
    - **`owa`**: tell the user «open in browser → Ctrl+A → Ctrl+C → paste into OWA». Do not include signature (OWA adds it automatically).
    - **`mac`**: open a draft in Outlook via AppleScript (`open newMsg`, never `send`). Do not include signature (Outlook injects it). Prompt the user to send with ⌘+Enter.
    - **`graph`**: include signature as an inline CID image. Authenticate via *device code flow* with credentials from `~/.secrets.yaml` (`GRAPH_API`). Send with `POST /me/sendMail`. Also save the HTML as a backup.
    Result: email delivered or draft opened.

Conclusion:
- The resulting HTML must comply with OWA rules (`bgcolor` on `<td>`, *inline* styles, no external CSS).
- The signature is only included in the HTML when the mode is `graph` (as an inline CID image).
- In `owa` and `mac`, Outlook adds the signature automatically.
- References: «~/rules/rulesets/MAIL.md» ([../rulesets/MAIL.md](../rulesets/MAIL.md)).
