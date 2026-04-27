# 执行手册

## 路径常量

```bash
ZONE="$HOME/Desktop/个人悬置区"
ARCHIVE="$ZONE/归档"
```

首次使用前创建目录：

```bash
mkdir -p "$ZONE" "$ARCHIVE"
```

如果 `README.md` 不存在，可创建一个简短说明：

```bash
cat > "$ZONE/README.md" <<'EOF'
# 个人悬置区

这里保存“重要但还没想清楚”的议题。

- 根目录：当前仍在悬置中的卡片
- 归档/：已经有结论的卡片
EOF
```

## 动作一：建卡

### 触发

用户明确说“悬置”时直接建卡。

用户只说“先放一放”“回头再说”等模糊表达时，先问一句是否需要保存到悬置区。确认后再建卡。

### 步骤

1. 提炼主题，主题要能一眼看懂这件事。
2. 用 `date +%Y-%m-%d` 获取日期。
3. 生成文件名：`YYYY-MM-DD-主题.md`。
4. 如果重名，追加 `-2`、`-3`。
5. 按 `card-template.md` 写入内容。

### 示例命令

```bash
ZONE="$HOME/Desktop/个人悬置区"
ARCHIVE="$ZONE/归档"
mkdir -p "$ZONE" "$ARCHIVE"

TODAY=$(date +%Y-%m-%d)
SLUG="博客方案"
TARGET="$ZONE/${TODAY}-${SLUG}.md"

i=2
while [ -f "$TARGET" ]; do
  TARGET="$ZONE/${TODAY}-${SLUG}-${i}.md"
  i=$((i+1))
done
```

写入模板：

```bash
cat > "$TARGET" <<EOF
---
created: $TODAY
status: 悬置中
source: agent
updated: $TODAY
---

## 背景

（填写背景）

## 待判断的核心问题

- （填写还没想清楚的判断点）

## 相关材料

- （填写链接、文件或对话摘要）

## 判断讨论记录

（暂无）
EOF
```

## 动作二：查询

### 触发

用户说“看一下悬置区”“悬置区里有什么”“现在挂着哪些事”。

### 命令

```bash
python3 - <<'PY'
from pathlib import Path
from datetime import date, datetime

zone = Path.home() / "Desktop" / "个人悬置区"
today = date.today()

if not zone.exists():
    print("悬置区还不存在。")
    raise SystemExit

items = []
for path in zone.glob("*.md"):
    if path.name == "README.md":
        continue
    text = path.read_text(encoding="utf-8")
    if "status: 悬置中" not in text:
        continue
    created = None
    for line in text.splitlines():
        if line.startswith("created:"):
            created = line.split(":", 1)[1].strip()
            break
    days = 0
    if created:
        days = (today - datetime.strptime(created, "%Y-%m-%d").date()).days
    items.append((days, path.stem))

for days, stem in sorted(items, reverse=True):
    suffix = "（建议重新判断）" if days >= 7 else ""
    print(f"- {stem} · 已悬置 {days} 天{suffix}")
PY
```

如果没有结果，回复“悬置区里没有活跃卡片”。

## 动作三：归档

### 触发

用户明确说某件事已经决定做、不做、结束，或要求归档。

### 步骤

1. 在根目录匹配相关卡片。
2. 零匹配时，请用户给更准确的关键词。
3. 多匹配时，列出候选文件名让用户选。
4. 一匹配时，更新 `status` 和 `updated`。
5. 正文末尾追加“最终结论”区块。
6. 移入 `归档/`。

### 示例命令

```bash
ZONE="$HOME/Desktop/个人悬置区"
ARCHIVE="$ZONE/归档"
mkdir -p "$ARCHIVE"

KEYWORD="博客"
find "$ZONE" -maxdepth 1 -type f -name "*${KEYWORD}*.md"
```

归档时可用 `python3` 安全改写：

```bash
python3 - <<'PY'
from pathlib import Path
from datetime import date

path = Path.home() / "Desktop" / "个人悬置区" / "2026-04-27-博客方案.md"
archive_dir = path.parent / "归档"
archive_dir.mkdir(exist_ok=True)

today = date.today().isoformat()
decision = "不做"
reason = "现有方案已经够用，暂时没有必要新增一套工具。"
status = "已决定不做" if decision == "不做" else "已决定做"

text = path.read_text(encoding="utf-8")
text = text.replace("status: 悬置中", f"status: {status}", 1)
text = text.replace(next(line for line in text.splitlines() if line.startswith("updated:")), f"updated: {today}", 1)
text += f"""

## 最终结论

### {today}

决定：{decision}

原因：{reason}
"""

path.write_text(text, encoding="utf-8")
path.rename(archive_dir / path.name)
PY
```

## 冲突处理

- 同一天同主题重名：文件名追加 `-2`、`-3`。
- 匹配到多张卡：不要自行选择，列出候选让用户确认。
- 活跃目录不存在：自动创建。
- `归档/` 不存在：自动创建。
- 已归档卡片不主动修改，除非用户明确要求。
