# Global synchronisation mechanism

*Last modified: 30 March 2026 (CST)*

This document describes in detail how `scripts/sync_global.sh` works: what it copies, where it copies to, how it detects the platform, and why each design decision exists.

## Purpose

Warp and other AI agents discover *skills* and *workflows* from fixed paths in the user's filesystem. The `rules` repository stores them under version control in `.agents/skills/` and `.warp/workflows/`, but those paths are only useful within the repository itself. `sync_global.sh` bridges that gap: it copies the artefacts to the global paths each tool and platform expects.

## What is synchronised and what is not

| Artefact | Synchronised? | Destination |
|----------|---------------|-------------|
| *Skills* (`.agents/skills/*/SKILL.md`) | Yes | Varies by platform (see table below) |
| *Workflows* (`.warp/workflows/*.yaml`) | Yes | Varies by platform (see table below) |
| `scripts/` | No | Accessed directly from `~/rules/scripts/` |
| `templates/` | No | Accessed directly from `~/rules/templates/` |
| `rulesets/` | No | Accessed directly from `~/rules/rulesets/` |
| `cot/` | No | Accessed directly from `~/rules/cot/` |

Artefacts that are **not** synchronised do not need to be on a global path because they are always referenced via canonical paths such as `~/rules/rulesets/X.md`.

## General execution flow

```mermaid
flowchart TD
    A([Script invoked]) --> B[Detect repository root]
    B --> C{".agents/skills/ and .warp/workflows/ exist?"}
    C -->|No| D{"~/rules/.agents/skills/ exists?"}
    D -->|No| E([Error: clone first])
    D -->|Yes| F[REPO_ROOT = ~/rules]
    C -->|Yes| G[REPO_ROOT = script directory]
    F --> H[Detect platform]
    G --> H
    H --> I[Calculate destinations]
    I --> J[Sync skills]
    J --> K[Sync workflows]
    K --> L([Sync complete])

    style A fill:#d0e8ff,stroke:#336
    style L fill:#d0ffd0,stroke:#363
    style E fill:#ffd0d0,stroke:#633
```

## Repository root detection

The script determines its location with:

```bash
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
```

This allows it to be invoked from any directory: both `./scripts/sync_global.sh` (from the repo root) and `~/rules/scripts/sync_global.sh` (from anywhere) produce the same result. If the calculated path does not contain the expected directories, it falls back to `~/rules`.

## Platform detection

Detection uses `uname -s` as the base, with a special case for WSL within the `Linux` branch:

```mermaid
flowchart TD
    A[uname -s] --> B{Result}
    B -->|Darwin| C[PLATFORM = macos]
    B -->|Linux| D{WSL?}
    D -->|grep -qi microsoft /proc/version| E[PLATFORM = wsl]
    D -->|WSL_DISTRO_NAME defined| E
    D -->|Neither condition| F[PLATFORM = linux]
    B -->|MINGW* / MSYS* / CYGWIN*| G[PLATFORM = windows]
    B -->|Other| H[PLATFORM = unknown]

    style C fill:#ffe0b0,stroke:#963
    style E fill:#b0d0ff,stroke:#336
    style F fill:#d0ffb0,stroke:#363
    style G fill:#e0d0ff,stroke:#639
    style H fill:#f0f0f0,stroke:#999
```

The WSL/Linux separation is critical: although `uname -s` returns `Linux` in both cases, Warp runs on **Windows** inside a WSL environment and needs to read *skills* from the Windows filesystem, not the Linux one.

## Destinations by platform

### *Skills*

*Skills* must be in a path that Warp (or another agent) can discover globally. On WSL the Linux path (`~/.agents/skills/`) is invisible to Warp, so the destination is the Windows home directory:

```mermaid
flowchart LR
    SRC[".agents/skills/\n(in the repo)"]

    SRC --> MAC["macOS\n~/.agents/skills/"]
    SRC --> LIN["Native Linux\n~/.agents/skills/"]
    SRC --> WSL["WSL\n%USERPROFILE%\\.agents\\skills\\\nvia wslpath + cmd.exe"]
    SRC --> WIN["Native Windows\n%USERPROFILE%\\.agents\\skills\\"]

    style SRC fill:#fff8c0,stroke:#996
    style MAC fill:#ffe0b0,stroke:#963
    style LIN fill:#d0ffb0,stroke:#363
    style WSL fill:#b0d0ff,stroke:#336
    style WIN fill:#e0d0ff,stroke:#639
```

On WSL, the Windows home directory is resolved at runtime:

```bash
WIN_HOME="$(wslpath "$(cmd.exe /C "echo %USERPROFILE%" 2>/dev/null | tr -d '\r')")"
SKILLS_DST="$WIN_HOME/.agents/skills"
```

`cmd.exe /C "echo %USERPROFILE%"` returns the Windows path (e.g. `C:\Users\incognia`), and `wslpath` converts it to the equivalent Linux path (`/mnt/c/Users/incognia`).

### *Workflows*

Warp *workflows* have different paths on each platform, dictated by operating system conventions:

```mermaid
flowchart LR
    SRC[".warp/workflows/\n(in the repo)"]

    SRC --> MAC["macOS\n~/.warp/workflows/"]
    SRC --> LIN["Native Linux\n$XDG_DATA_HOME/warp-terminal/workflows/\nor ~/.local/share/warp-terminal/workflows/"]
    SRC --> WSL["WSL\n(same as native Linux;\nworkflows are read by the WSL session)"]
    SRC --> WIN["Native Windows\n$APPDATA\\warp\\Warp\\data\\workflows\\"]

    style SRC fill:#fff8c0,stroke:#996
    style MAC fill:#ffe0b0,stroke:#963
    style LIN fill:#d0ffb0,stroke:#363
    style WSL fill:#b0d0ff,stroke:#336
    style WIN fill:#e0d0ff,stroke:#639
```

> **Note on WSL and *workflows*:** unlike *skills*, *workflows* are synchronised to the Linux home because Warp loads them from the active WSL session, not from Windows.

## Copied structure

Each *skill* is a directory containing at least one `SKILL.md`. The script copies the entire directory, preserving any additional files (templates, helper scripts):

```text
.agents/skills/
├── commit/
│   └── SKILL.md          ← copied in full to $SKILLS_DST/commit/
├── changelog/
│   └── SKILL.md
├── context/
│   └── SKILL.md
└── ...
```

*Workflows* are flat YAML files copied directly to the destination directory:

```text
.warp/workflows/
├── backup_file.yaml       ← copied to $WORKFLOWS_DST/
├── commit_flow.yaml
├── cst_date.yaml
└── lint_markdown.yaml
```

## Update flow

After any `git pull`, re-running the script is sufficient. Because it uses `cp -r`, it overwrites existing files without needing to clean the destination manually:

```mermaid
sequenceDiagram
    actor U as User
    participant G as GitHub
    participant R as ~/rules (local)
    participant S as sync_global.sh
    participant D as Global destination

    U->>G: git pull origin main
    G-->>R: changes downloaded
    U->>S: ~/rules/scripts/sync_global.sh
    S->>R: reads .agents/skills/ and .warp/workflows/
    S->>D: cp -r (overwrites)
    D-->>U: skills and workflows updated
```

## Invocation modes

```bash
# From the cloned repo root
./scripts/sync_global.sh

# From any directory (canonical path)
~/rules/scripts/sync_global.sh

# Without cloning — direct remote execution
bash <(curl -sL https://raw.githubusercontent.com/incognia/rules/main/scripts/sync_global.sh)

# Full update in a single command
git -C ~/rules pull && ~/rules/scripts/sync_global.sh
```

## Claude Code integration

After syncing skills to `~/.agents/skills/`, the script creates symlinks so that Claude Code can discover each skill as a slash command.

### How it works

For every skill directory found in `~/.agents/skills/`, the script creates a symlink:

```text
~/.claude/commands/<name>.md  →  ~/.agents/skills/<name>/SKILL.md
```

This means the skill's instruction file is not copied — it is linked. Any update to the skill (via `sync_global.sh`) is reflected immediately in Claude Code without a separate step.

### Paths

| Element | Path |
|---------|------|
| Source (skill file) | `~/.agents/skills/<name>/SKILL.md` |
| Destination (Claude Code command) | `~/.claude/commands/<name>.md` |

### Invocation in Claude Code

Once the symlinks exist, each skill is available as a slash command in Claude Code:

```text
/commit       →  runs the commit skill
/changelogger →  runs the changelogger skill
/linguistics  →  runs the linguistics skill
```

Skills can also be invoked programmatically via the `Skill` tool in the Claude Code agent.

## References

- Source script: [`scripts/sync_global.sh`](../scripts/sync_global.sh)
- Repository skills: [`.agents/skills/`](../.agents/skills/)
- Repository workflows: [`.warp/workflows/`](../.warp/workflows/)
- Initial setup: [`~/rules/README.md`](../README.md) — «Initial setup» section
