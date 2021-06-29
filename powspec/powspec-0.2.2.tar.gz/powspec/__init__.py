# Licensed under a 3-clause BSD style license - see LICENSE.rst

# Packages may add whatever they like to this file, but
# should keep this content at the top.
# ----------------------------------------------------------------------------
from ._astropy_init import *  # noqa

# ----------------------------------------------------------------------------

__all__ = []
from .powspec import power_spectral_density, cross_spectral_density
from .utils.apod import shrink_mask, fft_2d_hanning
from .utils.generator import Pk, gen_pkfield
# from .example_mod import *   # noqa
# Then you can be explicit to control what ends up in the namespace,
# __all__ += ['do_primes']   # noqa
__all__ += ["power_spectral_density", "cross_spectral_density"]
__all__ += ["shrink_mask", "fft_2d_hanning"]
__all__ += ["Pk", "gen_pkfield"]
# or you can keep everything from the subpackage with the following instead
