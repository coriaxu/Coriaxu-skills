# Coriaxu Skills

我（[@coriaxu](https://github.com/coriaxu)）的个人 Claude Code / Codex / Gemini Antigravity skill 库，**兼做三处本地 skill 目录的权威同步源**。

## 这是什么

一份我日常在用的 skill 合集，覆盖四类场景：

- **通用工具类**：笔记处理、内容制作、截图、EPUB 生成等
- **思维教练类**：人物视角（Elon Musk / Peter Senge）、商业诊断（dbs 系列）、圆桌讨论
- **元技能类**：skill 创作器、skill 优化器（darwin）、skill 规划器
- **集成工具类**：Obsidian、Google Workspace、web-access、claude-to-im 桥接

其中一部分是原创，一部分是社区作者的杰出作品，我收录进来方便本地一键部署 + 致谢原作者。**所有第三方作者和原协议见 [CREDITS.md](CREDITS.md)**。

## 快速开始

```bash
# 1. 克隆仓库
git clone https://github.com/coriaxu/Coriaxu-skills.git ~/Code/Coriaxu-skills
cd ~/Code/Coriaxu-skills

# 2. 一键同步到三处 skill 目录
./install.sh
```

`install.sh` 默认同步到：

- `~/.claude/skills/`（Claude Code）
- `~/.codex/skills/`（Codex）
- `~/.gemini/antigravity/skills/`（Gemini Antigravity）

只需要其中一两个目标，改 `install.sh` 里的 `TARGETS` 数组即可。

## 更新已有 skill

```bash
cd ~/Code/Coriaxu-skills
git pull
./install.sh
```

## 占位符约定

部分 skill 里涉及个人工作区路径，统一用两个占位符表达：

| 占位符 | 含义 | 默认值 |
|--------|------|--------|
| `${HOME}` | 用户 home 目录 | shell 自带 |
| `${SKILL_WORKSPACE}` | 你的知识库 / 工作区根目录 | 你自己在 `~/.skillrc` 里设置 |

可选的 `~/.skillrc` 示例：

```bash
# ~/.skillrc
export SKILL_WORKSPACE="$HOME/Documents/my-workspace"
```

不设置也能跑，只是涉及个人工作区的 skill 会 fallback 到 `${HOME}`。

## 仓库结构

```
Coriaxu-skills/
├── README.md            # 你在看的这个
├── LICENSE              # MIT
├── CREDITS.md           # 第三方作者致谢（重要）
├── install.sh           # 一键同步到三处本地目录
├── skills/              # 所有 skill 的权威源
│   ├── yao-meta-skill/
│   ├── nuwa-skill/
│   └── ...
└── docs/
    └── origin-audit.md  # 每个 skill 的归属溯源表
```

## 贡献 skill

欢迎 PR。新 skill 放在 `skills/<skill-name>/SKILL.md`，遵循 Anthropic 官方 skill 格式（YAML frontmatter + Markdown 正文）。

## 协议

本仓库整体采用 [MIT 协议](LICENSE)。第三方 skill 各自保留原始 LICENSE 文件（均为 MIT）。详见 [CREDITS.md](CREDITS.md)。

## 致谢

感谢以下开源作者的 skill，没有他们就没有这个仓库的完整形态：花叔（nuwa-skill、darwin-skill）、op7418、MrGeDiao、一泽 Eze、姚金刚（yao-meta-skill）、RKiding。

---

_maintained by 徐浩 [@coriaxu](https://github.com/coriaxu) · 2026_
