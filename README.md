# math-in-chat

A Claude skill that makes Claude write math in chat replies as LaTeX, so formulas render in the
Claude apps (claude.ai, desktop, mobile, and Claude Code on the web) instead of breaking into
stray italics.

**Why:** Markdown reads `π̂_k = n_k/n` as italics between the two underscores, drops braces, and
Unicode combining marks (π̂, c̃) drift off their letter. Inline `$...$` and display `$$...$$` render
correctly; long formulas inside table cells do not (tested in the Claude app, October 2026).

The rules are in [`skills/math-in-chat/SKILL.md`](skills/math-in-chat/SKILL.md).

## Install

**Claude Code / Codex（同一仓库，两种原生入口）**

本仓库的 `main` 同时包含 `.claude/skills/math-in-chat/` 和 `.agents/skills/math-in-chat/`。
根目录 `CLAUDE.md` 与 `AGENTS.md` 分别指向对应规则，原始 `skills/math-in-chat/` 继续保留。
要接入一门课程，可从本仓库运行：

```bash
python3 scripts/install_skills.py --target /absolute/path/to/course
```

安装器同时复制两个平台的完整技能文件夹；重复运行时保留相同副本，遇到不同内容会停下，绝不直接覆盖。
若不准备提交这些本地副本，可在课程仓库自己的 `.git/info/exclude` 中排除相应路径。
原生技能列表可能需要重新加载；当前会话仍可直接读取对应 `SKILL.md` 并遵循其规则。

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

## Codex 版

Claude 原版保留不变。Codex 版使用标准 `SKILL.md`，仓库内技能目录为 `.agents/skills/`，并提供 `.codex-plugin/plugin.json` 作为技能插件入口。仅克隆到另一个仓库旁边，不等于账号级安装或本 session 已加载。

使用方式：

1. 在以本仓库为工作目录的新 Codex 会话中发现仓库技能；技能列表是否更新以实际客户端为准，当前会话可能需要重开。
2. 要在课程仓库使用，把需要的**完整技能文件夹**复制到课程的 `.agents/skills/`，包括 `references/`、脚本和 `examples/`。目标已有同名技能时先比较，勿直接覆盖。
3. 若客户端支持技能安装器，可给它下方的 GitHub 技能目录 URL；支持自定义插件的客户端也可使用本仓库的插件清单。安装后按客户端要求重新加载。

Codex 原生技能文档：https://developers.openai.com/codex/skills 。技能插件示例：https://github.com/openai/plugins 。不同客户端的自定义技能/插件入口可能不同，仓库存在不代表已在所有客户端启用。

保留原版学习规则、辅助脚本和示例。必要适配只有：`.claude/skills` → `.agents/skills`、课程规则 → `AGENTS.md`、`/skill-name` → `$skill-name`、Claude 专用文件/Artifact 输出 → 当前 Codex 可用工具及独立文件。LaTeX 渲染取决于实际客户端；历史 Claude 测试结果不当成 Codex 验证。

各技能 `references/conversion.json` 记录原始提交和文件 SHA-256，方便核对及后续同步。未来修改 Claude 版后，应同步对应 Codex 版并重新检查；两个版本不会自动互相更新。

### math-in-chat

- Claude / 通用原版：`skills/math-in-chat/SKILL.md`
- Codex：`.agents/skills/math-in-chat/SKILL.md`
- 安装 URL：https://github.com/jackiectl2/math-in-chat/tree/main/.agents/skills/math-in-chat
- 显式使用：`$math-in-chat 请按这个技能排版接下来的数学解释。`

两个平台的版本统一维护在 `main`。更新原始 Claude 规则时，也同步 `.claude/skills/math-in-chat/SKILL.md`；Codex 版保留对应规则并适配客户端差异。
