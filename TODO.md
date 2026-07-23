# TODO — traducciones y ajustes pendientes

Contexto de referencia:
- Usar el mismo patrón aplicado en `linguistics/linguistica`:
  1) definir versión canónica en inglés internacional,
  2) crear alias espejo cuando aplique,
  3) validar sincronía y referencias.

## 1) CoTs por traducir/normalizar (prioridad alta)
- Traducir a inglés internacional los CoTs que siguen con estructura o contenido principal en español:
  - `cot/context.md`
  - `cot/git_init.md`
  - `cot/backup.md`
  - `cot/quick_backup.md`
  - `cot/lint.md`
  - `cot/mail.md`
  - `cot/release.md`
  - `cot/styling.md`
  - `cot/kube.md`
  - `cot/kubetbs.md`
  - `cot/github_metadata.md`
  - `cot/repo_context.md`
  - `cot/aws_naming.md`
  - `cot/arithmetic.md`
  - `cot/devops.md`
  - `cot/latex.md`
  - `cot/restore.md`
- Mantener solo ejemplos en español cuando sean necesarios como ejemplo lingüístico, no como idioma operativo por defecto.

## 2) Rulesets por traducir/ajustar (prioridad alta)
- Auditar y traducir reglas operativas que sigan predominantemente en español:
  - `rulesets/COMMITTING.md`
  - `rulesets/GIT.md`
  - `rulesets/BACKUPS.md`
  - `rulesets/MAIL.md`
  - `rulesets/RELEASING.md`
  - `rulesets/TODO.md` (histórico, requiere depuración o archivo)
  - `rulesets/TEACHING.md` (validar si queda como excepción por contexto personal)
- Verificar que la política bilingüe por contexto quede explícita y consistente en cada archivo.

## 3) Skills por ajustar (prioridad media)
- Revisar skills con fragmentos aún en español y normalizar a inglés internacional en contexto corporativo:
  - `.agents/skills/git-init/SKILL.md`
  - `.agents/skills/release/SKILL.md`
  - `.agents/skills/commit/SKILL.md` (terminología residual)
- Validar consistencia entre skill ↔ CoT ↔ ruleset para cada flujo.

## 4) Ajustes de consistencia global (prioridad media)
- Actualizar métricas/contadores en `README.md` (CoTs, skills, rulesets) para que coincidan con el estado real.
- Unificar referencias de organización/usuario remotos (`incognia` vs `incogniaops`) donde ya aplique contexto laboral.
- Definir criterio documental para `FILOSOFIA.md` (archivo espejo histórico en español) y su relación con `PHILOSOPHY.md`.
- Añadir una verificación rápida de sincronía para pares alias/canónico (ej. `linguistica` vs `linguistics`) antes de commit.

## 5) Cierre de migración (prioridad baja)
- Ejecutar lint de markdown y revisión de enlaces cuando esté disponible la toolchain local.
- Ejecutar una pasada final de QA lingüístico (UK English en contexto corporativo).
- Registrar en `CHANGELOG.md` el cierre de cada bloque de migración.
