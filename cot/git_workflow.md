Quick guide: Git flow (SSH, no HTTPS)

Summary
- Configure the repo with SSH by context (see ~/rules/rulesets/GIT.md, section on initial configuration and assistant).
- Use ~/rules/rulesets/COMMITTING.md for the daily flow: update CHANGELOG (CST date), commit, and simple push.

Key steps
1) Initialisation: `git init` and `bash scripts/git-init-context.sh`.
2) Verification: `git config --list | grep ^user\.` and `git config core.sshCommand`.
3) Remote: `git remote -v` (SSH), upstream on first push: `git push -u origin main`.
4) Daily flow: update CHANGELOG, `git add`, `git commit -m` and `git push`.
