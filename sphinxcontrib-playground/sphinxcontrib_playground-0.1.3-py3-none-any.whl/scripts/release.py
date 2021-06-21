import json
import subprocess
import sys

import koloro

try:
  from semver import VersionInfo
except ImportError:
  raise ImportError(
    'semver must be installed for release. `pip install semver`'
  )


RELEASE_TYPES = ('major', 'minor', 'patch', 'prerelease')

run = subprocess.call


def main():
  pre_id = sys.argv[1] if len(sys.argv) > 1 else 'rc'

  print('Release types are: ', RELEASE_TYPES)
  idx = int(input('Select release type (index): '))

  with open('package.json', 'r') as f:
    VERSION = json.load(f)['version']

  target_version = str(
    VersionInfo.parse(VERSION).next_version(RELEASE_TYPES[idx], pre_id)
  )

  if not VersionInfo.isvalid(target_version):
    raise ValueError(f'Invalid target version: {target_version}')

  tag = f'v{target_version}'

  yes = input(f'Releasing {tag}. Confirm? [y/N] ').lower()
  if yes in ('yes', 'y'):
    yes = True
  elif yes in ('no', 'n'):
    yes = False
  else:
    yes = False

  if not yes:
    return

  print(koloro.cyan('Updating package version...'))
  with open('package.json', 'r') as f:
    pkg = json.load(f)
    pkg['version'] = target_version

  with open('package.json', 'w') as f:
    json.dump(pkg, f)

  print(koloro.cyan('Generating changelog...'))
  run(['pnpm', 'changelog'])

  print(koloro.cyan('Formatting...'))
  run(['pnpm', 'fmt'])

  changelogOk = input('Changelog generated. Does it look good? [y/N] ').lower()

  if changelogOk in ('yes', 'y'):
    changelogOk = True
  elif changelogOk in ('no', 'n'):
    changelogOk = False
  else:
    changelogOk = False

  if not changelogOk:
    return

  print(koloro.cyan('Committing changes...'))
  run(['git', 'add', '.'])
  run(['git', 'commit', '-m', f'release: {tag}'])

  print(koloro.cyan('Pushing to GitHub...'))
  run(['git', 'tag', tag])
  run(['git', 'push', 'origin', tag])
  run(['git', 'push', '-u', 'origin', 'main'])


if __name__ == '__main__':
  main()
