"""Defines this package's main Angle class."""

from ._version import __author__, __version__

import math

class Angle:
    """A class for representing and performing calculations with angles.

    This is a lightweight data structure for representing angles. It is
    designed to make performing common operations with angles easy, with a
    focus on applications involving headings in the 2D plane.

    An Angle object has three public attributes:
        measure (float) -- the numerical measure of the angle, used for most
            calculations
        mod (float) -- the measure of one full revolution (e.g. 2pi for
            radians, 360 for degrees)
        unit (str) -- string version of the angle's unit

    All Angle measures are normalized to be between -1/2 (exclusive) and 1/2
    (inclusive) of a full revolution, with negative measures indicating
    clockwise rotation and positive indicating counterclockwise.

    Binary operations that are defined between Angle objects use the first
    object's unit. Most (Angle, Angle) binary operators have an equivalent
    (Angle, float) version that performs the same operation, but treating the
    given float as the measure of a second angle that matches the first
    angle's unit.
    """

    # Static attributes for accepted unit names
    _rad_str = {"radians", "radian", "rad", "r"}
    _deg_str = {"degrees", "degree", "deg", "d"}
    _grad_str = {"gradians", "gradian", "grad", "g"}

    #=========================================================================
    # Technical Methods
    #=========================================================================

    def __init__(self, measure=0.0, mod="radians"):
        """Angle([measure[, mod]]) -> Angle
        Angle constructor.

        Keyword arguments:
        measure (float) [0.0] -- initial angle measure
        mod (str or float) ["radians"] -- angle unit, or measure of one full
            revolution

        The optional "mod" argument is used to specify the unit of angle
        measure. If given as a number, this number is treated as the measure
        of one full revolution. If given as a string, it uses a standardized
        unit of measure. The following strings are recognized:
            radians, radian, rad, r -- radians (2pi)
            degrees, degree, deg, d -- degrees (360)
            gradians, gradian, grad, g -- gradians (400)
        """

        # Parse unit arguments
        self._set_mod(mod)

        # Set initial measure (automatically normalizes self)
        self.measure = float(measure) # current angle measure

    #-------------------------------------------------------------------------

    def __str__(self):
        """str(Angle) -> str
        Angle string conversion.

        Returns the measure of the angle as a string, along with an
        abbreviation of the angle unit.
        """

        return str(self.measure) + " " + self.unit

    #-------------------------------------------------------------------------

    def _set_mod(self, mod):
        """Angle._set_mod(mod) -> None
        Sets mod and unit based on a given mod input.

        Positional arguments:
        mod (str or float) -- angle unit, or measure of one full revolution

        This is a private method called during the Angle's initialization, or
        when its mod value is reset. It includes a procedure for parsing the
        input (which can have several different types) and setting the unit
        string.
        """

        # Initialize mod and unit
        self.mod = 0.0 # full revolution measure
        self.unit = "rad" # name of unit for string output

        # Attempt to parse string mod argument
        if isinstance(mod, str) == True:
            # Search through recognized words
            if mod in Angle._rad_str:
                self.mod = 2*math.pi
                self.unit = "rad"
            elif mod in Angle._deg_str:
                self.mod = 360.0
                self.unit = "deg"
            elif mod in Angle._grad_str:
                self.mod = 400.0
                self.unit = "grad"
            else:
                # If unrecognized, raise a value error
                raise ValueError("unrecognized unit name string")
        else:
            # Otherwise attempt to parse numerical mod argument
            self.mod = abs(float(mod))
            self.unit = "/ " + str(self.mod)

            # Raise a value error in case of nonpositive mod
            if self.mod <= 0.0:
                raise ValueError("measure of full revolution must be positive")

        # Rename unit for recognized moduli
        if mod == 2*math.pi:
            self.unit = "rad"
        elif mod == 360.0:
            self.unit = "deg"
        elif mod == 400.0:
            self.unit = "grad"

    #-------------------------------------------------------------------------

    def _get_other_measure(self, other):
        """Angle._get_other_measure(other) -> float
        Gets a measure argument as a float.

        Positional arguments:
        other (Angle or float) -- other Angle or float to be treated as a
            measure

        This is a private method used in some operations that can accept
        either another Angle object or a float. If given an Angle, this
        method returns that Angle's measure converted to this Angle's unit.
        If given a float, it simply returns the float directly.
        """

        # Determine class of argument
        if isinstance(other, Angle) == True:
            # If another angle, convert the other argument
            m = other.convert(self.mod)
        else:
            # Otherwise attempt to parse second argument as a float
            m = float(other)

        # Return the float
        return m

    #-------------------------------------------------------------------------

    @property
    def measure(self):
        """Angle.measure() -> float
        Retrieves normalized angle measure.
        """

        return self._measure

    #-------------------------------------------------------------------------

    @measure.setter
    def measure(self, value):
        """Angle.measure(value) -> None
        Updates the angle measure, then automatically normalizes.

        Positional arguments:
        value (float) -- new angle measure
        """

        # Set private measure variable
        self._measure = value

        # Normalize if needed
        if self._measure < -self.mod/2 or self._measure > self.mod/2:
            self._measure = (((self._measure + (self.mod/2)) % self.mod)
                             - (self.mod/2))
        if (self._measure == -self.mod/2):
            self._measure = -self._measure

    #=========================================================================
    # Custom Methods
    #=========================================================================

    def convert(self, new_mod="radians"):
        """Angle.convert([mod]) -> float
        Returns the angle measure converted into a different unit.

        Positional arguments:
        mod (str or float) ["radians"] -- angle unit, or measure of one full
            revolution

        The resulting measure is between (-1/2,1/2] full revolutions (relative
        to the given unit).
        """

        # Attempt to parse string mod argument
        if isinstance(new_mod, str) == True:
            # Search through recognized words
            if new_mod in Angle._rad_str:
                new_mod = 2*math.pi
            elif new_mod in Angle._deg_str:
                new_mod = 360.0
            elif new_mod in Angle._grad_str:
                new_mod = 400.0
            else:
                # If unrecognized, raise a value error
                raise ValueError("unrecognized unit name string")
        else:
            # Otherwise attempt to parse numerical mod argument
            new_mod = abs(float(new_mod))

        # Convert measure as a fraction of a complete revolution
        return ((self._measure/self.mod) % 1.0)*new_mod

    #-------------------------------------------------------------------------

    def reldiff(self, other):
        """Angle.reldiff(other) -> float
        Calculates the relative difference between two Angles' measures.

        Positional arguments:
        other (Angle or float) -- measure to be compared to this Angle's
            measure

        If the argument is an Angle, it is first converted to this Angle's
        unit. If the second argument is a float, it is assumed to already
        match this Angle's unit.

        The returned value is the relative difference between the two
        measures, scaled so that 0.0 represents equal measures and 1.0
        represents diametrically opposed measures.
        """

        # Calculate absolute difference between the measures
        diff = abs(self - other)

        # Return normalized difference value
        return diff/(self.mod/2)

    #=========================================================================
    # Overloaded Numerical Operators
    #=========================================================================

    def __abs__(self):
        """abs(Angle) -> float
        Returns the absolute value of the Angle's measure.
        """

        return abs(self.measure)

    #-------------------------------------------------------------------------

    def __int__(self):
        """int(Angle) -> int
        Returns the measure of the Angle, cast as an integer.
        """

        return int(self.measure)

    #-------------------------------------------------------------------------

    def __float__(self):
        """float(Angle) -> float
        Returns the measure of the Angle, cast as a float.
        """

        return float(self.measure)

    #-------------------------------------------------------------------------

    def __round__(self):
        """round(Angle) -> int
        Returns the measure of the Angle, rounded to the nearest integer.
        """

        return round(self.measure)

    #=========================================================================
    # Overloaded Operators
    #=========================================================================

    def __pos__(self):
        """+Angle -> Angle
        Returns an exact copy of this Angle.

        The returned Angle has this Angle's mod and measure, automatically
        normalized to lie within (-1/2,1/2] full revolutions.
        """

        return Angle(self.measure, self.mod)

    #-------------------------------------------------------------------------

    def __neg__(self):
        """-Angle -> Angle
        Returns a new Angle with the negative of this Angle's measure.

        The returned Angle has this Angle's mod, and the negative of its
        measure, automatically normalized to lie within (-1/2,1/2] full
        revolutions.
        """

        return Angle(-self.measure, self.mod)

    #-------------------------------------------------------------------------

    def __add__(self, other):
        """Angle + Angle -> Angle
        Angle + float -> Angle
        Returns a new Angle with the sum of two angles' measures.

        Positional arguments:
        other (Angle or float) -- measure to be added to this Angle's measure

        This is a method of the operator's first argument. If the second
        argument is an Angle, it is first converted to this Angle's unit. If
        the second argument is a float, it is assumed to already match this
        Angle's unit.

        The returned Angle has this Angle's mod, and its measure is
        automatically normalized to lie within (-1/2,1/2] full revolutions.
        """

        # Get second argument as a float
        theta = self._get_other_measure(other)

        # Add to this Angle's measure and return result
        return Angle(self.measure + theta, self.mod)

    #-------------------------------------------------------------------------

    def __sub__(self, other):
        """Angle - Angle -> Angle
        Angle - float -> Angle
        Returns a new Angle with the difference between two angles' measures.

        Positional arguments:
        other (Angle or float) -- measure to be subtracted from this Angle's
            measure

        This is a method of the operator's first argument. If the second
        argument is an Angle, it is first converted to this Angle's unit. If
        the second argument is a float, it is assumed to already match this
        Angle's unit.

        The returned Angle has this Angle's mod, and its measure is
        automatically normalized to lie within (-1/2,1/2] full revolutions.
        """

        # Get second argument as a float
        theta = self._get_other_measure(other)

        # Subtract from this Angle's measure and return result
        return Angle(self.measure - theta, self.mod)

    #-------------------------------------------------------------------------

    def __mul__(self, other):
        """Angle * float -> Angle
        Returns a new Angle with its measure multiplied by a given float.

        Positional arguments:
        other (float) -- factor by which to multiply this Angle's measure

        This is a method of the operator's first argument. The second argument
        is a float, it is assumed to already match this Angle's unit.

        The returned Angle has this Angle's mod, and its measure is
        automatically normalized to lie within (-1/2,1/2] full revolutions.
        """

        # Multiply this Angle's measure and return result
        return Angle(self.measure*other, self.mod)

    #-------------------------------------------------------------------------

    def __div__(self, other):
        """Angle / float -> Angle
        Returns a new Angle with its measure divided by a given float.

        Positional arguments:
        other (float) -- factor by which to divide this Angle's measure

        This is a method of the operator's first argument. The second argument
        is a float, it is assumed to already match this Angle's unit.

        The returned Angle has this Angle's mod, and its measure is
        automatically normalized to lie within (-1/2,1/2] full revolutions.
        """

        # Divide this Angle's measure and return result
        return Angle(self.measure/other, self.mod)

    #-------------------------------------------------------------------------

    def __floordiv__(self, other):
        """Angle // float -> Angle
        Returns a new Angle with its measure (floor) divided by a given float.

        Positional arguments:
        other (float) -- factor by which to (floor) divide this Angle's
            measure

        This is a method of the operator's first argument. The second argument
        is a float, it is assumed to already match this Angle's unit.

        The returned Angle has this Angle's mod, and its measure is
        automatically normalized to lie within (-1/2,1/2] full revolutions.
        """

        # Floor divide this Angle's measure and return result
        return Angle(self.measure//other, self.mod)

    #-------------------------------------------------------------------------

    def __pow__(self, other):
        """Angle ** float -> Angle
        Returns a new Angle with its measure raised to a given float power.

        Positional arguments:
        other (float) -- power to which to raise this Angle's measure

        This is a method of the operator's first argument. The second argument
        is a float, it is assumed to already match this Angle's unit.

        The returned Angle has this Angle's mod, and its measure is
        automatically normalized to lie within (-1/2,1/2] full revolutions.
        """

        # Exponentiate this Angle's measure and return result
        return Angle(self.measure**other, self.mod)

    #=========================================================================
    # Overloaded Equality Comparisons
    #=========================================================================

    def __eq__(self, other):
        """Angle == Angle -> bool
        Angle == float -> bool
        Determines whether two angles have the same measure.

        Positional arguments:
        other (Angle or float) -- measure to be compared to this Angle's
            measure

        This is a method of the operator's first argument. If the second
        argument is an Angle, it is first converted to this Angle's unit. If
        the second argument is a float, it is assumed to already match this
        Angle's unit.

        Note that, since Angle measures are maintained as floats which are
        occasionally converted, it is not recommended to use this method to
        test for measure equality. Instead, Angle.reldiff(Angle) should be
        used to determine whether the relative difference in the two Angles'
        measures is sufficiently small.
        """

        # Find the difference between the Angles
        delta = float(self - other)

        # Angles equal if difference is zero
        return delta == 0

    #-------------------------------------------------------------------------

    def __ne__(self, other):
        """Angle != Angle -> bool
        Angle != float -> bool
        Determines whether two angles have the different measures.

        Positional arguments:
        other (Angle or float) -- measure to be compared to this Angle's
            measure

        This is a method of the operator's first argument. If the second
        argument is an Angle, it is first converted to this Angle's unit. If
        the second argument is a float, it is assumed to already match this
        Angle's unit.

        Note that, since Angle measures are maintained as floats which are
        occasionally converted, it is not recommended to use this method to
        test for measure equality. Instead, Angle.reldiff(Angle) should be
        used to determine whether the relative difference in the two Angles'
        measures is sufficiently small.
        """

        # Negate equality definition
        return not (self == other)

    #=========================================================================
    # Overloaded Inequality Comparisons
    #=========================================================================

    def __gt__(self, other):
        """Angle > Angle -> bool
        Angle > float -> bool
        Determines the direction of the smallest angle between two Angles.

        Positional arguments:
        other (Angle or float) -- measure to be compared to this Angle's
            measure

        This is a method of the operator's first argument. If the second
        argument is an Angle, it is first converted to this Angle's unit. If
        the second argument is a float, it is assumed to already match this
        Angle's unit.

        The return value is based on the smallest angle between A and B, and
        is True if and only if the smallest angle between them places A
        counterclockwise relative to B.
        """

        # Find the difference between the Angles
        delta = float(self - other)

        # Determine output based on sign of difference
        return delta > 0

    #-------------------------------------------------------------------------

    def __lt__(self, other):
        """Angle < Angle -> bool
        Angle < float -> bool
        Determines the direction of the smallest angle between two Angles.

        Positional arguments:
        other (Angle or float) -- measure to be compared to this Angle's
            measure

        This is a method of the operator's first argument. If the second
        argument is an Angle, it is first converted to this Angle's unit. If
        the second argument is a float, it is assumed to already match this
        Angle's unit.

        The return value is based on the smallest angle between A and B, and
        is True if and only if the smallest angle between them places A
        clockwise relative to B.
        """

        # Find the difference between the Angles
        delta = float(self - other)

        # Determine output based on sign of difference
        return delta < 0

    #-------------------------------------------------------------------------

    def __ge__(self, other):
        """Angle >= Angle -> bool
        Angle >= float -> bool
        Determines the direction of the smallest angle between two Angles.

        Positional arguments:
        other (Angle or float) -- measure to be compared to this Angle's
            measure

        This is a method of the operator's first argument. If the second
        argument is an Angle, it is first converted to this Angle's unit. If
        the second argument is a float, it is assumed to already match this
        Angle's unit.

        The return value is based on the smallest angle between A and B, and
        is True if and only if the smallest angle between them places A
        counterclockwise relative to B (or if the measures are equal).
        """

        # Combine > operator and == operator
        return (self == other) or (self > other)

    #-------------------------------------------------------------------------

    def __le__(self, other):
        """Angle <= Angle -> bool
        Angle <= float -> bool
        Determines the direction of the smallest angle between two Angles.

        Positional arguments:
        other (Angle or float) -- measure to be compared to this Angle's
            measure

        This is a method of the operator's first argument. If the second
        argument is an Angle, it is first converted to this Angle's unit. If
        the second argument is a float, it is assumed to already match this
        Angle's unit.

        The return value is based on the smallest angle between A and B, and
        is True if and only if the smallest angle between them places A
        clockwise relative to B (or if the measures are equal).
        """

        # Combine < operator and == operator
        return (self == other) or (self < other)
