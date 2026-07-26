# Backup policies

## Naming convention

### Backup file name structure

Each backup file follows this naming structure:

```text
[name_without_extension]_[timestamp].[original_extension].bkp
```

**Components:**

- **Base name:** the original file name without its extension
- **Separator:** underscore (_)
- **Timestamp:** date and time in ISO format: `YYYY-MM-DDTHH-MM-SS` (CST timezone, Ciudad de México, UTC-6)
- **Original extension:** the original file extension is preserved
- **Backup extension:** `.bkp` is appended at the end

**Naming examples:**

- `archivo.txt` → `archivo_2025-08-01T04-38-18.txt.bkp`
- `config.yaml` → `config_2025-08-01T04-38-18.yaml.bkp`
- `script.sh` → `script_2025-08-01T04-38-18.sh.bkp`
- `database.sql` → `database_2025-08-01T04-38-18.sql.bkp`

### Backup location

Backups must be stored in a folder called `backups`, created according to the project or system context.

If a file with a `.bak` or `.bkp` extension is found that does not comply with the established standards, review its timestamp and update the name to align with this convention.

Including the time component guarantees unique names and precise traceability, regardless of how frequently backups are taken during the day.

Avoid overwriting previous backups. The date and time convention preserves the historical sequence of each copy.

**Mandatory timezone:** all timestamps must be generated using the CST timezone of Ciudad de México (UTC-6). Never use UTC or the system's local timezone if it differs from CST.

⚠️ **CRITICAL WARNING:** It is not sufficient to append the suffix "CST" to a UTC date. You must subtract 6 hours from the UTC date to obtain the correct CST date. Using `TZ="America/Mexico_City"` in `date` commands guarantees automatic conversion.

## Backup policy before destructive operations

### Definition

This policy applies to any script or command that performs permanent deletion of files, records, configurations, or any other type of data.

### Manual execution

If the script or command is executed manually (initiated by a user), the system must:

1. Display a warning message indicating that an irreversible deletion will be performed
2. Explicitly ask whether a backup should be created before continuing
3. Allow the user to choose from the following options:
   - Create an automatic backup following the established backup policy
   - Cancel execution
   - Continue without backup (only if confirmed twice)

### Automated execution

If execution is automated (by cron jobs, pipelines, bots, or other non-interactive processes):

1. The script must verify whether an active backup policy exists
2. It must perform a full backup in accordance with that policy before starting any destructive operation
3. If the backup fails, the script must not proceed with the deletion. It must log the error and exit safely

### Logging and auditing

Every deletion action must be logged with:

- Date and time (24-hour format, CST timezone, Ciudad de México, UTC-6)
- User or process that initiated the execution
- Backup result
- Elements affected by the deletion

⚠️ **IMPORTANT:** For audit logging, always use `TZ="America/Mexico_City" date` to ensure the date is calculated correctly in CST (subtracting 6 hours from UTC), not merely appending the CST suffix.

### Recommended best practices

- Implement reusable backup functions in scripts
- Use environment variables to define backup paths
- Include tests in staging environments before applying to production

## Backup directory structure

```text
backups/
├── daily/          # Respaldos diarios automáticos (subcarpetas por fecha YYYY-MM-DD)
├── manual/         # Respaldos manuales por demanda (subcarpetas por fecha)
├── pre-deploy/     # Respaldos antes de despliegues
├── pre-delete/     # Respaldos antes de operaciones destructivas
└── archive/        # Respaldos antiguos comprimidos
```

Example with today's date (CST):

```bash
DATE_CST=$(TZ="America/Mexico_City" date +"%Y-%m-%d")
mkdir -p "backups/daily/${DATE_CST}"
```

## Restoration

- Locate the backup to restore and its checksum file (.sha256 if it exists).
- Verify integrity before restoring.
- Restore preserving permissions where applicable and validate the result.

Example (single file):

```bash
# Verificación previa (si hay checksum)
sha256sum -c backups/daily/2025-08-18/archivo_2025-08-18T12-00-00.txt.bkp.sha256

# Restauración
cp backups/daily/2025-08-18/archivo_2025-08-18T12-00-00.txt.bkp ./archivo.txt

# Validación posterior (opcional)
sha256sum ./archivo.txt
```

Example (tar.zst):

```bash
# Verificar e inspeccionar
zstd -t archivo_2025-08-18T12-00-00.tar.zst
unzstd -c archivo_2025-08-18T12-00-00.tar.zst | tar -tvf -
# Restaurar en ruta destino
unzstd -c archivo_2025-08-18T12-00-00.tar.zst | tar -xvf - -C /ruta/destino
```

## Verification and integrity (checksums)

- Policy: generate .sha256 only for large backups (size >= 100 MB) to optimise cost/time.
  - Configurable threshold: `BACKUP_SHA_THRESHOLD_BYTES` (default 104857600 = 100 MB).
- Files with .sha256 must always be verified; those below the threshold may be verified on demand.
- Bulk verification:

```bash
find backups -type f -name "*.sha256" -exec sha256sum -c {} \;
```

## Recommended compression (zstd)

- Better ratio/speed than gzip in many cases.
- Example for packaging and compressing a file/directory:

```bash
TS=$(TZ=America/Mexico_City date +"%Y-%m-%dT%H-%M-%S")
TARGET="mi_carpeta"
tar --mtime="$(date -d "$TS" +%Y-%m-%d)" --owner=0 --group=0 --numeric-owner -cf - "$TARGET" | zstd -T0 -19 -o "${TARGET}_${TS}.tar.zst"
```

## Efficient incrementals with rsync (--link-dest)

- Enables daily snapshots with hardlinks to unchanged files.
- Scheme:

```bash
BASE="/datos"
DEST="backups/daily"
DATE_CST=$(TZ=America/Mexico_City date +"%Y-%m-%d")
SNAP="$DEST/$DATE_CST"
LAST=$(ls -1 "$DEST" | sort | tail -n1)
mkdir -p "$SNAP"
if [ -n "$LAST" ] && [ "$LAST" != "$DATE_CST" ]; then
  rsync -a --delete --link-dest="$DEST/$LAST" "$BASE/" "$SNAP/"
else
  rsync -a --delete "$BASE/" "$SNAP/"
fi
```

## Encryption and offsite

- Encrypt with age (recommended) or gpg before sending offsite.
- age example:

```bash
age -r RECIPIENT -o backup.tar.zst.age backup.tar.zst
```

- Offsite upload with rclone (S3/Backblaze/SSH):

```bash
rclone copy backups remote:bucket/path
```

- 3-2-1 policy: 3 copies, 2 media, 1 offsite.

## Scheduling (Fedora, systemd)

Example units (see systemd/backups/ folder):

- `backup@.service`
- `backup@daily.timer`

Recommended variables in the service:

- Environment=TZ=America/Mexico_City
- Logs to a fixed path in CST.

## Logging and auditing

Suggested log line format:

```text
YYYY-MM-DD HH:MM:SS | action | file | result | checksum
```

- Rotate backup.log and deletion.log periodically.

## Security and permissions

- Owner/group: root:root for sensitive backups; permissions 0640.
- Add backups/ to the repository's .gitignore.
- SELinux: when restoring on SELinux systems, relabel contexts: `restorecon -R /restored/path`.

## Databases (examples)

PostgreSQL (dump/restore):

```bash
# Dump
pg_dump --format=custom --no-owner --no-privileges "${PGDATABASE}" > "backups/daily/${DATE_CST}/db_${DATE_CST}.dump"
# Restore
pg_restore --clean --no-owner --no-privileges -d "${PGDATABASE}" "db_${DATE_CST}.dump"
```

MySQL/MariaDB (dump/restore):

```bash
# Dump
mysqldump --single-transaction --routines --events "$MYSQL_DATABASE" > "backups/daily/${DATE_CST}/db_${DATE_CST}.sql"
# Restore
mysql "$MYSQL_DATABASE" < "db_${DATE_CST}.sql"
```

## Implementation examples

### Basic backup script

#### Quick backup in the same directory (small files)

```bash
# Uso: quick_bkp.sh archivo1 [archivo2 ...]
# Ejemplo: archivo.txt -> archivo_YYYY-MM-DD.txt.bkp
bash ~/rules/scripts/quick_bkp.sh archivo.txt
```

```bash
#!/usr/bin/env bash
set -euo pipefail

log() {
  printf "%s | %s\n" "$(TZ=America/Mexico_City date '+%Y-%m-%d %H:%M:%S')" "$*" | tee -a "${BACKUP_LOG_FILE:-backups/backup.log}"
}

# Función para crear respaldo con timestamp y checksum
create_backup() {
  local source_file="$1"
  local backup_dir="${2:-backups}"
  local timestamp=$(TZ="America/Mexico_City" date +"%Y-%m-%dT%H-%M-%S")
  local filename=$(basename "$source_file")
  local name_without_ext="${filename%.*}"
  local extension="${filename##*.}"

  if [[ "$filename" == "$extension" ]]; then
    local backup_name="${filename}_${timestamp}.bkp"
  else
    local backup_name="${name_without_ext}_${timestamp}.${extension}.bkp"
  fi

  mkdir -p "$backup_dir"
  cp -a "$source_file" "$backup_dir/$backup_name"
  (cd "$backup_dir" && sha256sum "$backup_name" > "$backup_name.sha256")
  log "backup | $backup_dir/$backup_name | ok | $(awk '{print $1}' "$backup_dir/$backup_name.sha256")"
}

# Función para operaciones destructivas con confirmación
safe_delete() {
  local target="$1"
  echo "ADVERTENCIA: Se eliminará permanentemente: $target"
  read -p "¿Desea crear un respaldo antes de continuar? (s/n): " -n 1 -r; echo
  if [[ $REPLY =~ ^[SsYy]$ ]]; then
    create_backup "$target" "backups/pre-delete"
  else
    read -p "¿Está seguro de continuar sin respaldo? (escriba 'CONFIRMAR'): " confirm
    if [[ ${confirm:-} != "CONFIRMAR" ]]; then
      echo "Operación cancelada"; return 1
    fi
  fi
  rm -f "$target"
  echo "$(TZ="America/Mexico_City" date '+%Y-%m-%d %H:%M:%S') - Eliminado: $target" >> backups/deletion.log
}
```

### Recommended environment variables

```bash
export BACKUP_DIR="/path/to/backups"
export BACKUP_RETENTION_DAYS="30"
export BACKUP_COMPRESS_AFTER_DAYS="7"
export BACKUP_LOG_FILE="$BACKUP_DIR/backup.log"
```

## Backup maintenance

### File retention

- Daily backups: retain for 30 days
- Manual backups: retain for 90 days
- Pre-deploy backups: retain for 180 days
- Pre-delete backups: retain permanently (archive after 1 year)

### Automatic compression

Backups older than 7 days should be compressed automatically to optimise storage space:

```bash
# Comprimir respaldos antiguos
find backups/ -name "*.bkp" -mtime +7 -exec gzip {} \;
```

### Automatic cleanup

```bash
# Eliminar respaldos expirados
find backups/daily/ -name "*.bkp*" -mtime +30 -delete
find backups/manual/ -name "*.bkp*" -mtime +90 -delete
```

---
*Written by Rodrigo Álvarez (@incognia)*
