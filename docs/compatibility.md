# 状态与兼容性

[首页](../README.md) · [完整目录](../CATALOG.md) · [实测记录](validation-results.md)

| 内容/状态 | 含义 |
|---|---|
| 附带正文 | 本地有实际内容，不等于全依赖齐全 |
| 仅简介 | SKILL.md 主要介绍上游，不能替代完整技能 |
| 仅外链 | 不附带完整目录 |
| 未检出缺失 | 限定文件路径扫描未发现问题，不等于运行通过 |
| 显式试用 | 当前会话读取安装后文件，完成一个任务和修改；不证明自动发现或稳定成功率 |

本轮三项显式试用：faq-page、resume-modern、reference-design-contract。其他 160 项未运行验证。Codex 新会话自动发现、Claude 执行及 Windows/Linux 均未测试。

## 需要注意的依赖

- FAQ：需给定 DESIGN.md 和问答材料；原文的 artifact 输出约定在本次输入中明确改为写文件。
- 简历：无额外 API；打印还依赖浏览器，应每次检查内容是否溢出。
- 设计规范：需目标或参考材料；没有参考时只能以简报为依据。
- ui-ux-pro-max：只有简介，没有完整搜索数据与脚本。
- library-curator、od-next-media-inputs、brand-extract、ecommerce-image-workflow：涉及 OpenDesign 专属接口或工作流，未进入试用包。
- web-clone：脚本存在，独立路径和浏览器依赖尚未验证。

原目录未填写服务依赖不代表免费。Agent 使用成本与技能额外服务成本分开；本轮没有调用付费媒体 API。
