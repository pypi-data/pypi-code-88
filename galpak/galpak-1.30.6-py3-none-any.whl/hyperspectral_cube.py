# -*- coding: utf-8 -*-
from __future__ import division

import logging
import math


import numpy as np

from astropy.io import fits

logging.basicConfig(level=logging.INFO)
logHC = logging.getLogger('GalPak: HyperCube')


# Some todos
#
#Sanitization operations :
#    - IDL-made FITS :
#        - keyword FSCALE (http://astro.uni-tuebingen.de/software/idl/astrolib/fits/mrdfits.html)
#        - other non-ISO header blunders -_-
#    - CDEL_3 => CDELT3
#
#Use SI units, http://www.aanda.org/articles/aa/full_html/2010/16/aa15362-10/aa15362-10.html#S39
#Uniformization operations :
#    - Spatial Units !
#    - Spectral Units !

class HyperspectralCube:
    """
    A hyperspectral cube has 3 dimensions : 2 spatial, and 1 spectral.
    It is basically a rectangular region of the sky seen on a discrete subset of
    the light spectrum. It is heavily used in spectral imaging, and is provided
    by spectroscopic explorers such as MUSE.

    This class is essentially a convenience wrapper for data values and header
    specs of a single hyperspectral cube.

    It understands the basic arithmetic operations ``+ - * / **``,
    which should behave much like with numpy's ndarrays, and update the header accordingly.
    An operation between a cube and a number will behave as expected, by applying the operation voxel-by-voxel
    to the cube. (it broadcasts the number to the shape of the cube)
    An operation between a cube and an image (a slice along the spectral axis, z) will behave as expected,
    by applying the operation image-by-image to the cube. (it broadcasts the image to the shape of the cube)

    It also understands indexation of the form ``cube[zmin:zmax, ymin:ymax, xmin:xmax]``.

    See also http://en.wikipedia.org/wiki/Hyperspectral_imaging .

    Note : no FSCALE management is implemented yet.


    Factories
    ---------

    You can load from a single HDU of a FITS (Flexible Image Transport System) file : ::

        HyperspectralCube.from_file(filename, hdu_index=None, verbose=False)


    Parameters
    ----------

    data: numpy.ndarray|None
        3D numpy ndarray holding the raw data.
        The indices are the pixel coordinates in the cube.
        Note that in order to be consistent with astropy.io.fits,
        data is indexed in that order : λ, y, x.

    header: fits.Header|None
        http://docs.astropy.org/en/latest/io/fits/api/headers.html
        Note: this might become its own wrapper class in the future.

    verbose: boolean
        Set to True to log everything and anything.

    """
    xy_step = None
    z_cunit = 'Undef'
    z_step = None
    z_central = None

    def __init__(self, data=None, header=None, verbose=False, filename=None, variance=None):
        self.data = data
        self.header = header
        self.verbose = verbose
        self.filename = filename
        self.var = variance

        if header is not None:
            if not isinstance(header, fits.Header):
                raise TypeError("Header must be a fits Header")
            # Sanitize
            self.sanitize()
            #initialize
            try:
                self.initialize_self_cube()
            except:
                pass

    def defaults_from_instrument(self, instrument=None):
        """
        First reads the header for
            xy_step (CDELT1 or CD1_1)
            z_step (CDELT3 or CD3_3)
            z_cunit (CUNIT3)
            crpix (CRPIX3)
            crval (CRVAL3).
        If some of these are None, get the default values from the instrument
        and then reset the header :
            xy_step: Instrument.xy_step --> self.xy_step
            z_step:  Instrument.z_step -->  self.z_step --> CDELT3
            z_cunit: Instrument.z_cunit --> self.z_cunit --> CUNIT3
            crpix:  shape[0]/2 --> CRPIX3
            crval: Instrument.z_central --> self.z_central --> CRVAL3

         for CUNIT3 CRVAL3 CRPIX3 CDELT3
        """

        xy_step = self.get_steps()[1]
        z_step = self.header.get('CDELT3')
        z_cunit = self.header.get('CUNIT3')
        crpix = self.header.get('CRPIX3')
        crval = self.header.get('CRVAL3')

        if xy_step is None:
            self.xy_step = instrument.cube_default_xy_step

        if z_step is None:
            self.z_step = instrument.cube_default_z_step
            self.header.set('CDELT3', self.z_step)
            if 'CD3_3' in self.header.keys():
                self.header.remove('CD3_3')

        if z_cunit is None and instrument.cube_default_cunit is not None:
            self.z_cunit = instrument.cube_default_cunit
            self.header.set('CUNIT3', self.z_cunit)
        if crval is None and instrument.cube_default_z_central is not None:
            self.z_central = instrument.cube_default_z_central
            self.header.set('CRVAL3', self.z_central)
        if crpix is None:
            self.header.set('CRPIX3', (self.shape[0]) / 2.)

    def initialize_self_cube(self):
        """
        Initialize steps xy_steps z_steps z_cunnit and z_central
        z_central requires CRPIX3 CRVAL3 CDELT3
        """

        steps = self.get_steps()
        if (steps[1] is not None) and (steps[2] is not None):
            if np.abs(np.abs(steps[1]) - np.abs(steps[2])) > 1e-2:
                # when the size of pixels differ by more than 1%
                raise NotImplementedError(
                    "GalPak does not support unsquare pixels")
            xy_step = steps[1]
            if (self.header.get('CUNIT1') is not None):
                if ('deg' in self.header.get('CUNIT1') ):
                    xy_step *= 3600  # convert from deg to "
                if ('mas' in self.header.get('CUNIT1') ):
                    xy_step /= 1e3 # convert from mas to "
            else:
                raise ValueError("The Cube has no cunit1 for the spaxels, "
                                 "use cunit1 to provide it")

            self.xy_step = xy_step

        self.z_step = steps[0]

        if self.header.get('CUNIT3') is not None:
            self.z_cunit = self.header['CUNIT3']
        else:
           raise ValueError("The Cube has no cunit3 for the spaxels, "
                                 "use cunit3 to provide it")

        if self.z_central is None:
                self.z_central = self.wavelength_of(math.floor(self.shape[0] / 2.)-1)

    @staticmethod
    def from_file(filename, hdu_index=None, verbose=False):
        """
        Factory to create a HyperspectralCube from one HDU in a FITS file.
        http://fits.gsfc.nasa.gov/fits_standard.html

        No other file formats are supported at the moment.
        You may specify the index of the HDU you want.
        If you don't, it will try to guess by searching for a HDU with EXTNAME=DATA,
        or it will pick the first HDU in the list that has 3 dimensions.

        filename: string
            An absolute or relative path to the FITS file we want to load.
            The `astropy.io.fits` module is used to open the file.
        hdu_index: integer|None
            Index of the HDU to load. If you set this, guessing is not attempted.
        verbose: boolean
            Should we fill up the log with endless chatter ?

        :rtype: HyperspectralCube
        """
        try:
            hdu_list = fits.open(filename)
        except Exception:
            raise IOError("Could not open provided FITS file '%s'", filename)

        if verbose:
            logHC.disabled=False
        else:
            logHC.disabled=True

        logHC.info("Opening %s.", filename)

        # Find out which HDU we should read the data from
        hdu = header = None
        extnames = [h.header.get('EXTNAME','').lower() for h in hdu_list]

        def _sanity_check_dimensions(header, hdu_index):
            if header.get('NAXIS') != 3:
                logHC.error("HDU dimensions : NAXIS is only #%d not 3", header.get('NAXIS'))
                raise ValueError("Not a cube")

        # 1/ If set, use HDU indexed at hdu_index
        if hdu_index is not None:
            if hdu_index < 0 or hdu_index >= len(hdu_list):
                raise IOError("Specified HDU #%d is not available", hdu_index)
            logHC.warning("Found extention %d for data" % (hdu_index))

            hdu = hdu_list[hdu_index]
            header = hdu.header
            data = hdu.data
            if hdu_index < len(hdu_list):
                logHC.warning("Using next extention %d for Variance"  % (hdu_index+1))
                variance = hdu_list[hdu_index+1].data
            else:
                variance = None
            _sanity_check_dimensions(header, hdu_index)
        else:
            # 2/ Try to find DATA extension HDU
            found_data_hdu = False
            hdu_index = 0
            while not found_data_hdu and hdu_index < len(hdu_list):
                hdu = hdu_list[hdu_index]
                header = hdu.header
                if 'data' in header.get('EXTNAME', '').lower():
                    try:
                        _sanity_check_dimensions(header, hdu_index)
                    except IOError:
                        hdu_index += 1
                    else:
                        found_data_hdu = True
                else:
                    hdu_index += 1

            # 3/ Try any other HDU, starting with Primary
            if not found_data_hdu:
                hdu_index = 0
                while not found_data_hdu and hdu_index < len(hdu_list):
                    hdu = hdu_list[hdu_index]
                    header = hdu.header
                    try:
                        _sanity_check_dimensions(header, hdu_index)
                    except IOError:
                        hdu_index += 1
                    else:
                        found_data_hdu = True

            # 4/ Alert! Exception raised
            if not found_data_hdu:
                raise IOError("Could not find a HDU containing 3 dimensional "
                              "data in file '%s'." % filename)
            else:
                # Zealous sanity check (skipped if python is run with -O or -OO)
                assert hdu is not None and header is not None

                # Collect and numpyfy data
                data = np.array(hdu.data, dtype=float)

                #look for variance
                found_variance_hdu = False
                hdu_index = 0
                if ('variance' in extnames):
                    hdu_index = hdu_list.index_of('STAT')
                    hdu = hdu_list[hdu_index]
                    header = hdu.header
                    found_variance_hdu = True
                if ('stat' in extnames):
                    hdu_index = hdu_list.index_of('STAT')
                    hdu = hdu_list[hdu_index]
                    header = hdu.header
                    found_variance_hdu = True
                if found_variance_hdu:
                    logHC.info('Found Variance data in file %s' % (filename))
                    try:
                        _sanity_check_dimensions(header, hdu_index)
                        variance = np.array(hdu.data, dtype=float)
                    except IOError:
                        raise IOError("Could not find a variance with proper dimensions")
                else:
                    logHC.debug("Variance data not present in file '%s'." % filename)
                    variance = None
                    
        return HyperspectralCube(data=data, header=header, verbose=verbose, filename=filename, variance=variance)

    @staticmethod
    def from_mpdaf(cube, verbose=False):
        """
        Factory to create a cube from a `MPDAF Cube <http://urania1.univ-lyon1.fr/mpdaf/chrome/site/DocCoreLib/user_manual_cube.html>`_.
        """
        header = cube.data_header
        data = cube.data
        variance = cube.var

        return HyperspectralCube(data=data, header=header, verbose=verbose, filename=cube.filename, variance=variance)

    @property
    def shape(self):
        """
        Returns the shape of the data, that is a tuple of the cardinality of each dimension.
        """
        if self.data is None:
            return ()  # behave consistently with numpy.ndarray
        return self.data.shape

    def is_empty(self):
        """
        Is this cube void of any data ?

        return boolean
        """
        return self.data is None

    def has_header(self):
        """
        Does this cube have a header ?

        return boolean
        """
        return self.header is not None

    def patch(self, crval3=None, crpix3=None, cunit3=None, cdelt3=None, ctype3=None, cunit1=None, force=False):
        """
        Patches up the Cube's missing header values.
        Will raise a ValueError if the values are already in the header unless you use the force=.

        crval3: float
            A value for the cube's header's CRVAL3.
        crpix3: float
            A value for the cube's header's CRPIX3.
        cunit3: str
            A value for the cube's header's CUNIT3.
        cdelt3: float
            A value for the cube's header's CDELT3.
        ctype3: float
            A value for the cube's header's CTYPE3.
        cunit1: str
            A value for the cube's header's CUNIT1.
        force: bool
            Set to True if you want to overwrite existing header cards.
        """

        logHC.info('Patching the header with cards provided')

        if not self.has_header():
            self.header = fits.Header()

        if crval3 is not None:
            if force or self.header.get('CRVAL3') is None:
                self.header.set('CRVAL3', crval3)
            else:
                raise ValueError("The cube already has a CRVAL3 header card. Use the force=.")

        if crpix3 is not None:
            if force or self.header.get('CRPIX3') is None:
                self.header.set('CRPIX3', crpix3)
            else:
                raise ValueError("The cube already has a CRPIX3 header card. Use the force=.")

        if cdelt3 is not None:
            if force or self.header.get('CDELT3') is None:
                self.header.set('CDELT3', cdelt3)
                if 'CD3_3' in self.header.keys():
                     self.header.remove('CD3_3')
            else:
                raise ValueError("The cube already has a CDELT3 header card. Use the force=.")

        if cunit3 is not None:
            if force or self.header.get('CUNIT3') is None:
                self.header.set('CUNIT3', cunit3)
            else:
                raise ValueError("The cube already has a CUNIT3 header card. Use the force=.")

        if ctype3 is not None:
            if force or self.header.get('CTYPE3') is None:
                self.header.set('CTYPE3', ctype3)
            else:
                raise ValueError("The cube already has a CTYPE3 header card. Use the force=.")

        if cunit1 is not None:
            if force or self.header.get('CUNIT1') is None:
                self.header.set('CUNIT1', cunit1)
            else:
                raise ValueError("The cube already has a CUNIT1 header card. Use the force=.")

        #logging.debug('Header after patch ' +  self.__str__() )

    def __str__(self):
        """
        Simple but useful string representation of the header and the data's shape.
        """
        if self.has_header():
            header = self.header.tostring("\n        ").strip()
        else:
            header = "None"
        if self.is_empty():
            data = "None"
        else:
            data = "ndarray of shape %s" % str(self.data.shape)

        return """HyperspectralCube
    header :
        {header}
    data : {data}
""".format(header=header, data=data)

    def __add__(self, other):
        """
        Addition should work pretty much like numpy's ndarray addition.

        HyperspectralCube + Number = HyperspectralCube
            => add the number to each voxel of the cube

        HyperspectralCube + HyperspectralCube = HyperspectralCube
            => requires the input cubes to be of broadcast-compatible shapes

        Raises TypeErrors when cubes are empty or operands are not compatible.
        """
        if self.is_empty():
            raise TypeError("Cannot use operand + on empty HyperspectralCube.")

        if isinstance(other, HyperspectralCube):
            if other.is_empty():
                raise TypeError("Cannot use operand + on empty HyperspectralCube.")
            data = self.data + other.data
        else:
            data = self.data + other  # numpy will raise when inappropriate

        return HyperspectralCube(data=data, header=self.header)

    def __radd__(self, other):
        """
        Addition following Peano axioms is commutative on our sets.
        """
        return self.__add__(other)

    def __sub__(self, other):
        """
        Subtraction should work pretty much like numpy's ndarray subtraction.

        HyperspectralCube - Number = HyperspectralCube
            => subtract the number to each voxel of the cube

        HyperspectralCube - HyperspectralCube = HyperspectralCube
            => requires the input cubes to be of broadcast-compatible shapes

        Raises TypeErrors when cubes are empty or operands are not compatible.
        """
        if self.is_empty():
            raise TypeError("Cannot use operand - on empty HyperspectralCube.")

        if isinstance(other, HyperspectralCube):
            if other.is_empty():
                raise TypeError("Cannot use operand - on empty HyperspectralCube.")
            data = self.data - other.data
        else:
            data = self.data - other  # numpy will raise when inappropriate

        return HyperspectralCube(data=data, header=self.header)

    def __rsub__(self, other):
        """
        Subtraction should work pretty much like numpy's ndarray subtraction.

        Number - HyperspectralCube = HyperspectralCube
            => subtract each voxel of the cube to the number, in each voxel

        HyperspectralCube - HyperspectralCube = HyperspectralCube
            => requires the input cubes to be of broadcast-compatible shapes

        Raises TypeErrors when cubes are empty or operands are not compatible.
        """
        if self.is_empty():
            raise TypeError("Cannot use operand - on empty HyperspectralCube.")

        if isinstance(other, HyperspectralCube):
            if other.is_empty():
                raise TypeError("Cannot use operand - on empty HyperspectralCube.")
            data = other.data - self.data
        else:
            data = other - self.data  # numpy will raise when inappropriate

        return HyperspectralCube(data=data, header=self.header)

    def __mul__(self, other):
        """
        Multiplication should work pretty much like numpy's ndarray multiplication.

        HyperspectralCube * Number = HyperspectralCube
            => multiply each voxel of the cube by the number

        HyperspectralCube * HyperspectralCube = HyperspectralCube
            => requires the input cubes to be of broadcast-compatible shapes

        Raises TypeErrors when cubes are empty or operands are not compatible.
        """
        if self.is_empty():
            raise TypeError("Cannot use operand * on empty HyperspectralCube.")

        if isinstance(other, HyperspectralCube):
            if other.is_empty():
                raise TypeError("Cannot use operand * on empty HyperspectralCube.")
            data = self.data * other.data
        else:
            data = self.data * other  # numpy will raise when inappropriate

        return HyperspectralCube(data=data, header=self.header)

    def __rmul__(self, other):
        """
        Multiplication following Peano axioms is commutative on our sets.
        """
        return self.__mul__(other)

    def __truediv__(self, other):
        """
        Division should work pretty much like numpy's ndarray division.
        We don't check for division by 0, and let exceptions bubble from numpy.
        It's faster, tends to be IEEE 754 compliant, and is consistent with numpy.

        TODO: find out the potential impact of from __future__ import division on this

        HyperspectralCube / Number = HyperspectralCube
            => divide each voxel of the cube by the number

        HyperspectralCube / HyperspectralCube = HyperspectralCube
            => requires the input cubes to be of broadcast-compatible shapes

        Raises TypeErrors when cubes are empty or operands are not compatible.
        """
        if self.is_empty():
            raise TypeError("Cannot use operand / on empty HyperspectralCube.")

        if isinstance(other, HyperspectralCube):
            if other.is_empty():
                raise TypeError("Cannot use operand / on empty HyperspectralCube.")
            data = self.data / other.data
        else:
            data = self.data / other  # numpy will raise when inappropriate

        return HyperspectralCube(data=data, header=self.header)

    def __rdiv__(self, other):
        """
        Division should work pretty much like numpy's ndarray division.
        We don't check for division by 0, and let exceptions bubble from numpy.
        It's faster, tends to be IEEE 754 compliant, and is consistent with numpy.

        Number / HyperspectralCube = HyperspectralCube
            => divide each voxel of the cube by the number

        HyperspectralCube / HyperspectralCube = HyperspectralCube
            => requires the input cubes to be of broadcast-compatible shapes

        Raises TypeErrors when cubes are empty or operands are not compatible.
        """
        if self.is_empty():
            raise TypeError("Cannot use operand / on empty HyperspectralCube.")

        if isinstance(other, HyperspectralCube):
            if other.is_empty():
                raise TypeError("Cannot use operand / on empty HyperspectralCube.")
            data = other.data / self.data
        else:
            data = other / self.data  # numpy will raise when inappropriate

        return HyperspectralCube(data=data, header=self.header)

    def __pow__(self, power):
        """
        Exponentiation should work pretty much like numpy's ndarray exponentiation.

        HyperspectralCube ** Number = HyperspectralCube
            => power each voxel of the cube by the number

        HyperspectralCube ** HyperspectralCube = HyperspectralCube
            => requires the input cubes to be of broadcast-compatible shapes

        Raises TypeErrors when cubes are empty or operands are not compatible.
        """
        if self.is_empty():
            raise TypeError("Cannot use operand ** on empty HyperspectralCube.")

        if isinstance(power, HyperspectralCube):
            if power.is_empty():
                raise TypeError("Cannot use operand ** on empty HyperspectralCube.")
            data = self.data ** power.data
        else:
            data = self.data ** power  # numpy will raise when inappropriate

        return HyperspectralCube(data=data, header=self.header)

    def __rpow__(self, base):
        """
        Exponentiation should work pretty much like numpy's ndarray exponentiation.

        Number ** HyperspectralCube = HyperspectralCube
            => each voxel of the cube is the exponent of the number

        HyperspectralCube ** HyperspectralCube = HyperspectralCube
            => requires the input cubes to be of broadcast-compatible shapes

        Raises TypeErrors when cubes are empty or operands are not compatible.
        """
        if self.is_empty():
            raise TypeError("Cannot use operand ** on empty HyperspectralCube.")

        if isinstance(base, HyperspectralCube):
            if base.is_empty():
                raise TypeError("Cannot use operand ** on empty HyperspectralCube.")
            data = base.data ** self.data
        else:
            data = base ** self.data  # numpy will raise when inappropriate

        return HyperspectralCube(data=data, header=self.header)

    def __getitem__(self, item):
        """
        HyperspectralCube[λmin:λmax, ymin:ymax, xmin:xmax] => HyperspectralCube

        The selector is quite similar to numpy's ndarray selector : min is included, max is excluded.
        You can use negative values, Python slicing syntax, as described here :
        http://docs.scipy.org/doc/numpy/reference/arrays.indexing.html

        :rtype: HyperspectralCube
        """
        if self.is_empty():
            raise TypeError("Cannot use [:,:,:] selector on empty HyperspectralCube.")

        data = self.data[item]

        if self.has_header():
            header = self.header.copy()
            self.check_header()
            # todo : adjust header values to the cut
            raise NotImplementedError("This class does not update the headers. "
                                      "Use mpdaf.obj.Cube to cut AND update headers.")
        else:
            header = None

        return HyperspectralCube(data=data, header=header)

    def __setitem__(self, key, value):
        """
        HyperspectralCube[λmin:λmax, ymin:ymax, xmin:xmax] = HyperspectralCube
        HyperspectralCube[λmin:λmax, ymin:ymax, xmin:xmax] = Number
        HyperspectralCube[λmin:λmax, ymin:ymax, xmin:xmax] = numpy.ndarray

        The indexed mutator is quite similar to numpy's ndarray's : min is included, max is excluded.
        You can use negative values, Python slicing syntax, as described here :
        http://docs.scipy.org/doc/numpy/reference/arrays.indexing.html

        This mutates this HyperspectralCube's data and does not return anything.

        value: HyperspectralCube or numpy.ndarray or Number
            Must be broadcastable to shape defined by the [λ,y,x] slice.

        """
        if self.is_empty():
            raise TypeError("Cannot use [:,:,:] selector on empty HyperspectralCube.")

        if isinstance(value, HyperspectralCube):
            values = value.data
            # fixme: make sure headers are compatible
        else:
            values = value

        self.data[key] = values  # numpy will raise appropriate errors

    def copy(self, out=None):
        """
        Copies this cube into out (if specified) and returns the copy.

        :rtype: HyperspectralCube
        """
        # LBYL pattern, as self.data MUST be a numpy.ndarray and we don't want this to be silenced
        if self.is_empty():
            data = None
        else:
            data = self.data.copy()
            # Same for header, MUST be an instance of astropy.io.fits.Header
        if self.has_header():
            header = self.header.copy()
        else:
            header = None

        if out is None:
            out = HyperspectralCube(data=data, header=header)
        else:
            if not isinstance(out, HyperspectralCube):
                raise IOError("out parameter must be an instance of HyperspectralCube")
            out.data = data
            out.header = data

        return out

    def write_to(self, filename, overwrite=False):
        """
        Write this cube to a FITS file.

        filename: string
            The filename (absolute or relative) of the file we want to write to.
            The `astropy.io.fits` module is used to write to the file.
        overwrite: bool
            When set to True, will overwrite the output file if it exists.
        """
        #astropy v1.2.1 IO does not work with MaskedArrays
        if 'ndarray' in str(type(self.data)):
            primary_hdu = fits.PrimaryHDU(data=self.data, header=self.header)
        elif 'MaskedArray' in str(type(self.data)):
            primary_hdu = fits.PrimaryHDU(data=self.data.data, header=self.header)
        else:
            IOError('Hyperspectral cube data is neither ndarray or MaskedArray')
        hdulist = fits.HDUList([primary_hdu])
        hdulist.writeto(filename, overwrite=overwrite)
        if self.verbose:
            logHC.info("Writing HyperspectralCube to file %s.", filename)
            # Note: astropy already logs something similar, is this really necessary ?

    def get_steps(self):
        """
        Returns a list of the 3 steps [λ,y,x].
        The units are the ones specified in the header.
        """
        if not self.has_header():
            raise IOError("Cannot get the steps of a Cube without header.")
        else:
            #@fixme: need to fix when both present
            if ('CD3_3' in self.header.keys() and 'CDELT3' in self.header.keys()):
                  logHC.info('Both CD3_3 and CDELT3 are present \n will use CDELT3 !')
                  z_step = self.header.remove('CD3_3')
            z_step = self.header.get('CD3_3') or self.header.get('CDELT3')
            try:
                x_step = np.sqrt(self.header.get('CD1_1')**2. + self.header.get('CD1_2')**2. )
                y_step = np.sqrt(self.header.get('CD2_2')**2. + self.header.get('CD2_1')**2. )
            except:
                x_step = self.header.get('CDELT1')
                y_step = self.header.get('CDELT2')


        return [z_step, y_step, x_step]

    def pixel_from_lambda(self, wavelength):
        """
        Returns the pixel index (starting at 0) for the passed wavelength,
        whose unit must be the one specified in the header.

        :rtype: float
        """

        wavelength_array = np.array(wavelength)
        crval = self.header.get('CRVAL3')
        crpix = self.header.get('CRPIX3')
        if 'CD3_3' in self.header.keys() and 'CDELT3' in self.header.keys():
            logHC.info("CD3_3 and CDELT3 are both present\n will use CDELT3")
            self.header.remove('CD3_3')
        cdelt = self.header.get('CDELT3') or self.header.get('CD3_3')

        if crval is None or crpix is None or cdelt is None:
            raise IOError("Cube is missing required 'CRVAL3', 'CRPIX3' or 'CDELT3' header card.")

        return (wavelength_array - crval) / cdelt - 1.0 + crpix

    def wavelength_of(self, pixel_index):
        """
        Get the wavelength (in the unit specified in the header) of the specified pixel index along z.
        The pixel index should start at 0.

        :rtype: float
        """
        pixel_array = np.array(pixel_index)
        crval = self.header.get('CRVAL3')
        crpix = self.header.get('CRPIX3')
        if 'CD3_3' in self.header.keys() and 'CDELT3' in self.header.keys():
            logHC.info("CD3_3 and CDELT3 are both present\n will use CDELT3")
            self.header.remove('CD3_3')
        cdelt = self.header.get('CDELT3') or self.header.get('CD3_3')

        if crval is None or crpix is None or cdelt is None:
            raise IOError("Cube is missing required 'CRVAL3', 'CRPIX3' or 'CDELT3' header card.")

        return (pixel_array - crpix + 1.0) * cdelt + crval

    def sanitize(self, header=None, data=None):
        """
        Procedurally apply various sanitization tasks :
        - http://docs.astropy.org/en/latest/io/fits/usage/verification.html (todo)
        - Fix spectral step keyword :
            - CDEL_3 --> CDELT3
            - CD3_3  --> CDELT3
        - Fix blatantly illegal units :
            - DEG --> deg
            - MICRONS --> um

        Sanitizes this cube's header and data, or provided header and data.

        .. warning::
            header and data are mutated, not copied, so this method returns nothing.
        """

        if header is None:
            header = self.header
        if data is None:
            data = self.data

        if header is None:
            return

        # Fix spectral step keyword
        if header.get('CDELT3') is None:
            if header.get('CDEL_3') is not None:
                header.set('CDELT3', header.get('CDEL_3'))
            if header.get('CD3_3') is not None:
                header.set('CDELT3', header.get('CD3_3'))

        # Fix illegal units
        units_keywords = ['CUNIT1', 'CUNIT2', 'CUNIT3']
        for unit_keyword in units_keywords:
            unit = header.get(unit_keyword)
            if unit is not None:
                unit = unit.strip()
                if unit == 'DEG':
                    unit = 'deg'
                elif 'micron' in unit.lower():
                    unit = 'um'
                header.set(unit_keyword, unit)

    def check_header(self):
        """
        Will check that the header exists and has the cards we need :
            - CUNIT3
            - CDELT3
        We need those cards because they contain calibration markers (start value, step, unit)
        without which the data is pretty much just wasted disk space.

        Raises AttributeError when the header does not check out.

        When you load the data into a HyperspectralCube using a FITS file, the factory will
        require the FITS header to pass this check. (unless you specify check=False)
        Note that the sanitization routine will also automatically create a CDELT3 header card
        from a CDEL_3 header card, for example, and therefore will make this check pass.

        If you want this check to pass, you should add the missing cards to the header using
        assignations like the following (albeit after replacing values in <>) : ::

        self.header.set('<MISSING_CARD>', <missing_value>)
        """

        if self.header is None:
            raise AttributeError("Header is not set. You need a Header for this operation.")

        mandatory_cards = [
            'CUNIT3'
            'CDELT3'
        ]

        for card in mandatory_cards:
            value = self.header.get(card)
            if value is None:
                raise AttributeError("Header's '%s' card is missing, but required for this operation.", card)
