""" Module for logging GPS data to a database
"""

import sqlite3
from typing import Union
from pathlib import Path
import sys

from . import data_frame, sv_obs

__author__ = "Brendan Kristiansen"
__copyright__ = "Copyright 2021, Brendan Kristiansen"
__credits__ = ["Brendan Kristiansen"]
__license__ = "MPL 2.0"
__maintainer__ = "Brendan Kristiansen"
__email__ = "b@bek.sh"


class GenericDBConnection:
    """ Generic Database connection
    """

    _cnx = None
    _crs = None

    def __init__(self, connection):
        """ Constructor

        :param connection: Instance of a database connection. Either mysql connector or sqlite3

        """

        self._cnx = connection
        self._crs = self._cnx.cursor()

        self._create_schema()

    def _create_schema(self):
        """ Create tables and indices
        """

        self.execute(SCHEMA_DDL_FRAME)
        self.execute(SCHEMA_DDL_SV_OBS)

    def execute(self, stmt: str):
        """ Safely execute an SQL insert statement

        :param stmt: Statement to execute

        """

        assert isinstance(stmt, str)

        stmt = stmt.replace("None", "NULL")
        self._crs.execute(stmt)
            
    def insert_dataframe(self, frame: data_frame.DataFrame):
        """ Insert a DataFrame object into the database

        :param frame: Instance of DataFrame

        """

        if not isinstance(frame, data_frame.DataFrame):
            raise TypeError('Object passed to function must be a DataFrame')

        gpst_utc = "NULL" if frame._fix_message is None else frame._fix_message.gpst_utc
        qual = "NULL" if frame.fix_quality is None else str(frame.fix_quality)

        svs = "NULL" if frame._fix_message is None else str(frame._fix_message.sv_count)
        alt = "NULL" if frame._fix_message is None else str(frame._fix_message.altitude)
        alt_unit = "NULL" if frame._fix_message is None else str(frame._fix_message.alt_unit)

        rm_fix_date = "NULL" if frame._rec_min_message is None else frame._rec_min_message.fix_date
        rm_fix_time = "NULL" if frame._rec_min_message is None else frame._rec_min_message.fix_time

        stmt = "INSERT INTO data_frame VALUES ("
        stmt += '"%s", ' % frame.gps_time
        stmt += '%s, ' % (str(frame.latitude) if frame.latitude != '' else "NULL")
        stmt += '%s, ' % (str(frame.longitude) if frame.longitude != '' else "NULL")
        stmt += '%s, ' % (str(frame._quality) if frame._quality is not None else "NULL")
        stmt += '%s, ' % (str(frame._sv_count) if frame._sv_count is not None else "NULL")
        stmt += '%s, ' % (str(frame._alt) if frame._alt is not None else "NULL")
        stmt += '"%s", ' % (str(frame._alt_unit) if frame._alt_unit is not None else "NULL")
        stmt += '%s, ' % (str(frame._active_sv_message.ndims) if frame._active_sv_message is not None else "NULL")
        stmt += '"%s", ' % rm_fix_date
        stmt += '"%s", ' % rm_fix_time
        stmt += '%s, ' % (str(frame._rec_min_message.latitude) if frame._rec_min_message is not None else "NULL")
        stmt += '%s, ' % (str(frame._rec_min_message.longitude) if frame._rec_min_message is not None else "NULL")
        stmt += '%s, ' % (str(frame._rec_min_message.speed_kts) if frame._rec_min_message is not None else "NULL")
        stmt += '%s, ' % (str(frame._rec_min_message.track) if frame._rec_min_message is not None else "NULL")
        stmt += '%s, ' % (str(frame._rec_min_message.variation) if frame._rec_min_message is not None else "NULL")
        stmt += '%s, ' % (str(frame._latlon_message.latitude) if frame._latlon_message is not None else "NULL")
        stmt += '%s, ' % (str(frame._latlon_message.longitude) if frame._latlon_message is not None else "NULL")
        stmt += '"%s", ' % (str(frame._latlon_message.fix_time) if frame._latlon_message is not None else "NULL")
        stmt += '%s, ' % (str(frame._vel_message.true_track) if frame._vel_message is not None else "NULL")
        stmt += '%s, ' % (str(frame._vel_message.mag_track) if frame._vel_message is not None else "NULL")
        stmt += '%s' % (str(frame._vel_message.velocity_kts) if frame._vel_message is not None else "NULL")
        stmt += ");"

        self.execute(stmt)
    
    def insert_sv_obs(self, obs: sv_obs.SVObservation):
        """ Insert a satellite observation to the database

        :param obs: Instance of SVObservation

        """

        if not isinstance(obs, sv_obs.SVObservation):
            raise TypeError('Object passed to function must be a SVObservation')

        stmt = "INSERT INTO sv_observation ("
        stmt += '"%s", ' % obs.gpst
        stmt += str(obs._prn) + ', '
        stmt += str(obs._elev) + ', '
        stmt += str(obs._az) + ', '
        stmt += str(obs._snr) + ', '
        stmt += ');'

        self.execute(stmt)


class SQLiteConnection(GenericDBConnection):
    """ Wrap an SQLite database connection
    """

    def __init__(self, cnx: sqlite3.Connection):
        """ Constructor

        :param path: SQLite3 database connection

        """

        GenericDBConnection.__init__(self, cnx)

    def __repr__(self):
        return '<SQLite 3 connection>'

    @classmethod
    def from_path(cls, path: Union[Path, str]):
        """ Open an SQLite connection at a path

        :param path: Path to database. Either string or pathlib.Path
        :return: New instance of SQlite connection

        """

        if not isinstance(path, str) and not isinstance(path, Path):
            raise TypeError('Path parameter must be `str` or `pathlib.Path`')

        cnx = sqlite3.connect(str(path))
        return SQLiteConnection(cnx)

    def execute(self, stmt: str):
        """ Safely execute a database statement. Commit afterwards.

        :param stmt: Statement to execute

        """

        GenericDBConnection.execute(self, stmt)
        self._cnx.commit()


SCHEMA_DDL_FRAME = "CREATE TABLE IF NOT EXISTS data_frame (gpst datetime, fix_lat real default null, " \
                         "fix_lon real default null, quality integer, sv_in_sol integer, alt real, alt_unit char," \
                         "fix_dims integer, rmc_fix_date date, rmc_time time, rmc_lat real default null, rmc_lon real,"\
                         "rmc_spd_kts real default null, rmc_track_deg real default null," \
                         "mag_variation real default null, gll_lat real default null, gll_lon real default null," \
                         "gll_fix_time time, vtg_true_track float default null, vtg_mag_track real default null," \
                         "vtg_gs_kts real default null);"

SCHEMA_DDL_SV_OBS = "CREATE TABLE IF NOT EXISTS sv_observation (gpst datetime, prn int, elevation real, azimuth real," \
                    "snr real);"
