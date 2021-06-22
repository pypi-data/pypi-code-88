#print('importing...')

# py standard library
#from math import*
import importlib as imp
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as spe
import pandas as pd


# specific libraries
from . import displayStandards as dsp
from . import regionManager as regMg
from . import materialManager as matMg
from . import newtonRaphson as nwt
from . import bissection as bis
from . import commonInputOutput as iostd
from . import physicsConstants as cst
from . import glob_colors  as colors
from .glob_colors import *

def funcs(obj):
    import inspect
    functions = '\n'.join([f[0] for f in inspect.getmembers(obj,predicate=inspect.isfunction)])
    print(functions)
