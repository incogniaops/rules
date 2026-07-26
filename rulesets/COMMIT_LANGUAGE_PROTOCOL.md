# Critical protocol: commit messages in English

**MAXIMUM PRIORITY — NEVER IGNORE**

## Fundamental rule

**ALL commit messages MUST be in ENGLISH**

```bash
# ✅ CORRECT
git commit -m "feat: add new functionality"
git commit -m "fix: resolve authentication issue" 
git commit -m "docs: update installation guide"

# ❌ INCORRECT
git commit -m "feat: agregar nueva funcionalidad"
git commit -m "fix: resolver problema de autenticación"
git commit -m "docs: actualizar guía de instalación"
```

## Reference

- **Source**: `~/rules/cot/committing.md` line 15
- **Exact text (current policy)**: commits always in international English; documentation and `CHANGELOG.md` language depends on context (personal: Mexican Spanish, corporate: international English).

## Language distribution

| Context | Personal | Corporate |
|---------|----------|-----------|
| **Commit messages** | 🇺🇸 International English | 🇺🇸 International English |
| **CHANGELOG.md** | 🇲🇽 Mexican Spanish | 🇺🇸 International English |
| **Documentation** | 🇲🇽 Mexican Spanish | 🇺🇸 International English |
| **Code/comments** | 🇺🇸 International English | 🇺🇸 International English |

## Mandatory protocol for the assistant

**Each time `~/rules/cot/committing.md` is executed, the assistant MUST:**

### Step 0: Language checkpoint (BEFORE any commit)

```text
🔍 CHECKPOINT: Verifying commit language...
📋 RULE: Commit messages in ENGLISH (~/rules/cot/committing.md line 15)
⚠️  CRITICAL: Do NOT proceed until correct language is confirmed
```

### Mandatory declaration

**The assistant must explicitly declare:**

> «⚠️ LANGUAGE CHECK: All commit messages must be in English per ~/rules/cot/committing.md line 15»

### Pre-commit verification

**Before each `git commit -F /tmp/commit-msg.txt`:**

1. ✅ **Build or update `/tmp/commit-msg.txt`**
2. ✅ **Show the planned message and confirm it is in English**
3. ✅ **Proceed with the commit using `-F`**
4. ✅ **Confirm that `CHANGELOG.md` has changes (staged or unstaged) via mandatory gate**

### Mandatory execution gate (changelog + language)

Proceeding to `git add`/`git commit` is not permitted if either of these conditions fails:

1. **CHANGELOG gate**: `CHANGELOG.md` must have changes relative to the repo.
   - Validation: `git --no-pager diff --quiet -- CHANGELOG.md && git --no-pager diff --cached --quiet -- CHANGELOG.md`
   - If both commands return 0, there are no changes: abort and run `/changelogger`.
2. **LANGUAGE gate**: the subject and body of the commit are not fully in international English.

If either fails:

- 🛑 stop the flow,
- 🔍 if CHANGELOG gate fails: run `/changelogger`, then retry `/commit`,
- 🔍 if LANGUAGE gate fails: correct the message in `/tmp/commit-msg.txt`,
- 🙋 ask the user for confirmation before a second attempt.

### Example of correct application

```text
🔍 CHECKPOINT: Verifying commit language...
📋 RULE: Commit messages in ENGLISH

Planned temporary file (`/tmp/commit-msg.txt`):
feat: integrate Loki and Promtail for centralized logging

- Add Helm values and manifests required for centralized logging
- Update runtime configuration to route logs through
  Promtail
- Document deployment and rollback procedure in project docs

Co-Authored-By: Oz <oz-agent@warp.dev>

✅ Message in English validated — proceeding with:
git commit -F /tmp/commit-msg.txt
```

Mandatory body format before validating language:

- The bullet `-` must start at column 1 (no leading spaces).
- If a line is too long, break it and continue on the next line.
- Continuation lines must be indented with two spaces to align with the bullet text.

## Protocol failure

**If the assistant makes a language error:**

1. 🛑 **STOP** the process immediately
2. 🔄 **CORRECT** with reset/amend if necessary
3. 📝 **DOCUMENT** the error to prevent recurrence
4. ✅ **REPEAT** the process with the correct language

## Forbidden anti-patterns (stop immediately)

- Committing or pushing with `CHANGELOG.md` unchanged relative to the repo.
- Attempting to edit `CHANGELOG.md` from `/commit` instead of invoking `/changelogger`.
- Committing in Spanish by skipping the language checkpoint.
- Skipping `/tmp/commit-msg.txt` and falling back to ad-hoc messages without review.

## Identified recurring error

- **Problem**: tendency to write commits in Spanish
- **Cause**: not verifying language before committing
- **Solution**: this mandatory checkpoint protocol
