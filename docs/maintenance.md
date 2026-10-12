# 维护与检查

本地要求：Python 3，脚本仅使用标准库。以下命令在仓库根目录执行。

```bash
python3 scripts/check_catalog.py
python3 scripts/check_catalog.py --check
```

第一条根据 registry.json 重建 CATALOG、首页数量和资产报告；第二条只检查生成物一致性、入口对应、原文件哈希和维护文档链接。

## 修改规则

- 新条目或信息变化先修改 registry.json；不直接手改 CATALOG 的统计。
- 不自动把静态扫描通过提升为运行通过。
- 依赖关键词只是线索，保留行号便于回看。
- 修改原技能前记录原因、上游版本和差异；当前哈希检查有意阻止静默修改。
- 原许可审计保留为来源记录，新的复核结论单独追加证据。

## 扫描边界

脚本扫描明确 Markdown 文件链接，以及 scripts/references/templates 中可识别的文件名；不执行技能，不解析所有动态路径，不连接外部服务，也不证明法律许可或输出质量。

原文件基线保存在 docs/audit/original-sha256.json。原始完整备份位于仓库外，避免混入未来发布包。

## 试用包验证与构建

```bash
python3 -m unittest discover -s tests -v
python3 scripts/build_release.py
```

release.json 固定本次选择和原技能文件哈希。打包器只纳入三项、安装器、必要许可和实测材料，不把全部目录装进 Agent。生成 ZIP 和 SHA256 到 dist/，不自动上传。

更换选择或更新上游后，先重新运行测试，再更新 release.json 哈希。严禁只为让检查通过而静默刷新基线。

静态检查还要求 CATALOG 每个条目只出现一次，避免分组生成重复。
