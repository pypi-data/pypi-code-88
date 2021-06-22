from enum import Enum, unique

class BaseEnum(Enum):
    @classmethod
    def values(cls) -> list:
        """Returns a list of raw values for the class"""
        values = [member.value for role, member in cls.__members__.items()]
        return values

@unique
class LogLevel(BaseEnum):
    """Represents the log levels that are supported"""

    NONE    = 0
    FAILURE = 1
    SUCCESS = 2
    ERROR   = 3
    WARN    = 4
    INFO    = 5
    DEBUG   = 6
    TRACE   = 7

@unique
class Colors(BaseEnum):
    """Represents the terminal formatting commands"""

    BLACK     = '\033[30m'
    RED       = '\033[31m'
    GREEN     = '\033[32m'
    YELLOW    = '\033[33m'
    BLUE      = '\033[34m'
    MAGENTA   = '\033[35m'
    CYAN      = '\033[36m'
    WHITE     = '\033[37m'
    RESET     = '\033[0m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'
    REVERSED  = '\033[7m'

@unique
class Html(BaseEnum):
    """Represents the terminal formatting commands"""

    BLACK     = '#000000'
    RED       = '#ff0000'
    GREEN     = '#00ff00'
    YELLOW    = '#ffff00'
    BLUE      = '#0000ff'
    MAGENTA   = '#ff00ff'
    CYAN      = '#00ffff'
    WHITE     = '#ffffff'