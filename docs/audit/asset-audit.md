# 本地资产核查

核查日期：2026-10-12。范围：本地文件、目录口径、明确资源引用；未执行技能，也未逐一访问上游。

共 **163 项**：**77 项附带正文**、**41 项仅简介**、**45 项仅外链**。其中 **3 项完成当前会话显式读取试用**；其余未运行验证。自动发现与跨平台执行另行验证。

- 本地技能入口：118。
- 原始文件快照：317 个文件。
- 受保护原文、资源与许可文件：314 个；哈希变化：0。
- 明确引用待复核：1 个技能。

## 引用待复核

以下为静态扫描线索，需要区分缺失依赖、运行产物和示例路径；不能把命中数量当作缺陷数量。

### ui-ux-pro-max

- `scripts/search.py`：[skills/design-system/ui-ux-pro-max/SKILL.md:31](../../skills/design-system/ui-ux-pro-max/SKILL.md)

## 人工核查补充

- **frontend-design**：正文包含 OpenDesign 注入 design system/craft 的条件说明；是否可独立完成任务仍需实测。
- **web-clone**：完整目录核对后，正文明确引用的脚本均存在。正文含 OpenDesign staging 路径；需验证独立工作目录下的路径解析和浏览器依赖。
- **ecommerce-image-workflow**：正文要求 OD_NODE_BIN / OD_BIN media generate 和 media wait；依赖 OpenDesign 媒体调度，独立环境待适配。
- **library-curator**：正文需要 OD_TOOL_TOKEN 和 /api/tools/library 接口；属于 OpenDesign 环境工作流。
- **od-next-media-inputs**：OpenDesign 内部媒体输入工作流；不能把目录复制视为独立安装成功。
- **brand-extract**：正文依赖 daemon 预置 brand.json/brand.html 与 od brand preview；独立浏览器能力不能直接替代整个工作流。

## 边界

- 许可信息沿用原 LICENSE-AUDIT，不代表本轮完成上游许可复核。
- 依赖信号按正文关键词提取并保留行号，只能帮助定位，不能当作最终依赖清单。
- hatch-pet 的 canonical-base.png 与 layout-guides 是正文说明的运行产物，不属于静态漏打包。
- ui-ux-pro-max 的 search.py 属于其明确未附带的上游完整实现；已标仅简介。
- 自动化结果见 asset-audit.json；人工判断与后续任务见 review.md。
