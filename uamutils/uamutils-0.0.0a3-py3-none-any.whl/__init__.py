# import numpy as np
import math
# import os

# TODO: is this problem completely solved on new versions?
# ignore pandas "Panel class" warning 
# import warnings
# warnings.simplefilter(action='ignore', category=FutureWarning)

# FIXME: this library takes _forever_ to import, can it be optimized with .pyc? 
#   or should we trim down all the cascading imports and such things?

from .data import UAMData, Coords
from .config import param_attributes

# from .mod4 import MOD4
# from .blocks import Sphere, Tube, Potential
# from .shared import DatasetID, BlockName, TimeMoment, ReferenceFrame

def params():
    return param_attributes
    # return [param_name for param_name in param_attributes]

def load_mod4(mod4_path):
    return UAMData(mod4_path)

def coords(altkm=None, colat=None, lon=None, ref_frame='geom'):
    return Coords(altkm, colat, lon, ref_frame)

def dir_ex(obj):
    return list(filter(lambda s: s[:2] != '__', dir(obj)))

# TODO: move to shared.py
# FIXME: np.vectorize to speed it up?
def sphere2cart(alt, lat, lon):
    # spherical system conversion
    x = alt * sin(radians(lat)) * cos(radians(lon)) 
    y = alt * sin(radians(lat)) * sin(radians(lon))
    z = alt * cos(radians(lat))
    # geographic conversion
    # x = alt * cos(lat) * cos(lon) 
    # y = alt * cos(lat) * sin(lon)
    # z = alt * sin(lat)

    return x, y, z
