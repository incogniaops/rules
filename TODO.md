# TODO

The Spanish → International English (UK) translation is complete; its plan is archived in [docs/archive/ROADMAP-translation-2026.md](./docs/archive/ROADMAP-translation-2026.md).

## Upstream (`incognia/rules`) changes worth porting

- [ ] CI and git hooks (`6ecca91`): GitHub Actions for markdownlint and ShellCheck, weekly link check, Dependabot, CODEOWNERS, and `pre-commit`/`commit-msg` hooks (CHANGELOG gate, Conventional Commits subject) installable with `npm run hooks:install`
- [ ] Sensitive data to `.env` (`f9ebd77`): replace internal IPs and namespaces in the `kube` and `kubetbs` examples and the delivery mail template with placeholders filled from `.env`
- [ ] Link check stability (`4a6d90a`): higher timeout and retries in `.markdownlinkcheck.json`, ignore flaky `gnu.org`
- [ ] Optional model argument for `/commit` (`0b45ff4`) so the `Co-Authored-By` trailer names the model that did the work

## Documentation

- [ ] `/styling`: the skill, its CoT, and `rulesets/STYLING.md` still describe Kabat One branding; align with the Elsevier palette already used by the `bmail` templates

## `/tio-readiness`

- [ ] Calibrate weights and criteria against real specifications (for example the Jenkins → GitHub Actions SDDs in TIOCDT) before posting comments on other teams' pages
- [ ] Fill `TIO_READINESS_MENTIONS` in `~/rules/.env` with the default reviewers

## Tooling

- [x] markdownlint configured (`.markdownlint.yaml`)
- [x] Full markdownlint QA pass (851 → 0 errors, 2026-07-25)
- [ ] CoT validation hook (at least 3 numbered steps and a conclusion section); can ship with the upstream git hooks above
