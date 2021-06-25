# -*- coding: utf-8 -*-
import numpy
from math import isnan
import logging, os
from astropy.table import Table

#local imports
from .galaxy_parameter import GalaxyParameter
from .string_stdout import StringStdOut
from .ansi_colors import AnsiColors

logging.basicConfig(level=logging.INFO)

class GalaxyParameters(numpy.ndarray):
    """
    A simple wrapper for an array of galaxy parameters.
    It is basically a flat numpy.ndarray of a bunch of floats with convenience
    attributes for explicit (and autocompleted!) access and mutation of
    parameters, and nice casting to string.

    .. warning::
        Undefined parameters will be NaN, not None.

    Example : ::

        from galpak import GalaxyParameters
        gp = GalaxyParameters(x=1.618)

        // Classic numpy.ndarray numeric access
        assert(gp[0] == 1.618)
        // Autocompleted and documented property access
        assert(gp.x == 1.618)
        // Convenience dictionary access,
        assert(gp['x'] == 1.618)
        // ... useful when you're iterating :
        for (name in GalaxyParameters.names):
            print gp[name]

    Parameters :
        - x (pix)
        - y (pix)
        - z (pix)
        - flux
        - radius aka. r½ (pix)
            half-light radius in pixel
        - inclination (deg)
        - pa (deg)
            position angle from y-axis, anti-clockwise.
        - turnover_radius aka. rv (pix)
            turnover radius for arctan, exp, velocity profile
            [is ignored for mass profile]
        - maximum_velocity aka. Vmax (km/s)
            de-projected V_max
            [forced to be positive, with 180deg added to PA]
        - velocity_dispersion aka. s0 (km/s)

    Note that all the parameters are lowercase, even if they're sometimes displayed mixed-case.

    Additional attributes :
        - stdev : Optional stdev margin (GalaxyParametersError).
                  GalPaK3D fills up this attribute.

    """

    # HOW TO CHANGE THE PARAMETERS
    #
    # Say we want to add a new galaxy parameter named `sugar` :
    # 1. Update the list `GalaxyParameters.names`, add 'sugar' at the end.
    # 2. Add the property
    #    sugar = GalaxyParameter(name='sugar', key=10, doc="Some more sugar", unit="sweetness", format="3.2f")
    #      - name (string) : the name of the variable, that MUST be the same as
    #                        the name in `GalaxyParameters.names`
    #      - key (int) : the position in the the ndarray of this parameter.
    #      - short (string) : a shorter name, for compact display.
    #      - doc (string) : some documentation that will appear to the enduser.
    #      - unit (string) : the unit, if any.
    #      - format (string) : the precision to use during string casting,
    #                             as used by `string.format()`.
    # 3. Update this class' __init__() method (signature and assignation)
    # 4. Update this class' __new__() method  (signature and call to __init__)

    names = [
        'x', 'y', 'z',
        'flux',
        'radius',
        'inclination',
        'pa',
        'turnover_radius',
        'maximum_velocity',
        'velocity_dispersion',
    ]

    x = GalaxyParameter(name='x', key=0, doc="X coordinates of the center.", unit="pixel")
    y = GalaxyParameter(name='y', key=1, doc="Y coordinates of the center.", unit="pixel")
    z = GalaxyParameter(name='z', key=2, doc="Z coordinates of the center.", unit="pixel", format='3.6f')
    flux = GalaxyParameter(name='flux', key=3, format='3.2e',
                           doc="Sum of the values of all pixels.", unit="same units as the input Cube")
    radius = GalaxyParameter(name='radius', short="rhalf", key=4, unit="pixel",
                             doc="Radius (half-light) of the galaxy.")
    inclination = pitch = GalaxyParameter(name='inclination', short="incl", key=5, unit="deg", format='4.1f',
                                          doc="Inclination, aka. pitch along observation axis.")
    pa = PA = roll = GalaxyParameter(name='pa', short="PA", key=6, unit="deg", format='5.1f',
                                     doc="Position Angle, anti-clockwise from Y (in degrees),"
                                         "aka. roll along observation axis.")
    turnover_radius = rv = GalaxyParameter(name='turnover_radius', short='rv', key=7, unit="pixel",
                                           doc="The turnover radius, inverse factor rv in arctan(r/rv).")
    maximum_velocity = max_vel = GalaxyParameter(name='maximum_velocity', short="Vmax", key=8, unit="km/s", format='6.2f',
                                                 doc="De-projected maximum velocity."
                                                     "Positive only, with 180deg added to PA.")
    velocity_dispersion = sigma0 = GalaxyParameter(name='velocity_dispersion', short="Vdisp", key=9, unit="km/s",
                                                   doc="Spatially constant disk dispersion,"
                                                       "added to kinematics dispersion.")

    # Developer notes :
    # There are many ways of doing the above :
    #   - decorators : @property, @prop.setter, etc.
    #   - __getattr__() and __setattr__()
    #   - __getattribute__() and __setattribute__()
    #   - explicit property()
    # We are using an extension of property() as it provides a cleaner way
    # to reuse getters and setters with multiple property names,
    # and provides autocompletion and customized docstrings.
    # Python dir() function is useful with __getattr__() and the likes, yet not
    # enough for proper documentation, and function wrappers are just horrible.
    # Another implementation of a similar feature :
    # https://github.com/numpy/numpy/blob/master/numpy/core/records.py

    ## CONSTRUCTORS
    stdev = None #standard deviation

    #confidence intervals
    ICpercentile = None
    lower = None
    upper = None

    """ Optional
    stdev margin (GalaxyParametersError)
    lower / upper bounds for a given percentile
    """

    def __init__(self,
                 x=None, y=None, z=None,
                 flux=None, radius=None,
                 inclination=None, pa=None,
                 turnover_radius=None,
                 maximum_velocity=None,
                 velocity_dispersion=None):


        self.x = x
        self.y = y
        self.z = z
        self.flux = flux
        self.radius = radius
        self.inclination = inclination
        self.pa = pa
        self.turnover_radius = turnover_radius
        self.maximum_velocity = maximum_velocity
        self.velocity_dispersion = velocity_dispersion

    def __new__(cls,
                x=None, y=None, z=None,
                flux=None, radius=None,
                inclination=None, pa=None,
                turnover_radius=None,
                maximum_velocity=None,
                velocity_dispersion=None):
        obj = super(GalaxyParameters, cls).__new__(cls, shape=len(GalaxyParameters.names), dtype=float)
        obj.__init__(
            x, y, z,
            flux, radius,
            inclination, pa,
            turnover_radius,
            maximum_velocity,
            velocity_dispersion
        )
        return obj

    ## NAMED CONSTRUCTORS (FACTORIES)

    @staticmethod
    def from_ndarray(a):
        """
        Factory to easily create a GalaxyParameters object from an ordered ndarray
        whose elements are in the order of `GalaxyParameters.names`.

        Use like this : ::

            from galpak import GalaxyParameters
            gp = GalaxyParameters.from_ndarray(my_ndarray_of_data)

        :rtype: GalaxyParameters
        """
        required_number_of_values = len(GalaxyParameters.names)
        if numpy.size(a, 0) < required_number_of_values:
            raise ValueError("Provide an array of at least %d floats (nan is allowed)" % required_number_of_values)
        return GalaxyParameters(*a)

    def save_to_file(self, filename, overwrite=False):
        """
        filename: file to save parameters
        overwrite: True/False to overwrite file
        """

        if not overwrite and os.path.isfile(filename):
            raise IOError("The file '%s' already exists. Specify overwrite=True to overwrite it.")
        else:
            t1 = self.as_table()
            t1.write(filename, format='ascii.fixed_width', overwrite=overwrite)

    def from_file(self, filename):
        """
        Reads the content from output.dat of GalaxyParameters
        """
        try:
            m = Table.read(filename, format='ascii.fixed_width')
            p = numpy.size(m)

            if p >= 2:
                self.stdev = GalaxyParameters()
            if p >= 3:
                self.lower = GalaxyParameters()
            if p >= 4:
                self.upper = GalaxyParameters()

            for k in self.names:
                self.__setitem__(k,m[k][0])
                if p >= 2:
                    self.stdev.__setitem__(k,m[k][1])
                if p >= 3:
                    self.lower.__setitem__(k,m[k][2])
                if p >= 4:
                    self.upper.__setitem__(k,m[k][3])

        except ImportError:
            raise ImportError("Need astropy module for this")

    def as_table(self):
        """
        generates a astropy Table
        :return:
        """
        t1 = Table(self, names=self.names)

        if self.stdev is not None:
            t1.add_row(self.stdev)
        if self.lower is not None and self.upper is not None:
            t1.add_row(self.lower)
            t1.add_row(self.upper)

        return t1

    def as_vector(self):
        """
        generates a vector
        :return: ndarray
        """
        vector = self.as_table()[0]
        return numpy.array(vector.as_void().tolist())

    #Hidden Extentions
    def set_v22(self, v22):
        #@fixme: can the be made into a new Parameter property?
        self._v22 = v22

    def get_v22(self):
        return self._v22

    def del_v22(self):
        del self._v22

    # class property([fget[, fset[, fdel[, doc]]]])
    v22 = property(get_v22, set_v22,  del_v22)

    #Hidden Extentions
    def set_dvdx(self, dvdx):
        #@fixme: can the be made into a new Parameter property?
        self._dvdx = dvdx

    def get_dvdx(self):
        return self._dvdx

    def del_dvdx(self):
        del self._dvdx

    # class property([fget[, fset[, fdel[, doc]]]])
    dvdx = property(get_dvdx, set_dvdx,  del_dvdx)


    ## MAGIC METHODS
    def __getitem__(self, key):
        """
        Support for dictionary-like accessors, like x = gp['x'].
        This has a (tiny) performance cost.
        """
        if isinstance(key, str):
            try:
                return self[self.names.index(key)]
            except ValueError:
                raise ValueError("Property '%s' is not available. Use one of %s" % (key, self.names))
        else:
            return super(GalaxyParameters, self).__getitem__(key)

    def __setitem__(self, key, value):
        """
        Support for dictionary-like mutators, like gp['x'] = x
        This has a (tiny) performance cost.
        """
        if isinstance(key, str):
            try:
                return super(GalaxyParameters, self).__setitem__(self.names.index(key), value)
            except ValueError:
                raise ValueError("Property '%s' is not available. Use one of %s" % (key, self.names))
        else:
            return super(GalaxyParameters, self).__setitem__(key, value)

    def __str__(self):
        return self.short_info()

    def __repr__(self):
        return self.long_info()

    def __unit__(self, key):
        """
        :return: shortname
        """
        if isinstance(key, str):
            try:
                return  vars(GalaxyParameters)[key].unit
            except:
                raise ValueError("Property '%s' is not available. Use one of %s" % (key, self.names))

    def unit_dict(self):
        """
         :return:  dict of short names for GalaxyParameters "
        """
        return dict([(n,vars(GalaxyParameters)[n].unit) for n in self.names])

    def __shortname__(self, key):
        """
        :return: shortname
        """
        if isinstance(key, str):
            try:
                return  vars(GalaxyParameters)[key].short
            except ValueError:
                raise ValueError("Property '%s' is not available. Use one of %s" % (key, self.names))

    def short_dict(self):
        """
         :return:  dict of short names for GalaxyParameters "
        """
        return dict([(n,vars(GalaxyParameters)[n].short) for n in self.names])

    ## STRING CASTING

    def short_info(self):
        """
        Casts to single-line string.
        This is called by ``print()``.

        Looks like this :
        x=0.00 y=1.00 z=2.000000 flux=3.00e+00 r½=4.00 incl=5.00 PA=6.00 rv=7.00 Vmax=8.00 s0=9.00

        :rtype: string
        """
        s = ''
        for name in GalaxyParameters.names:
            attribute = vars(GalaxyParameters)[name]
            s += ("{short}={value:%s} " % attribute.format).format(
                name=name,
                short=attribute.short,
                value=self.__getattribute__(name)
            )
        return s

    def colored_info(self, warn):
        """
        Casts to colored single-line string when GalaxyParameters `warn` is 1.
        The parameter `warn` is a GalaxyParameters object too, but it's values
        should be either 0 (no warning) or 1 (warning).

        Looks just like short info, but with additional ANSI characters for color
        where `warn` flag is 1.

        :rtype: string
        """
        s = ''
        for name in GalaxyParameters.names:
            attribute = vars(GalaxyParameters)[name]
            s += attribute.short + '='
            s += self._wrap_with_warn("{value:%s}" % attribute.format, warn.__getattribute__(name)).format(
                name=name,
                short=attribute.short,
                value=self.__getattribute__(name)
            )
            s += ' '
        return s

    def long_info(self, error_as_percentage=False):
        """
        Casts to multi-line string.
        This is called by ``repr()``.

        error_as_percentage: bool
            When true, will print the stdev margin as a percentage of the value.

        :rtype: string
        """
        if self.stdev is not None:
            s = "\n Galaxy Parameters : value (± stdev) [units]"
        else:
            s = "\n Galaxy Parameters : value [units]"

        if self.lower is not None and self.upper is not None:
            s += "\t [Confidence Interval]"
        s += '\n'

        for name in GalaxyParameters.names:
            prop = vars(GalaxyParameters)[name]
            value = self.__getattribute__(prop.name)
            # The name of the property, and its value
            s += ('    {name}: {value:%s}' % prop.format).format(
                name=prop.name,
                value=value
            )
            # The optional stdev margin
            if getattr(self, 'stdev', None) is not None:
                error_value = getattr(self.stdev, prop.name, None)
                if error_as_percentage:
                    error_value = 100 * error_value / value
                if not isnan(error_value):
                    s += (' ± {error_value:%s}' % prop.format).format(
                        error_value=error_value
                    )
                    if error_as_percentage:
                        s += '%'
            # And, finally, the optional unit
            if prop.unit is not None:
                s += " ({unit})".format(unit=prop.unit)
            if self.lower is not None and self.upper is not None:
                lower = getattr(self.lower, prop.name, None)
                upper = getattr(self.upper, prop.name, None)
                s += '\t CI '+str(self.ICpercentile)+'%:'
                s += (' [{lower:%s},{upper:%s}]  ' % (prop.format,prop.format)).format(
                    lower=lower,
                    upper=upper
                )

            s += '\n'

        return s

    def structured_info(self):
        """
        Casts to multiline parsable ``Table`` string.
        Use the ``ascii.fixed_width`` reader to easily retrieve the data.
        This method is used to store the parameters into the `<prefix>_galaxy_parameters.dat`.

        See the tutorials for an example of how to retrieve the data.
        """

        out = StringStdOut()

        t1 = self.as_table()
        t1.write(out,format='ascii.fixed_width')

        return str(out.content)

    @staticmethod
    def _wrap_with_warn(string, condition):
        """
        Will return string wrapped by WARN color escape sequence if condition is not zero.
        """
        if condition != 0 and not isnan(condition):
            return AnsiColors.WARNING + string + AnsiColors.ENDC
        else:
            return string


class GalaxyParametersError(GalaxyParameters):
    """
    Error margin for GalaxyParameters.
    We could just use another GalaxyParameters object instead of extending it,
    but this makes sure that stdev recursion never happens,
    and it also customizes the casting to string.
    """

    def get_error(self):
        return None

    def set_error(self, value):
        pass

    stdev = property(get_error, set_error, doc="""
    This property is useless.
    Error margins have no stdev margins.
    They don't, do they ?
    """)

    @staticmethod
    def from_ndarray(a):
        """
        Factory to easily create a GalaxyParametersError object from an ordered
        ndarray whose elements are in the order of `GalaxyParameters.names`.

        Use like this : ::

            gp = GalaxyParametersError.from_ndarray(my_ndarray_of_data)

        :rtype: GalaxyParametersError
        """
        required_number_of_values = len(GalaxyParameters.names)
        if numpy.size(a, 0) < required_number_of_values:
            raise ValueError("Provide an array of at least %d floats (nan is allowed)" % required_number_of_values)
        return GalaxyParametersError(*a)
