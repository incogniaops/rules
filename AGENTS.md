# AGENTS.md

This file provides guidance to AI coding agents when working with code in this repository.

## Repository overview

This is the `rules` repository containing technical standards, philosophy, and Chain-of-Thought (CoT) prompts that guide professional and academic work for Rodrigo Álvarez (@incognia). It serves as structured context for LLMs and maintains consistency across personal and corporate projects.

## Core philosophy

The repository combats three endemic problems in Latin American technology:

- **Mercenary work**: mediocre work without real commitment
- **Technical selfishness**: hoarding knowledge to create artificial dependencies
- **Cultural identity loss**: abandoning Spanish cultural identity for perceived professional advancement

Language policy is context-based:

- **Personal context**: documentation and `CHANGELOG.md` in **Mexican Spanish**; code and commits in **International English**.
- **Corporate context**: **100% International English** (documentation, `CHANGELOG.md`, code, and commits).

## Common development tasks

### Linting and quality checks

```bash
# Lint all Markdown files
npm run lint:md

# Check all markdown links
npm run check:links
```

### Working with documentation

Documentation follows strict linguistic rules from `rulesets/LINGUISTICS.md` and the active context:

- Personal: use **Mexican Spanish** terminology and expressions.
- Corporate: use **International English** consistently.
- Apply correct capitalisation (only the first word and proper nouns in titles).
- Use angular quotes «» in Spanish text, double quotes "" only in code.
- Calculate CST timezone correctly (UTC - 6 hours, not just appending "CST").

### Backup operations

```bash
# Backup individual files/directories with checksums
./scripts/backup_file.sh [source_path]

# Create incremental daily backups with rsync
./scripts/backup_rsync_snapshot.sh [source] [destination]
```

### Commit workflow (CRITICAL)

**MANDATORY PROCESS - Always follow this exact order:**

1. **FIRST**: Update `CHANGELOG.md` through `changelogger` in the active context language (personal: Mexican Spanish, corporate: International English). The `commit` skill only validates this prerequisite.
2. **SECOND**: Analyse changed files with `git status`, group them by logical type, and validate that `CHANGELOG.md` has a staged or unstaged diff before staging
3. **THIRD**: Stage selectively per logical group: `git add file1 file2` — never `git add .` across mixed change types
4. **FOURTH**: Resolve the current session's co-author, rewrite `/tmp/commit-msg.txt` for the staged group, and commit atomically: `git commit -F /tmp/commit-msg.txt`
5. **FIFTH**: Push all commits: `git push`

**Date calculation for CHANGELOG.md:**

```bash
# Get correct CST date (never use UTC with "CST" suffix)
DATE_CST=$(TZ=America/Mexico_City date +"%Y-%m-%d")
```

**Commit message rules:**

- Always use **International English** for commit messages
- Follow [Conventional Commits](https://www.conventionalcommits.org/) specification
- Use non-interactive commands: `git --no-pager log --oneline -5`

### Commit attribution

Before each commit in Codex, Claude Code, or GitHub Copilot CLI, run:

```bash
python3 ~/rules/scripts/commit_trailer.py
```

Use stdout only when the helper succeeds. It reads the active session and generates `Co-Authored-By: [<Tool> ]<Model> (<effort>) <email>`, for example `Codex GPT-6.1 Sol (high)`, `Claude Opus 5.5 (medium)`, or `Copilot GPT-6 Luna (low)`. These are format examples; resolve the actual identity again for every commit.

- If multiple tool identifiers are present, rerun with `--tool codex`, `--tool claude`, or `--tool copilot`, matching the tool executing the commit.
- If effort is unavailable, use the verified model without parentheses. If detection fails, report the limitation and use an attribution supplied by the active tool or harness in the shared format; if the model remains unverified, omit the trailer.
- Never infer the model or effort from previous commits, another session, examples, or configuration defaults. The helper rejects an invalid latest model rather than reusing an earlier identity; Claude's synthetic placeholders and sidechain turns are excluded from model selection.

Provider emails, session identifiers, filtering, and fallback behaviour are defined in [COMMITTING.md — Agent attribution](./rulesets/COMMITTING.md#26-agent-attribution). Keep that ruleset as the detailed reference.

## Architecture and structure

### Directory organisation

```text
├── rulesets/           # Core rules and documentation
│   ├── LINGUISTICS.md      # Mexican Spanish language standards
│   ├── COMMITTING.md       # Git workflow and CHANGELOG rules
│   ├── LICENSING.md        # Licensing strategy (GPLv3 personal, MIT corporate)
│   └── [other standards]
├── cot/                # Chain-of-Thought reasoning prompts
│   ├── committing.md       # Git commit workflow with SSH validation
│   ├── context.md          # Project context detection
│   ├── changelog.md        # CHANGELOG maintenance
│   ├── linguistics.md      # Mexican Spanish rules application
│   └── [other CoTs]
├── templates/          # Reusable document templates
├── scripts/            # Utility scripts for backups and automation
├── .agents/skills/     # AI agent-discoverable skills (see below)
└── .warp/workflows/    # Parameterised command workflows (see below)
```

### Context switching (personal vs corporate)

The repository supports dual contexts with different rules:

**Personal projects (`@incognia`)**:

- Licence: GPLv3 (copyleft)
- Email: <incognia@gmail.com>
- SSH key: ~/.ssh/incognia
- Documentation: Mexican Spanish

**Corporate projects (`@incogniaops` for Elsevier)**:

- Licence: MIT (permissive)
- Email: <r.alvarez1@elsevier.com>
- SSH key: ~/.ssh/elsevier
- Documentation: International English with STYLING.md rules

### Chain-of-Thought (CoT) system

The repository implements structured reasoning prompts following this format:

```markdown
---
domain: [project area]
task: [specific task]
difficulty: [basic|intermediate|advanced]
priority: [critical|high|medium|low]
---

# CoT: [descriptive title]

## Reasoning
[Brief mental framework of approach]

## Steps
1. Action: [what to do]
   Result: [expected outcome]

## Conclusion
[Clear, verifiable final answer]
```

Key CoT files:

- `cot/context.md` - Get project context quickly
- `cot/committing.md` - Git workflow with SSH validation
- `cot/linguistics.md` - Apply Mexican Spanish rules
- `cot/changelog.md` - Maintain CHANGELOG.md

## Skills

Skills are lightweight, agent-discoverable instruction sets in `.agents/skills/`. Each skill references detailed CoTs and rulesets without duplicating content.

Available skills:

- **commit** — Full commit workflow with CHANGELOG validation and attribution from the active model and reasoning effort
- **changelogger** — CHANGELOG.md maintenance with CST dates (optional `utc`, `est`, `ist`)
- **linguistics** — Apply Mexican Spanish linguistic rules
- **linguistica** — Spanish alias of `linguistics` with its own skill identifier
- **context** — Quick project context detection
- **backup** — File/directory backup with standard naming
- **licensing** — Apply the correct licence based on project context (GPLv3 vs MIT)
- **git-init** — Initialise a repository with SSH, identity, and remote by context
- **ssh-import** — Import an SSH public key from GitHub into the current server
- **release** — Non-interactive semantic release with tag and notes validation
- **aws-naming** — Normalise filenames for S3 and CloudFront with a `.tsv` audit log
- **mail** — Compose and send OWA-compatible HTML email (`owa`, `mac`, `graph`)
- **bmail** — Compose structured business-email drafts in English from templates
- **styling** — Apply corporate Markdown styling by platform (HedgeDoc, GitLab, GitHub)
- **kube** — Kubernetes cluster analysis over SSH
- **kubetbs** — Kubernetes microservice troubleshooting across namespaces
- **tio-readiness** — Assess whether an AWS infrastructure specification is ready to implement under TIO conventions

Invoke with the tool-specific prefix:

- **Claude Code**: `/commit`, `/changelogger`, etc. (slash command via `~/.claude/commands/`)
- **GitHub Copilot CLI**: `/commit`, `/changelogger`, etc.; discovers the shared skills copied to `~/.agents/skills/` directly
- **Codex**: `$commit`, `$changelogger`, etc. (`$` prefix)
- **Warp**: `/skill-name` slash command or via the Agents panel; the Warp agent auto-discovers skills from `~/.agents/skills/` and picks the right one by context

## Workflows

Parameterised commands in `.warp/workflows/` for frequent operations:

- **backup_file** — Backup a file or directory with checksums
- **lint_markdown** — Run markdownlint on all files
- **commit_flow** — Complete commit flow with type and description
- **cst_date** — Get current date/time in CST (México City)

## Time and date handling (CRITICAL)

**Never append "CST" to UTC times without calculation.**

**Correct conversion**: CST = UTC - 6 hours

- UTC 14:30 → CST 08:30
- UTC 03:15 → CST 21:15 (previous day)

**Commands for correct CST time:**

```bash
# Always use this for accurate CST dates
TZ=America/Mexico_City date +"%Y-%m-%d %H:%M %Z"

# For CHANGELOG.md (date only)
TZ=America/Mexico_City date +"%Y-%m-%d"

# Verify conversion
echo "UTC: $(date -u '+%H:%M')" && echo "CST: $(TZ=America/Mexico_City date '+%H:%M')"
```

## Technical specialisation context

Primary focus areas reflected in the documentation:

- **Kubernetes on bare-metal Proxmox**: kubeadm, containerd, cloud-init
- **GitOps automation**: Argo CD, Helm charts, versioned manifests
- **Service mesh networking**: Istio, Envoy, Cilium, MetalLB
- **Observability**: Prometheus, Grafana, OpenTelemetry, distributed tracing
- **Enterprise CI/CD**: Jenkins, GitLab CI with GitOps integration

## Key rules to follow

1. **CRITICAL**: Always read complete CoT files from line 1 to end when referenced - never assume based on partial reading
2. **CRITICAL**: Update CHANGELOG.md BEFORE every commit - this is mandatory workflow
3. **CRITICAL**: Convert UTC to CST by subtracting 6 hours - never just append "CST" suffix
4. **Language**: personal context → documentation/CHANGELOG in Mexican Spanish + code/commits in International English; corporate context → 100% International English
5. **Markdown**: Use the `.yaml` extension (never `.yml`), always use Mermaid for diagrams (never ASCII)
6. **Commits**: Non-interactive only, use conventional commits format
7. **Files**: Markdown files use UPPERCASE.md format (README.md, PHILOSOPHY.md, etc.)

## Integration with other repositories

When working in other projects, reference this repository:

- Path convention: `~/rules/rulesets/LINGUISTICS.md`
- Philosophy: `~/rules/PHILOSOPHY.md`
- Commit rules: `~/rules/rulesets/COMMITTING.md`
- Templates: `~/rules/templates/`
- CoTs: `~/rules/cot/`

---

## Claude Code specifics

> **Note for non-Claude agents:** This section applies exclusively to Claude Code (CLI/IDE). Other AI tools can safely skip it.

This file is symlinked as `CLAUDE.md` so Claude Code loads it automatically as project context.

### Skill invocation

`scripts/sync_global.sh` copies repository skills to `~/.agents/skills/`, then links each copied `SKILL.md` to `~/.claude/commands/<name>.md`. Invoke them with the `Skill` tool or the `/name` slash command:

- `/commit` — full commit workflow (reads `cot/committing.md`)
- `/changelogger` — CHANGELOG maintenance (reads `cot/changelog.md`)
- `/linguistics <file>` — apply Mexican Spanish rules
- `/context` — detect project context
- `/release <semver>` — publish a semantic release

Always invoke skills through the `Skill` tool rather than reading CoT files directly — the skill handles the mandatory gates and anti-error protocol.

### Atomic commits (enforced)

Each commit must represent a single logical change type. Workflow:

1. Run `git status` and classify each changed file by type (`feat`, `docs`, `fix`, etc.)
2. Stage one group: `git add file1 file2`
3. Write `/tmp/commit-msg.txt` and commit: `git commit -F /tmp/commit-msg.txt`
4. Repeat for the next group before pushing
5. Push once all atomic commits are done: `git push`

Never use `git add .` when the working tree contains mixed change types.

**Anti-pattern — stale commit subject**: `/tmp/commit-msg.txt` persists across invocations in the same session. Always rewrite the subject line from scratch for each commit; never assume it matches the current staged changes. Verify subject matches staged files before running `git commit -F`.

### Memory

Project memory lives at `~/.claude/projects/-Users-alvarezr3-rules/memory/`. Check `MEMORY.md` there for stored feedback and preferences before starting non-trivial work.

---

## Codex specifics

> **Note for non-Codex agents:** This section applies to OpenAI Codex CLI. Other AI tools can safely skip it.

Skills are synced to `~/.codex/agents/skills/<name>/SKILL.md` by `scripts/sync_global.sh`.

### Skill invocation in Codex

Codex uses `$` as the prefix for custom skills — **not** `/`:

| Prefix | What it does |
| ------ | ------------ |
| `$name` | Invokes a custom skill from `~/.codex/agents/skills/` (e.g. `$commit`, `$changelogger`) |
| `/command` | Built-in Codex commands only — `/resume`, `/title`, `/help`, `/plugins`, `/share`, etc. |

To invoke the `changelogger` skill explicitly in Codex, use `$changelogger`. `/changelogger` is the Claude Code and Copilot form.

**Auto-discovery**: skills can also be triggered by describing the task in natural language; Codex matches the description against skill metadata and loads the appropriate `SKILL.md` automatically.

**There is no way to define custom `/` slash commands in Codex.** The `/` namespace belongs to Codex built-ins only.

### Sync command

```bash
~/rules/scripts/sync_global.sh
```

This first refreshes the copies from the repository into `~/.agents/skills/`, then links their `SKILL.md` files into `~/.codex/agents/skills/`. Re-run after pulling updates or changing skills. The attribution helper is accessed directly from `~/rules/scripts/`.
