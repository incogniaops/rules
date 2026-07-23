---
name: linguistics
description: "Apply Mexican Spanish linguistic rules to a file: sentence-case titles, angular quotes, italics for loanwords, no anglicisms. Usage: /linguistics <file>"
---
# Mexican Spanish linguistic rules

## Target file

Apply rules to: **$0**

If no file was specified, ask the user which file to review.

## Instructions

1. **Read the full CoT**: Load and follow `~/rules/cot/linguistics.md` from line 1 to end
2. **Scan all headings**: Run `grep -n "^#" $0` and verify each one
3. **Fix titles**: Sentence case only — capitalise first word and proper nouns, nothing else
4. **After colons**: Lowercase after `:` unless it's a proper noun
5. **Loanwords in italics**: *commit*, *pull request*, *pipeline*, *container*, *stack*, *bare-metal*, *sprint*
6. **Angular quotes**: Use «» in Spanish text, "" only inside code blocks
7. **Fix anglicisms**: "realizar" → "hacer/ejecutar", "soportar" → "admitir", "eventualmente" → "finalmente"
8. **Fix peninsularisms**: "ordenador" → "computadora", "fichero" → "archivo"
9. **Verify programmatically**: Run `grep -n "^#" $0` again and document each correction
10. **Verify no Title Case remains**: Every heading should be sentence case
11. **When writing in English, enforce UK spelling**: use International English forms only (e.g. `colour`, `organisation`, `virtualisation`)

## Quick reference

- «IA» not «AI», «TI» not «IT», «Biblioteca» not «Librería»
- «Desplegar» not «deployar», «Respaldar» not «backupear»
- Time: 24h format, CST (Ciudad de México), TZ=America/Mexico_City
- International English (UK): `colour` (not `color`), `organisation` (not `organization`), `virtualisation` (not `virtualization`)
- Proper-noun accents are mandatory even in English text: `México`, `Álvarez`

## References

- Detailed CoT: `~/rules/cot/linguistics.md`
- Rules: `~/rules/rulesets/LINGUISTICS.md`
