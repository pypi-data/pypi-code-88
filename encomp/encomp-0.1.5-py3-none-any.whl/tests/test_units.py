import pytest
from pytest import approx

from encomp.units import Q, wraps
from encomp.utypes import *


def test_Q():

    # test that Quantity objects can be constructed
    Q(1, 'dimensionless')
    Q(1, 'kg')
    Q(1, 'bar')
    Q(1, 'h')
    Q(1, 'newton')
    Q(1, 'cSt')

    # input Quantity as unit
    Q(1, Q(2, 'bar'))

    # input Quantity as val
    Q(Q(2, 'bar'), 'kPa')

    # input Quantity as both val and unit
    Q(Q(2, 'bar'), Q(3, 'kPa'))
    Q(Q(2, 'bar'), Q(3, 'mmHg'))

    # check that the dimensionality constraints work
    Q[Length](1, 'm')
    Q[Pressure](1, 'kPa')
    Q[Temperature](1, '°C')

    # the dimensionalities can also be specified as strings
    Q['Temperature'](1, '°C')

    P = Q(1, 'bar')
    # this Quantity must have the same dimensionality as P
    Q[P](2, 'kPa')

    with pytest.raises(Exception):
        Q[Temperature](1, 'kg')
        Q[Pressure](1, 'meter')
        Q[Mass](1, P)

    # in-place conversion
    # NOTE: don't use this for objects that are passed in by the user
    P3 = Q(1, 'bar')
    P3.ito('kPa')
    P3.ito(Q(123123, 'kPa'))

    assert P3.m == approx(100, rel=1e-12)

    a = Q([1, 2, 3], 'bar')
    a.ito('kPa')

    # conversion to new object
    P4 = Q(1, 'bar')
    P4_b = P4.to('kPa')
    P4_b = P4.to(Q(123123, 'kPa'))

    assert P4_b.m == approx(100, rel=1e-12)

    # check that nested Quantity objects can be used as input
    # only the first value is used as magnitude, the other Quantity
    # objects are only used to determine unit
    P2 = Q(Q(2, 'feet_water'), Q(321321, 'kPa')).to(Q(123123, 'feet_water'))

    # floating point math might make this off at the N:th decimal
    assert P2.m == approx(2, rel=1e-12)
    assert isinstance(P2, Q['Pressure'])

    with pytest.raises(Exception):

        # incorrect dimensionalities should raise Exception
        Q(Q(2, 'feet_water'), Q(321321, 'kg')).to(Q(123123, 'feet_water'))

    # the UnitsContainer objects can be used to construct new dimensionalities
    Q[Length * Length * Length / Temperature](1, 'm³/K')

    with pytest.raises(Exception):
        Q[Pressure / Area](1, 'bar/m')

    # percent or %
    Q(1.124124e-3, '').to('%').to('percent')


def test_wraps():

    # @wraps(ret, args, strict=True|False) is a convenience
    # decorator for making the input/output of a function into Quantity
    # however, it does not enforce the return value

    @wraps('kg', ('m', 'kg'), strict=True)
    def func(a, b):

        # this is incorrect, cannot add 1 to a dimensional Quantity
        return a * b**2 + 1

    assert isinstance(func(Q(1, 'yd'), Q(20, 'lbs')), Q['Mass'])

    assert Q(1, 'bar').check(Pressure)
