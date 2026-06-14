# reading-companion.config.md 模板

首次使用时由 Onboarding 自动生成，放在笔记库根目录。用户可以随时手动修改。

```yaml
# 读书陪读配置

profile:
  reader_name: ""          # 希望 AI 怎么称呼你，留空就用"你"
  assistant_name: "AI"     # 卡片署名用的助手名，可以自定义
  language: "zh-CN"

library:
  root: ""                 # 读书笔记库根目录，绝对路径（必填）
  bookshelf_file: "00-当前加工书架.md"
  link_style: "markdown"   # markdown / wikilink（Obsidian 等双链软件选 wikilink）

cards:
  template: "light"        # light（三层轻量卡）/ full（六字段完整卡）
  write_policy: "preview_then_write"  # preview_then_write / draft_only
  filename_max_chars: 56   # 文件名主题句最长字符数；中文建议 28，英文建议 56
  duplicate_policy: "ask"  # ask / suffix；同名卡片默认先问，不静默覆盖

research:
  web_policy: "when_available"  # when_available / never
  chapter_policy: "mark_unknown" # mark_unknown；查不到章节时写"章节待确认"
```

## 字段说明

- `profile.reader_name`：可留空。填了之后，AI 在对话和卡片里用这个称呼。
- `profile.assistant_name`：存档卡片 frontmatter 的 `assistant` 字段和「[助手名]的延伸/洞察」标题用它。默认 `AI`，你可以改成自己给 AI 起的名字。
- `library.root`：唯一必填项。所有书的文件夹、书架文件都放在这个目录下。
- `library.link_style`：决定索引页和书架里的链接写法。`wikilink` 生成 `[[卡片标题]]`，`markdown` 生成 `[卡片标题](./卡片标题.md)`。用普通编辑器（VS Code、记事本）的选 `markdown`。
- `cards.template`：`light` 是默认档，卡片只有三层（作者原文 / 我的分享 / 助手的延伸），上手轻；`full` 是进阶档，增加问题轨迹、行动线索、一句话结晶三个字段，记录更完整但每次存档更重。
- `cards.write_policy`：`preview_then_write` 是默认值，预览确认后写入文件；`draft_only` 用于没有文件读写权限的环境，AI 只输出完整文件内容，用户自己保存。
- `cards.filename_max_chars`：标题生成文件名时的长度上限。标题过长时截断主题句，不截断日期。
- `cards.duplicate_policy`：同名文件处理方式。`ask` 先问续写、改名或另存；`suffix` 自动追加 `-2`、`-3`。
- `research.web_policy`：`when_available` 表示环境允许联网时可查作者、目录和章节；`never` 表示只基于用户提供材料和已有知识。
- `research.chapter_policy`：固定为 `mark_unknown`。章节查不到就写 `章节待确认`，不猜。

## 最小配置示例

```yaml
library:
  root: "/Users/me/Documents/reading-notes"
```

其余字段全部走默认值：助手署名 AI、markdown 链接、轻量卡、预览后写入。

## Obsidian 用户示例

```yaml
profile:
  assistant_name: "书僮"

library:
  root: "/Users/me/ObsidianVault/读书笔记"
  link_style: "wikilink"

cards:
  template: "full"
  duplicate_policy: "ask"
```
