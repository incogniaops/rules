# Tagging and release rules

## 1. Objective

Define a single, reproducible, non-interactive policy for publishing versions with semantic tags and consistent releases.

## 2. Tag convention

- Mandatory format: `vMAJOR.MINOR.PATCH` (example: `v0.5.0`).
- Use SemVer strictly.
- Do not mix formats for the same version (`v0.5.0` and `0.5.0` at the same time is forbidden).
- The release tag must always point to the commit published on `main`.
- The tag must be annotated (`git tag -a`), not lightweight.

## 3. Release convention

- Release tag: `vX.Y.Z`.
- Recommended name: `vX.Y.Z — Short descriptor`.
- Release language: Mexican Spanish.
- Minimum required notes:
  - brief introductory paragraph;
  - `## Funcionalidades incluidas` section;
  - bulleted list of main changes.

## 4. Mandatory publishing workflow

1. Confirm that `dev` is ready for promotion.
2. Promote `dev` to `main` with fast-forward (`--ff-only`).
3. Create an annotated tag on `main`.
4. Publish `main` and the tag to the remote.
5. Create or update the release associated with the same tag.
6. Return to `dev`.

## 5. Automatic derivation of name and changes

For an invocation such as `/release v0.5.0`, the name and notes are generated from real evidence:

1. Detect the most recent `PREV_TAG`.
2. Obtain changes from `${PREV_TAG}..dev` (commits and files).
3. Infer the descriptor:
   - if `feat` commits predominate, use a feature-oriented descriptor;
   - if `fix/perf` predominate, use a stability/robustness-oriented descriptor;
   - if changes are support-related, use a maintenance-oriented descriptor.
4. Build the final name `vX.Y.Z — Descriptor`.
5. Generate notes in a temporary file and publish with `--notes-file`.

## 6. Critical operational rules

- Do not use interactive editors to publish or correct a release.
- The entire workflow must be non-interactive (including release notes).
- Before publishing a new version, validate that no tag/release with that version already exists.
- If there is a format inconsistency in previous tags/releases, correct it first.
- If an incorrect tag without the `v` prefix was published, create the correct version and remove the incorrect duplicates.

## 7. Validated baseline for `zabbix-k1`

Expected tags:

- `v0.1.0`
- `v0.2.0`
- `v0.3.0`
- `v0.4.0`

Expected releases:

- `v0.1.0 — MVP`
- `v0.2.0 — NOC 16:9`
- `v0.3.0 — NOC operativo y gobernanza`
- `v0.4.0 — Collector-first robusto`

If this baseline does not match, stop publishing and correct the history before continuing.

## 8. Mandatory post-publish verification

After publishing, always validate:

- that only the correct tag exists on the remote for the version;
- that the release associated with the same tag exists;
- that the name and notes follow the convention.

Reference commands:

- `git ls-remote --tags origin vX.Y.Z vX.Y.Z^{}`
- `glab release list`
- `glab api projects/operaciones-ti%2Fzabbix-k1/releases/vX.Y.Z`

---

These rules complement `COMMITTING.md` and focus exclusively on version and release publishing.
