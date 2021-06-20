from pathlib import Path

PACKAGE_DIR = Path(__file__).parent

APPLESCRIPT_LAUNCHER = 'osascript'
APPLESCRIPT_NAME = 'findersel.applescript'
APPLESCRIPT_PATH = PACKAGE_DIR / 'scripts' / APPLESCRIPT_NAME
