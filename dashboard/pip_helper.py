import argparse
import os
import subprocess
import sys

import yaml


def read_config(config_file):
    return yaml.safe_load(config_file)


def pip_install(deps, dest_dir, constraints_file):
    args = [sys.executable, '-m', 'pip', 'install',
            '-c', constraints_file, '--src', dest_dir] + deps
    print(' '.join(args))
    subprocess.check_call(args)


# Do a pip install from either Git or from an existing directory.
def install(config, dest_dir, constraints_file):
    deps = []
    for repo in config.get('repos', []):
        name = repo['name']
        path = os.path.join(dest_dir, name)
        if os.path.exists(path):
            if not path.startswith('/'):
                path = './' + path
            requirement = path
        else:
            requirement = get_git_requirement_string(config, repo)
        deps.extend(['-e', requirement])

    if deps:
        pip_install(deps, dest_dir, constraints_file)


def get_git_requirement_string(config, repo):
    template = 'git+{src}@{branch}#egg={name}'
    defaults = config.get('default-branches', {})
    default_branches = [
        default for match, default in defaults.items()
        if match in repo['src']]
    if default_branches:
        repo.setdefault('branch', default_branches[0])
    return template.format(**repo)


if __name__ == '__main__':
    description="""Manage Pip installs for development environments.

Clones repos using a git+ requirements string if the directory doesn't
exist already.

Any existing directories are used as-is and installed using `pip -e ./project`."""

    parser = argparse.ArgumentParser(
        description=description,
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument('config', type=argparse.FileType('r'),
                        help='Path to repo config file.')
    parser.add_argument('destdir',
                        help='Directory for repositories.')
    parser.add_argument('constraints',
                        help='Path to constraints file.')
    args = parser.parse_args()
    config = read_config(args.config)
    install(config, args.destdir, args.constraints)
