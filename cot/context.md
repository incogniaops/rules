---
domain: project
task: get_context
target: current_directory
difficulty: basic
priority: critical
estimated_time: 10-15 minutes
last_updated: 2025-09-18
version: "2.1"
---
<!-- markdownlint-disable MD041 -->

# CoT: get context for the current project

## Purpose

Obtain full project context in the current directory through:

- Identifying project location and structure
- Analysing primary documentation files and subdirectory docs
- Understanding purpose, current status, and planning
- Detecting tools, technologies, and conventions
- Identifying Kubernetes and Talos infrastructure

## Use cases

- **New work session**: establish quick context in any project
- **Repository exploration**: understand unfamiliar projects
- **Progress review**: assess current status versus objectives
- **Collaboration**: understand project rules and conventions
- **Diagnostics**: identify structure and available tools

## Reasoning

1. **`pwd`** identifies the current project location.
2. **`tree`** reveals the full file and directory structure.
3. **Key files** (README, CHANGELOG, etc.) provide primary documentation.
4. **Systematic analysis** enables fast understanding of any project.
5. **Automatic detection** reveals the technologies and tools in use.

## Steps

### 1. Identify location and context

```bash
# Get current directory
pwd

# Show project structure (install tree if needed)
tree -L 3 -a
```

**If `tree` is not installed, install it by system**:

```bash
# Fedora/RHEL/CentOS
sudo dnf install tree

# Ubuntu/Debian
sudo apt update && sudo apt install tree

# Alpine
sudo apk add tree

# Arch Linux
sudo pacman -S tree

# macOS (with Homebrew)
brew install tree
```

### 2. Identify documentation files

```bash
# Search primary documentation files in the root directory
ls -la | grep -i -E '(readme|changelog|roadmap|contributing|license|warp)'

# Check existence of specific root files
for file in README.md CHANGELOG.md ROADMAP.md CONTRIBUTING.md LICENSE.md LICENSE.txt LICENSE AGENTS.md .warp.md; do
    [ -f "$file" ] && echo "✅ $file exists" || echo "❌ $file not found"
done

# Find second- and third-level READMEs (collaborative projects)
echo "\n=== READMEs in subdirectories ==="
find . -maxdepth 3 -name "README.md" -not -path "./README.md" 2>/dev/null | head -10
```

**Record discovered files**:

- ✅ **README**: [exists/does not exist]
- ✅ **CHANGELOG**: [exists/does not exist]
- ✅ **ROADMAP**: [exists/does not exist]
- ✅ **CONTRIBUTING**: [exists/does not exist]
- ✅ **LICENSE**: [exists/does not exist]
- ✅ **WARP**: [exists/does not exist]

### 3. Read primary documentation

```bash
# Read documentation files (if present)
if [ -f README.md ]; then echo "=== README.md ==="; head -50 README.md; fi
if [ -f CHANGELOG.md ]; then echo "\n=== CHANGELOG.md (last 20 lines) ==="; tail -20 CHANGELOG.md; fi
if [ -f ROADMAP.md ]; then echo "\n=== ROADMAP.md ==="; head -30 ROADMAP.md; fi
if [ -f AGENTS.md ]; then echo "\n=== AGENTS.md ==="; head -30 AGENTS.md; fi
if [ -f .warp.md ]; then echo "\n=== .warp.md ==="; head -30 .warp.md; fi

# Read README files in subdirectories (collaborative projects)
echo "\n=== Subdirectory READMEs ==="
find . -maxdepth 3 -name "README.md" -not -path "./README.md" 2>/dev/null | while read readme; do
    echo "\n--- $readme ---"
    head -20 "$readme"
done
```

**Extract key information**:

- ✅ **Project purpose**: [main description]
- ✅ **Technologies used**: [languages, frameworks, tools]
- ✅ **Current status**: [version, latest update]
- ✅ **Future goals**: [roadmap, next steps]

### 4. Analyse technical structure

```bash
# Detect project type and technologies
echo "=== Technology detection ==="

# Languages and frameworks
[ -f package.json ] && echo "✅ Node.js (package.json)" || echo "❌ Not a Node.js project"
[ -f requirements.txt ] && echo "✅ Python (requirements.txt)" || echo "❌ Not a Python project (requirements.txt)"
[ -f Pipfile ] && echo "✅ Python (Pipfile)" || echo "❌ Not a Python project (Pipfile)"
[ -f go.mod ] && echo "✅ Go (go.mod)" || echo "❌ Not a Go project"
[ -f Cargo.toml ] && echo "✅ Rust (Cargo.toml)" || echo "❌ Not a Rust project"
[ -f pom.xml ] && echo "✅ Java Maven (pom.xml)" || echo "❌ Not a Java Maven project"
[ -f build.gradle ] && echo "✅ Java Gradle (build.gradle)" || echo "❌ Not a Java Gradle project"

# Containers and orchestration
[ -f docker-compose.yml ] && echo "✅ Docker Compose" || echo "❌ Does not use Docker Compose"
[ -f docker-compose.yaml ] && echo "✅ Docker Compose (.yaml)" || echo "❌ Does not use Docker Compose (.yaml)"
[ -f Dockerfile ] && echo "✅ Docker" || echo "❌ Does not use Docker"

# Kubernetes
[ -d k8s ] && echo "✅ Kubernetes (k8s/ directory)" || echo "❌ No k8s/ directory"
[ -d kubernetes ] && echo "✅ Kubernetes (kubernetes/ directory)" || echo "❌ No kubernetes/ directory"
[ -d manifests ] && echo "✅ Kubernetes (manifests/ directory)" || echo "❌ No manifests/ directory"
find . -maxdepth 2 -name "*.yaml" -o -name "*.yml" | grep -E '(deployment|service|ingress|configmap|secret)' | head -3 | while read file; do echo "✅ Kubernetes manifest: $file"; done

# Cluster configuration (local files for EXPORT)
[ -f kubeconfig ] && echo "✅ Root kubeconfig found" || echo "❌ No root kubeconfig"
[ -f talosconfig ] && echo "✅ Root talosconfig found" || echo "❌ No root talosconfig"
echo "Searching for Kubernetes configurations..."
find . -name "*kubeconfig*" -o -name "*kube.config*" -o -name "*.kubeconfig" 2>/dev/null | head -5 | while read config; do echo "✅ Kubernetes config: $config"; done
echo "Searching for Talos configurations..."
find . -name "*talosconfig*" -o -name "*talos.config*" -o -name "*.talosconfig" 2>/dev/null | head -5 | while read config; do echo "✅ Talos config: $config"; done

# CI/CD
[ -d .github/workflows ] && echo "✅ GitHub Actions" || echo "❌ Does not use GitHub Actions"
[ -f .gitlab-ci.yml ] && echo "✅ GitLab CI" || echo "❌ Does not use GitLab CI"
```

**Record findings**:

- ✅ **Project type**: [web, CLI, library, infrastructure, etc.]
- ✅ **Primary technologies**: [detected languages]
- ✅ **Build tools**: [npm, pip, cargo, etc.]
- ✅ **Containerisation**: [Docker, Docker Compose]
- ✅ **Orchestration**: [Kubernetes, manifests, directories]
- ✅ **Cluster configuration**: [kubeconfig, talosconfig]
- ✅ **CI/CD**: [GitHub Actions, GitLab CI, etc.]
- ✅ **Additional READMEs**: [subdirectories with documentation]

### 5. Inspect configuration and scripts

```bash
# Search important configuration files
echo "=== Configuration files ==="
ls -la | grep -E '\.(json|yaml|yml|toml|ini|conf|config)$' | head -10

# Search executable scripts
echo "\n=== Available scripts ==="
find . -maxdepth 2 -name "scripts" -type d 2>/dev/null && ls -la scripts/ 2>/dev/null
ls -la | grep -E '\.(sh|py|js|rb)$' | head -5

# Check git
echo "\n=== Git information ==="
git remote -v 2>/dev/null || echo "❌ Not a Git repository"
git branch --show-current 2>/dev/null || echo "❌ No active branch"
```

**Summarise operational information**:

- ✅ **Directory organisation**: [main structure]
- ✅ **Available scripts**: [tools found]
- ✅ **Configuration**: [important config files]
- ✅ **Version control**: [Git, current branch, remotes]

### 6. Validate understanding and generate summary

**Verify understanding**:

- ✅ Is the project purpose clear?
- ✅ Were the primary technologies identified?
- ✅ Is the directory structure understood?
- ✅ Are the available tools known?
- ✅ Is the current development status understood?

## Conclusion

After completing this CoT, you will have full context to:

- **Work effectively** in any project
- **Understand quickly** the structure and technologies in use
- **Identify tools** available for development
- **Understand conventions** specific to the project
- **Plan contributions** aligned with project goals

## Expected output

A structured summary including:

```text
## Project context: [name/directory]

### Location
- Directory: [full path]
- Type: [Git repository, local project, etc.]

### Purpose
- [Project description]

### Technologies
- [Languages, frameworks, identified tools]

### Structure
- [Main directory organisation]

### Current status
- [Latest update, version, Git branch]

### Available tools
- [Scripts, commands, configurations]

### Recommended next steps
- [Suggested actions based on the analysis]
```

## References

- **./README.md** — main project documentation
- **./CHANGELOG.md** — change history (if present)
- **./ROADMAP.md** — future planning (if present)
- **./CONTRIBUTING.md** — contribution guidelines (if present)
- **./AGENTS.md** — project-specific configuration and rules (if present)
- **./.warp.md** — project-specific configuration and rules as a dotfile (if present)
- **tree command** — directory structure visualisation
- **pwd command** — current directory identification
