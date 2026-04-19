# Skill Catalog · 技能清单

本仓库当前收录的所有 skill 一览。点击技能名称可以跳到对应目录查看 `SKILL.md`。

| 技能名称 | 触发词 | 一句话详细介绍 | 备注 |
|---------|--------|---------------|------|
| [**yao-meta-skill**](../skills/yao-meta-skill/) | create a skill、make this a skill、把这个流程做成 skill、package skill、improve existing skill、skill 评测 | 元技能工厂：把你日常重复的流程、零碎提示词、对话记录或笔记，系统化沉淀为带评测闭环、可复用、可交接的 agent skill。 | 姚金刚原创（MIT）· 核心哲学是"结构化设计 + 评测 + 打包"三合一 |
| [**nuwa-skill**](../skills/nuwa-skill/) | 蒸馏 XX、造一个 XX 的 skill、女娲、用 XX 的视角、distill X、nuwa、X's thinking framework | 女娲造人术：输入任意人物名，自动派多 agent 并行调研并提炼心智模型与表达 DNA，一键生成一个"像那个人一样思考"的视角 skill。 | 花叔原创（MIT）· 已集成 web-access 做深度联网调研 |
| [**三级笔记**](../skills/三级笔记/) | 提炼大纲、整理笔记、总结要点、拆解文章、三级笔记、深度解读、拆书 | 深度长文阅读教练：用阅读研究者 + 编辑的双重视角，把长文章或演讲稿拆成三级大纲，让你既能抓住作者观点也能看清他的思考路径。 | 小能熊老师原创 · 适合微信长文、演讲稿、论文等深度阅读 |
| [**darwin-skill**](../skills/darwin-skill/) | 优化 skill、skill 评分、自动优化、skill 质量检查、帮我改改 skill、skill review、skill 打分 | 达尔文 skill 自动优化器：按 8 维 rubric 评分 + 爬山算法 + git 版本控制，边改 SKILL.md 边跑测试，只保留变好的版本、变差自动回滚。 | 花叔原创 · 灵感来自 Andrej Karpathy autoresearch |

## 如何安装某一个 skill

最简单：[让你的 AI 助理帮你装](./ai-install-guide.md)，复制粘贴一段话给它即可。

命令行：

```bash
git clone https://github.com/coriaxu/Coriaxu-skills.git ~/Code/Coriaxu-skills
cd ~/Code/Coriaxu-skills
./install.sh yao-meta-skill   # 把 yao-meta-skill 换成你想装的
```

## 作者归属

表格中的所有第三方作者信息、协议说明、链接集中整理在 [CREDITS.md](../CREDITS.md)。

---

_最后更新：2026-04-19 · 本清单随仓库内容自动同步更新_
