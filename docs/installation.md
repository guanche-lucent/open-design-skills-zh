# 安装与试用

当前版本：`0.1.0-preview.2`。包含 FAQ 页面、简历排版、参考转设计规范三项。需要 Python 3.9+ 和能读取本地文件的 Agent；仅当前 Codex 会话的显式读取方式完成测试。

## 安装一个技能

下载并解压试用包，进入解压后的目录。先创建一个用于试用的项目目录，再运行：

```bash
mkdir -p ../my-design-project
python3 scripts/install.py list
python3 scripts/install.py install --skill faq-page --project ../my-design-project --agent codex
```

这会安装到该项目的 `.agents/skills/faq-page`，不修改全局目录。其他可选 ID：`resume-modern`、`reference-design-contract`。每次只装需要的一项。

需要 Claude 目录布局时用 `--agent claude`，目的地为 `.claude/skills/<技能名>`；本轮只验证了文件安装，尚未验证 Claude 执行。

## 第一次使用

在试用项目中打开 Agent。显式提供路径，避免把未验证的自动发现当作前提：

> 请读取 .agents/skills/faq-page/SKILL.md，用我提供的 DESIGN.md 和问答材料生成单文件 index.html，内联 CSS 和 JS，无外部资源。请直接保存文件，不使用 artifact 标签；完成后检查搜索、分类、键盘操作和手机布局。

FAQ 需要问答和设计约束。可以使用本包 examples/validation-20261012 中的虚构测试材料；先读说明再使用。安装完成不代表自动生成，仍需给 Agent 具体任务。

简历：提供自己的事实材料，明确不得编造指标，要求生成 HTML 后实际导出检查页数。设计规范：提供目标、受众和参考材料，未知品牌事实应保留为未知。

## 更新与卸载

在新版解压目录运行：

```bash
python3 scripts/install.py update --skill faq-page --project ../my-design-project --agent codex
python3 scripts/install.py uninstall --skill faq-page --project ../my-design-project --agent codex
```

更新前会校验已安装文件未被修改，将旧目录移到项目 `.ods-backups/`，再安装新版本。已有用户修改或新增文件时拒绝覆盖，请先自行备份和处理。卸载只删除本工具管理且未被修改的技能目录，保留项目作品。已有同名非托管技能不会覆盖。

## 验证范围

[详细实测](validation-results.md)。官方目录参考：[OpenAI](https://learn.chatgpt.com/docs/build-skills)、[Claude Code](https://code.claude.com/docs/en/skills)，查阅于 2026-10-12。独立新会话自动发现、Windows/Linux 与 Claude 实际执行仍待验证。
