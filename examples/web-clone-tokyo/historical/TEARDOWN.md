# Littlest Tokyo 技术拆解

所有证据均来自保存的官方部署源码 `source/index-original.html`，未拟合或重写着色器。

| 支柱 | 真实实现 | 证据 |
|---|---|---|
| 渲染 | Three.js WebGLRenderer、抗锯齿、ACES 色调映射 | SOURCE：64–68 行 |
| 天空 | Sky，保留全部太阳位置、大气与云参数 | SOURCE：74–83 行 |
| 环境光 | PMREMGenerator 从天空生成环境贴图 | SOURCE：85–87 行 |
| 相机交互 | 40° 透视相机，OrbitControls 阻尼旋转/缩放/平移 | SOURCE：89–95 行 |
| 资源 | Draco 解压原版 LittlestTokyo.glb，内嵌四张纹理 | SOURCE：97–107 行；GLB JSON |
| 动画 | AnimationMixer 播放模型内第一个关键帧片段 | SOURCE：109–112、129–141 行 |
| 响应式 | resize 同步相机宽高比和渲染器尺寸 | SOURCE：120–127 行 |

无额外物理系统、音频系统或后期合成管线。模型形状、纹理、动画与渲染参数不做猜测替代。
