# LaTeX document generation rules

This document defines the conventions for generating corporate LaTeX documents on Fedora Linux with XeLaTeX.

## Pandoc vs. LaTeX from scratch

**Pandoc can convert Markdown to PDF via LaTeX, but the result is mediocre and inconsistent:**
- Tables do not fill the page width and have incorrect column widths.
- Code blocks (`listings`) leave blank lines between the background and the text.
- The corporate header/footer requires external patches (`--include-in-header`) that accumulate and are fragile.
- Missing-package errors are hard to anticipate and block compilation.

**Correct workflow:**
1. Use the Markdown as a **content reference** (text, tables, data).
2. Write the `.tex` from scratch following this document.
3. Compile directly with `xelatex`.

Pandoc is only acceptable for quick internal drafts with no visual quality requirement.

## Engine and compilation

- **Mandatory engine:** `xelatex` — native Unicode support, fontspec, and emoji without conversions.
- **Compilation:** `xelatex -interaction=nonstopmode file.tex`
- **Error checking:** use single quotes in `grep` to avoid issues with `!` in zsh:
  ```bash
  xelatex -interaction=nonstopmode file.tex 2>&1 | grep -iE 'error|missing|not found'
  ```
- **Note:** `grep` returns exit code 1 when no matches are found (no errors). Do not confuse this with a real failure.
- **Installing missing packages:**
  ```bash
  sudo dnf install -y 'tex(name.sty)'
  ```

## Fonts

- **Body:** `Liberation Sans` (sans-serif; do NOT use Liberation Serif in corporate documents)
- **Code:** `Liberation Mono`
- **Emoji:** `Noto Emoji` (already installed on Fedora via `google-noto-emoji-fonts`)
- Minimal configuration:
  ```latex
  \usepackage{fontspec}
  \setmainfont{Liberation Sans}
  \setmonofont{Liberation Mono}
  \usepackage{newunicodechar}
  \newfontfamily\emojifont{Noto Emoji}[Renderer=HarfBuzz]
  \newunicodechar{❌}{{\emojifont ❌}}
  \newunicodechar{✅}{{\emojifont ✅}}
  ```

## Page and typography

- **Margins:** `\usepackage[margin=2cm]{geometry}`
- **Paragraph spacing:** `\usepackage{parskip}` (no indentation; vertical space between paragraphs)
- **Typographic enhancement:** `\usepackage{microtype}`

## Standard header

```latex
\includegraphics[height=1.8cm]{promad-logo.png}\\
\makebox[\linewidth][r]{\footnotesize\textit{Última modificación: DD de mes de AAAA, HH:MM (CST)}}

\vspace{10pt}
{\LARGE\bfseries Título principal}\\[4pt]
{\large Subtítulo descriptivo}
\vspace{8pt}
```

**Rules:**
- The timestamp goes **below the logo**, right-aligned with `\makebox[\linewidth][r]{...}`
- Do **not** use `\hfill` at the start of a line — it does not work in that context
- Title in `\LARGE\bfseries`; subtitle in `\large` without bold
- Subtitle with sentence-case initial (title case)
- Logo always local (`promad-logo.png`); **never** use URLs in `\includegraphics`
- Download images with `curl -sL URL -o file.png` before compiling

## Document metadata

Use the `\meta` command for consistency:

```latex
\newcommand{\meta}[2]{\textbf{#1:} #2\\}
```

```latex
\meta{Fecha}{2026-03-23}
\meta{Elaborado por}{Rodrigo Álvarez — Líder DevOps, Promad}
```

## Section titles

```latex
\usepackage{titlesec}
\titleformat{\section}{\large\bfseries}{}{0em}{}
\titlespacing{\section}{0pt}{14pt}{6pt}
```

- **No** decorative lines under titles (`\hrule` in blue or similar)
- Colour lines go **in tables**, not in titles

## Tables

**Required packages:**
```latex
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{colortbl}
\usepackage{array}
\renewcommand{\arraystretch}{1.35}
\setlength{\tabcolsep}{8pt}
```

**Border colour:** define once in the preamble:
```latex
\arrayrulecolor{promad}   % borders in PROMAD blue
```

**Standard structure** (full-width table):
```latex
\begin{tabularx}{\linewidth}{>{\bfseries}l X}
\toprule
\rowcolor{rowhead} Column 1 & Column 2 \\
\midrule
Value A & Long description that wraps automatically \\
\bottomrule
\end{tabularx}
```

**Recommended column specifiers:**
- `X` — flexible column that absorbs remaining space
- `l` — fixed left-aligned
- `c` — fixed centred
- `>{\bfseries}l` — left-aligned bold (for parameter column)

**Critical rules:**
- Always use `\linewidth` as the table width, **never** `\textwidth` inside minipages
- `\toprule`, `\midrule`, `\bottomrule` from `booktabs` — **not** `\hline`
- `\rowcolor{rowhead}` on the header row for a soft grey background

## Code blocks

**Package:** `tcolorbox` — generates blocks with a solid background and rounded corners.
`listings` only colours line by line and leaves blank spaces between them.

```latex
\usepackage{tcolorbox}
\tcbuselibrary{listings,skins,breakable}
\tcbset{
  codestyle/.style={
    colback=codebg,
    colframe=codebg,
    boxrule=0pt,
    arc=5pt,
    left=10pt, right=10pt, top=8pt, bottom=8pt,
    breakable,
    listing only,
    listing options={
      basicstyle=\ttfamily\small\color{codefg},
      breaklines=true,
      columns=fullflexible,
    }
  }
}
\newtcblisting{codebox}{codestyle}
```

Usage:
```latex
\begin{codebox}
apt update && apt dist-upgrade
\end{codebox}
```

## Corporate colour palette

```latex
\usepackage{xcolor}
\definecolor{codebg}{HTML}{2d2d2d}    % code block background
\definecolor{codefg}{HTML}{f8f8f2}    % code block text
\definecolor{promad}{HTML}{00B2E0}    % PROMAD blue (table borders, accents)
\definecolor{rowhead}{HTML}{e8e8e8}   % table header background
```

## Standard footer

```latex
\vfill
\noindent\rule{\linewidth}{0.4pt}
\vspace{4pt}

\textbf{Rodrigo Ernesto Álvarez Aguilera} — Líder DevOps\\
\href{mailto:ralvarez@kabatone.com}{ralvarez@kabatone.com} · Ejército Nacional 57, Miguel Hidalgo · +52 (55) 7980-9502
```

**Rules:**
- Separator: thin grey line (`0.4pt`), **not** blue
- **No avatar** — profile images do not work well in LaTeX without CSS
- Contact in one or two lines of plain text

## Images

- **Mandatory:** download locally before compiling
- **Do not use URLs** in `\includegraphics` with XeLaTeX
- Verify with `file image.png` that the download was successful
- Suppress "Figure 1":
  ```latex
  \usepackage{caption}
  \DeclareCaptionFormat{empty}{}
  \captionsetup[figure]{format=empty,skip=0pt}
  ```

## Packages to install on Fedora (session reference)

```bash
sudo dnf install -y pandoc texlive-xetex texlive-collection-latexrecommended
sudo dnf install -y 'tex(newunicodechar.sty)'
sudo dnf install -y 'tex(framed.sty)'
sudo dnf install -y 'tex(xurl.sty)'
sudo dnf install -y 'tex(tcolorbox.sty)'
sudo dnf install -y google-noto-emoji-fonts
```

---

*Written by Rodrigo Álvarez (@incognia)*
