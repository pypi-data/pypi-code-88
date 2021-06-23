"""Common code"""
from .discord_common import make_embed, error_embed
from .database import build_database_url
from .make_logger import make_logger
from .check_update import check_update

__version__ = "0.0.2"

__all__ = [
    "__version__",
    "make_logger",
    "make_embed",
    "error_embed",
    "build_database_url",
    "check_update",
]
