---
name: init-memory-student
description: 为已有项目添加 AI 记忆初始化能力。适用于业务文件夹里主要是 PPT、Excel、Word、PDF 等材料的场景；先根据文件夹名和文件名理解项目，再展示理解和准备写入的内容，用户确认后才创建 AI_专属 四个记忆文件；不新建项目，不改原文件。 Initialize AI memory for an existing business project folder by inferring the project from folder names and filenames, showing the planned memory content first, and only creating AI_专属 files after user confirmation.
---

# Init Memory Student

## 触发方式

- `/init-memory`
- `/memory`
- `初始化记忆`
- `让 AI 记住我的项目`

## 适用边界

- 只用于已有项目
- 只给项目补上 `AI_专属/` 记忆文件
- 不新建项目文件夹
- 不创建 `README.md`、`AGENTS.md`、`CLAUDE.md`
- 不修改用户原有业务文件

## 执行流程

1. 运行 `python3 scripts/scan_project.py <当前目录>`，先看目录名、文件名、文件类型、是否已有 `AI_专属/`。
2. 如果结果是 `existing`，优先汇报已有记忆里的项目目标、当前阶段、最近记录，确认信息是否仍然有效，不重复初始化。
3. 如果结果是 `fresh` 且 `confidence=high`，直接先说出你对项目的理解，再展示准备写入四个记忆文件的具体草稿内容。
4. 如果结果是 `fresh` 且 `confidence=low`，只从 `peek_candidates` 里选 1 到 2 个文件补读前约 500 字。
5. 补读优先配合 `$markitdown` 读取 Office 文件；如果补读失败或还是判断不出来，就直接请用户用一句话说明项目在做什么，不要硬猜。
6. 确认环节是阻塞式的。用户没有明确同意前，不创建任何文件。
7. 用户确认后，才创建 `AI_专属/`，并写入 `task_plan.md`、`findings.md`、`decisions.md`、`scratchpad.md`。

## 生成规则

- `task_plan.md`：写项目目标、当前阶段、下一步。
- `findings.md`：写已经存在的素材、模板、资料来源。
- `decisions.md`：新项目默认写明暂无线下决策记录，后续再补。
- `scratchpad.md`：默认空白，用来放未成熟想法。

详细模板和预填规则见 `references/templates.md`。

## 安全规则

- 已有文件一律不覆盖。
- 如果 `AI_专属/` 已存在但只是空模板，按首次初始化处理。
- 如果 `AI_专属/` 已存在且有实质内容，只做恢复和状态汇报。
- 对用户展示的重点永远是“我理解你的项目是什么”和“我准备写进去的内容”，不是目录结构本身。

触发校验样例见 `evals/trigger_cases.json`。
