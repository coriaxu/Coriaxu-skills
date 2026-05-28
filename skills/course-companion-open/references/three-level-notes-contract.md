# three-level-notes Contract

`course-companion-open` 的 Phase 1 必须使用 `three-level-notes` 生成课程骨架笔记。

## Required Behavior

当用户提供课程原文、讲稿、访谈稿、字幕稿或长篇课程材料时：

```text
Skill(skill="three-level-notes", args="<完整课程材料>")
```

不要自己手写一个简化大纲来替代。

## Required Output Shape

调用结果必须包含三段：

1. **Part 1: 认知拆解**
   - Dots
   - Lines
   - Ideas & Web
   - Iterations
2. **Part 2: 三级大纲笔记**
   - 模块标题
   - 核心论点
   - 支撑细节
3. **Part 3: 总结与洞察**
   - 核心结论
   - 下一步思考

## Dependency Missing

如果当前环境无法调用 `three-level-notes`：

1. 先说明缺少本仓库自带的 `三级笔记` skill；它的注册名是 `three-level-notes`。
2. 告诉用户如果是从 `Coriaxu-skills` 安装，不需要去外部下载，只需要同时安装 `course-companion-open` 和 `三级笔记`。
3. 只有用户明确同意临时继续，才生成 fallback 骨架。
4. fallback 输出必须标明：`当前为 fallback 骨架，未调用 three-level-notes`。

## Self-Check Before Phase 2

进入 Phase 2 前检查：

- 是否真的调用了 `three-level-notes`
- 是否拿到了三个 Part
- 是否能从 Dots 和 Lines 中提取搜索词
- 是否能把 Part 2 作为最终笔记骨架

任一项不满足，先处理 Phase 1 问题。
