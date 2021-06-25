# coding=utf-8

import os, sys
from distutils.version import LooseVersion, StrictVersion
import numpy as np
sys.path.append('../')

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('GalPaK_Tests:')


## GENERAL PACKAGES
import unittest
import matplotlib
matplotlib.use('Agg')

import galpak
from galpak import GalPaK3D, DefaultModel, ModelSersic
from galpak import GalaxyParameters, GalaxyParametersError
from galpak import MUSE
from galpak.instruments import *
from galpak import GaussianPointSpreadFunction, MoffatPointSpreadFunction
from galpak import HyperspectralCube as Cube
try:
    import corner
    corner_true = True
except:
    corner_true = False

from tests.tools.numpy_ndarray_assertions import NumpyNdArrayAssertions

#Python3 compatibility
try:
  basestring
except NameError:
  basestring = str


class Something(object):
    """ Mock class for testing invalid input """
    pass


class GalPaK3DTest(unittest.TestCase, NumpyNdArrayAssertions):
    """
    Some tests plot images, and they WILL PAUSE THE RUNNER until you close the images. (CTRL+W = Close)
    """

    longMessage = True

    root_folder = os.path.abspath(os.path.join(
        os.path.dirname(os.path.abspath(__file__)), os.pardir, os.pardir
    ))

    fits_folder = os.path.join(root_folder, 'data/input')
    fits_mpdaf_filename = os.path.join(fits_folder, 'cube/subcube_mpdaf.fits')
    fits_muse_filename = os.path.join(fits_folder, 'cube/subcube_MUSE.fits')
    fits_real_muse_filename = os.path.join(fits_folder,
                                           'cube/zoom_oii_subcube_3Dcontinuum_subtracted.fits')
    fits_real_muse_variance = os.path.join(fits_folder, 'cube/zoomVariance_oii_subcube_3Dcontinuum_subtracted.fits')

    alma_filename = os.path.join(fits_folder, 'ALMA_Freq_test1.fits') #pixscale 0.7
    alma_instrument = os.path.join(fits_folder, 'alma_instrument.txt')
    myinstrument = os.path.join(fits_folder, 'myinstrument.txt')

    def assertEqualish(self, expected, actual, expected_similarity=99.):
        """
        Assert that actual is similar to expected, at expected_similarity (in %).
        This assertion can be improved :
        - Failure message
        - Input type-check
        """
        actual_precision = 100. * (1 - np.abs(expected - actual) / expected)
        self.assertTrue(actual_precision >= expected_similarity)

    def test_init_with_not_a_cube_nor_a_filename(self):
        with self.assertRaises(TypeError):
            g = GalPaK3D(Something())

    def test_init_with_empty_cube(self):
        with self.assertRaises(ValueError):
            g = GalPaK3D(Cube())

    def test_init_with_unfit_cube(self):
        with self.assertRaises(Exception):
            g = GalPaK3D(Cube.from_file('this_is_not_a_fits_file'))

    def test_init_with_unfit_filename(self):
        with self.assertRaises(Exception):
            g = GalPaK3D('this_is_not_a_fits_file')

    def test_init_with_mpdaf_cube(self):
        logger.info('Test init with mpdaf')
        try:
            import mpdaf
            cube = mpdaf.obj.Cube(filename=self.fits_muse_filename)
            g = GalPaK3D(cube)  # should not raise
            self.assertIsNotNone(g.variance_cube)
        except ImportError:
            pass

    #def test_init_with_real_muse_cube(self):
    #    logger.info("Test init with muse cube")
    #    g = GalPaK3D(self.fits_real_muse_filename,
    #                 variance=self.fits_real_muse_variance,
    #                 seeing=0.65)
    #    g.run_mcmc(max_iterations=100, verbose=False)

    def test_init_with_all_of_our_input_fits(self):
        for filename in os.listdir(self.fits_folder):
            if os.path.isfile(filename):
                filename = os.path.join(self.fits_folder, filename)
                g = GalPaK3D(filename)  # should not raise; if it does, use sanitizer

    def test_init_with_default_context(self):
        logger.info("test_default_context")
        g = GalPaK3D(self.fits_muse_filename)
        self.assertIsInstance(g.instrument, MUSE,
                              "Default instrument should be MUSE")

    def test_init_with_default_model(self):
        logger.info("test_init_default_model")

        g = GalPaK3D(self.fits_muse_filename)
        m = DefaultModel(redshift=0.8)
        g.run_mcmc(max_iterations=10, model=m, verbose=False)

    def test_reference(self):
        logger.info("test against reference")
        #def _test_model(self, galaxy=None, instrument=None, model=None, ref_clean=None, ref_conv=None):
        #"""
        #test model calculation against a reference cube
        #:param galaxy:
        #:param instrument: Instrument MUSE(psf_fwhm=0.8) [default]
        #:param model: DefaultModel [default]
        #:param ref_cube:
        #:return:
        #"""

        fits_folder = os.path.join(self.root_folder, 'data/input/ref')
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

        if LooseVersion(galpak.__version__) >= LooseVersion('1.9'):
            model = DefaultModel(flux_profile='exponential', rotation_curve='arctan', \
                                 thickness_profile='gaussian', dispersion_profile='thick')
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


        clean_cube = gk1.create_clean_cube(galaxy, ref_clean.data.shape)
        convolved_cube = gk2.create_convolved_cube(galaxy, ref_conv.data.shape)

        diff_clean = np.nansum( (clean_cube - ref_clean).data)
        diff_conv = np.nansum( (convolved_cube - ref_conv).data)

        test = (diff_clean) !=0 or (diff_conv) !=0
        if test:
            logger.warning("Difference found with reference cube!!! %.3e" %  (diff_clean))
            logger.warning("Difference found with ref convolved cube!!! %.3e" % (diff_conv))
        else:
            logger.info("Test passed successfully !! No differences found")

        self.assertTrue(test, "Model still works")

    def test_variance(self):
        logger.info("Test with manual variance float")
        glpk3d = GalPaK3D(self.fits_muse_filename,variance=1.0)
        self.assertTrue(isinstance(glpk3d.variance_cube, Cube))
        glpk3d.run_mcmc(max_iterations=50, verbose=False)

        logger.info("Test with manual variance HyperCube")
        var = np.random.normal(0,1.,size=glpk3d.cube.shape)
        glpk3d = GalPaK3D(self.fits_muse_filename, variance=Cube(var))
        self.assertTrue(isinstance(glpk3d.variance_cube, Cube))
        glpk3d.run_mcmc(max_iterations=50, verbose=False)

        logger.info("Test with manual variance filename")
        glpk3d = GalPaK3D(self.fits_real_muse_filename, variance=self.fits_real_muse_variance)
        self.assertTrue(glpk3d.variance_cube, Cube)
        glpk3d.run_mcmc(max_iterations=50, verbose=False)

    def test_run_mcmc_output(self):
        logger.info("test run mcmc")
        glpk3d = GalPaK3D(self.fits_muse_filename)
        galaxy = glpk3d.run_mcmc(max_iterations=10, verbose=False)

        self.assertIsInstance(galaxy, GalaxyParameters,
                              "Deconvolution should return galaxy parameters")
        self.assertIsInstance(galaxy.stdev, GalaxyParametersError,
                              "Deconvolution should return galaxy parameters with stdev")
        self.assertIsNotNone(glpk3d.deconvolved_cube,
                             "Deconvolution should fill deconvolved_cube property")
        self.assertIsNotNone(glpk3d.convolved_cube,
                             "Deconvolution should fill convolved_cube property")
        self.assertIsNotNone(glpk3d.residuals_cube,
                             "Deconvolution should fill residuals_cube property")
        self.assertIsNotNone(glpk3d.chain,
                             "Deconvolution should fill chain property")
        self.assertIsNotNone(glpk3d.psf3d,
                             "Deconvolution should fill psf3d property")
        self.assertIsNotNone(glpk3d.acceptance_rate,
                             "Deconvolution should fill acceptance_rate property")
        self.assertIsNotNone(glpk3d.galaxy,
                             "Deconvolution should fill galaxy property")
        self.assertIsNotNone(glpk3d.stdev,
                             "Deconvolution should fill stdev property")
        self.assertIs(glpk3d.galaxy, galaxy,
                      "Returned galaxy should be a view to galaxy property")
        self.assertIs(glpk3d.stdev, galaxy.stdev,
                      "Returned galaxy's stdev should be a view to stdev property")

    def test_run_two_instances(self):
        logger.info("test with 2 instances")
        glpk3d_a = GalPaK3D(self.fits_muse_filename)
        galaxy_a = glpk3d_a.run_mcmc(max_iterations=10, verbose=False)
        glpk3d_b = GalPaK3D(self.fits_muse_filename)
        galaxy_b = glpk3d_b.run_mcmc(max_iterations=10, verbose=False)

        self.assertIsInstance(glpk3d_a.galaxy, GalaxyParameters)
        self.assertIsInstance(glpk3d_b.galaxy, GalaxyParameters)

    def test_run_with_variance(self):
        logger.info("test with variance")
        g = GalPaK3D(self.fits_real_muse_filename, variance=self.fits_real_muse_variance, seeing=0.65)
        p = g.run_mcmc(max_iterations=10, verbose=False)

        self.assertIsInstance(p,GalaxyParameters)

    def test_run_with_boundaries(self):

        glpk3d = GalPaK3D(self.fits_muse_filename)
        glpk3d.instrument.psf.fwhm = 0.6
        min_boundaries = GalaxyParameters(x=14.)
        max_boundaries = GalaxyParameters(x=16.)
        galaxy = glpk3d.run_mcmc(max_iterations=10,
                                 min_boundaries=min_boundaries,
                                 max_boundaries=max_boundaries,
                                 verbose=False)

        self.assertTrue(galaxy.x >= min_boundaries.x,
                        "Galaxy's x should be more than min_boundaries's x")
        self.assertTrue(galaxy.x <= max_boundaries.x,
                        "Galaxy's x should be less than max_boundaries's x")

    def test_run_with_doublet(self):
        g = GalPaK3D(self.fits_real_muse_filename)
        model = DefaultModel(line=galpak.OII)
        p = g.run_mcmc(max_iterations=30, verbose=False, model=model)

        self.assertIsInstance(p,GalaxyParameters)

    def test_Cosmology(self):

        m = DefaultModel(redshift=1)
        self.assertIsInstance(m.DeltaVir,float)

    def test_Extention_DefaultModel(self):

        for rc in DefaultModel.CURVE_VALID:
            m = DefaultModel(rotation_curve=rc, redshift=1)
            g = m.Parameters()
            g.from_ndarray(np.arange(len(g)))
            m.set_v22(g)
            m.set_dvdx(g)


    def test_instruments(self):

        muse_nfm = MUSENFM()
        self.assertEqual(muse_nfm.cube_default_xy_step, 0.025)
        muse_wfm = MUSEWFM()
        self.assertEqual(muse_wfm.cube_default_xy_step, 0.2)
        muse = MUSE()
        self.assertEqual(muse.cube_default_xy_step, muse_wfm.cube_default_xy_step,
                         "Default MUSE Field Mode is Wide")

        # ... many additional tests can go here
        kmos = KMOS()
        self.assertEqual(kmos.cube_default_xy_step, 0.2)

        alma = ALMA()
        self.assertEqual(alma.cube_default_xy_step, None)

        alma = ALMA(pixscale=0.1)
        self.assertEqual(alma.cube_default_xy_step, 0.1)

        sinfok1 = SINFOK250()
        self.assertEqual(sinfok1.cube_default_xy_step, 0.125)

        sinfok2 = SINFOK100()
        self.assertEqual(sinfok2.cube_default_xy_step, 0.05)

        sinfoj1 = SINFOJ250()
        self.assertEqual(sinfoj1.cube_default_xy_step, 0.125)

        sinfoj2 = SINFOJ100()
        self.assertEqual(sinfoj2.cube_default_xy_step, 0.05)

        osiris = OSIRIS()
        self.assertEqual(osiris.cube_default_xy_step, 0.035)

        harmoni = HARMONI(pixscale=0.030, psf_fwhm=1.0, lsf_fwhm=0.3)
        self.assertEqual(harmoni.cube_default_xy_step, 0.030)

    def test_models(self):
        inst = MUSEWFM()

        mymodel = DefaultModel()
        glpk3d = GalPaK3D(self.fits_muse_filename, instrument=inst, model=mymodel)
        glpk3d._save_to_file('test_model.txt', glpk3d.model.__str__(), True)
        self.assertTrue(os.path.isfile('test_model.txt'))
        new = GalPaK3D(glpk3d.cube, instrument=inst, model='test_model.txt')
        self.assertEqual(new.model.__str__(), glpk3d.model.__str__())
        os.remove('test_model.txt')

        mymodel = DefaultModel(redshift=0.7)
        glpk3d = GalPaK3D(self.fits_muse_filename, instrument=inst, model=mymodel)
        glpk3d._save_to_file('test_model.txt', glpk3d.model.__str__(), True)
        self.assertTrue(os.path.isfile('test_model.txt'))
        new = GalPaK3D(glpk3d.cube, instrument=inst, model='test_model.txt')
        self.assertEqual(new.model.__str__(), glpk3d.model.__str__())
        os.remove('test_model.txt')

        for flux in ModelSersic.FLUX_VALID:
            for curve in ModelSersic.CURVE_VALID:
                for disp in ModelSersic.DISPERSION_VALID:
                    for thi in ModelSersic.THICKNESS_VALID:
                        mymodel = ModelSersic(flux_profile=flux,rotation_curve=curve,dispersion_profile=disp,thickness_profile=thi,redshift=0.7)
                        glpk3d = GalPaK3D(self.fits_muse_filename, instrument=inst, model=mymodel)
                        glpk3d._save_to_file('test_model.txt', glpk3d.model.__str__(), True)
                        self.assertTrue(os.path.isfile('test_model.txt'))
                        new = GalPaK3D(glpk3d.cube, instrument=inst, model='test_model.txt')
                        self.assertEqual(new.model.__str__(), glpk3d.model.__str__())
                        os.remove('test_model.txt')

        glpk3d = GalPaK3D(self.fits_muse_filename, instrument=self.myinstrument)
        self.assertTrue(glpk3d.instrument.psf.fwhm==0.3)
        self.assertTrue(glpk3d.instrument.lsf.fwhm==7.9)
        self.assertEqual(glpk3d.instrument.__class__, Generic)

    def test_instruments_psf(self):
        glpk3d = GalPaK3D(self.fits_muse_filename)
        self.assertIsInstance(glpk3d.instrument.psf, GaussianPointSpreadFunction,
                              "Gaussian PSF is the default for MUSE when unspecified")

        #for inst in [MUSEWFM(), MUSENFM(), KMOS(), SINFOK250(), ALMA(pixscale=0.1), OSIRIS(), HARMONI(pixscale=30,lsf_fwhm=0.3)]:
        inst = MUSEWFM()
        glpk3d = GalPaK3D(self.fits_muse_filename, instrument=inst)
        glpk3d._save_to_file('test_instrument.txt', glpk3d.instrument.__str__(), True)
        self.assertTrue(os.path.isfile('test_instrument.txt'))
        new = GalPaK3D(glpk3d.cube, instrument='test_instrument.txt')
        self.assertEqual(new.instrument.__str__(),glpk3d.instrument.__str__())
        os.remove('test_instrument.txt')

        inst = MUSENFM()
        glpk3d = GalPaK3D(Cube(data=np.ones((20,30,30))), instrument=inst)
        glpk3d._save_to_file('test_instrument.txt', glpk3d.instrument.__str__(), True)
        self.assertTrue(os.path.isfile('test_instrument.txt'))
        new = GalPaK3D(glpk3d.cube, instrument='test_instrument.txt')
        self.assertEqual(new.instrument.__str__(), glpk3d.instrument.__str__())
        os.remove('test_instrument.txt')

        inst = ALMA(pixscale=0.1)
        glpk3d = GalPaK3D(Cube(data=np.ones((20,30,30))), instrument=inst, crval3=1.0, cdelt3=1.0)
        glpk3d._save_to_file('test_instrument.txt', glpk3d.instrument.__str__(), True)
        self.assertTrue(os.path.isfile('test_instrument.txt'))
        new = GalPaK3D(Cube(data=np.ones((20,30,30))), instrument='test_instrument.txt', crval3=1.0, cdelt3=1.0)
        self.assertEqual(new.instrument.__str__(), glpk3d.instrument.__str__())
        os.remove('test_instrument.txt')

        inst = ALMA()
        glpk3d = GalPaK3D(self.alma_filename, instrument=inst)
        new = GalPaK3D(self.alma_filename, instrument=self.alma_instrument)
        self.assertEqual(glpk3d.instrument.__str__(),new.instrument.__str__())

        inst = KMOS()
        glpk3d = GalPaK3D(Cube(data=np.ones((20,30,30))), instrument=inst, crval3=1.0)
        glpk3d._save_to_file('test_instrument.txt', glpk3d.instrument.__str__(), True)
        self.assertTrue(os.path.isfile('test_instrument.txt'))
        new = GalPaK3D(Cube(data=np.ones((20,30,30))), instrument='test_instrument.txt', crval3=1.0)
        self.assertEqual(new.instrument.__str__(), glpk3d.instrument.__str__())
        os.remove('test_instrument.txt')

        inst = OSIRIS()
        glpk3d = GalPaK3D(Cube(data=np.ones((20,30,30))), instrument=inst)
        glpk3d._save_to_file('test_instrument.txt', glpk3d.instrument.__str__(), True)
        self.assertTrue(os.path.isfile('test_instrument.txt'))
        new = GalPaK3D(glpk3d.cube, instrument='test_instrument.txt')
        self.assertEqual(new.instrument.__str__(), glpk3d.instrument.__str__())
        os.remove('test_instrument.txt')

        inst = HARMONI(pixscale=0.03, psf_fwhm=0.2, lsf_fwhm=1.2)
        glpk3d = GalPaK3D(Cube(data=np.ones((20,30,30))), instrument=inst, crval3=1.0, cdelt3=0.0002)
        glpk3d._save_to_file('test_instrument.txt', glpk3d.instrument.__str__(), True)
        self.assertTrue(os.path.isfile('test_instrument.txt'))
        new = GalPaK3D(Cube(data=np.ones((20,30,30))), instrument='test_instrument.txt', crval3=1.0, cdelt3=0.0002)
        self.assertEqual(new.instrument.__str__(), glpk3d.instrument.__str__())
        os.remove('test_instrument.txt')

        #inst = Generic(psf_fwhm=1, psf_pa=0, psf_ba=1, lsf_fwhm=1.2)
        #glpk3d = GalPaK3D(Cube(data=np.ones((20,30,30))), instrument=inst)
        #glpk3d._save_to_file('test_instrument.txt', glpk3d.instrument.__str__(), True)
        #self.assertTrue(os.path.isfile('test_instrument.txt'))
        #new = GalPaK3D(glpk3d.cube, instrument='test_instrument.txt')
        #self.assertEqual(new.instrument.__str__(), glpk3d.instrument.__str__())
        #os.remove('test_instrument.txt')

        # glpk3d = GalPaK3D(self.fits_muse_filename, instrument=MUSE(psf=None))
        # self.assertIsNone(glpk3d.instrument.psf,
        #                   "PSF should be de-activated when psf=None is specified")

        glpk3d = GalPaK3D(self.fits_muse_filename, instrument=MUSE(psf=MoffatPointSpreadFunction(fwhm=1,beta=2.5,ba=1,pa=0)))
        self.assertIsInstance(glpk3d.instrument.psf, MoffatPointSpreadFunction,
                              "Use specified PSF")

    def test_wavelength_conversion(self):
        glpk3d = GalPaK3D(self.fits_muse_filename)
        params = glpk3d.run_mcmc(max_iterations=100, verbose=False)

        expected = 6743.46774459
        actual = glpk3d.cube.wavelength_of(params.z)
        self.assertEqualish(expected, actual, 95.)

    def test_api(self):

        g = galpak.run(self.fits_real_muse_filename, max_iterations=250, verbose=False)

        self.assertIsInstance(g, GalPaK3D)

    def test_api_auto(self):

        g = galpak.autorun(self.fits_real_muse_filename, max_iterations=250, verbose=False)

        self.assertIsInstance(g, GalPaK3D)

    def test_plotting(self):
        logger.info("test plotting")
        glpk3d = GalPaK3D(self.fits_real_muse_filename)
        glpk3d.run_mcmc(max_iterations=300, verbose=False)

        # MCMC
        glpk3d.plot_mcmc('test_plot_mcmc.png')
        self.assertTrue(os.path.isfile('test_plot_mcmc.png'))
        os.remove('test_plot_mcmc.png')
        #glpk3d.plot_mcmc()
        #glpk3d.plot_mcmc(sort_by_chi=True)

        # IMAGES
        glpk3d.plot_images('test_plot_images.png')
        self.assertTrue(os.path.isfile('test_plot_images.png'))
        os.remove('test_plot_images.png')

        # CoRNER
        glpk3d.plot_corner('test_plot_corner.png')
        if corner_true:
            self.assertTrue(os.path.isfile('test_plot_corner.png'))
            os.remove('test_plot_corner.png')

        # Geweke
        glpk3d.plot_geweke('test_plot_geweke.png')
        self.assertTrue(os.path.isfile('test_plot_geweke.png'))
        os.remove('test_plot_geweke.png')

        #ModelUtilities
        glpk3d.model.plot_vprofile(glpk3d.galaxy, filename='test_rotcurve.png')
        self.assertTrue(os.path.isfile('test_rotcurve.png'))
        os.remove('test_rotcurve.png')

        glpk3d.model.plot_SBprofile(glpk3d.galaxy, filename='test_SBprofile.png')
        self.assertTrue(os.path.isfile('test_SBprofile.png'))
        os.remove('test_SBprofile.png')
        # ANIMATION
        #glpk3d.make_animation()

    def test_save(self):
        logger.info("test save")
        os.system('rm -f test_*')

        glpk3d = GalPaK3D(self.fits_real_muse_filename)
        glpk3d.run_mcmc(max_iterations=300, verbose=False)
        glpk3d.save('test', overwrite=True)

        self.assertTrue(os.path.isfile('test_galaxy_parameters.txt'))
        os.remove('test_galaxy_parameters.txt')
        self.assertTrue(os.path.isfile('test_galaxy_parameters.dat'))
        os.remove('test_galaxy_parameters.dat')
        self.assertTrue(os.path.isfile('test_chain.dat'))
        os.remove('test_chain.dat')
        self.assertTrue(os.path.isfile('test_convolved_cube.fits'))
        os.remove('test_convolved_cube.fits')
        self.assertTrue(os.path.isfile('test_deconvolved_cube.fits'))
        os.remove('test_deconvolved_cube.fits')
        self.assertTrue(os.path.isfile('test_residuals_cube.fits'))
        os.remove('test_residuals_cube.fits')
        self.assertTrue(os.path.isfile('test_3Dkernel.fits'))
        os.remove('test_3Dkernel.fits')

        self.assertTrue(os.path.isfile('test_obs_disp_map.fits'))
        os.remove('test_obs_disp_map.fits')
        self.assertTrue(os.path.isfile('test_obs_flux_map.fits'))
        os.remove('test_obs_flux_map.fits')
        self.assertTrue(os.path.isfile('test_obs_vel_map.fits'))
        os.remove('test_obs_vel_map.fits')

        self.assertTrue(os.path.isfile('test_true_disp_map.fits'))
        os.remove('test_true_disp_map.fits')
        self.assertTrue(os.path.isfile('test_true_flux_map.fits'))
        os.remove('test_true_flux_map.fits')
        self.assertTrue(os.path.isfile('test_true_vel_map.fits'))
        os.remove('test_true_vel_map.fits')

        if glpk3d.error_maps:
            self.assertTrue(os.path.isfile('test_true_disp_map_error.fits'))
            os.remove('test_true_disp_map_error.fits')
            self.assertTrue(os.path.isfile('test_true_flux_map_error.fits'))
            os.remove('test_true_flux_map_error.fits')
            self.assertTrue(os.path.isfile('test_true_vel_map_error.fits'))
            os.remove('test_true_vel_map_error.fits')

        self.assertTrue(os.path.isfile('test_mcmc.png'))
        self.assertTrue(os.path.isfile('test_mcmc.pdf'))
        os.remove('test_mcmc.png')
        os.remove('test_mcmc.pdf')


        self.assertTrue(os.path.isfile('test_images.png'))
        self.assertTrue(os.path.isfile('test_images.pdf'))
        os.remove('test_images.png')
        os.remove('test_images.pdf')

        self.assertTrue(os.path.isfile('test_true_maps.png'))
        self.assertTrue(os.path.isfile('test_true_maps.pdf'))
        os.remove('test_true_maps.png')
        os.remove('test_true_maps.pdf')

        self.assertTrue(os.path.isfile('test_obs_maps.png'))
        self.assertTrue(os.path.isfile('test_obs_maps.pdf'))
        os.remove('test_obs_maps.png')
        os.remove('test_obs_maps.pdf')

        self.assertTrue(os.path.isfile('test_true_Vrot.dat'))
        os.remove('test_true_Vrot.dat')

        self.assertTrue(os.path.isfile('test_instrument.txt'))
        os.remove('test_instrument.txt')
        self.assertTrue(os.path.isfile('test_run_parameters.txt'))
        os.remove('test_run_parameters.txt')

        if corner_true:
            self.assertTrue(os.path.isfile('test_corner.pdf'))
            os.remove('test_corner.pdf')
            self.assertTrue(os.path.isfile('test_corner.png'))
            os.remove('test_corner.png')

        self.assertTrue(os.path.isfile('test_geweke.pdf'))
        os.remove('test_geweke.pdf')
        self.assertTrue(os.path.isfile('test_geweke.png'))
        os.remove('test_geweke.png')

        self.assertTrue(os.path.isfile('test_galaxy_parameters_convergence.dat'))
        os.remove('test_galaxy_parameters_convergence.dat')

        self.assertTrue(os.path.isfile('test_model.txt'))
        os.remove('test_model.txt')

        self.assertTrue(os.path.isfile('test_stats.dat'))
        os.remove('test_stats.dat')

        self.assertTrue(os.path.isfile('test_rotcurve.pdf'))
        os.remove('test_rotcurve.pdf')
        self.assertTrue(os.path.isfile('test_rotcurve.png'))
        os.remove('test_rotcurve.png')

    # def test_load_from_chain_dat(self):
    #     glpk3d = GalPaK3D(self.fits_real_muse_filename)
    #     glpk3d.import_chain('test_chain.dat')
    #     glpk3d.plot_mcmc()



