"""
    API for Era5 dataset from Copernicus Climate Datastore
     
    Metadata regarding the dataset can be found here:
        https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels?tab=overview
"""

import os
import logging
import warnings
import configparser
from os.path import isfile, dirname
from datetime import datetime, timedelta

import cdsapi
import pygrib
import numpy as np

from kadlu import index
from kadlu.geospatial.data_sources.data_util    import (
        database_cfg,
        dev_null,
        dt_2_epoch,
        epoch_2_dt,
        logmsg,
        logmsg_nodata,
        storage_cfg,
        str_def,
    )


era5_tables  = [
        'significant_height_of_combined_wind_waves_and_swell',
        'mean_wave_direction',
        'mean_wave_period',
        'u_component_of_wind',
        'v_component_of_wind',
        'convective_precipitation',
        'convective_snowfall',
        'normalized_energy_flux_into_ocean',
        'normalized_energy_flux_into_waves',
        'normalized_stress_into_ocean',
        'precipitation_type',
    ]


logging.getLogger('cdsapi').setLevel(logging.WARNING)

def initdb():
    conn, db = database_cfg()
    for var in era5_tables:
        db.execute(f'CREATE TABLE IF NOT EXISTS {var}'
                    '( val     REAL    NOT NULL, ' 
                    '  lat     REAL    NOT NULL, ' 
                    '  lon     REAL    NOT NULL, ' 
                    '  time    INT     NOT NULL, ' 
                    '  source  TEXT    NOT NULL) ') 
        db.execute(f'CREATE UNIQUE INDEX IF NOT EXISTS '
                   f'idx_{var} on {var}(time, lon, lat, val, source)')
    conn.close()



def era5_cfg(key=None, url=None):

    cfg = configparser.ConfigParser()       # read .ini into dictionary object
    cfgfile = os.path.join(dirname(dirname(dirname(dirname(__file__)))), "config.ini")
    #cfgfile = os.path.join(storage_cfg(), "config.ini")
    cfg.read(cfgfile)

    if 'cdsapi' not in cfg.sections():
        cfg.add_section('cdsapi')
    if key is not None:
        cfg.set('cdsapi', 'key', key)
        with open(cfgfile, 'w') as f:
            cfg.write(f)
    else:
        cfg.set('cdsapi', 'key', '20822:2d1c1841-7d27-4f72-bb8a-9680a073b4c3')
        with open(cfgfile, 'w') as f:
            cfg.write(f)
    if url is not None:
        cfg.set('cdsapi', 'url', url)
        with open(cfgfile, 'w') as f:
            cfg.write(f)
    else:
        cfg.set('cdsapi', 'url', 'https://cds.climate.copernicus.eu/api/v2')
        with open(cfgfile, 'w') as f:
            cfg.write(f)
    return 


def fetch_era5(var, *, west, east, south, north, start, end, **_):
    """ fetch global era5 data for specified variable and time range

        args:
            var: string
                the variable short name of desired wave parameter 
                according to ERA5 docs.  the complete list can be found 
                here (table 7 for wave params):
                https://confluence.ecmwf.int/display/CKB/ERA5+data+documentation#ERA5datadocumentation-Temporalfrequency
            kwargs: dict
                keyword arguments passed from the Era5() class as a dictionary

        return:
            True if new data was fetched, else False 
    """
    # cleaner stack trace by raising outside of try/except
    err = False

    era5_cfg()
    cfg = configparser.ConfigParser()       # read .ini into dictionary object
    cfgfile = os.path.join(dirname(dirname(dirname(dirname(__file__)))), "config.ini")
    #cfgfile = os.path.join(storage_cfg(), "config.ini")
    cfg.read(cfgfile)

    try: c = cdsapi.Client(url=cfg['cdsapi']['url'], key=cfg['cdsapi']['key'])
    except KeyError:
        try: c = cdsapi.Client()
        except Exception:
            err = True  

    if err: 
        raise KeyError('CDS API has not been configured for the ERA5 module. '
                       'obtain an API token from the following URL and run '
                       'kadlu.era5_cfg(url="URL_HERE", key="TOKEN_HERE"). '
                       'https://cds.climate.copernicus.eu/api-how-to')

    t = datetime(start.year, start.month, start.day, start.hour)
    assert end - start <= timedelta(days=1, hours=1), 'use index to bin fetch requests'
        
    # fetch the data
    fname = f'ERA5_reanalysis_{var}_{t.strftime("%Y-%m-%d")}.grb2'
    fpath = f'{storage_cfg()}{fname}'
    if not isfile(fpath):
        with dev_null():
            c.retrieve('reanalysis-era5-single-levels', {
                       'product_type' : 'reanalysis',
                       'format'       : 'grib',
                       'variable'     : var,
                       'year'         : t.strftime("%Y"),
                       'month'        : t.strftime("%m"),
                       'day'          : t.strftime("%d"),
                       'time'         : [datetime(t.year, t.month, t.day, h)
                                         .strftime('%H:00') for h in range(24)]
                    }, fpath)
    
    # load the data file and insert it into the database
    assert isfile(fpath)
    grb = pygrib.open(fpath)
    agg = np.array([[],[],[],[],[]])
    table = var[4:] if var[0:4] == '10m_' else var

    for msg, num in zip(grb, range(1, grb.messages)):
        if msg.validDate < start or msg.validDate > end: 
            continue

        # read grib data
        z, y, x = msg.data()
        if np.ma.is_masked(z):
            z2 = z[~z.mask].data
            y2 = y[~z.mask]
            x2 = x[~z.mask]
        else:  # wind data has no mask
            z2 = z.reshape(-1)
            y2 = y.reshape(-1)
            x2 = x.reshape(-1)

        # adjust latitude-zero to 180th meridian
        x3 = ((x2 + 180) % 360) - 180

        # index coordinates, select query range subset, aggregate results
        xix = np.logical_and(x3>=west,  x3<=east)
        yix = np.logical_and(y2>=south, y2<=north)
        idx = np.logical_and(xix, yix)
        agg = np.hstack((agg, [z2[idx],
                               y2[idx],
                               x3[idx],
                               dt_2_epoch([msg.validDate for i in z2[idx]]),
                               ['era5' for i in z2[idx]]]))

    # perform the insertion
    #if 'lock' in kwargs.keys(): kwargs['lock'].acquire()
    initdb()
    conn, db = database_cfg()
    n1 = db.execute(f"SELECT COUNT(*) FROM {table}").fetchall()[0][0]
    db.executemany(f"INSERT OR IGNORE INTO {table} "
                   f"VALUES (?,?,?,CAST(? AS INT),?)", agg.T)
    n2 = db.execute(f"SELECT COUNT(*) FROM {table}").fetchall()[0][0]
    db.execute("COMMIT")
    conn.commit()
    conn.close()
    #insert_hash(kwargs, f'fetch_era5_{era5_varmap[var]}')
    #if 'lock' in kwargs.keys(): kwargs['lock'].release()

    logmsg('era5', var, (n1, n2), **dict(south=south, west=west, north=north, east=east, start=start, end=end))
    #logging.info(f"ERA5 {msg.validDate.date().isoformat()} {var}: "
    #             f"processed and inserted {n2-n1} rows in region "
    #             f"{dict(south=south, west=west, north=north, east=east, start=start, end=end)}. "
    #             f"{len(agg[0])- (n2-n1)} duplicates ignored")
    return True


def load_era5(var, *, west, east, south, north, start, end, **_):
    """ load era5 data from local database

        args:
            var:
                variable to be fetched (string)
            kwargs:
                dictionary containing the keyword arguments used for the
                fetch request. must contain south, north, west, east
                keys as float values, and start, end keys as datetimes

        return:
            values:
                values of the fetched var
            lat:
                y grid coordinates
            lon:
                x grid coordinates
            epoch:
                timestamps in epoch hours since jan 1 2000
    """
    # check for missing data
    with index(storagedir=storage_cfg(), west=west, east=east, south=south, north=north, start=start, end=end) as fetchmap: 
        fetchmap(callback=fetch_era5, var=var)

    # load the data
    table = var[4:] if var[0:4] == '10m_' else var  # table cant start with int
    sql = ' AND '.join([f"SELECT * FROM {table} WHERE lat >= ?",
        'lat <= ?',
        'lon >= ?',
        'lon <= ?',
        'time >= ?',
        'time <= ?']) + ' ORDER BY time, lat, lon ASC'
    conn, db = database_cfg()
    db.execute(sql, tuple(map(str, [
            south,                north, 
            west,                 east, 
            dt_2_epoch(start), dt_2_epoch(end)
        ])))
    rowdata = np.array(db.fetchall(), dtype=object).T
    conn.close()

    if len(rowdata) == 0:
        logmsg_nodata('era5', var, west=west, east=east, south=south, north=north, start=start, end=end)
        return np.array([[],[],[],[]])

    val, lat, lon, epoch, source = rowdata 
    return np.array((val, lat, lon, epoch), dtype=np.float)


class Era5():
    """ collection of module functions for fetching and loading  """

    def load_windwaveswellheight(self, **kwargs):
        return load_era5('significant_height_of_combined_wind_waves_and_swell', **kwargs)

    def load_wavedirection(self, **kwargs):
        return load_era5('mean_wave_direction', **kwargs)

    def load_waveperiod(self, **kwargs):
        return load_era5('mean_wave_period', **kwargs)

    def load_precipitation(self, **kwargs):
        return load_era5('convective_precipitation', **kwargs)

    def load_snowfall(self, **kwargs):
        return load_era5('convective_snowfall', **kwargs)

    def load_flux_ocean(self, **kwargs):
        return load_era5('normalized_energy_flux_into_ocean', **kwargs)

    def load_flux_waves(self, **kwargs):
        return load_era5('normalized_energy_flux_into_waves', **kwargs)

    def load_stress_ocean(self, **kwargs):
        return load_era5('normalized_stress_into_ocean', **kwargs)

    def load_precip_type(self, **kwargs):
        return load_era5('precipitation_type', **kwargs)

    def load_wind_u(self, **kwargs):
        return load_era5('10m_u_component_of_wind', **kwargs)

    def load_wind_v(self, **kwargs):
        return load_era5('10m_v_component_of_wind', **kwargs)

    def load_wind_uv(self, **kwargs):
        with index(storagedir=storage_cfg(), west=kwargs['west'], east=kwargs['east'], south=kwargs['south'], north=kwargs['north'], start=kwargs['start'], end=kwargs['end']) as fetchmap: 
            fetchmap(callback=fetch_era5, var='10m_u_component_of_wind')
            fetchmap(callback=fetch_era5, var='10m_v_component_of_wind')

        sql = ' AND '.join(['SELECT u_component_of_wind.val, u_component_of_wind.lat, u_component_of_wind.lon, u_component_of_wind.time, v_component_of_wind.val FROM u_component_of_wind '\
            'INNER JOIN v_component_of_wind '\
            'ON u_component_of_wind.lat == v_component_of_wind.lat',
            'u_component_of_wind.lon == v_component_of_wind.lon',
            'u_component_of_wind.time == v_component_of_wind.time '\
            'WHERE u_component_of_wind.lat >= ?',
            'u_component_of_wind.lat <= ?',
            'u_component_of_wind.lon >= ?',
            'u_component_of_wind.lon <= ?',
            'u_component_of_wind.time >= ?',
            'u_component_of_wind.time <= ?']) + ' ORDER BY u_component_of_wind.time, u_component_of_wind.lat, u_component_of_wind.lon ASC'
        conn, db = database_cfg()
        db.execute(sql, tuple(map(str, [
                kwargs['south'],                kwargs['north'], 
                kwargs['west'],                 kwargs['east'], 
                dt_2_epoch(kwargs['start']), dt_2_epoch(kwargs['end'])
            ])))

        wind_u, lat, lon, epoch, wind_v = np.array(db.fetchall()).T
        val = np.sqrt(np.square(wind_u) + np.square(wind_v))
        conn.close()
        return np.array((val, lat, lon, epoch)).astype(float)


    def __str__(self):
        info = '\n'.join([
                "Era5 Global Dataset from Copernicus Climate Datastore.",
                "Combines model data with observations from across",
                "the world into a globally complete and consistent dataset",
                "\thttps://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels"])
        args = "(south, north, west, east, datetime, end)"
        return str_def(self, info, args)

