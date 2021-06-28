import sys

VERSION = '0.2.4'

if sys.version_info < (3, 0):
    from config import Config
else:
    from .config import Config
