import logging
from importlib import import_module
from pkgutil import iter_modules


def walk_modules(path: str):
    mods = []
    mod = import_module(path)
    mods.append(mod)
    if hasattr(mod, '__path__'):
        for _, subpath, ispkg in iter_modules(mod.__path__):
            fullpath = path + '.' + subpath
            if ispkg:
                mods += walk_modules(fullpath)
            else:
                submod = import_module(fullpath)
                mods.append(submod)
    return mods


LOG_FORMAT = '%(asctime)s [%(process)d] [%(levelname)s] %(message)s'
LOG_DATEFMT = '[%Y-%m-%d %H:%M:%S %z]'


def configure_logger(name: str, log_level: str):
    log_level = log_level.upper()
    logger = logging.getLogger(name)
    handler = logging.StreamHandler()
    handler.setLevel(log_level)
    formatter = logging.Formatter(LOG_FORMAT, LOG_DATEFMT)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(log_level)
    logger.propagate = False
