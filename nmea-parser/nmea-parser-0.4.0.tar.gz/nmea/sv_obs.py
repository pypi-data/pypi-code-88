""" Module containing data structures pertaining to NMEA observations
"""

__author__ = "Brendan Kristiansen"
__copyright__ = "Copyright 2021, Brendan Kristiansen"
__credits__ = ["Brendan Kristiansen"]
__license__ = "MPL 2.0"
__maintainer__ = "Brendan Kristiansen"
__email__ = "b@bek.sh"


class SVObservation:
    """ Contains a snapshot of the receiver's connection to a satellite at a point in time
    """

    _gpst: str
    _prn: int
    _elev: float
    _az: float
    _snr: float

    def __init__(self, gpst: str, prn: int, elev: float, azimuth: float, snr: float):
        """ Constructor

        :param gpst: GPS Timestamp
        :param prn: Satellite number
        :param elev: Elevation angle in sky
        :param azimuth: Azimuth of satellite
        :param snr: Signal to noise ratio
        """

        self._gpst = gpst
        self._prn = prn
        self._elev = elev
        self._az = azimuth
        self._snr = snr

    def __str__(self):
        return "Observation of SV %d: SNR %f" % (self._prn, self._snr)

    @property
    def gpst(self):
        return self._gpst

    @property
    def prn(self):
        return self._prn

    @property
    def elevation(self):
        return self._elev

    @property
    def azimuth(self):
        return self._az

    @property
    def snr(self):
        return self._snr
