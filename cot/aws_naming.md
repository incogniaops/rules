---
domain: aws
task: normalisation of asset names for S3 and CloudFront
dificultad: intermediate
longitud_objetivo: medium
validacion: resulting names contain only safe characters, normalised extensions, and generated .tsv log
---
<!-- markdownlint-disable MD041 -->

Reasoning:

- Normalise filenames to be 100% safe as *Object Keys* in Amazon S3 and distributable via Amazon CloudFront.
- Apply strict AWS rules: *case sensitivity*, removal of spaces, filtering of unsafe characters, path and length validation.
- Normalise image and web resource extensions (.jpeg → .jpg, .png, .svg, .ico) for consistency in the *bucket*.
- Generate a log file (.tsv) with the mapping from original name to normalised name for traceability.
- Style and flow references: «~/rules/rulesets/LINGUISTICS.md» ([../rulesets/LINGUISTICS.md](../rulesets/LINGUISTICS.md)), «~/rules/rulesets/COMMITTING.md» ([../rulesets/COMMITTING.md](../rulesets/COMMITTING.md)) and «~/rules/README.md» ([../README.md](../README.md)).

Steps:

1) Action: convert the entire filename and extension to lowercase.
   Result: *Object Keys* in S3 are case-sensitive [1] and CloudFront cache patterns are too (`*.jpg` does not apply to `LOGO.JPG`) [2].

2) Action: replace all whitespace with hyphens (`-`).
   Result: avoids issues with URL encoding (`%20`) and multiple-space sequences that AWS warns may be lost [3, 4, 5].

3) Action: remove accents (ñ → n) and retain only safe characters: `a-z`, `0-9`, `-`, `_`, and `.` (extension only).
   Result: removes non-ASCII characters and symbols requiring special handling (`&`, `$`, `@`, `~`, etc.) [6, 7, 8, 9, 10].

4) Action: normalise file extensions according to the following table.
   - `.jpeg` → `.jpg`
   - `.png` → `.png` (no change)
   - `.svg` → `.svg` (no change)
   - `.ico` → `.ico` (no change)
   - Uppercase extensions are already resolved in step 1 (`.PNG` → `.png`, `.JPEG` → `.jpeg` → `.jpg`).
   Result: consistent and predictable extensions for CloudFront cache policies and S3 *Content-Type* rules.

5) Action: verify the name contains no consecutive dots or relative path sequences (`../`, `./`).
   Result: avoids unexpected behaviour from directory interpretation [7, 12]. The dot appears only before the final extension.

6) Action: validate the resulting path does not exceed 255 characters (CloudFront limit [2]; S3 limit is 1,024 bytes [13]).
   Result: if exceeded, truncate the name preserving the extension and issue a warning.

7) Action: record each transformation in a `.tsv` file with format `original\tnormalised`.
   - Filename: `normalisation_YYYYMMDD.tsv` (CST date: `TZ=America/Mexico_City date +"%Y%m%d"`).
   - First line: headers `original\tnormalised`.
   - One line per processed file, including those that required no changes.
   Result: log file enabling audit and rollback of renames.

Conclusion:

- Resulting names contain only safe characters for S3/CloudFront: lowercase letters, digits, hyphens, underscores, and one dot before the normalised extension.
- The `normalisation_YYYYMMDD.tsv` file documents every transformation for full traceability.
