""" NMEA Message module

Contains a class for NMEA sentences

https://www.gpsinformation.org/dale/nmea.htm#AAM
"""

from typing import Union, List

from .core import gps_time
from . import util, sv_obs

__author__ = "Brendan Kristiansen"
__copyright__ = "Copyright 2021, Brendan Kristiansen"
__credits__ = ["Brendan Kristiansen"]
__license__ = "MPL 2.0"
__maintainer__ = "Brendan Kristiansen"
__email__ = "b@bek.sh"


class NMEAMessage:

    _str_message: str

    _epoch_time_created: Union[None, float]
    _timestamp_created: Union[None, str]

    def __init__(self, raw_message: bytes):

        self._epoch_time_created = gps_time.time()
        self._timestamp_created = gps_time.gps_timestamp()

        self._str_message = str(raw_message)

    def __str__(self):
        return "NMEA sentence: "+self._str_message

    @staticmethod
    def break_message(message) -> list:

        assert isinstance(message, NMEAMessage)
        sentence = message.get_sentence()
        splt = sentence.split(',')
        return splt

    @staticmethod
    def load_message(msg: bytes):
        """ Load a specialized NMEA message type

        :param msg: bytes from NMEA stream

        :return: NMEAMessage or a subclass.

        """

        dec = msg.decode()

        if NMEAFixMessage.prefix in dec:
            return NMEAFixMessage(msg)
        elif NMEARMCMessage.prefix in dec:
            return NMEARMCMessage(msg)
        elif NMEALatLonMessage.prefix in dec:
            return NMEALatLonMessage(msg)
        elif NMEAVelocityMessage.prefix in dec:
            return NMEAVelocityMessage(msg)
        elif NMEADOPActiveSatsMessage.prefix in dec:
            return NMEADOPActiveSatsMessage(msg)
        elif NMEASatsInViewMessage.prefix in dec:
            return NMEASatsInViewMessage(msg)
        else:
            return NMEAMessage(msg)

    def get_sentence(self) -> str:
        return self._str_message


class NMEAFixMessage (NMEAMessage):

    prefix = "GGA"

    _time_utc = ""
    _lat: float
    _lon: float
    _quality: int
    _svs: int
    _horiz_dilution: float
    _alt: float
    _alt_unit: str
    _geoid_height: float
    _geoid_unit: str
    _dgps_update = None     # TODO: Implement this
    _dgps_station = None    # TODO: Implement this

    def __init__(self, msg: bytes):

        NMEAMessage.__init__(self, msg)

        self._str_message = msg.decode()

        broken_msg = self._str_message.split(',')
        self._time_utc = None if broken_msg[1] == '' else util.format_time(broken_msg[1])
        self._lat = None if broken_msg[2] == '' else util.format_coordinate(float(broken_msg[2]), broken_msg[3])
        self._lon = None if broken_msg[4] == '' else util.format_coordinate(float(broken_msg[4]), broken_msg[5])
        self._quality = 0 if broken_msg[6] == '' else int(broken_msg[6])
        self._svs = None if broken_msg[7] == '' else int(broken_msg[7])
        self._horiz_dilution = None if broken_msg[8] == '' else float(broken_msg[8])
        self._alt = None if broken_msg[9] == '' else float(broken_msg[9])
        self._alt_unit = None if broken_msg[10] == '' else broken_msg[10]
        self._geoid_height = None if broken_msg[11] == '' else float(broken_msg[11])
        self._dgps_update = None if broken_msg[12] == '' else broken_msg[12]
        self._dgps_station = broken_msg[13].split('*')[0]

    def __str__(self):
        """ String override
        """

        return "Fix: %s, Lat %s Lon %s, Quality %s, %s SVs, %s Horiz. Dilution, %s%s Altitude." % (self._time_utc,
                                                                                                   str(self._lat),
                                                                                                   str(self._lon),
                                                                                                   str(self._quality),
                                                                                                   str(self._svs),
                                                                                                   str(self._horiz_dilution),
                                                                                                   str(self._alt),
                                                                                                   self._alt_unit)

    @property
    def gpst_utc(self):
        return self._time_utc

    @property
    def altitude(self):
        return self._alt

    @property
    def fix_quality(self):
        return self._quality

    @property
    def sv_count(self):
        return self._svs

    @property
    def alt_unit(self):
        return self._alt_unit


class GNSSFixData (NMEAMessage):

    prefix = "GNS"

    _fix_utc: Union[str, None]
    _lat: Union[float, None]
    _lon: Union[float, None]
    _mode: str
    _sv_count: int
    _hdop: Union[float, None]
    _ortho_height: Union[float, None]
    _geoidal_sep: Union[float, None]
    _diff_age: Union[float, None]
    _stat_id = None

    def __init__(self, msg: bytes):

        NMEAMessage.__init__(self, msg)

        self._prns = []

        self._str_message = msg.decode()
        broken_msg = self._str_message.split(',')

        self._fix_utc = None if broken_msg[1] == '' else broken_msg[1]
        self._lat = None if broken_msg[2] == '' else util.format_coordinate(float(broken_msg[2]), broken_msg[3])
        self._lon = None if broken_msg[4] == '' else util.format_coordinate(float(broken_msg[4]), broken_msg[5])
        self._mode = broken_msg[6] if broken_msg[6] != '' else "NULL"   # TODO: Do we do something about this?
        self._sv_count = int(broken_msg[7]) if broken_msg[7] != '' else 0
        self._hdop = float(broken_msg[8]) if broken_msg[8] != '' else None
        self._ortho_height = float(broken_msg[9]) if broken_msg[9] != '' else None
        self._geoidal_sep = float(broken_msg[10]) if broken_msg[10] != '' else None
        self._diff_age = float(broken_msg[11]) if broken_msg[11] != '' else None
        self._stat_id = float(broken_msg[12].split('*')[0])

    def __str__(self):
        """ String override
        """

        return "%s, %s fix mode %s" % (self._lat, self._lon, self._mode)

    @property
    def latitude(self):
        return self._lat

    @property
    def longitude(self):
        return self._lon

    @property
    def mode(self):
        return self._mode

    @property
    def sv_count(self):
        return self._sv_count

    @property
    def hdop(self):
        return self._hdop

    @property
    def ortho_height(self):
        return self._ortho_height

    @property
    def geoidal_sep(self):
        return self._geoidal_sep

    @property
    def diff_age(self):
        return self._diff_age

    @property
    def stat_id(self):
        return self._stat_id


class NMEADOPActiveSatsMessage (NMEAMessage):

    prefix = "GSA"

    _fix_mode: Union[str, None]
    _fix_dims: Union[int, None]
    _prns: List[int]
    _pdop: Union[float, None]
    _hdop: Union[float, None]
    _vdop: Union[float, None]

    def __init__(self, msg: bytes):

        NMEAMessage.__init__(self, msg)

        self._prns = []

        self._str_message = msg.decode()
        broken_msg = self._str_message.split(',')
        broken_msg[-1] = broken_msg[-1].split('*')[0]

        self._fix_mode = None if broken_msg[1] == '' else broken_msg[1]
        self._fix_dims = None if broken_msg[2] == '' else int(broken_msg[2])
        for prn in broken_msg[2:14]:
            if prn != '':
                self._prns.append(int(prn))

        self._pdop = None if broken_msg[15] == '' else float(broken_msg[15])
        self._hdop = None if broken_msg[16] == '' else float(broken_msg[16])
        self._vdop = None if broken_msg[17] == '' else float(broken_msg[17])

    def __str__(self):
        """ String override
        """

        fix_dims = "No fix" if self._fix_dims == 1 else "2D fix" if self._fix_dims == 2 else "3D fix"
        return "Active SVs: %s, %s PDOP. %s." % (str(self._prns), str(self._pdop), fix_dims)

    @property
    def fix_mode(self):
        return self._fix_mode

    @property
    def ndims(self):
        return self._fix_dims

    @property
    def prns(self):
        return self._prns

    @property
    def pdop(self):
        return self._pdop

    @property
    def hdop(self):
        return self._hdop

    @property
    def vdop(self):
        return self._vdop


class NMEASatsInViewMessage (NMEAMessage):

    prefix = "GSV"

    _n_sentences: Union[int, None]
    _sentence_num: Union[int, None]
    _sv_count: Union[int, None]

    _observations: List[sv_obs.SVObservation]

    def __init__(self, msg: bytes):

        NMEAMessage.__init__(self, msg)

        self._observations = []

        broken_msg = self._str_message.strip("\r\n").split(',')
        broken_msg[-1] = broken_msg[-1].split('*')[0]
        self._n_sentences = None if broken_msg[1] == '' else int(broken_msg[1])
        self._sentence_num = None if broken_msg[2] == '' else int(broken_msg[2])
        self._sv_count = None if broken_msg[3] == '' else int(broken_msg[3])

        obs_count = 4 if self._sentence_num < self._n_sentences else self._sv_count % 4

        if self._sv_count % 4 == 0:
            obs_count = 4

        if not self._sv_count:
            return

        for i in range(obs_count):
            idx = 4+(i*4)

            prn = None if broken_msg[idx] == '' else int(broken_msg[idx])
            el = None if broken_msg[idx+1] == '' else float(broken_msg[idx+1])
            az = None if broken_msg[idx+2] == '' else float(broken_msg[idx+2])
            snr = None if broken_msg[idx+3] == '' else float(broken_msg[idx+3])

            if prn is None or el is None or az is None or snr is None:
                continue

            self._observations.append(sv_obs.SVObservation(self._timestamp_created, prn, el, az, snr))

    def __str__(self):
        base = "Observation message %s of %s (%s):" % (str(self._sentence_num), str(self._n_sentences),
                                                       str(self._sv_count))
        for obs in self._observations:
            base +=" "+str(obs)
        return base

    @property
    def sentence_count(self):
        return self._n_sentences

    @property
    def sentence_number(self):
        return self._sentence_num

    @property
    def sv_count(self):
        return self._sv_count

    @property
    def observations(self):
        return self._observations


class NMEARMCMessage (NMEAMessage):

    prefix = "RMC"

    _fix_time: Union[str, None]
    _status: Union[str, None]
    _lat: Union[float, None]
    _lon: Union[float, None]
    _spd_knots: Union[float, None]
    _track_deg: Union[float, None]
    _fix_date: Union[str, None]
    _magnetic_variation: Union[float, None]

    def __init__(self, msg: bytes):
        NMEAMessage.__init__(self, msg)

        split_msg = self._str_message.strip("\r\n").split(',')
        split_msg[-1] = split_msg[-1].split('*')[0]

        self._fix_time = None if split_msg[1] == '' else util.format_time(split_msg[1])
        self._status = None if split_msg[2] == '' else split_msg[2]
        self._lat = None if split_msg[3] == '' else util.format_coordinate(float(split_msg[3]), split_msg[4])
        self._lon = None if split_msg[5] == '' else util.format_coordinate(float(split_msg[5]), split_msg[6])
        self._spd_knots = None if split_msg[7] == '' else float(split_msg[7])
        self._track_deg = float(split_msg[8]) if split_msg[8] != '' else None
        self._fix_date = None if split_msg[9] == '' else util.format_date(split_msg[9])
        self._magnetic_variation = float(split_msg[10]) if split_msg[10] != '' else None
        if split_msg[11] == 'W':
            self._magnetic_variation = -self._magnetic_variation

        if self._epoch_time_created is None:
            if self._fix_date is not None and self._fix_time is not None:
                gps_time.report_gpst('%s %s' % (self._fix_date, self._fix_time))

    def __str__(self):

        return "Recommended Min fix at %s %s: %s, %s, %s knots, %s degrees track." % (self._fix_time, self._fix_date,
                                                                                      str(self._lat), str(self._lon),
                                                                                      str(self._spd_knots),
                                                                                      str(self._track_deg))

    @property
    def fix_date(self):
        return self._fix_date

    @property
    def fix_time(self):
        return self._fix_time

    @property
    def latitude(self):
        return self._lat

    @property
    def longitude(self):
        return self._lon

    @property
    def speed_kts(self):
        return self._spd_knots

    @property
    def speed_ms(self):
        if self._spd_knots is None:
            return None

        return util.kts_to_ms(self._spd_knots)

    @property
    def track(self):
        return self._track_deg

    @property
    def variation(self):
        return self._magnetic_variation

    @property
    def status(self):
        return self._status


class NMEALatLonMessage (NMEAMessage):

    prefix = "GLL"

    _lat: Union[float, None]
    _lon: Union[float, None]
    _fix_time: Union[str, None]
    _status: Union[str, None]

    def __init__(self, msg: bytes):
        NMEAMessage.__init__(self, msg)

        split_msg = self._str_message.strip("\r\n").split(',')
        split_msg[-1] = split_msg[-1].split('*')[0]

        self._lat = None if split_msg[1] == '' else util.format_coordinate(float(split_msg[1]), split_msg[2])
        self._lon = None if split_msg[3] == '' else util.format_coordinate(float(split_msg[3]), split_msg[4])
        self._fix_time = None if split_msg[5] == '' else util.format_time(split_msg[5])
        self._status = None if split_msg[6] == '' else split_msg[6]

    def __str__(self):
        return "Geographic Lat/Lon: %s, %s at %s" % (str(self._lat), str(self._lon), self._fix_time)

    @property
    def latitude(self):
        return self._lat

    @property
    def longitude(self):
        return self._lon

    @property
    def fix_time(self):
        return self._fix_time

    @property
    def status(self):
        return self._status


class NMEAVelocityMessage (NMEAMessage):

    prefix = "VTG"

    _track_true: Union[float, None]
    _track_magnetic: Union[float, None]
    _gs_knots: Union[float, None]
    _gs_kmh: Union[float, None]

    def __init__(self, msg: bytes):
        NMEAMessage.__init__(self, msg)

        broken_msg = self._str_message.strip("\r\n").split(',')

        self._track_true = None if broken_msg[1] == '' else float(broken_msg[1])
        self._track_magnetic = None if broken_msg[3] == '' else float(broken_msg[3])
        self._gs_knots = None if broken_msg[5] == '' else float(broken_msg[5])
        self._gs_kmh = None if broken_msg[7] == '' else float(broken_msg[7])

    def __str__(self):
        return "Current Speed: %s KM/h, Track: %s degrees." % (str(self._gs_kmh), str(self._track_true))

    @property
    def true_track(self):
        return self._track_true

    @property
    def mag_track(self):
        return self._track_magnetic

    @property
    def velocity_kmh(self):
        return self._gs_kmh

    @property
    def velocity_kts(self):
        return self._gs_knots

    @property
    def velocity_ms(self):
        if self._gs_kmh is None:
            return None

        return util.kmh_to_ms(self._gs_kmh)
