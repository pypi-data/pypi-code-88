import math

from collections import namedtuple
from enum import Enum

# get ideas from xarray.DataArray.__str__()
def class_contents(obj):
    return '\n'.join([f'{key} :: {value}' for key, value in obj.__dict__.items()])

Timestamp = namedtuple('Timestamp', ['started', 'finished', 'f10_7'])

DatasetID = namedtuple('DatasetID', ['block_name', 'time_moment'])
BlockName = Enum('BlockName', ['sphere', 'tube', 'potential', 'tube_to_sphere', 'sphere_to_tube'])
# prev_prev = t-2, prev = t-1, current current = t
TimeMoment = Enum('TimeMoment', ['prev_prev', 'prev', 'current'])

# TODO: несколько имён для одной и той же системы координат (алиасы)
# (более подробные алиасы)
# ['geomagnetic', 'geodetic', 'dipole', 'solar_magnetic']
# ReferenceFrame = Enum('ReferenceFrame', [('geomagnetic', 'geom'), 'geodetic', 'dipole', 'solar_magnetic'])

# NOTE(arthur): these conversion procedures are ported by Sergey from UAM code, almost verbatim   
def mag2geo(lon_m, co_lat_m):
    # 11.3 - pole colatitude
    gm_pole = math.radians(11.3e0)
    cos_gmp = math.cos(gm_pole)
    sin_gmp = math.sin(gm_pole)
    lon_mtmp = lon_m
    lat_m = 90.0e0-co_lat_m
    cos_lat_m = math.cos(math.radians(lat_m))
    sin_lat_m = math.sin(math.radians(lat_m))
    cos_lon_m = math.cos(math.radians(lon_mtmp))
    sin_lon_m = math.sin(math.radians(lon_mtmp))
    sin_lat_g = sin_lat_m*cos_gmp - cos_lat_m*cos_lon_m*sin_gmp
    lat_g = math.asin(sin_lat_g)
    cos_lat_g = math.cos(lat_g)
    sin_lon_g = (cos_lat_m*sin_lon_m) / cos_lat_g
    cos_lon_g = (sin_lat_m*sin_gmp + cos_lat_m*cos_lon_m*cos_gmp) / cos_lat_g
    if (abs(cos_lon_g) > 1.0e0):
        cos_lon_g = math.copysign(1.0e0, cos_lon_g)
    lon_gtmp = math.acos(cos_lon_g)
    if (sin_lon_g < 0.0e0):
        lon_gtmp = 2*math.pi - lon_gtmp
    lat_g = math.degrees(lat_g)
    lon_gtmp = math.degrees(lon_gtmp)
    # pole longitude
    lon_gtmp = lon_gtmp+(-70.6e0)
    if (lon_gtmp < 0.0e0):
        lon_gtmp = lon_gtmp+360.0e0
    if (lon_gtmp > 360.0e0):
        lon_gtmp = lon_gtmp-360.0e0
    lon_g = lon_gtmp
    if (abs(co_lat_m-(-70.6)) < 1.0e-3):
        lon_g = (-70.6)+180.0e0
        lat_g = 180.0e0-(11.3e0)
    if (abs(180.0e0-(co_lat_m-(-70.6))) < 1.0e-3):
        lon_g = (-70.6)+360.0e0
        lat_g = 90.0e0-(11.3e0)
    co_lat_g = 90.0e0-lat_g

    # Transform lon_g from 0:360 to -180:180.
    if lon_g > 180.0:
        lon_g -= 360

    return lon_g, co_lat_g

def geo2mag(lon_g, lat_g):
    gm_pole = math.radians(11.3)
    cos_gmp = math.cos(gm_pole)
    sin_gmp = math.sin(gm_pole)
    lon_gtmp = lon_g - (-70.6)
    cos_lat_g = math.cos(math.radians(lat_g))
    sin_lat_g = math.sin(math.radians(lat_g))
    cos_lon_g = math.cos(math.radians(lon_gtmp))
    sin_lon_g = math.sin(math.radians(lon_gtmp))
    sin_lat_m = sin_lat_g * cos_gmp + cos_lat_g * cos_lon_g * sin_gmp
    lat_m = math.asin(sin_lat_m)
    cos_lat_m = math.cos(lat_m)
    sin_lon_m = (cos_lat_g * sin_lon_g) / cos_lat_m
    cos_lon_m = (-sin_lat_g * sin_gmp + cos_lat_g * cos_lon_g * cos_gmp) / cos_lat_m
    if (abs(cos_lon_m) > 1.0):
        cos_lon_m = math.copysign(1.0, cos_lon_m)
    lon_mtmp = math.acos(cos_lon_m)
    if (sin_lon_m < 0.0):
        lon_m_tmp = 2. * math.pi - lon_mtmp
    lat_m = math.degrees(lat_m)
    lon_mtmp = math.degrees(lon_mtmp)

    if (lon_mtmp < 0.0):
        lon_mtmp = lon_mtmp + 360.0
    if (lon_mtmp > 360.0):
        lon_mtmp = lon_mtmp - 360.0

    lon_m = lon_mtmp
    if (abs(lat_g - 90.0) < 1.0e-3):
        lon_m = 180.0
        lat_m = (90.0 - 11.3)
    if (abs(lat_g + 90.0) < 1.0e-3):
        lon_m = 0.0e0
        lat_m = -(90.0e0 - 11.3)

    return lon_m, lat_m
