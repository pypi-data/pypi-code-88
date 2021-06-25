# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from distutils.version import LooseVersion, StrictVersion
import pkg_resources

import os,re
import sys
from copy import deepcopy
import configparser

from astropy.io.fits import Header
import astropy.io.ascii as asciitable
from astropy.table import Table, Column

import math
import numpy as np
np.random.seed(seed=1234)

# LOCAL IMPORTS
from .__version__ import __version__
from .math_utils import merge_where_nan, median_clip, safe_exp

from .instruments import *
from .hyperspectral_cube import HyperspectralCube as HyperCube
from .string_stdout import StringStdOut

from .model_class import Model
from .model_sersic3d import ModelSersic
from .galaxy_parameters import GalaxyParameters, GalaxyParametersError
from .plot_utilities import Plots
from .mcmc import MCMC

#will be removed
DiskModel = ModelSersic #for backward compatibility
DefaultModel = ModelSersic

OII = {'wave': [3726.2, 3728.9], 'ratio':[0.8,1.0]}

# LOGGING CONFIGURATION
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('GalPaK')



# OPTIONAL IMPORTS
try:
    import bottleneck as bn
except ImportError:
    logger.info(" bottleneck (optional) not installed, performances will be degraded")
    import numpy as bn
try:
    import pyfftw
except ImportError:
    logger.info(" PyFFTW (optional) not installed, performances will be degraded")
try:
    import mpdaf
    logger.info("Found MPDAF version %s" % (mpdaf.__version__))
    mpdaf_there=True
except ImportError:
    mpdaf_there=False
    logger.warning(" MPDAF (optional) not installed / not required")
try:
    import emcee
    emcee_there=True
    logger.info("Found EMCEE version %s" % (emcee.__version__))
    logger.warning("EMCEE tested for version > 3.0")
except ImportError:
    emcee_there=False
    logger.warning(" EMCEE (optional) not installed / not required. So option use_emcee is disabled")
try:
    import dynesty
    dynesty_there=True
    logger.info("Found Dynesty version %s \n EXPERIMENTAL and UNSUPPORTED" % (dynesty.__version__))
except ImportError:
    dynesty_there=False
    logger.warning(" Dynesty (optional) not installed / not required. ")
try:
    import pymultinest
    multinest_there=True
    logger.info("Found PyMultinest version %s" % (pkg_resources.get_distribution("pymultinest").version))
except ImportError:
    multinest_there=False
    logger.warning(" PyMultinest (optional) not installed / not required. ")



#Python3 compatibility
try:
  basestring
except NameError:
  basestring = str

if sys.version>='2.7' and sys.version<'3.5':
    reload(sys)
    sys.setdefaultencoding('utf-8')


class GalPaK3D(Plots, MCMC):
    """
    GalPaK3D is a tool to extract Galaxy Parameters and Kinematics from
    3-Dimensional data, using reverse deconvolution with Bayesian analysis
    Markov Chain Monte Carlo. (random walk)

    cube: HyperspectralCube|string
        The actual data on which we'll work ; it should contain only one galaxy.
        Can be a HyperspectralCube object, a string filename to a FITS file, or
        even MPDAF's ``mpdaf.obj.Cube``.
    seeing: float
        Aka the Point Spread Function's Full Width Half Maximum.
        This convenience parameter, when provided, will override the FWHM value
        of the instrument's PSF.
    instrument: Instrument
        The instrument configuration to use when simulating convolution.
        The default is :class:`MUSE <galpak.MUSE>`.
    crval3: float
        A value for the cube's header's CRVAL3 when it is missing.
        You should update your cube's header.
    crpix3: float
        A value for the cube's header's CRPIX3 when it is missing.
        You should update your cube's header.
    cunit3: float
        A value for the cube's header's CUNIT3 when it is missing.
        You should update your cube's header.
    cdelt3: float
        A value for the cube's header's CDELT3 when it is missing.
        You should update your cube's header.
    cunit1: float
        A value for the cube's header's CUNIT1 (&2) when it is missing.
        You should update your cube's header.
    force_header_update: bool
        Set to True to force the update of the above header cards,
        when their values are not missing.
        Note: These will not be saved into the FITS file. (if the cube is one)

    """
    logger.info(' Running galpak ' + __version__)

    def __init__(self, cube, variance=None, model=None,
                 seeing=None, instrument=None, quiet=False,
                 crval3=None, crpix3=None, cunit3=None, cdelt3=None, ctype3=None, cunit1=None,
                 force_header_update=False):

        # DEVS : If you change the signature above,
        # remember to update the run() in api.py

       # Prepare output attributes
        self.acceptance_rate = 100.
        self.galaxy = GalaxyParameters()
        self.stdev = GalaxyParameters()
        self.chain = None
        self.sub_chain = None

        self.psf3d = None
        self.convolved_cube = None
        self.deconvolved_cube = None
        self.residuals_cube = None
        self.residuals_map = None
        self.variance_cube = None
        #true intrinsic maps
        self.true_flux_map = None
        self.true_velocity_map = None
        self.true_disp_map = None
        self.error_maps = False
        self.true_flux_map_error = None
        self.true_velocity_map_error = None
        self.true_disp_map_error = None
        #observed maps
        self.obs_flux_map = None
        self.obs_velocity_map = None
        self.obs_disp_map = None

        self.max_iterations = None
        self.method = None
        self.chain_fraction = None
        self.percentile = None
        self.initial_parameters = None
        self.min_boundaries = None
        self.max_boundaries = None
        self.known_parameters = None
        self.random_scale = None
        self.reduce_chi = None
        self.chi_stat = 'gaussian'
        self.chi_at_p = None
        self.best_chisq = None
        self.stats = None
        self.BIC = None
        self.DIC = None
        self.mcmc_method = None
        self.mcmc_sampling = None
        #self.redshift = None

        # Assign the logger to a property for convenience, and set verbosity
        self.logger = logger
        self.version = __version__
        self.config = configparser.RawConfigParser()

        self.model = None
        if quiet:
            self._set_verbose(None)
            self.verbose=None
        else:
            self._set_verbose(True)

        # Set up the input data cube
        if isinstance(cube, basestring):
            self.logger.info('Reading cube from %s' % (cube))
            cube = HyperCube.from_file(cube, verbose=not quiet)
        elif isinstance(cube, HyperCube):
            self.logger.info('Provided cube is a HyperSpectral Object')
        elif mpdaf_there:
            if isinstance(cube, mpdaf.obj.Cube):
                self.logger.info('Provided Cube is a mpdaf Cube object')
                cube = HyperCube.from_mpdaf(cube, verbose=not quiet)
            else:
                raise TypeError("Provided cube is not a HyperspectralCube "
                                    "nor mpdaf's Cube")
        else:
                raise TypeError("Provided cube is not a HyperspectralCube ")
        if cube.is_empty():
            raise ValueError("Provided cube is empty")
        self.cube = cube

        if not self.cube.has_header():
            self.logger.info("Reading hyperspectral cube without header. "
                             "Creating a minimal one.")
            self.cube.header = Header()

        # GalPaK needs a sane Cube
        #self.cube.sanitize()

        # Set up the variance
        if variance is not None:
            self.logger.info('Using user-provided variance input')
            if isinstance(variance, basestring):
                self.logger.info("Read provided variance cube   %s into HyperCube." % (variance))
                variance_cube = HyperCube.from_file(variance)
            elif isinstance(variance, HyperCube):
                variance_cube = variance
                if variance_cube.data is None:
                    self.logger.warning("Provided variance cube is empty.")
                else:
                    self.logger.info("Saving variance into varianceCube")
                if variance_cube.filename == None:
                    variance_cube.filename = 'Variance_cube_from_user'
            elif isinstance(variance, np.float):
                variance_cube = HyperCube(variance)
                variance_cube.filename = 'Variance_float_from_user={:.2e}'.format(variance)
            elif not (isinstance(variance,np.float) or  isinstance(variance, HyperCube) or isinstance(variance, basestring)):
                raise TypeError("Provided variance is not a string nor HyperCube nor a float")
        else:
            variance_cube = HyperCube(self.cube.var, filename='Variance_from_cube_extension')


        # Set up the instrument's context
        if instrument is None:
            instrument = MUSE()
            self.logger.warning('Using the MUSE instrument per default. '
                                'You should specify your own instrument.')
        if isinstance(instrument, basestring):
            #read config
            instrument = self._read_instrument(instrument)
            #raise ValueError("Instrument needs to be an instance of "
            #                 "Instrument, not a string.")
        if not isinstance(instrument, Instrument):
            raise ValueError("Instrument needs to be an instance of Instrument")
        self.instrument = instrument

        ## Set default cube specs from instrument when missing from headers
        # as we don't want to rely on the input fits having properly set headers.
        # So, we aggregate in the cube our own specs (in " and µm) for our personal use :
        # - xy_step
        # - z_step
        # - z_central

        # 1. Patch up the HyperCube's missing values
        try:
            self.cube.patch(
                crval3=crval3, crpix3=crpix3, cunit3=cunit3,
                cdelt3=cdelt3, ctype3=ctype3, cunit1=cunit1, force=force_header_update
            )
        except ValueError:
            raise ValueError("The cube already has one of the header cards "
                             "you're trying to provide. "
                             "Use force_header_update=True to override.")

        self.logger.debug('Header after patch : %s' % self.cube)
        #set xy_step z_step and z_central

        # 2. Set cube metadata from the the instrument if header is incomplete
        self.cube.defaults_from_instrument(instrument=instrument)

        # 3. Initialize steps xy_steps z_steps z_cunnit and z_central
        self.cube.initialize_self_cube()

        # 4. Calibrate the instrument with the cube
        self.instrument.use_pixelsize_from_cube(self.cube)

        self.logger.debug('z central : %4.e' % (self.cube.z_central) )

        # Override the PSF FWHM (aka. seeing) if provided
        if seeing is not None and self.instrument.psf is not None:
            try:
                self.instrument.psf.fwhm = seeing
            except AttributeError:
                raise IOError("You provided a seeing but your instrument's PSF has no FWHM.")

        # Handle the variance, when provided, or generate one
        variance_data = variance_cube.data
        if variance_data is not None:
            self.logger.info("Replacing 0s in the variance cube by 1e12")
            variance_data = np.where(variance_data == 0.0, 1e12, variance_data)
        else:
            # Clip data, and collect standard deviation sigma
            self.logger.warning("No variance provided. Estimating Variance from edge statistics")
            clipped_data, clip_sigma, __ = median_clip(self.cube.data[:, 2:-4, 2:4], 2.5)#yband at x[2:4]
            self.logger.info("Computed stdev from the edges: sigma=%.e" % clip_sigma)
            # Adjust stdev margin if it is zero, as we'll divide with it later on
            if not np.isfinite(clip_sigma):
                clipped_data, clip_sigma, __ = median_clip(self.cube.data, 2.5)
                self.logger.info("reComputing stdev from the whole cube: sigma=%.e" % clip_sigma)

            if np.size(clip_sigma) == 1 and clip_sigma == 0:
                clip_sigma = 1e-20
            variance_data = clip_sigma ** 2 *np.ones_like(self.cube.data)
            self.logger.info('Variance estimated is %s ' % (str(clip_sigma**2)))
        # Save the variance cube
        variance_cube.data = variance_data
        self.variance_cube = variance_cube   # cube of sigma^2
        self.error_cube = np.sqrt(self.variance_cube.data)  # cube of sigmas

        # Provide the user with some feedback
        self.logger.info("Setting up with the following setup :\n%s" % self.instrument)

        # 5. Init model
        #  Set up the model context
       #  Set up the model context
        if isinstance(model, basestring)==True:
            model = self._read_model(deepcopy(model))
        if model is not None:
            self._init_model(model)
            self.logger.info("Setting up the model : %s" % (self.model.__name__()))
            self.logger.info("Model setup :\n%s" % (self.model) )

    def _init_model(self, model):

        # Set up the simulation model
        if model is not None:
            self.model = model
            self.logger.info("Init boundaries from model '%s'" %(self.model.__name__()))
            self.model_dict = self.model.__dict__

            #important:
            self.model.pixscale = self.cube.xy_step

            # Compute a flux estimation
            # fixme: add weighted sum with variance if present
            self.flux_est = bn.nansum(self.cube.data)
            if self.flux_est < 0:
                self.logger.warning(
                    "WARNING: Initial flux (%4.2e) is <0 -- "
                    "likely wrong, will recompute it ignoring <0 values"
                    % self.flux_est
                )
                self.flux_est = np.sum(np.where(self.cube.data > 0, self.cube.data, 0))
                self.logger.warning('Initial flux is now %4.2e' % self.flux_est)
                self.logger.info('TIP: use `initial_parameters=` to set the flux')
            else:
                self.logger.info('Initial flux is %4.2e' % self.flux_est)

            # Default boundaries
            self.min_boundaries = self.model.min_boundaries(self)
            self.max_boundaries = self.model.max_boundaries(self)

            # Default initial parameters
            self.initial_parameters = (self.max_boundaries + self.min_boundaries) / 2.

            #set known parameters to ones
            self.known_parameters = self.model.Parameters()


    def run_mcmc(self, max_iterations=15000,
                 method_chain='last',
                 last_chain_fraction=60,
                 percentile=95,
                 model=None,
                 chi_stat='gaussian',
                 mcmc_method='galpak',
                 mcmc_sampling=None,
                 min_boundaries=None,
                 max_boundaries=None,
                 known_parameters=None,
                 initial_parameters=None,
                 random_scale=None,
                 min_acceptance_rate=10,
                 verbose=True,
                 emcee_nwalkers=30,
                 **kwargs):
        # DEVS : If you change the signature above,
        # remember to update the run() in api.py
        """
        Main method_chain of GalPak, computes and returns the galaxy parameters
        as a :class:`GalaxyParameters <galpak.GalaxyParameters>` object
        using reverse deconvolution with a MCMC.

        Also fills up the following attributes :
            - chain
            - psf3d
            - deconvolved_cube
            - convolved_cube
            - residuals_cube (Data-Model in units of sigma)
            - residuals_map (average of data-model in units of sigma or = 1/N_z.
                             Sum_z Residuals_cube.  sqrt(Nz) )
            - acceptance_rate
            - galaxy (same object as returned value)
                      with Vmax forced to be positive [and 180 added to PA]
            - stdev (also available as galaxy.stdev)
            - true_flux_map
            - true_velocity_map
            - true_disp_map

        Stops iteration if acceptance rate drops below ``min_acceptance_rate`` %
        or when ``max_iterations`` are reached.

        max_iterations: int
            Maximum number of useful iterations.

        method_chain: 'chi_sorted' | 'chi_min' | 'last' | 'MAP'
            Method used to determine the best parameters from the chain.
                - 'last' (default) : mean of the last_chain_fraction(%) last parameters of the chain
                - 'chi_sorted' : mean of the last_chain_fraction(%) best fit parameters of the chain
                - 'chi_min' : mean of last_chain_fraction(%) of the chain around the min chi
                - 'MAP': Parameters at Maximum At Posteriori, i.e. at chi_min

        last_chain_fraction: int
            Last Chain fraction (in %) used to compute the best parameters.
            Defaults to 60.

        model = DefaultModel()
            see class DiskModel or ModelSersic

        chi_stat: 'gaussian' [default] | 'Mighell' | 'Neyman' | 'Cstat' | 'Pearson'
            The chi2 statitics
            https://heasarc.gsfc.nasa.gov/xanadu/xspec/manual/XSappendixStatistics.html
                - 'gaussian' (default): Sum (D - M)^2 / e
                - 'Neyman'  Sum (D - M )^2 / max(D,1)
                - 'Mighell' Sum (D + min(D,1) - M)^2 / (D+1)  Mighell http://adsabs.harvard.edu/abs/1999ApJ...518..380M
                - 'Cstat' Sum ( M - D + D * log(D/M) ) Cash statistique Humphrey 2009, http://adsabs.harvard.edu/abs/2009ApJ...693..822H
                - 'Pearson'  Sum ( M - D )^2 / M  Pearson statistic  Humphrey 2009, http://adsabs.harvard.edu/abs/2009ApJ...693..822H


        mcmc_method: 'galpak' [default] | 'emcee_walkers'| 'emcee_MH' | 'dynesty' | 'multinest'
            The MCMC method.
                - galpak:   for the original MCMC algorithm using Cauchy proposal distribution
                - emcee_MH: emcee Metropolis Hasting
                - emcee_walkers: emcee multi-Walkers algorithms with Moves if version>=3.0
                - dynesty: unsupported
                - multinest: using Importance Nested Sampling w/ pyMultinest
                - pymc3: to be implemented

        mcmc_sampling: None [default] | 'Cauchy'  | 'Gaussian' | 'DE' | 'walkers'
            The sampling proposal distribution
            - 'Cauchy' default when mcmc_method = 'galpak' or 'emcee_MH'
            - 'walkers' (=StretchMove) default when mcmc_method ='emcee_walkers'

        min_boundaries: ndarray|GalaxyParameters
            The galaxy parameters will never be less than these values.
            Will override the default minimum boundaries for the parameters.
            If any of these values are NaN, they will be replaced by the default ones.

        max_boundaries: ndarray|GalaxyParameters
            The galaxy parameters will never be more than these values.
            Will override the default minimum boundaries for the parameters.
            If any of these values are NaN, they will be replaced by the default ones.

        known_parameters: ndarray|GalaxyParameters
            All set parameters in this array will be skipped in the MCMC,
            the algorithm will not try to guess them.

        initial_parameters: ndarray|GalaxyParameters
            The initial galaxy parameters of the MCMC chain.
            If None, will use the inital parameters provided by the model.
            The galaxy parameters not initialized by the model or by this
            parameter will be set to the mean of the boundaries.


        random_scale: float
            Scale the amplitude of the MCMC sampling by these values.
            This is an important parameter to adjust for reasonable acceptance rate.
            The acceptance rate should be around 30-50%.
            If the acceptance rate is <20-30% (too low), decrease random_scale
            IF the acceptance rate is >50-60% (too high), increase random_scale

        verbose: boolean
            Set to True to output a detailed log of the process.
            The run is faster when this is left to False.

        """
        # DEVS : If you change the signature above,
        # remember to update the run() in api.py

        #re initialize psf
        self.instrument.psf3d_fft = None

        # Save the parameters (the animation uses them)
        self.max_iterations = max_iterations
        self.method = method_chain
        self.chain_fraction = last_chain_fraction
        self.chi_stat = chi_stat
        self.percentile = percentile
        self.verbose = verbose

        #save intermediate model maps
        self.error_maps = None #will be set later
        self.chain_flux_map = []
        self.chain_velocity_map = []
        self.chain_dispersion_map = []

        # Set up the simulation model
        if model is None:
            if self.model is not None:
                self.logger.warning("Model already specified: '%s'" % (self.model.__name__()))
            else:
                self.model = DefaultModel()
                self.logger.warning("Will use default model '%s'" %(self.model.__name__()))
                self.logger.info("Model setup :\n%s" % (self.model) )

        elif model is not None:
            if isinstance(model, basestring):
                #read from config file
                self.model = self._read_model(model)
                self.logger.info("Model set to %s from file: %s" % (self.model.__name__(), self.model) )
            elif isinstance(model, Model):
                self.logger.warning("Model was already set")
                self.model = model
                self.logger.info("Model set to %s : %s" % (self.model.__name__(), self.model))
            else:
                raise ValueError
        self._init_model(self.model)

        #For backwards compatibility:
        ## will be removed in the future
        #if self.model.line is None:
        #    self.model.line = self.line
        #else:
        #    self.line = self.model.line
        #save attribute
        #For backwards compatibility:
        ## will be removed in the future
        ## if not None, computes Mdyn(Re)
        #if self.model.redshift is not None:
        #    self.redshift = self.model.redshift


        # Sanitize data and set arbitrary big stdev where NaNs are
        #cube_data = self.cube.data
        #cube_data = np.nan_to_num(cube_data)

        # Set verbosity
        self._set_verbose(verbose)


        dim_p = np.size(GalaxyParameters())

        # In fraction of boundary space, an arbitrarily
        # small value for closeness to boundaries
        self.eps = 0.003


        # Merge provided boundaries (if any) with default boundaries
        if isinstance(min_boundaries, basestring):
            min_boundaries = self._read_params(deepcopy(min_boundaries),'MIN')
        if isinstance(max_boundaries, basestring):
            max_boundaries = self._read_params(deepcopy(max_boundaries),'MAX')

        if min_boundaries is not None:
            min_boundaries = deepcopy(min_boundaries)
            merge_where_nan(min_boundaries, self.min_boundaries) #this returns a ndarray
            self.min_boundaries = GalaxyParameters().from_ndarray(min_boundaries)
        if max_boundaries is not None:
            max_boundaries = deepcopy(max_boundaries)
            merge_where_nan(max_boundaries, self.max_boundaries) #this returns a ndarray
            self.max_boundaries = GalaxyParameters().from_ndarray(max_boundaries)


        bug_boundaries = self.min_boundaries > self.max_boundaries
        if bug_boundaries.any():
            self.logger.debug("Min Boundaries : %s", self.min_boundaries)
            self.logger.debug("Max Boundaries : %s", self.max_boundaries)
            raise ValueError("Boundaries are WRONG, because min > max")

        # Default initial parameters
        self.initial_parameters = self.model.initial_parameters(self)

        # Create initial galaxy parameters using mean and provided values
        mean_parameters = (self.max_boundaries + self.min_boundaries) / 2.
        #complete default values with mean parameters
        merge_where_nan(self.initial_parameters, mean_parameters)
        self.logger.info("Default Param_init : %s", self.initial_parameters)

        # read initial parameter from config file
        if isinstance(initial_parameters, basestring):
            initial_parameters = self._read_params(deepcopy(initial_parameters), 'INIT')

        # Merge provided initial parameters (if any) with the defaults
        if initial_parameters is not None:
            #complete input with default values
            template = self.model.Parameters()
            merge_where_nan(template, initial_parameters)
            merge_where_nan(template, self.initial_parameters)
            self.initial_parameters = template

        self.logger.info("Initial parameters : %s", self.initial_parameters)

        # By default, try to guess all parameters
        should_guess_flags = np.ones(dim_p)  # 0: we know it / 1: try to guess

        #if using input image
        # @fixme; this is unused
        if self.model_dict['flux_profile'] == 'user' and known_parameters is None:
                raise self.logger.error(
              "With an input image it is advised to freeze "
              "the `inclination`, using `known_parameters=`.")

        # Flag parameters that we manually specified and don't need to guess
        if isinstance(known_parameters, basestring):
            known_parameters = self._read_params(deepcopy(known_parameters), 'KNOWN')

        if known_parameters is not None:
            if len(known_parameters) != dim_p:
                raise ValueError("The `known_parameters=` must be an array of "
                                 "length %d, or even better an instance of `%s`"
                                 % (dim_p, self.model.parameters_class()))
            else:
                merge_where_nan(self.known_parameters, known_parameters)

        self.logger.info("Using known parameters: %s", self.known_parameters)

        # Freeze the known parameters by flagging them as not-to-guess
        for idx in range(dim_p):
            parameter = self.known_parameters[idx]
            if not math.isnan(parameter):
                should_guess_flags[idx] = 0
                sign = math.copysign(1., parameter)
                self.min_boundaries[idx] = parameter * (1 - self.eps * sign) - self.eps
                self.max_boundaries[idx] = parameter * (1 + self.eps * sign) + self.eps
                self.initial_parameters[idx] = parameter

        # The setup is finished, let's dump some information
        self.logger.info("Min Boundary: %s", self.min_boundaries)
        self.logger.info("Max Boundary: %s", self.max_boundaries)

        # The setup is done, we can now start the MCMC loop.
        if isinstance(random_scale, basestring):
            random_scale = self._read_params(deepcopy(random_scale), 'RSCALE')

        self.random_scale = random_scale
        random_amplitude = self._init_sampling_scale(random_scale, should_guess_flags)

        # Zero random amplitude where parameters are known
        random_amplitude = random_amplitude * should_guess_flags
        self.random_amplitude = random_amplitude


        self.logger.info("Starting with χ² = %f", self.compute_chi(self.initial_parameters) / self.Ndegree)

        ## The actual MCMC #####################################################
        #self.error_maps = save_error_maps #save intermediate model maps

        #set walkers
        if mcmc_method == 'galpak' and mcmc_sampling is None:
            mcmc_sampling = 'Cauchy'
        #if mcmc_method == 'emcee_MH' and mcmc_sampling is None:
        #    mcmc_sampling = 'Cauchy'
        if mcmc_method == 'emcee_walkers' and mcmc_sampling is None:
            mcmc_sampling = 'walkers'

        self.mcmc_method = mcmc_method
        self.mcmc_sampling = mcmc_sampling


        #burnin = np.int(0.15*self.max_iterations)
        if mcmc_method == 'galpak':
            chain = self.myMCMC(max_iterations, random_amplitude, sampling_method=mcmc_sampling, min_acceptance_rate=min_acceptance_rate)
        elif mcmc_method == 'emcee_MH' and emcee_there:
            #DEFAULT EMCEE parameters for EnsembleSampler(EMCEE)
            pass

        elif mcmc_method == 'emcee_walkers' and emcee_there:
            #DEFAULT EMCEE parameters for EnsembleSampler(EMCEE)

            #kwargs_sampler = {
            #        'pool':None,  \
            #        'backend':None,\
            #        'vectorize':False,\
            #        'blobs_dtype':None,\
            #        'postargs':None,\
            #        'threads': 1,
            #        }
            emcee_threads = 4
            kwargs_emcee ={
                     'store': True, \
                     'tune': True, \
                    'thin': 30
                    }
            #update default parameters
            kwargs_emcee.update(kwargs)

            #@fixme: need to accept parallelize
            pos0 = np.array([self.initial_parameters * (1+1e-3*np.random.randn(dim_p)) for i in range(emcee_nwalkers) ])
            self.logger.critical("Running EMCEE with %d walkers on %d iterations" % (emcee_nwalkers, self.max_iterations))

            if LooseVersion(emcee.__version__)<LooseVersion('3.0'):
                raise Exception("EMCEE version not supported ", emcee.__version__)

            #EMCE version3
            if mcmc_sampling == 'Cauchy':
                from .mcmc import CauchyMove
                myMove=CauchyMove(self.random_amplitude.as_vector()**2)
                self.logger.critical("Running EMCEE Walkers with Cauchy Sampling")
            elif mcmc_sampling == 'Normal':
                from emcee.moves import GaussianMove
                myMove=GaussianMove(self.random_amplitude.as_vector()**2)
                self.logger.info("Random Ampl : %s", self.random_amplitude.as_vector())
                self.logger.critical("Running EMCEE Walkers with Gaussian Sampling")
            elif mcmc_sampling == 'DE':
                from emcee.moves import DEMove
                myMove=DEMove()
                self.logger.critical("Running EMCEE Walkers with DE Sampling")
            elif mcmc_sampling == 'Snooker':
                from emcee.moves import DESnookerMove
                myMove=DESnookerMove()
                self.logger.critical("Running EMCEE Walkers with Snooker Sampling")
            elif mcmc_sampling == 'walkers':
                myMove = None #default StretchMove from EMCEE
                self.logger.critical("Running EMCEE Walkers with default Stretch Sampling")
            elif mcmc_sampling == 'walkersCauchy':
                from .mcmc import CauchyMove
                #50/50 StretchMove and CauchyMove
                myMove = [  (emcee.moves.StretchMove(),0.6), (CauchyMove(self.random_amplitude.as_vector()**2),0.4)]
                self.logger.critical("Running EMCEE Walkers with 60/40 StretchMove() & Cauchy Sampling")
            else:
                raise Exception("mcmc_sampling not valid. Options are  ", self.SAMPLING_VALID)
            kwargs_emcee.update(kwargs)
            #Multiprocessing
            #try:
            #    from multiprocessing import Pool
            #    self.logger.info("Running EMCEE with multiprocessing")
            #    with Pool() as pool:
            #        self.sampler = emcee.EnsembleSampler(emcee_nwalkers, dim_p, self, moves=myMove, pool=pool)
            #        if self.verbose is not True:
            #            self.sampler.run_mcmc(pos0, self.max_iterations, progress=True, **kwargs_emcee)
            #        else:
            #            for state in self.sampler.sample(pos0, iterations=self.max_iterations, **kwargs_emcee):
            #                for k, r in enumerate(state.coords):
            #                    print("%d %s log L=%f" % (self.sampler.iteration, self.model.Parameters().from_ndarray(r), \
            #                                              state.log_prob[k]))


            #except ImportError:
            self.logger.info(" Running EMCEE with 4 threads")
            self.sampler = emcee.EnsembleSampler(emcee_nwalkers, dim_p, self, moves=myMove, threads=4)


            if self.verbose is not True:
                self.sampler.run_mcmc(pos0, self.max_iterations, progress=True, **kwargs_emcee)
            else:
                for state in self.sampler.sample(pos0, iterations=self.max_iterations, **kwargs_emcee):
                    for k,r in enumerate(state.coords):
                        print("%d %s log L=%f" %(self.sampler.iteration, self.model.Parameters().from_ndarray(r),\
                                             state.log_prob[k]))

            self.sampler.__dict__['kwargs'] = kwargs_emcee

            self.acceptance_rate = self.sampler.acceptance_fraction
            self.logger.info("EMCEE MH: Acceptance: %s " % (self.sampler.acceptance_fraction))
            #self.logger.info("EMCEE MH: Naccepted states ",  (self.sampler.naccepted))
            #flat_chain = self.sampler.get_chain(discard=burnin, flat=True)
            chain_data = self.sampler.flatchain
            chain = Table(chain_data, names=self.model.Parameters().names)
            lnprob = self.sampler.flatlnprobability
            chain.add_column(Column(-2*lnprob / self.Ndegree), name='reduced_chi')

        #using dynesty
        elif mcmc_method == 'dynesty' and dynesty_there:
            # "Dynamic" nested sampling.
            #
            nlive = 500
            self.sampler = dynesty.DynamicNestedSampler(self.loglike, self.ptform, dim_p \
                                                        , bound='single' #to force posterior weights
                                                        , sample='unif' #unif/hscale
                                                        )
            kwargs_dynesty = {'nlive_init': 30 , 'nlive_batch': 200 }
            kwargs_dynesty.update(kwargs)

            self.logger.critical('EXPERIMENTAL Running Dynesty with ', kwargs_dynesty)
            self.sampler.run_nested(wt_kwargs={'pfrac': 0.9} #posterior based
                                    , maxiter = self.max_iterations
                                    , **kwargs_dynesty
                                    )

            self.dresults = self.sampler.results

            chain_data = self.dresults.samples
            chain = Table(chain_data, names=self.galaxy.names)
            lnprob = self.dresults.logz
            chain.add_column(Column(-2*lnprob / self.Ndegree), name='reduced_chi')

        #using pymultinest
        elif mcmc_method == 'multinest' and multinest_there:
            """
                run(LogLikelihood, Prior, n_dims, n_params=None, n_clustering_params=None,
                wrapped_params=None, importance_nested_sampling=True, multimodal=True,
                const_efficiency_mode=False, n_live_points=400, evidence_tolerance=0.5,
                sampling_efficiency=0.8, n_iter_before_update=100, null_log_evidence=-1e+90,
                max_modes=100, mode_tolerance=-1e+90, outputfiles_basename=u'chains/1-',
                seed=-1, verbose=False, resume=True, context=0, write_output=True,
                log_zero=-1e+100, max_iter=0, init_MPI=True, dump_callback=None)
            """

            if 'outpath' not in kwargs.keys():
                outpath = './pymulti'
                if os.path.isdir(outpath) is False:
                    os.mkdir(outpath)
                output = outpath + '/out'
            else:
                output = kwargs['outpath']
                kwargs.pop('outpath')

            #default parameters
            kwargs_multi={'n_live_points': 200, \
                        'evidence_tolerance':0.5, \
                        'n_iter_before_update' : 200, \
                        'const_efficiency_mode' : False, \
                        'sampling_efficiency':0.8, \
                        'resume' : False}
            kwargs_multi.update(kwargs)

            self.logger.critical("Running MultiNest with ", kwargs_multi)
            self.logger.info(" Multinest, ignoring max_iteration")

            pymultinest.run(self.pyloglike, self.pycube, n_dims= dim_p, \
                max_iter=0, verbose=self.verbose, \
                outputfiles_basename=output, **kwargs_multi)

            # create analyzer object
            #embedded in solve
            analyzer = pymultinest.Analyzer(dim_p, outputfiles_basename = output)


            # get a dictionary containing information about
            #   the logZ and its errors
            #   the individual modes and their parameters
            #   quantiles of the parameter posteriors
            data = analyzer.get_data()[:,:-1]
            #print(data.shape)

            stats = analyzer.get_mode_stats()

            #lnZ = stats['evidence']

            #  iterate through the "posterior chain"
            #for params in a.get_equal_weighted_posterior():
            #        print(params)

            samples = analyzer.get_equal_weighted_posterior()
            #print(chain_data.shape)

            chain = Table(samples[:,:-1], names=self.galaxy.names)

            lnprob = samples[:,-1]

            chain.add_column(Column(-2*lnprob / self.Ndegree), name='reduced_chi')

            # get the best fit (highest likelihood) point
            #bestfit_params = stats['modes'][0]['mean']
            #bestfit_params = stats['modes'][0]['maximum']
            #bestfit_params = stats['modes'][0]['maximum a posterior']
            #OR
            #bestfit_params = stats.get_best_fit()['parameters']

            self.sampler = dict(samples = samples, stats=stats, \
                kwargs=kwargs_multi
                )



        elif mcmc_method == 'pymc3':
            raise NotImplementedError

        elif mcmc_method == 'pynuts':
            raise NotImplementedError
        else:
            raise Exception("method_mcmc %s not valid. Used of of %s" % (mcmc_method, self.MCMC_VALID))

        # Store chain
        self.logger.info("self.chain : full Markov chain")
        #good_idx = np.where(chain['reduced_chi']!=0)
        #self.chain = Table(chain[good_idx])
        # Sanitize the chain if vel <0
        self.model.sanitize_chain(chain)
        self.chain = chain

        # Store PSF 3D, which may not be defined
        try:
            self.psf3d = HyperCube(self.instrument.psf3d)
        except AttributeError:
            pass

        # Extract Galaxy Parameters from chain, and store them
        self.logger.info("Extracting best parameters (medians) from chain")
        self.best_parameters_from_chain(method_chain, last_fraction=last_chain_fraction, percentile=percentile)

        # Create output cubes
        self.logger.info("self.convolved_cube : simulated convolved cube from found galaxy parameters")
        self.convolved_cube = self.create_convolved_cube(self.galaxy, self.cube.shape)
        self.convolved_cube.header = self.cube.header
        self.logger.info("self.deconvolved_cube : deconvolved cube from found galaxy parameters")
        self.deconvolved_cube = self.create_clean_cube(self.galaxy, self.cube.shape, final=True)
        self.deconvolved_cube.header = self.cube.header
        self.logger.info("self.residuals_cube : diff between actual data and convolved cube, scaled by stdev margin")
        self.residuals_cube = (self.cube - self.convolved_cube) / self.error_cube  # * np.mean(variance_cube)
        self.residuals_cube.header = self.cube.header
        #compute observed maps
        #_ = self._make_moment_maps(self.convolved_cube, mask=True) # make moment maps with cube convolved with 3DPSF
        _ = self._make_maps_Epinat(self.convolved_cube, mask=True)
        # Average of residuals, normalized to sigma_mu
        nz = self.residuals_cube.shape[0]
        self.residuals_map = (self.residuals_cube.data.sum(0) / nz) * np.sqrt(nz)

        # Compute the χ²
        self.compute_stats()
        self.logger.info("χ² at best param: %f", self.chi_at_p)
        self.logger.info("Best min χ², %f ", self.best_chisq)

        self.logger.info("BIC (full) : %f ", self.BIC)
        self.logger.info("DIC : %f ", self.DIC)


        # Show a plot of the chain if verbose, to draw attention to the chain
        if verbose:
            # Sometimes, when the number of iterations is low, plotting fails.
            # It is a complex issue with matplotlib, so we're 'try'-wrapping it.
            try:
                self.plot_mcmc(adapt_range='5stdev')
            except:
                pass

            try:
                self.plot_geweke()
            except:
                pass

        return self.galaxy


    def best_parameters_from_chain(self, method_chain='last', last_fraction=60, percentile=95):
        """
        Computes best fit galaxy parameters from chain, using medians from a specified method_chain.

        method_chain: string 'last' | 'chi_sorted' | 'chi_min' | 'MAP'
            The method to use to extract the fittest parameters from the chain.
            'last' (default) : mean of the last_fraction(%) last parameters of the chain
            'chi_sorted' : mean of the last_fraction(%) best fit parameters of the chain
            'chi_min' : mean of last_fraction(%) of the chain around the min chi
            'MAP': Parameters at Maximum At Posteriori, i.e. at chi_min
        last_fraction: float % (60 as default)
            Fraction of the end of the chain used in determining the parameters.
        percentile: float % (95 as default)
            None: the method to use to compute the errors on the parameter is the standard deviation of the median
            float: the percentile (the 68th, or 95th percentile) to be used for the errors on the parameters
            #fixme: in which case returns the lower and upper values.

        Returns the galaxy parameters and the stdev
        """

        self.method = method_chain
        self.chain_fraction = last_fraction
        self.percentile = percentile

        if self.chain is None:
            raise RuntimeError("No chain! Run .run_mcmc() first.")

        # Data correction for Vmax
        #vmax_sign = (self.chain['maximum_velocity'] < 0)
        #pa_correction = np.where(vmax_sign, self.chain['pa'] + 180., self.chain['pa'])
        #pa_correction = np.where(pa_correction > 180, pa_correction - 360, pa_correction)
        #self.chain['pa'] = pa_correction
        #self.chain['maximum_velocity'] = np.abs(self.chain['maximum_velocity'])

        cols = [ Column(data=np.cos(np.radians(self.chain['pa'])),  name='cospa'),
                 Column(data=np.cos(np.radians(self.chain['pa']*2)),name='cos2pa'),
                 Column(data=np.sin(np.radians(self.chain['pa'])),  name='sinpa'),
                 Column(data=np.sin(np.radians(self.chain['pa']*2)),name='sin2pa')
                 ]
        chain_full = self.chain.copy()
        chain_full.add_columns(list(cols))


        #extract subchain
        chain_size = np.size(chain_full)
        n = np.int(chain_size * last_fraction / 100.)  # number of samples (last_fraction(%) of total)

        idx = chain_full.argsort('reduced_chi')
        self.chain.idxsorted = idx

        if method_chain == 'chi_min' or method_chain == 'MAP':
            min_chi_index = self._get_min_chi_index()
            xmin = np.max([0, min_chi_index - n // 2])
            xmax = np.min([chain_size, min_chi_index + n // 2])
            sub_chain = chain_full[xmin: xmax]
        elif method_chain == 'last':
            sub_chain = chain_full[-n:]
            xmin = chain_size - n
            xmax = chain_size
        elif method_chain == 'chi_sorted':
            sub_chain = chain_full[idx][:n]
            sub_idx = idx[:n]
            xmin = 0
            xmax = n
        else:
            raise ValueError("Unsupported  `method_chain` '%s'"
                             % method_chain)
        #compute error model maps
        #@fixme
        # if self.error_maps:
        #    if method_chain == 'chi_min' or method_chain =='MAP':
        #        tmp_f = np.array(self.chain_flux_map)[min_chi_index - n // 2: min_chi_index + n // 2]
        #        tmp_v = np.array(self.chain_velocity_map)[min_chi_index - n // 2: min_chi_index + n // 2]
        #        tmp_s = np.array(self.chain_dispersion_map)[min_chi_index - n // 2: min_chi_index + n // 2]
        #    elif method_chain == 'last':
        #        tmp_f = np.array(self.chain_flux_map)[-n:]
        #        tmp_v = np.array(self.chain_velocity_map)[-n:]
        #        tmp_s = np.array(self.chain_dispersion_map)[-n:]
        #    elif method_chain == 'chi_sorted':
        #        tmp_f = np.array(self.chain_flux_map)[sub_idx]
        #        tmp_v = np.array(self.chain_velocity_map)[sub_idx]
        #        tmp_s = np.array(self.chain_dispersion_map)[sub_idx]
        #    self.true_flux_map_error = HyperCube(
        #        np.percentile(tmp_f, 50 + percentile/2., axis=0) -
        #        np.percentile(tmp_f, 50 - percentile/2., axis=0)
        #    )
        #    self.true_velocity_map_error = HyperCube(
        #        np.percentile(tmp_v, 50 + percentile/2., axis=0) -
        #        np.percentile(tmp_v, 50 - percentile/2., axis=0)
        #    )
        #    self.true_disp_map_error = HyperCube(
        #        np.percentile(tmp_s, 50 + percentile/2., axis=0) -
        #        np.percentile(tmp_s, 50 - percentile/2., axis=0)
        #    )

        # Compute best_parameters
        parameter_names = list(self.model.Parameters().names)

        if self.method == 'MAP':
            tmp_chain = np.array(chain_full[parameter_names].as_array().tolist())
            best_parameter = tmp_chain[idx[0]]
        else:
            tmp_chain = np.array(sub_chain[parameter_names].as_array().tolist()) #convert astropy Table into array
            best_parameter = np.median(tmp_chain, axis=0)
        # Compute errors to parameters
        sigma_parameter = np.std(tmp_chain, axis=0)

        #handle PA edges at +/-180
        #following https://ncss-wpengine.netdna-ssl.com/wp-content/themes/ncss/pdf/Procedures/NCSS/Circular_Data_Analysis.pdf
        cos1=np.median(sub_chain['cospa'])
        sin1=np.median(sub_chain['sinpa'])
        invtan = np.arctan2(sin1,cos1)
        pa_circular_best = np.degrees(invtan) # over -180;180
        #save
        pa_idx = sub_chain[parameter_names].index_column('pa')
        best_parameter[pa_idx] = np.where(pa_circular_best>0, pa_circular_best, pa_circular_best+360)

        r1 = np.sqrt(sub_chain['cospa'].sum()**2+sub_chain['sinpa'].sum()**2)
        r1 = r1/np.size(sub_chain)
        pa_circular_std = np.sqrt(-2.*np.log(r1))

        cos2=np.median(sub_chain['cos2pa'])
        sin2=np.median(sub_chain['sin2pa'])
        #r2 = np.sqrt(sub_chain['cos2pa']**2+sub_chain['sin2pa']**2)
        #r2 = np.median(r2)
        invtan2= np.arctan2(sin2,cos2)
        angle2= np.degrees(invtan2)

        ## this is??
        #pa_circular_dispersion = (1-angle2)/(2*r1**2)
        #print "pa disp  %.3f " % (pa_circular_dispersion)

        #center chain['pa']
        sub_chain_pa = sub_chain['pa'] - best_parameter[pa_idx]
        #sub_chain_pa = np.where(sub_chain_pa > 180, sub_chain_pa - 360, sub_chain_pa)
        #sub_chain_pa = np.where(sub_chain_pa < -180, sub_chain_pa + 360, sub_chain_pa)

        std_pa = np.std(sub_chain_pa)
        #This is identical to pa_circular_std
        #print "pa sigma %.3f" % (std_pa)
        #print "pa stdev %.3f " % (np.degrees(pa_circular_std))
        sigma_parameter[pa_idx] = std_pa

        #add back centering offset
        sub_chain['pa'] = sub_chain_pa + best_parameter[pa_idx]
        #keep full set
        chain_names = deepcopy(parameter_names)
        chain_names.append('reduced_chi')
        self.sub_chain = sub_chain[chain_names]
        self.chain = chain_full[chain_names]
        self.chain.xmin = xmin
        self.chain.xmax = xmax
        # self.sub_chain = sub_chain[parameter_names] #will be used for correlation plots

        #min in sub_chain:
        #self.best_chisq = np.min(self.sub_chain['reduced_chi'])
        #min absolute
        self.best_chisq = self.chain[idx[0]]['reduced_chi']

        #Save
        self.galaxy = GalaxyParameters.from_ndarray(best_parameter)
        self.galaxy.stdev = GalaxyParametersError.from_ndarray(sigma_parameter)
        self.stdev = self.galaxy.stdev

        # Compute percentiles
        if percentile is not None:
            self.logger.info('Setting %2d percentiles ' % (percentile))

            error_parameter_upper = np.percentile(self.sub_chain[parameter_names].as_array().tolist(), 50. + percentile/2., axis=0)
            error_parameter_lower = np.percentile(self.sub_chain[parameter_names].as_array().tolist(), 50. - percentile/2., axis=0)

            self.galaxy.upper = GalaxyParametersError.from_ndarray(error_parameter_upper)
            self.galaxy.lower = GalaxyParametersError.from_ndarray(error_parameter_lower)
            self.galaxy.ICpercentile = percentile



        # Store galaxy parameters and stdev
        self.logger.info("self.galaxy : fittest parameters : %s", repr(self.galaxy))
        self.logger.info("self.stdev : parameters stdev : %s", str(self.stdev))

        return None

    def compute_stats(self, snr_min=0.02):
        """
        snr_min : float [default = 0.02]
            minimum snr to compute BIC restricted over pixels with snr > snr_min
        compute stats (BIC, DIC, AIC)
        """

        dim_data = np.size(self.cube.data)

        self.chi_at_p = self.compute_chi(self.galaxy) / self.Ndegree

        self.convolved_cube = self.create_convolved_cube(self.galaxy, self.cube.shape)
        snr = (self.convolved_cube.data) / np.median(self.variance_cube.data)**0.5
        good = np.ones_like(snr)
        good[snr<snr_min] = 0
        dim_good = good.sum() #count only pixels with snr >snr_min and above

        Nd_good = (dim_good - self.dim_p_free - 1) # degree of freedom


        # like = -0.5*np.nansum(self.variance_chi)-0.5*self.compute_chi(params)
        #BIC = -2 * like(theta)
        self.BIC = self.chi_at_p * self.Ndegree + self.dim_p_free * np.log(dim_data)


        #AIC = -2 * like + 2 dim_p
        self.AIC = self.chi_at_p * self.Ndegree + 2* self.dim_p_free

        #DIC
        if self.method != 'chi_sorted':
            log_Lp = -0.5 * self.sub_chain['reduced_chi'] * self.Ndegree
            if np.isfinite(log_Lp).all():
                pD = 2 * np.var(log_Lp)
            else:
                pD = 2 * np.nanvar(log_Lp[np.isfinite(log_Lp)==True])
            # P = 2 * (logp_max-np.mean(self.lnp))
            #pD = 2 * -0.5 * (self.chi_at_p - np.mean(self.sub_chain['reduced_chi'])) * self.Ndegree

            #DIC = -2 * like + 2 pd
            self.DIC = self.chi_at_p * self.Ndegree + 2 * pD
        else:
            self.DIC = 0
            pD=0

        self.stats = Table(np.array(['%.8f' % (self.best_chisq), '%.8f' % (self.chi_at_p),
                                     int(self.BIC), self.Ndegree,
                                     int(self.AIC), self.dim_p_free,
                                     '%.2f' % (pD), int(self.DIC),
                                     np.max(snr)]
                                    ), \
                           names=['best_chi2', 'chi2_at_p', 'BIC', 'Ndegree', \
                                  'AIC', 'k', \
                                  'pD', 'DIC', 'SNRmax'])

        if self.mcmc_method == 'multinest':
            evidence = self.sampler['stats']['global evidence']
            self.stats.add_column(evidence*-2,name='log Z')

        return self.stats

    def create_clean_cube(self, galaxy, shape, final=False):
        """
        Creates a cube containing a clean simulation of a galaxy according to
        the provided model.

        galaxy: GalaxyParameters
            The parameters upon which the simulated galaxy will be built.
        shape: Tuple of 3
            The 3D (z, y, x) shape of the resulting cube.
            Eg: (21, 21, 21)

        Returns a HyperspectralCube
        """
        # Create radial velocities and radial dispersions
        #flux_cube, vz, vz_map, s_map, sig_map, sigz_disk_map, sig_intr = \
        #    self.model._compute_galaxy_model(galaxy, shape)

        ## normalize to real flux
        #flux_map = flux_cube.sum(0)
        #flux_map = galaxy.flux * flux_map / flux_map.sum()

        if self.model is None:
                raise AssertionError(" Model is undefined. Please define model first")

        modelcube, flux_map, vz_map, s_map = self.model._create_cube(galaxy, shape,\
                                self.instrument.z_step_kms, zo=galaxy['z'])

        #@fixme: currently records all calculations..
        # if self.error_maps:
        #    self.chain_flux_map.append(flux_map)
        #    self.chain_velocity_map.append(vz_map)
        #    self.chain_dispersion_map.append(s_map)

        # This is too expensive ! We create Cubes on each iteration...
        # There are ways to optimize this, as only the last one is used.
        if final is True:
            self.true_flux_map = HyperCube(flux_map)
            self.true_velocity_map = HyperCube(vz_map)
            self.true_disp_map = HyperCube(s_map)

        #modelcube = self.model._create_cube(shape, flux_map, vz_map, s_map,
        #                         self.instrument.z_step_kms, zo=galaxy.z)
        #is this used?
        modelcube.xy_step = self.cube.xy_step
        modelcube.z_step = self.cube.z_step
        modelcube.z_central = self.cube.z_central

        return modelcube

    def create_convolved_cube(self, galaxy, shape):
        """
        Creates a cube containing a convolved simulation of a galaxy according
        to the provided model.
        The convolution is done by the instrument you provided upon
        instantiation of this class.

        galaxy: GalaxyParameters
            The parameters upon which the simulated galaxy will be built.
        shape: Tuple of 3
            The 3D (Z, Y, X) shape of the resulting cube.
            Eg: (21, 21, 21)

        Returns a HyperspectralCube
        """

        clean_cube = self.create_clean_cube(galaxy, shape)
        return self.instrument.convolve(clean_cube)

    def import_chain(self, filepath, compute_best_params=False, method_chain='last'):
        """
        Imports the chain stored in a .dat file so that you may plot.
        compute_best_parameters False[default] | True
            if True will use 'last' method and 60%
            use best_parameters_from_chain method to customize
        """

        with open(filepath, 'r') as chain_data:
            self.chain = asciitable.read(chain_data.read(), Reader=asciitable.FixedWidth)

        self.model.sanitize_chain(self.chain)

        if compute_best_params is True:
            self.best_parameters_from_chain(method_chain=method_chain, last_fraction=60, percentile=95)

    NO_CHAIN_ERROR = "No chain to plot! Run .run_mcmc() or .import_chain() " \
                     "first."


    def save(self, name, overwrite=False):
        """
        Saves the results of the MCMC to files :

        - <name>_galaxy_parameters.txt
            A plain text representation of the parameters of the galaxy.
        - <name>_galaxy_parameters.dat
            A table representation of the parameters of the galaxy.
        - <name>_chain.dat
            A table representation of the Markov Chain.
            Each line holds one set of galaxy parameters and its associated reduced chi.
        - <name>_run_parameters.txt
            A plain text representation of the run_parameters.
        - <name>_instrument.txt
            A plain text representation of the instrument parameters.
        - <name>_convolved_cube.fits
            A FITS file containing the PSF-convolved result cube.
        - <name>_deconvolved_cube.fits
            A FITS file containing the pre-convolution clean cube.
        - <name>_residuals_cube.fits
            A FITS file containing the diff between input data and simulation.
        - <name>_3Dkernel.fits
            A FITS file containing the 3D kernel used

        - <name>_true_flux_map.fits
            A FITS file containing the true flux map [intrinsic]
        - <name>_true_vel_map.fits
            A FITS file containing the true velocity map [intrinsic]
        - <name>_true_sig_map.fits
            A FITS file containing the true dispersion map [intrinsic]

        - <name>_obs_flux_map.fits
            A FITS file containing the observed flux map [intrinsic]
        - <name>_obs_vel_map.fits
            A FITS file containing the observed velocity map [intrinsic]
        - <name>_obs_sig_map.fits
            A FITS file containing the observed dispersion map [intrinsic]

        - <name>_images.pdf/png
            A PNG image generated by the ``plot_images`` method.
            Note: the overwrite option is always true for this file.
        - <name>_mcmc.pdf/png
            A PNG image generated by the ``plot_mcmc`` method.
            Note: the overwrite option is always true for this file.

        - <name>_true_maps.pdf/png
            A PNG image generated by the ``plot_true_vfield`` method.
        - <name>_obs_maps.pdf/png
            The observed maps generated by the ``plot_obs_vfield`` method.

        - <name>_model.txt
            The model configuration
        - <name>_instrument.txt
            The instrument configuration

        - <name>_geweke.pdf/png
            The geweke diagnostics plot
        - <name>_galaxy_parameters_convergence.dat
            The convergence of each parameter based on the geweke diagnostics

        - <name>_corner.pdf/png
            The corner plot for the MCMC chain. Requires

        - <name>_stats.dat
            A ascii file containing the BIC/DIC etc criteria

        The .dat files can be easily read using astropy.table and its ``ascii_fixedwidth`` format : ::

            Table.read('example.chain.dat', format='ascii.fixed_width')

        .. warning::
            The generated files are not compressed and may take up a lot of disk
            space.

        name: string
            An absolute or relative name that will be used as prefix for the
            save files.
            Eg: 'my_run', or '/home/me/science/my_run'.
        overwrite: bool
            When set to true, will OVERWRITE existing files.
        """
        if self.chain is None:
            raise RuntimeError("Nothing to save! Run .run_mcmc() first.")

        filename = '%s_galaxy_parameters.txt' % name
        self._save_to_file(filename, self.galaxy.long_info(), overwrite)
        filename = '%s_galaxy_parameters.dat' % name
        self._save_to_file(filename, self.galaxy.structured_info(), overwrite)

        filename = '%s_chain.dat' % name
        self._save_to_file(filename, self._chain_as_asciitable(), overwrite)

        filename = '%s_stats.dat' % name
        self.stats.write(filename, format='ascii.fixed_width', overwrite=overwrite)

        filename = '%s_run_parameters.txt' % name
        self._save_to_file(filename, self.__str__(), overwrite)
        filename = '%s_instrument.txt' % name
        self._save_to_file(filename, self.instrument.__str__(), overwrite)
        filename = '%s_model.txt' % name
        self._save_to_file(filename, self.model.__str__(), overwrite)

        filename = '%s_convolved_cube.fits' % name
        self.convolved_cube.write_to(filename, overwrite)
        filename = '%s_deconvolved_cube.fits' % name
        self.deconvolved_cube.write_to(filename, overwrite)
        filename = '%s_residuals_cube.fits' % name
        self.residuals_cube.write_to(filename, overwrite)
        filename = '%s_3Dkernel.fits' % name
        self.psf3d.write_to(filename, overwrite)

        filename = '%s_obs_flux_map.fits' % name
        self.obs_flux_map.write_to(filename, overwrite)
        filename = '%s_obs_vel_map.fits' % name
        self.obs_velocity_map.write_to(filename, overwrite)
        filename = '%s_obs_disp_map.fits' % name
        self.obs_disp_map.write_to(filename, overwrite)

        filename = '%s_true_flux_map.fits' % name
        self.true_flux_map.write_to(filename, overwrite)
        filename = '%s_true_vel_map.fits' % name
        self.true_velocity_map.write_to(filename, overwrite)
        filename = '%s_true_disp_map.fits' % name
        self.true_disp_map.write_to(filename, overwrite)

        filename = '%s_rotcurve' % name
        self.model.plot_vprofile(self.galaxy,chain=self.sub_chain,filename=filename + '.png')
        self.model.plot_vprofile(self.galaxy,chain=self.sub_chain,filename=filename + '.pdf')

        #for quick display only
        filename = '%s_true_maps' % name
        self.plot_true_vfield(filename + '.png')
        self.plot_true_vfield(filename + '.pdf')

        filename = '%s_obs_maps' % name
        self.plot_obs_vfield(filename + '.png')
        self.plot_obs_vfield(filename + '.pdf')

        #@fixme
        # if self.error_maps:
        #    filename = '%s_true_flux_map_error.fits' % name
        #    self.true_flux_map_error.write_to(filename, overwrite)
        #    filename = '%s_true_vel_map_error.fits' % name
        #    self.true_velocity_map_error.write_to(filename, overwrite)
        #    filename = '%s_true_disp_map_error.fits' % name
        #    self.true_disp_map_error.write_to(filename, overwrite)

        filename = '%s_images' % name
        self.plot_images(filename + '.png')
        self.plot_images(filename + '.pdf')

        filename = '%s_mcmc' % name
        self.plot_mcmc(filename + '.png', method='last')
        self.plot_mcmc(filename + '.pdf', method='last')

        #Deprecicated
        # filename = '%s_correlations' % name
        #self.plot_correlations(filename + '.png')
        #self.plot_correlations(filename + '.pdf')

        try:
            filename = '%s_corner' % name
            self.corner=self.plot_corner(filename + '.png',nsigma=4)
            _ = self.plot_corner(filename + '.pdf',nsigma=4)
        except:
            self.corner=False
            self.logger.warning("plot corner failed ")

        filename = '%s_geweke' % name
        self.plot_geweke(filename + '.png')
        self.plot_geweke(filename + '.pdf')

        filename = '%s_galaxy_parameters_convergence.dat' % name
        self.convergence.write(filename, format='ascii.fixed_width', overwrite=overwrite)

        self.logger.info("Saved files in %s" % os.getcwd())

    #fixme: to do
    # def read_files(self, name):

    def __str__(self):
        """
        Return information about this run in a multiline string.
        """
        return """
galpak_version = %s

input_cube = %s
Var_cube = %s

%s

mcmc_method = %s
mcmc_sampling = %s
iterations = %s
random_scale = %s

parameters method = %s, chain_fraction: %s,
CI percentile: %s,

%s

min_boundaries = %s
max_boundaries = %s
known_parameters = %s
initial_parameters = %s

final_parameters = \n %s
best_chi2 = %s
median_chi2 = %s
BIC = %s

acceptance_rate = %s
    """ % (
            self.version,
            self.cube.filename,
            self.variance_cube.filename,
            self.instrument, self.mcmc_method, self.mcmc_sampling, self.max_iterations, self.random_scale,
            self.method,
            self.chain_fraction, self.percentile,
            self.model,
            self.min_boundaries, self.max_boundaries,
            self.known_parameters, self.initial_parameters,
            self.galaxy.structured_info(),
            self.best_chisq, self.chi_at_p,
            self.BIC,
            self.acceptance_rate
        )

    def _chain_as_asciitable(self):
        """
        Exports the chain as an `asciitable`.
        See the public API `import_chain()` for the reverse operation of loading
        the chain from an `asciitable` file.
        """
        out = StringStdOut()
        asciitable.write(self.chain,
                         output=out,
                         Writer=asciitable.FixedWidth,
                         names=self.chain.dtype.names)
        return out.content

    def _save_to_file(self, filename, contents, clobber):
        if not clobber and os.path.isfile(filename):
            raise IOError("The file {} already exists. Specify overwrite=True to overwrite it.".format(filename))
        with open(filename, 'w') as f:
            f.write(contents)

    def _read_file(self, filename):
        with open(filename, 'r') as f:
            contents=f.read()
        return contents

    def _get_min_chi_index(self):
        """
        Gets the index in the chain of the parameters with the minimal chi.
        """

        if self.chain is None:
            raise RuntimeError("No chain! Run `run_mcmc()` first.")

        idx = self.chain.idxsorted[0]

        return idx




    #############################################
    #
    # Private methods, modeling
    #
    #############################################

    def _set_verbose(self, verbose):
        """
        Update the logger's status
        """
        self.logger.disabled=False
        if verbose is True:
            #self.logger.setLevel('INFO')
            if self.model is not None:
                self.model.logger.disabled = False
            np.seterr(all='warn')
        elif verbose is False:
            #self.logger.setLevel('DEBUG')
            if self.model is not None:
                self.model.logger.disabled = True
            np.seterr(all='ignore')
        elif verbose is None:
            self.logger.disabled=True
            if self.model is not None:
                self.model.logger.disabled = True
        else:
            raise ValueError("verbose should be None | True | False")

    def _set_psf(self):
        """
        set PSF from config file
        """
        psf = None
        config = self.config['PSF']
        psf_keys={}
        for k in ['type', 'fwhm', 'alpha', 'beta', 'ba', 'pa']:
            if k in config.keys():
                psf_keys[k] = k
            elif 'psf_'+k in config.keys():
                psf_keys[k] = 'psf_'+k

        if 'type' in psf_keys:
            psf_type = config[psf_keys['type']].lower()
            self.logger.info("CONFIG: PSF: type {%s} found " % (psf_type))
        else:
            self.logger.error("CONFIG: PSF: type not specified")

        if psf_type == 'moffat':
            try:
                tmp_fwhm = float(config[psf_keys['fwhm']].split()[0])
            except:
                tmp_fwhm = None
            try:
                tmp_alpha = float(config[psf_keys['alpha']].split()[0])
            except:
                tmp_alpha = None

            if tmp_alpha is None:
                psf = MoffatPointSpreadFunction(
                    fwhm=float(config[psf_keys['fwhm']].split()[0]),  # psf_fwhm,
                    #alpha=float(self.config.get('PSF', psf_keys['alpha']).split()[0]),
                    beta=float(config[psf_keys['beta']].split()[0]),
                    pa  =float(config[psf_keys['pa']].split()[0]),
                    ba  =float(config[psf_keys['ba']].split()[0])
                )
            elif tmp_fwhm is None:
                psf = MoffatPointSpreadFunction(
                    #fwhm=self.config.get('PSF', psf_keys['fwhm']).split()[0]),  # psf_fwhm,
                    alpha=float(config[psf_keys['alpha']].split()[0]),
                    beta =float(config[psf_keys['beta']].split()[0]),
                    pa   =float(config[psf_keys['pa']].split()[0]),
                    ba   =float(config[psf_keys['ba']].split()[0])
                )
            else:
                raise self.logger.error("CONFIG: PSF: specify alpha or fwhm but not both")

        elif psf_type == 'gaussian':
            psf = GaussianPointSpreadFunction(
                    fwhm=float(config[psf_keys['fwhm']].split()[0]),  # psf_fwhm,
                    pa=float(config[psf_keys['pa']].split()[0]),
                    ba=float(config[psf_keys['ba']].split()[0])
            )
        elif psf_type == 'custom':
            if '.fits' in psf_keys['filename']:
                psf = ImagePointSpreadFunction(image_2d=config[psf_keys['filename']])
            else:
                raise self.logger.error("CONFIG: PSF: filename not supported (use .fits)")
        else:
            #@fixme add other options
            raise NotImplementedError("Currently only PSF type = `moffat` and `gaussian` supported")

        return psf

    def _set_lsf(self):
        """
        sets LSF from config LSF: lsf_fwhm
        :return:
        """
        lsf = None
        config = self.config['LSF']
        lsf_keys={}
        for k in ['type', 'fwhm']:
            if k in list(config.keys()):
                lsf_keys[k] = k
            elif 'lsf_'+k in config.keys():
                lsf_keys[k] = 'lsf_'+k

        if 'type' in lsf_keys:
            lsf_type = config[lsf_keys['type']].lower()
        else:
            lsf_type = None
            self.logger.warning("CONFIG: LSF: type not specified")

        if lsf_type == 'gaussian':
            lsf = GaussianLineSpreadFunction(
                fwhm=float(config[lsf_keys['fwhm']].split()[0])
            )  # lsf_fwhm,
        elif lsf_type is None:
            lsf = None
        else:
            #@fixme
            raise NotImplementedError

        return lsf

    def _read_instrument(self, file_config):

        if os.path.isfile(file_config):
            self.config.read(file_config)
        else:
            raise ValueError("Instrument Config file %s not present! " % (file_config))

        psf = self._set_psf()
        try:
            lsf = self._set_lsf()
        except:
            lsf = None
            self.logger.warning("CONFIG: LSF not found in config file")

        if 'INSTRUMENT' in self.config.sections():
            config = self.config['INSTRUMENT']
            myinstr = config['type'].lower()
            self.logger.info("CONFIG: INSTRUMENT: type {%s} found " % (myinstr))

            if 'pixscale' in list(config.keys()):
                scale = float(config['pixscale'].split()[0])  #
            else:
                scale = None

            if 'muse' == myinstr:
                instrument = MUSE(psf=psf, lsf=lsf)
            elif 'musewfm' == myinstr:
                instrument = MUSEWFM(psf=psf, lsf=lsf)
            elif 'musenfm' == myinstr:
                instrument = MUSENFM(psf=psf, lsf=lsf)
            elif 'alma' in myinstr:
                instrument = ALMA(psf=psf, lsf=lsf, pixscale=scale)
            elif 'sinfok250' in myinstr:
                instrument = SINFOK250(psf=psf, lsf=lsf)
            elif 'sinfok100' in myinstr:
                instrument = SINFOK100(psf=psf, lsf=lsf)
            elif 'sinfoj250' in myinstr:
                instrument = SINFOJ250(psf=psf, lsf=lsf)
            elif 'sinfoj100' in myinstr:
                instrument = SINFOJ100(psf=psf, lsf=lsf)
            elif 'harmoni' in myinstr:
                instrument = HARMONI(psf=psf, lsf=lsf, pixscale=scale)
            elif 'kmos' in myinstr:
                instrument = KMOS(psf=psf, lsf=lsf)
            elif 'osiris' in myinstr:
                instrument = OSIRIS(psf=psf, lsf=lsf)
            elif 'generic' in myinstr:
                instrument = Generic(psf=psf, lsf=lsf, default_spaxel_size=scale)
            else:
                # @fixme:generalize
                raise NotImplementedError
        else:
            #default
            self.logger.info("CONFIG: INSTRUMENT not present. Will use MUSE as default")
            instrument = MUSE(psf=psf, lsf=lsf)
        return instrument

    def _read_model(self, file_config):
        """
        sets model from config MODEL
        :return:
        """

        model = None
        if os.path.isfile(file_config):
            self.logger.info("Reading model {:s}".format(file_config))
            self.config.read(file_config)
        else:
            raise ValueError("Model Config file %s not present" % (file_config))

        if self.config.has_section('MODEL'):
            config = self.config['MODEL']
        else:
            self.logger.warning("CONFIG file has no MODEL section")

        if 'type' in list(config.keys()):
            model_type = config['type'].lower()
        else:
            self.logger.error("CONFIG: Model: type not specified")


        args={}
        #try:
        #    redshift = float(config['redshift'])
        #except:
        #    redshift = None

        #args['redshift']=redshift

        if  'default' in model_type:
            model = DefaultModel
        elif 'sersic' in model_type:
            model = ModelSersic
        else:
            raise ValueError("Model type invalid. Must be DefaultModel or ModelSersic")

        #args parameters
        import inspect
        var_args = inspect.getargspec(model).args
        for k in var_args[1:]:
            if k in list(config.keys()):
                try:
                    args[k]=eval(config[k])
                except:
                    args[k]=config[k]


        return model(**args)

    def _read_params(self, file_config, type):
        """
        sets random scale from config file
        :return: ModelParamers
        """
        if os.path.isfile(file_config):
            self.config.read(file_config)
        else:
            raise ValueError("Random Scale: Config file %s not present" % (file_config))

        if self.config.has_section(type):
            config = self.config[type]
        else:
            self.logger.warning("Config file has no %s section" % (type))

        par = self.model.parameters_class()()

        for r in list(config.keys()):
            if r in par.names:
                par[r] = eval(config[r])
            else:
                self.logger.warning("Config %s has keys not used for this model" % (type))
        return par

    def _init_sampling_scale(self, random_scale, should_guess_flags):
        dim_d = np.size(self.cube.data)
        dim_p = len(self.initial_parameters)

        # Tweak the random amplitude vector (Kp coeff, as pid)
        # that we can document Model.setup_random_amplitude() adequately
        random_amplitude = np.sqrt(
            (self.min_boundaries - self.max_boundaries) ** 2 / 12.
        ) * dim_p / dim_d

        # Let the model adjust the random amplitude of the parameter jump
        self.model.setup_random_amplitude(random_amplitude)

        # Scale MCMC if needed // allowing vectors
        if random_scale is not None:
            if np.size(random_scale) != 1:
                merge_where_nan(random_scale, np.ones_like(random_amplitude))
            random_amplitude = random_amplitude * random_scale

        # Zero random amplitude where parameters are known
        random_amplitude = random_amplitude * should_guess_flags

        return random_amplitude
