# math-in-chat

A Claude skill that makes Claude write math in chat replies as LaTeX, so formulas render in the
Claude apps (claude.ai, desktop, mobile, and Claude Code on the web) instead of breaking into
stray italics.

**Why:** Markdown reads `π̂_k = n_k/n` as italics between the two underscores, drops braces, and
Unicode combining marks (π̂, c̃) drift off their letter. Inline `$...$` and display `$$...$$` render
correctly; long formulas inside table cells do not (tested in the Claude app, October 2026).

The rules are in [`skills/math-in-chat/SKILL.md`](skills/math-in-chat/SKILL.md).

## Install

**claude.ai (applies to all your chats and to Claude Code cloud sessions)**

1. Zip the skill folder so the zip contains `math-in-chat/SKILL.md` at its root:
   `cd skills && zip -r math-in-chat.zip math-in-chat`
2. On claude.ai go to **Customize → Skills**, click **+ → Create skill → Upload a skill**, and
   upload the zip ([official steps](https://support.claude.com/en/articles/12512180-use-skills-in-claude)).
3. Make sure the skill is toggled on.

**Claude Code (one repository)**

Copy `skills/math-in-chat/` into the repository's `.claude/skills/` and commit it.

## How it triggers

Skills are model-invoked: Claude sees each enabled skill's name and description and loads the
skill when a reply matches, with no slash command needed. The description here is written to match
any reply that contains math. Triggering is a judgment by the model, so for a must-always rule in a
specific project, also put the rule in that repository's `CLAUDE.md`, which is loaded every session.
