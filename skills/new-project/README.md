# new-project Skill

这是一份独立的学员版 `/new-project` Skill 包，按 `yao-meta-skill` 的 Production 思路整理。

它只解决一件事：先用自然对话问清一个非技术项目的关键信息，再创建带初始内容的项目文件夹，而不是吐一套空模板。

## 文件结构

- `SKILL.md`：触发边界、执行流程、输出要求
- `agents/interface.yaml`：Skill 元信息
- `references/checklist.md`：访谈、路径、更新规则
- `scripts/create_new_project.py`：实际创建目录与初始文件
- `evals/trigger_cases.json`：触发用例
- `evals/semantic_config.json`：触发概念配置

## 适用范围

- `/new-project`
- “新建项目”
- “帮我建一个项目”
- 学员要启动一个培训、业务、运营、内容、管理类项目

## 不适用范围

- 代码开发项目
- 只讨论想法，不创建文件
- 只整理已有项目

## 本地校验

```bash
python3.12 /Users/surfin/.codex/skills/yao-meta-skill/scripts/validate_skill.py .
python3.12 /Users/surfin/.codex/skills/yao-meta-skill/scripts/resource_boundary_check.py .
python3.12 /Users/surfin/.codex/skills/yao-meta-skill/scripts/trigger_eval.py --description-file SKILL.md --cases evals/trigger_cases.json --semantic-config evals/semantic_config.json
python3.12 scripts/create_new_project.py --project-name "示例项目" --target-dir /tmp/new-project-skill-demo --what "为业务团队整理一次培训项目" --why "需要统一协作方式" --goal "完成首版方案和资料目录" --user-role "项目负责人" --ai-role "协助访谈、建目录和写初稿"
```
