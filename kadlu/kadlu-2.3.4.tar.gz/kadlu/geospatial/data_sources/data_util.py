"""
    additional tools and utils used across data loading modules
"""

import configparser
import json
import logging
import os
import pickle
import sqlite3
import sys
import warnings
from contextlib import contextmanager, redirect_stdout, redirect_stderr
from datetime import datetime, timedelta
from functools import reduce
from io import StringIO
from os.path import dirname
from importlib import reload

import numpy as np


ext = lambda filepath, extensions: isinstance(extensions, tuple) and any(x.lower() == filepath.lower()[-len(x):] for x in extensions)


def database_cfg():
    """ configure and connect to sqlite database

        time is stored as an integer in the database, where each value
        is epoch hours since 2000-01-01 00:00

        returns:
            conn:   
                database connection object
            db:
                connection cursor object
    """
    conn = sqlite3.connect(storage_cfg() + 'geospatial.db')
    db = conn.cursor()

    return conn, db


class storage_cfg(os.PathLike):
    """ return filepath containing storage configuration string

        first checks the config.ini file in kadlu root folder, then
        defaults to kadlu/storage
    """
    """
    __file__  = '/home/matt_s/kadlu/kadlu/geospatial/data_sources/data_util.py'
    """
    cfg = configparser.ConfigParser()       # read .ini into dictionary object

    def __init__(self, setdir=None):
        self.cfg.read(os.path.join(dirname(dirname(dirname(dirname(__file__)))), "config.ini"))
        if setdir: self.__call__(setdir)

    def default_storage(self, msg):
        """ helper function for storage_cfg() """
        storage_location = os.path.join(os.path.expanduser('~'), f'kadlu_data{os.path.sep}')
        if not os.path.isdir(storage_location): os.mkdir(storage_location)
        warnings.warn(f'''{msg} storage location will be set to {storage_location}.\n'''
        '''use kadlu.storage_cfg('/path/to/new/directory') to configure a different storage location''')
        return storage_location

    def __call__(self, setdir=None) -> str:
        if 'storage' not in self.cfg.sections():
            self.cfg.add_section('storage')

        if setdir is not None:
            assert os.path.isdir(setdir), 'directory does not exist'
            self.cfg.set('storage', 'storage_location', setdir)
            with open(os.path.join(dirname(dirname(dirname(dirname(__file__)))), "config.ini"), 'w') as f:
                self.cfg.write(f)
        try:
            storage_location = self.cfg['storage']['storage_location']
        except KeyError:                        # missing config.ini file
            return self.default_storage('storage location not configured.')

        if storage_location == '':              # null value in config.ini
            return self.default_storage('null value in config.')

        if not os.path.isdir(storage_location):    # verify the location exists
            return self.default_storage('storage location does not exist.')

        if storage_location[-1] != os.path.sep: 
            return storage_location + os.path.sep

        return str(storage_location)

    def __repr__(self) -> str: 
        return self.__str__()

    def __str__(self) -> str: 
        return self.__call__()

    def __dir__(self) -> str: 
        return self.__call__()

    def __fspath__(self) -> str: 
        return self.__call__()

    def __add__(self, other) -> str: 
        return ''.join([self.__str__(), other.__str__()])


def verbosity(set_verbosity=None):
    '''
    __file__ = '/home/matt/kadlu/kadlu/geospatial/data_sources/data_util.py'
    '''
    cfg = configparser.ConfigParser()
    cfg.read(os.path.join(dirname(dirname(dirname(dirname(__file__)))), "config.ini"))

    if 'other' not in cfg.sections():
        cfg.add_section('other')
        cfg.set('other', 'verbosity', str(False))
        with open(os.path.join(dirname(dirname(dirname(dirname(__file__)))), "config.ini"), 'w') as f:
            cfg.write(f)
    
    if set_verbosity is not None:
        assert set_verbosity in (True, False), 'verbosity must be True or False'
        cfg.set('other', 'verbosity', str(set_verbosity))
        with open(os.path.join(dirname(dirname(dirname(dirname(__file__)))), "config.ini"), 'w') as f:
            cfg.write(f)

    return cfg['other']['verbosity'] == 'True'

def dt_2_epoch(dt_arr, t0=datetime(2000,1,1,0,0,0)):
    """ convert datetimes to epoch hours """
    delta = lambda dt: (dt - t0).total_seconds()/60/60
    if isinstance(dt_arr, (list, np.ndarray)): return list(map(int, map(delta, dt_arr)))
    elif isinstance(dt_arr, (datetime)): return int(delta(dt_arr))
    else: raise ValueError('input must be datetime or array of datetimes')


def epoch_2_dt(ep_arr, t0=datetime(2000,1,1,0,0,0), unit='hours'):
    """ convert epoch hours to datetimes """
    delta = lambda ep, unit: t0 + timedelta(**{f'{unit}' : ep})
    if isinstance(ep_arr, (list, np.ndarray)): return list(map(partial(delta, unit=unit), ep_arr))
    elif isinstance(ep_arr, (float, int)): return delta(ep_arr, unit=unit)
    else: raise ValueError('input must be integer or array of integers')


def index_arr(val, sorted_arr):
    """ converts value in coordinate array to grid index """
    if val > sorted_arr[-1]: return len(sorted_arr) -1
    return np.nonzero(sorted_arr >= val)[0][0]


def flatten(cols, frames):
    """ dimensional reduction by taking average of time frames """
    # assert that frames are of equal size
    assert len(cols) == 5
    assert reduce(lambda a, b: (a==b)*a, frames[1:] - frames[:-1])

    # aggregate time frame splits and reduce them to average
    frames_ix = np.append([0], frames)
    split_num = range(len(frames_ix) -1)
    val_split = np.array([cols[0][frames_ix[f] : frames_ix[f+1]] for f in split_num])
    value_avg = (reduce(np.add, val_split) / len(val_split))
    _, y, x, _, z = cols[:, frames_ix[0] : frames_ix[1]]
    return value_avg, y, x, z


def reshape_2D(cols):
    return dict(values=cols[0], lats=cols[1], lons=cols[2])


def reshape_3D(cols):
    """ prepare loaded data for interpolation 
    
        args:
            cols: flattened numpy array of shape (4, n)
                cols[0]: values
                cols[1]: latitude
                cols[2]: longitude
                cols[3]: depth

        return: gridded
            dict(values=gridspace, lats=ygrid, lons=xgrid, depths=zgrid)
    
    """
    if isinstance(cols[0], (float, int)):
        return dict(values=cols[0])

    # if data is 4D, take average of values at time frame intervals
    frames = np.append(np.nonzero(cols[3][1:] > cols[3][:-1])[0] + 1, len(cols[3]))
    if len(np.unique(frames)) > 1: vals, y, x, z = flatten(cols, frames) 
    else: vals, y, x, _, z  = cols
    rows = np.array((vals, y, x, z)).T

    # reshape row data to 3D array
    xgrid, ygrid, zgrid = np.unique(x), np.unique(y), np.unique(z)
    gridspace = np.full((len(ygrid), len(xgrid), len(zgrid)), fill_value=None, dtype=float)
    # this could potentially be optimized to avoid an index lookup cost
    for row in rows:
        x_ix = index_arr(row[2], xgrid)
        y_ix = index_arr(row[1], ygrid)
        z_ix = index_arr(row[3], zgrid)
        gridspace[y_ix, x_ix, z_ix] = row[0]

    # remove nulls for interpolation:
    # fill missing depth values with last value in each column
    for xi in range(0, gridspace.shape[0]):
        for yi in range(0, gridspace.shape[1]):
            col = gridspace[xi, yi]
            if sum(np.isnan(col)) > 0 and sum(np.isnan(col)) < len(col):
                col[np.isnan(col)] = col[~np.isnan(col)][-1]
                gridspace[xi, yi] = col

    # null depth columns are filled with the average value at each depth plane
    for zi in range(0, gridspace.shape[2]):
        gridspace[:,:,zi][np.isnan(gridspace[:,:,zi])] = np.average(gridspace[:,:,zi][~np.isnan(gridspace[:,:,zi])])

    return dict(values=gridspace, lats=ygrid, lons=xgrid, depths=zgrid)


def str_def(self, info, args):
    """ builds string definition for data source class objects """
    fcns = [fcn for fcn in dir(self) if callable(getattr(self, fcn)) 
            and 'load' in fcn and not fcn.startswith("__")]
    return (f'{info}\n\nfunction input arguments:\n\t{args}\n\nclass functions:\n\t'
            + '\n\t'.join(fcns) + '\n')


def ll_2_regionstr(south, north, west, east, regions, default=[]):
    """ convert input bounds to region strings with seperating axis theorem """
    if west > east:  # recursive function call if query intersects antimeridian
        return np.union1d(ll_2_regionstr(south, north, west, +180, regions, default), 
                          ll_2_regionstr(south, north, -180, east, regions, default))

    query = Boundary(south, north, west, east)
    matching = [str(reg) for reg in regions if query.intersects(reg)]

    if len(matching) == 0: 
        warnings.warn(f"No regions matched for query. Defaulting to {default} ({len(default)} regions)")
        return default

    return np.unique(matching)


def fmt_coords(kwargs):
      return (
            f"{abs(kwargs['south']):.2f}°{'S' if kwargs['south'] <= 0 else 'N'}," 
            f"{abs(kwargs['west']):.2f}°{'W' if kwargs['west'] <= 0 else 'E'}"
            f"{','+str(kwargs['top'])+'m' if 'top' in kwargs.keys() else ''} : "
            f"{abs(kwargs['north']):.2f}°{'S' if kwargs['north'] <= 0 else 'N'},"
            f"{abs(kwargs['east']):.2f}°{'W' if kwargs['east'] <= 0 else 'E'}"
            f"{','+str(kwargs['bottom'])+'m' if 'bottom' in kwargs.keys() else ''}"
        )


def logmsg(source, var, ntup=(), **kwargs):
    logging.info(f'{source.upper()} {var.lower()}  logged {reduce(np.subtract, ntup[::-1])} points in region\t{json.dumps(kwargs, default=str, sort_keys=True)}')


def logmsg_nodata(source, var, **kwargs):
    logging.warning(f'{source.upper()} {var.lower()}: no data found, returning empty arrays for region\t{json.dumps({k:v for k,v in kwargs.items() if k in ("north","south","west","east","top","bottom","start","end")} , default=str, sort_keys=True)}')



class Boundary():
    """ compute intersecting boundaries with separating axis theorem """
    def __init__(self, south, north, west, east, fetchvar='', **_):
        self.south, self.north, self.west, self.east, self.fetchvar = \
                south, north, west, east, fetchvar

    def __str__(self): return self.fetchvar

    def intersects(self, other):
        return not (self.east  < other.west or
                    self.west  > other.east or
                    self.north < other.south or
                    self.south > other.north)


class Capturing(list):
    # https://stackoverflow.com/questions/16571150/how-to-capture-stdout-output-from-a-python-function-call
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio
        sys.stdout = self._stdout


@contextmanager
def dev_null():
    """ context manager to redirect output to /dev/null """
    with open(os.devnull, 'w') as null:
        try:
            with redirect_stderr(null) as err, redirect_stdout(null) as out: 
                yield (err, out)
        finally:
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__

