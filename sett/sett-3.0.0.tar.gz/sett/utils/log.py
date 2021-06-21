import enum
import io
import logging
import logging.handlers
import platform
import time
from contextlib import contextmanager
from functools import wraps
from pathlib import Path
from typing import Callable, Tuple, Dict, cast, ContextManager, Optional

import colorama  # type: ignore

from .. import RUNTIME_INFO

LOG_FORMAT = "[%(levelname)s] %(message)s"
LOG_FORMAT_WITH_EMOJI = "%(levelname)s  %(message)s"
LOG_FORMAT_WITH_TIME = "[%(asctime)s] " + LOG_FORMAT

colorama.init()


class LogStyle(enum.Enum):
    EMOJI = enum.auto()
    TERMINAL = enum.auto()
    HTML = enum.auto()

    def get_style(self, log_level: int) -> Optional[str]:
        style = {
            LogStyle.EMOJI: {
                logging.DEBUG: "🔬",
                logging.INFO: "ℹ️",
                logging.WARNING: "⚠️",
                logging.ERROR: "💥",
                logging.CRITICAL: "☢️",
            },
            LogStyle.TERMINAL: {
                logging.WARNING: colorama.Fore.YELLOW,
                logging.ERROR: colorama.Fore.RED,
                logging.CRITICAL: colorama.Fore.RED,
            },
            LogStyle.HTML: {
                logging.DEBUG: "gray",
                logging.INFO: "black",
                logging.WARNING: "orange",
                logging.ERROR: "red",
                logging.CRITICAL: "red",
            },
        }
        return style[self].get(log_level)


class EmojiLevelFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord):
        emoji = LogStyle.EMOJI.get_style(record.levelno)
        if emoji:
            record.levelname = emoji
        return super().format(record)


class ColoredTerminalFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        color = LogStyle.TERMINAL.get_style(record.levelno)
        if color:
            return f"{color}{super().format(record)}{colorama.Fore.RESET}"
        return super().format(record)


@contextmanager
def log_task(
    message: str,
    ok_logger: Callable = logging.info,
    err_logger: Callable = logging.error,
):
    """Context manager / decorator that logs a user-defined message with level INFO upon
    entering the context manager, and either "OK" or "FAILED" upon exiting
    depending on whether exceptions occurred during its body or not.

    : param message: message to log with INFO level when entering the
        context manager.
    : param ok_logger: method associated with the logger level at which the
        message string should be logged. E.g. logging.info will log the message
        at the INFO level.
    : param err_logger: same as above but for logger level associated with
        errors.
    """
    ok_logger(message)
    try:
        yield None
    except Exception:
        err_logger("FAILED")
        raise
    ok_logger("OK")


def log_timing(logger):
    """A function decorator, logging processing time taken by the contained code"""

    def decorator(f):
        @wraps(f)
        def wrapped_f(*args, **kwargs):
            tic = time.perf_counter()
            r = f(*args, **kwargs)
            tac = time.perf_counter()
            logger.info(f"{f.__name__!r} took {sec_to_hours(int(tac - tic))}")
            return r

        return wrapped_f

    return decorator


def sec_to_hours(seconds: int) -> str:
    """Converts given seconds into something like '9h 36mn 38s'"""
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    start = 0 if h else 1 if m else 2
    return " ".join(
        f"{n}{u}" for n, u in zip((h, m, s)[start:], ("h", "m", "s")[start:])
    )


def log_runtime_info(logger: logging.Logger):
    """Logs:
    - application version
    - versions of the main dependencies
    - version of the operating system where the application is running
    """
    logger.info(RUNTIME_INFO)


class LoggerExt(logging.Logger):
    """Logger class with additional functionality"""

    def log_task(self, message: str) -> ContextManager:
        """A context manager to log a task which can potentially fail"""
        return log_task(message, ok_logger=self.info, err_logger=self.error)


logging.setLoggerClass(LoggerExt)


class StringIoHandler(logging.Handler):
    """Logging handler logging to a StringIo."""

    def __init__(self, *args, **kwargs):
        self.log = io.StringIO()
        super().__init__(*args, **kwargs)

    def emit(self, record):
        self.log.write(self.formatter.format(record))
        self.log.write("\n")


@contextmanager
def log_to_memory(logger: Optional[logging.Logger] = None):
    mem_handler = StringIoHandler()
    mem_handler.setFormatter(logging.Formatter(LOG_FORMAT_WITH_TIME))
    if logger is None:
        logger = logging.getLogger()
    logger.addHandler(mem_handler)
    saved_level = logger.level
    logger.setLevel(logging.NOTSET)
    yield mem_handler.log
    logger.removeHandler(mem_handler)
    logger.setLevel(saved_level)


def create_logger(name, logger_level: int = logging.DEBUG) -> LoggerExt:
    """Instantiate and return a new logger object with the user selected name
     and logging level (e.g. DEBUG, INFO).

    :param name: name of logger.
    :param logger_level: level of logger. Any messages under the selected
        level will not be printed to screen and logfile.
    :return: logger object
    """
    logger = logging.getLogger(name)
    logger.setLevel(logger_level)
    return cast(LoggerExt, logger)  # We called logging.setLoggerClass


def log_to_rotating_file(
    log_dir: str,
    logger: Optional[logging.Logger] = None,
    logger_level: int = logging.DEBUG,
    file_max_number: int = 1000,
    file_max_size: int = 1000000,
) -> None:
    """Add a rotating file handler to the specified logger. When the logfile
    reaches file_max_size, it gets renamed (a number is appended) and a new
    logfile is started. When file_max_number is exceeded, the oldest backup
    file is deleted.
    Logging to a file can be disabled, by setting `file_max_number = 0` or
    `file_max_size = 0`.

    :param logger: logger object to which the file handler should be added.
    :param log_dir: directory where to write the logfile.
    :param logger_level: level of logger (e.g. logging.DEBUG, logging.INFO).
        Messages under the selected level will be ignored by the handler.
    :param file_max_number: maximum number of logfiles to keep as backup.
    :param file_max_size: maximum size in bytes of an individual logfile.
    """
    if file_max_number == 0 or file_max_size == 0:
        return
    if logger is None:
        logger = logging.getLogger()
    # Create log directory if it does not exist yet.
    log_dir_path = Path(log_dir)
    if not log_dir_path.is_dir():
        try:
            log_dir_path.mkdir(parents=True)
        except PermissionError:
            logger.error("unable to create directory %s.", log_dir_path.as_posix())

    # Setup handler for logging info to file. The file logging format adds
    # the data and time at the start of each logged message.
    log_file = log_dir_path.joinpath("log")
    file_handler = logging.handlers.RotatingFileHandler(
        filename=log_file.as_posix(),
        mode="a",
        maxBytes=file_max_size,
        backupCount=file_max_number - 1,
    )
    file_handler.setFormatter(logging.Formatter(LOG_FORMAT_WITH_TIME))
    file_handler.setLevel(logger_level)
    logger.addHandler(file_handler)


def log_to_stream(
    logger: Optional[logging.Logger] = None, logger_level: int = logging.INFO
) -> None:
    """Add a stream handler to display logging info in console.

    :param logger: logger object to which the stream handler should be added.
    :param logger_level: level of logger (e.g. logging.DEBUG, logging.INFO).
        Messages under the selected level will be ignored by the handler.
    """
    if logger is None:
        logger = logging.getLogger()
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(
        ColoredTerminalFormatter(LOG_FORMAT)
        if platform.system() == "Windows"
        else EmojiLevelFormatter(LOG_FORMAT_WITH_EMOJI)
    )
    console_handler.setLevel(logger_level)
    logger.addHandler(console_handler)


def get_default_log_dir() -> str:
    """Returns a string with the default location of the directory where log
    files are stored on the host operating system.
    """
    default_log_dir_by_os: Dict[str, Tuple[str, ...]] = {
        "Linux": (".local/var/log/sett",),
        "Darwin": (".local/var/log/sett",),
        "Windows": ("AppData", "Roaming", "sett"),
    }
    return Path.home().joinpath(*default_log_dir_by_os[platform.system()]).as_posix()
