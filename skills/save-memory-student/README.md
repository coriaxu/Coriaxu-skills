# Save Memory Student

## 适用场景

这个技能适合一轮工作对话结束后，用一句“`/save-memory`”把今天做过的事先记下来。它会先整理出一版准备保存的内容给你看。你确认后，AI 会把内容写进桌面的 `AI 工作日报`，方便后面回看和整理周报素材。

## 不会做什么

它不会改你的业务文件，也不会替你自动存档。它不接 Google Drive，不写全局规则，也不会直接帮你产出成品周报。它做的是把当天工作记录清楚，把项目里的最新进展记住。

## 学员单 AI 安装说明

你只需要安装自己正在用的那一个 AI 目录，不需要像多环境维护那样同步三处。

- 用 `Codex`：放到 `~/.codex/skills/save-memory-student/`
- 用 `Claude`：放到 `~/.claude/skills/save-memory-student/`
- 用 `Gemini`：放到 `~/.gemini/antigravity/skills/save-memory-student/`

只有你自己平时同时使用多个 AI，才需要分别安装到多个目录。

## 与 init-memory-student 的配合关系

`save-memory-student` 可以单独使用。哪怕项目里还没有 `AI_专属/`，它也能把今天的工作写进桌面的 `AI 工作日报`。如果你先用过 `init-memory-student`，让项目有了 `AI_专属/`，那它就会在写日报的同时，把这个项目的任务计划、发现记录、决策日志、临时草稿一起更新掉。这样下次回来，AI 就更容易接着干。
