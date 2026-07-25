# TODO

## Translation migration

See [ROADMAP.md](./ROADMAP.md) for the full plan and per-file checklist.

## Content fixes (non-translation)

All resolved during Phase 1:

- [x] `docs/SYNC.md` — Claude Code section added
- [x] `cot/licensing.md` — Promad references removed
- [x] `rulesets/CRITICAL_COT_READING.md` — emojis removed, plain-text markers applied

## Tooling

- [ ] Configure markdownlint (`.markdownlint.json`) with project rules and exclusions
- [ ] Add pre-commit hook to validate CoT files (≥3 numbered steps, conclusion section present)
- [ ] Final QA pass (UK English spelling, broken links) — Phase 1 complete, run now
