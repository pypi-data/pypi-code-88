import operator

import torch

"""
Tiny tests
"""


def test(a, b, cmp, cname=None):
    """
    Test main
    """
    if cname is None:
        cname = cmp.__name__
        assert cmp(a, b), f"{cname}: \n{a}\n{b}"


def test_eq(a, b):  #%t
    """
    Test if equal

    """
    test(a, b, operator.eq, "==")


def near(a, b):
    return torch.allclose(a, b, rtol=1e-3, atol=1e-5)


def test_near(a, b):  #%t
    """
    Test if two values are near each other

    """
    test(a, b, near)
