""" Miscillaneous tools for the NMEA parser
"""

from .core import python_logger


def format_date(date: str) -> str:
    """ Format a datetime correctly

    :param date: Date formatted DDMMYY

    :return: Date formatted YYYY-MM-DD

    """

    assert isinstance(date, str)

    day = date[0:2]
    mo = date[2:4]
    yr_end = date[4:6]
    yr = "20" if int(yr_end) < 78 else "19"     # In 2078, we're going to have some trouble here :(
    yr += yr_end

    return yr+'-'+mo+'-'+day


def format_time(tm: str) -> str:
    """ Format a time correctly

    :param tm: Time formatted HHMMSS

    :return: Time formatted HH:MM:SS

    """

    assert isinstance(tm, str)

    return tm[0:2] + ':' + tm[2:4] + ':' + tm[4:6]


def format_coordinate(coord: float, hemi: str) -> float:
    """ Format a latitude or longitude correctly

    :param coord: Latitude or Longitude value
    :param hemi: Hemisphere (W, E, N, S)

    :return: Floating point number positive in northern and eastern hemispheres and negative in southern and western.

    """

    assert isinstance(coord, float) or isinstance(coord, int)
    assert isinstance(hemi, str)

    if hemi in ['W', 'E']:
        deg_len = 3
    elif hemi in ['N', 'S']:
        deg_len = 2
    else:
        # uh oh
        pass

    deg = float(str(coord)[0:deg_len])
    min = float(str(coord)[deg_len:])
    angle = deg + min / 60

    if hemi in ['W', 'S']:
        angle = -angle

    return angle


def kmh_to_ms(spd: float) -> float:
    """ Convert kilometers per hour to meters per second

    :param spd: Speed in km/h

    :return: Speed in m/s

    """

    if spd is None:
        return 0

    assert isinstance(spd, float) or isinstance(spd, int)

    return spd * 5 / 18


def kts_to_ms(spd: float) -> float:
    """ Convert knots to meters per second

    :param spd: Speed in kts

    :return: Speed in m/s

    """

    if spd is None:
        return 0

    assert isinstance(spd, float) or isinstance(spd, int)

    return spd * 0.5144444444


def set_log_level(level: int):
    """ Set log level for NMEA Parser logger

    :param level: Log level. Use one of the constants in the python logging module

    """

    python_logger.get_logger().setLevel(level)
