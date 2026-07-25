# Translation roadmap

Migration of this repository's documentation from Mexican Spanish to International English (UK), following the bilingual context policy.

## Bilingual policy

| Context | Language | Scope |
|---------|----------|-------|
| Corporate (`@incogniaops`, `r.alvarez1@elsevier.com`) | International English (UK) | CoTs, rulesets, skills, CHANGELOG entries |
| Personal (`@incognia`) | Mexican Spanish | Documentation and CHANGELOG entries |
| Cultural / philosophical sources | Spanish (preserved) | `FILOSOFIA.md`, `ENSEÑANZA.md`, `LINGUISTICA.md`, `cot/linguistica.md` |

## Translation patterns

- **Translate in place** — operational documents with no cultural voice worth preserving: replace content, keep filename.
- **ES source + EN pair** (FILOSOFIA pattern) — documents with personal or cultural authenticity: keep Spanish file with Spanish name, create a separate English file alongside it.

---

## Done ✅

### Skills (`.agents/skills/`)

`aws-naming`, `backup`, `bmail`, `changelogger`, `commit`, `context`, `git-init`, `kube`, `kubetbs`, `licensing`, `linguistica`, `linguistics`, `mail`, `ssh-import`, `styling`

### CoTs (`cot/`)

`backup.md`, `committing.md`, `context.md`, `linguistics.md`, `quick_backup.md`, `restore.md`

### Rulesets (`rulesets/`)

`LINGUISTICS.md`

### Root

`AGENTS.md`, `PHILOSOPHY.md`, `README.md`

### ES ↔ EN pairs already in place

| Spanish source | English translation |
|----------------|---------------------|
| `FILOSOFIA.md` | `PHILOSOPHY.md` |
| `rulesets/ENSEÑANZA.md` | `rulesets/TEACHING.md` |
| `rulesets/LINGUISTICA.md` | `rulesets/LINGUISTICS.md` |
| `cot/linguistica.md` | `cot/linguistics.md` |

---

## Phase 1 — Translate in place ✅

Replace content with International English (UK); keep filename unchanged.

### Skills

- [x] `.agents/skills/release/SKILL.md`

### CoTs (`cot/`)

- [x] `_template.md`
- [x] `arithmetic.md`
- [x] `aws_naming.md`
- [x] `bmail.md`
- [x] `changelog.md`
- [x] `devops.md`
- [x] `git_init.md`
- [x] `git_workflow.md`
- [x] `github_metadata.md`
- [x] `kube.md`
- [x] `kubetbs.md`
- [x] `latex.md`
- [x] `licensing.md` — Promad references removed
- [x] `lint.md`
- [x] `mail.md`
- [x] `release.md`
- [x] `repo_context.md`
- [x] `styling.md`

### Rulesets (`rulesets/`)

- [x] `ATTRIBUTION.md`
- [x] `BACKUPS.md`
- [x] `BMAIL.md`
- [x] `COMMIT_LANGUAGE_PROTOCOL.md`
- [x] `COMMITTING.md`
- [x] `CORPORATE.md`
- [x] `CRITICAL_COT_READING.md` — emojis removed, plain-text markers applied
- [x] `GIT.md`
- [x] `GLOSSARY.md`
- [x] `KUBE.md`
- [x] `KUBETBS.md`
- [x] `LATEX.md`
- [x] `LICENSING.md`
- [x] `MAIL.md`
- [x] `RELEASING.md`
- [x] `STYLING.md`
- [x] `VAULT.md`

### Docs (`docs/`)

- [x] `MAIL.md`
- [x] `SYNC.md` — translated and Claude Code section added

### Templates (`templates/`)

- [x] `github-readme.md`
- [x] `gitlab-readme.md`
- [x] `hedgedoc.md`
- [x] `issue_template.md`

---

## Phase 2 — ES source + EN pair ✅

| Spanish source | English translation | Status |
|----------------|---------------------|--------|
| `rulesets/ENSEÑANZA.md` | `rulesets/TEACHING.md` | done — pair already in place |

---

## Special cases — resolved ✅

- **`CHANGELOG.md`**: translate the entire file to English — header, note, section titles, and all historical Spanish entries.
- **`rulesets/TEACHING.md`**: follows the FILOSOFIA pattern — `TEACHING.md` renamed to `ENSEÑANZA.md` (Spanish source), new `TEACHING.md` created as English translation.
