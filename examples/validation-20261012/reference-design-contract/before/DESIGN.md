# 纸间帮助中心 · 设计规范

依据：本次虚构测试简报。没有外部视觉参考；具体色值和间距为 inferred 设计选择。

## 1. Visual Theme & Atmosphere

温和的编辑式帮助中心。大标题、细分隔线和安静留白，优先帮助用户找到答案。

## 2. Color

背景 #f6f5f0，内容 #ffffff，正文 #202a25，次要文字 #59635d，强调色 #215b45，边线 #d9dfd8。错误/空结果用文字解释，不只用颜色。强调按钮使用白字。

## 3. Typography

使用 Georgia 搭配系统中文衬线作标题；正文使用系统 sans-serif，不请求外部字体。桌面标题 56px，手机 36px；正文 16px、行高 1.65；辅助文字最小 13px。

## 4. Spacing & Grid

间距 8/16/24/32/48/64px。主内容最大 1040px。桌面左右留白 40px，手机 20px；容器用 min() 避免水平溢出。

## 5. Layout & Composition

顺序：品牌与测试说明、标题、搜索、分类、FAQ、联系入口。单列问答。390px 下分类换行、输入占满宽度，禁用固定宽度内容。

## 6. Components

搜索框关联 label，最小高度 48px。分类按钮最小 44px 且有 aria-pressed。FAQ 使用 details/summary；每项点击区域最小 56px。搜索结果数用 aria-live；无结果显示可理解的原因。

## 7. Motion & Interaction

颜色/背景过渡 150ms；尊重 prefers-reduced-motion。按问题或答案搜索，不区分大小写；分类和关键词同时生效。键盘可操作所有交互，focus-visible 为 3px 实线。

## 8. Voice & Brand

短句、直接回答。所有产品规则来自测试提供的问答；未知事实不能补成承诺。页脚显示「虚构测试案例」。

## 9. Anti-patterns

不使用紫蓝光晕、巨型阴影、外部图片、假客户数或真实收费承诺。不让分类切换清空关键词，不把无结果状态误当作加载中。
