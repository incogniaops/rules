---
domain: workflow
task: follow COMMITTING.md (validate pre-updated CHANGELOG, conventional commit, and simple push)
difficulty: low
target_length: short
validation: CHANGELOG detected as modified, identity visually confirmed, and commit/push successful
version: "1.3"
last_updated: 2026-05-10
---
<!-- markdownlint-disable MD041 -->

Reasoning:
- Follow the mandatory flow: `CHANGELOG.md` must already be updated; `/commit` ONLY validates that prerequisite and then executes add/commit/push (see `~/rules/rulesets/COMMITTING.md` ([../rulesets/COMMITTING.md](../rulesets/COMMITTING.md))).
- If `CHANGELOG.md` has no changes relative to the repository, abort and delegate the update to `/changelogger`.
- CRITICAL: use `git status` to analyse changes before proceeding and determine whether separate commits are required.
- Evaluate whether changes are mixed types (e.g. feat + fix, docs + refactor) that require separate atomic commits.
- CRITICAL: commit message ALWAYS in International English with Conventional Commits; documentation in Mexican Spanish (personal context) or International English (corporate context), as applicable.
- Push should remain simple (`git push`) when the repository was configured correctly in advance (see `~/rules/rulesets/GIT.md` initial configuration section).

Steps:
0) Action: validate repository configuration and show active identity before proceeding.
   SESSION CONDITION: If this step has already been completed successfully in the current conversation session, SKIP it and continue directly at step 1. Do not repeat validation in the same session.
   REQUIRED COMMANDS:
   - `git config --list | grep -E "^(user\.(name|email)|core\.sshCommand|remote\.origin)"`
   - `git remote -v` to verify remote URLs
   - **NEW**: show active identity on screen:
     ```bash
     echo "=== ACTIVE IDENTITY FOR THIS COMMIT ==="
     echo "Email: $(git config user.email)"
     echo "Name: $(git config user.name)"
     echo "SSH key: $(git config core.sshCommand | grep -o '/[^"]*' || echo 'default ~/.ssh/id_rsa')"
     echo "Remote: $(git remote get-url origin)"
     echo "======================================="
     ```
   Critical validations:
   - Confirm these exist: user.name, user.email, core.sshCommand, and remote.origin
   - **CRITICAL**: verify remote.origin uses SSH (`git@github.com` or `git@gitlab.com`), NOT HTTPS
   - **CRITICAL**: visually confirm that the displayed identity is correct for this repository
   - If HTTPS is used: configuration is incorrect; redirect to `git_init`
   - If identity is not expected: pause and review configuration
   If any required configuration is missing: apply `~/rules/cot/git_init.md` ([./git_init.md](./git_init.md)) before continuing.
   Result: repository validated with SSH, identity visually confirmed, and ready for commits.

1) Action: analyse current repository state to identify change types.
   Result: `git status` — examine modified/added/deleted files and their purpose.
   Evaluation: determine whether changes are a single type (e.g. docs only) or mixed (e.g. feat + fix).
   Decision: if mixed, plan separate atomic commits using selective `git add` per file/directory.

2) Action: validate the `CHANGELOG.md` gate before staging/commit.
   REQUIRED COMMANDS:
   - `git --no-pager diff --quiet -- CHANGELOG.md`
   - `git --no-pager diff --cached --quiet -- CHANGELOG.md`
   Critical decision:
   - If **both commands return 0**: no changes in `CHANGELOG.md` (neither staged nor unstaged) → **ABORT** flow and suggest `/changelogger`.
   - If **either returns 1**: `CHANGELOG.md` has changes → continue.
   Result: changelog prerequisite confirmed for `/commit`.

2b) Action: inspect `CHANGELOG.md` diff (optional but recommended for traceability).
   COMMANDS:
   - `git --no-pager diff -- CHANGELOG.md`
   - `git --no-pager diff --cached -- CHANGELOG.md`
   Result: explicit visibility of changelog changes before commit.

3) Action: build a detailed commit message in a reusable temporary file.
   Result: create `/tmp/commit-msg.txt` with this template:
   ```text
   <type>[optional scope]: <summary in english>
   
   - detail 1 in english
   - detail 2 in english with optional continuation
     aligned with the bullet text
   - detail 3 in english

   Co-Authored-By: Oz <oz-agent@warp.dev>
   ```
   Critical validations:
   - First line in International English using Conventional Commits.
   - Body uses bullets describing concrete, substantive changes.
   - DO NOT include bullets such as `update/edit CHANGELOG.md` (or equivalents), because `CHANGELOG.md` is a prerequisite validated by step 2 gate.
   - Bullet marker `-` starts in column 1 (no leading spaces or tabs).
   - If a bullet is too long, wrap manually and align continuation with two spaces.
   - Keep one blank line between header/body and body/footer.

3b) Action: mandatory language checkpoint before `git commit -F`.
   Mandatory declaration:
   - `⚠️ LANGUAGE CHECK: All commit messages must be in English per ~/rules/cot/committing.md line 15`
   Validation:
   - Show/review `/tmp/commit-msg.txt` content and confirm English in subject/body.
   - Confirm presence of `Co-Authored-By: Oz <oz-agent@warp.dev>`.
   Result: message validated in International English and ready for non-interactive commit.

4) Action: perform atomic commits based on step 1 analysis using the temporary file from step 3.
   - If changes are homogeneous (single type): `git add -A && git commit -F /tmp/commit-msg.txt`
   - If changes are mixed: separate commits with selective `git add file(s)`, rewriting `/tmp/commit-msg.txt` before each commit:
     * `git add file1 file2 && git commit -F /tmp/commit-msg.txt`
     * `git add file3 && git commit -F /tmp/commit-msg.txt`
     * etc.

5) Action: simple push of all commits.
   Result: `git push`.

6) Action: non-interactive verification of commits performed.
   Result: `git --no-pager log --oneline -5` (view latest commits without pager).

Conclusion:
- Verify commit(s) appear in `git --no-pager log --oneline -5`.
- **CRITICAL**: confirm the identity shown in step 0 matches the expected identity for this repository (correct email and SSH key).
- If multiple commits were made, ensure each is atomic and has an appropriate conventional type (feat, fix, docs, etc.).
- To avoid `quote>` and escape issues, always prefer `git commit -F /tmp/commit-msg.txt`.
- **IMPORTANT HINT**: if `git remote -v` shows `https://` URLs instead of `git@`, configuration is incorrect and `git_init` must be applied.
- **MULTI-ACCOUNT HINT**: if email/key does not match expectations, review repository configuration before proceeding.
- Commit atomicity improves maintenance: each commit should represent a single logical, functional change.
- Forbidden anti-patterns (stop and request confirmation if any appears):
  - Proceeding to `git add`/`git commit` without passing the `CHANGELOG.md` change gate.
  - Attempting to edit `CHANGELOG.md` from `/commit` instead of running `/changelogger`.
  - Including a changelog-edit maintenance bullet in the commit body as a change detail.
  - Committing with a Spanish message or without explicit language checkpoint.
  - Using interactive flow (editor/pager) instead of `git commit -F /tmp/commit-msg.txt`.
- References: `~/rules/rulesets/COMMITTING.md` ([../rulesets/COMMITTING.md](../rulesets/COMMITTING.md)), `~/rules/cot/changelog.md` ([./changelog.md](./changelog.md)), `~/rules/cot/git_init.md` ([./git_init.md](./git_init.md)), `~/rules/rulesets/GIT.md` ([../rulesets/GIT.md](../rulesets/GIT.md)), `~/rules/README.md` ([../../README.md](../../README.md)), and `~/rules/rulesets/LINGUISTICS.md` ([../rulesets/LINGUISTICS.md](../rulesets/LINGUISTICS.md)).

