---
domain: workflow
task: configure GitHub repository metadata (description, topics, settings) without interactive editors
dificultad: low
longitud_objetivo: short
validacion: metadata updated correctly via API, no editor interaction
version: "1.0"
last_updated: 2025-10-12
---
<!-- markdownlint-disable MD041 -->

Reasoning:

- **CRITICAL**: avoid any command that opens interactive editors (gh repo edit with certain flags, commands without fully specified parameters).
- Use the GitHub REST API directly with curl for complex operations.
- Simple gh commands only for operations guaranteed to be non-interactive.
- Configure description, topics, homepage, licence, and other repository properties.
- Validate changes without opening browsers or editors.

Steps:

1) Action: verify that gh is installed and correctly authenticated.
   Result:
   - `gh --version` to confirm installation
   - `gh auth status` to verify authentication
   - `gh auth token` must return a valid token (without printing it to screen)
   If not authenticated: `gh auth login` following the non-interactive flow.

2) Action: retrieve current repository information.
   Result: `curl -s -H "Authorization: token $(gh auth token)" -H "Accept: application/vnd.github.v3+json" https://api.github.com/repos/OWNER/REPO | jq '{name: .name, description: .description, topics: .topics, homepage: .homepage, license: .license.spdx_id}'`
   Note: replace OWNER/REPO with actual repository values.

3) Action: configure repository description (safe method).
   Options:
   - **Method 1 (gh, verified non-interactive)**: `gh repo edit --description "project description"`
   - **Method 2 (curl, safer)**: `curl -s -H "Authorization: token $(gh auth token)" -H "Accept: application/vnd.github.v3+json" -X PATCH -d '{"description":"project description"}' https://api.github.com/repos/OWNER/REPO`

4) Action: configure repository topics (curl only to avoid editors).
   **CRITICAL**: do NOT use `gh repo edit --add-topic` as it may open an editor.
   Result: `curl -s -H "Authorization: token $(gh auth token)" -H "Accept: application/vnd.github.v3+json" -X PUT -d '{"names":["topic1","topic2","topic3","topic4"]}' https://api.github.com/repos/OWNER/REPO/topics`
   Common topic examples:
   - Documentation: "documentation", "readme", "markdown"
   - Technical analysis: "technical-analysis", "regression-analysis", "debugging"
   - Specific projects: "warp-terminal", "github-issues", "open-source"
   - Languages/technologies: "bash", "shell", "macos", "linux"

5) Action: configure repository homepage (optional).
   Result: `curl -s -H "Authorization: token $(gh auth token)" -H "Accept: application/vnd.github.v3+json" -X PATCH -d '{"homepage":"https://example.com"}' https://api.github.com/repos/OWNER/REPO`

6) Action: configure additional repository settings.
   Options available via API:

   ```bash
   # Enable issues
   curl -s -H "Authorization: token $(gh auth token)" -H "Accept: application/vnd.github.v3+json" -X PATCH -d '{"has_issues":true}' https://api.github.com/repos/OWNER/REPO

   # Enable wiki
   curl -s -H "Authorization: token $(gh auth token)" -H "Accept: application/vnd.github.v3+json" -X PATCH -d '{"has_wiki":true}' https://api.github.com/repos/OWNER/REPO

   # Enable pages
   curl -s -H "Authorization: token $(gh auth token)" -H "Accept: application/vnd.github.v3+json" -X PATCH -d '{"has_pages":false}' https://api.github.com/repos/OWNER/REPO

   # Set default branch
   curl -s -H "Authorization: token $(gh auth token)" -H "Accept: application/vnd.github.v3+json" -X PATCH -d '{"default_branch":"main"}' https://api.github.com/repos/OWNER/REPO
   ```

7) Action: validate applied changes.
   Result: `curl -s -H "Authorization: token $(gh auth token)" -H "Accept: application/vnd.github.v3+json" https://api.github.com/repos/OWNER/REPO | jq '{description: .description, topics: .topics, homepage: .homepage, has_issues: .has_issues, has_wiki: .has_wiki, default_branch: .default_branch}'`

8) (Optional) Action: configure main branch protection.
   Result:

   ```bash
   curl -s -H "Authorization: token $(gh auth token)" \
        -H "Accept: application/vnd.github.v3+json" \
        -X PUT \
        -d '{"required_status_checks":null,"enforce_admins":false,"required_pull_request_reviews":null,"restrictions":null}' \
        https://api.github.com/repos/OWNER/REPO/branches/main/protection
   ```

Commands to AVOID (may open editors):

- `gh repo edit` without specific flags
- `gh repo edit --add-topic` (known to open editor)
- `gh issue create` without `-t` and `-b`
- `gh pr create` without complete flags
- Any gh command that does not fully specify all parameters

SAFE commands (guaranteed non-interactive):

- `gh repo edit --description "text"`
- `gh repo view --json field`
- `curl` with GitHub REST API
- `gh auth token` (for use in curl)

Common topic templates:

```bash
# Documentation project
["documentation","markdown","readme","technical-writing"]

# Issue/bug analysis
["technical-analysis","debugging","regression-analysis","github-issues"]

# Open source project
["open-source","community","foss","libre-software"]

# Specific tools
["warp-terminal","terminal","shell","command-line"]

# Technologies
["bash","shell-scripting","macos","linux","cross-platform"]
```

Full usage examples:

```bash
# Configure a technical documentation repo
OWNER="incognia"
REPO="OSS"

# Description
curl -s -H "Authorization: token $(gh auth token)" -H "Accept: application/vnd.github.v3+json" -X PATCH -d '{"description":"Technical documentation of issues in open source projects"}' https://api.github.com/repos/$OWNER/$REPO

# Topics
curl -s -H "Authorization: token $(gh auth token)" -H "Accept: application/vnd.github.v3+json" -X PUT -d '{"names":["documentation","open-source","technical-analysis","github-issues","regression-analysis"]}' https://api.github.com/repos/$OWNER/$REPO/topics

# Validate
curl -s -H "Authorization: token $(gh auth token)" -H "Accept: application/vnd.github.v3+json" https://api.github.com/repos/$OWNER/$REPO | jq '{description: .description, topics: .topics}'
```

Conclusion:

- Use curl + REST API for maximum control and to avoid editors.
- Only use gh for simple, fully specified commands.
- Always validate changes with GET queries to the API.
- Keep tokens secure by using `$(gh auth token)` instead of exposed variables.
- For repos with complex configuration, use scripts that combine multiple API calls.
- References: [GitHub REST API](https://docs.github.com/en/rest), [GitHub CLI Manual](https://cli.github.com/manual/), «~/rules/rulesets/GIT.md» ([../rulesets/GIT.md](../rulesets/GIT.md)).
