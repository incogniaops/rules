---
domain: documentation
task: update CHANGELOG.md correctly, avoiding common errors of chronological order, timezone calculation, duplication, and language mixing
dificultad: medium-high
longitud_objetivo: medium
validacion: CHANGELOG.md in reverse chronological order, correct CST dates, no duplicates, language consistent with context (personal es_MX, corporate International English)
---
<!-- markdownlint-disable MD041 -->

Reasoning:
- Main rule: CHANGELOG.md must follow reverse chronological order (most recent first) with correctly calculated CST México City dates and language by context (personal in Mexican Spanish, corporate in International English) (see «~/rules/CHANGELOG.md» ([../CHANGELOG.md](../CHANGELOG.md)), «~/rules/rulesets/LINGUISTICS.md» ([../rulesets/LINGUISTICS.md](../rulesets/LINGUISTICS.md)) and «~/rules/cot/committing.md» ([./committing.md](./committing.md))).
- Common critical errors: (1) incorrect chronological order, (2) wrong CST calculation (labelling UTC as CST), (3) duplicating identical entries, (4) mixing International English with Mexican Spanish.
- Flow: verify current timezone → review chronological order → detect duplicates → apply linguistic rules → validate structure.
- This CoT is executed via `/changelogger` before `/commit`; the `/commit` flow does not edit the changelog and only validates that a diff exists in `CHANGELOG.md`.

Steps:
0) Action: run `git --no-pager status --short` to validate all changes made before any other operation.
   MANDATORY COMMAND: `git --no-pager status --short`
   ABSOLUTE HARD STOP: if this command was not executed in the current run, stop the process and restart from 0.
   Restriction: reading the changelog, `grep`, searches, date calculation, anchor calculation, `diff`, and patches are not permitted before this step is completed and validated.
   Validation: confirm explicit visibility of the current state of the working tree.
   Result: initial change context loaded and validated.
0b) Action: read lines 1-200 of `CHANGELOG.md` before any search or edit of the file.
   MANDATORY TOOL: `read_files` on `CHANGELOG.md` with range `1-200`
   ABSOLUTE HARD STOP: if this exact read was not executed in the current run, stop the process and restart from 0.
   Restriction: `grep`, searches, date calculation, anchor calculation, `diff`, and patches are not permitted before this step is completed and validated.
   Validation: confirm the current-day heading, separation between date blocks, and the first bullet of the target block.
   Result: exact base context loaded before running `grep`, calculating anchors, or attempting patches.
0c) Action: validate the cross-cutting precondition of steps 0 and 0b before any other section.
   Validation: require explicit evidence in the current run of `git --no-pager status --short` and of the precise read of `CHANGELOG.md` (1-200).
   Stop rule: if evidence of either step is missing, IMMEDIATE HARD STOP and restart from 0; continuing or recovering mid-run is forbidden.
   Result: no subsequent section may execute without steps 0 and 0b validated.
1) Action: calculate the correct current CST date and time.
   MANDATORY COMMAND: `TZ=America/Mexico_City date +"%Y-%m-%d %H:%M:%S"`
   Validation: confirm mathematical calculation CST = UTC - 6 hours
   Result: current date in CST for new entry; never label UTC time as CST.

2) Action: review the structure and chronological order of CHANGELOG.md.
   MANDATORY COMMAND: `grep -n "^## \[" CHANGELOG.md | head -10`
   Validation: confirm dates are ordered from most recent to oldest
   Result: detect entries out of reverse chronological order.

3) Action: verify whether an entry already exists for the current CST date.
   MANDATORY COMMAND: `grep -n "^## \[${DATE_CST}\]" CHANGELOG.md`
   Critical decision:
   - If an entry for that date ALREADY EXISTS: add new typed bullets (`- feat: ...`, `- docs: ...`) INSIDE the existing entry. Do NOT create a new heading.
   - If it does NOT exist: create a new heading `## [YYYY-MM-DD] - Descriptive title` in the correct position (above all existing entries).
   Result: never two headings with the same date in the CHANGELOG.

4) Action: validate language consistency in the new entry.
   Validation: apply rules from ~/rules/rulesets/LINGUISTICS.md according to context.
   Result:
   - Personal: Mexican Spanish without English calques, angular quotes «», correct technical terminology.
   - Corporate: consistent International English.

5) Action: verify heading format.
   Required format: `## [YYYY-MM-DD] - Descriptive title`
   Validation: date only, no time component; title in sentence case (first word capitalised + proper nouns)
   Result: heading compliant with the established format.
6) Action: organise changes into typed bullets within the date entry.
   Format of each bullet:
   - Personal: `- tipo: descripción`
   - Corporate: `- type: description`
   Validation: do not use subheadings `### type`; use direct bullets with type prefix
   Result: compact entry consistent with the format of the operations-it repos.

6b) Action: insert bullets in reverse chronological order within the date entry.
   CRITICAL RULE: the new bullet goes FIRST within the date block.
   MANDATORY EDITING TECHNIQUE for `edit_files`:
   - GOLDEN RULE: `search` ends on the LAST LINE to be used as anchor. `replace` reproduces that line intact and ADDS the new content BEFORE or AFTER it. NEVER include in `search` a line that is then reproduced truncated or modified in `replace`.
   - MANDATORY OPERATIONAL RULE for existing date: direct, simple edit in a single hunk; once the target block is identified, do not repeat exploratory searches.
   - CROSS-CUTTING HARD STOP: if at any section evidence of steps 0 or 0b is absent from the current run, stop immediately and restart from 0; no exceptions exist.
   - MANDATORY FIRST ATTEMPT for existing date: use exact micro-block in a single hunk with `search` = `## [DATE] - ...` + immediate blank line + first existing bullet.
   - In that same hunk, `replace` reproduces the heading and blank line intact, inserts the new bullet at the top, and preserves the previous bullet below.
   - Partial anchors for existing dates are forbidden (e.g., `search` with heading only).
   - Inserting a blank line between bullets of the same date block is forbidden.
   - For existing dates, anchoring `search` on `# Changelog` or including that heading in the insertion hunk is forbidden.
   - Replacing the top section of the file to insert bullets in an existing date is forbidden.
   - INCREMENTAL INSERTION MODE (MANDATORY): by default only additions (`+`) are permitted. If any deleted line (`-`) appears in `CHANGELOG.md`, abort the patch and reconstruct the anchor; deletions are permitted only with explicit user instruction.
   - To insert a new `## [DATE]` entry at the top of the file: `search` is ONLY the immediately preceding anchor line (e.g. the `<!-- markdownlint-disable -->` comment or the blank line that follows it). `replace` reproduces that exact anchor line and adds the new entry after. NEVER include the first existing `## [DATE]` in `search` unless it is reproduced FULLY and INTACT in `replace`.
   - MANDATORY FALLBACK (two hunks) for a new date when the blank line before the next heading is missing:
     - Hunk 1: insert the `## [DATE]` block with its bullets above the next `## [PREVIOUS_DATE]`.
     - Hunk 2: use the next heading `## [PREVIOUS_DATE]` as anchor and replace it with `blank line + the same heading` to force the separator.
   - Repeating the same insertion patch (`+6`) when the preview still shows no blank separator is forbidden.
   - If `search` fails, read the file with `read_files` to obtain the exact content before retrying.
   Result: typed bullets ordered chronologically within each date, with new bullet at the top.

6c) Action: validate the diff immediately after each edit.
   MANDATORY COMMAND: `git --no-pager diff -- CHANGELOG.md`
   Mandatory acceptance criterion:
   - In incremental insertion mode: only added lines (`+`) in the target date block.
   - Zero deleted lines (`-`) across all of `CHANGELOG.md`, unless the user explicitly instructed a deletion.
   - NEVER edit lines outside `DATE_CST` (current day) unless the user explicitly instructs it.
   Failure management:
   - If validation fails: re-read the exact block and correct once with a minimal edit.
   - If any `-` appears in the diff during an incremental insertion: abort that attempt and reconstruct the anchor before retrying.
   - If `DATE_CST` already exists and only a bullet is being added: maintain a single hunk with the exact micro-block (`heading + blank line + first bullet`); do not use the two-hunk fallback.
   - If a new date is being created and the preview shows the blank line before the next `## [DATE]` is missing: apply the two-hunk fallback immediately; do not repeat the same insertion patch.
   - If the diff shows historical changes outside `DATE_CST`: stop and request confirmation; auto-correcting entries outside the current day is forbidden.
   - If it fails again: stop and request user confirmation before any further attempt.
   - Chaining 3 or more consecutive attempts on CHANGELOG without an intermediate successful diff validation is forbidden.
   Result: minimal, traceable changes with no side effects.
7) Action: review text in the target date block (`DATE_CST`).
   MANDATORY COMMAND: `grep -A 20 '^## \[${DATE_CST}\]' CHANGELOG.md` to review the current entry
   Validation: detect language mixing, calques, and regionalisms inconsistent with the active context, ONLY in the current day's block
   Result: adjust only the new bullets in `DATE_CST`; report historical inconsistencies without editing them.

8) Action: apply typographical rules.
   Validation: em dash in titles, angular quotes in text, italics for technical loanwords
   Result: *commit*, *pipeline*, *stack* in italics; «code» in angular quotes.

9) Action: verify final structure.
   MANDATORY COMMAND: `head -30 CHANGELOG.md` to review the first entries
   Validation: reverse chronological order, consistent format, homogeneous language
   Result: CHANGELOG.md correctly ordered with new entry in the appropriate position.

10) Action: verify precondition for `/commit` after updating the changelog.
    RECOMMENDED COMMANDS:
    - `git --no-pager diff -- CHANGELOG.md`
    - `git --no-pager diff --cached -- CHANGELOG.md`
    Validation: at least one change in `CHANGELOG.md` (staged or unstaged) must exist to pass the `/commit` gate.
    Result: changelog ready to proceed with `/commit` without further edits.

CRITICAL VERIFICATION (before completing):
- Confirm: `TZ=America/Mexico_City date` executed for real CST date
- Validate: reverse chronological order with `grep "^## \[" CHANGELOG.md`
- Verify: no duplicates by counting identical headings
- Review language by context:
  - Personal: 100% Mexican Spanish
  - Corporate: 100% International English
- Check: heading format `[YYYY-MM-DD] - Descriptive title`
- Check: bullets with correct prefix by context (`tipo:` personal / `type:` corporate) and absence of `### type` subheadings
- Validate: `git --no-pager diff -- CHANGELOG.md` meets acceptance criterion (only minimal additions in target date)
- Confirm: explicit evidence of step 0 (`git --no-pager status --short`) and step 0b (precise read 1-200) exists in the current run; if not, hard stop and restart
- Confirm: a diff of `CHANGELOG.md` exists to pass the `/commit` gate; if not, do not proceed to `/commit`

FORBIDDEN ANTI-PATTERNS (stop and request confirmation if any of the following occurs):
1. Retrying the same patch on the heading without changing the real block anchor.
2. Escalating to a full rewrite of `CHANGELOG.md` to insert a single bullet.
3. Making more than one retry without first re-reading the exact block.
4. Chaining failed attempts without validating the diff at each attempt.
5. NEVER edit entries outside `DATE_CST` (current day) unless the user explicitly instructs it.
6. Proceeding to `/commit` when `CHANGELOG.md` is not ready for the gate (no changes or acceptance criterion not met).
7. Improvising alternative flows outside `/changelogger` and `/commit` to force edits.
8. Repeating the same insertion patch when the preview already showed the blank separator line was missing.
9. Inserting a blank line between bullets of the same date block.
10. Repeating exploratory searches when the target block is already identified.
11. Using partial anchors for existing dates (e.g., `search` with heading only) instead of the exact micro-block on the first attempt.
12. Starting with changelog reading, `grep`, exploratory searches, or patch attempts without having run `git --no-pager status --short` and without having read `CHANGELOG.md` lines `1-200` in that execution; if it occurs, apply immediate hard stop and restart from 0, never continue from intermediate steps.
13. Using `search = heading + first bullet` without including the required intermediate blank line for existing dates.
14. Anchoring existing-date insertions from `# Changelog` or rewriting the top section of the file.
15. Accepting an "insertion-only" patch that shows deleted lines (`-`) in headings or blank separators.
16. Deleting any existing line from `CHANGELOG.md` during incremental insertions without explicit user instruction.
17. Continuing any section of the flow without explicit evidence of `git --no-pager status --short` in the current run.
18. Continuing any section of the flow without explicit evidence of the precise read of `CHANGELOG.md` (1-200) in the current run.
19. Attempting to resume the flow after skipping step 0 or 0b instead of restarting from 0.

Conclusion:
- Deliver: CHANGELOG.md updated with a new entry in the correct chronological position, accurate CST date, language consistent with context, no duplicates, and typed bullets organised semantically.
- Avoid: mixing languages, labelling UTC as CST, incorrect chronological order, duplicating entries, ungrouped micro-changes.
- Expected operation: run this CoT from `/changelogger` and then invoke `/commit` (which only validates the changelog gate + commit language).
- References: «~/rules/CHANGELOG.md» ([../CHANGELOG.md](../CHANGELOG.md)), «~/rules/rulesets/LINGUISTICS.md» ([../rulesets/LINGUISTICS.md](../rulesets/LINGUISTICS.md)), «~/rules/cot/committing.md» ([./committing.md](./committing.md)) for the full flow.
