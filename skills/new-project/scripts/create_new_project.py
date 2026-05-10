#!/usr/bin/env python3
import argparse
from pathlib import Path


PLACEHOLDER = "待补充"


def clean(value: str | None) -> str:
    return value.strip() if value and value.strip() else ""


def value_or_placeholder(value: str) -> str:
    return value if value else PLACEHOLDER


def missing_items(data: dict[str, str]) -> list[str]:
    mapping = {
        "what": "项目做什么",
        "why": "为什么做",
        "goal": "目标是什么",
        "user_role": "你的角色",
        "ai_role": "AI 的角色",
    }
    return [label for key, label in mapping.items() if not data.get(key)]


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def write_text(path: Path, content: str) -> None:
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def compose_readme(project_name: str, data: dict[str, str]) -> str:
    missing = missing_items(data)
    intro_parts = []
    if data["what"]:
        intro_parts.append(f"这个项目要做的是：{data['what']}")
    else:
        intro_parts.append(f"这个项目要做的内容：{PLACEHOLDER}")
    if data["why"]:
        intro_parts.append(f"这样做的原因是：{data['why']}")
    else:
        intro_parts.append(f"发起原因：{PLACEHOLDER}")

    lines = [
        f"# {project_name}",
        "",
        "## 项目简介",
        "",
        "\n".join(intro_parts),
        "",
        "## 目标",
        "",
        f"- {value_or_placeholder(data['goal'])}",
        "",
        "## 负责人角色",
        "",
        f"- {value_or_placeholder(data['user_role'])}",
        "",
        "## AI 协作方式",
        "",
        f"- {value_or_placeholder(data['ai_role'])}",
        "",
        "## 当前信息状态",
        "",
        "### 已确认",
        "",
        f"- 项目做什么：{value_or_placeholder(data['what'])}",
        f"- 为什么做：{value_or_placeholder(data['why'])}",
        f"- 目标：{value_or_placeholder(data['goal'])}",
        f"- 用户角色：{value_or_placeholder(data['user_role'])}",
        f"- AI 角色：{value_or_placeholder(data['ai_role'])}",
        "",
        "### 待补充",
        "",
    ]
    if missing:
        lines.extend(f"- {item}" for item in missing)
    else:
        lines.append("- 当前五项核心信息已齐全")
    return "\n".join(lines)


def compose_task_plan(data: dict[str, str]) -> str:
    missing = missing_items(data)
    todo_items = missing[:] if missing else ["把项目拆成第一轮执行清单"]
    next_steps = []
    if data["goal"]:
        next_steps.append("根据目标拆出第一版可执行动作")
    else:
        next_steps.append("先补齐项目目标")
    if not data["what"]:
        next_steps.append("补一句项目做什么")
    if not data["ai_role"]:
        next_steps.append("明确 AI 在项目里的具体职责")

    lines = [
        "# 任务计划",
        "",
        "## 项目目标",
        "",
        f"- {value_or_placeholder(data['goal'])}",
        "",
        "## 当前已知情况",
        "",
        f"- 项目做什么：{value_or_placeholder(data['what'])}",
        f"- 为什么做：{value_or_placeholder(data['why'])}",
        f"- 用户角色：{value_or_placeholder(data['user_role'])}",
        f"- AI 角色：{value_or_placeholder(data['ai_role'])}",
        "",
        "## 当前待办",
        "",
    ]
    lines.extend(f"- [ ] {item}" for item in todo_items)
    lines.extend(
        [
            "",
            "## 下一步行动",
            "",
        ]
    )
    lines.extend(f"- [ ] {item}" for item in next_steps)
    return "\n".join(lines)


def compose_findings(data: dict[str, str]) -> str:
    missing = missing_items(data)
    lines = [
        "# 已知信息与发现",
        "",
        "## 已确认信息",
        "",
        f"- 项目做什么：{value_or_placeholder(data['what'])}",
        f"- 为什么做：{value_or_placeholder(data['why'])}",
        f"- 目标是什么：{value_or_placeholder(data['goal'])}",
        f"- 用户角色：{value_or_placeholder(data['user_role'])}",
        f"- AI 角色：{value_or_placeholder(data['ai_role'])}",
        "",
        "## 待验证 / 待补充",
        "",
    ]
    if missing:
        lines.extend(f"- {item}" for item in missing)
    else:
        lines.append("- 当前没有待补充的核心字段")
    return "\n".join(lines)


def compose_scratchpad(data: dict[str, str]) -> str:
    missing = missing_items(data)
    lines = [
        "# 临时工作区",
        "",
        "## 访谈摘录",
        "",
        f"- 项目做什么：{value_or_placeholder(data['what'])}",
        f"- 为什么做：{value_or_placeholder(data['why'])}",
        f"- 目标：{value_or_placeholder(data['goal'])}",
        f"- 用户角色：{value_or_placeholder(data['user_role'])}",
        f"- AI 角色：{value_or_placeholder(data['ai_role'])}",
        "",
        "## 还缺什么",
        "",
    ]
    if missing:
        lines.extend(f"- {item}" for item in missing)
    else:
        lines.append("- 当前没有核心缺口")
    return "\n".join(lines)


def compose_decisions() -> str:
    return "\n".join(
        [
            "# 决策记录",
            "",
            "## 初始化说明",
            "",
            "- 当前暂无关键决策。",
            "- 当项目出现方案取舍、范围变化或关键判断时，从这里开始连续记录。",
        ]
    )


def should_preserve_decisions(path: Path) -> bool:
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8").strip()
    return bool(text) and "当前暂无关键决策" not in text


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a filled new-project scaffold.")
    parser.add_argument("--project-name", required=True, help="Project folder name")
    parser.add_argument("--target-dir", required=True, help="Parent directory for the project")
    parser.add_argument("--what", default="")
    parser.add_argument("--why", default="")
    parser.add_argument("--goal", default="")
    parser.add_argument("--user-role", default="")
    parser.add_argument("--ai-role", default="")
    args = parser.parse_args()

    data = {
        "what": clean(args.what),
        "why": clean(args.why),
        "goal": clean(args.goal),
        "user_role": clean(args.user_role),
        "ai_role": clean(args.ai_role),
    }

    root = Path(args.target_dir).expanduser().resolve() / args.project_name.strip()
    ai_dir = root / "AI_专属"

    for dirname in ("01_工作台", "02_经验库", "03_交付物", "04_归档", "AI_专属"):
        ensure_dir(root / dirname)

    write_text(root / "README.md", compose_readme(args.project_name.strip(), data))
    write_text(ai_dir / "task_plan.md", compose_task_plan(data))
    write_text(ai_dir / "findings.md", compose_findings(data))
    write_text(ai_dir / "scratchpad.md", compose_scratchpad(data))

    decisions_path = ai_dir / "decisions.md"
    if not should_preserve_decisions(decisions_path):
        write_text(decisions_path, compose_decisions())

    print(root)


if __name__ == "__main__":
    main()
