---
domain: backups
task: quick backup in the same directory
difficulty: very low
target_length: very short
validation: file_YYYY-MM-DD.ext.bkp created next to the original
---
<!-- markdownlint-disable MD041 -->
Reasoning:

- For small text files, an immediate local backup is sufficient without compression or checksum.
- Keep the CST date convention (YYYY-MM-DD) and the `.bkp` suffix.
- Reference: `~/rules/rulesets/BACKUPS.md` (quick backup section) and script `~/rules/scripts/quick_bkp.sh`.

Steps:

1) Action: identify files to back up (in the current directory).
   Result: e.g. `file.txt`.
2) Action: run quick backup using CST date.
   Result: `bash ~/rules/scripts/quick_bkp.sh file.txt` (can accept multiple files).
3) Action: validate that the backup exists next to the original.
   Result: `ls -1 file_$(TZ=America/Mexico_City date +"%Y-%m-%d").txt.bkp`.
4) (Optional) Action: repeat for multiple files in one command.
   Result: `bash ~/rules/scripts/quick_bkp.sh *.md`.

Conclusion:

- Backup is created as `name_YYYY-MM-DD.ext.bkp` in the same directory.
- Manual restore: copy/rename the `.bkp` file to the original name when needed.
