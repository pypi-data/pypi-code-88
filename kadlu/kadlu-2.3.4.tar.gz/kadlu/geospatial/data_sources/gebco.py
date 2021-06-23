import os
import logging
import zipfile
import requests
from functools import reduce

import numpy as np
from tqdm import tqdm

import kadlu
from kadlu import index
from kadlu.geospatial.data_sources.data_util import (
        database_cfg,
        logmsg,
        logmsg_nodata,
        storage_cfg,
    )


fname = 'GEBCO_2020.nc'

def initdb():
    conn, db = database_cfg()
    db.execute('CREATE TABLE IF NOT EXISTS gebco' 
                '(   val     REAL    NOT NULL,  ' 
                '    lat     REAL    NOT NULL,  ' 
                '    lon     REAL    NOT NULL  )' )
    db.execute('CREATE UNIQUE INDEX IF NOT EXISTS idx_gebco on gebco(val, lat, lon)')
    conn.close()


class Gebco():

    def fetch_bathymetry_grid(self):
        """ download geotiff zip archive and extract it """

        zipf = os.path.join(kadlu.storage_cfg(), "gebco_2020_netcdf.zip")

        # unzip the file if necessary
        if not os.path.isfile(os.path.join(storage_cfg(), fname)):

            # if there is no zip file, download it
            if not os.path.isfile(zipf):
                logging.info('downloading and decompressing gebco bathymetry (netcdf ~8GB)... ')
                url = 'https://www.bodc.ac.uk/data/open_download/gebco/gebco_2020/zip/'
                with requests.get(url, stream=True) as payload_netcdf:
                    assert payload_netcdf.status_code == 200, 'error fetching file'
                    with open(zipf, 'wb') as f:
                        with tqdm(total=4008688379, desc='gebco_2020_netcdf.zip', unit='B', unit_scale=True) as t:
                            for chunk in payload_netcdf.iter_content(chunk_size=8192): 
                                f.write(chunk)
                                _ = t.update(8192)

            # unzip the downloaded file
            with zipfile.ZipFile(zipf, 'r') as zip_ref:
                logging.info('extracting bathymetry data...')
                zip_ref.extractall(path=storage_cfg())
        return


    def fetch_callback(self, south, north, west, east, top=None, bottom=None, start=None, end=None):
        """ build data grid indexes from .nc grid and insert into the database """

        if not os.path.isfile(os.path.join(storage_cfg(), fname)):
            self.fetch_bathymetry_grid()

        rows = kadlu.load_file(os.path.join(storage_cfg(), fname), south=south, north=north, west=west, east=east).T

        initdb()
        conn, db = database_cfg()
        n1 = db.execute(f"SELECT COUNT(*) FROM gebco ").fetchall()[0][0]
        db.executemany(f"INSERT OR IGNORE INTO gebco (val, lat, lon)  VALUES (?,?,?)", rows)
        n2 = db.execute(f"SELECT COUNT(*) FROM gebco ").fetchall()[0][0]

        logmsg('gebco', 'bathymetry', (n1, n2), south=south, west=west, north=north, east=east)
        conn.commit()
        conn.close()
        return


    def load_bathymetry(self, south, north, west, east, **_):
        """ load gebco bathymetry data """

        with index(storagedir=storage_cfg(), bins=True, south=south, north=north, west=west, east=east) as fetchmap:
            fetchmap(callback=self.fetch_callback)

        conn, db = kadlu.database_cfg()
        qry = ' AND '.join([f'SELECT val, lat, lon FROM gebco WHERE lat >= ?','lat <= ?','lon >= ?','lon <= ?'])
        #print(qry)
        logging.debug(f'query: {qry}')
        db.execute(qry, (south, north, west, east))
        res = np.array(db.fetchall()).T
        conn.close()
        if len(res) == 0: 
            logmsg_nodata('gebco', 'bathymetry', south=south, north=north, west=west, east=east)
            return np.array([[],[],[]])
        val, lat, lon = res
        return val, lat, lon

