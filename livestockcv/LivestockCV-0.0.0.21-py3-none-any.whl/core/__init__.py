import os
import matplotlib
from LivestockCV.core.fatal_error import fatal_error
from LivestockCV.core.classes import Params
from LivestockCV.core.classes import Outputs

params = Params()
outputs = Outputs()

from LivestockCV.core.deprecation_warning import deprecation_warning
from LivestockCV.core.print_image import print_image
from LivestockCV.core.plot_image import plot_image
from LivestockCV.core.color_palette import color_palette
from LivestockCV.core.rgb2gray import rgb2gray
from LivestockCV.core.rgb2gray_hsv import rgb2gray_hsv
from LivestockCV.core.rgb2gray_lab import rgb2gray_lab
from LivestockCV.core import transform
from LivestockCV.core.apply_mask import apply_mask
from LivestockCV.core.crop import crop
from LivestockCV.core.invert import invert
from LivestockCV.core import roi
from LivestockCV.core import threshold
from LivestockCV.core.gaussian_blur import gaussian_blur
from LivestockCV.core.analyze_color import analyze_color
# add new functions to end of lists

# Auto versioning
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

__all__ = ['fatal_error', 'Params', 'Outputs', 'deprecation_warning', 'print_image', 'plot_image', 'color_palette', 'rgb2gray', 'rgb2gray_hsv', 'rgb2gray_lab', 'transform', 'apply_mask', 'crop', 'invert', 'roi', 'threshold', 'gaussian_blur', 'analyze_color']
