"""Time utils."""
import time
import datetime

DEFAULT_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'


class SECONDS_IN:
    """Units of time."""
    MINUTE = 60
    HOUR = 3600
    DAY = 86400
    WEEK = 7 * 86400
    FORTNIGHT = 14 * 86400
    MONTH = 365.25 * 4 * 86400 / 12
    QTR = 365.25 * 86400 / 4
    YEAR = 365.25 * 86400


def get_timezone():
    """Get timezone."""
    return str(datetime.datetime.now().astimezone().tzinfo)


def get_unixtime():
    """Get current unixtime."""
    return (int)(time.time())


def parse_time(
    time_str,
    time_format=DEFAULT_TIME_FORMAT,
):
    """Parse time string, and return unixtime."""
    _datetime = datetime.datetime.strptime(time_str, time_format)
    return (int)(time.mktime(_datetime.timetuple()))


def format_time(
    unixtime,
    time_format=DEFAULT_TIME_FORMAT,
):
    """Format unixtime as time string."""
    _datetime = datetime.datetime.fromtimestamp(unixtime)
    return _datetime.strftime(time_format)


class StopWatch:
    """Implements StopWatch.

    .. code-block:: python

        >>> import time
        >>> from utils import timex
        >>> sw = timex.StopWatch()
        >>> time.sleep(3)
        >>> print(sw.stop('Test'))
        3930.06706237793

    """

    def __init__(self):
        """__init__."""
        self.reset()

    def reset(self):
        """Reset StopWatch."""
        self.t_start = time.time()

    def stop(self, label=""):
        """Stop StopWatch, print and return elapsed time.

        Args:
            label(str, optional): Optional label to prefix the output

        Return:
            Elapsed time in miliseconds (float)

        """
        delta_t = (time.time() - self.t_start) * 1000
        print('{label} {delta_t}ms'.format(label=label, delta_t=delta_t))
        return delta_t
