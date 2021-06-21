__version__ = '0.1.8'

import logging
import cleanlog.formatter as cf
import cleanlog.handler as ch

# Integer representation of level names.
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0


def BasicLogger(name=None, tqdm=False, *args, **kwargs):
    """
    """
    logger = logging.getLogger(name)
    if not tqdm:
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(cf.BasicFormatter())
        logger.addHandler(stream_handler)

    else:
        tqdm_handler = ch.TqdmHandler()
        tqdm_handler.setFormatter(cf.BasicFormatter())
        logger.addHandler(tqdm_handler)

    return logger

def ColoredLogger(name=None, tqdm=False, time=False, *args, **kwargs):
    """
    """
    logger = logging.getLogger(name)
    if not tqdm:
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(cf.ColoredFormatter(time=time))
        logger.addHandler(stream_handler)

    else:
        tqdm_handler = ch.TqdmHandler()
        tqdm_handler.setFormatter(cf.ColoredFormatter(time=time))
        logger.addHandler(tqdm_handler)

    return logger


# Wrap logging.getLogger just for convenience.
getLogger = logging.getLogger

# Aliases.
basic_logger = BasicLogger
colored_logger = ColoredLogger
