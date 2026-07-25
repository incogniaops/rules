# TODO

## Translation migration

See [ROADMAP.md](./ROADMAP.md) for the full plan and per-file checklist.

## Content fixes (non-translation)

- [ ] `docs/SYNC.md` — add Claude Code section; sync script was updated but doc was not
- [ ] `cot/licensing.md` — remove stale Promad references when translating
- [ ] `rulesets/CRITICAL_COT_READING.md` — remove emojis and update to current format when translating

## Tooling

- [ ] Configure markdownlint (`.markdownlint.json`) with project rules and exclusions
- [ ] Add pre-commit hook to validate CoT files (≥3 numbered steps, conclusion section present)
- [ ] Final QA pass (UK English spelling, broken links) after Phase 1 translations are complete
