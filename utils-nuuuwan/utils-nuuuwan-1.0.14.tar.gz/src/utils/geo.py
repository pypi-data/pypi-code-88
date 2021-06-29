"""Geo-Spatial Utils."""
from math import sin, cos, sqrt, atan2, pi
from area import area

EARTH_RADIUS = 6373.0
QUANTUMS = 1_000_000
LAT_LNG_COLOMBO = [6.9271, 79.8612]
LAT_LNG_KANDY = [7.2906, 80.6337]


def parse_latlng(latlng_str):
    """Parse latlng string.

    Args:
        latlng_str(str): String containing lat, lng
    Return:
        [lat, lng] float pair

    .. code-block:: python

        >>> from utils import geo
        >>> print(geo.parse_latlng('5N,70E'))
        (5.0, 70.0)
        >>> print(geo.parse_latlng('5°N,70°E'))
        (5.0, 70.0)
        >>> print(geo.parse_latlng('5,70'))
        (5.0, 70.0)
    """
    latlng_str = latlng_str.replace('°', '')
    lat_sign = 1
    if 'N' in latlng_str:
        latlng_str = latlng_str.replace('N', '')
    elif 'S' in latlng_str:
        latlng_str = latlng_str.replace('S', '')
        lat_sign = -1

    lng_sign = 1
    if 'E' in latlng_str:
        latlng_str = latlng_str.replace('E', '')
    elif 'W' in latlng_str:
        latlng_str = latlng_str.replace('W', '')
        lng_sign = -1

    lat_str, lng_str = latlng_str.split(',')
    return (float)(lat_str) * lat_sign, (float)(lng_str) * lng_sign


def deg_to_rad(deg):
    """Convert degrees to radians.

    Args:
        deg (float): Angle in degrees

    Return:
        Angle in radians

    .. code-block:: python

        >>> from utils import geo
        >>> print(geo.deg_to_rad(180))
        3.141592653589793

    """
    deg_round = round(deg * QUANTUMS, 0) / QUANTUMS
    return deg_round * pi / 180


def get_distance(latlng1, latlng2):
    """Get distance between two points.

    Args:
        latlng1 ([lat, lng]): First point
        latlng2 ([lat, lng]): Second point


    Returns:
        Distance in km

    Note:
        Assumes EARTH_RADIUS = 6373.0 km

    .. code-block:: python

        >>> from utils import geo
        >>> print(geo.get_distance(geo.LAT_LNG_COLOMBO, geo.LAT_LNG_KANDY))
        94.36504869698388

    """
    lat1, lng1 = latlng1
    lat2, lng2 = latlng2

    lat1 = deg_to_rad(lat1)
    lng1 = deg_to_rad(lng1)
    lat2 = deg_to_rad(lat2)
    lng2 = deg_to_rad(lng2)

    dlat = lat2 - lat1
    dlng = lng2 - lng1

    a_var = (sin(dlat / 2)) ** 2 + cos(lat1) * cos(lat2) * (sin(dlng / 2)) ** 2
    c_var = 2 * atan2(sqrt(a_var), sqrt(1 - a_var))
    return EARTH_RADIUS * c_var


def get_area(lnglat_list_list):
    """Find the area of a lnglat list list."""
    def get_area_for_lnglat_list(lnglat_list):
        obj = {
            'type': 'Polygon',
            'coordinates': [lnglat_list],
        }
        return area(obj) / 1000_000

    return sum(list(map(get_area_for_lnglat_list, lnglat_list_list)))
