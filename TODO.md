# TODO

The Spanish → International English (UK) translation is complete; its plan is archived in [docs/archive/ROADMAP-translation-2026.md](./docs/archive/ROADMAP-translation-2026.md).

## Upstream (`incognia/rules`) changes worth porting

- [ ] CI and git hooks (`6ecca91`): GitHub Actions for markdownlint and ShellCheck, weekly link check, Dependabot, CODEOWNERS, and `pre-commit`/`commit-msg` hooks (CHANGELOG gate, Conventional Commits subject) installable with `npm run hooks:install`
- [ ] Sensitive data to `.env` (`f9ebd77`): replace internal IPs and namespaces in the `kube` and `kubetbs` examples and the delivery mail template with placeholders filled from `.env`
- [ ] Link check stability (`4a6d90a`): higher timeout and retries in `.markdownlinkcheck.json`, ignore flaky `gnu.org`
- [ ] Optional explicit author-model argument for `/commit` (`0b45ff4`); automatic model and effort detection is already implemented in `scripts/commit_trailer.py`, while this proposed argument would provide a manual override

## Documentation

- [ ] `/styling`: the skill, its CoT, and `rulesets/STYLING.md` still describe Kabat One branding; align with the Elsevier palette already used by the `bmail` templates

## `/tio-readiness`

- [ ] Calibrate weights and criteria against real specifications (for example the Jenkins → GitHub Actions SDDs in TIOCDT) before posting comments on other teams' pages
- [ ] Fill `TIO_READINESS_MENTIONS` in `~/rules/.env` with the default reviewers

## Commit attribution

The three issues reproduced during review of `a2a89de` and `c4bfb28` in [scripts/commit_trailer.py](./scripts/commit_trailer.py) have been resolved by the corresponding agents. Completed items retain their validation criteria and the fixing commit for traceability.

- [x] **Copilot CLI — medium:** fix `copilot_identity()` retaining an earlier model and effort when the latest root-agent usage record has no valid model. Fail detection so the commit skill can use its attribution fallback. Validate with a valid usage record followed by one without a model; the earlier identity must not be returned. Resolved in `d1945ab`.
- [x] **Claude Code — medium:** fix `claude_model()` accepting a model from a record with a different `sessionId` after any record verifies the session. Filter each assistant candidate by the requested session, continue ignoring sidechain turns, and fail detection when the latest relevant assistant turn has no valid model. Validate mixed-session records and a final assistant turn without a model; neither may yield another session's or an earlier turn's model. `<synthetic>` placeholders (written for interruptions and errors) are skipped rather than treated as a missing model. Resolved in `a3e46b7`.
- [x] **Copilot CLI — low:** normalise the model identifier when `modelDisplayName` is missing or invalid in `copilot_identity()`, using the shared `gpt_display_name()` formatter. Validate that `gpt-6-luna` without a display name produces `Copilot GPT-6 Luna`, matching the shared trailer format. Resolved in `6965010`.

## Tooling

- [x] markdownlint configured (`.markdownlint.yaml`)
- [x] Full markdownlint QA pass (851 → 0 errors, 2026-07-25)
- [ ] CoT validation hook (at least 3 numbered steps and a conclusion section); can ship with the upstream git hooks above
