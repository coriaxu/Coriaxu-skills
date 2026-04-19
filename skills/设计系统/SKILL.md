---
name: ui-design-system
description: 结构化的UI/UX设计知识库，让AI生成的界面代码从"能用但丑"升级为"专业美观"。当需要生成前端界面、创建UI组件、设计落地页、构建仪表板、制作Web应用时触发。覆盖风格选择、行业配色、字体配对、图表选型、UX最佳实践，支持React/Vue/Next.js/Tailwind/SwiftUI/Flutter等技术栈。
---

# UI Design System

将设计决策从"凭感觉"变成"有依据"。

## 核心理念

AI写代码很强，但审美往往灾难。问题不在模型能力，而在缺乏结构化的设计知识。这个skill提供专业设计师的集体智慧，让AI能做出明智的设计决策。

## 工作流程

生成UI代码前，按需查阅以下知识库：

1. **确定风格** → 查阅 [references/styles.md](references/styles.md)
   - 产品类型适合什么风格？
   - 风格的视觉特征、适用场景、性能影响、可访问性

2. **选择配色** → 查阅 [references/colors.md](references/colors.md)
   - 行业专属配色方案（含十六进制色值）
   - 主色/辅色/强调色的搭配逻辑

3. **搭配字体** → 查阅 [references/typography.md](references/typography.md)
   - 标题/正文字体配对
   - Google Fonts导入方式
   - Tailwind配置示例

4. **图表选型** → 查阅 [references/charts.md](references/charts.md)
   - 数据类型匹配图表类型
   - 交互需求与可访问性
   - 推荐图表库

5. **UX检查** → 查阅 [references/ux-guidelines.md](references/ux-guidelines.md)
   - 动画/加载状态/错误处理
   - 可访问性检查清单
   - Do & Don't代码示例

6. **技术实现** → 查阅 [references/tech-stacks.md](references/tech-stacks.md)
   - 各框架的设计最佳实践
   - 组件库选择与配置

## 决策原则

- **风格服从产品**：先问"这是什么产品、给谁用"，再选风格
- **配色传递信任**：金融用稳重色调，医疗用柔和色调，科技用现代色调
- **字体创造层次**：标题醒目，正文易读，两者形成对比
- **可访问性优先**：对比度至少4.5:1，支持键盘导航，提供替代文本
- **性能不可牺牲**：backdrop-filter谨慎使用，动画适度，图片优化

## 快速示例

**请求**："做一个医疗美容SPA的落地页"

**设计决策链**：
- 风格 → 玻璃态（现代、精致、高端感）
- 配色 → 美容行业方案（柔和粉色/米色/金色点缀）
- 字体 → Playfair Display + Lato（优雅标题 + 清晰正文）
- 结构 → Hero区块 + 服务卡片 + 社会证明 + CTA
- 动画 → 平滑hover过渡，subtle入场动画
