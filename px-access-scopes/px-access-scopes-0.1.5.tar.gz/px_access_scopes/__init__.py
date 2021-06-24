__version__ = '0.1.5'

VERSION = tuple(__version__.split('.'))

from .scopes import *
from .aggregates import *
from .checkers import *
from .exceptions import *
from .export import *
