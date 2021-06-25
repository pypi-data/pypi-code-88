# -*- coding: utf-8 -*-

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('GalPaK: Instrument: ')

from .spread_functions import *
from . import convolution

class Instrument(object):
    """
    This is a generic instrument class to use or extend.

    psf: None|PointSpreadFunction
        The 2D Point Spread Function instance to use in the convolution, or None (the default).
        When this parameter is None, the instrument's PSF will not be applied to the cube.
    lsf: None|LineSpreadFunction
        The 1D Line Spread Function instance to use in the convolution, or None (the default).
        Will be used in the convolution to spread the PSF 2D image through a third axis, z.
        When this parameter is None, the instrument's PSF will not be applied to the cube.
    """

    # SPREAD FUNCTIONS
    psf = None  # Object implementing PointSpreadFunction, or None.
    lsf = None  # Object implementing LineSpreadFunction, or None.
    # MEMORIZATION HOLDERS
    psf3d = None      # 3D ndarray, product of 2D PSF and 1D LSF
    psf3d_fft = None  # Fast Fourier Transform of above

    cube_default_z_step = None   #
    cube_default_z_central = None   #
    cube_default_xy_step = None     #
    cube_default_cunit = 'Undef'  #

    cube_xy_step = cube_default_xy_step
    xy_step = cube_default_xy_step
    z_step = cube_default_z_step
    z_central = cube_default_z_central
    z_cunit = cube_default_cunit
    z_step_kms = None

    logger = logger

    def __init__(self, psf=None, lsf=None):

        if (self.xy_step is None) and (self.cube_default_xy_step is not None):
            self.xy_step = self.cube_default_xy_step

        if (self.z_step is not None) and (self.z_central is not None):
                self.z_step_kms = 3e5 * self.z_step / self.z_central
        else:
                self.z_step_kms = None

        if psf:
            if not isinstance(psf, PointSpreadFunction):
                raise ValueError("PSF should be an instance of galpak.PointSpreadFunction")
            self.psf = psf

        if lsf:
            if not isinstance(lsf, LineSpreadFunction):
                raise ValueError("LSF should be an instance of galpak.LineSpreadFunction")
            self.lsf = lsf
            self.lsf.z_cunit = self.z_cunit

    def use_pixelsize_from_cube(self, cube):
        """
        This should use_pixelsize_from_cube the Instrument and its PSF with the values from the Cube.
        Sometimes an instrument's precision depends upon which region of the sky and spectrum it's looking at.
        This callback is here to solve that problem.

        The passed cube has additional attributes provided by GalPak :
            - xy_step (in ")
            - z_step (in cunit3)
            - z_central (in cunit3)
        """

        #xy_step = cube.get_steps()[1]
        #z_step = cube.header.get('CDELT3')
        #z_cunit = cube.header.get('CUNIT3')
        #crpix = cube.header.get('CRPIX3')
        #crval = cube.header.get('CRVAL3')

        if cube.z_step is None or cube.z_central is None or cube.xy_step is None:
            self.logger.warning("The Cube probably lacks spectral headers.")

        if self.cube_default_xy_step is None:
            # if no default, use cube
            if cube.xy_step is not None:
                self.logger.warning('Forcing instrument pixelscale to that of cube')
                self.cube_xy_step = cube.xy_step
                self.xy_step = cube.xy_step  # pixel size in arcsec
            #if no default and no cube header Error
            else:
                raise ValueError("No default pixscale and No header information")

        elif self.cube_default_xy_step is not None:
            # use default from instrument if cube does not
            if cube.xy_step is not None:
                self.cube_xy_step = cube.xy_step
                if np.abs(self.cube_default_xy_step - self.cube_xy_step) / self.cube_xy_step > 0.1:
                    raise ValueError("INSTRUMENT pixscale differs from that of data!!")
                else:
                    self.xy_step = self.cube_xy_step

        if cube.z_step is not None:
            self.z_step = cube.z_step
        if cube.z_step is not None and cube.z_central is not None:
            self.z_step_kms = 3e5 * cube.z_step / cube.z_central  # km/s
            #logger.info("z_step_kms = %.3e km/s", self.z_step_kms)
        if cube.z_central is not None:
            self.z_central = cube.z_central
        if cube.z_cunit is not None:
            self.z_cunit = cube.z_cunit
            self.lsf.z_cunit = cube.z_cunit  #fixme: need to convert default lsf_fwhm to proper units

    def convolve(self, cube):
        """
        Convolve the provided data cube using the 3D Spread Function
        made from the 2D PSF and 1D LSF.
        Should transform the input cube and return it.
        If the PSF or LSF is None, it will do nothing.

        .. warning::
            The 3D spread function and its fast fourier transform are
            memoized for optimization, so if you change the instrument's
            parameters after a first run, the SF might not reflect your changes.
            Delete ``psf3d`` and ``psf3d_fft`` to clear the memory.

        cube: HyperspectralCube
        """
        # Skip if missing PSF or LSF
        if self.psf is None or self.lsf is None:
            return cube

        # PSF's FFT is memoized for optimization
        if self.psf3d_fft is None:
            # Apply LSF to PSF
            self.psf3d = self.extrude_psf(self.psf.as_image(cube), self.lsf.as_vector(cube))
            cube_convolved, self.psf3d_fft = convolution.convolve_3d_same(cube.data, self.psf3d, compute_fourier=True)
        else:
            cube_convolved, __ = convolution.convolve_3d_same(cube.data, self.psf3d_fft, compute_fourier=False)

        cube.data = cube_convolved

        return cube

    @staticmethod
    def extrude_psf(psf2d, lsf1d):
        """
        Apply the 1D LSF to provided 2D PSF image, and return the resulting 3D PSF cube.
        LSF should extrude the image along the z-axis (wavelength).
        """
        return psf2d * lsf1d[:, None, None]

    def __str__(self):
        return """[INSTRUMENT] :
  type = {i.__class__.__name__}
  pixscale = {i.xy_step} "

{i.psf}
{i.lsf}
cube_xy_step   = {i.cube_xy_step} "
cube_z_step    = {i.z_step} {i.z_cunit}

cube z_step_kms = {i.z_step_kms} km/s  at {i.z_central} {i.z_cunit}

""".format(i=self)


class Generic(Instrument):
    """
    Generic instrument with no defaults.
    """

    def __init__(self, psf=None, lsf=None,
                 lsf_fwhm=None,
                 psf_fwhm=None, psf_pa=None, psf_ba=None,
                 default_spaxel_size=None, default_zstep=None, default_zcentral=None, default_cunit=None):
        """
        Generic instrument with no defaults.

          lsf_fwhm None
            the lsf FWHM in units of the cube CUNIT3
          psf_fwhm None
            the psf FWHM in arcsec
          psf_pa None
            the psf PA of the major-axis, anti-clockwise
          psf_ba None
            the psf axis ratio
         default_spaxel_size
            the Generic Instrument spaxel size [kpc, "]
         default_zstep_size
            the Generic Instrument cdelt3 step in [default_cunit]
         default_cunit
            the Generic Instrument cdelt3 unit
         default_zcentral
            the Generic Instrument central wavelength/frequency in [default_cunits]
        """

        _errmsg = "Generic instrument's `%s` is required."

        if default_spaxel_size is not None:
            self.cube_default_xy_step = default_spaxel_size

        if (default_zcentral is not None and default_cunit is not None and default_zstep is not None):
            if default_zstep is not None:
                self.cube_default_z_step = default_zstep

            if default_zcentral is not None:
                self.cube_default_z_central = default_zcentral

            if default_cunit is not None:
                self.cube_default_cunit = default_cunit
        elif not(default_zcentral is None and default_cunit is None and default_zstep is None):
            self.logger.error("Please specify together the default_zcentral, default_cunit, default_ztep values")


        if lsf is None:
            if lsf_fwhm is None:
                raise TypeError(_errmsg % 'lsf_fwhm')
            lsf = GaussianLineSpreadFunction(fwhm=lsf_fwhm)
        if psf is None:
            if psf_fwhm is None:
                raise TypeError(_errmsg % 'psf_fwhm')
            if psf_pa is None:
                raise TypeError(_errmsg % 'psf_pa')
            if psf_ba is None:
                raise TypeError(_errmsg % 'psf_ba')
            psf = GaussianPointSpreadFunction(fwhm=psf_fwhm,
                                              pa=psf_pa, ba=psf_ba)

        Instrument.__init__(self, psf=psf, lsf=lsf)

    def use_pixelsize_from_cube(self, cube):
        """
        method to use pixelsize from cube, called by galpak.__init__
        """

        Instrument.use_pixelsize_from_cube(self, cube)


class ALMA(Instrument):
    """
    ALMA instrument mode
    psf_fwhm: float
        The PSF Full Width Half Maximum in arcsec, aka. "seeing".
    psf_pa: float
        The PSF Position Angle (from y-axis) of the major axis: anti-clockwise rotation from Y axis, in angular degrees.
    psf_ba: float
        The PSF axis ratio (<1)

    spax_scale: float
        The spatial scale (arcsec)
    zstep_scale: float
        The frequency pixel size (Hz)

    """
    cube_default_z_step = None   # Hz
    cube_default_z_central = None   # Hz
    cube_default_xy_step = None     # "
    cube_default_cunit = 'Hz'

    def __init__(self, psf=None, lsf=None, lsf_fwhm=None, psf_fwhm=1.2, psf_pa=0., psf_ba=1.0, pixscale=cube_default_xy_step, zstep_scale=cube_default_z_step):
        #if (spaxel_scale is None):
        #        self.logging.WARNING('WARNING: ALMA instrument has no default spatial scale (arcsec), will try to use the cube header. It can be specified with spaxel_scale(arcsec)')
        #if (zstep_scale is None):
        #        self.logging.WARNING('WARNING: ALMA instrument has no default freq. scale (Hz), will try to use the cube header. It can be specified with zstep_scale')

        if pixscale is None:
            self.logger.warning("ALMA: no spaxel defined; will use cube header")

        self.xy_step = self.cube_default_xy_step = pixscale  # "
        self.z_step = zstep_scale
        self.lsf_fwhm = lsf_fwhm

        if lsf is None:
            lsf = GaussianLineSpreadFunction(fwhm=lsf_fwhm)
        if psf is None:
            psf = GaussianPointSpreadFunction(fwhm=psf_fwhm, pa=psf_pa, ba=psf_ba)

        Instrument.__init__(self, psf=psf, lsf=lsf)

    def use_pixelsize_from_cube(self, cube):
        Instrument.use_pixelsize_from_cube(self, cube)

        if (cube.z_step is not None) and (self.lsf.fwhm is None):
            self.lsf.fwhm = cube.z_step
            self.logger.warning('Setting LSF FWHM to 1 z_pixel')

class HARMONI(Instrument):
    """
    pixelscale : float
         4, 10, 20, 30 mas

    """
    VALID_pixscale = [4, 10, 20, 30]

    cube_default_xy_step = None
    cube_default_z_step = None   # µm
    cube_default_z_central = None   # µm
    cube_default_cunit = 'micron'

    def __init__(self, psf=None, lsf=None, pixscale=cube_default_xy_step, psf_fwhm=None, psf_pa=0., psf_ba=1.0, lsf_fwhm=None):
        if pixscale is not None:
            self.logger.warning(" Will assume pixel scale in arcsecs")
            self.xy_step = self.cube_default_xy_step =  pixscale   # @fixme deal with units
        else:
            self.cube_default_xy_step = None
            self.logger.warning("HARMONI: no spaxel defined; will use cube header")

        if lsf is None:
            if lsf_fwhm is None:
                raise TypeError('Harmoni lsf_fwhm is required when no LSF')
            lsf = GaussianLineSpreadFunction(fwhm=lsf_fwhm)
        if psf is None:
            if psf_fwhm is None:
                raise TypeError('Harmoni psf_fwhm is required when no PSF')
            psf = GaussianPointSpreadFunction(fwhm=psf_fwhm, pa=psf_pa, ba=psf_ba)
        Instrument.__init__(self, psf=psf, lsf=lsf)

    def use_pixelsize_from_cube(self, cube):
        Instrument.use_pixelsize_from_cube(self, cube)



class MUSE(Instrument):
    """
    MUSE Wide Field Mode (default mode).
    Also used as a parent class for both field modes.

    psf_pa: float
        The PSF Position Angle (from y-axis) of the major axis: anti-clockwise rotation from Y axis, in angular degrees.
    psf_ba: float
        The PSF axis ratio (<1)

    psf_fwhm: float
        The PSF's Full Width Half Maximum in arcsec, aka. "seeing".
        Default to 0.8.

    lsf_mode 'gaussian' for a LSF 1D gaussian // 'mpdaf' qsim version of LSF
    """
    cube_default_xy_step = 0.2      # Spatial step in "
    cube_default_z_step = 1.25   # Spectral step in µm
    cube_default_z_central = 6564  # µm
    cube_default_cunit = 'Angstrom'

    def __init__(self, psf=None, lsf=None, lsf_fwhm=None, psf_fwhm=1.0, psf_pa=0., psf_ba=1.0):

        if lsf is None:
            lsf = GaussianLineSpreadFunction(fwhm=lsf_fwhm)
        if psf is None:
            psf = GaussianPointSpreadFunction(fwhm=psf_fwhm, pa=psf_pa, ba=psf_ba)

        Instrument.__init__(self, psf=psf, lsf=lsf)

    def lsf_fwhm_for_MUSE(self, wave=None):
        """
        computes fwhm of lsf from wavelength using
         fwhm = 5.835 10−8λ2 − 9.080 10−4λ+ 5.983 [Bacon+17]
        :param wave: wavelength in Angstrom
        :return:
        """
        fwhm = None
        if wave is None:
            try:
                wave = self.z_central
                fwhm = 5.835e-8*wave**2-9.08e-4*wave+5.983
                self.logger.info("lsf_fwhm set up for lambda in MUSE. See Bacon+17")
            except:
                self.logger.warning("Wavelength undefined for MUSE LSF\n Specify wave or z_central ")
        else:
            fwhm = 5.835e-8*wave**2-9.08e-4*wave+5.983

        return fwhm

    def use_pixelsize_from_cube(self, cube):
        """
        MUSE's LSF's FWHM depends on the z step
        """

        Instrument.use_pixelsize_from_cube(self, cube)
        try:
            if self.lsf.fwhm is None:
                self.logger.info("Adjusting LSF FWHM for MUSE cube.z_central")
                self.lsf.fwhm = self.lsf_fwhm_for_MUSE()
        except:
            pass

class MUSEWFM(MUSE):
    """
    MUSE Wide Field Mode (default mode).
    See MUSE for its default values.
    """


class MUSENFM(MUSE):
    """
    MUSE Narrow Field Mode.
    Has default values of MUSE, except for the spatial step.
    """
    cube_default_xy_step = 0.025  # Spatial step in "


class KMOS(Instrument):
    cube_default_z_step = 0.0002   # µm
    cube_default_z_central = None   # µm
    cube_default_xy_step = 0.2    # "
    cube_default_cunit = 'micron'

    def __init__(self, psf=None, lsf=None, lsf_fwhm=0.00065, psf_fwhm=0.6, psf_pa=90., psf_ba=0.8):

        if lsf is None:
            lsf = GaussianLineSpreadFunction(fwhm=lsf_fwhm)
        if psf is None:
            psf = GaussianPointSpreadFunction(fwhm=psf_fwhm, pa=psf_pa, ba=psf_ba)

        Instrument.__init__(self, psf=psf, lsf=lsf)

    def use_pixelsize_from_cube(self, cube):
        Instrument.use_pixelsize_from_cube(self, cube)


class SINFOK250(Instrument):
    """
    psf_fwhm: float
        The PSF Full Width Half Maximum in arcsec, aka. "seeing".
    psf_pa: float
        The PSF Position Angle (from y-axis) of the major axis: anti-clockwise rotation from Y axis, in angular degrees.
    psf_ba: float
        The PSF axis ratio (<1)

    cube_default_z_step = 2.45e-4   # µm
    cube_default_z_central = 2.20   # µm
    cube_default_xy_step = 0.125    # "
    cube_default_cunit = 'micron'
    """
    cube_default_z_step = 2.45e-4   # µm
    cube_default_z_central = 2.20   # µm
    cube_default_xy_step = 0.125    # "
    cube_default_cunit = 'micron'

    def __init__(self, psf=None, lsf=None, lsf_fwhm=0.00065, psf_fwhm=1.2, psf_pa=90., psf_ba=0.8):

        if lsf is None:
            lsf = GaussianLineSpreadFunction(fwhm=lsf_fwhm)
        if psf is None:
            psf = GaussianPointSpreadFunction(fwhm=psf_fwhm, pa=psf_pa, ba=psf_ba)

        Instrument.__init__(self, psf=psf, lsf=lsf)

    def use_pixelsize_from_cube(self, cube):
        Instrument.use_pixelsize_from_cube(self, cube)


class SINFOK100(Instrument):
    """
    psf_fwhm: float
        The PSF Full Width Half Maximum in arcsec, aka. "seeing".
    psf_pa: float
        The PSF Position Angle (from y-axis) of the major axis: anti-clockwise rotation from Y axis, in angular degrees.
    psf_ba: float
        The PSF axis ratio (<1)

    cube_default_z_step = 2.45e-4   # µm
    cube_default_z_central = 2.20   # µm
    cube_default_xy_step = 0.05     # "
    cube_default_cunit = 'micron'
    """

    cube_default_z_step = 2.45e-4   # µm
    cube_default_z_central = 2.20   # µm
    cube_default_xy_step = 0.05     # "
    cube_default_cunit = 'micron'

    def __init__(self, psf=None, lsf=None, lsf_fwhm=0.00065, psf_fwhm=1.2, psf_pa=90., psf_ba=0.8):

        if lsf is None:
            lsf = GaussianLineSpreadFunction(fwhm=lsf_fwhm)
        if psf is None:
            psf = GaussianPointSpreadFunction(fwhm=psf_fwhm, pa=psf_pa, ba=psf_ba)

        Instrument.__init__(self, psf=psf, lsf=lsf)

    def use_pixelsize_from_cube(self, cube):
        Instrument.use_pixelsize_from_cube(self, cube)


class SINFOH250(Instrument):
    """
    psf_fwhm: float
        The PSF Full Width Half Maximum in arcsec, aka. "seeing".
    psf_pa: float
        The PSF Position Angle (from y-axis) of the major axis: anti-clockwise rotation from Y axis, in angular degrees.
    psf_ba: float
        The PSF axis ratio (<1)

    cube_default_z_step = 1.95e-4   # µm
    cube_default_z_central = 1.50   # µm
    cube_default_xy_step = 0.125    # "
    cube_default_cunit = 'micron'
    """

    cube_default_z_step = 1.95e-4   # µm
    cube_default_z_central = 1.50   # µm
    cube_default_xy_step = 0.125    # "
    cube_default_cunit = 'micron'

    def __init__(self, psf=None, lsf=None, lsf_fwhm=0.00078, psf_fwhm=1.2, psf_pa=90., psf_ba=0.8):

        if lsf is None:
            lsf = GaussianLineSpreadFunction(fwhm=lsf_fwhm)
        if psf is None:
            psf = GaussianPointSpreadFunction(fwhm=psf_fwhm, pa=psf_pa, ba=psf_ba)

        Instrument.__init__(self, psf=psf, lsf=lsf)

    def use_pixelsize_from_cube(self, cube):
        Instrument.use_pixelsize_from_cube(self, cube)


class SINFOJ250(Instrument):
    """
    psf_fwhm: float
        The PSF Full Width Half Maximum in arcsec, aka. "seeing".
    psf_pa: float
        The PSF Position Angle (from y-axis) of the major axis: anti-clockwise rotation from Y axis, in angular degrees.
    psf_ba: float
        The PSF axis ratio (<1)

    cube_default_z_step = 1.45e-4   # µm
    cube_default_z_central = 1.20   # µm
    cube_default_xy_step = 0.125    # "
    cube_default_cunit = 'micron'
    """

    cube_default_z_step = 1.45e-4   # µm
    cube_default_z_central = 1.20   # µm
    cube_default_xy_step = 0.125    # "
    cube_default_cunit = 'micron'

    def __init__(self, psf=None, lsf=None, lsf_fwhm=0.00065, psf_fwhm=1.2, psf_pa=90., psf_ba=0.8):

        if lsf is None:
            lsf = GaussianLineSpreadFunction(fwhm=lsf_fwhm)
        if psf is None:
            psf = GaussianPointSpreadFunction(fwhm=psf_fwhm, pa=psf_pa, ba=psf_ba)

        Instrument.__init__(self, psf=psf, lsf=lsf)

    def use_pixelsize_from_cube(self, cube):
        Instrument.use_pixelsize_from_cube(self, cube)


class SINFOJ100(Instrument):
    """
    psf_fwhm: float
        The PSF Full Width Half Maximum in arcsec, aka. "seeing".
    psf_pa: float
        The PSF Position Angle (from y-axis) of the major axis: anti-clockwise rotation from Y axis, in angular degrees.
    psf_ba: float
        The PSF axis ratio (<1)

    cube_default_z_step = 1.45e-4   # µm
    cube_default_z_central = 1.20   # µm
    cube_default_xy_step = 0.05     # "
    cube_default_cunit = 'micron'
    """

    cube_default_z_step = 1.45e-4   # µm
    cube_default_z_central = 1.20   # µm
    cube_default_xy_step = 0.05     # "
    cube_default_cunit = 'micron'

    def __init__(self, psf=None, lsf=None, lsf_fwhm=0.00065, psf_fwhm=1.2, psf_pa=90., psf_ba=0.8):

        if lsf is None:
            lsf = GaussianLineSpreadFunction(fwhm=lsf_fwhm)
        if psf is None:
            psf = GaussianPointSpreadFunction(fwhm=psf_fwhm, pa=psf_pa, ba=psf_ba)

        Instrument.__init__(self, psf=psf, lsf=lsf)

    def use_pixelsize_from_cube(self, cube):
        Instrument.use_pixelsize_from_cube(self, cube)


class OSIRIS(Instrument):
    cube_default_z_step = 0.25e-4   # µm
    cube_default_z_central = 1.99   # µm
    cube_default_xy_step = 0.035     # "
    cube_default_cunit = 'micron'

    def __init__(self, psf=None, lsf=None, lsf_fwhm=0.00065, psf_fwhm=0.091, psf_pa=0., psf_ba=1.0):

        if lsf is None:
            lsf = GaussianLineSpreadFunction(fwhm=lsf_fwhm)
        if psf is None:
            psf = GaussianPointSpreadFunction(fwhm=psf_fwhm, pa=psf_pa, ba=psf_ba)

        Instrument.__init__(self, psf=psf, lsf=lsf)

    def use_pixelsize_from_cube(self, cube):
        self.lsf.fwhm = 2.5 * cube.z_step
        Instrument.use_pixelsize_from_cube(self, cube)
