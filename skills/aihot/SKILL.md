# aihot — AI HOT 中文 AI 资讯查询

> AI HOT (aihot.virxact.com) 中文 AI 资讯查询 Skill。直接查询公开 REST API，无需 API Key，实时返回中文 Markdown 报告。

## 触发词

"今天 AI 圈有什么"、"AI 日报"、"AI 热点"、"最近 AI 发布"、"AI 新闻"、"今天 AI 有啥"、"过去 24 小时大新闻"、"aihot"

## 关键前置：User-Agent 必填

所有 `/api/public/*` API 调用**必须带浏览器 User-Agent**，否则 nginx 返回 403：

```bash
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
```

## 路由规则（第一原则）

| 用户意图 | API 端点 |
|---|---|
| **默认**（"今天 AI 圈"、"过去 24 小时大新闻"、"最近 AI 有啥"） | `GET /api/public/items?mode=selected&since=<语义时间窗口>` |
| **明确说"日报"**（"AI 日报"、"看下日报"） | `GET /api/public/daily`（最新）或 `/daily/{YYYY-MM-DD}` |
| **明确说"全部/完整/所有/全量"** | `GET /api/public/items?mode=all` |
| "最近的论文/模型/产品" | `GET /api/public/items?mode=selected&category=<slug>&since=<7d back>` |
| "OpenAI/Anthropic 最近发的" / "Sora 相关" | `GET /api/public/items?q=<keyword>` |
| "看下精选" | `GET /api/public/items?mode=selected` |

**黄金法则**：泛泛问题默认走 `mode=selected` + 语义 `since`。只有用户明确说"日报"才用 `/daily`；只有说"全部/完整/所有/全量"才用 `mode=all`。

## API 端点速查

| 端点 | 用途 | 关键参数 |
|---|---|---|
| `/api/public/daily` | 最新日报 | 无 |
| `/api/public/daily/{YYYY-MM-DD}` | 按日期查日报 | path: `date` |
| `/api/public/dailies` | 日报归档索引 | `take` (1-180, 默认 30) |
| `/api/public/items` | AI 动态流 | `mode` / `category` / `since` / `take` / `cursor` / `q` |

**约束**：
- Base URL: `https://aihot.virxact.com`
- 认证: 无（匿名访问）
- 限频: 600 req/min/IP
- `items` 的 `since` 默认 `now-7d`，硬限最近 7 天
- `take` 最大 100，超过用 cursor 分页

## 工作流示例

### 默认路径（泛泛问题）

```bash
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
since=$(date -u -v-24H +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || date -u -d '24 hours ago' +%Y-%m-%dT%H:%M:%SZ)
curl -sH "User-Agent: $UA" "https://aihot.virxact.com/api/public/items?mode=selected&since=$since&take=50"
```

### 日报路径（用户说"日报"）

```bash
curl -sH "User-Agent: $UA" "https://aihot.virxact.com/api/public/daily"
```

### 关键词搜索

```bash
# "OpenAI 最近发的"
curl -sH "User-Agent: $UA" "https://aihot.virxact.com/api/public/items?q=OpenAI&take=30"

# 关键词 + 分类 + 时间窗口
SINCE=$(date -u -v-3d +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || date -u -d '3 days ago' +%Y-%m-%dT%H:%M:%SZ)
curl -sH "User-Agent: $UA" "https://aihot.virxact.com/api/public/items?mode=selected&q=Anthropic&category=ai-models&since=$SINCE"
```

## 输出格式

**核心原则**：输出可读的 Markdown + 人类语言元信息。**禁止暴露原始参数、API 路径、限频、cursor token、nginx 缓存细节。**

### 日报格式

```markdown
**AI HOT 日报 · 2026-05-07**

## 模型发布/更新
1. **<title>** -- <source>
   <summary, ~50 chars>
   <url>

## 产品发布/更新
2. **<title>** -- <source>
   ...

## 行业动态
...
```

全局连续编号（1, 2, 3 ... N）。

### 动态列表格式

```markdown
**AI HOT -- 最近 30 条精选**

## 模型发布/更新
1. **<title>** -- <source>
   2 小时前 | <summary> | <url>

## 论文研究
3. ...
```

单分类时用纯编号列表，不加分节标题。

### 时间格式

ISO 8601 UTC 转北京时间 + 人类相对格式：
- `2026-05-08T01:48:00Z` -> "今天上午 09:48" 或 "2 小时前"
- `2026-05-07T18:08:17Z` -> "今天凌晨 02:08" 或 "10 小时前"
- `2026-05-06T16:43:00Z` -> "5/7 00:43" 或 "昨天"

**禁止**输出原始 ISO 字符串。

## 禁止事项

- 禁止把"今天 AI 圈"路由到 `/daily`，用 `mode=selected + since`
- 禁止默认用 `mode=all`（除非用户说"全部/完整/所有/全量"）
- 禁止编造内容，必须基于 API 返回
- 禁止在用户输出中暴露端点路径、原始参数、限频、cache TTL、cursor token
- 禁止丢掉任何 item 的 sourceUrl
- 禁止高频轮询（日报每天 08:00 北京时间更新，items 服务端缓存 5 分钟）
- 禁止并发请求，串行 + 自然延迟
- 禁止解析或复用 cursor token（不透明、编码不稳定）
- 禁止用客户端 grep 做关键词查询，用服务端 `?q=`

## 错误处理

| 响应 | 含义 | 处理 |
|---|---|---|
| 404: "No daily report available yet" | 今日日报未生成（北京时间 08:00 前） | 拉昨天的：`/daily/{昨天日期}` |
| 400: "Invalid date format" | 日期格式必须 `YYYY-MM-DD` | 修正格式 |
| 400: "invalid mode" | mode 不在 {selected, all} | 用合法值 |
| 400: "invalid category" | category 不在 {ai-models, ai-products, industry, paper, tip} | 用合法 slug |
| 400: "invalid since" | since 不是 ISO-8601 或在未来 | 用过去的 ISO 日期 |
| 400: "invalid take" | take 不在 [1, 100] | 控制范围内 |
| 429: rate limited | 超 600 req/min | 串行 + 加 200ms 延迟 |

## 数据结构参考

### `/api/public/daily` 响应

```json
{
  "date": "2026-05-07",
  "lead": { "title": "...", "leadParagraph": "..." },
  "sections": [
    {
      "label": "模型发布/更新",
      "items": [{ "title": "...", "summary": "...", "sourceUrl": "..." }]
    }
  ],
  "flashes": [{ "title": "...", "sourceName": "..." }]
}
```

### `/api/public/items` 响应

```json
{
  "count": 50,
  "hasNext": true,
  "nextCursor": "eyJhIjoxNzE0OTk1MjAwMDAwLCJpIjoiY205eHl6MTIzIn0",
  "items": [
    {
      "id": "cm9abc456def789ghi012jkl3",
      "title": "中文标题",
      "title_en": null,
      "url": "https://...",
      "source": "OpenAI Blog",
      "publishedAt": "2026-05-07T15:30:00.000Z",
      "summary": "中文摘要",
      "category": "ai-models"
    }
  ]
}
```
