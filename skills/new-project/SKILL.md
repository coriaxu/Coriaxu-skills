---
name: new-project
description: Initialize a new L&D or business project for non-technical users. Use when the user says /new-project, asks to start a new project, or wants the AI to interview first and then create a filled project folder with README and AI memory files.
---

# New Project

面向非技术用户的新项目初始化 Skill。

重点不是生成空壳目录，而是先问清项目，再把当前已知信息直接写进项目文件。

## Boundary

适用场景：

- 用户明确说 `/new-project`
- 用户说“新建项目”“帮我建一个项目”
- 项目属于培训、业务、运营、内容、管理等非技术工作

不适用场景：

- 代码开发、脚本工具、工程类项目
- 只想讨论想法，还不准备创建文件
- 只想整理已有项目，不需要新建结构

技术开发项目应改用 `init-project`。

## Workflow

1. 先判断项目类型。若明显是技术开发项目，切到 `init-project`。
2. 确认项目名称与创建位置。
   - 如果用户没说项目名，先问项目名。
   - 如果用户没说路径，优先使用当前工作目录；如果当前目录不适合，补问一句放在哪里。
3. 用自然对话收集五项信息：
   - 项目做什么
   - 为什么做
   - 目标是什么
   - 用户角色
   - AI 角色
4. 提取已知信息，不要把访谈做成填表。
   - 用户一次说全，直接提取。
   - 用户只说了部分，允许先创建。
   - 用户只敲 `/new-project`，必须先追问，不能直接创建空文件。
5. 生成项目结构与初始文件。优先运行：

```bash
python3.12 scripts/create_new_project.py --project-name "项目名" --target-dir "目标目录" --what "项目做什么" --why "为什么做" --goal "成功标准" --user-role "用户角色" --ai-role "AI角色"
```

6. 创建完成后明确说明：
   - 哪些信息已经写进文件
   - 哪些信息仍待补充
   - 后续补充信息时会更新 `README.md`、`AI_专属/task_plan.md`、`AI_专属/findings.md`、`AI_专属/scratchpad.md`
7. 用户后续补充信息时：
   - 更新已有文件，不重建空模板
   - 保留 `AI_专属/decisions.md` 的连续记录

## Output Contract

项目结构必须包含：

- `01_工作台/`
- `02_经验库/`
- `03_交付物/`
- `04_归档/`
- `AI_专属/`
- `README.md`

`AI_专属/` 必须包含：

- `task_plan.md`
- `findings.md`
- `decisions.md`
- `scratchpad.md`

`README.md` 至少包含：

- 项目名称
- 项目简介
- 目标
- 负责人角色
- AI 协作方式

所有文件都必须根据当前访谈结果写入内容。即使信息不完整，也要明确写出“已知信息”和“待补充项”，不能留纯空白模板。

## Reference Map

- 读取 `references/checklist.md`，确认访谈、路径、文件映射与补录更新规则。
- 读取 `evals/trigger_cases.json` 与 `evals/semantic_config.json`，检查触发边界是否稳定。
