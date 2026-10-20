---
name: math-in-chat
description: "Formatting rule for any reply that contains math, formulas, variables with subscripts or superscripts, Greek letters, hats/tildes, fractions, sums, matrices or equations, in any project or course. Use whenever writing math in a chat reply so it renders correctly in Codex chat surfaces that support LaTeX, with an ASCII fallback for surfaces that do not."
---

# Math in chat replies

Use Markdown plus LaTeX when the current Codex chat surface supports it. Math written as plain text with `_` and `^`
(e.g. `π̂_k = n_k/n`) breaks: Markdown reads the pair of underscores as italics, braces vanish,
and Unicode combining marks (π̂, c̃) drift off their letter. The original Claude skill records these observations from the student's Claude app
(Oct 2026); do not treat them as verification of the current Codex surface: inline `$...$` and display `$$...$$` render; a long formula inside a table cell
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
7. Surfaces that do not render LaTeX (a terminal or editor surface without math rendering): write each
   formula in a code span with ASCII names (`pi_hat_k = n_k / n`), no Unicode combining marks.
8. Files written to a repository (`.md`) use the same `$...$` / `$$...$$` syntax; GitHub renders it.

## Codex compatibility

Use `$math-in-chat` to request this skill explicitly. Keep the eight rules above.
Do not assume all Codex clients have identical math rendering; use the ASCII fallback
only when the current surface is known not to render LaTeX or the user reports a failure.
The Claude original remains at `skills/math-in-chat/SKILL.md` in the source repository.
