# 设计技能完整目录

共 **163 项**：**77 项附带正文**、**41 项仅简介**、**45 项仅外链**。其中 **3 项完成当前会话显式读取试用**；其余未运行验证。自动发现与跨平台执行另行验证。

按任务浏览：[场景导航](docs/scenarios.md) · [状态解释与限制](docs/compatibility.md) · [静态核查](docs/audit/asset-audit.md)

> 此文件由 registry.json 生成。附带正文不代表资源完全齐备、能独立运行或已验证许可。依赖列继承原目录；“待确认”不是免费或无依赖。

- [原型与网页](#prototype)
- [设计系统与创意方向](#design-system)
- [图像](#image)
- [视频](#video)
- [演示文稿](#deck)
- [模板](#template)
- [工具](#utility)
- [音频](#audio)
- [品牌设计](#design)

<a id="prototype"></a>
## 原型与网页（53）

### 工程与验证

| 技能 | 用途 | 包内内容 | 静态检查 | 服务依赖（原目录） | 许可声明 | 运行记录 |
|---|---|---|---|---|---|---|
| [浏览器自动化 · `agent-browser`](skills/prototype/agent-browser/SKILL.md) | 面向 AI agent 的浏览器自动化 CLI：导航、填表、点击、截图、抓取页面数据和测试 | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | 未测试 |
| [完整输出 · `output-skill`](skills/prototype/output-skill/SKILL.md) | 覆盖 LLM 截断习惯，强制完整生成代码、禁止占位符，并妥善处理超长分段 | 附带正文 | 未检出缺失* | 待确认 | MIT | 未测试 |
### 文章文档

| 技能 | 用途 | 包内内容 | 静态检查 | 服务依赖（原目录） | 许可声明 | 运行记录 |
|---|---|---|---|---|---|---|
| [杂志文章 · `article-magazine`](skills/prototype/article-magazine/SKILL.md) | 把 Markdown 或笔记排成精致长文 HTML 的杂志式文章版式 | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | 未测试 |
| [Word 文档（OpenAI） · `doc`](https://github.com/openai/skills) | 通过 OpenAI 文档技能读取、创建和编辑 .docx，保持格式与版式 | 仅外链 | 不适用 | 待确认 | unknown | 未测试 |
| [Kami 羊皮纸文档 · `doc-kami-parchment`](skills/prototype/doc-kami-parchment/SKILL.md) | 暖色羊皮纸底、墨蓝强调色、单一衬线字体的编辑级文档排版 | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | 未测试 |
| [Word 文档（Anthropic） · `docx`](https://github.com/anthropics/skills/tree/main/skills/docx) | 创建、编辑、分析 Word 文档，支持修订、批注和格式 | 仅外链 | 不适用 | 待确认 | Proprietary (© Anthropic, all rights reserved) | 未测试 |
| [MiniMax DOCX · `minimax-docx`](skills/prototype/minimax-docx/SKILL.md) | 用 OpenXML SDK 专业创建和编辑 DOCX，适合品牌报告与模板化写作 | 仅简介 | 非完整技能 | 待确认 | MIT | 未测试 |
| [MiniMax PDF · `minimax-pdf`](skills/prototype/minimax-pdf/SKILL.md) | 用 token 化设计系统和 15 种封面样式生成、填写、重排 PDF | 仅简介 | 非完整技能 | 待确认 | MIT | 未测试 |
| [PDF 处理（Anthropic） · `pdf`](https://github.com/anthropics/skills/tree/main/skills/pdf) | 提取文本、创建 PDF 和处理表单 | 仅外链 | 不适用 | 待确认 | Proprietary (© Anthropic, all rights reserved) | 未测试 |
| [发布说明单页 · `release-notes-one-pager`](skills/prototype/release-notes-one-pager/SKILL.md) | 发布说明单页 HTML：亮点、新增、修复、破坏性变更、已知问题和升级说明 | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | 未测试 |
| [极简简历 · `resume-modern`](skills/prototype/resume-modern/SKILL.md) | 现代极简单页 A4 简历，可直接打印或导出 PDF | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | [显式试用](docs/validation-results.md) |
| [写作规范审查 · `writing-guidelines`](skills/prototype/writing-guidelines/SKILL.md) | 按 Vercel 写作规范审查文档/文案的语气、风格与用词 | 附带正文 | 未检出缺失* | 待确认 | MIT | 未测试 |
### 网页和组件

| 技能 | 用途 | 包内内容 | 静态检查 | 服务依赖（原目录） | 许可声明 | 运行记录 |
|---|---|---|---|---|---|---|
| [Artifact 构建套件 · `artifacts-builder`](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/artifacts-builder) | 用 React、Tailwind、shadcn/ui 构建多组件的复杂 claude.ai HTML artifact | 仅外链 | 不适用 | 待确认 | unknown | 未测试 |
| [FAQ 页面 · `faq-page`](skills/prototype/faq-page/SKILL.md) | 生成带折叠手风琴、搜索和分类筛选的常见问题/帮助中心页面 | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | [显式试用](docs/validation-results.md) |
| [高质量前端界面 · `frontend-design`](skills/prototype/frontend-design/SKILL.md) | 生成有鲜明视觉方向、精致排版与布局的生产级前端界面（HTML/CSS/JS 或框架代码） | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | 未测试 |
| [全栈前端开发 · `frontend-dev`](skills/prototype/frontend-dev/SKILL.md) | 带电影感动效、MiniMax API 生成素材和生成艺术的前端开发，适合 Hero 页和展示站 | 仅简介 | 非完整技能 | MiniMax API | MIT | 未测试 |
| [登录流程 · `login-flow`](skills/prototype/login-flow/SKILL.md) | 移动端登录与身份验证流程界面 | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | 未测试 |
| [Web Artifact 构建器 · `web-artifacts-builder`](skills/prototype/web-artifacts-builder/SKILL.md) | Anthropic 参考流程：用 React + Tailwind 构建可嵌入的复杂 HTML artifact | 仅简介 | 非完整技能 | 待确认 | Apache-2.0 | 未测试 |
### 设计风格

| 技能 | 用途 | 包内内容 | 静态检查 | 服务依赖（原目录） | 许可声明 | 运行记录 |
|---|---|---|---|---|---|---|
| [野兽派风格 · `brutalist-skill`](skills/prototype/brutalist-skill/SKILL.md) | 瑞士印刷排版融合军用终端美学的粗野主义界面，适合数据密集仪表盘 | 附带正文 | 未检出缺失* | 待确认 | MIT | 未测试 |
| [Emil 设计工程 · `emil-design-eng`](skills/prototype/emil-design-eng/SKILL.md) | Emil Kowalski 的 UI 打磨、组件设计与动画决策理念 | 附带正文 | 未检出缺失* | 待确认 | MIT | 未测试 |
| [GPT 品味 + GSAP 动效 · `gpt-tasteskill`](skills/prototype/gpt-tasteskill/SKILL.md) | 强制布局随机化、AIDA 页面结构、宽幅编辑排版与高级 GSAP 动效的 UI 设计规范 | 附带正文 | 未检出缺失* | 待确认 | MIT | 未测试 |
| [Impeccable 设计打磨 · `impeccable-design-polish`](skills/prototype/impeccable-design-polish/SKILL.md) | 在页面完成后做审计、点评、打磨、加动效与加固，准备上线 | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | 未测试 |
| [极简编辑风 · `minimalist-skill`](skills/prototype/minimalist-skill/SKILL.md) | 暖色单色、排版对比、扁平 Bento 网格和柔和色的极简编辑风界面，无渐变无重阴影 | 附带正文 | 未检出缺失* | 待确认 | MIT | 未测试 |
| [高端代理商风格 · `soft-skill`](skills/prototype/soft-skill/SKILL.md) | 规定字体、间距、阴影、卡片和动画细节，让网站有高端设计公司质感，屏蔽廉价默认样式 | 附带正文 | 未检出缺失* | 待确认 | MIT | 未测试 |
| [品味前端（反模板） · `taste-skill`](skills/prototype/taste-skill/SKILL.md) | 反 AI 模板化的前端技能：读需求推断设计方向，产出落地页/作品集/改版且不显得套模板 | 附带正文 | 未检出缺失* | 待确认 | MIT | 未测试 |
| [品味前端 v1 · `taste-skill-v1`](skills/prototype/taste-skill-v1/SKILL.md) | 原版 v1 taste-skill，为依赖其确切行为的项目保留 | 附带正文 | 未检出缺失* | 待确认 | MIT | 未测试 |
### 社交卡片

| 技能 | 用途 | 包内内容 | 静态检查 | 服务依赖（原目录） | 许可声明 | 运行记录 |
|---|---|---|---|---|---|---|
| [Twitter 分享卡 · `card-twitter`](skills/prototype/card-twitter/SKILL.md) | 配合推文使用的 Twitter 引用/数据卡片 | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | 未测试 |
| [小红书图文卡片 · `card-xiaohongshu`](skills/prototype/card-xiaohongshu/SKILL.md) | 小红书风格知识卡片，可左右滑动的多图轮播 | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | 未测试 |
| [营销海报 · `poster-hero`](skills/prototype/poster-hero/SKILL.md) | 竖版营销海报或朋友圈分享图，视觉冲击力强 | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | 未测试 |
| [Reddit 帖子卡 · `social-reddit-card`](skills/prototype/social-reddit-card/SKILL.md) | 逼真的 Reddit 帖子卡片，带投票栏和评论数 | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | 未测试 |
| [Spotify 正在播放卡 · `social-spotify-card`](skills/prototype/social-spotify-card/SKILL.md) | Spotify「正在播放」风格卡片，含专辑封面、进度条和播放控件 | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | 未测试 |
| [X (Twitter) 帖子卡 · `social-x-post-card`](skills/prototype/social-x-post-card/SKILL.md) | 逼真的 X 帖子卡片，含点赞/转发/浏览数据，适合视频叠加或分享图 | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | 未测试 |
### 数据图表

| 技能 | 用途 | 包内内容 | 静态检查 | 服务依赖（原目录） | 许可声明 | 运行记录 |
|---|---|---|---|---|---|---|
| [D3 数据可视化 · `d3-visualization`](skills/prototype/d3-visualization/SKILL.md) | 用 D3.js 生成各类图表和交互式数据可视化 | 仅简介 | 非完整技能 | 待确认 | MIT | 未测试 |
| [数据可视化报告 · `data-report`](skills/prototype/data-report/SKILL.md) | 把 CSV/Excel/JSON 数据变成精致的可视化报告页 | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | 未测试 |
| [手绘风图表 · `hand-drawn-diagrams`](skills/prototype/hand-drawn-diagrams/SKILL.md) | 根据提示生成手绘风 Excalidraw 图表：动画 SVG、在线编辑链接和 PNG 导出 | 仅简介 | 非完整技能 | 待确认 | MIT | 未测试 |
| [研究决策室 · `research-decision-room`](skills/prototype/research-decision-room/SKILL.md) | 把零散用户研究、访谈、工单、问卷整理成带证据台账、主题图和置信度的决策 HTML | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | 未测试 |
### 3D和动效

| 技能 | 用途 | 包内内容 | 静态检查 | 服务依赖（原目录） | 许可声明 | 运行记录 |
|---|---|---|---|---|---|---|
| [Emil 动效 · `emilkowalski-motion`](https://emilkowal.ski/skill) | 在界面完成后添加克制的微交互、状态过渡和页面动效 | 仅外链 | 不适用 | 待确认 | unknown | 未测试 |
| [Flutter 动画 · `flutter-animating-apps`](skills/prototype/flutter-animating-apps/SKILL.md) | 在 Flutter 应用中实现动画效果、过渡和动效 | 仅简介 | 非完整技能 | 待确认 | BSD-3-Clause | 未测试 |
| [GSAP 核心 · `gsap-core`](skills/prototype/gsap-core/SKILL.md) | GSAP 官方核心 API：to/from/fromTo、缓动、stagger、matchMedia 与减少动效 | 附带正文 | 未检出缺失* | 待确认 | MIT | 未测试 |
| [GSAP 框架集成 · `gsap-frameworks`](skills/prototype/gsap-frameworks/SKILL.md) | GSAP 在 Vue/Nuxt/Svelte 等非 React 框架中的生命周期、作用域和卸载清理 | 附带正文 | 未检出缺失* | 待确认 | MIT | 未测试 |
| [GSAP 性能 · `gsap-performance`](skills/prototype/gsap-performance/SKILL.md) | GSAP 动画性能优化：优先 transform、避免布局抖动、will-change、批处理 | 附带正文 | 未检出缺失* | 待确认 | MIT | 未测试 |
| [GSAP 插件 · `gsap-plugins`](skills/prototype/gsap-plugins/SKILL.md) | GSAP 插件用法：ScrollTo、ScrollSmoother、Flip、Draggable、SplitText、SVG 与物理插件等 | 附带正文 | 未检出缺失* | 待确认 | MIT | 未测试 |
| [GSAP + React · `gsap-react`](skills/prototype/gsap-react/SKILL.md) | GSAP 在 React/Next.js 中的用法：useGSAP、refs、gsap.context 与清理 | 附带正文 | 未检出缺失* | 待确认 | MIT | 未测试 |
| [GSAP 滚动触发 · `gsap-scrolltrigger`](skills/prototype/gsap-scrolltrigger/SKILL.md) | ScrollTrigger 滚动联动动画：固定、scrub、视差与触发器 | 附带正文 | 未检出缺失* | 待确认 | MIT | 未测试 |
| [GSAP 时间轴 · `gsap-timeline`](skills/prototype/gsap-timeline/SKILL.md) | GSAP 时间轴编排：position 参数、嵌套与播放控制 | 附带正文 | 未检出缺失* | 待确认 | MIT | 未测试 |
| [GSAP 工具函数 · `gsap-utils`](skills/prototype/gsap-utils/SKILL.md) | gsap.utils 工具：clamp、mapRange、interpolate、random、snap、wrap、pipe 等 | 附带正文 | 未检出缺失* | 待确认 | MIT | 未测试 |
| [动效评审 · `review-animations`](skills/prototype/review-animations/SKILL.md) | 按 Emil Kowalski 的高标准评审动画/动效代码，默认挑问题 | 附带正文 | 未检出缺失* | 待确认 | MIT | 未测试 |
| [GLSL 着色器 · `shader-dev`](skills/prototype/shader-dev/SKILL.md) | 光线步进、流体模拟、粒子系统和程序化生成等 GLSL 着色器技术 | 仅简介 | 非完整技能 | 待确认 | MIT | 未测试 |
| [Three.js 3D · `threejs`](https://github.com/CloudAI-X/threejs-skills) | 用 Three.js 在浏览器中构建 3D 场景、材质、控制与后期处理 | 仅外链 | 不适用 | 待确认 | unknown | 未测试 |
### 网站复刻

| 技能 | 用途 | 包内内容 | 静态检查 | 服务依赖（原目录） | 许可声明 | 运行记录 |
|---|---|---|---|---|---|---|
| [设计图转代码 · `image-to-code-skill`](skills/prototype/image-to-code-skill/SKILL.md) | 先自行生成网页设计图并深度分析，再按图高保真实现为前端代码 | 附带正文 | 未检出缺失* | 待确认 | MIT | 未测试 |
| [网站高级感改版 · `redesign-skill`](skills/prototype/redesign-skill/SKILL.md) | 审计现有网站/应用设计，识别 AI 模板化痕迹，在不破坏功能的前提下升级到高端设计标准 | 附带正文 | 未检出缺失* | 待确认 | MIT | 未测试 |
| [网站复刻 · `web-clone`](skills/prototype/web-clone/SKILL.md) | 复刻/克隆网站的方法论：先拿真源码→判路径→逆向拆解→搭工程→替换内容，覆盖静态站、React/Vue/Next 及 WebGL/Canvas 交互效果 | 附带正文 | 未检出缺失* | 待确认 | MIT | 未测试 |
### 产品展示

| 技能 | 用途 | 包内内容 | 静态检查 | 服务依赖（原目录） | 许可声明 | 运行记录 |
|---|---|---|---|---|---|---|
| [iPhone × MacBook 立体展架 · `mockup-device-3d`](skills/prototype/mockup-device-3d/SKILL.md) | iPhone 与 MacBook 立体展示，屏幕内嵌真实 HTML，带玻璃折射与 360° 转台构图 | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | 未测试 |

<a id="design-system"></a>
## 设计系统与创意方向（36）

### 营销与文案

| 技能 | 用途 | 包内内容 | 静态检查 | 服务依赖（原目录） | 许可声明 | 运行记录 |
|---|---|---|---|---|---|---|
| [广告创意 · `ad-creative`](skills/design-system/ad-creative/SKILL.md) | 生成并迭代广告标题、描述和正文，适合付费社交和搜索广告 | 仅简介 | 非完整技能 | 待确认 | MIT | 未测试 |
| [竞品广告分析 · `competitive-ads-extractor`](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/competitive-ads-extractor) | 从广告库提取并分析竞品广告的信息与创意策略 | 仅外链 | 不适用 | 待确认 | unknown | 未测试 |
| [营销文案 · `copywriting`](skills/design-system/copywriting/SKILL.md) | 撰写/改写落地页、首页和广告的营销文案 | 仅简介 | 非完整技能 | 待确认 | MIT | 未测试 |
| [域名头脑风暴 · `domain-name-brainstormer`](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/domain-name-brainstormer) | 生成创意域名并检查 .com/.io/.dev/.ai 等后缀可用性 | 仅外链 | 不适用 | 待确认 | unknown | 未测试 |
| [营销心理学 · `marketing-psychology`](skills/design-system/marketing-psychology/SKILL.md) | 把心理学和行为科学原理用于文案与设计（钩子、框架、定价呈现） | 仅简介 | 非完整技能 | 待确认 | MIT | 未测试 |
| [付费墙转化优化 · `paywall-upgrade-cro`](skills/design-system/paywall-upgrade-cro/SKILL.md) | 设计并优化升级页、付费墙和追加销售弹窗 | 仅简介 | 非完整技能 | 待确认 | MIT | 未测试 |
### 平台与设计系统规范

| 技能 | 用途 | 包内内容 | 静态检查 | 服务依赖（原目录） | 许可声明 | 运行记录 |
|---|---|---|---|---|---|---|
| [Apple 人机界面指南 · `apple-hig`](skills/design-system/apple-hig/SKILL.md) | Apple HIG 的 14 个子技能，覆盖 iOS/macOS/visionOS/watchOS/tvOS 的平台、基础、组件与模式 | 仅简介 | 非完整技能 | 待确认 | MIT | 未测试 |
| [Anthropic 品牌规范 · `brand-guidelines`](skills/design-system/brand-guidelines/SKILL.md) | 应用 Anthropic 官方品牌色和字体，可作为制定自家品牌规范的参考 | 仅简介 | 非完整技能 | 待确认 | Apache-2.0 | 未测试 |
| [色彩专家 · `color-expert`](skills/design-system/color-expert/SKILL.md) | 色彩科学专家：OKLCH/OKLAB、调色板生成、对比度无障碍、色名和色彩理论 | 仅简介 | 非完整技能 | 待确认 | CC-BY-4.0 | 未测试 |
| [跨平台设计规则 · `platform-design`](skills/design-system/platform-design/SKILL.md) | 来自 Apple HIG、Material Design 3 和 WCAG 2.2 的 300+ 条跨平台设计规则 | 仅简介 | 非完整技能 | 待确认 | MIT | 未测试 |
| [shadcn/ui 组件 · `shadcn-ui`](https://github.com/google-labs-code/skills) | 用 shadcn/ui 构建结构化、无障碍的 UI 组件 | 仅外链 | 不适用 | 待确认 | unknown | 未测试 |
| [SwiftUI 设计 · `swiftui-design`](skills/design-system/swiftui-design/SKILL.md) | SwiftUI 前端设计：反 AI 套路规则、设计方向建议、品牌资产协议和五维评审 | 仅简介 | 非完整技能 | 待确认 | MIT | 未测试 |
| [主题工厂 · `theme-factory`](skills/design-system/theme-factory/SKILL.md) | 给幻灯片、文档、报告和落地页套用专业字体与配色主题，内置 10 套 | 仅简介 | 非完整技能 | 待确认 | Apache-2.0 | 未测试 |
| [UI 约束集 · `ui-skills`](skills/design-system/ui-skills/SKILL.md) | 指导 agent 构建界面的一组有主见的约束，保持大量小 UI 的一致性 | 仅简介 | 非完整技能 | 待确认 | MIT | 未测试 |
| [UI/UX Pro Max · `ui-ux-pro-max`](skills/design-system/ui-ux-pro-max/SKILL.md) | UI/UX Pro Max 目录入口（完整模板与数据未随 OpenDesign 打包） | 仅简介 | 待复核引用 | 待确认 | MIT | 未测试 |
| [Web 界面规范审查 · `web-design-guidelines`](skills/design-system/web-design-guidelines/SKILL.md) | 按 Vercel Web Interface Guidelines 审查 UI 代码的布局、排版、色彩、动效和无障碍 | 附带正文 | 未检出缺失* | 待确认 | MIT | 未测试 |
| [WordPress 设计系统 · `wpds`](https://github.com/WordPress/skills) | 应用 WordPress 官方设计 token、排版和组件模式 | 仅外链 | 不适用 | 待确认 | unknown | 未测试 |
### 创意方向与评审

| 技能 | 用途 | 包内内容 | 静态检查 | 服务依赖（原目录） | 许可声明 | 运行记录 |
|---|---|---|---|---|---|---|
| [头脑风暴 · `brainstorming`](skills/design-system/brainstorming/SKILL.md) | 通过结构化提问和备选探索把粗略想法变成完整设计 | 仅简介 | 非完整技能 | 待确认 | MIT | 未测试 |
| [AI 创意总监 · `creative-director`](skills/design-system/creative-director/SKILL.md) | AI 创意总监：20+ 创意方法论、对标戛纳/D&AD 的三轴自评和五阶段流程 | 仅简介 | 非完整技能 | 待确认 | CC-BY-4.0 | 未测试 |
| [设计咨询 · `design-consultation`](skills/design-system/design-consultation/SKILL.md) | 从零构建完整设计系统，带创意冒险与真实产品样机 | 仅简介 | 非完整技能 | 待确认 | MIT | 未测试 |
| [设计评审修复 · `design-review`](skills/design-system/design-review/SKILL.md) | 视觉审计后以原子提交修复问题并给出前后截图 | 仅简介 | 非完整技能 | 待确认 | MIT | 未测试 |
| [OpenAI 前端手册 · `frontend-skill`](https://github.com/openai/skills) | 用克制构图打造视觉强的落地页、网站和应用 UI（OpenAI 前端手册） | 仅外链 | 不适用 | 待确认 | unknown | 未测试 |
| [资深设计评审 · `plan-design-review`](skills/design-system/plan-design-review/SKILL.md) | 按维度 0-10 打分、说明满分标准并标出 AI 粗制痕迹，作为合并前关卡 | 仅简介 | 非完整技能 | 待确认 | MIT | 未测试 |
### DESIGN.md 与设计流程

| 技能 | 用途 | 包内内容 | 静态检查 | 服务依赖（原目录） | 许可声明 | 运行记录 |
|---|---|---|---|---|---|---|
| [设计简报解析 · `design-brief`](skills/design-system/design-brief/SKILL.md) | 把 I-Lang 协议格式的结构化设计简报解析成明确的设计规格，消除模糊需求 | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | 未测试 |
| [DESIGN.md 管理 · `design-md`](https://github.com/google-labs-code/skills) | 创建和管理 DESIGN.md，把设计方向、token 和视觉规则集中到单一来源 | 仅外链 | 不适用 | 待确认 | unknown | 未测试 |
| [提示词增强 · `enhance-prompt`](https://github.com/google-labs-code/skills) | 用设计规范和 UI/UX 术语改写提示词，澄清视觉输出需求 | 仅外链 | 不适用 | 待确认 | unknown | 未测试 |
| [参考转设计合约 · `reference-design-contract`](skills/design-system/reference-design-contract/SKILL.md) | 把模糊品味、截图、URL、参考转成有依据的 DESIGN.md 和实现交接文档 | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | [显式试用](docs/validation-results.md) |
| [Stitch 迭代循环 · `stitch-loop`](https://github.com/google-labs-code/skills) | 设计到代码的反馈循环：点评→调整→交付，提升成品与需求的视觉一致性 | 仅外链 | 不适用 | 待确认 | unknown | 未测试 |
| [Stitch 语义设计系统 · `stitch-skill`](skills/design-system/stitch-skill/SKILL.md) | 为 Google Stitch 生成高标准、反模板化的 DESIGN.md 设计系统文件 | 附带正文 | 未检出缺失* | 待确认 | MIT | 未测试 |
### Figma

| 技能 | 用途 | 包内内容 | 静态检查 | 服务依赖（原目录） | 许可声明 | 运行记录 |
|---|---|---|---|---|---|---|
| [Figma Code Connect · `figma-code-connect-components`](https://github.com/figma/skills) | 用 Code Connect 把 Figma 组件与代码组件关联 | 仅外链 | 不适用 | Figma（账号/MCP） | unknown | 未测试 |
| [Figma 设计系统规则 · `figma-create-design-system-rules`](https://github.com/figma/skills) | 为 Figma 到代码流程生成项目专属设计系统规则（token、命名、lint） | 仅外链 | 不适用 | Figma（账号/MCP） | unknown | 未测试 |
| [新建 Figma 文件 · `figma-create-new-file`](https://github.com/figma/skills) | 新建空白 Figma Design 或 FigJam 文件 | 仅外链 | 不适用 | Figma（账号/MCP） | unknown | 未测试 |
| [生成 Figma 设计 · `figma-generate-design`](https://github.com/figma/skills) | 用设计系统组件根据代码或描述在 Figma 中构建/更新页面 | 仅外链 | 不适用 | Figma（账号/MCP） | unknown | 未测试 |
| [生成 Figma 组件库 · `figma-generate-library`](https://github.com/figma/skills) | 从代码库构建或更新 Figma 设计系统组件库 | 仅外链 | 不适用 | Figma（账号/MCP） | unknown | 未测试 |
| [Figma 转代码 · `figma-implement-design`](https://github.com/figma/skills) | 把 Figma 设计 1:1 还原为生产级代码 | 仅外链 | 不适用 | Figma（账号/MCP） | unknown | 未测试 |
| [Figma 插件 API · `figma-use`](https://github.com/figma/skills) | 运行 Figma Plugin API 脚本进行画布写入、检查、变量和设计系统操作（其他 Figma 技能前置） | 仅外链 | 不适用 | Figma（账号/MCP） | unknown | 未测试 |

<a id="image"></a>
## 图像（28）

### 生成艺术与动图

| 技能 | 用途 | 包内内容 | 静态检查 | 服务依赖（原目录） | 许可声明 | 运行记录 |
|---|---|---|---|---|---|---|
| [算法艺术 · `algorithmic-art`](skills/image/algorithmic-art/SKILL.md) | 用 p5.js 和固定随机种子创作可复现的生成艺术 | 仅简介 | 非完整技能 | 待确认 | Apache-2.0 | 未测试 |
| [画布设计 · `canvas-design`](skills/image/canvas-design/SKILL.md) | 依据设计理念产出 PNG/PDF 海报、插画等静态视觉作品 | 仅简介 | 非完整技能 | 待确认 | Apache-2.0 | 未测试 |
| [Codex 宠物精灵 · `hatch-pet`](skills/image/hatch-pet/SKILL.md) | 从角色图创建、修复、校验、预览并打包 Codex 兼容的动画宠物精灵图 | 附带正文 | 未检出缺失* | OpenAI API（文中提及） | Apache-2.0 | 未测试 |
| [Slack 动图 · `slack-gif-creator`](skills/image/slack-gif-creator/SKILL.md) | 制作符合 Slack 尺寸限制的动画 GIF，含校验器和动画原语 | 仅简介 | 非完整技能 | 待确认 | Apache-2.0 | 未测试 |
### 设计参考图与品牌视觉

| 技能 | 用途 | 包内内容 | 静态检查 | 服务依赖（原目录） | 许可声明 | 运行记录 |
|---|---|---|---|---|---|---|
| [品牌套件图 · `brandkit`](skills/image/brandkit/SKILL.md) | 生成高端品牌规范板、Logo 系统、识别提案和视觉世界展示图 | 附带正文 | 未检出缺失* | 待确认 | MIT | 未测试 |
| [电商产品图 · `ecommerce-image-workflow`](skills/image/ecommerce-image-workflow/SKILL.md) | 基于真实产品参考照生成主图、卖点图和场景图（需上传产品图） | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | 未测试 |
| [移动端设计参考图 · `imagegen-frontend-mobile`](skills/image/imagegen-frontend-mobile/SKILL.md) | 生成高端原生感的 iOS/Android 应用界面概念与流程图 | 附带正文 | 未检出缺失* | 待确认 | MIT | 未测试 |
| [网页设计参考图 · `imagegen-frontend-web`](skills/image/imagegen-frontend-web/SKILL.md) | 生成高端、注重转化的网页设计参考图（每屏一张横图） | 附带正文 | 未检出缺失* | 待确认 | MIT | 未测试 |
### AI 生图与编辑

| 技能 | 用途 | 包内内容 | 静态检查 | 服务依赖（原目录） | 许可声明 | 运行记录 |
|---|---|---|---|---|---|---|
| [fal 3D 生成 · `fal-3d`](https://github.com/fal-ai-community/skills) | 通过 fal.ai 从文字或图片生成 3D 模型 | 仅外链 | 不适用 | fal.ai | unknown | 未测试 |
| [fal 生成 · `fal-generate`](https://github.com/fal-ai-community/skills) | 通过 fal.ai 调用 Flux、SDXL、ideogram 等模型生成图像和视频 | 仅外链 | 不适用 | fal.ai | unknown | 未测试 |
| [fal 图像编辑 · `fal-image-edit`](https://github.com/fal-ai-community/skills) | 通过 fal.ai 做风格迁移、去背景、去物体和局部重绘 | 仅外链 | 不适用 | fal.ai | unknown | 未测试 |
| [fal 实时生图 · `fal-realtime`](https://github.com/fal-ai-community/skills) | 通过 fal.ai 实时/流式生成图像，适合情绪板和快速迭代 | 仅外链 | 不适用 | fal.ai | unknown | 未测试 |
| [fal LoRA 训练 · `fal-train`](https://github.com/fal-ai-community/skills) | 在 fal.ai 训练 LoRA，用于品牌/角色/风格定制生图 | 仅外链 | 不适用 | fal.ai | unknown | 未测试 |
| [fal 虚拟试衣 · `fal-tryon`](https://github.com/fal-ai-community/skills) | 通过 fal.ai 虚拟试穿服装，适合电商和造型实验 | 仅外链 | 不适用 | fal.ai | unknown | 未测试 |
| [GIF 表情贴纸 · `gif-sticker-maker`](skills/image/gif-sticker-maker/SKILL.md) | 通过 MiniMax API 把照片转成泡泡玛特/Funko 风动态 GIF 贴纸 | 仅简介 | 非完整技能 | MiniMax API | MIT | 未测试 |
| [OpenAI 生图 · `imagegen`](https://github.com/openai/skills) | 用 OpenAI Image API 生成和编辑项目素材：UI 样机、图标、插画、社交卡 | 仅外链 | 不适用 | OpenAI Image API | unknown | 未测试 |
| [Gemini 生图 · `imagen`](https://github.com/sanjay3290/imagen) | 用 Google Gemini 图像生成 API 生成 UI 样机、图标、插画等 | 仅外链 | 不适用 | Google Gemini API | unknown | 未测试 |
| [Pixelbin 媒体 · `pixelbin-media`](https://github.com/pixelbin-dev/skills) | 通过 Pixelbin 85+ API 生成和编辑图像/视频并搭建网页 | 仅外链 | 不适用 | Pixelbin API | unknown | 未测试 |
| [Replicate 模型 · `replicate`](skills/image/replicate/SKILL.md) | 通过 Replicate API 发现、比较和运行图像/音频/视频 AI 模型 | 仅简介 | 非完整技能 | Replicate API | Apache-2.0 | 未测试 |
| [Venice 图像编辑 · `venice-image-edit`](skills/image/venice-image-edit/SKILL.md) | 通过 Venice.ai API 编辑图像、放大和去背景 | 仅简介 | 非完整技能 | Venice.ai | MIT | 未测试 |
| [Venice 生图 · `venice-image-generate`](skills/image/venice-image-generate/SKILL.md) | 通过 Venice.ai API 生成图像及可用风格 | 仅简介 | 非完整技能 | Venice.ai | MIT | 未测试 |
### 图像增强与分析

| 技能 | 用途 | 包内内容 | 静态检查 | 服务依赖（原目录） | 许可声明 | 运行记录 |
|---|---|---|---|---|---|---|
| [fal 修复 · `fal-restore`](https://github.com/fal-ai-community/skills) | 通过 fal.ai 去模糊、降噪、修复人脸和老文档 | 仅外链 | 不适用 | fal.ai | unknown | 未测试 |
| [fal 超分 · `fal-upscale`](https://github.com/fal-ai-community/skills) | 通过 fal.ai 超分辨率放大增强图像和视频 | 仅外链 | 不适用 | fal.ai | unknown | 未测试 |
| [fal 视觉分析 · `fal-vision`](https://github.com/fal-ai-community/skills) | 通过 fal.ai 做分割、检测、OCR、描述和视觉问答 | 仅外链 | 不适用 | fal.ai | unknown | 未测试 |
| [图像增强 · `image-enhancer`](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/image-enhancer) | 提升图片和截图的分辨率、锐度与清晰度 | 仅外链 | 不适用 | 待确认 | unknown | 未测试 |
### 截图

| 技能 | 用途 | 包内内容 | 静态检查 | 服务依赖（原目录） | 许可声明 | 运行记录 |
|---|---|---|---|---|---|---|
| [整页截图 · `full-page-screenshot`](https://github.com/LewisLiu007/full-page-screenshot) | 通过 Chrome DevTools Protocol 零依赖截取网页整页截图 | 仅外链 | 不适用 | 待确认 | unknown | 未测试 |
| [系统截图 · `screenshot`](skills/image/screenshot/SKILL.md) | 跨平台截取桌面、应用窗口或像素区域 | 仅简介 | 非完整技能 | 待确认 | Apache-2.0 | 未测试 |
| [营销截图 · `screenshots-marketing`](https://github.com/Shpigford/screenshots) | 用 Playwright 生成落地页 Hero、App Store 和更新日志营销截图 | 仅外链 | 不适用 | 待确认 | unknown | 未测试 |

<a id="video"></a>
## 视频（17）

### AI 视频生成与编辑

| 技能 | 用途 | 包内内容 | 静态检查 | 服务依赖（原目录） | 许可声明 | 运行记录 |
|---|---|---|---|---|---|---|
| [可灵 O3 · `fal-kling-o3`](https://github.com/fal-ai-community/skills) | 通过 fal.ai 使用可灵 Kling O3 生成图像和视频 | 仅外链 | 不适用 | fal.ai | unknown | 未测试 |
| [fal 口型同步 · `fal-lip-sync`](https://github.com/fal-ai-community/skills) | 通过 fal.ai 生成数字人说话视频并对口型 | 仅外链 | 不适用 | fal.ai | unknown | 未测试 |
| [fal 视频编辑 · `fal-video-edit`](https://github.com/fal-ai-community/skills) | 通过 fal.ai 对视频做风格重绘、超分、去背景和配音 | 仅外链 | 不适用 | fal.ai | unknown | 未测试 |
| [Sora 视频 · `sora`](https://github.com/openai/skills) | 通过 OpenAI Sora API 生成、混剪和管理短视频 | 仅外链 | 不适用 | OpenAI Sora API | unknown | 未测试 |
| [Venice 视频 · `venice-video`](skills/video/venice-video/SKILL.md) | 通过 Venice.ai API 生成视频和转写 | 仅简介 | 非完整技能 | Venice.ai | MIT | 未测试 |
### 程序化视频与帧动画

| 技能 | 用途 | 包内内容 | 静态检查 | 服务依赖（原目录） | 许可声明 | 运行记录 |
|---|---|---|---|---|---|---|
| [NYT 风数据图表帧 · `frame-data-chart-nyt`](skills/video/frame-data-chart-nyt/SKILL.md) | 纽约时报风排版、错峰揭示动画的编辑级数据图表帧 | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | 未测试 |
| [便利贴流程图帧 · `frame-flowchart-sticky`](skills/video/frame-flowchart-sticky/SKILL.md) | SVG 曲线连线、便利贴节点和光标交互的白板流程图帧 | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | 未测试 |
| [故障艺术标题帧 · `frame-glitch-title`](skills/video/frame-glitch-title/SKILL.md) | 数字故障、色差偏移的赛博风标题帧 | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | 未测试 |
| [胶片漏光电影帧 · `frame-light-leak-cinema`](skills/video/frame-light-leak-cinema/SKILL.md) | 胶片漏光、颗粒、16:9 遮幅和大号衬线字的电影感开场帧 | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | 未测试 |
| [流体背景 Hero 帧 · `frame-liquid-bg-hero`](skills/video/frame-liquid-bg-hero/SKILL.md) | WebGL 风流体背景加引言叠字的开场/Hero 帧 | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | 未测试 |
| [品牌 Logo 收尾帧 · `frame-logo-outro`](skills/video/frame-logo-outro/SKILL.md) | Logo 分段组装、辉光和标语揭示的片尾帧 | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | 未测试 |
| [macOS 通知横幅 · `frame-macos-notification`](skills/video/frame-macos-notification/SKILL.md) | 逼真的 macOS 通知横幅，用于视频叠加或产品预告 | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | 未测试 |
| [Remotion · `remotion`](https://github.com/remotion-dev/remotion) | 用 React 程序化制作视频 | 仅外链 | 不适用 | 待确认 | Remotion License（自定义，部分公司需付费授权） | 未测试 |
| [VFX 文字光标 · `vfx-text-cursor`](skills/video/vfx-text-cursor/SKILL.md) | 光标光迹、色散光线和光晕的逐词引言揭示特效 | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | 未测试 |
| [Hyperframes 视频脚本 · `video-hyperframes`](skills/video/video-hyperframes/SKILL.md) | 兼容 Hyperframes/Remotion 的连续帧动画，支持自动播放 | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | 未测试 |
### 视频下载与剪辑

| 技能 | 用途 | 包内内容 | 静态检查 | 服务依赖（原目录） | 许可声明 | 运行记录 |
|---|---|---|---|---|---|---|
| [视频下载 · `video-downloader`](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/video-downloader) | 从 YouTube 等平台下载视频，支持多种格式和画质 | 仅外链 | 不适用 | 待确认 | unknown | 未测试 |
| [YouTube 剪辑 · `youtube-clipper`](skills/video/youtube-clipper/SKILL.md) | 拉取 YouTube 视频、切精彩片段、加字幕并导出 | 仅简介 | 非完整技能 | 待确认 | MIT | 未测试 |

<a id="deck"></a>
## 演示文稿（9）

### HTML 演示

| 技能 | 用途 | 包内内容 | 静态检查 | 服务依赖（原目录） | 许可声明 | 运行记录 |
|---|---|---|---|---|---|---|
| [归藏编辑墨水 Deck · `deck-guizang-editorial`](skills/deck/deck-guizang-editorial/SKILL.md) | 杂志编辑风 × 墨水屏质感，10 种版式、5 套配色 | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | 未测试 |
| [1920 画布自由 Deck · `deck-open-slide-canvas`](skills/deck/deck-open-slide-canvas/SKILL.md) | 锁定 1920×1080 画布、React 组件级自由排版的演示 | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | 未测试 |
| [瑞士国际主义 Deck · `deck-swiss-international`](skills/deck/deck-swiss-international/SKILL.md) | 16 栏网格、单一高饱和强调色、22 种锁定版式的瑞士风演示 | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | 未测试 |
| [动效 HTML 演示 · `frontend-slides`](skills/deck/frontend-slides/SKILL.md) | 生成动画丰富的 HTML 演示，并提供视觉风格预览 | 仅简介 | 非完整技能 | 待确认 | MIT | 未测试 |
| [Keynote 风格 PPT · `ppt-keynote`](skills/deck/ppt-keynote/SKILL.md) | Apple Keynote 品质的 HTML 幻灯片，一屏一卡，键盘左右翻页 | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | 未测试 |
### PPTX 文件

| 技能 | 用途 | 包内内容 | 静态检查 | 服务依赖（原目录） | 许可声明 | 运行记录 |
|---|---|---|---|---|---|---|
| [NanoBanana PPT · `nanobanana-ppt`](https://github.com/op7418/NanoBanana-PPT-Skills) | 结合文档分析与 AI 配图生成风格化 PPT | 仅外链 | 不适用 | 待确认 | unknown | 未测试 |
| [PPTX（Anthropic） · `pptx`](https://github.com/anthropics/skills/tree/main/skills/pptx) | 读取、生成和调整 PowerPoint 幻灯片、版式和模板 | 仅外链 | 不适用 | 待确认 | Proprietary (© Anthropic, all rights reserved) | 未测试 |
| [MiniMax PPTX 生成 · `pptx-generator`](skills/deck/pptx-generator/SKILL.md) | 用 PptxGenJS 从零创建和编辑 PPT（MiniMax 生产流程） | 仅简介 | 非完整技能 | 待确认 | MIT | 未测试 |
| [PPTX（OpenAI） · `slides`](https://github.com/openai/skills) | 用 PptxGenJS 创建和编辑 .pptx 演示文稿 | 仅外链 | 不适用 | 待确认 | unknown | 未测试 |

<a id="template"></a>
## 模板（9）

### 视频模板

| 技能 | 用途 | 包内内容 | 静态检查 | 服务依赖（原目录） | 许可声明 | 运行记录 |
|---|---|---|---|---|---|---|
| [8 位轨道视频模板 · `8-bit-orbit-video-template`](skills/template/8-bit-orbit-video-template/SKILL.md) | 基于 HyperFrames 的复古像素风多场景 HTML 转视频模板 | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | 未测试 |
| [午夜编辑视频模板 · `after-hours-editorial-template`](skills/template/after-hours-editorial-template/SKILL.md) | 高级时装感暗色编辑风三页电影分镜 HyperFrames 模板 | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | 未测试 |
| [瑞士风用户研究模板 · `swiss-user-research-video-template`](skills/template/swiss-user-research-video-template/SKILL.md) | 暖纸色瑞士风用户研究叙事模板（演示/视频） | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | 未测试 |
| [微信读书年度报告模板 · `weread-year-in-review-video-template`](skills/template/weread-year-in-review-video-template/SKILL.md) | 微信读书风 9:16 竖版年度阅读报告/书摘回顾视频模板 | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | 未测试 |
### 演示模板

| 技能 | 用途 | 包内内容 | 静态检查 | 服务依赖（原目录） | 许可声明 | 运行记录 |
|---|---|---|---|---|---|---|
| [金融科技瑞士网格模板 · `digits-fintech-swiss-template`](skills/template/digits-fintech-swiss-template/SKILL.md) | 黑/暖纸/荧光青柠配色的瑞士网格金融数据故事演示模板 | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | 未测试 |
| [酒红编辑宣言模板 · `editorial-burgundy-principles-template`](skills/template/editorial-burgundy-principles-template/SKILL.md) | 酒红/腮红/哑金配色的宣言、文化类编辑风演示模板 | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | 未测试 |
| [复古季度复盘模板 · `html-ppt-retro-quarterly-review`](skills/template/html-ppt-retro-quarterly-review/SKILL.md) | 蓝+橙复古编辑风季度复盘/路线图演示模板 | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | 未测试 |
| [瑞士创意模式模板 · `swiss-creative-mode-template`](skills/template/swiss-creative-mode-template/SKILL.md) | 瑞士风创意演示模板：大字排版、几何卡片、主题切换与热点叠层 | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | 未测试 |
### 报告模板

| 技能 | 用途 | 包内内容 | 静态检查 | 服务依赖（原目录） | 许可声明 | 运行记录 |
|---|---|---|---|---|---|---|
| [田野笔记报告模板 · `field-notes-editorial-template`](skills/template/field-notes-editorial-template/SKILL.md) | 纸张底、衬线大标题、柔和洞察卡和留存图表的编辑风报告模板 | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | 未测试 |

<a id="utility"></a>
## 工具（6）

### 工作流工具

| 技能 | 用途 | 包内内容 | 静态检查 | 服务依赖（原目录） | 许可声明 | 运行记录 |
|---|---|---|---|---|---|---|
| [聊天动效叠层 · `chat-motion-overlay`](skills/utility/chat-motion-overlay/SKILL.md) | 根据聊天记录或截图生成可配置的聊天气泡动效叠层（头像、设备框、昵称） | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | 未测试 |
| [导出下载排障 · `export-download-debugging`](skills/utility/export-download-debugging/SKILL.md) | 诊断修复浏览器/预览/Electron 中图片导出、Blob、另存为、0KB 文件等下载问题 | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | 未测试 |
| [PPTX 还原度审计 · `pptx-html-fidelity-audit`](skills/utility/pptx-html-fidelity-audit/SKILL.md) | 对比 python-pptx 导出与源 HTML 演示，找出版式漂移并严格重新导出 | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | 未测试 |
| [PR 反馈质量关卡 · `pr-feedback-quality-gate`](skills/utility/pr-feedback-quality-gate/SKILL.md) | 安全跟踪 PR 反馈、解决评审意见和冲突、验证修复并只读交叉评审 | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | 未测试 |
### OpenDesign 内部

| 技能 | 用途 | 包内内容 | 静态检查 | 服务依赖（原目录） | 许可声明 | 运行记录 |
|---|---|---|---|---|---|---|
| [素材库管理 · `library-curator`](skills/utility/library-curator/SKILL.md) | 搜索 OD 素材库（全局资源登记）并把匹配素材应用到当前项目（依赖 OpenDesign 应用） | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | 未测试 |
| [OD Next 素材输入 · `od-next-media-inputs`](skills/utility/od-next-media-inputs/SKILL.md) | 在 OD Next 计划中准备所需媒体素材、复用能力证据并处理异步任务（依赖 OpenDesign 应用） | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | 未测试 |

<a id="audio"></a>
## 音频（4）

### 音乐生成

| 技能 | 用途 | 包内内容 | 静态检查 | 服务依赖（原目录） | 许可声明 | 运行记录 |
|---|---|---|---|---|---|---|
| [AI 音乐专辑 · `ai-music-album`](skills/audio/ai-music-album/SKILL.md) | AI 音乐专辑全流程：概念、歌词、曲目编排和导出 | 仅简介 | 非完整技能 | 待确认 | CC0-1.0 | 未测试 |
| [Venice 音乐生成 · `venice-audio-music`](skills/audio/venice-audio-music/SKILL.md) | 通过 Venice.ai 排队生成和获取音乐 | 仅简介 | 非完整技能 | Venice.ai | MIT | 未测试 |
### 语音合成

| 技能 | 用途 | 包内内容 | 静态检查 | 服务依赖（原目录） | 许可声明 | 运行记录 |
|---|---|---|---|---|---|---|
| [OpenAI 语音合成 · `speech`](skills/audio/speech/SKILL.md) | 用 OpenAI API 内置声音把文本转为语音 | 仅简介 | 非完整技能 | OpenAI API | Apache-2.0 | 未测试 |
| [Venice 语音合成 · `venice-audio-speech`](skills/audio/venice-audio-speech/SKILL.md) | 通过 Venice.ai 的 TTS 模型、声音和流式输出生成语音 | 仅简介 | 非完整技能 | Venice.ai | MIT | 未测试 |

<a id="design"></a>
## 品牌设计（1）

### 品牌提取

| 技能 | 用途 | 包内内容 | 静态检查 | 服务依赖（原目录） | 许可声明 | 运行记录 |
|---|---|---|---|---|---|---|
| [品牌提取 · `brand-extract`](skills/design/brand-extract/SKILL.md) | 驱动应用内浏览器从真实网站提取完整品牌套件（依赖 OpenDesign 应用） | 附带正文 | 未检出缺失* | 待确认 | Apache-2.0 | 未测试 |

\* 仅覆盖明确 Markdown 本地链接和 scripts/references/templates 文件路径；不证明运行依赖齐全。全部运行状态见 registry.json。
