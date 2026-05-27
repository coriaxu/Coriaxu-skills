# course-companion-open

中文名：课程共学搭档

这是一个公开版 Agent Skill，用来陪用户学习一堂课。它不是普通课程总结工具，而是一条完整的共学流程：

1. 用 `three-level-notes` 生成课程骨架笔记
2. 按用户选择接入已有笔记
3. 找出 3-5 个强相关连接或课程内部锚点
4. 进入多轮深度对话
5. 生成最终研读笔记和可选知识卡片

## 适合谁

- 正在学在线课、音频课、讲稿、访谈课的终身学习者
- 有个人笔记库，希望把新课接入旧知识的人
- 没有笔记库，但希望 AI 陪自己把课聊透的人

## 依赖

必须安装或同时提供：

- `three-level-notes`

`course-companion-open` 会在 Phase 1 调用它生成骨架笔记。没有这个依赖时，默认不手写替代。

## 三种知识库模式

### 1. 无知识库模式

只基于课程内容学习。系统会提取 3-5 个课程内部锚点，不扫描旧笔记。

### 2. 指定文件夹模式

用户提供一个或多个笔记文件夹。系统只扫描这些文件夹，找出 3-5 个强相关文件。

### 3. Obsidian 模式

用户提供 Obsidian vault 根目录和要扫描的子目录。系统会理解 Markdown、frontmatter、tags、wikilinks 和笔记标题。

## 推荐文件结构

```text
course-companion-open/
├── SKILL.md
├── README.md
├── agents/
│   └── interface.yaml
├── references/
│   ├── config-template.md
│   ├── knowledge-modes.md
│   ├── output-formats.md
│   └── three-level-notes-contract.md
├── examples/
│   ├── sample-course-input.md
│   ├── sample-discussion-opening.md
│   └── sample-final-note.md
└── evals/
    └── evals.json
```

## 快速开始

把这句话发给支持 Agent Skills 的助手：

```text
Use $course-companion-open to study this lesson with me.
```

第一次使用时，它会问：

```text
这堂课要不要接入你已有笔记？选一个就行：不接入 / 扫描指定文件夹 / 接入 Obsidian 库。
```

更稳定的做法是在课程目录放一个 `course-companion.config.md`，模板见 `references/config-template.md`。

## 公开版边界

这个版本不包含任何私人路径、私人称呼、固定知识库结构或个人案例。用户需要自己配置笔记路径和输出位置。

## 建议迭代

- 增加安装脚本，把 `course-companion-open` 和 `three-level-notes` 一起复制到用户 skill 目录
- 增加文件扫描脚本，减少不同 Agent 对目录检索的表现差异
- 增加更多真实课程样例，用于测试 Phase 2 的对话质量
