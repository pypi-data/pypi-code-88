from .core import Core, CoreProvider
from .logger import Logger
from .utils import random_crid

__author__ = "Guo Y.K. <hi@guoyk.net>"
__version__ = "1.0.0"
__all__ = [
    "setup",
    "default_logger",
    "create_logger",
    "event",
    "topic",
    "job",
    "log",
    "debug",
    "info",
    "warn",
    "error",
    "fatal",
    "random_crid",
]

_core_provider: CoreProvider = CoreProvider()
_core_provider.core = Core(None)

default_logger = Logger(_core_provider)


def setup(opts: dict):
    _core_provider.core = Core(opts)


def create_logger() -> Logger:
    """
    创建一个独立的 Logger，用于自定义 crid, extra 和 keyword

    :return:
    """
    return Logger(_core_provider)


event = default_logger.event

topic = default_logger.topic

job = default_logger.job

log = default_logger.log

debug = default_logger.debug

info = default_logger.info

warn = default_logger.warn

error = default_logger.error

fatal = default_logger.fatal
