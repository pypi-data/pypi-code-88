"""Utils related to simple data types"""


def parse_float(float_str, default=None):
    """Parse float.

    Args:
        float_str (str): float as string
        default (, optional): optional value to return of parsing fails

    Return:
        float value

    .. code-block:: python

        >>> from utils.dt import parse_float
        >>> parse_float('1.23')
        1.23
        >>> parse_float('1.23abc')
        None
        >>> parse_float('1.23abc', 'abc')
        'abc'

    """
    try:
        return (float)(float_str)
    except ValueError:
        return default


def parse_int(int_str, default=None):
    """Parse int."""
    try:
        return (int)(int_str)
    except ValueError:
        return default
