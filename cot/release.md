---
domain: release
task: validate history, derive descriptor/notes, and publish a non-interactive semantic release
dificultad: medium
longitud_objetivo: medium
validacion: unique remote tag, aligned release, and notes in official format
version: "1.0"
last_updated: 2026-05-05
---
<!-- markdownlint-disable MD041 -->

Reasoning:

- Publication must follow a strict `vX.Y.Z` tag convention and the flow `dev -> main (ff-only) -> tag -> release -> back to dev`.
- Before creating a new version, validate historical consistency to avoid carrying forward format errors.
- The release name and notes must be derived from real changes since the last tag, not invented.
- All execution must be non-interactive: no editors, use `--notes-file`, and include explicit verifications.

Steps:
0) Action: validate the argument received by the `/release vX.Y.Z` invocation.
   Validation: must match `^v[0-9]+\\.[0-9]+\\.[0-9]+$`.
   Result: valid `TARGET_VERSION` variable (e.g. `v0.5.0`).

1) Action: load rules and initial state.
   References: `~/rules/rulesets/RELEASING.md`, `~/rules/rulesets/COMMITTING.md`, and `AGENTS.md` of the target repository.
   Verifications:
   - clean working tree (`git status --short`);
   - current branch is the expected one (`dev`);
   - access to remote and releases API.
   Result: context ready to publish.

2) Action: validate the historical baseline of `zabbix-k1` before the new release.
   Expected tags on remote:
   - `v0.1.0`
   - `v0.2.0`
   - `v0.3.0`
   - `v0.4.0`
   Expected releases:
   - `v0.1.0 — MVP`
   - `v0.2.0 — NOC 16:9`
   - `v0.3.0 — NOC operativo y gobernanza`
   - `v0.4.0 — Collector-first robusto`
   Result: consistency confirmed, or list of discrepancies to resolve before continuing.

3) Action: validate that the target version does not already exist.
   Guide commands:
   - `git rev-parse -q --verify "refs/tags/${TARGET_VERSION}"`
   - `git ls-remote --tags origin "${TARGET_VERSION}" "${TARGET_VERSION}^{}"`
   - `glab api "projects/operaciones-ti%2Fzabbix-k1/releases/${TARGET_VERSION}"`
   Result: confirmation that there is no tag/release collision for `TARGET_VERSION`.

4) Action: identify the previous tag and change range for the new release.
   Guide commands:
   - `PREV_TAG=$(git --no-pager tag --list 'v*' --sort=version:refname | tail -n 1)`
   - `git --no-pager log --pretty=format:'%s' "${PREV_TAG}..dev"`
   - `git --no-pager log --name-only --pretty=format:'%h %s' "${PREV_TAG}..dev"`
   Result: concrete input for building the descriptor and relevant bullets.

5) Action: derive the short descriptor and final release name.
   Mandatory heuristic:
   - Prioritise `feat` over `fix/perf/docs/chore` for the descriptor.
   - If there are multiple themes, use the dominant impact for operations/NOC.
   - Descriptor in English, concise and specific.
   Final format: `RELEASE_NAME="${TARGET_VERSION} — ${DESCRIPTOR}"`.
   Result: release name consistent with history.

6) Action: generate non-interactive release notes in a temporary file.
   Suggested path: `/tmp/release-notes-${TARGET_VERSION}.md`.
   Mandatory minimum structure:
   - short introductory paragraph;
   - heading `## Features included`;
   - bullets with relevant, verifiable changes from the range `${PREV_TAG}..dev`.
   Result: notes file ready for `glab release create/update --notes-file`.

7) Action: promote `dev` to `main` with fast-forward and publish tag.
   Sequence:
   - `git checkout main`
   - `git merge --ff-only dev`
   - `git push origin main`
   - `git tag -a "${TARGET_VERSION}" -m "release: ${TARGET_VERSION}"`
   - `git push origin "${TARGET_VERSION}"`
   Result: `main` published and annotated tag visible on remote.

8) Action: create or update the release on GitLab without interactive mode.
   Recommended sequence:
   - if release does not exist:
     `glab release create "${TARGET_VERSION}" --name "${RELEASE_NAME}" --notes-file "/tmp/release-notes-${TARGET_VERSION}.md"`
   - if release exists:
     `glab release update "${TARGET_VERSION}" --name "${RELEASE_NAME}" --notes-file "/tmp/release-notes-${TARGET_VERSION}.md"`
   Result: release associated with the tag, with correct name/notes.

9) Action: verify final publication.
   Mandatory validations:
   - `git ls-remote --tags origin "${TARGET_VERSION}" "${TARGET_VERSION}^{}"` returns only the expected tag;
   - `glab release list` includes `TARGET_VERSION`;
   - `glab api "projects/operaciones-ti%2Fzabbix-k1/releases/${TARGET_VERSION}"` reflects the name and notes following the convention.
   Result: publication validated.

10) Action: return to the development branch.
    Command: `git checkout dev`.
    Result: flow closed and repository ready to continue work.

Conclusion:

- A release is considered correct only if it passes historical validation, avoids version collisions, derives the descriptor/notes from real changes, and completes the full non-interactive flow.
- If there are pre-existing format inconsistencies, fix them first and then publish the new version.
- References: `~/rules/rulesets/RELEASING.md`, `~/rules/rulesets/COMMITTING.md`, `AGENTS.md` of the target repo.
