# Web Clone 实际案例：Littlest Tokyo

这是用户此前在 OpenDesign 中使用 web-clone 制作的作品迁入，不是这轮新生成的技能测试。原模型、渲染代码和署名保留。

## 查看

从仓库根目录运行 `python3 scripts/preview_examples.py`，然后访问终端打印的案例集地址。入口 `index.html` 在 HTTP 环境加载 3D 页面；直接双击时展示截图和启动说明。不要单独复制 tokyo-keyframes.html，它依赖整个 assets 文件夹。

## 来源与验证

- 原站：https://threejs.org/examples/webgl_animation_keyframes.html
- Three.js MIT；模型 Glen Fox 的 Littlest Tokyo 为 CC BY 4.0。详见 ATTRIBUTION.md 与 source/THREE-LICENSE.txt。
- 本次从原 OpenDesign 项目复制模型和脚本，在本地 HTTP 环境已看到完整模型。preview.png 是本次运行截图。
- historical 中是原项目的历史报告，里面的评分和检查不代表本次重新验证；历史报告引用的 RECON 路径未随本目录迁入。
- 本次迁入不改变技能安装包的三项验证名单，也不代表 web-clone 已完成跨环境安装测试。

迁入后复核：通过 scripts/preview_examples.py 的 HTTP 服务打开本地副本，完整模型已显示；4 个 canvas。资源检查仅 favicon.ico 返回 404，不影响场景。运行截图为 migrated-check.png。本次未重测全部旋转、缩放及移动端交互。
