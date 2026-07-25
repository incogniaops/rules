# Changelog

**Note:** All dates are in CST (México City, UTC-6).

<!-- markdownlint-disable MD013 MD024 MD022 MD032 -->
## [2026-07-25] - Update README, philosophy manifest, and Claude Code sync integration

- fix: repair broken relative links across CoTs and rulesets: correct ../../ depth errors, remove stale PROMPTS.md references, and fix ./PHILOSOPHY.md and ./README.md paths in rulesets/ENSEÑANZA.md and rulesets/TEACHING.md
- i18n: translate 18 CoTs and skills/release to International English (UK) as Phase 1 of the full repository translation plan
- i18n: translate 17 rulesets to International English (UK); remove emojis from CRITICAL_COT_READING.md and Promad references from cot/licensing.md
- i18n: translate docs/MAIL.md and 4 templates to International English (UK)
- docs: translate docs/SYNC.md and add Claude Code integration section documenting the skill symlink mechanism
- fix: remove duplicate git-init skill entry misplaced in [2025-07-31] date block
- feat: add CLAUDE.md as a relative symlink to AGENTS.md so Claude Code loads project context automatically
- docs: add Claude Code specifics section to AGENTS.md with skill invocation, atomic commit rules, and memory path; fix commit workflow to use selective git add instead of git add .
- feat: add ROADMAP.md with the full EN translation plan: bilingual policy, per-file checklist grouped by directory, ES-source pairs, and pending decisions
- chore: consolidate TODO.md — merge rulesets/TODO.md into root TODO.md, remove stale completed items, delegate translation tracking to ROADMAP.md, and delete rulesets/TODO.md
- docs: document Claude Code skill support in README.md installation notes and add a per-tool skill installation paths table comparing copy vs symlink methods across Warp, Claude Code, and other agents
- docs: adjust tone and phrasing in `PHILOSOPHY.md` for a more direct and authentic voice throughout the manifesto
- docs: update `README.md`: fix last-modified date, refresh badge counts (CoTs 21→25, Skills 10→16, Rulesets 16→21), correct remote URL from `incognia` to `incogniaops`
- docs: add `FILOSOFIA.md` and `LINGUISTICA.md` to the documents section in `README.md` and extend the skills list with `/aws-naming`, `/bmail`, `/linguistica`, `/release`, `/kube`, and `/kubetbs`
- feat: extend `scripts/sync_global.sh` with a Claude Code integration block that symlinks skills from `~/.agents/skills/` into `~/.claude/commands/`

## [2026-07-22] - Align corporate profile and git initialisation standards

- feat: apply context-based bilingual policy across core rules so personal projects document in Mexican Spanish while corporate projects remain fully in International English
- docs: translate `AGENTS.md`, `cot/context.md`, and `cot/committing.md` to International English (UK) and standardise CoT labels in English
- docs: enforce the `México` accent exception across bilingual references, including `México City`, in rules, skills, and CoT guidance
- docs: add root `TODO.md` with a translation and consistency backlog aligned to the `linguistics`/`linguistica` migration pattern
- docs: update `README.md` to expose `FILOSOFIA` and `LINGUISTICA` as original Spanish sources and clarify that English variants derive from those baselines
- docs: translate `cot/quick_backup.md`, `cot/backup.md`, and `cot/restore.md` to International English (UK) while preserving operational commands and CST workflow
- docs: document mandatory proper-noun accent exceptions (`México`, `Álvarez`) in `rulesets/LINGUISTICS.md` and `rulesets/LINGUISTICA.md`
- docs: align linguistic skills and attribution guidance so the surname is always written as `Álvarez` in regular documentation text
- docs: update bilingual language policy in `README.md`, `AGENTS.md`, and `rulesets/COMMIT_LANGUAGE_PROTOCOL.md` to enforce personal Spanish documentation/CHANGELOG and fully International English corporate workflows
- docs: update `.agents/skills/changelogger/SKILL.md` and `cot/changelog.md` to make changelog language and bullet prefix context-aware (`tipo:` personal, `type:` corporate)
- docs: translate `README.md` and `PHILOSOPHY.md` to International English and preserve Spanish philosophical baseline in `FILOSOFIA.md`
- docs: translate linguistic guidance corpus to International English in `.agents/skills/linguistics/SKILL.md`, `cot/linguistics.md`, and `rulesets/LINGUISTICS.md` with UK spelling consistency
- feat: add `linguistica` aliases as direct copies of linguistics assets in `.agents/skills/linguistica/SKILL.md`, `cot/linguistica.md`, and `rulesets/LINGUISTICA.md`
- docs: update labour identity references to Elsevier, GitHub `incogniaops` and email `r.alvarez1@elsevier.com` across rules and skills
- feat: align git initialisation flows and helper script with SSH key `~/.ssh/elsevier` and SSH remote examples for `incogniaops`
- docs: switch changelog maintenance guidance to International English (UK) with consistent `type:` bullets

## [2026-06-22] - Add bmail workflow for corporate email in English

- feat: standardise the seven templates in `templates/bmail/` with a new HTML structure, metadata block (from/to/date/subject), and optional fields per scenario
- feat: create the `bmail` skill with email-type selection, field validation, and HTML save convention
- feat: add CoT `cot/bmail.md`, rules `rulesets/BMAIL.md`, and seven HTML templates in `templates/bmail/` for corporate email composition
- fix: extend `scripts/sync_global.sh` to also synchronise `cot/`, `rulesets/`, and `templates/` to the global destination `~/rules`

## [2026-06-19] - Update central philosophy quote and clean up document closing

- docs: update the main quote in `PHILOSOPHY.md` to include a complete formulation on universal access to technological and scientific progress
- fix: remove a residual duplicate italic line at the close of `PHILOSOPHY.md` to maintain editorial consistency

## [2026-06-01] - Create CoT and skill for AWS S3 asset naming normalisation

- feat: create `cot/aws_naming.md` standardised with CoT template format (frontmatter, reasoning, steps, conclusion) for normalising file names in S3 and CloudFront
- feat: add extension normalisation to CoT: `.jpeg` → `.jpg`, support for `.png`, `.svg`, and `.ico`
- feat: add generation of a `.tsv` audit file mapping original name → normalised name
- feat: create `.agents/skills/aws-naming/SKILL.md` based on the CoT with operational instructions, examples, and a name-collision prevention rule

## [2026-05-25] - Update generic mail template and add logo

- docs: document anchor rule in `edit_files`: the `search` field must begin at the first character of the line indicated by `search_start_line_number`; rule added to `rulesets/STYLING.md`, `cot/styling.md`, and `.agents/skills/styling/SKILL.md`
- style: add 192 px Kabat One logo as an asset for HTML mail templates
- fix: remove embedded signature image from `generic_template.html` and document in a comment that it is only included in `graph` mode via CID; `owa` and `mac` modes delegate the signature to Outlook

## [2026-05-14] - Adjust changelogger and commit flows without redundancies

- feat: redefine `/changelogger` and `cot/changelog.md` to execute `git --no-pager status --short` as a mandatory step 0 before the precise read of `CHANGELOG.md` (lines 1–200)
- feat: update `/commit` and `cot/committing.md` to keep the `CHANGELOG.md` gate and forbid redundant changelog-edit bullets in the commit body

## [2026-05-11] - Reinforce styling with single-date policy

- docs: clarify `/styling`, `cot/styling.md`, and `rulesets/STYLING.md` to eliminate redundant reported dates and retain a single "Last modified" field

## [2026-05-10] - Strengthen changelog flow and skill consistency

- docs: define an absolute hard stop in `/changelogger` and `cot/changelog.md`: if the precise read of `CHANGELOG.md` (lines 1–200) is not executed, the flow stops and restarts from step 0
- docs: reinforce `/changelogger` and `cot/changelog.md` with insertion-only incremental mode and mandatory abort if the diff shows deleted lines (`-`) without explicit user instruction
- docs: reinforce `/changelogger` and `cot/changelog.md` with a prohibition on anchoring from `# Registro de cambios` and rejection of insertion patches that remove separators
- docs: forbid the pattern `search = heading + first bullet` without a blank line and require an initial read of `CHANGELOG.md` (lines 1–200) in `/changelogger`
- feat: rename the `/changelog` skill to `/changelogger` and update operational references in documentation and repository rules
- feat: strengthen the `/commit` gate to validate changes in `CHANGELOG.md` and delegate its editing exclusively to the `/changelogger` flow
- fix: harden `scripts/sync_global.sh` to clean up obsolete skills managed during global synchronisation
- docs: update `cot/changelog.md` and the `changelogger` skill with explicit rules against editing entries outside the current day and requiring a blank line between date blocks

## [2026-05-07] - Reinforce anti-error protocol in changelog and commit

- feat: make anti-error and anti-pattern checkpoints explicit in the `/changelog` and `/commit` flows within skills and CoTs (`.agents/skills/changelog/SKILL.md`, `.agents/skills/commit/SKILL.md`, `cot/changelog.md`, `cot/committing.md`)
- feat: formalise in `rulesets/COMMITTING.md` and `rulesets/COMMIT_LANGUAGE_PROTOCOL.md` mandatory validation gates for `CHANGELOG.md` and a language checkpoint before committing

## [2026-05-04] - Standardise CHANGELOG format with operaciones-ti standard

- feat: create `.agents/skills/release/SKILL.md` to publish non-interactive semantic versions with historical validation and flow closure in `dev`
- feat: create `rulesets/RELEASING.md` with canonical rules for `vX.Y.Z` tagging, name/notes convention, and mandatory post-publication verifications
- feat: update `cot/release.md` with a non-interactive publication CoT: baseline validation, automatic descriptor/notes derivation, and `dev -> main -> tag -> release -> dev` sequence
- feat: migrate `CHANGELOG.md` to date-heading format with direct typed bullets (`- type: ...`) and remove `### type` subheadings
- docs: update `.agents/skills/changelog/SKILL.md` and `.agents/skills/commit/SKILL.md` to require the new entry format
- docs: update `cot/changelog.md`, `cot/committing.md`, and `rulesets/COMMITTING.md` to document and validate the standardised format

## [2026-05-02] - Standardise detailed commit with temporary file

- feat: make the format of `/tmp/commit-msg.txt` explicit in the skill, CoT, and rules: bullets at column 1, manual line-wrapping for long lines, and continuation lines indented with two spaces
- feat: update `.agents/skills/commit/SKILL.md`: formalise the base flow to build `/tmp/commit-msg.txt` with a detailed template and execute `git commit -F /tmp/commit-msg.txt`
- feat: update `cot/committing.md`: move the construction of the detailed message to an explicit step before the commit and use `-F` as the primary method for atomic commits
- feat: update `rulesets/COMMITTING.md` and `rulesets/COMMIT_LANGUAGE_PROTOCOL.md`: document the detailed template, language verification over the temporary file, and consistent execution with `git commit -F`

## [2026-04-30] - Direct-edit rule in commit skill

- feat: update `.agents/skills/commit/SKILL.md`: embed critical CHANGELOG rules directly in the skill to avoid dependency on nested references — verification of existing entry, mandatory `edit_files` technique (single anchor without duplicating content), reverse chronological order, and language

## [2026-04-28] - CHANGELOG.md editing rule

- feat: update `cot/changelog.md`: add step 6b with the golden rule for `edit_files` (single anchor, without truncating lines in `replace`), reverse chronological order of bullets within `### type`, and top-insertion technique without affecting adjacent lines

## [2026-04-23] - Optimise commit flow and improve mail skill

- improve: optimise `cot/committing.md`: add session condition to step 0 to skip identity validation in subsequent invocations within the same conversation session
- improve: optimise `.agents/skills/commit/SKILL.md` (repo and global): merge validation steps (identity + SSH) into a single conditional step; skip directly to the CST date step if already validated in the session
- improve: add step-0 guard in `.agents/skills/mail/SKILL.md` (repo and global): display help with usage, modes, types, subject, and examples when invoked without parameters; stop execution without loading CoT or rules

## [2026-04-18] - Update corporate email across rules and skills

- docs: update corporate email across all rules, CoTs, skills, and templates: `ralvarez@promad.com.mx` → `ralvarez@kabatone.com` for labour projects (`@incogniadev`) on GitHub and GitLab
- docs: update `rulesets/GIT.md`: `git config user.email` configuration blocks for labour projects (recommended section and manual steps)
- docs: update `rulesets/ATTRIBUTION.md`: email in the labour digital identifiers section and in the commit signature example
- docs: update `rulesets/LICENSING.md`: header templates in Bash scripts, Python, and Argo CD YAML manifests
- docs: update `scripts/git-init-context.sh`: `EMAIL` variable for labour context
- docs: update `cot/git_init.md`: email in manual steps for labour context (Promad)
- docs: update `.agents/skills/git-init/SKILL.md`: identity configuration block for `laboral` context
- docs: update `.agents/skills/licensing/SKILL.md`: corporate context indicators
- docs: update `AGENTS.md`: email in the corporate projects section
- docs: update `README.md`: email in the rules-by-context table

## [2026-03-30] - Create `docs/` folder and separate responsibilities

- style: update corporate colour palette: replace old CSS variables (`--promad`, `--electric`, `--lavender`) with new Kabat One palette (`--midday`, `--midnight`, `--ice`, `--connect`, `--code`, `--deep`, `--video`)
- style: change `body` text from colour variable to black/white depending on light/dark mode
- style: add `a:visited` with colour `--video` (#7252D8) and `a:hover` with `--connect` (#31D8FF)
- style: implement dual light/dark logo with `.logo-light`/`.logo-dark` classes and CSS visibility rules by mode
- style: update corporate signature image in the footer
- style: add signature image with dimensions for HedgeDoc (`ralvarez_firma_728.png`)
- style: add corporate typefaces via Google Fonts: Space Grotesk (primary, general text) and Montserrat (secondary, headings)
- style: apply new palette and typefaces to HTML mail templates (`delivery_template.html`, `generic_template.html`): replace generic colours with Kabat One palette (Midday, Midnight, Safety, Traffic, Dispatch, Video, Code, Ice), add Space Grotesk/Montserrat with Arial fallback

- fix: remove explicit `color` from `.markdown-body` in HedgeDoc CSS; delegate light/dark text colour handling to HedgeDoc's native theme
- fix: detect WSL in `sync_global.sh` using `/proc/version` and `$WSL_DISTRO_NAME`; copy skills to Windows home (`%USERPROFILE%/.agents/skills/`) instead of the Linux home, which Warp cannot read when running on Windows

- docs: create `docs/SYNC.md`: detailed documentation of the synchronisation mechanism with Mermaid diagrams (general flow, platform detection, destinations by platform, update flow)

- refactor: move `MAIL.md` → `docs/MAIL.md`: separate process documentation (Graph API, Entra, OAuth2) from rules and CoT
- refactor: invert reference direction: `cot/mail.md` and `rulesets/MAIL.md` no longer point to docs; `docs/MAIL.md` references the CoT, ruleset, skill, and script
- refactor: clarify in README.md what `sync_global.sh` copies (skills and workflows) and what it does not (`scripts/`, `templates/`, `rulesets/`, `cot/`)
- refactor: add `docs/MAIL.md` to the documents list in README.md

## [2026-03-29] - Send email from CLI with three delivery modes

- feat: parametrise the mail skill with three delivery modes: `/mail <owa|mac|graph> <delivery|generic> <subject>`
  - `owa`: save HTML to copy and paste into Outlook Web (Linux)
  - `mac`: open draft in Outlook via AppleScript with native signature (macOS)
  - `graph`: send directly via Microsoft Graph API with inline CID signature (any OS)
- feat: create `MAIL.md`: full documentation of the Microsoft Entra application registration process, delegated permissions, device code flow, and sending via Graph API
- feat: integrate signature as inline CID attachment in `graph` mode using `~/rules/templates/mail/assets/ralvarez_firma.png`

- docs: update `cot/mail.md`: add steps 9 and 10 with file saving and delivery by mode; update reasoning and conclusion
- docs: update `rulesets/MAIL.md`: three-mode workflow, new section referencing the Graph API

- feat: create `scripts/graph_auth.py`: Graph API authentication with token cache in `~/.graph_tokens.json` (cache → silent refresh → device code flow)
- feat: add `token` mode to the mail skill: `/mail token` to authenticate and cache the token once (~90 days)
- feat: change `graph` mode signature to `ralvarez_firma_740.png` (740 px = usable area of the 800 px container with 30 px padding)

- docs: update `MAIL.md`: document container dimensions (800 − 60 = 740 px), token lifecycle with Mermaid diagram, periodicity, and involved files
- docs: add signature variants to `templates/mail/assets/`: `_740.png`, `_1024.png`

## [2026-03-28] - kube skill for Kubernetes cluster analysis

- feat: create parametrised kube skill for Kubernetes cluster analysis via SSH: `/kube <key> <user> <ip> <namespace>`
- feat: create `rulesets/KUBE.md`: cluster analysis rules (SSH access, manifest structure, diagnostic commands, observability ports, naming conventions)
- feat: create `cot/kube.md`: 10-step CoT for complete analysis (nodes, pods, services, VirtualServices, Istio, ArgoCD, manifests, health checks, observability)
- feat: document actual observability ports: Kiali 20001 (LoadBalancer), Prometheus 9090 (NodePort), Grafana 3000 (LoadBalancer)

- docs: add Mermaid sequence diagram to README.md: skill (interface) → CoT (middleware) → ruleset (backend) flow

- feat: create kubetbs skill for Kubernetes microservice troubleshooting: `/kubetbs <key> <user> <ip> <namespace> [service]`
- feat: create `rulesets/KUBETBS.md`: outside-in methodology, diagnostic commands, common errors (CrashLoopBackOff, ImagePullBackOff, cross-namespace)
- feat: rename `cot/kubernetes.md` → `cot/kubetbs.md` and add reference to new ruleset

- fix: correct relative paths to canonical paths (`~/rules/cot/`, `~/rules/rulesets/`, `~/rules/templates/`) in all skills (kube, kubetbs, mail, git-init)
- fix: correct CoT count in README.md: 20 → 22 (missing `mail.md` and `kube.md`)
- fix: add missing description to the workflows heading in the structure section

## [2026-03-27] - Simplify directory structure and create AI-agent skills

- refactor: simplify repository directory structure
  - rename `docs/` → `rulesets/` (more descriptive of the content)
  - move `prompts/cot/` → `cot/` (root, remove nesting)
  - consolidate `prompts/actions/release.md` and `prompts/guides/git_workflow_guide.md` into `cot/`
  - move `prompts/snippets/cst_date.sh` → `scripts/`
  - move `prompts/templates/` → `templates/` (root)
  - remove empty `prompts/` structure and subdirectories
  - update 80+ internal references in documentation and CoTs
- refactor: rename `WARP.md` → `AGENTS.md`: agent-agnostic project rules file (recognised by Warp, Claude, Cursor, Copilot, Gemini, etc.)
  - remove `<citations>` block (Warp artefact that does not belong in the versioned file)
  - rewrite content without Warp-specific product references
- refactor: remove obsolete files: PROMPTS.md (redundant with README and CoTs), ROADMAP.md (6 months without update), REFACTOR.md (replaced by this change)

- feat: create 6 AI-agent-discoverable skills in `.agents/skills/`
  - **commit**: full commit workflow with mandatory CHANGELOG
  - **changelog**: CHANGELOG.md maintenance with CST dates
  - **linguistics**: apply Mexican Spanish language rules
  - **context**: quick project context detection
  - **backup**: backup using standard naming
  - **licensing**: automatic licensing (GPLv3 vs MIT)
- feat: create 4 parametrised YAML workflows in `.warp/workflows/`
  - **backup_file**: backup individual file/directory
  - **lint_markdown**: run markdownlint on all files
  - **commit_flow**: full commit flow with type and description
  - **cst_date**: get date/time in CST (Ciudad de México)

- docs: update README.md: new directory structure, skills and workflows section, correct symlink commands
- docs: update PHILOSOPHY.md: replace references to ROADMAP.md and TODO.md with AGENTS.md
- docs: update AGENTS.md: paths to new structure (`rulesets/`, `cot/`)

- fix: correct invocation paths in README.md: use `~/rules/cot/` (canonical path) instead of `~/cot/` (symlink-dependent) in examples and Mermaid diagram

- feat: create `scripts/sync_global.sh`: cross-platform script to synchronise global skills and workflows
  - automatically detects macOS, Linux, and Windows/WSL
  - copies skills to `~/.agents/skills/` and workflows to the correct path per platform
  - can be run from the local copy or directly from the public repo

- docs: rewrite initial setup section in README.md: simplify to `git clone` + `sync_global.sh`
- docs: remove `~/cot` symbolic link: does not work well in Warp with WSL; use only canonical paths
- docs: add remote execution option without prior cloning
- docs: document per-platform paths in setup notes
- docs: document access to YAML workflows via Workflow Search (`Ctrl+Shift+R`) on macOS, Linux, and Windows
- docs: mark workflow paths on Linux and Windows as pending validation

- improve: parametrise linguistics skill with `$0` argument for target file: `/linguistics README.md`

- feat: create parametrised git-init skill with 4 arguments: context (personal/laboral), SSH key name (looked up in `~/.ssh/`), remote URL, and branch

- feat: create parametrised mail skill to compose OWA-compatible HTML emails: `/mail <delivery|generic> <subject>`
- feat: create `rulesets/MAIL.md`: HTML email composition rules (OWA restrictions, `bgcolor` in `<td>`, colour palette, placeholders)
- feat: create `cot/mail.md`: 9-step CoT to produce emails from templates
- feat: migrate mail templates from the stab repo to `templates/mail/` (`delivery_template.html`, `generic_template.html`)
- feat: migrate signature image (`ralvarez_firma.png`) to `templates/mail/assets/` and correct paths in templates
- feat: add mandatory signature-with-image step to the mail skill

- feat: create parametrised ssh-import skill to import SSH keys to remote servers via GitHub: `/ssh-import <faraday|cad> <user@server>`
  - `faraday` → personal servers (GitHub: @incognia)
  - `cad` → client servers (GitHub: @incogniadev)
  - supports 3 options: Ubuntu auto-import, manual `ssh-import-id`/`curl`, and cloud-init

- docs: update SSH keys across all files: `id_ed25519` → `incognia` (personal), `promad_ed25519` → `kone` (labour/repos)
- docs: document convention of 4 keys: `incognia` (personal repos), `kone` (labour repos + infra), `faraday` (personal servers), `cad` (client servers)

- docs: update README.md: complete list of 9 skills with syntax, 4 workflows, 4 SSH keys (repos + servers), MAIL.md in documents, sync_global.sh in tools

- style: apply LINGUISTICS.md to README.md: convert loose text into headings (`Definiciones rápidas`, `Ejemplos de comandos`), italics on loanwords (*Prompt*, *Chain-of-Thought*), correct calque «ciclar» → «navegar»

- style: apply LINGUISTICS.md to PHILOSOPHY.md: italics on loanword (`Helm *charts*`), correct calque «desarrollado» → «elaborado» in footer
- style: apply LINGUISTICS.md to CHANGELOG.md: italics on *overview* and *lint*, correct calque «comprehensiva» → «exhaustiva», correct typo «systemáticamente» → «sistemáticamente»

- feat: create parametrised `styling` skill to apply Kabat One style to Markdown documents by platform: `/styling <hedgedoc|gitlab|github> [mit|gpl] <file>`
  - header with Kabat One logo, CST timestamp, and YAML tags (HedgeDoc only)
  - footer with corporate signature (HedgeDoc only); GPLv3/MIT copyright (README.md only on GitLab/GitHub)
  - mandatory removal of spurious `---` separators; mandatory licence badges
- feat: create per-platform templates in `templates/`: `hedgedoc.md`, `gitlab-readme.md`, `github-readme.md`

- docs: update `rulesets/STYLING.md`: new Kabat One branding, per-platform structure, syntax difference table, badge and template rules
- docs: update `cot/styling.md`: reinforce `---` removal rule with a programmatic step
- docs: update `cot/changelog.md`: add mandatory validation of existing entry before creating a new heading for the same date
- docs: apply GitHub styling (GPLv3) to `README.md`: CST timestamp, correct `###` → `##` hierarchy in "Definiciones rápidas", update Skills badge (9→10), add `/styling` to skills list
- docs: apply GitHub styling to `PHILOSOPHY.md`: CST timestamp, remove 2 spurious `---` separators (before `## Referencias` and before the copyright)
- docs: correct timestamp format in `README.md` and `PHILOSOPHY.md`: replace `<div style>` with pure Markdown italic (`*Last modified: ...*`) — GitLab and GitHub strip `style` attributes
- docs: add YAML frontmatter (`title:`, `description:`) to GitLab/GitHub templates and rules: GitHub renders as a horizontal table, GitLab as a code block; update compatibility table in `rulesets/STYLING.md`
- docs: track Kabat One logo images in `templates/mail/assets/`: variants at 100, 160, 200, and 600 px
- docs: restrict YAML frontmatter (`title:`, `description:`) to README.md only on GitLab/GitHub (criterion similar to licensing); other documents only carry H1 and timestamp
- docs: add YAML frontmatter to `README.md`; update timestamps in `README.md` and `PHILOSOPHY.md`
- docs: fix YAML error in `README.md`: quote values with double quotes; values with `:` without quotes cause «mapping values are not allowed» on GitHub; update templates and skill with the same rule
- docs: correct relative paths in all skills: replace references such as `cot/X.md` and `rulesets/X.md` with absolute paths `~/rules/cot/X.md` and `~/rules/rulesets/X.md` to prevent the agent from looking in `~/.agents/skills/` instead of `~/rules/`

## [2026-03-23] - Add LaTeX ruleset and CoT

- feat: create rulesets/LATEX.md: complete reference rules for generating LaTeX documents with XeLaTeX on Fedora (fonts, tables with `tabularx`+`booktabs`, code blocks with `tcolorbox`, PROMAD palette, standard header/footer, package installation with `dnf`)
- feat: create cot/latex.md: 8-step CoT for generating LaTeX documents from scratch using Markdown as the content reference
- feat: document the critical reason NOT to use pandoc directly: inconsistent tables, broken code block backgrounds, and uncontrollable header/footer

## [2026-03-23] - Separator rule in styling CoT

- docs: add critical rule to cot/styling.md (step 5): remove all `---` from the document body; the only one permitted is the one immediately preceding `## Contacto`

## [2026-02-26] - Update professional title and corporate email in STYLING.md

- docs: update STYLING.md: change professional title from «Ingeniero DevOps» to «Líder DevOps» and corporate email from promad.com.mx to kabatone.com in the signature template

## [2026-01-23] - Update copyright dates to 2026

- docs: update copyright dates from 2025 to 2026 in README.md, PHILOSOPHY.md, rulesets/VAULT.md, rulesets/LICENSING.md, and cot/licensing.md
- docs: update example dates in rulesets/LICENSING.md from 2025-07-30 to 2026-01-23 in header templates for Bash scripts, Python, and YAML manifests
- docs: update date validation in cot/licensing.md from 2025 to 2026 for footer verification in README.md

## [2025-12-29] - Create REFACTOR.md checklist

- docs: create REFACTOR.md: detailed checklist for directory structure refactoring (9 phases, 60+ steps, executable commands)

- style: apply LINGUISTICS.md to REFACTOR.md: correct 22 headings from Title Case to sentence case, add italics to technical loanwords (*symlink*, *snippet*, *commit*, *push*, *markdown-link-check*, *markdownlint*), correct English calques («testing» → «pruebas», «linting» → «análisis estático»)

## [2025-10-15] - Clarify CoT classification in COMMITTING.md

- docs: clarify COMMITTING.md: CoT files are classified as `feat:` (automated functionality) not `docs:` (documentation)

## [2025-10-11] - CoT for GitHub metadata configuration without interactive editors

- feat: create cot/github_metadata.md: functional CoT for configuring GitHub repositories avoiding interactive editors

## [2025-09-22] - Automated licensing based on project analysis

- docs: create cot/licensing.md: automated CoT that applies appropriate licensing (MIT for labour projects, GPLv3 for personal) by analysing indicators in README.md
- docs: implement automatic detection of project nature: look for mentions of "Promad", corporate email vs "@incognia", personal email
- docs: apply complete licensing templates according to rules established in ../../rulesets/LICENSING.md
- docs: generate LICENSE file with full text of the appropriate licence (MIT License or download GPL v3)
- docs: add correct licence footer to README.md with copyright and distribution information
- docs: include programmatic validation to verify correct file creation and change application

## [2025-09-19] - Prioritise daily CoT workflow and add coverage badge

- docs: update README.md: prioritise daily CoT workflow by moving section to a prominent position after the academic overview
- docs: document complete initial setup: clone to ~/rules and create `~/cot` symbolic link for quick access
- docs: specify macOS and Linux compatibility for the symbolic link flow
- docs: add daily usage examples with short paths (~/cot/committing.md, ~/cot/context.md, ~/cot/changelog.md)
- docs: emphasise operational principle: rulesets/ documents for logic vs cot/ CoTs as daily work tools
- docs: include commands to recreate the symbolic link and troubleshooting notes
- docs: add CoT Coverage badge (43%) with ROADMAP link for visual progress tracking
- docs: reorganise README to show workflow as priority information immediately after academic context
- docs: add Mermaid diagrams to visually illustrate the initial setup flow and daily CoT usage flow
- docs: create setup diagram (flowchart TD) showing process from a clean system to complete configuration
- docs: include daily usage diagram (flowchart LR) with the most common CoT options and convergence towards LLM execution
- docs: apply differentiated colours: pink for start, green for success, blue for conceptual references
- docs: integrate diagrams organically with step-by-step commands and invocation examples for better onboarding

- fix: correct symbolic link command in initial setup: use `ln -s ~/rules/prompts/cot cot` (no `~` in destination) for correct local link creation
- fix: update link recreation command to maintain consistency with the corrected syntax
- fix: apply LINGUISTICS.md rules to README.md: correct English calque "desarrollado" → "elaborado" in project footer
- fix: verify all headings and titles (25 lines found): confirm correct sentence-case usage without "Title Case For Every Word"
- fix: validate correct use of technical loanwords in italics (*commit*, *bare-metal*, *CoT*, *pipeline*, etc.) and standard Mexican Spanish terminology

## [2025-09-18] - Comprehensive improvements to context and committing CoTs for infrastructure and multiple accounts

- docs: refine cot/context.md v2.1: add README search in second- and third-level subdirectories for collaborative projects with multiple teams
- docs: extend technical detection to include Kubernetes configuration files throughout the repository (not just root)
- docs: add exhaustive search for kubeconfig, kube.config, and .kubeconfig files at any repository level
- docs: include full search for Talos configurations: talosconfig, talos.config, and .talosconfig for use with EXPORT commands
- docs: extend detection of Kubernetes YAML manifests: search for deployment, service, ingress, configmap, secret at depth
- docs: include detection of standard Kubernetes directories: k8s/, kubernetes/, manifests/
- docs: add support for docker-compose.yaml in addition to docker-compose.yml
- docs: reorganise detection by category: languages/frameworks, containers/orchestration, cluster configuration, CI/CD
- docs: expand findings documentation to include orchestration, cluster configuration, and additional READMEs
- docs: add automatic reading of READMEs found in subdirectories with first 20 lines
- docs: include detection of GitLab CI (.gitlab-ci.yml) in addition to GitHub Actions
- docs: extend cot/context.md to search for AGENTS.md and .warp.md files in the project documentation analysis
- docs: include both variants (standard AGENTS.md and .warp.md as dotfile) in existence check and automatic reading
- docs: add specific references for project configuration and rules in the CoT references section
- docs: create AGENTS.md with a complete guide for future WARP terminal instances in this repository
- docs: include description of repository purpose (technical rules, philosophy, and CoT for LLMs)
- docs: document core philosophy: combat mercenary work, technical selfishness, and cultural identity loss
- docs: specify common development commands: markdown lint (npm run lint:md), link checking, backup scripts
- docs: detail the critical commit flow: update CHANGELOG.md first, then add/commit/push
- docs: document directory architecture: rulesets/ (rules), prompts/ (CoT and templates), scripts/ (tools)
- docs: include dual contexts: personal (@incognia, GPLv3) vs corporate (@incogniadev, MIT)
- docs: specify Chain-of-Thought system with structured format (Reasoning, Steps, Conclusion)
- docs: document critical timezone handling for CST (UTC - 6 hours, never just add suffix)
- docs: include technical specialisation: Kubernetes, GitOps, service meshes, observability
- docs: define 7 key rules including full CoT reading and mandatory CHANGELOG flow

- improve: refine cot/committing.md v1.1: add visual validation of active identity for users with multiple accounts and SSH keys
- improve: include mandatory display of email, name, SSH key, and remote before proceeding with commits
- improve: add critical verification to confirm the displayed identity matches the expected one for the repository
- improve: incorporate specific hints for users with multiple accounts in the conclusions section

## [2025-09-17] - Critical improvements for precise CST timezone calculation and structural reorganisation

- feat: create cot/context.md v2.0: portable generic CoT for any project with automatic technology detection (Node.js, Python, Go, Rust, Java, Docker), structure analysis with tree, cross-platform installation (dnf, apt, apk, pacman, brew), and identification of standard documentation files

- docs: update README.md: add reference to generic context.md CoT in the quick-use section
- docs: update ROADMAP.md: increment CoT statistics (14→15 files, 57%→60% independent), document Sprint 1 progress with completed CoT, and update completed infrastructure with new CoT characteristics
- docs: consolidate ROADMAP.md at root combining CoT infrastructure with specific coverage analysis
- docs: correct markdown lint errors systematically in main files (README, ROADMAP, CHANGELOG, PROMPTS, PHILOSOPHY)
- docs: add blank lines around headings and lists per MD022/MD032
- docs: correct orphaned links after moving rulesets/ROADMAP.md to root
- docs: specify languages in code blocks and correct ordered-list prefixes
- docs: install and configure npm/nodejs for link checking and automatic lint
- docs: create CoT for changelog maintenance in cot/changelog.md with common error corrections: reverse chronological order, precise CST calculation, duplicate detection, and linguistic consistency in Mexican Spanish
- docs: add logical reference in cot/committing.md to the changelog CoT for a coherent update flow
- docs: add repository configuration validation to the committing CoT with reference to git_init CoT for unconfigured repos
- docs: improve validation to detect HTTPS vs SSH remotes: if `git remote -v` shows https:// it indicates incorrect configuration
- docs: update README.md and ROADMAP.md with mentions of the changelog CoT and improvements to the committing CoT with SSH validation
- docs: apply linguistic rules to ROADMAP.md: correct headings to sentence case and add italics to technical loanwords (*Sprint*, *commits*, *timestamps*)
- docs: apply linguistic rules to CHANGELOG.md: add italics to technical loanwords (*commit*, *git log*, *push*, *hook*, *prompt*, *git status*)

- fix: correct broken relative links in cot/changelog.md after initial location change

- refactor: move CRITICAL_COT_READING.md from root to rulesets/ for better organisation
- refactor: consolidate CRITICAL_COMMIT_LANGUAGE.md and COMMIT_LANGUAGE_PROTOCOL.md into unified rulesets/COMMIT_LANGUAGE_PROTOCOL.md
- refactor: clean up repository root by removing duplicate files and moving protocols to rulesets/
- refactor: remove .githooks/ directory and non-functional pre-commit hook to simplify structure
- refactor: update reference in CHANGELOG.md to reflect new file locations
- refactor: remove git hooks section from README.md

- docs: reinforce timezone instructions in cot/committing.md to prevent the common error of labelling CST onto UTC times
- docs: add mandatory verification with `TZ=America/Mexico_City date` to get the real CST time
- docs: include practical conversion examples: UTC 14:30 → CST 08:30, UTC 03:15 → CST 21:15 (previous day)
- docs: emphasise precise mathematical calculation: CST = UTC - 6 hours with correct day-change handling
- docs: update README.md with improved CST date/time section and verification examples
- docs: add command to compare UTC vs CST and mathematical conversion examples

## [2025-09-10] - Improve linguistics CoT and critical fix for commit language rule

- improve: improve cot/linguistics.md with mandatory programmatic validation to prevent superficial application
- improve: add mandatory command `grep -n "^#" file.md` in step 6 for systematic heading validation
- improve: require explicit documentation of each heading found and the correction applied
- improve: add mandatory verification section before completing the CoT
- improve: prevent omission of Title Case correction through forced programmatic verification

- fix: correct inconsistency in commit language rule: ALL commit messages must be in international English
- fix: update cot/committing.md line 15: emphasise «CRITICAL» for commit messages in English
- fix: update reference in rulesets/COMMIT_LANGUAGE_PROTOCOL.md to maintain consistency with the corrected text
- fix: resolve conflict between rules where some documents suggested commits in Spanish vs English
- fix: clarify language distribution: commits in English, documentation in Mexican Spanish

## [2025-08-31] - Complete CHANGELOG restructure

- docs: restructure CHANGELOG.md: correct inverted structure (heading at top), consolidate duplicate sections, eliminate redundancies, standardise format, and group related micro-changes

## [2025-08-29] - Fix format inconsistencies in CHANGELOG

- docs: fix format inconsistencies in CHANGELOG.md (duplicate entry, headings without descriptive titles, and hierarchical structure)

## [2025-08-28] - Specify descriptive title format for CHANGELOG

- docs: add descriptive title rule for CHANGELOG.md headings using format '[YYYY-MM-DD] - Descriptive title of the main change'
- docs: update COMMITTING.md to avoid emojis in CHANGELOG and improve committing.md prompt with git status analysis and multiple commits

## [2025-08-25] - Fix interactive editors and personal SSH configuration

- docs: correct COMMITTING.md and cot/committing.md to eliminate use of interactive editors, especially with git log (use --no-pager)
- docs: document common `quote>` issue in git commit from incorrect quote escaping in messages

- fix: configure personal repository to use personal identity `incognia@gmail.com` and personal SSH key (id_ed25519) instead of labour credentials

## [2025-08-18] - Reorganise prompts, CoT, and documentation improvements

- docs: README.md: update title to «Technical rules: prompts and CoT to accelerate LLM context» and add brief definitions of «prompt» and «CoT» at the start
- docs: LINGUISTICS.md: correct capitalisation in «Estados Unidos» and add note on geopolitical proper nouns («Estado de México», «Estados Unidos»)
- docs: LINGUISTICS.md: add «Writing subtleties» (do not start a sentence with a figure; avoid ending paragraphs with symbols/abbreviations such as % or «etc.»; use «por ciento» and «etcétera»)
- docs: PHILOSOPHY.md: replace straight quotes with angular quotes («Agüelo», «Hagrid») per LINGUISTICS.md
- docs: CORPORATE.md: align with LINGUISTICS.md (sentence-case title with em dash, angular quotes, typographic loanwords, «nube pública» instead of «cloud público»)
- docs: TEACHING.md: align with LINGUISTICS.md (lower case after colon, translations in table, «preparación» instead of «setup»)
- docs: cot/linguistics.md: extend checklist to cover all LINGUISTICS.md rules in logical order (calques, terminology, verbs, loanwords, typography, quotes, subtleties, acronyms, tenses, CST dates, naming, dislikes, expressions)
- docs: COMMITTING.md: simplify flow to simple push (`git push`) and link to initial configuration in GIT.md
- docs: GIT.md: add interactive post-`git init` assistant (configures identity, `core.sshCommand`, and optional SSH remote)
- docs: cot/committing*.md: align to simple push and clean up artefacts
- docs: cot/committing_{personal,corporate}.md: consolidate into cot/committing.md and update references
- docs: cot/git_init.md: new CoT to initialise repos with SSH following GIT.md
- docs: prompts/: create subdirectory structure (templates/, guides/, actions/, snippets/) with examples and README per folder
- docs: PROMPTS.md: add catalogued index of prompts by subdirectory
- docs: BACKUPS.md: extend with restore, verification, zstd, incremental rsync, encryption/offsite, systemd, and security/permissions; checksum policy only for files > 100 MB
- docs: cot/backup.md and cot/restore.md: new CoTs to execute backups and restores
- docs: BACKUPS.md: document quick backup in the same directory and its usage
- docs: cot/quick_backup.md: new CoT for quick same-dir backup
- docs: Reorganisation: move thematic documents to ./rulesets/ keeping PHILOSOPHY.md at root
- docs: Links: correct cross-references to moved documents in README.md, PHILOSOPHY.md, PROMPTS.md, and prompts/* (cot, guides, actions)
- docs: CHANGELOG.md: record daily update with no functional changes
- docs: cot/committing_personal.md and cot/committing_corporate.md: removed; use cot/committing.md
- docs: README.md: add note to disable MD041 after the `---` frontmatter block in CoT, ensuring correct rendering
- docs: cot/*: MD041 audit in CoT; confirmed correct placement of the tag immediately after the frontmatter close
- docs: style(md): fix trailing spaces (MD009) in multiple files (rulesets/*, cot/*, VAULT.md, LINGUISTICS.md, LICENSING.md)
- docs: style(md): fix MD012 (remove consecutive blank lines) in TEACHING.md, BACKUPS.md, and cot/lint.md
- docs: style(md): fix MD022 (blank lines around headings) in multiple documents (ATTRIBUTION.md, BACKUPS.md, STYLING.md, TEACHING.md, LINGUISTICS.md, LICENSING.md, PHILOSOPHY.md)

- feat: scripts/git-init-context.sh: interactive assistant to configure identity and SSH (per repo) and optional SSH remote
- feat: scripts/backup_file.sh: file/directory backup with zstd compression and size-conditional checksums
- feat: scripts/backup_rsync_snapshot.sh: daily incremental snapshots with rsync --link-dest
- feat: scripts/verify_backups.sh: bulk checksum verification
- feat: scripts/quick_bkp.sh: quick backup in the same directory with CST date (YYYY-MM-DD)

- chore: add Markdown linter configuration (.markdownlint.yaml) aligned to the repo style
- chore: add link checker (.markdownlinkcheck.json) with timeout adjustments and headers for shields.io
- chore: initialise package.json with scripts: `lint:md`, `lint:md:fix`, `check:links`

- ci: clean up repo: add .gitignore to exclude node_modules/ and artefacts; remove node_modules/ from version control with `git rm -r --cached`
- ci: npm install: E404 error when trying to install non-existent package `markdownlint-cli2-fix@^0.3.0`; removed from package.json
- ci: update npm scripts: `lint:md` uses markdownlint-cli2 without globs (invoked with npx "**/*.md" "#node_modules")
- ci: run Markdown linter: `npx markdownlint-cli2 "**/*.md" "#node_modules"` → 938 errors in 40 files
  - Main rules: MD013 (line-length), MD022/MD032 (blank lines around headings/lists), MD040/MD031 (code blocks without language and without blank lines), MD041 (H1 on first line in prompts), MD024 (duplicate headings in CHANGELOG)
- ci: quick fix: adjust link in README.md to `./rulesets/STYLING.md` to avoid 404
- ci: proposed pending items: relax MD013 to 120, disable MD041 in `prompts/**`, allow MD024 in CHANGELOG, add language to code blocks and blank lines around headings/lists

## [2025-08-17] - Generic CoT implementation and 90-day roadmap

- docs: cot/repo_context.md: generic CoT to obtain complete context from GitHub/GitLab repos (structure, dependencies, CI/CD, deployment, style, tests, licences, and contribution)
- docs: PROMPTS.md: initial CoT guide (format, style, references) in es_MX; add section of reference paths «~/rules...»
- docs: cot/_template.md: add use of «~/rules...» paths. Initial examples: arithmetic (renamed from aritmetica), devops, kubernetes, linguistics, styling, and committing (personal/corporate) with cross-references added
- docs: GLOSSARY.md: add term «Cadena de razonamiento (Chain-of-Thought, CoT)» with references to PROMPTS.md and arXiv
- docs: LINGUISTICS.md: fix quotes; clarify verb tenses; add CST date/time section
- docs: COMMITTING.md: explicit commands with TZ=America/Mexico_City; non-interactive flow for CHANGELOG
- docs: STYLING.md: CST timestamp examples (short and long format in es_MX)
- docs: README.md: date/time conventions section (CST) and link to LINGUISTICS; links to ROADMAP and TODO; chain-of-thought note (Wei et al., arXiv:2201.11903)
- docs: PHILOSOPHY.md: references to ROADMAP and TODO in universal rules
- docs: ROADMAP.md: created 90-day roadmap (CoT, evaluation, automation)
- docs: TODO.md: created tactical CoT plan (immediate tasks)
- docs: TEACHING.md: restore ethical emphasis on exclusive use of free software in K-12 and outreach; writing and cross-cutting principle improvements (bilingualism, reproducibility, accessibility, CST)

- feat: .githooks/pre-commit: optional hook to block 'CST' without TZ=America/Mexico_City in added lines

## [2025-08-01] - Refine LINGUISTICS.md and develop TEACHING.md

- fix: correct terminology in LICENSING.md: change «desarrollado por» to «elaborado por»
- fix: align terminology with technologist profile instead of developer
- fix: apply correction to both labour and personal projects

- docs: add precision in LINGUISTICS.md to avoid over-correction of third-level headings (###)
- docs: add specific rule about NOT correcting capitalisation in already-correct ### headings
- docs: include clear examples of correct and incorrect third-level headings
- docs: extend PHILOSOPHY.md introduction with professional-educational duality
- docs: add characteristic nicknames ("Agüelo" at work, "Hagrid" in the classroom) to reinforce dual identity
- docs: connect the fight against endemic problems with the democratisation of technical knowledge
- docs: maintain irreverent tone and Mexican Spanish per LINGUISTICS.md
- docs: improve writing of the professional-educational duality paragraph with a more natural flow
- docs: refine Mexican expressions and direct connection with the fight against code mercenary work
- docs: soften the transition between the irreverent introduction and the technical section
- docs: eliminate redundancies between the introduction and the professional-educational intersection section
- docs: better integrate the duality of contexts with the general philosophical message
- docs: extend the technical bilingualism section with the reality of English among Mexican students
- docs: add reflection on cultural vs geographical distance with the US in an educational context
- docs: correct punctuation and grammar in the educational context section
- docs: add a quote as an epigraph on technological and scientific progress
- docs: improve epigraph writing to include technological development and scientific discoveries
- docs: add file naming rule in international English in LINGUISTICS.md
- docs: add specific rule for Markdown files with NAMES_IN_UPPERCASE.md
- docs: correct incorrect use of upper case after colons in LINGUISTICS.md
- docs: correct additional capitalisation in the file naming and special dislikes section
- docs: add extra emphasis to the upper-case-after-colon rule as it is a frequent error
- docs: add examples of correct and incorrect usage for upper case after colons
- docs: add rule on verb tenses in documents: past tense for reports, second person for guides
- docs: include specific examples to differentiate reports (past tense) vs guides (second person)
- docs: emphasise avoiding impersonal third person in both document types
- docs: specify in COMMITTING.md that CHANGELOG.md must use date only, without time
- docs: add missing GIT.md to the list of included documents in README.md
- docs: add CHANGELOG.md to the universal rules references in PHILOSOPHY.md
- docs: change README.md title to reflect the professional and academic role of a technologist
- docs: develop TEACHING.md with a detailed educational profile based on the Juno project
- docs: include innovative pedagogical methodologies using DevOps tools
- docs: document the Juno project as the main case study in STEM education
- docs: add the Chicxulub project as a case study in interdisciplinary science outreach: programming + geography + Earth sciences focus, outreach impact metrics, and historical contextualisation methodology
- docs: add quantitative educational impact metrics (6+ years, 50+ students, 100+ containers) and specify technical tools (Docker, JupyterLab, Python)
- docs: include science outreach philosophy and contributions to the educational community
- docs: emphasise mandatory CHANGELOG.md update in COMMITTING.md with a step-by-step process
- docs: add warnings and correct flow examples to avoid oversights in future updates

- docs: add philosophy of free tools as a fundamental part of the educational methodology
- docs: emphasise exclusive use of free software in educational environments
- docs: clarify commitment to GPL licensing for all educational content
- docs: document principles of software freedom applied to pedagogy
- docs: add cross-platform educational philosophy (Linux, Windows, Mac)
- docs: include analogy of tools to justify teaching on multiple operating systems
- docs: document critical stance on overpricing and ethics of closed platforms
- docs: emphasise teaching WSL on Windows as a bridge to Unix environments
- docs: refine writing and structure of the cross-platform philosophy with clear sections
- docs: remove redundancies in fundamental principles of technical competence

- fix: correct TEACHING.md to comply with LINGUISTICS.md rules: italics for technical terms (*hands-on*), anglicisms (troubleshooting → resolución de problemas, feedback → retroalimentación), loanword format
- fix: correct teaching experience in TEACHING.md from 6+ years to 8 years and update educational impact metrics
- fix: correct terminology in TEACHING.md: "backup" → "respaldo", "debugging" → "depuración", "implementación" → "aplicación", "realizar" → "hacer", "Soporte" → "Compatibilidad"
- fix: reorganise logical structure of TEACHING.md: philosophy → specialisation → competencies → projects → context → outreach
- fix: extend teaching experience with Montessori approaches, active secondary schools, and social programmes for vulnerable populations
- fix: add professional-educational intersection section to PHILOSOPHY.md connecting DevOps with pedagogy
- fix: correct typo in PHILOSOPHY.md: "intersacción" → "intersección"
- fix: correct CST timezone specifications in multiple documents (BACKUPS.md, COMMITTING.md, STYLING.md): warning on correct UTC-6 conversion, use of TZ="America/Mexico_City", practical example 22:21 UTC → 16:21 CST

## [2025-07-31] - Separate GIT/COMMITTING and establish backup policies with CST

- docs: add reference to BACKUPS.md in README.md and PHILOSOPHY.md
- docs: include BACKUPS.md in the universal rules section that apply to both contexts
- docs: specify mandatory use of CST Ciudad de México timezone in COMMITTING.md for CHANGELOG.md dates
- docs: add context-specific SSH commands in COMMITTING.md (personal vs labour)
- docs: create GIT.md with initial GitHub and GitLab account configuration

- refactor: separate responsibilities between GIT.md (initial setup) and COMMITTING.md (daily flow)
- refactor: remove redundancies between both documents
- refactor: focus GIT.md on configuration of new repositories
- refactor: focus COMMITTING.md on the commit and push workflow
- refactor: clearly differentiate between AUTHORING.md and LICENSING.md by their specific purposes
- refactor: refactor ATTRIBUTION.md for personal attribution in individual documents/scripts (personal projects only)
- refactor: refactor LICENSING.md for LICENSE generation in complete projects (personal and labour)
- refactor: specify that ATTRIBUTION.md is used exclusively in personal context
- refactor: specify that LICENSING.md applies to both contexts
- refactor: rename AUTHORING.md to ATTRIBUTION.md to better reflect its purpose
- refactor: organise documents in README.md and PHILOSOPHY.md by usage: universal, dual, personal only, labour only
- refactor: clearly classify GIT.md as a universal rule
- refactor: classify CORPORATE.md as a dual-use rule
- refactor: specify ATTRIBUTION.md as exclusively personal use
- refactor: specify STYLING.md as exclusively labour use

- fix: correct use of upper case after colons in README.md to comply with LINGUISTICS.md
- fix: rename COMMITING.md to COMMITTING.md to correct a spelling error

- feat: create BACKUPS.md with backup and destructive operation policies, mandatory CST timezone, and scripts updated with TZ="America/Mexico_City"
- feat: add informational badges to README.md (GPLv3 licence, Markdown, Mexican Spanish) and decision flow section for dual-use rules

- style: create STYLING.md with style rules for labour Markdown documents: corporate palette (midnight, electric, lavender), standard structure for headers/footers, dynamic CST timestamp in Mexican Spanish
- style: change icon colour in contact section to --promad for visual consistency

- docs: update PHILOSOPHY.md to reflect COMMITTING.md rename and add reference to STYLING.md with labour scope
- docs: improve CSS colour documentation with descriptive naming
- docs: clarify that licence information and timestamps must be dynamic, not hardcoded

## [2025-01-30] - Final capitalisation corrections and alignment with LINGUISTICS

- fix: correct use of upper case after colons in ATTRIBUTION.md to comply with LINGUISTICS.md rules
- fix: correct use of upper case after colons in GLOSSARY.md to comply with LINGUISTICS.md rules
- fix: correct remaining cases of upper case after colons in ATTRIBUTION.md (professional specialisation section)
- fix: correct capitalisation of title in README.md ("Ingeniero" → "ingeniero")

- feat: create parametrised git-init skill with 4 arguments: context (personal/laboral), SSH key, remote URL, and branch

- style: adjust README.md for better alignment with LINGUISTICS.md (use of lower case in lists and correction of "acomplejos")
- style: update link format in PHILOSOPHY.md to match README.md style

---

<!-- markdownlint-disable MD036 -->
*Written by Rodrigo Álvarez (@incognia)*
