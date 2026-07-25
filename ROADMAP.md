# Translation roadmap

Migration of this repository's documentation from Mexican Spanish to International English (UK), following the bilingual context policy.

## Bilingual policy

| Context | Language | Scope |
|---------|----------|-------|
| Corporate (`@incogniaops`, `r.alvarez1@elsevier.com`) | International English (UK) | CoTs, rulesets, skills, CHANGELOG entries |
| Personal (`@incognia`) | Mexican Spanish | Documentation and CHANGELOG entries |
| Cultural / philosophical sources | Spanish (preserved) | `FILOSOFIA.md`, `LINGUISTICA.md`, `cot/linguistica.md` |

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
| `rulesets/LINGUISTICA.md` | `rulesets/LINGUISTICS.md` |
| `cot/linguistica.md` | `cot/linguistics.md` |

---

## Phase 1 — Translate in place ⬜

Replace content with International English (UK); keep filename unchanged.

### Skills

- [ ] `.agents/skills/release/SKILL.md`

### CoTs (`cot/`)

- [ ] `_template.md`
- [ ] `arithmetic.md`
- [ ] `aws_naming.md`
- [ ] `bmail.md`
- [ ] `changelog.md`
- [ ] `devops.md`
- [ ] `git_init.md`
- [ ] `git_workflow.md`
- [ ] `github_metadata.md`
- [ ] `kube.md`
- [ ] `kubetbs.md`
- [ ] `latex.md`
- [ ] `licensing.md` — also remove stale Promad references
- [ ] `lint.md`
- [ ] `mail.md`
- [ ] `release.md`
- [ ] `repo_context.md`
- [ ] `styling.md`

### Rulesets (`rulesets/`)

- [ ] `ATTRIBUTION.md`
- [ ] `BACKUPS.md`
- [ ] `BMAIL.md`
- [ ] `COMMIT_LANGUAGE_PROTOCOL.md`
- [ ] `COMMITTING.md`
- [ ] `CORPORATE.md`
- [ ] `CRITICAL_COT_READING.md` — also remove emojis and update format
- [ ] `GIT.md`
- [ ] `GLOSSARY.md`
- [ ] `KUBE.md`
- [ ] `KUBETBS.md`
- [ ] `LATEX.md`
- [ ] `LICENSING.md`
- [ ] `MAIL.md`
- [ ] `RELEASING.md`
- [ ] `STYLING.md`
- [ ] `VAULT.md`

### Docs (`docs/`)

- [ ] `MAIL.md`
- [ ] `SYNC.md` — also add Claude Code section (content is outdated)

### Templates (`templates/`)

- [ ] `github-readme.md`
- [ ] `gitlab-readme.md`
- [ ] `hedgedoc.md`
- [ ] `issue_template.md`

---

## Phase 2 — ES source + EN pair ⬜

| Keep Spanish source | Create English file | Reason |
|---------------------|---------------------|--------|
| `rulesets/TEACHING.md` | `rulesets/TEACHING_EN.md` (name TBD) | personal educational profile with authentic voice |

---

## Special cases — pending decisions ⬜

- **`CHANGELOG.md` header**: heading (`# Historial de cambios`) and note are in Spanish. Decision: keep as historical archive header or migrate to English.
- **`rulesets/TEACHING.md`**: confirm Phase 2 pattern or translate in place like the other rulesets.
- **`CHANGELOG.md` older entries**: pre-2026-07 entries were written in personal context (Spanish). Leave historical entries as-is regardless of header decision.
