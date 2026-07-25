# Initial Git configuration for new repositories

This document describes the initial configuration required when cloning or initialising a new repository, specifying user settings and SSH keys according to project context.

## 1. Identify the project context

Before configuring, determine whether the project is:

- 💼 **Corporate:** Elsevier (Tech Hub Ciudad de México / México City)
- 📺 **Personal:** independent or experimental projects

## 2. Local repository configuration

### Personal projects

```bash
# Configure user for this repository
git config user.name "Rodrigo Álvarez"
git config user.email "incognia@gmail.com"

# Verify configuration
git config --list | grep ^user\.
```

**Platform credentials:**
- **GitHub:** incognia
- **GitLab:** incognia
- **SSH Key:** `~/.ssh/incognia`

### Corporate projects (Elsevier)

```bash
# Configure user for this repository
git config user.name "Rodrigo Álvarez"
git config user.email "r.alvarez1@elsevier.com"

# Verify configuration
git config --list | grep ^user\.
```

**Platform credentials:**

- **GitHub:** incogniaops
- **GitLab:** incogniadev
- **SSH Key:** `~/.ssh/elsevier`

## 3. Initial configuration and SSH by context

To allow daily use with a simple `git push` — no SSH alias, no HTTPS — configure the repository right after `git init` using the included interactive script.

### 3.1. Using the interactive script

```bash
# After initialising the repo
git init

# Run the assistant
bash scripts/git-init-context.sh
```

The assistant will ask whether the repository is Personal or Corporate and will do the following in the current repository:

- Configure `user.name` and `user.email`.
- Configure `core.sshCommand` to use the appropriate key with `ssh -i` (SSH, not HTTPS).
- Optionally configure `origin` with an SSH URL (`git@github.com:ORG/REPO.git` or `git@gitlab.com:ORG/REPO.git`).
- Set `main` as the default branch if it does not yet exist.

Once finished, you can use `git push` directly.

### 3.2. Manual steps (if not using the script)

```bash
# Choose context
# Personal
git config user.name  "Rodrigo Álvarez"
git config user.email "incognia@gmail.com"
git config core.sshCommand "ssh -i ~/.ssh/incognia -o IdentitiesOnly=yes"

# Corporate (Elsevier)
# git config user.name  "Rodrigo Álvarez"
# git config user.email "r.alvarez1@elsevier.com"
# git config core.sshCommand "ssh -i ~/.ssh/elsevier -o IdentitiesOnly=yes"

# Configure SSH remote (examples)
# Personal GitHub:    git@github.com:incognia/REPO.git
# Corporate GitHub:   git@github.com:incogniaops/REPO.git
# Personal GitLab:    git@gitlab.com:incognia/REPO.git
# Corporate GitLab:   git@gitlab.com:incogniadev/REPO.git

git remote add origin git@github.com:ORG/REPO.git

git branch -M main
```

### 3.3. Test SSH connection

```bash
ssh -T git@github.com || true
ssh -T git@gitlab.com || true
```

## 4. Clone or initialise repositories

### Clone existing repository (always SSH)

```bash
git clone git@github.com:incognia/repo-name.git              # Personal GitHub
git clone git@github.com:incogniaops/repo-name.git           # Corporate GitHub

git clone git@gitlab.com:incognia/repo-name.git              # Personal GitLab
git clone git@gitlab.com:incogniadev/repo-name.git           # Corporate GitLab
```

### Initialise new repository

```bash
# Initialise local repository and run the assistant
git init
bash scripts/git-init-context.sh

# Verify remote configuration (if configured)
git remote -v || true

# To make the script available globally:
# install -Dm755 scripts/git-init-context.sh ~/.local/bin/git-init-context
# Then: git init && git-init-context
```

## 5. First commit and push

```bash
# Stage files
git add .

# First commit
git commit -m "feat: initial project setup"

# Initial push
git push -u origin main
```

---

**Next step:** Once the repository is configured, see **[COMMITTING.md](./COMMITTING.md)** for the daily commit and push workflow.

---

*Written by Rodrigo Álvarez (@incognia)*
