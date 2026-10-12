#!/usr/bin/env python3
"""Build the selected preview package with stable ZIP metadata and SHA256."""
import hashlib
import json
import zipfile
from pathlib import Path
from install import hashes
ROOT=Path(__file__).resolve().parents[1]

def main():
    release=json.loads((ROOT/'release.json').read_text())
    if release['status']!='explicit_path_trial_preview':raise SystemExit('Release is not ready for preview packaging')
    paths={'release.json','LICENSE','NOTICE','scripts/install.py','docs/installation.md','docs/validation-results.md','docs/audit/upstream/selected-source-check.json','docs/audit/upstream/selected-resources.json','tests/test_install.py'}
    for name,item in release['skills'].items():
        source=ROOT/item['source']
        if hashes(source)!=item['files']:raise SystemExit(f'Source drift: {name}')
        paths.update(str(f.relative_to(ROOT)) for f in source.rglob('*') if f.is_file())
    paths.update(str(f.relative_to(ROOT)) for f in (ROOT/'examples/validation-20261012').rglob('*') if f.is_file())
    readme='''# OpenDesign 中文设计技能试用包

版本：0.1.0-preview.2。包含 faq-page、resume-modern、reference-design-contract。

## 安装

需要 Python 3.9+ 和可读写本地文件的 Agent。在本目录打开终端：

```bash
mkdir -p ../my-design-project
python3 scripts/install.py install --skill faq-page --project ../my-design-project --agent codex
```

然后在该项目的 Agent 中明确要求读取 `.agents/skills/faq-page/SKILL.md`，提供 DESIGN.md 和问答材料，要求保存 index.html。当前测试走的是显式读取流程，不承诺自动发现或 Claude 执行。

其他技能 ID：resume-modern、reference-design-contract。安装器不会覆盖已有目录；更新、卸载与实际任务示例见 [使用说明](docs/installation.md)。

## 证据与边界

[实测记录和预览](docs/validation-results.md)。当前 Codex 会话完成虚构任务及修改，未在独立新会话测试；不代表跨模型稳定性。简历本例最终为 A4 单页，自己的内容仍需重新检查。

examples 下是本项目实测，skills 下 example 文件属于上游示例。上游原文和原许可保留；本包只含三项，完整导航里的简介、外链与其他未测试项没有打包。

[LICENSE](LICENSE) · [NOTICE](NOTICE)
'''
    content={'README.md':readme.encode()}
    for name in sorted(paths):
        f=ROOT/name
        if f.is_symlink():raise SystemExit(f'Refusing symlink: {name}')
        content[name]=f.read_bytes()
    checksums=''.join(hashlib.sha256(b).hexdigest()+'  '+name+'\n' for name,b in sorted(content.items()))
    content['SHA256SUMS.txt']=checksums.encode()
    folder='open-design-skills-zh-'+release['version']
    dist=ROOT/'dist';dist.mkdir(exist_ok=True);out=dist/(folder+'.zip')
    with zipfile.ZipFile(out,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for name,data in sorted(content.items()):
            info=zipfile.ZipInfo(folder+'/'+name,date_time=(2026,10,12,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o100644<<16
            z.writestr(info,data)
    digest=hashlib.sha256(out.read_bytes()).hexdigest()
    (dist/(out.name+'.sha256')).write_text(digest+'  '+out.name+'\n')
    print(json.dumps({'file':str(out),'bytes':out.stat().st_size,'sha256':digest,'entries':len(content)},ensure_ascii=False))
if __name__=='__main__':main()
