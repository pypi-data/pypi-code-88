import pytest
import kadlu
import numpy as np
from datetime import datetime, timedelta
import os


# gulf st lawrence - small test area
south =  45.01
north =  45.99923
west  = -63.99
east  = -63
top   =  0
bottom=  5000
start = datetime(2000, 1, 10)
end   = datetime(2000, 1, 10, 12)

bounds = dict(
        south =  45,
        north =  46,
        west  = -64,
        east  = -63,
        top   =  0,
        bottom=  5000,
        start = datetime(2000, 1, 10),
        end   = datetime(2000, 1, 10, 12),
    )

def test_load_salinity():
    val, lat, lon, time, depth = kadlu.load(var='salinity', source='hycom', south=south, north=north, west=west, east=east, start=start, end=end, top=top, bottom=bottom)
    assert(len(val) == len(lat) == len(lon) == len(time))
    assert(sum(lat <= 90) == sum(lat >= -90) == len(lat))
    assert(sum(lon <= 180) == sum(lon >= -180) == len(lon))

def test_fetch_load_over_antimeridian():
    south, west = 44, 179
    north, east = 45, -179
    top, bottom = 0, 100

    val, lat, lon, time, depth = kadlu.load(var='salinity', source='hycom',
            south=south, north=north, 
            west=west, east=east, 
            start=start, end=end, 
            top=top, bottom=bottom
        )
    
    # commented to improve test speed
    """
    assert(len(val) > 0)
    assert(len(val) == len(lat) == len(lon) == len(time))
    assert(sum(lat <= 90) == sum(lat >= -90) == len(lat))
    assert(sum(lon <= 180) == sum(lon >= -180) == len(lon))

    assert np.all(lat >= south)
    assert np.all(lat <= north)
    #assert np.all(lon >= east)
    #assert np.all(lon <= west)
    """

# matt_s 2019-12
# hycom connection seems to be pretty slow for some reason... im getting ~2kbps download speeds
# in the meantime i've commented out the other fetch tests to make integrated testing faster

#def test_fetch_temp():
#    hycom.Hycom().fetch_temp(south=south, north=north, west=west, east=east, start=start, end=end, top=top, bottom=bottom)

def test_load_temp():
    val, lat, lon, time, depth = kadlu.load(source='hycom', var='temp', south=south, north=north, west=west, east=east, start=start, end=end, top=top, bottom=bottom)
    assert(len(val) == len(lat) == len(lon) == len(time))
    assert(sum(lat <= 90) == sum(lat >= -90) == len(lat))
    assert(sum(lon <= 180) == sum(lon >= -180) == len(lon))

#def test_fetch_water_u():
#    hycom.Hycom().fetch_water_u(south=south, north=north, west=west, east=east, start=start, end=end, top=top, bottom=bottom)

def test_load_water_uv():
    bounds = dict(
            south =  44.01,
            north =  44.31,
            west  = -63.1,
            east  = -62.9,
            top   =  0,
            bottom=  500,
            start = datetime(2000, 1, 10),
            end   = datetime(2000, 1, 10, 12),
        )

    data = kadlu.load(source='hycom', var='water_uv', **bounds)

def test_load_water_u():
    uval = kadlu.load(source='hycom',var='water_u', **bounds)
    # commented to improve test speed
    """
    assert(len(val) == len(lat) == len(lon) == len(time))
    assert(sum(lat <= 90) == sum(lat >= -90) == len(lat))
    assert(sum(lon <= 180) == sum(lon >= -180) == len(lon))
    """

#def test_fetch_water_v():
#    hycom.Hycom().fetch_water_v(south=south, north=north, west=west, east=east, start=start, end=end, top=top, bottom=bottom)

def test_load_water_v():
    vval = kadlu.load(source='hycom',var='water_v', **bounds)
    # commented to improve test speed
    """
    assert(len(val) == len(lat) == len(lon) == len(time))
    assert(sum(lat <= 90) == sum(lat >= -90) == len(lat))
    assert(sum(lon <= 180) == sum(lon >= -180) == len(lon))
    """


""" interactive mode debugging: assert db ordering is correct

    step through fetch_hycom() and put output and grid arrays into memory. 
    example test input:
>>>     
        year = '2000'
        var = 'salinity'
        slices = [
            (0, 2),         # time: start, end 
            (0, 3),         # depth: top, bottom
            (800, 840),     # x grid index: lon min, lon max
            (900, 1000)     # y grid index: lat min, lat max
        ]
        lat, lon = load_grid()
        epoch = load_times()
        depth = load_depth()

    run through the output builder loop again. this time, add an assertion to check 
    that the 4D array was flattened correctly
>>>     
        ix = 0  # debug index: assert order is correct
        for arr in payload.split("\n"):
            ix_str, row_csv = arr.split(", ", 1)
            a, b, c = [int(x) for x in ix_str[1:-1].split("][")]
            # output[a][b][c] = np.array(row_csv.split(", "), dtype=np.int)
            assert((output[a][b][c] == grid[ix:ix+len(output[a][b][c]), 0]).all())
            ix += len(output[a][b][c])

"""
"""
    import timeit 

    lat, sorted_arr = load_grid()
    def fcn():
        return index(np.random.rand()*360 - 180, sorted_arr)
    
    timeit.timeit(fcn, number=1000000)
    
"""


"""
    var = 'salinity'
    qry = {
            'south':44,  
            'north':45,
            'west':-60,
            'east':-59,
            'top':0,
            'bottom':5000,
            'start':datetime(2015, 10, 1),
            'end':datetime(2015, 10, 1, 12)
        }
    self = hycom.Hycom()
"""
