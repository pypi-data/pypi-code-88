import os
import matplotlib
from LivestockCV.core.fatal_error import fatal_error
from LivestockCV.core.classes import Params
from LivestockCV.core.classes import Outputs
# Initialize an instance of the Params and Outputs class with default values
# params and outputs are available when plantcv is imported
params = Params()
outputs = Outputs()

from LivestockCV.core.print_image import print_image
from LivestockCV.core.plot_image import plot_image
from LivestockCV.core.rgb2gray import rgb2gray
from LivestockCV.core.crop import crop
# add new functions to end of lists

# Auto versioning
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

__all__ = ['fatal_error', 'Params', 'Outputs', 'print_image', 'plot_image', 'rgb2gray', 'crop']
