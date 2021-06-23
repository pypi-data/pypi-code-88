import logging

from logging.handlers import TimedRotatingFileHandler

from better_log.handler import ColorHandler


logger = logging.getLogger(__name__)
_formatter = '%(asctime)s - %(levelname)s "%(pathname)s:%(lineno)s":%(funcName)s() - %(message)s'


def set_logger(level=logging.INFO):
    _logger = logging.getLogger(__name__)
    _logger.setLevel(level)

    color_handler = ColorHandler()
    color_handler.setFormatter(logging.Formatter(_formatter))
    color_handler.setLevel(level)

    _logger.addHandler(color_handler)

    return _logger


def remove_all_handlers():
    global logger

    # Remove all handlers on exiting logger
    if logger:
        for handler in list(logger.handlers):
            logger.removeHandler(handler)


def reset_default_logger():
    """
    Resets the internal default logger to the initial configuration
    """
    global logger
    # Remove all handlers on exiting logger
    remove_all_handlers()

    # Resetup
    logger = set_logger()


reset_default_logger()


def set_time_rotating_file_logger(file, when, interval, backupCount, atTime, level=logging.INFO, only_handler=True):
    global logger
    _logger = logging.getLogger(__name__)
    rf_handler = _generate_rf_handler(
        file,
        when,
        interval,
        backupCount,
        atTime,
        level
    )
    if only_handler:
        remove_all_handlers()
    _logger.addHandler(rf_handler)
    logger = _logger


def _generate_rf_handler(file, when, interval, backupCount, atTime, level=logging.INFO):
    rf_handler = TimedRotatingFileHandler(
        file,
        when=when,
        interval=interval,
        backupCount=backupCount,
        atTime=atTime
    )
    rf_handler.setFormatter(
        logging.Formatter(_formatter))
    rf_handler.setLevel(level)
    return rf_handler

