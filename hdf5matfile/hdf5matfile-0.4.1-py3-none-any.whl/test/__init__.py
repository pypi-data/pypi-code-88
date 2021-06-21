import importlib.resources

import numpy as np

from hdf5matfile import Hdf5Matfile, load_hdf5mat


def resource_path(name):
    return importlib.resources.path(__name__, name)


def get_var_loader(resource):
    def load_var(var):
        with resource_path(resource) as p:
            return load_hdf5mat(p, var)

    return load_var


def get_matfile(resource, squeeze=False):
    with resource_path(resource) as p:
        return Hdf5Matfile(p, squeeze)


def assert_array_equal(a: np.ndarray, b: np.ndarray):
    """Assert that two arrays have the same values, dtype, and shape."""
    assert a.dtype == b.dtype
    np.testing.assert_array_equal(a, b)


def assert_array_close(actual: np.ndarray,
                       desired: np.ndarray,
                       rtol: float = 1e-7,
                       atol: float = 0):
    """Assert that two arrays have the same values (within tolerance),
    dtype, and shape.
    """
    assert desired.dtype == actual.dtype
    assert desired.shape == actual.shape
    np.testing.assert_allclose(actual, desired, rtol, atol)
