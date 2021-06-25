# -*- coding: utf-8 -*-

import numpy as np


try:
    from astropy.io import fits
except ImportError:
    import pyfits as fits

import logging

logging.basicConfig(level=logging.INFO)

#
# This file contains the PointSpreadFunction and LineSpreadFunction interfaces
# as well as some basic implementations of these interfaces :
#   - Gaussian PSF
#   - Moffat PSF
#   - Gaussian LSF
#   - MUSE LSF (only if mpdaf module is available)
#
# The instrument will use both 2D PSF and 1D LSF
# to create a 3D PSF with which it will convolve the cubes.
#


## POINT SPREAD FUNCTIONS ######################################################


class PointSpreadFunction:
    """
    This is the interface all Point Spread Functions (PSF) should implement.
    """

    logger = logging.getLogger('GalPaK')

    def as_image(self, for_cube):
        """
        Should return this PSF as a 2D image shaped [for_cube].

        for_cube: HyperspectralCube
            Has additional properties computed and attributed by GalPaK :
                - xy_step (in ")
                - z_step (in µm)
                - z_central (in µm)

        :rtype: ndarray
        """
        raise NotImplementedError()


class NoPointSpreadFunction(PointSpreadFunction):
    """
    A point spread function that does not spread anything, and returns the cube unchanged.
    Passing this to the instrument's psf is the same as passing None.
    """
    def __init__(self):
        pass

    def as_image(self, for_cube):
        """
        Return the identity PSF, chock-full of ones.
        """
        shape = for_cube.shape[1:]
        return np.ones(shape)


class ImagePointSpreadFunction(PointSpreadFunction):
    """
    A custom point spread function using a provided 2D image
    that should have the same shape as the cube's (x,y) and
    centroid should be at
        xo = (shape[1] - 1) / 2 - (shape[1] % 2 - 1)
        yo = (shape[0] - 1) / 2 - (shape[0] % 2 - 1)

    """
    def __init__(self, image_2d):
        """
        accepts fits file or ndarray

        """
        if isinstance(image_2d, str):
            self.filename = image_2d
            my_image = fits.open(image_2d)
            if my_image['PRIMARY'].data is not None:
                 image_2d = my_image['PRIMARY'].data
            elif my_image['DATA'].data is not None:
                 image_2d = my_image['DATA'].data
            
        elif isinstance(image_2d,np.ndarray):
             image_2d = image_2d
             self.filename = str(image_2d.__class__)
        else:
            raise ValueError(' PSF provided is not a fits file nor an array !!')

        logging.info( "Normalizing PSF image")
        self.image_2d =  image_2d /  image_2d.sum()

        if isinstance(self.image_2d,np.ndarray) is False:
            raise ValueError(' PSF provided could not be stored in an ndarray')

        if len(self.image_2d.shape)!=2:
            raise ValueError(' PSF provided is not a 2D image')

    def as_image(self, for_cube):
        #check for size
        if for_cube.shape[1:] != self.image_2d.shape:
            raise ValueError(' PSF Image and cube have different sizes: %s vs. %s' % (str(for_cube.shape[1:]),str(self.image_2d.shape)) )
        return self.image_2d

    def __str__(self):
        return """[PSF] :
  type = custom
  filename = {i.filename}""".format(i=self)


class GaussianPointSpreadFunction(PointSpreadFunction):
    """
    The default Gaussian Point Spread Function.

    fwhm: float
        Full Width Half Maximum in arcsec, aka. "seeing".
    pa: float [default is 0.]
        Position Angle of major-axis, anti-clockwise rotation from Y-axis, in angular degrees.
    ba: float [default is 1.0]
        Axis ratio of the ellipsis, b/a ratio (y/x).
    """
    def __init__(self, fwhm=None, pa=0, ba=1.0):
        self.fwhm = fwhm
        self.pa = pa
        self.ba = ba

    def __str__(self):
        return """[PSF] :
  type = gaussian
  fwhm         = {i.fwhm} "
  pa           = {i.pa} °
  ba           = {i.ba}""".format(i=self)

    def as_image(self, for_cube, xo=None, yo=None):

        shape = for_cube.shape[1:]

        if xo is None:
            xo = (shape[1] - 1) / 2 - (shape[1] % 2 - 1)
        if yo is None:
            yo = (shape[0] - 1) / 2 - (shape[0] % 2 - 1)

        y, x = np.indices(shape)
        r = self._radius(xo, yo, x, y)
        fwhm = self.fwhm / for_cube.xy_step #in pixels

        psf = np.exp(-0.5 * (r / (fwhm / 2.35482)) ** 2)

        return psf / psf.sum()

    def _radius(self, xo, yo, x, y):
        """
        Computes the radii, taking into account the variance and the elliptic shape
        """
        dx = xo - x
        dy = yo - y
        # Rotation matrix around z axis
        # R(90)=[[0,1],[-1,0]] so anti-clock-wise y -> x & x -> -y
        radian_pa = np.radians(self.pa)
        dx_p = dx * np.cos(radian_pa) + dy * np.sin(radian_pa)
        dy_p = -dx * np.sin(radian_pa) + dy * np.cos(radian_pa)

        return np.sqrt(dx_p ** 2 / self.ba ** 2+ dy_p ** 2 )


class MoffatPointSpreadFunction(GaussianPointSpreadFunction):
    """
    The Moffat Point Spread Function

    fwhm if alpha is None: float [in arcsec]
        Moffat's distribution fwhm variable : http://en.wikipedia.org/wiki/Moffat_distribution
    alpha if fwhm is None: float [in arcsec]
        Moffat's distribution alpha variable : http://en.wikipedia.org/wiki/Moffat_distribution
    beta: float
        Moffat's distribution beta variable : http://en.wikipedia.org/wiki/Moffat_distribution

    pa: float [default is 0.]
        Position Angle of major-axis, the anti-clockwise rotation from Y,
        in angular degrees.
    ba: float [default is 1.0]
        Axis ratio of the ellipsis, b/a ratio (y/x).
    """

    def __init__(self, fwhm=None, alpha=None, beta=None, pa=None, ba=None):
        self.alpha = alpha
        self.beta = beta
        if (alpha is None) or (fwhm is None):
            GaussianPointSpreadFunction.__init__(self, fwhm, pa, ba)
        else:
            raise Exception("Moffat error: please set alpha or fwhm but not both ")
        if self.pa is None:
            raise Exception("Moffat error: please set P.A. 'pa'")
        if self.ba is None:
            raise Exception("Moffat error: please set axis ratio b/a 'ba'")
        if self.beta is None:
            raise Exception("Moffat error: please set beta parameter")

    def __str__(self):
        return """[PSF] :
  type = Moffat
  fwhm         = {i.fwhm} "
  alpha        = {i.alpha} "
  beta         = {i.beta}  
  pa           = {i.pa} °
  ba           = {i.ba}""".format(i=self)

    def as_image(self, for_cube, xo=None, yo=None):
       
        shape = for_cube.shape[1:]

        if xo is None:
            xo = (shape[1] - 1) / 2 - (shape[1] % 2 - 1)
        if yo is None:
            yo = (shape[0] - 1) / 2 - (shape[0] % 2 - 1)

        y, x = np.indices(shape)
        r = self._radius(xo, yo, x, y)

        beta = self.beta
        if self.alpha is None:
            # Get the FWHM in pixels (we assume the pixels are squares!)
            fwhm = self.fwhm / for_cube.xy_step
            alpha = fwhm / (2.*np.sqrt(2.**(1./beta)-1) )
        if self.fwhm is None:
            # Get the FWHM in pixels (we assume the pixels are squares!)
            alpha = self.alpha / for_cube.xy_step
            fwhm = alpha  * ( 2.*np.sqrt(2.**(1./beta)-1) )  

        psf = (1. + (r / alpha) ** 2) ** (-beta)

        return psf / psf.sum()


## LINE SPREAD FUNCTIONS #######################################################


class LineSpreadFunction:
    """
    This is the interface all Line Spread Functions (LSF) should implement.
    """

    z_cunit = 'Undef'

    def as_vector(self, for_cube):
        """
        Should return this LSF as a 1D vector shaped [for_cube].

        for_cube: HyperspectralCube

        :rtype: ndarray
        """
        raise NotImplementedError()

class NoLineSpreadFunction(LineSpreadFunction):
    """
    A point spread function that does not spread anything, and returns the cube unchanged.
    Passing this to the instrument's lsf is the same as passing None.
    """
    def __init__(self):
        pass

    def as_vector(self, for_cube):
        """
        returns the identity LSF with ones
        :param for_cube:
        :return:
        """
        shape = for_cube.shape[0]
        return np.ones(shape)

    def __str__(self):
        return """[LSF] :\n  type = undefined """


class VectorLineSpreadFunction(LineSpreadFunction):
    """
    A custom line spread function using a provided 1D `vector`
    that should have the same length as the cube's (z).
    Should be centered around zo = (zsize - 1) / 2 - (zsize % 2 - 1)
    """

    def __init__(self, vector):
        self.vector = vector

    def as_vector(self, for_cube):
        return self.vector

    def __str__(self):
        return """[LSF] \n type = Custom """


class GaussianLineSpreadFunction(LineSpreadFunction):
    """
    A line spread function that spreads as a gaussian.
    We assume the centroid is in the middle.

    fwhm: float
        Full Width Half Maximum, in units of CUNIT3
    """
    def __init__(self, fwhm):
        self.fwhm = fwhm

    def __str__(self):
        return """[LSF] :
  type = Gaussian
  fwhm = {i.fwhm}  {i.z_cunit} \n""".format(i=self)

    def as_vector(self, for_cube):
        # Std deviation from FWHM
        sigma = self.fwhm / 2.35482 / for_cube.z_step
        # Resulting vector shape
        depth = for_cube.shape[0]
        # Assymmetric range around 0
        zo = (depth - 1) / 2 - (depth % 2 - 1)
        z_range = np.arange(depth) - zo
        # Compute gaussian (we assume peak is at 0, ie. µ=0)
        lsf_1d = self.gaussian(z_range, 0, sigma)
        # Normalize and serve
        return lsf_1d / lsf_1d.sum()

    @staticmethod
    def gaussian(x, mu, sigma):
        """
        Non-normalized gaussian function.

        x : float|numpy.ndarray
            Input value(s)
        mu : float
            Position of the peak on the x-axis
        sigma : float
            Standard deviation

        :rtype: Float value(s) after transformation, of the same shape as input x.
        """
        return np.exp((x - mu) ** 2 / (-2. * sigma ** 2))


class MUSELineSpreadFunction(LineSpreadFunction):
    """
    A line spread function that uses MPDAF's LSF.
    See http://urania1.univ-lyon1.fr/mpdaf/chrome/site/DocCoreLib/user_manual_PSF.html

    .. warning::
        This requires the mpdaf module.
        Currently, the MPDAF module only works for odd arrays.
    model: string
        See ``mpdaf.MUSE.LSF``'s ``typ`` parameter.
    """
    def __init__(self, model="qsim_v1"):
        self.model = model
        try:
            from mpdaf.MUSE import LSF
        except ImportError:
            raise ImportError("You need the mpdaf module to use MUSELineSpreadFunction.")
        self.lsf = LSF(typ=self.model)


    def __str__(self):
        return """MUSE LSF : model = '{i.model}'""".format(i=self)

    def as_vector(self, cube):
        # Resulting vector shape
        depth = cube.shape[0]
        odd_depth = depth if depth % 2 == 1 else depth+1
        # Get LSF 1D from MPDAF
        if 'micron' in cube.z_cunit.lower():
            wavelength_aa = cube.z_central * 1e4  # unit conversion from microns to AA
            z_step_aa = cube.z_step * 1e4
        else:
            wavelength_aa = cube.z_central
            z_step_aa = cube.z_step

        lsf_1d = self.lsf.get_LSF(lbda=wavelength_aa, step=z_step_aa, size=odd_depth)

        x=np.arange(np.size(lsf_1d))
        sigma = np.sqrt(np.sum(x**2*lsf_1d)-np.sum(x*lsf_1d)**2) * cube.z_step

        self.fwhm = sigma * 2.35

        # That LSF is of an odd depth, truncate it if necessary
        # FIXME @nicolas : this is a hotfix, not really pretty, how can we do this better?
        if depth % 2 == 0:
            lsf_1d = lsf_1d[:-1]
        # Normalize and serve
        return lsf_1d / lsf_1d.sum()
