# This file's purpose is to make MPDAF's distutils `setup.py` work.

from .__version__ import __version__

from .galpak3d import *
from .galaxy_parameter import *
from .galaxy_parameters import *
from .model_sersic3d import ModelSersic
DefaultModel = ModelSersic
from .instruments import *
from .spread_functions import *
from .hyperspectral_cube import *
from .string_stdout import *
from .api import *
from .ansi_colors import *
from .math_utils import  *
