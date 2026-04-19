# Skill Catalog · 技能清单

本仓库当前收录的所有 skill 一览，按能力类型分四大类。技能名可点击跳到对应目录查看 `SKILL.md`。

---

## 🧬 元技能类（Meta-Skills）

用来**创造、管理、进化 skill 本身**的 skill。

| 技能名称 | 触发词 | 一句话详细介绍 | 备注 |
|---------|--------|---------------|------|
| [**yao-meta-skill**](../skills/yao-meta-skill/) | create a skill、make this a skill、把这个流程做成 skill、package skill、improve existing skill | 元技能工厂：把你日常重复的流程、零碎提示词、对话记录或笔记，系统化沉淀为带评测闭环、可复用、可交接的 agent skill。 | 姚金刚原创（MIT） |
| [**nuwa-skill**](../skills/nuwa-skill/) | 蒸馏 XX、造一个 XX 的 skill、女娲、用 XX 的视角、distill X | 女娲造人术：输入任意人物名，自动派多 agent 并行调研并提炼心智模型与表达 DNA，一键生成一个"像那个人一样思考"的视角 skill。 | 花叔原创（MIT） |
| [**darwin-skill**](../skills/darwin-skill/) | 优化 skill、skill 评分、自动优化、skill 质量检查、帮我改改 skill、skill review | 达尔文 skill 自动优化器：按 8 维 rubric 评分 + 爬山算法 + git 版本控制，边改 SKILL.md 边跑测试，只保留变好的版本、变差自动回滚。 | 花叔原创（灵感来自 Karpathy autoresearch） |
| [**career-skill-planner**](../skills/career-skill-planner/) | 帮我规划 XX 职业的 Skill、我是 XX 帮我拆 Skill、XX 职业需要哪些 Skill | 职业 Skill 规划器：输入职业名，输出该职业的核心工作流分解，以及每个工作流对应的 Skill 制作指南（提示词 + 实现逻辑）。 | 空格的键盘原创 |
| [**agent-review**](../skills/agent-review/) | 复盘、agent review、/复盘、/agent-review | 每日复盘：根据 Claude Code 本地对话记录，生成结构化的每日工作复盘报告。支持当天、昨天、近 3 天、近 7 天。 | akira82-ai 原创（MIT） |

---

## 🧠 思维教练类（Thinking Coaches）

用特定思想家的视角、或结构化框架**深度思考某个议题**的 skill。

| 技能名称 | 触发词 | 一句话详细介绍 | 备注 |
|---------|--------|---------------|------|
| [**elon-musk-perspective**](../skills/elon-musk-perspective/) | 用 Musk 的视角、Musk perspective、像 Musk 一样思考 | 像 Elon Musk 一样思考：应用他的思维模型（第一性原理、The Algorithm、级联策略）、决策启发式和沟通风格，分析问题、评估策略、挑战假设。 | 基于 nuwa-skill 自建（80+ 一手信源） |
| [**peter-senge-perspective**](../skills/peter-senge-perspective/) | 用圣吉的视角、圣吉会怎么看、第五项修炼视角、系统思考 | 像彼得·圣吉一样思考：基于 40+ 一手来源提炼的 5 个核心心智模型和 8 条决策启发式，分析组织问题、审视变革策略、诊断学习障碍。 | 基于 nuwa-skill 自建（40+ 一手信源） |
| [**ljg-roundtable**](../skills/ljg-roundtable/) | 圆桌讨论、圆桌、roundtable、辩论、多视角辩证 | 结构化圆桌讨论器：围绕一个议题邀请 3-5 位真实历史或当代人物展开多轮辩证讨论，由主持人持续提炼核心争议、生成 ASCII 思考框架图。 | 李继刚原创 |
| [**dbs**](../skills/dbs/) | /dbs、/商业、帮我看看 | dontbesilent 商业工具箱主入口：根据你的问题自动路由到最合适的诊断 skill（问诊 / 体检 / 内容 / 对标 / 概念拆解）。 | dontbesilent 原创 |
| [**dbs-diagnosis**](../skills/dbs-diagnosis/) | /dbs-diagnosis、/问诊、帮我看看商业模式、诊断一下我的业务 | dontbesilent 商业模式诊断：两种模式，问诊（消解问题）和体检（拆解商业模式），用本体论框架给业务做全身检查。 | dontbesilent 原创 |
| [**dbs-content**](../skills/dbs-content/) | /dbs-content、/内容诊断、这个内容怎么做、帮我看看这个文案 | dontbesilent 内容创作诊断：选题通过后，五维检测内容质量，诊断怎么把这个选题做成好内容。 | dontbesilent 原创 |
| [**dbskill-knowledge**](../skills/dbskill-knowledge/) | 无独立触发，搭配 dbs 系列使用 | dontbesilent 商业工具箱共享知识包：高频概念词典 + 原子库，供 dbs 系列 skill 查询。 | dontbesilent 原创 |

---

## 🛠 通用工具类（Everyday Tools）

各类**日常工作流工具**，笔记处理、内容制作、截图、打包、拆书、深度阅读等。

| 技能名称 | 触发词 | 一句话详细介绍 | 备注 |
|---------|--------|---------------|------|
| [**三级笔记**](../skills/三级笔记/) | 提炼大纲、整理笔记、总结要点、拆解文章、三级笔记、深度解读、拆书 | 深度长文阅读教练：用阅读研究者 + 编辑的双重视角，把长文章、演讲稿、论文拆成三级大纲，让你既能抓住作者观点也能看清他的思考路径。 | 小能熊老师原创 |
| [**ljg-card**](../skills/ljg-card/) | 铸、cast、做成图、做成卡片、做成信息图、视觉笔记、sketchnote、漫画、白板 | 内容铸造器 · Content Caster：把内容铸成 PNG 视觉图片，六种模具（长卡 `-l`、信息图 `-i`、多卡 `-m`、视觉笔记 `-v`、漫画 `-c`、白板 `-w`）。 | 李继刚原创 |
| [**qiaomu-epub-book-generator**](../skills/qiaomu-epub-book-generator/) | 生成 EPUB、制作电子书、Markdown 转 EPUB、博客文章做成电子书 | EPUB 电子书生成器：博客文章、Markdown 文档、AI 搜索资料转 EPUB，支持图片下载 + 代码块渲染 + 专业封面，兼容微信读书和 Apple Books。 | 乔木原创 |
| [**shuorenhua**](../skills/shuorenhua/) | 说人话、去 AI 味、自然一点、别像模板、别太像 ChatGPT | 清理中英文文本里的 AI 套路：保留事实和术语，按 chat / status / docs / public-writing 四种场景控制改写力度。 | MrGeDiao 原创（MIT） |
| [**reading-notes-splitter**](../skills/reading-notes-splitter/) | 读书笔记、flomo、HTML 转 MD、拆分卡片、笔记整理 | 把 flomo 等 HTML 格式的读书笔记转换为结构化 Markdown 卡片：自动拆分每条笔记，区分标题、个人想法和原书摘要。 | 徐浩原创 |
| [**wechat-article-deep-reader**](../skills/wechat-article-deep-reader/) | 微信文章链接（mp.weixin.qq.com）+ 提炼大纲 / 整理笔记 / 三级笔记 | 稳定抓取微信公众号文章并输出"主旨 - 论证 - 细节"三级阅读笔记，适合微信长文的深度结构化阅读。 | 徐浩原创 |
| [**html-screenshot**](../skills/html-screenshot/) | 截图、网页截图、HTML 转图片、截成图片 | 本地 HTML 文件截图为竖版 PNG 图片，支持单文件和批量，用 Chrome 无头模式 2x 视网膜清晰度。 | 徐浩原创 |
| [**brand-design-md**](../skills/brand-design-md/) | XX 风格、做成 XX 的感觉、参考 XX 设计 | 根据品牌名称从 `getdesign.md` 自动获取设计规范并生成匹配风格的 UI 代码，支持 62 个顶级品牌（Apple、Notion、Claude、Stripe 等）。 | 徐浩原创 |
| [**设计系统**](../skills/设计系统/) | 生成前端界面、创建 UI 组件、设计落地页、构建仪表板、制作 Web 应用 | 结构化 UI/UX 设计知识库：让 AI 生成的界面代码从"能用但丑"升级为"专业美观"，覆盖风格选择、配色、字体配对、图表选型。 | 徐浩原创 |
| [**structured-context-compressor**](../skills/structured-context-compressor/) | 压缩上下文、交接摘要、9 段摘要、CC Context Compressor | 长对话续接、切上下文或交接给其他 Agent 时，将当前进展压成 9 段结构化摘要，重点保住用户原话、关键文件、错误、待办和下一步。 | 徐浩原创 |
| [**init-project-claude**](../skills/init-project-claude/) | /init-project、新项目、初始化项目 | 初始化新项目并创建带场景路由的记忆文件（task_plan / findings / scratchpad / decisions / memory_map）。 | 徐浩原创 |
| [**init-memory-claude**](../skills/init-memory-claude/) | /init-memory、初始化记忆、唤醒记忆 | 为当前项目初始化或读取记忆文件，按场景路由生成可直接开工的启动简报。 | 徐浩原创 |

---

## 🔌 集成工具类（Integrations）

连接**外部应用 / 平台**的桥接 skill。

| 技能名称 | 触发词 | 一句话详细介绍 | 备注 |
|---------|--------|---------------|------|
| [**obsidian-markdown**](../skills/obsidian-markdown/) | 处理 Obsidian 笔记、wikilinks、callouts、frontmatter | 创建和编辑 Obsidian 风格的 Markdown：wikilinks、embeds、callouts、properties/frontmatter、tags 等 Obsidian 特有语法。 | Obsidian 原创 |
| [**obsidian-bases**](../skills/obsidian-bases/) | 创建数据库视图、表格视图、卡片视图、`.base` 文件 | 创建和编辑 Obsidian Bases（`.base` 文件）：视图、过滤器、公式、汇总等数据库式笔记组织能力。 | Obsidian 原创 |
| [**web-access**](../skills/web-access/) | 搜索信息、查看网页、抓取社交媒体、读取动态渲染页面 | 联网操作总控：自动选择 WebSearch / WebFetch / curl / Jina / CDP 浏览器，支持登录态操作、动态页面、视频采帧、并行子 Agent 分治调研。 | 一泽 Eze 原创（MIT） |

---

## 📦 如何安装

最简单：[让你的 AI 助理帮你装](./ai-install-guide.md)，复制粘贴一段话给它就行。

命令行：

```bash
git clone https://github.com/coriaxu/Coriaxu-skills.git ~/Code/Coriaxu-skills
cd ~/Code/Coriaxu-skills
./install.sh yao-meta-skill            # 装一个
./install.sh yao-meta-skill nuwa-skill # 装多个
./install.sh                           # 装全部
./install.sh --list                    # 看可选
```

## 📚 更多

- 所有第三方作者致谢：[CREDITS.md](../CREDITS.md)
- 归属扫描历史：[origin-audit.md](./origin-audit.md)
- 仓库整体介绍：[README.md](../README.md)

---

_最后更新：2026-04-19 · 本清单随仓库内容同步更新_
