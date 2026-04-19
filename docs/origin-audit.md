# Origin Audit — Skill 开源前溯源表

**扫描时间**：2026-04-18
**扫描范围**：`/Users/surfin/.claude/skills/` 下候选开源的 ~40 个 skill
**扫描方式**：SKILL.md frontmatter + LICENSE 文件 + README.md 归属关键词

## 溯源结果总览

- **徐老师原创**：约 27 个
- **徐老师 AI 团队（小萌/若谷）署名**：2 个（flomo-processor、daily-review）
- **第三方原创（明确作者+MIT 协议）**：5 个（yao-meta-skill、nuwa-skill、shuorenhua、web-access、claude-to-im）
- **第三方包装/致敬**：2 个（awesome-finance-skills 基于 RKiding、darwin-skill 致敬 Karpathy）
- **所有第三方协议均为 MIT 或未声明**，徐老师仓库可安全采用 MIT

## 详细明细

### 🟢 徐老师原创（可直接开源，标注 `Author: 徐浩 / Surfin L&D`）

| skill | 证据 | 备注 |
|-------|------|------|
| 三级笔记 | 无外部归属 | 原创 |
| luiz | 无外部归属 | 原创 |
| ljg-card | 无外部归属 | 原创 |
| ljg-roundtable | 无外部归属 | 原创 |
| skill-creator | 无外部归属 | 原创 |
| xray-book | 自有方法论 | 原创 |
| brand-design-md | 自有集成 | 原创 |
| elon-musk-perspective | 自建 80+ 信源研究 | 原创 |
| peter-senge-perspective | 自建 40+ 信源研究 | 原创 |
| career-skill-planner | 原创框架 | 原创 |
| html-screenshot | 原创脚本 | 原创 |
| google-workspace-gws | 原创 gws 集成 | 原创 |
| qiaomu-epub-book-generator | 原创方案 | 原创 |
| wechat-article-deep-reader | 原创方案 | 原创 |
| structured-context-compressor | 原创算法 | 原创 |
| reading-notes-splitter | 原创方案 | 原创 |
| obsidian-markdown | 原创手册 | 原创 |
| obsidian-bases | 原创手册 | 原创 |
| pending-zone | 徐老师个人工作流 | 原创 |
| init-project-claude | 原创 | 原创 |
| init-memory-claude | 原创 | 原创 |
| agent-review | 原创 | 原创 |
| skill-manager | 原创 | 原创 |
| design-system | 原创 | 原创 |
| dbs / dbs-diagnosis / dbs-content / dbs-benchmark / dbs-hook / dbs-action / dbs-deconstruct | 原创 | 系列原创 |

### 🟡 徐老师原创但需致敬启发源

| skill | 原创人 | 启发/致敬对象 | 处理方式 |
|-------|--------|---------------|---------|
| darwin-skill | 徐老师 | Karpathy's autoresearch | SKILL.md 里已提 "Inspired by Karpathy's autoresearch"，开源时在 README 明确致敬 |
| awesome-finance-skills | 徐老师 | RKiding/Awesome-finance-skills | SKILL.md 已写 "基于 RKiding/Awesome-finance-skills 封装"，README 补原仓链接 |

### 🔵 徐老师 AI 团队（小萌 ChatGPT + 若谷 Gemini）署名

这两个 skill 的 SKILL.md frontmatter 写的是 `author: Xiaomeng (ChatGPT) & Ruogu (Gemini)`。从上下文判断是徐老师引导下他的 AI 团队协作产出的。

| skill | 作者字段 | 处理建议 |
|-------|---------|---------|
| flomo-processor | Xiaomeng (ChatGPT) & Ruogu (Gemini) | 保留原署名，README 注明「徐浩 AI Team 协作产出」 |
| daily-review | Xiaomeng (ChatGPT) & Ruogu (Gemini) | 同上 |

**待徐老师确认**：这两个是不是的确由小萌和若谷写的（你引导），若是，保留 AI 署名作为一种透明的创作记录。

### 🔴 第三方原创（保留 LICENSE + CREDITS 致谢）

| skill | 原作者 | 协议 | 证据 | 原仓/联系方式 |
|-------|--------|------|------|---------------|
| yao-meta-skill | Yao Team | MIT | `LICENSE:2 Copyright (c) 2026 Yao Team` | 待徐老师补链接 |
| nuwa-skill | 花叔 Huashu | MIT | `LICENSE:2 Copyright (c) 2026 Huashu (花叔)` | 待徐老师补链接 |
| shuorenhua | MrGeDiao | MIT | `LICENSE:2 Copyright (c) 2026 MrGeDiao` | 待徐老师补链接 |
| web-access | 一泽 Eze | MIT | `SKILL.md:560 author: 一泽Eze` | 待徐老师补链接 |
| claude-to-im | op7418 | MIT | `LICENSE:3 Copyright (c) 2024-2025 op7418` | 独立 GitHub 仓（有 `.git` 目录） |

**特别处理**：`claude-to-im` 本身是独立开源项目，带 `.git` 目录。**不建议直接塞进 monorepo**（会形成 git 嵌套或丢失原 git 历史）。建议在 README 做「第三方 skill 推荐」章节，贴原仓链接引导用户自己 clone。

### ⚪ 扫描异常 / 不开源（本次跳过）

| skill | 原因 |
|-------|------|
| sophia / vera / reading-companion / save-memory-claude / okr-review / grace skill / dbskill-knowledge | 重度个人化，按 plan 不开源 |

---

## 待徐老师 3 个确认

1. **仓库定位**：是要「只放徐老师自创 + CREDITS 链接推荐第三方」，还是「把第三方 skill 也打包进 monorepo（保留原作者信息致谢）」？
2. **flomo-processor / daily-review**：AI 团队署名（小萌 + 若谷）是否属实？保留还是改写？
3. **5 个第三方 skill 的原仓链接**：徐老师记得自己从哪下载的吗？比如花叔的 nuwa-skill 具体在哪个 GitHub 地址，方便发致谢 PR。

---

## 协议结论

所有已扫描第三方 skill 的 LICENSE 都是 **MIT**，没有 GPL/AGPL 传染源。徐老师仓库整体可采用 **MIT 协议**，兼容所有第三方收录。
