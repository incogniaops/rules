# Commit message rules and change management

## 1. Core philosophy

A well-structured commit history is one of the most valuable tools for project maintainability. Each commit must be atomic, have a clear purpose, and a message that describes it concisely.

## 2. Commit message format

Follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification.

### 2.1. General structure

```text
<type>[optional scope]: <description>

[optional body]

[optional footer]
```

### 2.2. Commit types

- **feat:** a new feature for the user.
- **fix:** a bug fix.
- **docs:** changes to documentation.
- **style:** changes that do not affect code meaning (whitespace, formatting, etc.).
- **refactor:** a code restructuring that neither fixes a bug nor adds a feature.
- **perf:** a performance improvement.
- **test:** adding or correcting tests.
- **build:** changes that affect the build system or external dependencies.
- **ci:** changes to CI configuration files and scripts.
- **chore:** other changes that do not modify source code or tests (e.g. dependency updates).

**⚠️ IMPORTANT:** CoT (Chain of Thought) files such as `cot/committing.md` are functional documents that define automated workflows. They are classified as **`feat:`** (not `docs:`), as they represent new project functionality and automation, not simple documentation.

### 2.3. Message rules

- **Language:** always write in **international English**.
- **Emojis:** do not use emojis.
- **Description:** must be concise, in the imperative mood, and lower case (e.g. `fix: correct user login flow`).
- **Body:** optional, to explain the *what* and *why* of the change.
- **Footer:** optional, for issue references (`Refs: #123`) or to mark breaking changes (`BREAKING CHANGE:`).
- **Recommended format:** for detailed messages, build `/tmp/commit-msg.txt` first and use `git commit -F /tmp/commit-msg.txt`.

### 2.4. Examples

#### Good

```text
feat(auth): add password reset functionality

Implement the password reset feature using a token-based system.
Users will receive an email with a secure link to reset their password.

Fixes: #42
```

#### Bad

```text
fix
```

```text
Updated files
```

### 2.5. Recommended detailed template (temporary file)

When a clearer, reusable commit message is needed, use a temporary file with the same Conventional Commits structure:

```text
docs: add frontend/backend GitLab cross-references

- Document zabbix-k1 as the FrontEnd and vpn-relay as the BackEnd using canonical GitLab URLs
- Replace relative backend references with repository links and
  backend-local startup commands
- Add SSH key alignment and relay host-key stability notes in README and docs/SERVERS.md
- Update CHANGELOG.md with the 2026-05-01 (CST) entry before commit

Co-Authored-By: Oz <oz-agent@warp.dev>
```

Mandatory formatting rules for this template:

- The bullet marker `-` is left-aligned (column 1), with no leading spaces or tabs.
- If a bullet is too long, break the line manually and continue below.
- The continuation line must have two spaces of indentation to align text with the bullet content.
- Keep one blank line between subject and body, and another between body and footer.

Then run the commit with:

```bash
git commit -F /tmp/commit-msg.txt
```

## 3. Workflow and change management

### 3.1. Validate `CHANGELOG.md` before committing (CRITICAL)

🔥 **CRITICAL RULE: the `/commit` flow does NOT modify `CHANGELOG.md`; it only validates that it has already been updated.**

**MANDATORY PROCESS:**
1. **FIRST:** Update `CHANGELOG.md` using `/changelogger` (or an equivalent dedicated flow).
1. **SECOND:** Validate that `CHANGELOG.md` has changes relative to the repository.
1. **THIRD:** Run `git add` for the required files (including `CHANGELOG.md`).
1. **FOURTH:** Run `git commit`.
1. **FIFTH:** Run `git push`.

**⚠️ WARNING:** If `CHANGELOG.md` has no changes, the flow must abort and suggest `/changelogger`.

#### 3.1.1. Anti-error and anti-pattern protocol (MANDATORY, NO EXCEPTIONS)

Before proceeding to `git add`/`git commit`, this protocol must be followed:

1. Run the `CHANGELOG.md` change gate:
   ```bash
   if git --no-pager diff --quiet -- CHANGELOG.md && git --no-pager diff --cached --quiet -- CHANGELOG.md; then
       echo "ERROR: CHANGELOG.md has no changes. Run /changelogger and retry /commit."
       exit 1
   fi
   ```
2. If the gate fails (no changes), stop execution immediately.
3. If the gate passes (staged or unstaged changes exist), proceed with `git add`/`git commit`.
4. CHANGELOG format and language maintenance is delegated to `/changelogger` + `~/rules/cot/changelog.md`.

Forbidden anti-patterns:

- Proceeding with commit/push when `CHANGELOG.md` has no changes.
- Attempting to edit `CHANGELOG.md` from `/commit` instead of using `/changelogger`.
- Omitting the changelog gate and relying solely on `git status`.
- Proceeding with commit/push when the changelog gate fails.

**Example of the correct flow:**

```bash
# 1. FIRST: update changelog outside /commit
/changelogger

# 2. SECOND: validate changelog gate
if git --no-pager diff --quiet -- CHANGELOG.md && git --no-pager diff --cached --quiet -- CHANGELOG.md; then
    echo "ERROR: CHANGELOG.md has no changes. Run /changelogger and retry /commit."
    exit 1
fi

# 3. THIRD: stage files
git add .

# 4. FOURTH: prepare detailed message and commit (non-interactive)
cat > /tmp/commit-msg.txt <<EOF
docs: validate changelog gate before commit

- Enforce changelog diff gate before staging and commit
- Abort commit flow when changelog has no repo diff
- Keep commit message workflow in English using temporary file

Co-Authored-By: Oz <oz-agent@warp.dev>
EOF
git commit -F /tmp/commit-msg.txt

# 5. FIFTH: push
git push
```

### 3.2. Commit atomicity

- **One purpose per commit:** each commit must reflect a single, functional change. Do not mix bug fixes with new features in the same commit.
- **Small changes:** break large changes into smaller, logical commits.

### 3.3. Task association

- **Issue references:** whenever possible, associate commits with their corresponding issue, ticket, or task in the footer (`Refs: #123`, `Closes: #123`).

### 3.4. Simplified push

If the repository is correctly configured (identity and SSH), the push command is simply:

```bash
git push
```

For initial configuration (choosing between personal or corporate credentials) see [GIT.md](./GIT.md#initial-configuration-and-ssh-by-context).

**Note:** You can quickly verify the active identity of the repository:

```bash
git config --list | grep ^user\.
```

### 3.5. Non-interactive git commands

**⚠️ IMPORTANT:** Always use non-interactive commands to avoid pagers and editors.

**Recommended commands:**

```bash
# View commit history (non-interactive)
git --no-pager log --oneline -10  # last 10 commits
git --no-pager log --oneline -5   # last 5 commits
git log -n 5                      # alternative without pager

# View diffs (non-interactive)
git --no-pager diff
git --no-pager diff --staged

# View repository status
git status  # already non-interactive by default

# Other non-interactive query commands
git --no-pager show HEAD
git --no-pager branch -v
```

**Optional global configuration:**

```bash
# Disable pager for all git commands (optional)
git config --global pager.log false
git config --global pager.diff false
```

### 3.6. Common problem solving

#### Problem: `quote>` in git commit

**Symptom:** Running `git commit -m "message"` shows `quote>` and the command does not finish.

**Cause:** Quote escaping error in the commit message.

**Solutions:**

1. **Escape quotes correctly:**
   ```bash
   # BAD: double quotes inside double quotes without escaping
   git commit -m "fix: correct "user" validation"
   
   # GOOD: escape inner quotes
   git commit -m "fix: correct \"user\" validation"
   
   # BEST: use single quotes for the message
   git commit -m 'fix: correct "user" validation'
   ```

2. **Cancel the `quote>` prompt if it appears:**
   ```bash
   # Press Ctrl+C to cancel the incomplete command
   # Then rewrite the message correctly
   ```

3. **Preferred method: use a detailed temporary file**
   ```bash
   cat > /tmp/commit-msg.txt <<EOF
   fix: correct user validation

   - Validate user payload before persistence
   - Keep login flow compatible with existing clients and
     preserve backward compatibility for existing callers
   - Add explicit error handling for invalid identifiers

   Co-Authored-By: Oz <oz-agent@warp.dev>
   EOF
   git commit -F /tmp/commit-msg.txt
   ```

**Prevention:**
- Avoid double quotes inside double-quoted messages
- Prefer single quotes for messages that contain double quotes
- Verify quote balance before running the command

---

*Written by Rodrigo Álvarez (@incognia)*
