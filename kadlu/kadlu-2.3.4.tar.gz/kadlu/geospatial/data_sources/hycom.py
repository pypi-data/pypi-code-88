"""
    data source:
        https://www.hycom.org/data/glbv1pt08

    web interface for manual hycom data retrieval:
        https://tds.hycom.org/thredds/dodsC/GLBv0.08/expt_53.X/data/2015.html
"""

import logging
import requests
import warnings
from functools import reduce
from datetime import datetime, timedelta

import numpy as np

from kadlu import index
from kadlu.geospatial.data_sources.data_util import (
        database_cfg,
        dt_2_epoch,
        epoch_2_dt,
        fmt_coords,
        index_arr,
        logmsg,
        logmsg_nodata,
        storage_cfg,
        str_def,
    )


#conn, db = database_cfg()
hycom_src = "https://tds.hycom.org/thredds/dodsC/GLBv0.08/expt_53.X/data"
hycom_tables = ['hycom_salinity', 'hycom_water_temp', 'hycom_water_u', 'hycom_water_v']


slices_str = lambda var, slices, steps=(1,1,1,1): f"{var}{''.join(map(lambda tup, step : f'[{tup[0]}:{step}:{tup[1]}]', slices, steps))}"

def initdb():
    conn, db = database_cfg()

    for var in hycom_tables:
        db.execute(f'CREATE TABLE IF NOT EXISTS {var}'
                    '( val     REAL NOT NULL,' 
                    '  lat     REAL NOT NULL,' 
                    '  lon     REAL NOT NULL,' 
                    '  time    INT  NOT NULL,' 
                    '  depth   INT  NOT NULL,' 
                    '  source  TEXT NOT NULL )')

        db.execute(f'CREATE UNIQUE INDEX IF NOT EXISTS '
                   f'idx_{var} on {var}(time, lon, lat, depth, val, source)')
    conn.close()

def fetch_grid(**_):
    """ download lat/lon/time/depth arrays for grid indexing.
        times are formatted as epoch hours since 2000-01-01 00:00 
    """
    import time
    logging.info("HYCOM  fetching coordinate index...")
    url = f"{hycom_src}/2015.ascii?lat%5B0:1:3250%5D,lon%5B0:1:4499%5D"
    grid_netcdf = requests.get(url)
    assert(grid_netcdf.status_code == 200)

    meta, data = grid_netcdf.text.split\
    ("---------------------------------------------\n")
    lat_csv, lon_csv = data.split("\n\n")[:-1]
    lat = np.array(lat_csv.split("\n")[1].split(", "), dtype=np.float)
    lon = np.array(lon_csv.split("\n")[1].split(", "), dtype=np.float)

    epoch = {}

    for year in map(str, range(1994, 2016)):
        logging.info(f"HYCOM  fetching time index for {year}...")
        url = f"{hycom_src}/{year}.ascii?time"
        time_netcdf = requests.get(url)
        assert(time_netcdf.status_code == 200)
        meta, data = time_netcdf.text.split\
        ("---------------------------------------------\n")
        csv = data.split("\n\n")[:-1][0]
        epoch[year] = np.array(csv.split("\n")[1].split(', ')[1:], dtype=float)
        time.sleep(1)

    logging.info(f"HYCOM  fetching depth index...")
    depth = np.array([0.0, 2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 15.0, 20.0, 25.0,
        30.0, 35.0, 40.0, 45.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0, 125.0,
        150.0, 200.0, 250.0, 300.0, 350.0, 400.0, 500.0, 600.0, 700.0, 800.0,
        900.0, 1000.0, 1250.0, 1500.0, 2000.0, 2500.0, 3000.0, 4000.0, 5000.0])

    return lat, lon, epoch, depth


def load_grid():
    """ put spatial grid into memory """
    with index(storagedir=storage_cfg(), bins=False, store=True) as fetchmap:
        return fetchmap(callback=fetch_grid, seed='hycom grids')[0]


class Hycom():
    """ collection of module functions for fetching and loading

        attributes:
            lat, lon: arrays
                spatial grid arrays. used to convert grid index to 
                coordinate point
            epoch: dict
                dictionary containing yearly time indexes.
                times formatted as epoch hours since 2000-01-01 00:00
            depth: array
                depth scale. used to convert depth index to metres
    """

    def __init__(self): 
        self.ygrid, self.xgrid, self.epoch, self.depth = None, None, None, None 

    def load_salinity (self, **kwargs): return self.load_hycom('salinity', kwargs)

    def load_temp     (self, **kwargs): return self.load_hycom('water_temp', kwargs)

    def load_water_u  (self, **kwargs): return self.load_hycom('water_u', kwargs)

    def load_water_v  (self, **kwargs): return self.load_hycom('water_v', kwargs)

    def callback(self, var, **kwargs): 
        """ build indices for query, fetch from hycom, insert into database
            
            args:
                var: string
                    variable to be fetched. complete list of variables here
                    https://tds.hycom.org/thredds/dodsC/GLBv0.08/expt_53.X/data/2015.html
                kwargs: dict
                    boundaries as keyword arguments
        """
        # build request indexes
        year = str(kwargs['start'].year)
        haystack = np.array([self.epoch[year], self.depth, self.ygrid, self.xgrid], dtype=object)
        needles1 = np.array([dt_2_epoch(kwargs['start']), kwargs['top'], kwargs['south'], kwargs['west'] ])
        needles2 = np.array([dt_2_epoch(kwargs['end']), kwargs['bottom'], kwargs['north'], kwargs['east'] ])
        slices = list(zip(map(index_arr, needles1, haystack), map(index_arr, needles2, haystack))) 
        #n = reduce(np.multiply, map(lambda s : s[1] - s[0] +1, slices))
        assert reduce(np.multiply, map(lambda s : s[1] - s[0] +1, slices)) > 0, "0 records available within query boundaries: {kwargs}"

        # generate request
        url = f"{hycom_src}/{year}.ascii?{slices_str(var, slices)}"
        with requests.get(url, stream=True) as payload_netcdf:
            assert payload_netcdf.status_code == 200, "couldn't access hycom server"
            meta, data = payload_netcdf.text.split\
            ("---------------------------------------------\n")

        # parse response into numpy array
        arrs = data.split("\n\n")[:-1]
        shape_str, payload = arrs[0].split("\n", 1)
        shape = tuple([int(x) for x in shape_str.split("[", 1)[1][:-1].split("][")])
        cube = np.ndarray(shape, dtype=np.float)

        for arr in payload.split("\n"):
            ix_str, row_csv = arr.split(", ", 1)
            a, b, c = [int(x) for x in ix_str[1:-1].split("][")]
            cube[a][b][c] = np.array(row_csv.split(", "), dtype=np.int)

        # build coordinate grid, populate with values, adjust scaling, remove nulls
        flatten = reduce(np.multiply, map(lambda s : s[1] - s[0] +1, slices))
        add_offset =  20 if 'salinity' in var or 'water_temp' in var else 0
        null_value = -10 if 'salinity' in var or 'water_temp' in var else -30
        grid = np.array([(None, y, x, t, d, 'hycom') 
                for t in self.epoch[year][slices[0][0] : slices[0][1] +1]
                for d in self.depth      [slices[1][0] : slices[1][1] +1]
                for y in self.ygrid      [slices[2][0] : slices[2][1] +1]
                for x in self.xgrid      [slices[3][0] : slices[3][1] +1]])
        grid[:,0] = np.reshape(cube, flatten) * 0.001 + add_offset
        grid = grid[grid[:,0] != null_value]

        # insert into db
        initdb()
        conn, db = database_cfg()
        n1 = db.execute(f"SELECT COUNT(*) FROM hycom_{var}").fetchall()[0][0]
        db.executemany(f"INSERT OR IGNORE INTO hycom_{var} VALUES "
                        "(?, ?, ?, CAST(? AS INT), CAST(? AS INT), ?)", grid)
        n2 = db.execute(f"SELECT COUNT(*) FROM hycom_{var}").fetchall()[0][0]
        db.execute("COMMIT")
        conn.commit()
        conn.close()

        logmsg('hycom', var, (n1, n2), **kwargs)
        return


    def fetch_hycom(self, var, kwargs): 
        """ convert user query to grid index slices, handle edge cases """
        assert kwargs['start'] <= kwargs['end']
        assert kwargs['start'] >  datetime(1994, 1, 1), 'data not available in this range'
        assert kwargs['end']   <  datetime(2016, 1, 1), 'data not available in this range'
        assert kwargs['south'] <= kwargs['north']
        assert kwargs['top']   <= kwargs['bottom']
        assert kwargs['start'] >= datetime(1994, 1, 1)
        assert kwargs['end']   <  datetime(2016, 1, 1)

        if self.ygrid is None:
            self.ygrid, self.xgrid, self.epoch, self.depth = load_grid()

        # if query spans antimeridian, make two seperate fetch requests
        if kwargs['west'] > kwargs['east']:
            logging.debug('splitting request')
            argsets = [kwargs.copy(), kwargs.copy()]
            argsets[0]['east'] = self.xgrid[-1]
            argsets[1]['west'] = self.xgrid[0]
        else: argsets = [kwargs]

        for argset in argsets:
            args = {k:v for k,v in argset.items() if k in ['west', 'east', 'south', 'north', 'top', 'bottom', 'start','end']}
            with index(storagedir=storage_cfg(), bins=True, **args) as fetchmap:
                fetchmap(callback=self.callback, var=var)

        return True


    def load_hycom(self, var, kwargs):
        """ load hycom data from local database

            args:
                var:
                    variable to be fetched. complete list of variables here
                    https://tds.hycom.org/thredds/dodsC/GLBv0.08/expt_53.X/data/2015.html
                south, north: float
                    ymin, ymax coordinate values. range: -90, 90
                kwargs: dict (boundaries as keyword arguments)
                    west, east: float
                        xmin, xmax coordinate values. range: -180, 180
                    start, end: datetime
                        temporal boundaries in datetime format

            return: 
                values: array
                    values of the fetched variable
                lat: array
                    y grid coordinates
                lon: array
                    x grid coordinates
                epoch: array
                    timestamps in epoch hours since jan 1 2000 
                depth: array
                    measured in meters
        """
        # check if grids are initialized
        if self.ygrid is None:
            self.ygrid, self.xgrid, self.epoch, self.depth = load_grid()

        # recursive function call for queries spanning antimeridian
        if (kwargs['west'] > kwargs['east']): 
            kwargs1 = kwargs.copy()
            kwargs2 = kwargs.copy()
            kwargs1['west'] = self.xgrid[0]
            kwargs2['east'] = self.xgrid[-1]
            return np.hstack((self.load_hycom(var, kwargs1), 
                              self.load_hycom(var, kwargs2)))

        # check for missing data
        self.fetch_hycom(var, kwargs)

        # validate and execute query
        assert 8 == sum(map(lambda kw: kw in kwargs.keys(),
                ['south', 'north', 'west', 'east',
                 'start', 'end', 'top', 'bottom'])), 'malformed query'

        assert kwargs['start'] <= kwargs['end']
        sql = ' AND '.join([f"SELECT * FROM hycom_{var} WHERE lat >= ?",
                'lat <= ?',
                'lon >= ?',
                'lon <= ?',
                'time >= ?',
                'time <= ?',
                'depth >= ?',
                'depth <= ?',
                "source == 'hycom' "]

            ) + 'ORDER BY time, depth, lat, lon ASC'

        conn, db = database_cfg()
        db.execute(sql, tuple(map(str, [
                kwargs['south'],                kwargs['north'], 
                kwargs['west'],                 kwargs['east'],
                dt_2_epoch(kwargs['start']),    dt_2_epoch(kwargs['end']),
                kwargs['top'],                  kwargs['bottom']
            ])))
        rowdata = np.array(db.fetchall(), dtype=object).T
        conn.close()

        if len(rowdata) == 0:
            #logging.warning(f'HYCOM {var.upper()}: no data found in region {fmt_coords(kwargs)}, returning empty arrays')
            logmsg_nodata('hycom', var, **kwargs)
            return np.array([[],[],[],[],[]])

        return rowdata[0:5].astype(float)


    def load_water_uv (self, **kwargs):
        self.fetch_hycom('water_u', kwargs)
        self.fetch_hycom('water_v', kwargs)

        sql = ' AND '.join(['SELECT hycom_water_u.val, hycom_water_u.lat, hycom_water_u.lon, hycom_water_u.time, hycom_water_u.depth, hycom_water_v.val FROM hycom_water_u '\
                'INNER JOIN hycom_water_v '\
                'ON hycom_water_u.lat == hycom_water_v.lat',
                'hycom_water_u.lon == hycom_water_v.lon',
                'hycom_water_u.time == hycom_water_v.time '\
                'WHERE hycom_water_u.lat >= ?',
                'hycom_water_u.lat <= ?',
                'hycom_water_u.lon >= ?',
                'hycom_water_u.lon <= ?',
                'hycom_water_u.time >= ?',
                'hycom_water_u.time <= ?',
                'hycom_water_u.depth >= ?',
                'hycom_water_u.depth <= ?',
            ]) + ' ORDER BY hycom_water_u.time, hycom_water_u.lat, hycom_water_u.lon ASC'

        conn, db = database_cfg()
        db.execute(sql, tuple(map(str, [
                kwargs['south'],                kwargs['north'], 
                kwargs['west'],                 kwargs['east'], 
                dt_2_epoch(kwargs['start']),    dt_2_epoch(kwargs['end']),
                kwargs['top'],                  kwargs['bottom'],
            ])))
        qry = np.array(db.fetchall()).T
        conn.close()

        if len(qry) == 0:
            logging.warning(f'HYCOM water_uv: no data found in region {fmt_coords(kwargs)}, returning empty arrays')
            return np.array([[],[],[],[],[]])

        water_u, lat, lon, epoch, depth, water_v = qry
        val = np.sqrt(np.square(water_u) + np.square(water_v))
        return np.array((val, lat, lon, epoch, depth)).astype(float)


    def __str__(self):
        info = '\n'.join([
                "Native hycom .[ab] data converted to NetCDF at the Naval",
                "Research Laboratory, interpolated to 0.08° grid between",
                "40°S-40°N (0.04° poleward) containing 40 z-levels.",
                "Availability: 1994 to 2015",
                "\thttps://www.hycom.org/data/glbv0pt08" ])

        args = ("(south, north, west, east, "
                "start, end, top, bottom)")

        return str_def(self, info, args)
    

