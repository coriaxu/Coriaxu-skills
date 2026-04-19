# Coriaxu Skills

（[@coriaxu](https://github.com/coriaxu)）的个人 Claude Code / Codex / Gemini Antigravity skill 库，**兼做三处本地 skill 目录的权威同步源**。

## 这是什么

一份我日常在用的 skill 合集，覆盖四类场景：

- **通用工具类**：笔记处理、内容制作、截图、EPUB 生成等
- **思维教练类**：人物视角（Elon Musk / Peter Senge）、商业诊断（dbs 系列）、圆桌讨论
- **元技能类**：skill 创作器、skill 优化器（darwin）、skill 规划器
- **集成工具类**：Obsidian、Google Workspace、web-access、claude-to-im 桥接

其中一部分是原创，一部分是社区作者的杰出作品，我收录进来方便本地一键部署 + 致谢原作者。**所有第三方作者和原协议见 [CREDITS.md](CREDITS.md)**。

👉 **看完整技能清单（触发词 + 一句话介绍）**：[docs/skill-catalog.md](docs/skill-catalog.md)

## 🤖 最简单的方式：让你的 AI 助理帮你装

完全不熟命令行？**把下面这段话复制粘贴给你的 Claude Code / Codex / Gemini Antigravity**，把 `<skill-name>` 换成你想装的那个：

> 请打开以下链接阅读安装指引，并按指引帮我安装其中的 `<skill-name>`：
> https://github.com/coriaxu/Coriaxu-skills/blob/main/docs/ai-install-guide.md

可选 skill 列表：[skills/](skills/) 目录下每一个子文件夹就是一个。AI 助理会自动帮你 clone + 安装 + 提示重启。

## 💻 命令行方式（推荐懂 shell 的朋友）

```bash
# 首次：克隆仓库
git clone https://github.com/coriaxu/Coriaxu-skills.git ~/Code/Coriaxu-skills
cd ~/Code/Coriaxu-skills

# 装某一个 skill
./install.sh yao-meta-skill

# 装多个
./install.sh yao-meta-skill nuwa-skill

# 装全部
./install.sh

# 预览不写盘
./install.sh --dry-run yao-meta-skill

# 看可选 skill
./install.sh --list
```

`install.sh` 会自动把 skill 同步到本机实际存在的这几处（不存在的目录会跳过）：

- `~/.claude/skills/`（Claude Code）
- `~/.codex/skills/`（Codex）
- `~/.gemini/antigravity/skills/`（Gemini Antigravity）

## 更新已有 skill

```bash
cd ~/Code/Coriaxu-skills
git pull
./install.sh <skill-name>   # 或跑过的所有
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
├── README.md              # 你在看的这个
├── LICENSE                # MIT
├── CREDITS.md             # 第三方作者致谢（重要）
├── install.sh             # 同步 skill 到本地（支持选装）
├── skills/                # 所有 skill 的权威源
│   ├── yao-meta-skill/
│   ├── nuwa-skill/
│   └── ...
└── docs/
    ├── skill-catalog.md     # 完整技能清单（触发词 + 介绍）
    ├── ai-install-guide.md  # 给 AI 助理的安装 SOP
    └── origin-audit.md      # 每个 skill 的归属溯源表
```

## 贡献 skill

欢迎 PR。新 skill 放在 `skills/<skill-name>/SKILL.md`，遵循 Anthropic 官方 skill 格式（YAML frontmatter + Markdown 正文）。

## 协议

本仓库整体采用 [MIT 协议](LICENSE)。第三方 skill 各自保留原始 LICENSE 文件（均为 MIT）。详见 [CREDITS.md](CREDITS.md)。

## 致谢

感谢以下开源作者的 skill，没有他们就没有这个仓库的完整形态：花叔（nuwa-skill、darwin-skill）、小能熊老师（三级笔记）、姚金刚（yao-meta-skill）、op7418、MrGeDiao、一泽 Eze、RKiding。

---

_maintained by 徐浩 [@coriaxu](https://github.com/coriaxu) · 2026_
