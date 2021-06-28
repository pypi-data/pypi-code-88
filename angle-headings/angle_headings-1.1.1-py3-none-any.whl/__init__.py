"""A Python class for representing and performing calculations with angles.

This module defines a lightweight class:
    angle_headings.Angle
for representing angles. It is designed to make performing common operations
with angles easy, with a focus on applications involving headings in the 2D
plane.

An Angle object has three public attributes:
    measure (float) -- the numerical measure of the angle, used for most
        calculations
    mod (float) -- the measure of one full revolution (e.g. 2pi for radians,
        360 for degrees)
    unit (str) -- string version of the angle's unit

All Angle measures are normalized to be between -1/2 (exclusive) and 1/2
(inclusive) of a full revolution, with negative measures indicating clockwise
rotation and positive indicating counterclockwise.

Binary operations that are defined between Angle objects use the first
object's unit. Most (Angle, Angle) binary operators have an equivalent
(Angle, float) version that performs the same operation, but treating the
given float as the measure of a second angle that matches the first angle's
unit.

The following is a summary of the major public Angle methods.
    Angle([measure[, mod]]) -- constructor can set the initial measure and mod
        (default 0.0 and 2pi, respectively)
    convert([mod]) -- returns the measure of the Angle converted to a
        different unit
    reldiff(other) -- computes a normalized relative difference between two
        Angles' measures, scaled so that equal measures are 0.0 and
        diametrically opposed measures are 1.0

The following operators are defined for Angle objects, and perform their usual
float operations on the Angle's measure, returning a numerical value of the
appropriate class.
    abs(A) (Angle) -- absolute value of measure
    int(A) (Angle) -- truncates measure to int
    float(A) (Angle) -- returns measure
    round(A) (Angle) -- rounds measure to nearest int

The following operators are defined for Angle objects, and combine the Angle
with either another Angle or a float. In all cases the expected operation is
performed on the Angles' measures (as floats), and a new Angle object (whose
unit matches the first Angle) is returned, normalized to be between -1/2
(exclusive) and 1/2 (inclusive) of a full revolution.
    +A (Angle) -- exact copy of this Angle
    -A (Angle) -- negates measure
    A + B (Angle, Angle) -- adds measures
    A + b (Angle, float)
    A - B (Angle, Angle) -- subtracts measures
    A - b (Angle, float)
    A * b (Angle, float) -- multiplies measure by a scalar
    A / b (Angle, float) -- divides measure by a scalar
    A // b (Angle, float) -- floor divides measure by a scalar
    A ** b (Angle, float) -- raises measure to a scalar power

The following comparison operators are defined for Angle objects, and perform
the expected comparison with the Angle's measure and another Angle's measure
or a float. Measures are considered to be equal if their normalized values are
equal after conversion to a common unit. Note that, since measures are
maintained as floats which occasionally require normalization, it is not
recommended to to directly test equality between two Angles (the
Angle.reldiff() method should be used instead).
    A == B (Angle, Angle) -- equal (after conversion to the same unit)
    A == b (Angle, float)
    A != B (Angle, Angle) -- not equal
    A != b (Angle, float)

The following comparison operators are defined for Angle objects, and compare
the Angle to either another Angle or a float. In all cases, the comparison's
result is based on the smallest angle between the two arguments. If the
smallest angle between A and B places A counterclockwise relative to B, then
we say that A > B, and if it places A clockwise relative to B, then we say
that A < B. By convention, if A and B are diametrically opposed, we say that
A > B if A is the caller and B > A if B is the caller. In all cases the
comparison is performed on the Angles' measures (as floats), after both have
been converted to the first argument's unit.
    A > B (Angle, Angle) -- smallest A--B angle is CW
    A > b (Angle, float)
    A >= B (Angle, Angle) -- A > B or A == B
    A >= b (Angle, float)
    A < B (Angle, Angle) -- smallest A--B angle is CCW
    A < b (Angle, float)
    A <= B (Angle, Angle) -- A < B or A == B
    A <= b (Angle, float)
"""

from ._version import __author__, __version__
from .angles import Angle
