#!/usr/bin/env python3
"""Install one preview skill into a project; no downloads or global changes."""
import argparse
import hashlib
import json
import os
import shutil
import tempfile
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKER = '.ods-install.json'

def hashes(folder):
    result={}
    for p in sorted(folder.rglob('*')):
        if p.is_symlink():raise ValueError(f'Symlink not supported: {p}')
        if p.is_file() and p != folder / MARKER:
            result[p.relative_to(folder).as_posix()]=hashlib.sha256(p.read_bytes()).hexdigest()
    return result

def assert_managed(target):
    receipt=target/MARKER
    if not receipt.is_file():raise ValueError('Directory not managed by this installer; refusing to replace/remove it')
    data=json.loads(receipt.read_text())
    if data.get('manager')!='open-design-skills-zh':raise ValueError('Unrecognized installation receipt')
    if hashes(target)!=data['files']:raise ValueError('Installed files were edited; back up/move the folder yourself before updating/removing')

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action',choices=['list','install','update','uninstall'])
    parser.add_argument('--skill');parser.add_argument('--project',type=Path)
    parser.add_argument('--agent',choices=['codex','claude'],default='codex')
    args=parser.parse_args()
    release=json.loads((ROOT/'release.json').read_text())
    if args.action=='list':
        print(json.dumps(release,ensure_ascii=False,indent=2));return
    if not args.skill or args.skill not in release['skills']:raise ValueError('Choose a skill from the list command')
    if not args.project:raise ValueError('--project is required; global installation is not the default')
    project=args.project.expanduser().resolve()
    if not project.is_dir():raise ValueError('Project directory must already exist')
    agentroot=project/('.agents' if args.agent=='codex' else '.claude')
    base=agentroot/'skills';target=base/args.skill
    for path in [agentroot,base,target]:
        if path.is_symlink():raise ValueError(f'Refusing symlink destination: {path}')
    if args.action=='install' and target.exists():raise ValueError('Skill already exists; use update for managed, unchanged installs')
    if args.action in ['update','uninstall']:
        if not target.is_dir():raise ValueError('Skill is not installed here')
        assert_managed(target)
    if args.action=='uninstall':
        shutil.rmtree(target);print(f'Removed {target}; project output files untouched');return
    rel=release['skills'][args.skill]['source']
    source=(ROOT/rel).resolve()
    if ROOT.resolve() not in source.parents or not (source/'SKILL.md').is_file():raise ValueError('Invalid source directory')
    source_hashes=hashes(source)
    if source_hashes!=release['skills'][args.skill]['files']:raise ValueError('Source differs from release manifest; rebuild and validate the release first')
    base.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='.ods-stage-',dir=project) as temp:
        staged=Path(temp)/args.skill;shutil.copytree(source,staged)
        shutil.copy2(ROOT/'LICENSE',staged/'BUNDLE-LICENSE.txt')
        shutil.copy2(ROOT/'NOTICE',staged/'BUNDLE-NOTICE.txt')
        receipt={'manager':'open-design-skills-zh','version':release['version'],'skill':args.skill,'agent':args.agent,'files':hashes(staged)}
        (staged/MARKER).write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
        backup=None
        if args.action=='update':
            backups=project/'.ods-backups'
            if backups.is_symlink():raise ValueError('Refusing symlink backup directory')
            backups.mkdir(exist_ok=True)
            backup=backups/(args.skill+'-'+uuid.uuid4().hex[:12]);os.rename(target,backup)
        try:os.rename(staged,target)
        except Exception:
            if backup:os.rename(backup,target)
            raise
    print(f'Installed {target}')
    print('Open a new agent session in this project. Explicit-path execution was tested; automatic discovery needs separate verification.')
    if backup:print(f'Previous version backed up: {backup}')

if __name__=='__main__':
    try:main()
    except (ValueError,OSError,KeyError,json.JSONDecodeError) as error:raise SystemExit(str(error))
