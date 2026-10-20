---
name: math-in-chat
description: Formatting rule for any reply that contains math, formulas, variables with subscripts or superscripts, Greek letters, hats/tildes, fractions, sums, matrices or equations, in any project or course. Use whenever writing math in a chat reply so it renders correctly in the Claude apps (claude.ai, desktop, mobile, claude.ai/code).
---

# Math in chat replies

The Claude apps render Markdown plus LaTeX. Math written as plain text with `_` and `^`
(e.g. `π̂_k = n_k/n`) breaks: Markdown reads the pair of underscores as italics, braces vanish,
and Unicode combining marks (π̂, c̃) drift off their letter. Tested on the student's app
(Oct 2026): inline `$...$` and display `$$...$$` render; a long formula inside a table cell
did not; backtick code with Unicode hats looked wrong.

## Rules
1. Every formula and every symbol with a subscript, superscript, hat, tilde or Greek letter goes
   inside LaTeX delimiters, even a single variable: `$\hat{\pi}_k$`, `$x$`, `$K$`.
   - Inline: `$...$`. No space right after the opening `$` or before the closing `$`.
   - Display: `$$...$$` on its own line, with a blank line before and after.
2. Never leave bare `_`, `^` or `*` math in prose.
3. Use LaTeX commands, not Unicode look-alikes: `\hat{\mu}_k`, `\tilde{c}`, `\Sigma`, `\log`,
   `\le`, `\propto`, `\mid` for the "given" bar.
4. Tables: only short math in cells (`$\hat{\pi}_k$`, `$p_k(x)$`), using `\mid` instead of `|`.
   Put any long formula (sums, fractions, products) in a `$$...$$` block outside the table and
   refer to it.
5. A dollar sign meant as money is written `\$`.
6. Code, file names and variable names stay in backticks, never inside `$...$`; when explaining
   code, name the matching symbol in LaTeX (`priors` ↔ $\hat{\pi}_k$).
7. Surfaces that do not render LaTeX (Claude Code terminal, the VS Code extension): write each
   formula in a code span with ASCII names (`pi_hat_k = n_k / n`), no Unicode combining marks.
8. Files written to a repository (`.md`) use the same `$...$` / `$$...$$` syntax; GitHub renders it.
