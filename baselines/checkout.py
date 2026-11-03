#!/usr/bin/env python3
"""Check out a pinned Flare Core source baseline into a new directory."""
import argparse
import json
import os
import re
import subprocess
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('manifest', type=Path)
    parser.add_argument('destination', type=Path)
    args = parser.parse_args()

    manifest = json.loads(args.manifest.read_text())
    if manifest.get('schema_version') != 1 or manifest.get('status') != 'source-baseline':
        parser.error('expected a v1 source baseline')
    entries = manifest['repositories']
    seen = set()
    for row in entries:
        name = row['directory']
        if (
            not re.fullmatch(r'flare-[a-z0-9-]+', name)
            or name in seen
            or row['repository'] != f'https://github.com/flare-im/{name}.git'
            or not re.fullmatch(r'[0-9a-f]{40}', row['revision'])
        ):
            parser.error(f'invalid or duplicate repository entry: {name!r}')
        seen.add(name)
    if not seen:
        parser.error('a source baseline must contain repositories')
    args.destination.mkdir()

    # Use public HTTPS only, even if the local Git installation has credentials.
    env = {k: v for k, v in os.environ.items() if not k.startswith('GIT_')}
    env.update(GIT_CONFIG_NOSYSTEM='1', GIT_CONFIG_GLOBAL=os.devnull, GIT_TERMINAL_PROMPT='0')
    for row in entries:
        name, url, revision = row['directory'], row['repository'], row['revision']
        path = args.destination / name
        path.mkdir()
        git = ['git', '-c', 'http.version=HTTP/1.1', '-C', str(path)]
        subprocess.run(git + ['init', '--quiet'], env=env, check=True)
        subprocess.run(git + ['remote', 'add', 'origin', url], env=env, check=True)
        subprocess.run(git + ['fetch', '--quiet', '--depth', '1', 'origin', revision], env=env, check=True)
        subprocess.run(git + ['checkout', '--quiet', '--detach', 'FETCH_HEAD'], env=env, check=True)
        actual = subprocess.check_output(git + ['rev-parse', 'HEAD'], env=env, text=True).strip()
        if actual != revision:
            raise SystemExit(f'{name}: checked out {actual}, expected {revision}')
        print(f'{name} {actual}', flush=True)
    print(f"Verified {len(seen)} anonymous source checkouts for {manifest['id']}")


if __name__ == '__main__':
    main()
