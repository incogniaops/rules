# Writing rules for `bmail`

## Purpose
Define standards for generating business email drafts in English using templates and functional phrases inspired by `docs/business_email.pdf`.

## Mandatory base structure
Every generated email must include:
1. **Subject** — specific and actionable.
2. **Opening** — with contextual reference.
3. **Core message** — with concrete information.
4. **Action request** — clear (if applicable).
5. **Polite close** — with next step.

## Tone and style
- Professional and courteous, without ambiguous language.
- Short, direct sentences.
- Avoid long paragraphs; prefer blocks of 2–4 lines.
- Use action verbs: confirm, send, review, advise, clarify.

## Content rules
- One email = one main intent.
- Include a reference (order ref, invoice, date, or meeting) when one exists.
- If there is a delay or problem, include:
  - acknowledgement of the problem,
  - apology,
  - brief cause,
  - corrective action,
  - new time commitment.

## Recommended model phrases (from the book)
- "Thank you for your email of 14 June."
- "I am writing in reference to your advertisement in yesterday's New York Times."
- "I am writing with reference to your enquiry of 6 November."
- "Please could you confirm the deadline?"
- "Would you please email me further information about..."
- "We regret to inform you that...."
- "Unfortunately, we are unable to…"
- "Please accept my apologies for this."
- "Once again please accept my apologies for any inconvenience caused."

## Standard placeholders
Use placeholders in UPPERCASE with curly braces:
- `{SUBJECT}`
- `{RECIPIENT_NAME}`
- `{RECIPIENT_COMPANY}`
- `{REFERENCE}`
- `{CONTEXT}`
- `{MAIN_REQUEST}`
- `{DETAILS}`
- `{DEADLINE}`
- `{NEXT_STEP}`
- `{SENDER_NAME}`
- `{SENDER_ROLE}`

## Available templates
- `opening_reference_template.html`
- `enquiry_template.html`
- `informing_good_news_template.html`
- `informing_bad_news_template.html`
- `apology_delay_template.html`
- `order_status_template.html`
- `meeting_request_template.html`
