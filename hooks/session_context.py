#!/usr/bin/env python3
"""Загрузка персонального и машинного контекста с fallback в основной ворктри."""
import json
import os
from pathlib import Path
import subprocess
import sys


def main_worktree(cwd):
    def git(*args):
        return subprocess.check_output(
            ['git', '-C', str(cwd), *args], stderr=subprocess.DEVNULL,
            timeout=5,
        ).decode().strip()
    try:
        root = Path(git('rev-parse', '--show-toplevel'))
        records = git('worktree', 'list', '--porcelain', '-z').split('\0')
        main = Path(next(r[9:] for r in records if r.startswith('worktree ')))
        return root, main
    except (subprocess.SubprocessError, StopIteration):
        return None, None


def collect(cwd, config_home):
    cwd = cwd.resolve()
    root, main = main_worktree(cwd)
    global_dir = (config_home / 'AGENTS.md').resolve().parent
    directories = [global_dir, config_home, *reversed(cwd.parents), cwd]
    seen = set()
    result = []
    for directory in directories:
        fallback = None
        if root and directory.is_relative_to(root):
            fallback = main / directory.relative_to(root)
        for suffix in ('personal', 'local'):
            selected = {}
            for location in (fallback, directory):
                if location and location.is_dir():
                    selected.update({p.name: p for p in location.glob(f'*.{suffix}.md') if p.is_file()})
            for name, path in sorted(selected.items()):
                resolved = path.resolve()
                if resolved in seen:
                    continue
                seen.add(resolved)
                scope = 'вся сессия' if directory in (global_dir, config_home) else directory
                result.append((scope, resolved, path.read_text()))
    return result


def render(files):
    if not files:
        return ''
    header = ('Дополнительный контекст сессии. В каждой области *.personal.md имеет '
              'приоритет над AGENTS.md, а *.local.md — над *.personal.md. '
              'Более узкая область имеет приоритет над родительской. '
              'Относительные пути разрешай относительно исходного файла.\n')
    return header + ''.join(
        f'\n## Источник: {path}\nОбласть действия: {scope}\n\n{content}\n'
        for scope, path, content in files
    )


def main():
    event = json.load(sys.stdin)
    config = Path(os.environ.get('CODEX_HOME', str(Path.home() / '.codex'))).expanduser()
    context = render(collect(Path(event['cwd']), config))
    print(json.dumps({'hookSpecificOutput': {
        'hookEventName': event.get('hook_event_name', 'SessionStart'),
        'additionalContext': context,
    }}, ensure_ascii=False))


if __name__ == '__main__':
    main()
