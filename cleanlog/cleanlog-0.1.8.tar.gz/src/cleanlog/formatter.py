import logging

from termcolor import colored

# Level name constants and converters.
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0

_level_to_name = {
    CRITICAL: 'CRITICAL',
    ERROR: 'ERROR',
    WARNING: 'WARNING',
    INFO: 'INFO',
    DEBUG: 'DEBUG',
    NOTSET: 'NOTSET',
}
_name_to_level = {
    'CRITICAL': CRITICAL,
    'FATAL': FATAL,
    'ERROR': ERROR,
    'WARN': WARNING,
    'WARNING': WARNING,
    'INFO': INFO,
    'DEBUG': DEBUG,
    'NOTSET': NOTSET,
}

_level_to_color = {
    CRITICAL: 'red',
    ERROR: 'red',
    WARNING: 'yellow',
    INFO: 'cyan',
    DEBUG: 'green',
    NOTSET: 'white',
}

class BasicFormatter(logging.Formatter):
    """
    """
    default_format = '[%(levelname)-.1s %(name)s %(asctime)s] %(message)s'

    def __init__(self, fmt=default_format, datefmt=None, style='%'):
        super(BasicFormatter, self).__init__(fmt=fmt, datefmt=datefmt, style=style)


class ColoredFormatter(logging.Formatter):
    """
    Formatter class for `ColoredLogger`.
    """
    # default_format = '[%(levelname)-.1s %(name)s %(asctime)s] %(message)s'
    # default_format = '[%(asctime)s %(name)s] [%(levelname)s] %(message)s'
    default_format = '%(levelname)10s %(name)s %(message)s'

    def __init__(self, fmt=default_format, datefmt=None, style='%', time=False):
        time_format = '%(levelname)10s %(relativeCreated)8s %(name)s %(message)s'

        self.time = time
        if time:
            fmt = time_format

        super(ColoredFormatter, self).__init__(fmt=fmt, datefmt=datefmt, style=style)

    def _is_colored(self, message):
        return message.startswith('\x1b[')

    def _format_relative_created(self, ms):
        if ms < 1000:
            return '%3d' % ms + 'ms'
        elif ms < 60 * 1000:
            s = ms // 1000
            return '%.1f' % s + 's'
        elif ms < 60 * 60 * 1000:
            m = ms // (60 * 1000)
            s = ms % (60 * 1000) // 1000
            return '%2d' % m + 'm' + '%2d' % s + 's'
        elif ms < 24 * 60 * 60 * 1000:
            h = ms // (60 * 60 * 1000)
            m = ms % (60 * 60 * 1000) // (60 * 1000)
            return '%2d' % h + 'h' + '%2d' % m + 'm'
            
    def formatMessage(self, record):
        if self.time:
            record.relativeCreated = self._format_relative_created(record.relativeCreated)

        record.message = colored(record.message, 'white') if not self._is_colored(record.message) else record.message
        return colored(self._style.format(record), _level_to_color[record.levelno])
