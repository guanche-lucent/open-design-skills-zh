# 项目进度

更新：2026-10-13。

| 阶段 | 状态 | 证据与限制 |
|---|---|---|
| A 全量资产清点 | 静态范围完成 | 163 项；其他条目的上游在线复核未全量开展 |
| B 中文浏览整理 | 本地版完成 | 首页、场景、目录与状态解释 |
| C 首轮运行验证 | 3 项显式读取试用完成 | [实测记录](validation-results.md)；自动发现和 Claude 执行未测 |
| D 试用包 | 首版已制作并验证解压安装 | 只包含首轮三项；不是全量合集安装包 |
| E GitHub 发布 | 预览版已公开发布并验证 | GitHub 仓库、Pages、Release 均已上线 |

发布版本：`v0.1.0-preview.2`。

- [公开仓库](https://github.com/guanche-lucent/open-design-skills-zh)
- [在线案例](https://guanche-lucent.github.io/open-design-skills-zh/)
- [精选试用包](https://github.com/guanche-lucent/open-design-skills-zh/releases/tag/v0.1.0-preview.2)

目录核对和七项安装器测试通过；GitHub Actions 检查与 Pages 部署成功。公开 README 五张图片加载正常；案例页四张预览图正常、390px 无横向溢出，原网站对比按钮仅在 Web Clone 卡片中。东京模型、脚本与解码器均返回 200，已目视确认公开站点场景呈现与动画运行。未在本轮重测全部场景交互。

发布 ZIP 已重新下载，SHA256 与本地一致：`e71153fcba9942115bc96b79b2dbb068400a1c9223dd175cd67b9893fc28c67a`。版本仍为预览版；安装包仅包含三项显式读取试用技能，Web Clone 为实际作品展示。
