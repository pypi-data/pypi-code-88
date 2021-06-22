import os
import logging
from datetime import datetime

import pytest
import numpy as np
#import pandas as pd
from kadlu.geospatial.ocean import Ocean
from kadlu.geospatial.data_sources.source_map import default_val
from kadlu import hycom


bounds = dict(
        start=datetime(2015, 1, 9), end=datetime(2015, 1, 9, 3),
        south=44,                   west=-64.5, 
        north=46,                   east=-62.5, 
        top=0,                      bottom=5000
    )

test_lat, test_lon, test_depth = bounds['south'], bounds['west'], bounds['top']

def test_null_ocean():
    """ Test that ocean is initialized with all variables set to 
        null (0) when default=False"""
    
    o = Ocean(load_bathymetry=0, **bounds)
    
    assert o.bathy(test_lat, test_lon) == 0
    assert o.temp(test_lat, test_lon, test_depth) == 0
    assert o.salinity(test_lat, test_lon, test_depth) == 0
    assert o.wavedir(test_lat, test_lon) == 0
    assert o.waveheight(test_lat, test_lon) == 0
    assert o.waveperiod(test_lat, test_lon) == 0
    assert o.wind_uv(test_lat, test_lon) == 0
    assert o.origin == (45, -63.5)
    assert o.boundaries == bounds

def test_uniform_bathy():
    """ Test that ocean can be initialized with uniform bathymetry"""
    #o = Ocean(default=False, cache=False, load_bathymetry=-500.5)
    o = Ocean(load_bathymetry=500.5, **bounds)

    assert o.bathymetry(test_lat, test_lon) == 500.5
    assert o.bathy(test_lat, test_lon) == 500.5
    assert o.temp(test_lat, test_lon, test_depth) == 0

def test_interp_uniform_temp():
    """ Test that we can interpolate a uniform ocean temperature 
        on any set of coordinates"""
    #o = Ocean(default=False, cache=False, load_temp=16.1)
    o = Ocean(load_temp=16.1, **bounds)
    assert o.temp(lat=41.2, lon=-66.0, depth=-33.0) == 16.1
    #assert o.temp_xy(x=1, y=2.2, z=-3.0) == 16.1
    #assert np.all(o.temp_xy(x=[5,20], y=[0,10], z=[-300,-400]) == [16.1, 16.1])

def test_uniform_bathy_deriv():
    """ Test that uniform bathy has derivative zero"""
    #o = Ocean(default=False, cache=False, load_bathymetry=-500.5)
    o = Ocean(load_bathymetry=-500.5, **bounds)
    assert o.bathy_deriv(lat=1,lon=17,axis='lon') == 0

def test_gebco_bathy():
    """ Test that ocean can be initialized with bathymetry data 
        from a CHS file with automatic fetching enabled"""
    o = Ocean(load_bathymetry='gebco', **bounds)
    test_lat = [44.4, 44.5]
    test_lon = [-64, -63]
    bathy = o.bathy(test_lat, test_lon)
    assert len(bathy) > 0 #check that some data was retrieved
    # check that all nodes have meaningful bathymetry values
    assert np.all(bathy < 10000), f'{bathy}'
    assert np.all(bathy > -15000), f'{bathy}'
    #assert o.interps['bathymetry'].origin == o.origin

def test_interp_gebco_bathy():
    """ Test that we can interpolate bathymetry data 
        obtained from a gebco file"""
    o = Ocean(load_bathymetry='gebco', 
            south=43.1, west=-59.8, north=43.8, east=-59.2, 
            top=0, bottom=0, start=default_val['start'], end=default_val['end'])
    b = o.bathy(lat=1, lon=2)

    assert isinstance(b, float)
    b = o.bathy(lat=[43.2,43.7], lon=[-59.3, -59.4])
    assert len(b) == 2

#def test_interp_gebco_bathy():
#    o = Ocean(load_bathymetry='gebco', 
#            south=43.1, west=-59.8, north=43.8, east=-59.2, 
#            top=0, bottom=0, start=default_val['start'], end=default_val['end'])
    

'''
def test_interp_hycom_temp_gebco_bathy():
    """ Test that ocean can be initialized with temperature data 
        from HYCOM with automatic fetching enabled and using 
        start/end args.
    """
    kwargs = dict(
            south=43.1, west=-59.8, 
            north=43.8, east=-59.2,
            top=-100, bottom=3000,
            start=datetime(2015,1,1),
            end=datetime(2015,1,2)
        )
    o = Ocean(#fetch=True, #cache=False,
        load_temp='hycom', 
        load_bathymetry='gebco',
        **kwargs
        )
    lats = [43.4, 43.5]
    lons = [-59.6, -59.5]
    depths = [200, 300]
    #(temp,lats,lons,depths) = o.temp()
    temp = o.temp(lats, lons, depths)
    assert len(temp) > 0   #check that some data was retrieved
    assert len(depths) > 1 #check that more than one depth was fetched
    # interpolate temperature at seafloor
    seafloor_depth = o.bathy(lats, lons)
    temp = o.temp(lats, lons, seafloor_depth)
    assert np.all(np.logical_and(temp > -5, temp < 105)), f'{temp = }' # check sensible temperature at bottom

    # load hycom temperature data
    temp, lat, lon, epoch, depth = hycom().load_temp(**kwargs)
    # select a location close to the center of the region
    df = pd.DataFrame({'temp': temp, 'lat': lat, 'lon': lon, 'epoch': epoch, 'depth': depth})
    lat_close = df.lat.values[np.argmin(np.abs(df.lat.values - 43.45))]
    lon_close = df.lon.values[np.argmin(np.abs(df.lon.values - 59.5))]
    df = df[(df.lat == lat_close) & (df.lon == lon_close)]
    # query temps from ocean interpolator    
    depths = np.unique(df.depth.values)
    temp_ocean = o.temp(lat_close, lon_close, depths, grid=True)
    df = df.set_index(['depth','epoch'])
    df = df.groupby(level=[0]).mean()
    # check that interpolated temps and original temps agree
    assert np.all(temp_ocean == df.temp.values)
'''

def test_array_bathy():
    """ Test that ocean can be initialized with bathymetry data 
        from arrays"""
    bathy = np.array([[-100., -200.],
                      [-100., -200.]])
    lats = np.array([44.5, 44.7])
    lons = np.array([-60.1, -59.5])
    # note that fetching does nothing when supplying raw array data
    o = Ocean(load_bathymetry=(bathy, lats, lons), **bounds)
    la = lats
    lo = lons
    b = o.bathy(lat=lats, lon=lons)
    res = o.bathy(lat=44.5, lon=-60.1)
    assert res == -100
    res = o.bathy(lat=44.5, lon=-59.8)
    assert pytest.approx(res == -150., abs=1e-6)

def test_small_full_ocean():
    """ test that the ocean can be initialized for a very small region """

    bounds = dict(
            start=datetime(2015, 1, 9), end=datetime(2015, 1, 9, 3),
            south=44.2,                 west=-64.4, 
            north=44.21,                east=-64.39, 
            top=0,                      bottom=1
        )
    try:
        o = Ocean(load_bathymetry='gebco', load_temp='hycom', load_salinity='hycom', 
                load_wavedirection='era5', load_waveheight='wwiii', load_waveperiod='era5', 
                load_wind_uv='wwiii', **bounds)
    except AssertionError as err:
        # this is intended behaviour
        logging.info('CAUGHT EXCEPTION: ' + str(err))
        pass 
    except Exception as err:
        raise err


def test_wind_water_uv():
        o = Ocean(load_water_u='hycom', load_water_v='hycom', load_water_uv='hycom', 
                load_wind_u='era5', load_wind_v='era5', load_wind_uv='era5', 
                **bounds)

def test_precip_type():
        o = Ocean(load_precip_type='era5', **bounds)
        print(o.precip_type(lat=[-62.5,  -64.5, ], lon=[46, 44,], epoch=[10000, 200000000]))

""" interactive testing

from datetime import datetime
kwargs = dict(
    south=44.25, west=-64.5,
    north=44.70, east=-63.33,
    top=0, bottom=5000,
    start=datetime(2015, 4, 1), end=datetime(2015, 4, 1, 12))

load_bathymetry=0
load_temp='hycom'
load_salinity=0
load_wavedir=0
load_waveheight=0
load_waveperiod=0
load_wind_uv=0
load_wind_u=0
load_wind_v=0
load_water_uv=0
load_water_u=0
load_water_v=0

v = 'bathy'

fetch=4

"""

