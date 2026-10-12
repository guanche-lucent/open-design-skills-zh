#!/usr/bin/env python3
"""Offline checks and generated docs; never installs or executes bundled skills."""
import argparse
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
FORM = {'bundled_content': '附带正文', 'stub': '仅简介', 'external_link': '仅外链'}

def scan(item):
    entry = item['local_entry']
    if entry is None:
        return {'status': 'not_applicable', 'missing_references': [], 'scanned_documents': 0}
    base = (ROOT / entry).parent
    missing = []
    documents = list(base.rglob('*.md'))
    for doc in sorted(documents):
        text = doc.read_text()
        for no, line in enumerate(text.splitlines(), 1):
            # Explicit Markdown file links. Skip URLs and anchors. These are leads,
            # not a claim that each target is a required bundled dependency.
            refs = set(re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', line))
            # Include command examples: checking only Markdown links misses scripts.
            refs.update(re.findall(r'(?<![\w/-])(?:scripts|references|templates)/[\w./-]+\.(?:py|mjs|js|sh|md|json|html)\b', line))
            for ref in sorted(refs):
                if re.match(r'[a-zA-Z][\w+.-]*:', ref) or ref.startswith(('#','/')):
                    continue
                if any(c in ref for c in '<>{}*$') or '/xxx.' in ref:
                    continue
                target = unquote(ref.split('#')[0])
                if not target:
                    continue
                # Commands normally resolve from skill root; Markdown links from doc.
                exists = (doc.parent / target).exists() or (base / target).exists()
                if not exists:
                    missing.append({'file':str(doc.relative_to(ROOT)), 'line':no, 'target':ref,
                                    'context':line.strip()[:240]})
    return {'status':'needs_review' if missing else 'no_missing_in_scanned_patterns',
            'missing_references':missing,'scanned_documents':len(documents)}

def generate():
    data=json.loads((ROOT/'registry.json').read_text()); items=data['items']; errors=[]
    ids=[x['id'] for x in items]
    if len(ids)!=len(set(ids)):errors.append('Duplicate skill IDs')
    actual={str(f.relative_to(ROOT)) for f in (ROOT/'skills').rglob('SKILL.md')}
    declared={x['local_entry'] for x in items if x['local_entry']}
    if actual!=declared:errors.append(f'Local entry mismatch: {sorted(actual^declared)}')
    baseline=json.loads((ROOT/'docs/audit/original-sha256.json').read_text())
    protected={n:h for n,h in baseline.items() if n.startswith('skills/') or n in ['NOTICE','LICENSE','LICENSE-AUDIT.md']}
    changed=[n for n,h in protected.items() if not (ROOT/n).is_file() or hashlib.sha256((ROOT/n).read_bytes()).hexdigest()!=h]
    if changed:errors.append('Original source changed: '+', '.join(changed))
    findings={x['id']:scan(x) for x in items}
    counts=Counter(x['content_form'] for x in items)
    stats=f"共 **{len(items)} 项**：**{counts['bundled_content']} 项附带正文**、**{counts['stub']} 项仅简介**、**{counts['external_link']} 项仅外链**。其中 **{sum(x['runtime_validation']['status']=='explicit_path_trial_passed' for x in items)} 项完成当前会话显式读取试用**；其余未运行验证。自动发现与跨平台执行另行验证。"
    cat=['# 设计技能完整目录','',stats,'','按任务浏览：[场景导航](docs/scenarios.md) · [状态解释与限制](docs/compatibility.md) · [静态核查](docs/audit/asset-audit.md)','',
         '> 此文件由 registry.json 生成。附带正文不代表资源完全齐备、能独立运行或已验证许可。依赖列继承原目录；“待确认”不是免费或无依赖。','']
    categories=list(dict.fromkeys(x['category'] for x in items))
    cat.extend(f"- [{next(x['category_zh'] for x in items if x['category']==c)}](#{c})" for c in categories)
    for c in categories:
        group=[x for x in items if x['category']==c]
        cat += ['',f'<a id="{c}"></a>',f"## {group[0]['category_zh']}（{len(group)}）",'']
        for sub in dict.fromkeys(x['subcategory'] for x in group):
            cat += [f'### {sub}','','| 技能 | 用途 | 包内内容 | 静态检查 | 服务依赖（原目录） | 许可声明 | 运行记录 |','|---|---|---|---|---|---|---|']
            for x in group:
                if x['subcategory'] != sub:
                    continue
                target=x['local_entry'] or x['source']['upstream_url'] or x['source']['opendesign_url']
                result=findings[x['id']]
                status='待复核引用' if result['missing_references'] else ('非完整技能' if x['content_form']=='stub' else ('不适用' if not x['local_entry'] else '未检出缺失*'))
                dep=x['dependency']['catalog_declaration'];dep='待确认' if dep=='—' else dep
                cat.append(f"| [{x['name_zh']} · `{x['id']}`]({target}) | {x['summary_zh']} | {FORM[x['content_form']]} | {status} | {dep} | {x['license']['declared']} | {'[显式试用](docs/validation-results.md)' if x['runtime_validation']['status']=='explicit_path_trial_passed' else '未测试'} |")
    cat += ['','\* 仅覆盖明确 Markdown 本地链接和 scripts/references/templates 文件路径；不证明运行依赖齐全。全部运行状态见 registry.json。','']
    if sum(line.startswith('| [') for line in cat) != len(items):
        errors.append('Catalog must list each skill exactly once')
    outputs={'CATALOG.md':'\n'.join(cat)}
    report=['# 本地资产核查','',f"核查日期：{data['as_of']}。范围：本地文件、目录口径、明确资源引用；未执行技能，也未逐一访问上游。",'',stats,'',
            f"- 本地技能入口：{len(actual)}。",f"- 原始文件快照：{len(baseline)} 个文件。",f"- 受保护原文、资源与许可文件：{len(protected)} 个；哈希变化：{len(changed)}。",
            f"- 明确引用待复核：{sum(bool(v['missing_references']) for v in findings.values())} 个技能。",'','## 引用待复核','',
            '以下为静态扫描线索，需要区分缺失依赖、运行产物和示例路径；不能把命中数量当作缺陷数量。','']
    for x in items:
        result=findings[x['id']]
        if result['missing_references']:
            report += [f"### {x['id']}",'']
            seen=set()
            for r in result['missing_references']:
                if r['target'] in seen:continue
                seen.add(r['target'])
                report += [f"- `{r['target']}`：[{r['file']}:{r['line']}](../../{r['file']})"]
            report.append('')
    report += ['## 人工核查补充','']
    for x in items:
        for note in x['review_notes']:report.append(f"- **{x['id']}**：{note}")
    report += ['','## 边界','',
               '- 许可信息沿用原 LICENSE-AUDIT，不代表本轮完成上游许可复核。',
               '- 依赖信号按正文关键词提取并保留行号，只能帮助定位，不能当作最终依赖清单。',
               '- hatch-pet 的 canonical-base.png 与 layout-guides 是正文说明的运行产物，不属于静态漏打包。',
               '- ui-ux-pro-max 的 search.py 属于其明确未附带的上游完整实现；已标仅简介。',
               '- 自动化结果见 asset-audit.json；人工判断与后续任务见 review.md。','']
    outputs['docs/audit/asset-audit.md']='\n'.join(report)
    outputs['docs/audit/asset-audit.json']=json.dumps({'date':data['as_of'],'counts':dict(counts),'errors':errors,'source_changes':changed,'findings':findings},ensure_ascii=False,indent=2)+'\n'
    readme=ROOT/'README.md'
    if '<!-- stats:start -->' in readme.read_text():
        outputs['README.md']=re.sub(r'<!-- stats:start -->.*?<!-- stats:end -->',f'<!-- stats:start -->\n{stats}\n<!-- stats:end -->',readme.read_text(),flags=re.S)
    return outputs,errors

def check_links():
    errors=[]
    # Maintained navigation only: upstream documents have contextual/runtime refs.
    docs=[ROOT/'README.md',ROOT/'CATALOG.md',ROOT/'SKILL.md',*list((ROOT/'docs').rglob('*.md'))]
    for f in docs:
        for ref in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)',f.read_text()):
            if re.match(r'[a-zA-Z][\w+.-]*:',ref) or ref.startswith('#'):continue
            if not (f.parent/unquote(ref.split('#')[0])).exists():errors.append(f'{f.relative_to(ROOT)}: broken link {ref}')
    return errors

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true',help='Verify without writing'); args=parser.parse_args()
    outputs,errors=generate()
    for name,content in outputs.items():
        f=ROOT/name
        if args.check:
            if not f.exists() or f.read_text()!=content:errors.append(f'Generated file stale: {name}')
        else:f.write_text(content)
    errors+=check_links()
    if errors:raise SystemExit('\n'.join(errors))
    print('PASS: registry, generated files, protected source hashes and navigation links')
