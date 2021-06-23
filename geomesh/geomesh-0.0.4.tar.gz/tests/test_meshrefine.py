#!/usr/bin/env python
import pathlib
import sys
import shutil
import tarfile
import tempfile
import unittest
from unittest.mock import patch
import urllib.request

from geomesh.cmd import remesh


DATA_DIRECTORY = pathlib.Path(__file__).parent.absolute() / 'data'
DATA_DIRECTORY.mkdir(exist_ok=True)
FORT14 = DATA_DIRECTORY / "NetCDF_Shinnecock_Inlet/fort.14"
TEST_DEM = DATA_DIRECTORY / "ncei19_n41x00_w072x50_2015v1.tif"


class BestTrackRunCliTestCase(unittest.TestCase):

    def setUp(self):
        if not FORT14.is_file():
            url = "https://www.dropbox.com/s/1wk91r67cacf132/"
            url += "NetCDF_shinnecock_inlet.tar.bz2?dl=1"
            g = urllib.request.urlopen(url)
            tmpfile = tempfile.NamedTemporaryFile()
            with open(tmpfile.name, 'b+w') as f:
                f.write(g.read())
            with tarfile.open(tmpfile.name, "r:bz2") as tar:
                tar.extractall(DATA_DIRECTORY / "NetCDF_Shinnecock_Inlet")

        if not TEST_DEM.is_file():
            url = "https://coast.noaa.gov/htdata/raster2/elevation/"\
                  "NCEI_ninth_Topobathy_2014_8483/northeast_sandy/"\
                  "ncei19_n41x00_w072x50_2015v1.tif"
            g = urllib.request.urlopen(url)
            with open(TEST_DEM, 'b+w') as f:
                f.write(g.read())

    def test_remesh(self):
        cmd = [
                'remesh',
                f'{TEST_DEM}',
                f'--mesh={FORT14.resolve()}',
                '--mesh-crs=EPSG:4326',
                '--contour', '0.', '0.001', '20.',
                '--constant', '0.', '20.',
                '-o=./test.2dm',
                '--zmax=20.',
                # '--hmin=0.e-16'
            ]
        # print(' '.join(cmd))
        with patch.object(sys, 'argv', cmd):
            remesh.main()


if __name__ == '__main__':
    unittest.main()
