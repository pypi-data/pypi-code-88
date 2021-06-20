from pathlib import Path

from prettyconf import config

PACKAGE_DIR = Path(__file__).parent

APPLESCRIPT_LAUNCHER = config('APPLESCRIPT_LAUNCHER', default='osascript')
APPLESCRIPT_NAME = config('APPLESCRIPT_NAME', default='findersel.applescript')
APPLESCRIPT_PATH = PACKAGE_DIR / 'scripts' / APPLESCRIPT_NAME
