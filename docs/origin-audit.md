# Origin Audit — Skill 开源前溯源表

**扫描时间**：2026-04-18
**扫描范围**：`/Users/surfin/.claude/skills/` 下候选开源的 ~40 个 skill
**扫描方式**：SKILL.md frontmatter + LICENSE 文件 + README.md 归属关键词
**更新记录**：2026-05-27 依据已确认上游仓库补全来源链接与许可信息。

## 溯源结果总览

- **徐老师原创**：约 20 个（2026-05-27 已将部分原误判条目改入第三方来源）
- **徐老师 AI 团队（小萌/若谷）署名**：2 个（flomo-processor、daily-review）
- **第三方原创（明确作者）**：yao-meta-skill = 姚金刚、nuwa-skill / darwin-skill = 花叔、三级笔记 = 小能熊老师、shuorenhua、web-access、claude-to-im、dbskill、obsidian-skills 等
- **第三方包装/致敬**：1 个（awesome-finance-skills 基于 RKiding）
- **已知第三方协议包含 MIT、CC BY-NC 4.0 或未声明**；徐老师原创内容仍可采用 MIT，但第三方目录需遵守各自 LICENSE
- **订正记录（2026-04-19）**：徐老师 confirm yao-meta-skill 作者是姚金刚（原 frontmatter 写 Yao Team），darwin-skill 作者是花叔，三级笔记作者是小能熊老师（之前三条都误判为徐浩原创）

## 详细明细

### 🟢 徐老师原创（可直接开源，标注 `Author: 徐浩`）

| skill | 证据 | 备注 |
|-------|------|------|
| skill-creator | 无外部归属 | 原创 |
| xray-book | 自有方法论 | 原创 |
| brand-design-md | 自有集成 | 原创 |
| elon-musk-perspective | 自建 80+ 信源研究 | 原创 |
| peter-senge-perspective | 自建 40+ 信源研究 | 原创 |
| html-screenshot | 原创脚本 | 原创 |
| google-workspace-gws | 原创 gws 集成 | 原创 |
| wechat-article-deep-reader | 原创方案 | 原创 |
| structured-context-compressor | 原创算法 | 原创 |
| reading-notes-splitter | 原创方案 | 原创 |
| pending-zone | 徐老师个人工作流 | 原创 |
| coriaxu-pending-zone | pending-zone 通用公开版 | 原创 |
| init-project-claude | 原创 | 原创 |
| init-memory-claude | 原创 | 原创 |
| skill-manager | 原创 | 原创 |
| design-system | 原创 | 原创 |

### 🟡 徐老师原创但需致敬启发源

| skill | 原创人 | 启发/致敬对象 | 处理方式 |
|-------|--------|---------------|---------|
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
| yao-meta-skill | 姚金刚 Yao Jingang（Yao Team） | MIT | `LICENSE:2 Copyright (c) 2026 Yao Team`（徐老师确认作者是姚金刚） | https://github.com/yaojingang/yao-meta-skill |
| nuwa-skill | 花叔 Huashu | MIT | `LICENSE:3 Copyright (c) 2026 Huashu (花叔)` | https://github.com/alchaincyf/nuwa-skill |
| darwin-skill | 花叔 Huashu | 待确认（仓内无 LICENSE，README 标 MIT） | 徐老师确认作者是花叔，扫描时误判为徐浩原创 | https://github.com/alchaincyf/darwin-skill |
| 三级笔记 | 小能熊老师 | 待确认（仓内无 LICENSE） | 徐老师确认作者是小能熊老师，扫描时误判为徐浩原创 | 待徐老师补链接 |
| agent-review | akira82-ai | MIT | `LICENSE:3 Copyright (c) 2026 akira82-ai` | 待补充 |
| career-skill-planner | 空格的键盘 | 待确认 | CREDITS 归属记录 | 待补充 |
| ljg-card / ljg-roundtable | 李继刚 Li Jigang | 待确认 | CREDITS 归属记录 | 待补充 |
| shuorenhua | MrGeDiao | MIT | `LICENSE:2 Copyright (c) 2026 MrGeDiao` | https://github.com/MrGeDiao/shuorenhua |
| web-access | 一泽 Eze | MIT | `SKILL.md` frontmatter: `license: MIT`, `github: https://github.com/eze-is/web-access` | https://github.com/eze-is/web-access |
| claude-to-im | op7418 | MIT | `LICENSE:3 Copyright (c) 2024-2025 op7418` | 独立 GitHub 仓（有 `.git` 目录） |
| aihot | 卡兹克 | MIT | 原始 skill 页面 https://aihot.virxact.com/aihot-skill/ | https://aihot.virxact.com/aihot-skill/ |
| dbs / dbs-content / dbs-diagnosis / dbskill-knowledge | dontbesilent | CC BY-NC 4.0 | 上游 `LICENSE` 标注 Attribution-NonCommercial 4.0 International | https://github.com/dontbesilent2025/dbskill |
| obsidian-markdown / obsidian-bases | kepano / Obsidian community | MIT | 上游 `LICENSE` | https://github.com/kepano/obsidian-skills |
| qiaomu-epub-book-generator | 乔木 / joeseesun | 待确认（上游仓内无 LICENSE） | 上游仓库公开发布 | https://github.com/joeseesun/qiaomu-epub-book-generator |

**特别处理**：`claude-to-im` 本身是独立开源项目，带 `.git` 目录。**不建议直接塞进 monorepo**（会形成 git 嵌套或丢失原 git 历史）。建议在 README 做「第三方 skill 推荐」章节，贴原仓链接引导用户自己 clone。

### ⚪ 扫描异常 / 不开源（本次跳过）

| skill | 原因 |
|-------|------|
| sophia / vera / reading-companion / save-memory-claude / okr-review / grace skill | 重度个人化，按 plan 不开源 |
| luiz | 徐老师决定不开源（2026-04-19） |

---

## 待徐老师 3 个确认

1. **仓库定位**：是要「只放徐老师自创 + CREDITS 链接推荐第三方」，还是「把第三方 skill 也打包进 monorepo（保留原作者信息致谢）」？
2. **flomo-processor / daily-review**：AI 团队署名（小萌 + 若谷）是否属实？保留还是改写？
3. **仍缺原仓链接的第三方 skill**：`agent-review`、`三级笔记`、`career-skill-planner`、`ljg-card`、`ljg-roundtable`。

---

## 协议结论

已确认第三方协议里包含 **MIT** 和 **CC BY-NC 4.0**，没有发现 GPL/AGPL 传染源。徐老师原创内容仍可采用 MIT；第三方目录按各自 LICENSE 分发。
