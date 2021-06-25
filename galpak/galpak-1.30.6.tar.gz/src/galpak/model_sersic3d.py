# -*- coding: utf-8 -*-

import numpy as np
from scipy import special
from astropy.io import fits
from copy import deepcopy
try:
    import bottleneck as bn
except ImportError:
    import numpy as bn

from .galaxy_parameters import  GalaxyParameters
from .model_utilities import modelPlots, ModelExt
from .model_class import Model
from .math_utils import flux_sersic

# LOGGING CONFIGURATION
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('GalPaK: DiskModel ')

class ModelSersic(Model,modelPlots, ModelExt):
    """
    The first and default galpak `Model` (when unspecified).
    It simulates a simple disk galaxy using `DiskParameters`.

    flux_profile: 'exponential' | 'gaussian' | 'de_vaucouleurs' | 'sersicN2' | 'user'
            The flux profile of the observed galaxy. The default is 'exponential'.
            See http://en.wikipedia.org/wiki/Sersic%27s_law
            If 'user' provided flux map, specify flux_image. Currently unsupported

    thickness_profile:  'gaussian' [default] | 'exponential' | 'sech2' | 'none'
        The perpendicular flux profile of the disk galaxy.
        The default is 'gaussian'.
        If none. the galaxy will become a cylinder.

    rotation_curve: 'arctan'  |  'exponential' | 'tanh' [default] |
                 'isothermal' | 'NFW' | 'Burkert' |
                 'mass' | 'Freeman' | 'Spano'
        The profile of the velocity v(r) can be in (with X=r/rV where rV=turnover radius):
            - arctan : Vmax arctan(X),
            - tanh : Vmax tanh(X),
            - exponential : inverted exponential, Vmax (1-exp(-X))
            - isothermal : for an isothermal halo, Vmax [1-arctan(X)/X)]^0.5
            - NFW :  for a NFW halo, Vmax {[ln(1+X) - X/(1+X)]/X}^0.5
            - Burkert : for a Burkert halo, Vmax {[ln(1 + X) + 0.5 ln (1 + X^2) - arctan(X)]/X}^0.5
            - Freeman : a Freeman disk with Vmax=V2.2
            - mass : a constant light-to-mass ratio v(r)=sqrt(G m(<r) / r); where m(<r) is the cumulative mass profile with m(<r) = \int I(r) 2 pi r dr
            - Spano: for a Spano 2008 profile, Vmax {arcsinh(X)/X - 1/sqrt(1+X2)}
                    See https://doi.org/10.1093/mnras/stz1969

        The default is 'tanh'.

    dispersion_profile: 'thick' [default] | 'thin'
        The local disk dispersion from the rotation curve and disk thickness
        from Binney & Tremaine 2008, see Genzel et al. 2008.
        GalPak has 3 components for the dispersion:
            - a component from the rotation curve arising from mixing velocities
              of a disk with non-zero thickness.
            - a component from the local disk dispersion specified by
              `disk_dispersion`
            - a spatially constant dispersion,
              which is the output parameter `velocity_dispersion`.

    line: None[default] | dict to fit doublets, use a dictionary with
            - line['wave']=[l, lref] eg. [3726.2, 3728.9] # Observed or Rest
            - line['ratio']=[0.8, 1.0] eg. [0.8, 1.0] # The primary line for redshifts is the reddest

    redshift: float
            The redshift of the observed galaxy, used in mass calculus.
            Will override the redshift provided at init ; this is a convenience parameter.
            If this is not set anywhere, GalPak will not try to compute the mass.

    """

    # fixme: use integers instead of strings here and enjoy the performance gain

    FLUX_VALID = ['gaussian', 'exponential', 'de_vaucouleurs', 'sersicN2', 'user']

    THICKNESS_VALID = [ 'gaussian', 'exponential', 'sech2', 'none']

    DISPERSION_VALID = [ 'thick', 'thin']

    CURVE_VALID = ['arctan', 'exponential', 'tanh', \
                   'isothermal', 'NFW', 'Burkert', 'Freeman', 'mass', 'Spano' ]

    logger = logger

    def __init__(self,
                 flux_profile='exponential',
                 thickness_profile='gaussian',
                 dispersion_profile='thick',
                 rotation_curve= 'tanh',
                 flux_image=None,
                 line=None,
                 aspect=None,
                 redshift=None,
                 pixscale=None,
                 cosmology='planck15'):
        if flux_profile in self.FLUX_VALID:
            self.flux_profile = flux_profile
        else:
            raise ValueError("Flux parameter should be one of self.FLUX_VALID",self.FLUX_VALID)

        if rotation_curve in self.CURVE_VALID:
            self.rotation_curve = rotation_curve
        else:
            raise ValueError("Rotation curve should be one of self.CURVE_VALID", self.CURVE_VALID)

        if thickness_profile in self.THICKNESS_VALID:
            self.thickness_profile = thickness_profile
        else:
            raise ValueError("Thickness profile should be one of self.THICKNESS_VALID", self.THICKNESS_VALID)

        if dispersion_profile in self.DISPERSION_VALID:
            self.dispersion_profile = dispersion_profile
        else:
            raise ValueError('Dispersion profile should be one of self.DISPERSION_VALID', self.DISPERSION_VALID)


        self.line = line
        self.aspect = aspect
        self.redshift = redshift
        self.pixscale = pixscale
        self.cosmology= cosmology
        self.logger = logging.getLogger('GalPaK: DiskModel')

        if self.rotation_curve == 'Freeman' and self.flux_profile != 'exponential':
            self.logger.warning("You have selected a Freeman disk and a flux profile that is not exponential. Use this at your own risks.")

        if self.rotation_curve == 'mass':
            self.logger.warning("You have selected the mass disk profile; which only works for gaussian/exponential/sersicN2 flux profile")

        #fluxmap user
        if self.flux_profile == 'user':
            if isinstance(flux_image, str):
                try:
                    self.flux_map_user = fits.open(flux_image)['DATA'].data
                except KeyError:
                    self.flux_map_user = fits.open(flux_image)[0].data
                else:
                    raise ValueError('Flux user image should have data in DATA or extention 0')
            elif isinstance(flux_image, np.ndarray):
                self.flux_map_user = flux_image
            else:
                self.logger.error("Flux image should be an array or a string")

        if self.redshift != None :
            if self.cosmology is not None:
                self.set_cosmology(self.cosmology)
            else:
                self.set_cosmology() #using default

        if self.aspect is not None:
            self.q = self.aspect
        else:
            self.q = 0.15 #default aspect ratio

        #self.logger.info("Set up model: %s" % (self.__str__()))


    def initial_parameters(self, runner):
        """
        Returns an instance of a class extending `ModelParameters`.
        You may omit parameters, they will be automatically set to the mean of
        the max and min.
        """
        # Default initial parameters
        init = self.parameters_class()(
            radius=3.0,
            turnover_radius=1.0,
            inclination=30,
            pa=np.random.uniform(0,360),
            maximum_velocity=100.0,
            velocity_dispersion=5.0,
            flux=runner.flux_est
        )

        return init

    def min_boundaries(self, runner):
        """
        Returns an instance of a class extending `ModelParameters`.
        You MUST provide all the parameters.
        """
                # Default boundaries
        return GalaxyParameters(
            x=runner.cube.shape[2] / 3.,
            y=runner.cube.shape[1] / 3.,
            z=runner.cube.shape[0] / 3.,
            flux=0.,
            radius=0.8,
            inclination=-5,
            pa=-40,
            turnover_radius=0.01,
            maximum_velocity=10.,
            velocity_dispersion=0.
        )


    def max_boundaries(self, runner):
        """
        Returns an instance of a class extending `ModelParameters`.
        You MUST provide all the parameters.
        """
        # changed max radius to 3/8th of cube size.
        return GalaxyParameters(
            x=runner.cube.shape[2] * 2 / 3.,
            y=runner.cube.shape[1] * 2 / 3.,
            z=runner.cube.shape[0] * 2 / 3.,
            flux=3. * runner.flux_est,
            radius= 0.5 * (runner.cube.shape[1]+runner.cube.shape[2]) * 3 / 8.,
            inclination=90.5,
            pa=400,
            turnover_radius=0.5 * (runner.cube.shape[1]+runner.cube.shape[2]) * 3 / 8. / 2.,
            maximum_velocity=350.,
            velocity_dispersion=180.
        )


    def setup_random_amplitude(self, amplitude):
        """
        Mutates the random `amplitude` of the parameter jump with custom logic.
        This is called during the setup of the MCMC runner.
        The amplitude is already filled with :
            sqrt((min_boundaries - max_boundaries) ** 2 / 12.) * p / v
        where
            p = number of parameters in the model
            v = number of voxels in the cube
        """
        amplitude['flux'] *= 0.5  # flux since we start at ~flux since flux is an integrated quantity
        amplitude['pa'] *= 1.5
        amplitude['maximum_velocity'] *= 1.5 #
        amplitude['velocity_dispersion'] *= 1.5  # velocity dispersion
        amplitude *= 3       # fixme: document this coefficient

    #CUSTOM METHODS
    def set_flux_profile(self, galaxy, radius_cube):
        """
        creates a flux_cube in 3D (x,y,z)
        returns flux_cube
        """

        rhalf = galaxy['radius']

        if self.flux_profile == 'de_vaucouleurs':
            flux_cube = flux_sersic(radius_cube, rhalf, 4.0)
        elif self.flux_profile == 'gaussian':
            flux_cube = flux_sersic(radius_cube, rhalf, 0.5)
        elif self.flux_profile == 'exponential':
            flux_cube = flux_sersic(radius_cube, rhalf, 1.0)
        elif self.flux_profile == 'sersicN2':
            flux_cube = flux_sersic(radius_cube, rhalf, 2.0)
        elif self.flux_profile == 'user':
            if len(radius_cube.shape)==1:
                #then measure 1D profile from parameters
                flux_cube = self._user_profile(parameters, radius_cube)
            elif len(radius_cube.shape)==3:
                flux_cube = self.flux_map_user[None, :, :]  # @fixme need thickness?
            else:
                raise ValueError("set profile with a 1d vector or 3d cube")
        else:
            raise ValueError("Flux profile is invalid. Should be one of '%s' ." % self.FLUX_VALID)

        return flux_cube


    def set_velocity_profile(self, galaxy, radius_cube):
        """
        creates a velocity profile for circular orbits
        return v_profile
        """
        max_vel = galaxy['maximum_velocity']
        rt = galaxy['turnover_radius']

        x = radius_cube / rt

        # Flat rotation curve
        if self.rotation_curve == 'arctan':
            v_profile = np.arctan(x) * max_vel * 2. / np.pi
        #
        elif self.rotation_curve == 'tanh':
            v_profile = max_vel * np.tanh(x)
        # For Feng's inv_exp profile
        elif self.rotation_curve == 'exponential':
            v_profile = max_vel * (1.0 - np.exp(-x))
        # ISOTHERMAL rotation curve;
        elif self.rotation_curve == 'isothermal' :
            v_profile = max_vel * np.sqrt(1 - np.arctan(x)/x)
        elif self.rotation_curve == 'NFW':
            v_sq =  ( np.log(1+x) - x / (1+x) ) / x #peaks at x=2.16
            v_sq /= ( np.log(1+2.16) - 2.16 / (1+2.16)) / 2.16
            v_profile = max_vel * np.sqrt(v_sq)
        elif self.rotation_curve == 'Burkert':
            v_sq =  (np.log(1+x)+0.5*np.log(1+x**2)-np.arctan(x)) / x # peaks at x=3.24
            v_sq /= (np.log(4.24)+0.5*np.log(1+3.24**2)-np.arctan(3.24)) / 3.24
            v_profile = max_vel * np.sqrt(v_sq)
        elif self.rotation_curve == 'mass':
            v_profile = self._fv_newton(radius_cube, galaxy['radius'], max_vel)
        elif self.rotation_curve == 'Freeman':
            #Using Freeman disk. Vmax = V2.2
            v_sq = self._v_disk_sq(galaxy, radius_cube)
            v_profile = np.sqrt(v_sq)
        elif self.rotation_curve == 'Spano':
            # From Spano et al. 2008: https://doi.org/10.1111/j.1365-2966.2007.12545.x
            # and Hernandez-Hernandez et al. 2019 https://doi.org/10.1093/mnras/stz1969
            v_sq = 1/x * np.vectorize(np.math.asinh)(x) - 1. / (1+x**2)
            v_profile = max_vel * np.sqrt(v_sq)
        else:
            raise NotImplementedError("Rotational Curve not supported. Should be '%s' " %
                                      self.CURVE_VALID)

        return v_profile

    #Private methods

    def _v_disk_sq(self, parameters, radius):
        ##disk Freeman model
        y = 1.68 * radius / parameters['radius'] / 2.
        B = special.i0(y) * special.k0(y) \
            - special.i1(y) * special.k1(y) #
        # Swinbank
        #  V(r)^2 = 0.5 (GMd/Rd) * (3.6*x)^2 * (I0K0-I1K1)
        #
        # Eq. 2.165. BinneyTremaine 2008
        # Vsq = 2 * (G Md/Rd) y**2 [I0K0-I1K1]
        # Vsq = 4 * (G Md/Rd)  0.5 * y**2 [I0K0-I1K1]

        B1 = 0.1934  #y^2 B(y) peaks at y=1.1;
        v_disk_sq =  parameters['maximum_velocity']**2. * (y)**2. * B / B1
        # 2 Vdisk_sq * B1 = Vmax_sq

        return v_disk_sq
