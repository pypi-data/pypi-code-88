import pytest
import kadlu
import logging
from datetime import datetime, timedelta
from kadlu.geospatial.data_sources import wwiii
from kadlu.geospatial.data_sources.wwiii import Wwiii, Boundary, wwiii_regions, wwiii_global


# gulf st lawrence
start   = datetime(2014, 2, 3, 0, 0, 0, 0)
end     = datetime(2014, 2, 3, 3, 0, 0, 0)
#south, west = 47,   -64
#north, east = 48,   -63
y, x, offset = 47.133, -63.51, 1
south, west = y-offset, x-offset
north, east = y+offset, x+offset 

"""
kwargs = dict(source='hycom', var='temp', south=south-1, west=west-1, north=north, east=east, start=start, end=end)
kadlu.plot2D(**kwargs, plot_wind='wwiii', top=0, bottom=0)
"""


def test_wwiii_ll2regionstr():
    # gulf st lawrence
    south =  46
    north =  52
    west  = -70
    east  = -56
    regions = wwiii.ll_2_regionstr(south, north, west, east, wwiii_regions, wwiii_global)
    assert(len(regions) == 1)
    assert(regions[0] == 'at_4m')

    # bering sea
    # test area intersection across antimeridian 
    south, north = 46, 67
    west, east = 158, -156
    east=-156
    regions = wwiii.ll_2_regionstr(south, north, west, east, wwiii_regions, wwiii_global)
    assert(len(regions) == 3)
    assert('ak_4m' in regions)
    assert('ao_30m' in regions)
    assert('wc_4m' in regions)

    # global 
    globe = wwiii.ll_2_regionstr(-90, 90, -180, 180, wwiii_regions, wwiii_global)
    assert(len(globe) == 5)


def test_wwiii_load_windwaveheight():
    result = kadlu.load(source='wwiii', var='waveheight', south=south, west=west, north=north, east=east, start=start, end=end)


def test_wwiii_load_waveperiod():
    result = kadlu.load(source='wwiii', var='waveperiod', south=south, west=west, north=north, east=east, start=start, end=end)
  
def test_wwiii_load_wavedir():
    result = kadlu.load(source='wwiii', var='wavedir', south=south, west=west, north=north, east=east, start=start, end=end)

def test_load_wind():
    ns_offset = 1
    ew_offset = 1

    uval,lat,lon,epoch = kadlu.load(source='wwiii', var='wind_u', 
                        start=datetime(2016, 3, 9) , end=datetime(2016,3,11),
                        south=44.5541333 - ns_offset, west=-64.17682 - ew_offset, 
                        north=44.5541333 + ns_offset, east=-64.17682 + ew_offset, 
                        top=0, bottom=0)
    assert(len(uval)==len(lat)==len(lon))
    assert len(uval) > 0

    vval,lat,lon,epoch = kadlu.load(source='wwiii', var='wind_v', 
                        start=datetime(2016, 3, 9) , end=datetime(2016,3,11),
                        south=44.5541333 - ns_offset, west=-64.17682 - ew_offset, 
                        north=44.5541333 + ns_offset, east=-64.17682 + ew_offset, 
                        top=0, bottom=0)
    assert(len(vval)==len(lat)==len(lon))
    assert len(vval) > 0

    uvval,lat,lon,epoch = kadlu.load(source='wwiii', var='wind_uv', 
                        start=datetime(2016, 3, 9) , end=datetime(2016,3,11),
                        south=44.5541333 - ns_offset, west=-64.17682 - ew_offset, 
                        north=44.5541333 + ns_offset, east=-64.17682 + ew_offset, 
                        top=0, bottom=0)

    assert(len(uvval)==len(lat)==len(lon))
    assert len(uvval) > 0


