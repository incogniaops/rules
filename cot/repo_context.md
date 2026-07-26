---
domain: workflow
task: obtain the complete context of a project on GitHub/GitLab (structure, flow, CI, licences, practices)
dificultad: medium
longitud_objetivo: medium
validacion: inventory of key files, flows, dependencies, and policies; sources cited (files/links)
---
<!-- markdownlint-disable MD041 -->

Reasoning:

- Start with entry documents, then move to structure, dependencies, CI/CD, deployment, style, tests, licences, and contribution.
- Maintain International English (UK) and CoT format; do not execute destructive actions or expose secrets.
- If CLI tools are available (gh/glab), use them only for listing (non-interactive); otherwise navigate the repo files.

Steps:

1) Action: identify base documents at the root.
   Result: README.md (purpose/usage), PHILOSOPHY.md or equivalent (framework), CONTRIBUTING.md, CODE_OF_CONDUCT.md.
2) Action: review licensing and attribution.
   Result: LICENSE/LICENCE/COPYING/NOTICE; if missing, look for licence headers in source files.
3) Action: map the repo structure.
   Result: key directories (src/, cmd/, pkg/, apps/, services/, rulesets/, scripts/, tools/, infra/, deployments/, charts/); Makefile/Taskfile.
4) Action: detect language and dependencies.
   Result: package.json/yarn.lock/pnpm-lock.yaml; go.mod; pyproject.toml/requirements*.txt; Cargo.toml; pom.xml/gradle.*; composer.json; Gemfile.
5) Action: review CI/CD.
   Result: .github/workflows/*.yaml, .gitlab-ci.yml, Jenkinsfile, .circleci/, .drone.yml; triggers, jobs, artefacts, quality gates.
6) Action: containers and deployment.
   Result: Dockerfile(s), docker-compose.yaml/compose.yaml; Helm charts (charts/), K8s manifests (k8s/, deploy/, manifests/).
7) Action: configuration and secrets.
   Result: .env.example/.env.sample; variable documentation; injection policies (CI vars/Secret managers). Do not expose secrets.
8) Action: style and linters.
   Result: .editorconfig; eslint/prettier, golangci-lint, flake8/black, markdownlint, Vale; conventions (Conventional Commits).
9) Action: tests and coverage.
   Result: tests/__tests__/*_test.go/pytest/jest; commands (npm test, go test ./..., pytest); fixtures/mock data.
10) Action: versioning and history.
    Result: CHANGELOG.md, tags/releases (GitHub/GitLab Releases), SemVer/Conventional Commits.
11) Action: contribution and branches.
    Result: CODEOWNERS, issue/PR/MR templates, protected branches, review policies.
12) Action (optional): issues and PR/MR via CLI.
    Result: `gh issue list`, `gh pr list`, or `glab` equivalents (if available and with permissions). Do not close/merge from here.
13) Action: synthesise context.
    Result: report covering: purpose, structure, dependencies, CI/CD, deployment, config/secrets, style, tests, version, and contribution. Cite paths/files.

Conclusion:

- Deliver a reproducible inventory and synthesis with references to files/paths and, where applicable, read-only commands (not destructive). Use standard English typography and avoid adding 's' to acronyms.
