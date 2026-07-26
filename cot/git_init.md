---
domain: workflow
task: initialise repo with Git and SSH (no HTTPS) following GIT.md
Dificultad: low
longitud_objetivo: short
validacion: repo initialised, correct identity, SSH forced, remote on SSH, and first push successful
---
<!-- markdownlint-disable MD041 -->

Reasoning:

- Avoid HTTPS and SSH aliases; use SSH with the appropriate key per repo (core.sshCommand).
- Configure identity (user.name, user.email) according to Personal/Corporate context.
- Set the default branch to main and origin remote in SSH format.
- Main reference: «~/rules/rulesets/GIT.md» (section "Initial configuration and SSH by context").

Steps (recommended option: interactive assistant):

1) Action: initialise the repository.
   Result: `git init`.
2) Action: run the context assistant.
   Result: `bash scripts/git-init-context.sh`.
   Note: the assistant will ask for "Personal" or "Laboral", configure user.name/user.email, core.sshCommand with the correct key, and optionally the origin remote in SSH; also sets main.
3) Action: verify identity and SSH.
   Result:
   - `git config --list | grep ^user\.`
   - `git config core.sshCommand`
4) (Optional) Action: configure origin if not done in the assistant.
   Result (examples):
   - GitHub personal: `git remote add origin git@github.com:incognia/REPO.git`
   - GitHub corporate: `git remote add origin git@github.com:incogniaops/REPO.git`
   - GitLab personal: `git remote add origin git@gitlab.com:incognia/REPO.git`
   - GitLab corporate: `git remote add origin git@gitlab.com:incogniadev/REPO.git`
   - Verify: `git remote -v`.
5) Action: first non-interactive commit.
   Result:
   - `git add .`
   - `git commit -m "feat: initial project setup"`
6) Action: first push and upstream.
   Result: `git push -u origin main`.

Steps (manual alternative, if not using the assistant):

1) `git init`
2) Choose context and configure identity + SSH:
   - Personal:
     - `git config user.name  "Rodrigo Álvarez"`
     - `git config user.email "incognia@gmail.com"`
     - `git config core.sshCommand "ssh -i ~/.ssh/incognia -o IdentitiesOnly=yes"`
   - Corporate (Elsevier):
     - `git config user.name  "Rodrigo Álvarez"`
     - `git config user.email "r.alvarez1@elsevier.com"`
     - `git config core.sshCommand "ssh -i ~/.ssh/elsevier -o IdentitiesOnly=yes"`
3) Configure remote in SSH (see examples above) and verify with `git remote -v`.
4) Set default branch: `git branch -M main`.
5) Commit and first push as in steps 5-6 of the recommended option.

Conclusion:

- After initial configuration, the daily flow uses a simple push: `git push`.
- References: «~/rules/rulesets/GIT.md» ([../rulesets/GIT.md](../rulesets/GIT.md)) and «~/rules/rulesets/COMMITTING.md» ([../rulesets/COMMITTING.md](../rulesets/COMMITTING.md)).
