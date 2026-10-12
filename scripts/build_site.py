#!/usr/bin/env python3
from pathlib import Path
import shutil
root=Path(__file__).resolve().parents[1]
out=root/'dist/site'
if out.exists(): shutil.rmtree(out)
shutil.copytree(root/'examples',out,ignore=shutil.ignore_patterns('historical','*-checks.json','checks.json','source-manifest.json'))
(out/'index.html').write_text('<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta http-equiv="refresh" content="0;url=reference-replicas/index.html"><title>OpenDesign 中文案例</title><a href="reference-replicas/index.html">进入案例集</a></html>')
(out/'.nojekyll').touch()
print(out)
