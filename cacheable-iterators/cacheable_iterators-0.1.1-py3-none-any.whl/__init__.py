"""
.. include:: ../../README.md
"""

from collections import namedtuple

__title__ = 'cacheable-iterators'
__author__ = 'Peter Zaitcev / USSX Hares'
__license__ = 'BSD 2-clause'
__copyright__ = 'Copyright 2021 Peter Zaitcev'
__version__ = '0.1.1'

VersionInfo = namedtuple('VersionInfo', 'major minor micro releaselevel serial')
version_info = VersionInfo(*__version__.split('.'), releaselevel='alpha', serial=0)

from .core import *

__all__ = \
[
    'version_info',
    '__title__',
    '__author__',
    '__license__',
    '__copyright__',
    '__version__',
    *core.__all__,
]

__pdoc__ = { k: False for k in core.__all__ }
