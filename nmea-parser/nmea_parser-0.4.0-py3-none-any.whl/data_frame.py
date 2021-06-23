""" Data Frame module

Contains a class to capture and store an entire second of NMEA data
"""

import sys
from typing import List

from . import input_stream, nmea_message
from .core import python_logger

__author__ = "Brendan Kristiansen"
__copyright__ = "Copyright 2021, Brendan Kristiansen"
__credits__ = ["Brendan Kristiansen"]
__license__ = "MPL 2.0"
__maintainer__ = "Brendan Kristiansen"
__email__ = "b@bek.sh"


class DataFrame:

    _fix_message: nmea_message.NMEAFixMessage
    _gnss_message: nmea_message.GNSSFixData
    _active_sv_message: nmea_message.NMEADOPActiveSatsMessage
    _sv_in_view_message: List[nmea_message.NMEASatsInViewMessage]
    _rec_min_message: nmea_message.NMEARMCMessage
    _latlon_message: nmea_message.NMEALatLonMessage
    _vel_message: nmea_message.NMEAVelocityMessage

    _date: str
    _gpst: str
    _latitude: float
    _longitude: float
    _alt: float
    _alt_unit: str
    _vel: float
    _mode: str
    _quality: int
    _fix_dims: int
    _sv_count: int

    _complete: bool

    _all_msgs: List[nmea_message.NMEAMessage]

    def __init__(self, fix=None, gnss=None, active=None, inview=None, rmc=None, latlon=None, vel=None):

        self._all_msgs = []

        self._fix_message = fix
        self._active_sv_message = active
        self._gnss_message = gnss
        if inview is None:
            self._sv_in_view_message = []
        elif isinstance(inview, list):
            self._sv_in_view_message = inview
        else:
            self._sv_in_view_message = [inview]
        self._rec_min_message = rmc
        self._latlon_message = latlon
        self._vel_message = vel

        self._complete = True

        self._date = None
        self._gpst = None
        self._latitude = None
        self._longitude = None
        self._alt = None
        self._alt_unit = None
        self._mode = None
        self._quality = None
        self._fix_dims = None
        self._sv_count = None
        self._vel = None

        if fix is not None:
            self._gpst = self._fix_message.gpst_utc
            self._alt = self._fix_message.altitude
            self._alt_unit = self._fix_message.alt_unit
            self._quality = self._fix_message.fix_quality
            self._sv_count = self._fix_message.sv_count

        if latlon is not None:
            self._latitude = self._latlon_message.latitude
            self._longitude = self._latlon_message.longitude

        if gnss is not None:
            self._latitude = self._gnss_message.latitude
            self._longitude = self._gnss_message.longitude
            self._mode = self._gnss_message.mode
            self._sv_count = self._gnss_message.sv_count

        if active is not None:
            self._fix_dims = self._active_sv_message.ndims

        if rmc is not None:
            self._vel = rmc.speed_ms
            self._date = rmc.fix_date
            self._gpst = rmc.fix_time

        if vel is not None:
            self._vel = vel.velocity_ms

        for var in [self._gpst, self._date, self._latitude, self._longitude, self._alt, self._alt_unit, self._mode,
                    self._quality, self._fix_dims, self._sv_count, self._vel]:
            if var is None:
                self._complete = False

    def __str__(self):

        output = ""

        if self.is_complete():
            output += "Complete data frame"
        else:
            output += "Incomplete data frame"

        output += " Lat %s Lon %s Speed %s m/s Track %s" % (str(self._latitude), str(self._longitude),
                                                            str(self.velocity), str(self.track))

        return output

    @classmethod
    def get_next_frame(cls, stream: input_stream.GenericInputStream, debug=False):
        """ Capture data frame from a NMEA stream

        :param stream: input stream to listen to
        :param debug: Indicate to dump stream and sentence info live. Default false

        :return: Instance of data frame

        """

        fix_message = None
        gnss_message = None
        active_sv_message = None
        sv_in_view_message = []
        rec_min_message = None
        latlon_message = None
        vel_message = None

        while True:

            data = stream.get_line()
            msg = nmea_message.NMEAMessage.load_message(data)

            if debug:
                print(data)
                print(msg)

            if isinstance(msg, nmea_message.NMEAFixMessage):
                if fix_message is None:
                    fix_message = msg
                else:
                    break
            elif isinstance(msg, nmea_message.NMEADOPActiveSatsMessage):
                if active_sv_message is None:
                    active_sv_message = msg
                else:
                    break
            elif isinstance(msg, nmea_message.GNSSFixData):
                if gnss_message is None:
                    gnss_message = msg
                else:
                    break
            elif isinstance(msg, nmea_message.NMEASatsInViewMessage):
                # TODO: Only push back if we have not seen all sats yet
                sv_in_view_message.append(msg)
            elif isinstance(msg, nmea_message.NMEARMCMessage):
                if rec_min_message is None:
                    rec_min_message = msg
                else:
                    break
            elif isinstance(msg, nmea_message.NMEALatLonMessage):
                if latlon_message is None:
                    latlon_message = msg
                else:
                    break
            elif isinstance(msg, nmea_message.NMEAVelocityMessage):
                if vel_message is None:
                    vel_message = msg
                else:
                    break
            else:
                python_logger.get_logger().warning("Error. Unknown message type.")

        return cls(fix=fix_message, gnss=gnss_message, active=active_sv_message, inview=sv_in_view_message,
                   latlon=latlon_message, rmc=rec_min_message, vel=vel_message)

    def push_back_message(self, msg: nmea_message.NMEAMessage):
        """ Add a message to the data frame

        :param msg: Instance of nmea message to add to the data frame

        """

        if not isinstance(msg, nmea_message.NMEAMessage):
            raise TypeError('Given object is not a NMEA message')

        self._all_msgs.append(msg)

        if isinstance(msg, nmea_message.NMEAFixMessage):
            if self._fix_message is None:
                self._fix_message = msg
        elif isinstance(msg, nmea_message.NMEADOPActiveSatsMessage):
            if self._active_sv_message is None:
                self._active_sv_message = msg
        elif isinstance(msg, nmea_message.NMEASatsInViewMessage):
            self._sv_in_view_message.append(msg)
        elif isinstance(msg, nmea_message.NMEARMCMessage):
            if self._rec_min_message is None:
                self._rec_min_message = msg
        elif isinstance(msg, nmea_message.NMEALatLonMessage):
            if self._latlon_message is None:
                self._latlon_message = msg
        elif isinstance(msg, nmea_message.NMEAVelocityMessage):
            if self._vel_message is None:
                self._vel_message = msg
        else:
            python_logger.get_logger().warning("Error. Unknown message type.")

    def is_complete(self):
        return self._complete

    @property
    def gps_time(self):

        if self._date is not None and self._gpst is not None:
            return "%s %s" % (self._date, self._gpst)
        else:
            return None

    @property
    def velocity(self):
        return self._vel

    @property
    def track(self):
        try:
            return self._vel_message.true_track
        except AttributeError:
            return None

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

    @property
    def altitude(self):
        return self._alt

    @property
    def fix_quality(self):
        return self._quality

    @property
    def nsats(self):
        return self._sv_count

    @property
    def sv_observations(self):
        observations = []
        if self._sv_in_view_message is not None:
            for msg in self._sv_in_view_message:
                for obs in msg.observations:
                    observations.append(obs)
        return observations

    @property
    def all_messages(self):
        return self._all_msgs
