# course-companion.config.md 模板

把这个文件复制到课程目录或项目根目录，并改成自己的设置。

```yaml
# 课程共学搭档配置

profile:
  display_name: ""
  assistant_role: "thinking partner"
  language: "zh-CN"

knowledge:
  # 可选：none / folder / obsidian
  mode: "none"
  connection_limit: 5

  # folder 模式使用
  knowledge_paths:
    - ""

  # obsidian 模式使用
  vault_root: ""
  scan_paths:
    - "读书笔记"
    - "知识卡片"
    - "课程笔记"
    - "AI 对话记录"
    - "Wiki"

output:
  write_policy: "ask_before_write"
  study_note_output_path: ""
  knowledge_card_output_path: ""
```

## 字段说明

- `profile.display_name`: 用户希望助手怎么称呼自己。可以留空。
- `profile.assistant_role`: 助手角色。建议保留 `thinking partner`。
- `knowledge.mode`: 知识库模式。
- `knowledge.connection_limit`: 最多展示几个强相关连接，建议 3-5。
- `knowledge.knowledge_paths`: 指定文件夹模式要扫描的路径。
- `knowledge.vault_root`: Obsidian vault 根目录。
- `knowledge.scan_paths`: vault 内要扫描的相对目录。
- `output.write_policy`: 建议使用 `ask_before_write`。
- `output.study_note_output_path`: 最终研读笔记保存位置。
- `output.knowledge_card_output_path`: 知识卡片保存位置。

## 最小配置示例：无知识库

```yaml
knowledge:
  mode: "none"
  connection_limit: 5

output:
  write_policy: "ask_before_write"
```

## 指定文件夹示例

```yaml
knowledge:
  mode: "folder"
  connection_limit: 5
  knowledge_paths:
    - "/Users/me/Documents/notes"
    - "/Users/me/Documents/course-notes"
```

## Obsidian 示例

```yaml
knowledge:
  mode: "obsidian"
  connection_limit: 5
  vault_root: "/Users/me/ObsidianVault"
  scan_paths:
    - "knowledge-base"
    - "course-notes"
    - "book-notes"
```
