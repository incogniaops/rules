---
domain: backups
task: restore backup and validate integrity
difficulty: low
target_length: short
validation: file/directory restored and checksum verified, log updated
---
<!-- markdownlint-disable MD041 -->
Reasoning:
- Verify integrity before restore (`sha256sum -c`) when `.sha256` exists.
- Restore while preserving permissions where applicable; validate output.
- Record actions with CST timestamps.
- Reference: `~/rules/rulesets/BACKUPS.md` (Restore and Verification section).

Steps:
1) Action: locate backup (`.bkp`, `.tar.zst`) and its `.sha256` (if present).
   Result: paths defined, e.g. `BKP=backups/daily/2025-08-18/my_folder_2025-08-18T12-00-00.tar.zst`.
2) Action: pre-restore verification.
   Result:
   - If `.sha256` exists (generated for backups >= 100 MB): `sha256sum -c "$BKP.sha256"`
   - If not: optionally compute manually and document: `sha256sum "$BKP"` (recommended if corruption is suspected)
3) Action: restore.
   Result:
   - `.bkp` file: `cp "$BKP" ./restored_file.ext` (rename as needed)
   - `tar.zst`: `unzstd -c "$BKP" | tar -xvf - -C /path/destination`
4) Action: post-restore validation.
   Result:
   - If it was a file: `sha256sum ./restored_file.ext` (compare)
   - If it was `tar.zst`: inspect with `tar -tvf` beforehand and verify by sampling or internal checksums if generated.
5) Action: log record.
   Result: `echo "$(TZ=America/Mexico_City date '+%Y-%m-%d %H:%M:%S') | restore | $BKP | ok" >> backups/backup.log`.

Conclusion:
- Restore completed and validated; log updated with CST date/time.
- References: `~/rules/BACKUPS.md` and scripts `~/rules/scripts/*`.

