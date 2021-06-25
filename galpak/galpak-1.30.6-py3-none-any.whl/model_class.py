# -*- coding: utf-8 -*-

import numpy as np
from scipy.interpolate import interp1d
from scipy import ndimage
from copy import deepcopy

try:
    import bottleneck as bn
except ImportError:
    import numpy as bn


from .hyperspectral_cube import HyperspectralCube as HyperCube
from .galaxy_parameters import  GalaxyParameters

# CONSTANTS
G = 6.67384e-11  # Gravitational Constant (m^3.kg^-1.s^-2)
SOL_MASS = 1.98e30  # Solar Mass (kg)
PARSEC = 3e16    # Parsec (m)

# LOGGING CONFIGURATION
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('GalPaK: DiskModel ')

#Python3 compatibility
try:
  basestring
except NameError:
  basestring = str

class Model:
    """
    An **interface** for your simulation models.
    The `runner` parameter is the instance of `galpak.Runner` using this model.
    """

    logger = logger
    flux_map_user = None

    def set_cosmology(self, cosmo_string='planck15'):
        try:
            from colossus.cosmology import cosmology
            from colossus import halo
            from colossus.halo import mass_defs, mass_adv, mass_so, concentration
            self.logger.info("setting cosmology with colossus package")
            if cosmo_string is cosmology.cosmologies.keys():
                cosmo=cosmology.setCosmology(cosmo_string)
            else:
                self.logger.info("colossus: cosmology %s is not available\n "
                                 "Please use one of %s \n"
                                 "Will be uing cosmology Planck15 as default" \
                                 % (cosmo_string, cosmology.cosmologies.keys()) )
                cosmo=cosmology.setCosmology('planck15')
            #put h in
            self.h = cosmo.h
            self.Ez = cosmo.Ez(self.redshift)
            DA = cosmo.angularDiameterDistance(self.redshift) / self.h  ####!!
            self.DeltaVir = halo.mass_so.deltaVir(self.redshift)
            self.halo = halo #Diemer Halo module for NFW halo models
        except ImportError:
            try:
                from astLib import astCalc
                #using  astLib for cosmology
                self.logger.info("Using AstLib for a 737 cosmology, h,OM, OL= (0.7, 0.3, 0.7)")
                self.h = astCalc.H0 / 100.
                self.Ez = astCalc.Ez(self.redshift)
                DA = astCalc.da(self.redshift)#for h=0.7
                self.DeltaVir = astCalc.DeltaVz(self.redshift)
                self.halo = None
                #self.logger.warning('Best to use colossus package from Diemer& Kratsov for this module')
            except ImportError:
                #using astropy
                from astropy import cosmology
                if cosmo_string in cosmology.parameters.available:
                    cosmo = cosmology.default_cosmology.get_cosmology_from_string(cosmo_string)
                else:
                    self.logger.info("Astropy: Parameter %s is not available\n "
                                     "Please use one of %s \n"
                                     "Will be uing astropy.cosmology Planck15 as default" \
                                     % (cosmo_string, cosmology.parameters.available))
                    cosmo = cosmology.default_cosmology.get_cosmology_from_string('Planck15')
                self.h = cosmo.h
                DA = cosmo.angular_diameter_distance(self.redshift).value #in Mpc
                self.Ez = cosmo.H(self.redshift).value/cosmo.H0
                x = cosmo.Om(self.redshift) - 1.0 #Omega_M(z) - 1.0
                self.DeltaVir = 18 * np.pi**2 + 82 *x - 39 * x**2
                self.halo = None
                #self.logger.warning('Best to use colossus package from Diemer& Kratsov for this module')

        self.kpc = DA * 1e3 * np.radians(1./3600)# in unit kpc
        #self.hkpc = self.kpc * h

    def Parameters(self):
        """
        Returns `GalaxyParameters' instance
        :return:
        """
        return GalaxyParameters()

    def parameters_class(self):
        """
        Returns the class of parameters extending `ModelParameters` that this
        model uses. Note that this returns the class itself, not an instance.
        """
        return GalaxyParameters

    def initial_parameters(self, runner):
        """
        Returns an instance of a class extending `ModelParameters`.
        You may omit parameters, they will be automatically set to the mean of
        the max and min.
        """
        raise NotImplementedError()

    def min_boundaries(self, runner):
        """
        Returns an instance of a class extending `ModelParameters`.
        You MUST provide all the parameters.
        """
        raise NotImplementedError()

    def max_boundaries(self, runner):
        """
        Returns an instance of a class extending `ModelParameters`.
        You MUST provide all the parameters.
        """
        raise NotImplementedError()

    def sanitize_parameters(self, parameters):
        """
        Mutates the parameters with custom logic.
        This is called right after parameter jumping in the loop.
        """
        #    # Handle reflection in parameters
        #    if parameters.pa > 90.:
        #        parameters.pa -= 180.
        #        parameters.maximum_velocity *= -1
        #    if parameters.pa < -90.:
        #        parameters.pa += 180.
        #        parameters.maximum_velocity *= -1

        inc = parameters['inclination']
        if inc<0:
            parameters.pa +=180

        parameters.pa = parameters.pa % 360. #to deal with circularity


    def sanitize_chain(self, chain):
        """
        Mutates the `chain` with custom logic.
        This is called at the end of the loop, before storing the chain.
        """
        pa = chain['pa']
        pa_corr = pa % 360
        chain['pa'] = pa_corr

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
        raise NotImplementedError()

    #CUSTOM METHODS
    def set_flux_profile(self, galaxy, radius_cube):
        """
        creates a flux_cube in 3D (x,y,z)
        returns flux_cube
        """
        raise NotImplementedError()

    def set_velocity_profile(self, galaxy, radius_cube):
        """
        creates a velocity profile for circular orbits
        return v_profile
        """
        raise NotImplementedError()

    # DEFAULT METHODS

    def set_thickness_profile(self, nz, hz, flux_cube):
        """
        add the thickness profile to the flux cube
        returns flux_cube
        """
        if self.thickness_profile == 'gaussian':
            tmp_cube = np.exp(-nz**2. / 2. / hz**2.)
        elif self.thickness_profile == 'exponential':
            tmp_cube = np.exp(-np.abs(nz) / hz)  # exponential z-profile
        elif self.thickness_profile == 'sech2':
            tmp_cube = np.cosh(-nz / hz)**(-2.)  # sech^2 z-profile
        elif self.thickness_profile == 'none':
            self.logger.warning("Using no disk thickness profile: "
                                 "this galaxy will become a cylinder!")
            tmp_cube = np.ones_like(flux_cube)
        else:
            raise NotImplementedError("Context profile not supported. Should be '%s'" %
                                      self.THICKNESS_VALID)
        #normalize gaussians
        #norm = tmp_cube.sum(0)

        return flux_cube * tmp_cube


    def set_dispersion_profile(self, hz, vtot, radius_cube):
        """
        set disk dispersion profile
        """
        ### ISOTROPIC but this IS the 1-d dispersion in z-direction
        # A) using R/h=0.5 (V/sigma)^2 for very thin disk
        if self.dispersion_profile == 'thin':
            # dimension of r [3D-spatial]
            sig_ale_disk = np.sqrt(hz * vtot ** 2. / radius_cube)
        # B) using R/h=V/Sigma for compact disk
        elif self.dispersion_profile == 'thick':
            # dimension of r [3D-spatial]
            sig_ale_disk = hz * vtot / radius_cube
        # C) Using Binney Merrifield
        # elif self.dispersion_profile == 'infinitely_thin':
            # dimension of r [3D-spatial]
            # sig_ale_disk = np.sqrt(math.tau * Surf_density * G * hz_kpc)
        else:
            raise ValueError("Disk dispersion is not valid. Should be '%s' " %
                             self.DISPERSION_VALID)

        return sig_ale_disk


    ###########################################
    #HEART of model
    ###########################################
    def _create_maps(self, galaxy, shape):
        """
        Creates and returns:
        - a cube sized like (`shape`) containing a clean simulation
          of a galaxy for the `parameters`.
        - the velocity map, which is an image.
        - the dispersion (sigma) map, which is an image.

        This is called on each loop, to compute the likelihood of each generated
        set of parameters. Therefore, it needs to be fast.

        parameters: DiskParameters
            The parameters upon which the simulated disk galaxy will be built.
        shape: Tuple of 3
            The 3D shape of the resulting cube.
            Eg: (21,21,21)

        Returns a tuple.
        """
        # Create radial velocities and radial dispersions

        flux_cube, vz, vz_map, s_map, sig_map, sigz_disk_map, sig_intr = \
            self._compute_galaxy_model(galaxy, shape)

        # normalize to real flux
        flux_map = flux_cube.sum(0)
        flux_map = galaxy.flux * flux_map / flux_map.sum()

        return flux_map, vz_map, s_map

    def _create_cube(self, galaxy, shape, z_step_kms, zo=None):
        """
        Creates and returns:
        - the flux map, of shape (shape[1], shape[0]) of a galaxy
        - the velocity map, which is an image.
        - the dispersion (sigma) map, which is an image.

        This is called on each loop, to compute the likelihood of each generated
        set of parameters. Therefore, it needs to be fast.

        parameters: DiskParameters
            The parameters upon which the simulated disk galaxy will be built.
        shape: Tuple of 3
            The 3D shape of the resulting cube.
            Eg: (21,21,21)

        Returns a tuple.
        """
        # Create radial velocities and radial dispersions

        flux_cube, vz, v_map, s_map, sig_map, sigz_disk_map, sig_intr = \
            self._compute_galaxy_model(galaxy, shape)

        # normalize to real flux
        flux_map = flux_cube.sum(0)
        flux_map = galaxy.flux * flux_map / flux_map.sum()

    #def _create_cube(self, shape, f_map, v_map, s_map, z_step_kms, zo=None):
    #    """
    #    Creates a 3D cube from Flux, Velocity and Dispersion maps.

    #    shape: tuple
    #        Defines the created cube's shape
    #    f_map: ndarray
    #        2D image of the flux
    #    v_map: ndarray
    #        2D image of the velocity
    #    s_map: ndarray
    #        2D image of the dispersion
    #    z_step_kms: float
    #        in km/s
    #    zo: int
    #        The centroid (in pixel) in the z-direction
    #        If not set, will be the middle of the z-axis
    #    """

        vmax = z_step_kms * (shape[0] - 1) / 2.

        if zo is None:
            vzero = vmax
        else:
            vzero = z_step_kms * zo  # fixme: shouldn't this be with zo-0.5 ?

        # Array of velocities : array of indices from to 0 to Vmax
        velocities = np.linspace(0, 2 * vmax, shape[0]) - vzero

        # Create a copy of Vmap in each z plane
        tmpcube = np.outer(np.ones_like(velocities), v_map)
        vcube = tmpcube.reshape(shape)

        # Create a copy of Smap in each z plane
        tmpcube = np.outer(np.ones_like(velocities), s_map)
        scube = tmpcube.reshape(shape)

        # Create a copy of velocities in each location
        if z_step_kms > 0:
            vbegin = np.min(velocities)
            vfinal = np.max(velocities)
        else:
            vbegin = np.max(velocities)
            vfinal = np.min(velocities)
        # Create grid of velocities
        vgrid, y, x = np.mgrid[
            vbegin: vfinal + 0.9 * z_step_kms: z_step_kms,
            0: np.shape(v_map)[0],
            0: np.shape(v_map)[1]
        ]

        # Apply Gaussian
        finalcube = np.exp(-0.5 * (vgrid - vcube) ** 2 / (scube ** 2))

        # For doublets, add the blue component
        # deltaV is defined as (l2-l1)/l2 * c ie from the reddest line
        if self.line is not None:
            # Delta between emission peaks (in km/s ?)
            # line['wave']=[l, lref] eg. [3726.2, 3728.9] # Observed or Rest;
            # line['ratio']=[0.8, 1.0] eg. [0.8, 1.0] ; the primary line for redshifts is the reddest
            delta = 3e5 * (self.line['wave'][1]-self.line['wave'][0])/(self.line['wave'][0]+self.line['wave'][1])*2
            ratio = self.line['ratio'][0] / self.line['ratio'][1]
            #ratio = galaxy.line_ratio

            # Add the blue doublet
            finalcube = finalcube + ratio * np.exp(-0.5 * (vgrid - (vcube - delta)) ** 2 / (scube ** 2))

        # delta = 217.  # km/s OII
        # delta = -945  # km/s Ha 6564.614 NII 6585.27
        # delta = 2872  # km/s OIII 4960.295 5008.240
        # delta = 641   # km/s SII 6718.29  6732.67

        # Normalize from amplitude ratios int f dv = int f dz
        ampsum = bn.nansum(finalcube,0)
        #amplitude = f_map / bn.nansum(finalcube, 0)
        #amplitude[np.isnan(amplitude)] = 0
        amplitude =  flux_map / ampsum
        amplitude[np.isfinite(amplitude)==False] = 0
        #amplitude =  np.where(np.isfinite(amplitude),f_map / ampsum, 0)

        # Create a cube of Amplitude in each z plane
        amplitude_cube = np.resize(amplitude, shape)

        finalcube = finalcube * amplitude_cube
        finalcube[np.isfinite(finalcube)==False] = 0

        cube = HyperCube(data=finalcube)

        return cube, flux_map, v_map, s_map

    def _compute_galaxy_model(self, parameters, shape):
        """
        Create the disk galaxy model related cubes and maps.

        parameters: DiskParameters
            The parameters of the disk galaxy.

        Returns
            3D flux cube,
            3D Vz cube,
            2D Vmap (1st moment of Vz),
            2D S_map,
            2D (2nd moment of Vz),
            2D disk_dispersion,
            2D intrinsic
        """
        if 'radius' in parameters.names:
            hz = parameters.radius * self.q ##0.15
        elif 'disk_radius' in parameters.names:
            hz = parameters.disk_radius * self.q ##0.15
        else:
            raise Exception("Parameter must have a radius")
        # trick to go faster, as we know the max z shape the resulting model will fit in
        #       z_shape = np.ceil(shape[1] / 2.5 * 0.15 * 6.) ## 6 sigmas
        #       z_shape = np.ceil(self.max_boundaries.radius / 2.5 * 0.15 * 6.) ## 6 sigmas
        #       or
        #       z_shape = np.ceil(self.max_boundaries.radius * 2 * 3 * 0.15) # 3 hz_max on each side
        # this short cut introduced a bug in the flux_deconvolved maps! fixed after 1.6.0
        z_shape = int(np.ceil ( (shape[1] + shape[2]) / 2.)) #mean of spatial dimensions
        self.logger.debug(" using z_shape %d in compute_galaxy_model" % (z_shape) )
        self.logger.debug(" cube is %d in z- " % (shape[0]) )
        # Minimum shape for z direction -- collapsed, so big sizes unimportant
        # z_shape = 6 hz(sigma)_max;
        # hz_max = size_box/2.5 (proxy for radius max) * 0.15

        # Create arrays of indices in image frame; this cube has spatial dimentions in x,y,z; so should be almost a perfect cube in shape.
        ind_shape = tuple([z_shape, shape[1], shape[2]])
        z, y, x = np.indices(ind_shape, dtype='float64')

        #Spatial Cubes and Vz from spatial dimensions ind_shape
        nx, ny, nz, vz_cube, vtot = self._map_indices(x, y, z, parameters)

        radius_cube = np.hypot(nx,ny) #np.sqrt(nx**2. + ny**2.)

        flux_cube = self.set_flux_profile(parameters, radius_cube)

        # Adjust disk thickness
        flux_cube = self.set_thickness_profile(nz, hz, flux_cube)

        # Normalize by flux
        total = bn.nansum(flux_cube) #should always be >0
        if total>0:
            flux_cube =  flux_cube / total
        else:
            raise ValueError("Something is wrong. Total flux is zero")

        # Flux weighted
        flux_map = bn.nansum(flux_cube, 0)
        bad = (flux_map**2 == 0)

        vz_map = bn.nansum(vz_cube * flux_cube / flux_map, 0)
        vz_map[bad] = np.nan  #force outer to 0

        v2_map = bn.nansum(vz_cube ** 2 * flux_cube / flux_map, 0)
        Var_map = v2_map - vz_map ** 2
        sig_map_disk = np.where(Var_map>0, np.sqrt(Var_map), 0)



        ### Add Sigma_Aleatoire_disk
        sig_ale_disk = self.set_dispersion_profile(hz, vtot, radius_cube)
        # Compute weighted mean for Sig_disk
        # a) 2D map = flux-weighted map
        #Sigz_disk_map = bn.nansum(Sig_disk*A,0)/Flux_map
        # b) 2D map = flux-weighted map rms
        #sigz_map_ale = np.sqrt(bn.nansum(sig_ale_disk**2*A,0)/Flux_map)
        # c) Normalized with flux squared
        norm =  bn.nansum(flux_cube * flux_cube, 0)
        sigz_map_ale = np.sqrt(bn.nansum(sig_ale_disk ** 2 * flux_cube ** 2, 0) / norm)


        # Intrinsic Dispersionmodel
        if 'velocity_dispersion' in parameters.names:
            sig_intr = np.ones_like(sigz_map_ale) * parameters.velocity_dispersion
        else:
            sig_intr = np.ones_like(sigz_map_ale)

        #correct outer regions
        #sigz_map_ale = np.where(bad, sig_intr, sigz_map_ale)

        # Total S-map
        s_map = np.sqrt(sig_map_disk ** 2 + sigz_map_ale ** 2 + sig_intr ** 2)
        s_map[bad]=np.nan

        return flux_cube, vz_cube, vz_map, s_map, \
            sig_map_disk, sigz_map_ale, sig_intr

    def _map_indices(self, xx, yy, zz, parameters):
        """
        Takes arrays of indices, galaxy parameters, and rotates accordingly.
        Returns xx, yy, zz indices of object in image frame
        Returns z-component of velocity of object in image frame
        """

        inclination = np.radians(parameters.inclination)
        pa = np.radians(parameters.pa - 90)

        zo = (np.size(zz, 0) - 1 ) / 2.  # center along z

        # Rotate inclination (around x)
        rot_i = self._make_rotation_matrix_around_x(inclination)
        rot_mi = self._make_rotation_matrix_around_x(-inclination)

        # Rotate PA (around z) anti-clockwise
        rot_pa = self._make_rotation_matrix_around_z(pa)
        rot_mpa = self._make_rotation_matrix_around_z(-pa)

        # Transformation from sky coords to disk plane
        xx = xx - parameters.x
        yy = yy - parameters.y
        zz = zz - zo

        # Rotation around z for PA
        nx = rot_pa[0, 0] * xx + rot_pa[0, 1] * yy
        ny = rot_pa[1, 0] * xx + rot_pa[1, 1] * yy
        nz = rot_pa[2, 2] * zz

        # Rotation around x for inclination
        x = rot_i[0, 0] * nx
        y = rot_i[1, 1] * ny + rot_i[1, 2] * nz
        z = rot_i[2, 1] * ny + rot_i[2, 2] * nz

        # Compute the radius cube
        radius_cube = np.sqrt(x ** 2. + y ** 2.)

        # Circular orbits -- we're DIVIDING BY ZERO ; it's okay, need for speed
        vx = np.where(np.isfinite(y / radius_cube),  +y / radius_cube, 0)
        vy = np.where(np.isfinite(x / radius_cube),  -x / radius_cube, 0)

        if 'virial_velocity' in parameters.names:
            radius_3d = np.sqrt(x**2. + y**2. + z**2.)
            v_profile = self.set_velocity_profile(parameters, radius_cube, radius_3d)
        else:
            v_profile = self.set_velocity_profile(parameters, radius_cube)
        # Remove NaNs where radius is 0
        v_profile[radius_cube == 0] = 0.

        # 3D velocity vectors
        vx = vx * v_profile
        vy = vy * v_profile

        # Rotation of [vx, vy, 0] -inclination around x
        vvx = rot_mi[0, 0] * vx
        vvy = rot_mi[1, 1] * vy
        vvz = rot_mi[2, 1] * vy

        # Rotation of -pa around z
        vx = rot_mpa[0, 0] * vvx + rot_mpa[0, 1] * vvy
        vy = rot_mpa[1, 0] * vvx + rot_mpa[1, 1] * vvy
        vz = rot_mpa[2, 2] * vvz

        v = np.sqrt(vx ** 2 + vy ** 2 + vz ** 2)

        return x, y, z, vz, v

    def __str__(self):
        dic=self.__mdict__()
        model = """[MODEL] :
  type = {i}""".format(i=self.__name__())
        for k in dic.keys():
            model += """
  {k} = {v} """.format(k=k,v=dic[k])

        return model

    def __name__(self):
        return self.__class__.__name__

    def __mdict__(self):
        dic = vars(self).copy() #@fixme should deepcopy
        dic['model'] = self.__name__()
        k = dic.pop('flux_map_user') if 'flux_map_user' in dic.keys() else None

        return dic

    ################### PRIVATE methods
    ####################################

    @staticmethod
    def _make_rotation_matrix_around_x(a):
        return np.array([[1,         0,          0],
                         [0, np.cos(a), -np.sin(a)],
                         [0, np.sin(a),  np.cos(a)]])

    @staticmethod
    def _make_rotation_matrix_around_z(a):
        return np.array([[np.cos(a),  np.sin(a), 0],
                         [-np.sin(a), np.cos(a), 0],
                         [0,          0,         1]])


    @staticmethod
    def _int_x_dev(x):
        """
        (-4 (5040 + 5040 x^(1/4) + 2520 sqrt(x) + 840 x^(3/4) + 210 x + 42 x^(5/4) + 7 x^(3/2) + x^(7/4)))/exp(x^(1/4))
        """
        return (-4. * (5040. + 5040. * x ** 0.25 + 2520. * np.sqrt(x) + 840. * x ** 0.75 + 210. * x + 42. * x ** 1.25 + 7. * x ** 1.5 + x ** 1.75)) * np.exp(-x ** 0.25)

    ##################################
    def _user_profile(self, parameters, radius_1d, resample_by=10):
        """
            returns 1D profile profile from user map
        :param parameters:
        :param radius_cube:
        :return:
        """
        shape = self.flux_map_user.shape #shape of image2d

        # Create arrays of indices in image frame; this cube has spatial dimentions in x,y,z; so should be almost a perfect cube in shape.
        ind_shape = tuple([21, shape[0]*resample_by, shape[1]*resample_by])#oversampling x10
        z, y, x = np.indices(ind_shape)

        galaxy = deepcopy(parameters)
        galaxy.x = galaxy.x * resample_by
        galaxy.y = galaxy.y * resample_by
        # Spatial Cubes and Vz from spatial dimensions ind_shape
        nx, ny, nz, vz_cube, vtot = self._map_indices(x, y, z, galaxy)

        radius_2d  = np.hypot(nx, ny)  # np.sqrt(nx**2. + ny**2.)
        rad = radius_2d[10,:,:]

        ##PA is from x axis clock-wise  // or y anti-clockwise
        #y,x = np.indices(self.flux_map_user.shape)
        #ang=np.radians(parameters['pa'])
        #ba = np.cos(np.radians(parameters['inclination'])) #approx
        #dx=parameters['x']-x
        #dy=parameters['y']-y
        #dx_p=dx*np.cos(ang)-dy*np.sin(ang)
        #dy_p=dx*np.sin(ang)+dy*np.cos(ang)
        ##rotation matrix
        #rad = np.sqrt( dx_p**2+dy_p**2/ba**2  )

        #flux_cube = self.set_flux_profile(parameters, radius )

        # xp=np.arange(rmax)
        xp = np.r_[0:radius_1d.max()+1.:1./resample_by]*resample_by  # starts at 1,2,3,4 pixels
        indata = self.flux_map_user.copy() #2d map
        indata = ndimage.zoom(indata, (resample_by, resample_by))

        mysum = np.array([indata[rad <= p].sum() for p in xp])

        # Compute SB profile
        # area=pi*(np.arange(rmax))**2*ba_raw
        dx = xp[1]-xp[0]
        on = np.ones(indata.shape) * dx

        area = [on[rad <= p].sum() for p in xp]
        diff_area = np.where(np.diff(area) == 0, dx, np.diff(area))

        SBprofile = np.diff(mysum) / diff_area #/ (pixscale * pixscale)
        SBprofile = np.hstack([SBprofile[0],SBprofile]) #to avoid infty at zero

        f = interp1d(xp,SBprofile, kind='cubic')
        SBprofile_interp = f(radius_1d*resample_by)

        return SBprofile_interp

    def compute_Mdyn_at_Rhalf(self, parameters, radius=None):
        """
        From parameters and pixscale computes Mdyn(<Rhalf)

        """
        if radius is None:
            radius = parameters['radius']

        if self.pixscale is None:
            raise ValueError("Pixel scale undefined")
        else:
            pixscale = self.pixscale

        # Compute angular distance in Mpc
        # Convert it to kpc/arcsec
        rhalf_kpc = radius * pixscale * self.kpc  # in kpc

        #define velocity function
        v_rhalf = self.set_velocity_profile(parameters, radius)

        # v² = (GM/r) in km/s
        dynamic_mass = self._mass_from_GMr(v_rhalf, rhalf_kpc)#computed at R1/2.

        return dynamic_mass

    def compute_MvirRvir(self, Vvir):
        """
        computes Mvir, Rvir from Vvir
            uses either colossus R_to_M or GM/R
        :param Vvir:
        :return:
        """

        ##Rvir in kpc/h
        #Rvir = Vvir /  np.sqrt(self.DeltaVir/2.) / (100 * self.Ez/1e3) #in kpc

        #Rvir in kpc
        Rvir = Vvir /  np.sqrt(self.DeltaVir/2.) / (100 * self.h * self.Ez) * 1e3 #in kpc

        Mvir = self._mass_from_GMr(Vvir, Rvir)

        return Mvir, Rvir

    def _colossus_Mvir_compare(self, Vvir):

        Rvir = Vvir /  np.sqrt(self.DeltaVir/2.) / (100 * self.h * self.Ez) * 1e3 #in kpc

        ###############shape independent /cosmology dependent
        mdef='vir'
        Mvir = self.halo.mass_so.R_to_M(R=Rvir*self.h,z=self.redshift,mdef='vir')#kpc

        return Mvir, self._mass_from_GMr(Vvir, Rvir * self.h)

    @staticmethod
    def _mass_from_GMr(velocity, radius):
        """
        compute mass from GM/r=v2
        :param velocity: in km/s
        :param radius: in kpc
        :return:
        """
        return (1e3 * velocity) ** 2 * (PARSEC * radius * 1e3) / G / SOL_MASS

    def _fv_newton(self, r, radius, vmax):
        """
        Returns the velocity for the mass profile given the r-cube.
        The cumulative flux I(<r) profile is analytically calculated
        Only for n=1,0.5,4.
        """

        mass = 1  # enclosed_mass for Gaussian

        if self.flux_profile == 'exponential':
            rr = 1.68 * r / radius
            mtot = mass * (1. - rr * np.exp(-rr) - np.exp(-rr))
        elif self.flux_profile == 'gaussian':
            mtot = mass * (1. - np.exp(-r ** 2 / 2. / (2 * radius / 2.35) ** 2))
        elif self.flux_profile == 'de_vaucouleurs':
            mtot = mass * (self._int_x_dev(r / radius) - self._int_x_dev(0))
        else:
            raise ValueError("Flux profile is not valid. Only for sersic_n=[0.5, 1, 4].")

        v = np.sqrt(mtot / (r + 1e-9))  # in km/s

        # Normalization set by Vmax (sets the mass)
        if np.size(v) > 1:
            v = v / bn.nanmax(v) * vmax
        else:
            v = v / np.max(v) * vmax

        return v

