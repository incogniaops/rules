---
domain: backups
task: perform backup (file or directory) with checksum and CST log
difficulty: low
target_length: short
validation: backup created, checksum generated and verified, log entry recorded
---
<!-- markdownlint-disable MD041 -->
Reasoning:
- Always use CST (México City) for timestamps (`TZ=America/Mexico_City`) and log actions.
- Generate a checksum (`.sha256`) for integrity.
- For directories, package and compress with `zstd` for efficiency.
- Reference: `~/rules/rulesets/BACKUPS.md` (restore, verification, compression, incremental rsync).

Steps:
1) Action: decide what to back up (file or directory) and destination.
   Result: variables defined, e.g. `SRC=./my_folder DEST=backups/daily`.
2) Action: create (if applicable) the CST day folder.
   Result:
   - `DATE_CST=$(TZ=America/Mexico_City date +"%Y-%m-%d")`
   - `mkdir -p "$DEST/$DATE_CST"`
3) Action: run basic backup with script.
   Result:
   - Directory: `bash ~/rules/scripts/backup_file.sh "$SRC" "$DEST/$DATE_CST"`
   - File: `bash ~/rules/scripts/backup_file.sh ./file.txt "$DEST/$DATE_CST"`
4) Action: verify checksum (only if `.sha256` exists; generated for backups >= 100 MB).
   Result: `find "$DEST/$DATE_CST" -maxdepth 1 -name "*.sha256" -exec sha256sum -c {} \;`
5) (Optional) Action: incremental snapshot of a tree with rsync.
   Result: `bash ~/rules/scripts/backup_rsync_snapshot.sh "/path/data" "backups/daily"`
6) Action: record/review CST log.
   Result: review/use `$DEST/backup.log` (or `$BACKUP_LOG_FILE`).

Conclusion:
- Copy is created and verified; log records the operation in CST.
- References: `~/rules/BACKUPS.md` and scripts in `~/rules/scripts/`.

