# original vs clone · 克隆评估报告

## 结论
- 原站 URL: https://threejs.org/examples/webgl_animation_keyframes.html
- 克隆 URL: http://127.0.0.1:8123/tokyo-keyframes.html
- 自动推断复杂度: L5
- 复刻模式建议: 技术拆解 / 忠实复刻优先
- 自动报告边界: 结构、数量、框架、console 可自动比；传入 visual-diff 后可纳入像素差异分。内容残留和法务仍需审计。

## 技术信号
| 项目 | 原站 | 克隆站 |
|---|---|---|
| title | three.js webgl - animation - keyframes | three.js WebGL · 关键帧动画 |
| lang | en | zh-CN |
| frameworks | none | none |
| scrollHeight | 900 | 900 |
| h1 | none | none |

## 数量对比
| 指标 | 原站 | 克隆站 | 自动评分 |
|---|---:|---:|---:|
| sections | 0 | 0 | 5/5 |
| links | 3 | 3 | 5/5 |
| images | 0 | 0 | 5/5 |
| video | 0 | 0 | 5/5 |
| canvas | 4 | 4 | 5/5 |
| forms | 0 | 0 | 5/5 |
| buttons | 0 | 0 | 5/5 |
| inputs | 0 | 0 | 5/5 |
| interactive | 3 | 3 | 5/5 |
| scripts | 0 | 0 | 5/5 |

## 复刻评分
- 源证据: 5/5（官方源码及本地依赖）
- 结构保真: 5/5
- 视觉保真: 5/5
- 动效/交互: 4/5（拖拽截图确认旋转，缩放和平移未逐项操作）
- 响应式: 4/5
- 功能完整: 4/5（核心动画运行已验证）
- 内容替换: 需人工看文案残留
- 法务/部署风险: 需人工核查 license / 素材

## Console
- 原站 console errors: 0
- 克隆 console errors: 0
- 原站 page errors: 0
- 克隆 page errors: 0

## 路由覆盖
- 未提供 route-crawl 结果。多页面站需要传 --original-routes / --clone-routes。


## 交互覆盖
- 原站可见交互目标: 3
- 克隆可见交互目标: 3
- 原站 canvas 目标: 2
- 克隆 canvas 目标: 2
- 原站 changed actions: 1/8
- 克隆 changed actions: 1/7
- 原站 interaction probe: RECON/interactions/original-interactions.json
- 克隆 interaction probe: RECON/interactions-clone/clone-interactions.json
- 判断: 交互数量信号接近，仍需看截图确认状态质量。


## 截图证据
- 原站侦察: RECON/original-recon.json
- 克隆侦察: RECON/clone-recon.json
- 像素差异: RECON/visual-diff-1440.json
- 像素差异率: 0.002990740740740741
- 原站截图: screenshots/original-1440.png, screenshots/original-768.png, screenshots/original-390.png
- 克隆截图: screenshots/clone-1440.png, screenshots/clone-768.png, screenshots/clone-390.png

## 已知缺口
- 未传入 visual-diff 时，视觉保真需要打开截图人工确认。
- 法务、素材授权、品牌替换完整度需要人工核查。

## 人工复核

模型内嵌许可为 CC BY 4.0；Three.js 许可为 MIT，详见 ATTRIBUTION.md。原始模型和渲染代码保留，说明文字中文化。像素差异数据对应首次截图，之后只缩短署名并移动手机统计面板以消除文字遮挡。最终手机检查见 RECON/mobile-final-recon.json。不是多页面产品，故不爬取站外作者链接。
