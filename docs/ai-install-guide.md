# AI Install Guide — 让你的 AI 助理帮你装 skill

适用场景：你是 **Coriaxu-skills 的使用者**，自己不熟命令行，但在用 **Claude Code / Codex / Gemini Antigravity** 这类 AI 助理。让 AI 帮你搞定安装。

---

## 📨 给使用者：复制这段给你的 AI 助理

你只需要把下面这段完整复制粘贴给你的小助理，把 `<skill-name>` 换成你想装的那个 skill：

> 请打开以下链接阅读安装指引，并按指引帮我安装其中的 `<skill-name>`：
> https://github.com/coriaxu/Coriaxu-skills/blob/main/docs/ai-install-guide.md

例如你想装 yao-meta-skill，就说：

> 请打开以下链接阅读安装指引，并按指引帮我安装其中的 `yao-meta-skill`：
> https://github.com/coriaxu/Coriaxu-skills/blob/main/docs/ai-install-guide.md

你想看可选 skill 列表，就到 [https://github.com/coriaxu/Coriaxu-skills/tree/main/skills](https://github.com/coriaxu/Coriaxu-skills/tree/main/skills) 浏览。

---

## 🤖 给 AI 助理：安装 SOP（请严格执行）

用户希望你帮 Ta 从 [Coriaxu-skills](https://github.com/coriaxu/Coriaxu-skills) 安装一个 / 多个 skill 到本地。按以下步骤操作。

### 步骤 1 — 确认要安装的 skill 名

从用户消息里提取 skill 名。如果用户没明确说，或者说得含糊，主动询问并给出可选项。
可选 skill 列表见 [`skills/` 目录](https://github.com/coriaxu/Coriaxu-skills/tree/main/skills)。

### 步骤 2 — 准备本地仓库

首次安装需要 clone 仓库到 `~/Code/Coriaxu-skills/`；已 clone 过就更新到最新。

```bash
if [ -d "$HOME/Code/Coriaxu-skills" ]; then
  cd "$HOME/Code/Coriaxu-skills" && git pull --quiet
else
  mkdir -p "$HOME/Code" && cd "$HOME/Code" && \
    git clone --quiet https://github.com/coriaxu/Coriaxu-skills.git
fi
```

### 步骤 3 — 执行安装

用仓库自带的 `install.sh` 装指定 skill。**永远带 skill 名作为参数**，不要不带参数跑（那会装全部）。

```bash
cd "$HOME/Code/Coriaxu-skills" && ./install.sh <skill-name>
```

多个 skill 就空格隔开：

```bash
cd "$HOME/Code/Coriaxu-skills" && ./install.sh yao-meta-skill nuwa-skill
```

`install.sh` 会自动把 skill 同步到 `~/.claude/skills/`、`~/.codex/skills/`、`~/.gemini/antigravity/skills/` 中本机实际存在的那几处，不存在的目录会跳过，不会报错。

### 步骤 4 — 告诉用户结果

安装成功后，给用户两句话的反馈：

1. 已经装好了 `<skill-name>`，同步到了哪几个 Agent 目录（照 `install.sh` 输出的 Target 行回报）
2. 提示用户 **重启对应的 AI Agent**（Claude Code / Codex / Gemini Antigravity）才能加载新 skill

### 常见问题处理

| 情况 | 处理方式 |
|------|----------|
| `install.sh` 报 `skill 'xxx' not found` | 列出可用 skill（脚本会自动打印），请用户确认正确的 skill 名 |
| 所有 target 都不存在 | 告诉用户本机似乎没装 Claude Code/Codex/Gemini，需先装好其中任何一个再重试 |
| `git clone` 失败（网络） | 让用户检查网络或 VPN，或者改用 `git clone https://mirror.ghproxy.com/https://github.com/coriaxu/Coriaxu-skills.git` 走镜像 |
| 用户说"装全部" | 不带参数跑 `./install.sh`，提醒用户这会装 4+ 个 skill 并占用若干 MB 磁盘 |
| 用户想预览不想真装 | 加 `--dry-run` 参数跑一遍，给用户看计划 |

### 🚫 不要做的事

- 不要用 `sudo`，`~/.claude/skills/` 这类都是用户目录，不需要管理员权限
- 不要手动 `cp -r` 单个文件，用 `install.sh` 保证一致性
- 不要改 `skills/` 源文件或 `install.sh`，用户如果想改建议他们 fork 仓库
- 不要在用户没确认的情况下全量安装

---

## 📋 一次完整示例（从用户视角）

> **用户**：请打开以下链接阅读安装指引，并按指引帮我安装其中的 `nuwa-skill`：
> https://github.com/coriaxu/Coriaxu-skills/blob/main/docs/ai-install-guide.md

> **AI 助理**：
> 好的，我看到你想装 `nuwa-skill`（花叔的女娲造人术）。开始执行：
>
> *[运行步骤 2 + 3 的命令]*
>
> 已同步到 `~/.claude/skills/nuwa-skill/`。请重启 Claude Code，`nuwa-skill` 就可以用了。触发词："女娲"、"蒸馏 XX"、"造一个 XX 的 skill"。

---

_最后更新：2026-04-19 · [Coriaxu-skills](https://github.com/coriaxu/Coriaxu-skills)_
