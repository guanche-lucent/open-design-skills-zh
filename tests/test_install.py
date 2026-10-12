import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.project=Path(self.temp.name);self.skill='resume-modern';self.target=self.project/'.agents/skills'/self.skill
    def tearDown(self):self.temp.cleanup()
    def run_cli(self,action,ok=True,skill=None,agent='codex'):
        p=subprocess.run([sys.executable,str(ROOT/'scripts/install.py'),action,'--skill',skill or self.skill,'--project',str(self.project),'--agent',agent],capture_output=True,text=True)
        self.assertEqual(p.returncode==0,ok,p.stdout+p.stderr);return p
    def test_install_update_uninstall_preserves_project(self):
        output=self.project/'my-output.txt';output.write_text('user work')
        self.run_cli('install');self.assertTrue((self.target/'SKILL.md').exists());self.assertTrue((self.target/'BUNDLE-LICENSE.txt').exists())
        self.run_cli('update');self.assertEqual(len(list((self.project/'.ods-backups').iterdir())),1)
        self.run_cli('uninstall');self.assertFalse(self.target.exists());self.assertEqual(output.read_text(),'user work')
    def test_existing_unmanaged_directory_is_not_overwritten(self):
        self.target.mkdir(parents=True);(self.target/'user.txt').write_text('original')
        self.run_cli('install',ok=False);self.run_cli('update',ok=False);self.assertEqual((self.target/'user.txt').read_text(),'original')
    def test_edited_skill_cannot_be_updated_or_removed(self):
        self.run_cli('install');(self.target/'SKILL.md').write_text('user edit')
        self.run_cli('update',ok=False);self.run_cli('uninstall',ok=False);self.assertEqual((self.target/'SKILL.md').read_text(),'user edit')
    def test_unknown_and_traversal_ids_are_rejected(self):
        self.run_cli('install',ok=False,skill='../../escape');self.run_cli('install',ok=False,skill='ui-ux-pro-max')
    def test_destination_symlink_is_rejected(self):
        outside=self.project/'outside';outside.mkdir();(self.project/'.agents').symlink_to(outside,target_is_directory=True)
        self.run_cli('install',ok=False);self.assertEqual(list(outside.iterdir()),[])
    def test_claude_directory_layout_only(self):
        self.run_cli('install',agent='claude');self.assertTrue((self.project/'.claude/skills/resume-modern/SKILL.md').exists())
    def test_added_user_file_is_preserved(self):
        self.run_cli('install');(self.target/'my-note.md').write_text('keep')
        self.run_cli('uninstall',ok=False);self.assertEqual((self.target/'my-note.md').read_text(),'keep')
if __name__=='__main__':unittest.main(verbosity=2)
