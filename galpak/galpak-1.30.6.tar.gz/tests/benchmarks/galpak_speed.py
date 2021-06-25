# coding=utf-8

import os
from distutils.version import LooseVersion, StrictVersion
import benchmark

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('GalPaK_bench:')


## GENERAL PACKAGES

from galpak import __version__
from galpak import GalPaK3D, DiskModel
from galpak import GalaxyParameters
from galpak import MUSE
from galpak import HyperspectralCube as Cube

#Python3 compatibility
try:
  basestring
except NameError:
  basestring = str

class Benchmark_galpak(benchmark.Benchmark):

    each = 100  # configure number of runs

    root_folder = os.path.abspath(os.path.join(
        os.path.dirname(os.path.abspath(__file__)), os.pardir, os.pardir
    ))


    fits_folder = os.path.join(root_folder, 'data/input/ref')
    ref_clean =  os.path.join(fits_folder, 'ref_cube_clean_gpk188.fits')
    ref_conv  = os.path.join(fits_folder, 'ref_cube_conv_gpk188.fits')


    instrument = MUSE(psf_fwhm=0.7, psf_ba=1.0, psf_pa=0)
    galaxy = None

    if isinstance(ref_clean, basestring):
        ref_clean = Cube.from_file(ref_clean)
    elif isinstance(ref_clean, Cube):
        pass
    else:
        raise NameError("ref_clean should be a string or a HyperCube")

    gk1 = GalPaK3D(ref_clean, instrument=instrument)

    if isinstance(ref_conv, basestring):
        ref_conv = Cube.from_file(ref_conv)
    elif isinstance(ref_conv, Cube):
        pass

    gk2 = GalPaK3D(ref_conv, instrument=instrument)

    if StrictVersion(__version__) >= StrictVersion('1.9'):
        model = DiskModel()
        gk1.model=model
        gk2.model=model
    else:
        model={}
        model['flux_profile']='exponential'
        model['rotation_curve']='arctan'
        model['disk_dispersion']='thick'
        model['hz_profile']='gaussian'

        gk1.disk_model=model
        gk2.disk_model=model
    #verbose
    gk1.verbose=False
    gk2.verbose=False


    if  galaxy is None:
        galaxy = GalaxyParameters(
            x=15, y=15, z=15,
            flux = 1,
            radius = 2.5,
            inclination = 45,
            pa = 280,
            turnover_radius=0.5,
            maximum_velocity=180,
            velocity_dispersion=40
        )

    def test_reference(self):
                #def _test_model(self, galaxy=None, instrument=None, model=None, ref_clean=None, ref_conv=None):
                #"""
                #test model calculation against a reference cube
                #:param galaxy:
                #:param instrument: Instrument MUSE(psf_fwhm=0.8) [default]
                #:param model: DiskModel [default]
                #:param ref_cube:
                #:return:
                #"""

        self.gk1.create_clean_cube(self.galaxy, self.ref_clean.data.shape)
        self.gk2.create_convolved_cube(self.galaxy, self.ref_conv.data.shape)

        #diff_clean = np.nansum( (clean_cube - ref_clean).data)
        #diff_conv = np.nansum( (convolved_cube - ref_conv).data)

        #test = (diff_clean) !=0 or (diff_conv) !=0
        #if test:
        #    logger.warning("Difference found with reference cube!!! %.3e" %  (diff_clean))
        #    logger.warning("Difference found with ref convolved cube!!! %.3e" % (diff_conv))
        #else:
        #    logger.info("Test passed successfully !! No differences found")

    def test_runner(self):

        self.gk1.run_mcmc(max_iterations=100,verbose=False,save_error_maps=False)

if __name__ == '__main__':
    benchmark.main(format="markdown", numberFormat="%.4g")

