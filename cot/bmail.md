---
domain: workflow
task: draft business emails in English using templates and model phrases from the Business Email book
dificultad: medium
longitud_objetivo: medium
validacion: HTML generated with complete placeholders, professional tone, and clear action
---
<!-- markdownlint-disable MD041 -->

Reasoning:

- The goal of `bmail` is to accelerate the drafting of professional emails in English.
- Thematic templates and phrase banks derived from `docs/business_email.pdf` will be used.
- The output must be reusable as an editable draft with a consistent structure:
  clear subject, contextual opening, actionable body, and courteous close.

Steps:

1) Action: identify the type of email requested.
   - opening, enquiry, informing-good, informing-bad, apology-delay, order-status, meeting-request.
   Result: target template selected.

2) Action: gather minimum required data.
   - Subject, recipient, context, order/information detail, deadline or next step.
   Result: required fields complete.

3) Action: select model phrases from the bank.
   - Prioritise functional phrases (referencing, requesting, apologising, informing).
   - Avoid extensive mechanical copying; adapt to the specific context.
   Result: candidate phrases integrated into the draft.

4) Action: substitute placeholders in the HTML template.
   Result: complete email with consistent structure.

5) Action: review clarity and tone.
   - One main request per email.
   - Professional, direct, and courteous tone.
   - Close with expected action or confirmation.
   Result: draft ready for review/sending.

6) Action: save file with naming convention.
   - `YYYY-MM-DD-bmail-{template-key}-{subject-slug}.html`
   Result: file saved at the agreed path.

Conclusion:

- `bmail` transforms book examples into actionable templates.
- The focus is speed + consistency + contextual personalisation.
