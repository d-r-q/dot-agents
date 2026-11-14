import subprocess
from pathlib import Path
from session_context import collect


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


def test_non_git_ancestors_and_all_names(tmp_path):
    write(tmp_path / 'a.personal.md', 'parent')
    write(tmp_path / 'child' / 'b.local.md', 'child')
    write(tmp_path / 'child' / 'hidden' / 'c.local.md', 'unrelated')
    files = collect(tmp_path / 'child', tmp_path / 'config')
    assert [c for _, p, c in files if p.is_relative_to(tmp_path)] == ['parent', 'child']


def test_worktree_fallback_and_individual_override(tmp_path):
    root = tmp_path / 'main repo'
    root.mkdir()
    def git(*args):
        subprocess.run(['git', '-C', str(root), *args], check=True, capture_output=True)
    git('init')
    git('-c', 'user.name=Test', '-c', 'user.email=test@example.invalid', 'commit', '--allow-empty', '-m', 'initial')
    wt = tmp_path / 'work tree'
    git('worktree', 'add', '-b', 'task', str(wt))
    write(root / 'a.personal.md', 'fallback')
    write(root / 'b.local.md', 'main')
    write(wt / 'b.local.md', 'override')
    write(root / 'module' / 'c.personal.md', 'nested fallback')
    (wt / 'module').mkdir()
    files = collect(wt / 'module', tmp_path / 'config')
    assert [c for _, p, c in files if p.is_relative_to(tmp_path)] == ['fallback', 'override', 'nested fallback']
    assert next(scope for scope, _, c in files if c == 'nested fallback') == wt / 'module'


def test_global_symlink_dedup_and_scope(tmp_path):
    config = tmp_path / 'config'
    shared = tmp_path / 'shared'
    write(shared / 'AGENTS.md', '')
    write(shared / 'one.personal.md', 'global')
    config.mkdir()
    (config / 'AGENTS.md').symlink_to(shared / 'AGENTS.md')
    (config / 'one.personal.md').symlink_to(shared / 'one.personal.md')
    assert [(scope, c) for scope, _, c in collect(tmp_path, config) if c == 'global'] == [('вся сессия', 'global')]
