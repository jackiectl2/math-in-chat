#!/usr/bin/env python3
"""Install this repository's Claude Code and Codex skills into a course repo.

Existing identical copies are left alone. Different files are never overwritten.
"""

import argparse
from pathlib import Path
import shutil


def files(root):
    return {
        str(p.relative_to(root)): p.read_bytes()
        for p in root.rglob('*')
        if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc'
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--target', required=True, type=Path, help='Existing course repository directory')
    args = parser.parse_args()
    target = args.target.resolve()
    if not target.is_dir():
        parser.error('Target must be an existing directory')
    repository = Path(__file__).resolve().parents[1]
    pending = []
    for platform in ('.claude', '.agents'):
        source_root = repository / platform / 'skills'
        for source in sorted(source_root.iterdir()):
            if not (source / 'SKILL.md').is_file():
                continue
            destination = target / platform / 'skills' / source.name
            for parent in (destination, *destination.parents):
                if parent == target:
                    break
                if parent.is_symlink():
                    parser.error(f'Refusing symlink destination: {parent}')
            if destination.exists():
                if not destination.is_dir() or files(source) != files(destination):
                    parser.error(f'Existing skill differs; compare manually before updating: {destination}')
                print(f'Already installed: {destination}')
            else:
                pending.append((source, destination))
    # Check every destination before copying any files.
    for source, destination in pending:
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(source, destination, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
        print(f'Installed: {destination}')
    print('Native skill folders are ready. Start/reload the client as required for skill discovery.')


if __name__ == '__main__':
    main()
