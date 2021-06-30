"""
iploka_geoip.exceptions
~~~~~~~~~~~~~~~~~~~~~~~

This module contains all iploka-geoip exceptions.
"""


class GeoIPException(Exception):
    """
    There was an ambiguous exception that occurred while attempting to fetch
    GeoIP data from the Iploka service.
    """
    pass


class ServiceError(GeoIPException):
    """
    The request failed because the Iploka service is currently down or
    experiencing issues.
    """
    pass


class ConnectionError(GeoIPException):
    """
    The request failed because it wasn't able to reach the Iploka service.
    This is most likely due to a networking error of some sort.
    """
    pass
