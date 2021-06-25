from typing import Generator

import numpy as np
import pytest
import scipy.ndimage as spnd
import skimage.transform as transform
from astropy.io import fits
from dkist_processing_common.models.fits_access import FitsAccessBase

from dkist_processing_math import affine_transform_arrays
from dkist_processing_math import average_numpy_arrays
from dkist_processing_math import bin_arrays
from dkist_processing_math import divide_arrays_by_array
from dkist_processing_math import divide_fits_access_by_array
from dkist_processing_math import do_hough
from dkist_processing_math import find_px_angles
from dkist_processing_math import make_binary
from dkist_processing_math import rotate_arrays_about_point
from dkist_processing_math import rotation_matrix
from dkist_processing_math import scale_matrix
from dkist_processing_math import shear_matrix
from dkist_processing_math import subtract_array_from_arrays
from dkist_processing_math import subtract_array_from_fits_access
from dkist_processing_math import translate_arrays
from dkist_processing_math import translation_matrix


rng = np.random.default_rng()


@pytest.fixture()
def numpy_arrays_wrong_shape():
    """
    Create an iterable of random arrays of differing sizes

    Returns
    -------
    List[np.ndarray]

    """
    arrays = [rng.standard_normal((10, 10)), rng.standard_normal((10, 15))]
    return arrays


@pytest.fixture()
def numpy_arrays():
    """
    Create an iterable of random 10 x 10 arrays

    Returns
    -------
    List[np.ndarray]

    """
    arrays = [rng.standard_normal((10, 10)), rng.standard_normal((10, 10))]
    return arrays


@pytest.fixture()
def numpy_array():
    """
    Create a single random 10 x 10 array

    Returns
    -------
    np.ndarray

    """
    array = rng.standard_normal((10, 10))
    return array


@pytest.fixture(params=["multiple", "single"])
def multiple_test_arrays(request, numpy_arrays):
    """
    Create an input test array or list of test arrays

    Parameters
    ----------
    request: Union['multiple, 'single']
        indicates whether to return a single array or an iterable of arrays
    numpy_arrays: List[np.ndarray]
        the arrays from which the return value is selected

    Returns
    -------
    Union[List[np.ndarray], np.ndarray]

    """
    if request.param == "multiple":
        return numpy_arrays
    else:
        return numpy_arrays[0]


@pytest.fixture(params=["multiple", "single"])
def multiple_test_fits_access(request, numpy_arrays):

    access_list = []
    for i, array in enumerate(numpy_arrays):
        hdu = fits.PrimaryHDU(data=array)
        hdu.header["TEST"] = i
        access_list.append(FitsAccessBase(hdu=hdu))
    if request.param == "multiple":
        return access_list
    return access_list[0]


@pytest.fixture()
def binned_array(numpy_array):
    """
    Create a binned array from numpy_array

    Parameters
    ----------
    numpy_array: np.ndarray
        The array to be binned

    Returns
    -------
    np.ndarray
        A 2x2 binned version of the input array

    """
    temp_array = np.zeros((2, 2), dtype=numpy_array.dtype)
    for row in range(temp_array.shape[1]):
        for column in range(temp_array.shape[0]):
            temp_array[column, row] = numpy_array[
                column * 5 : (column + 1) * 5, row * 5 : (row + 1) * 5
            ].mean()
    return temp_array


@pytest.fixture()
def binned_arrays(numpy_arrays):
    """
    Create a list of binned arrays from numpy_arrays

    Parameters
    ----------
    numpy_arrays: List[np.ndarray]
        A list of arrays to be binned

    Returns
    -------
    List[np.ndarray]
        A list of 2x2 binned versions of the input arrays

    """

    temp_arrays = np.zeros((2, 2, 2), dtype=numpy_arrays[0].dtype)
    for array, temp_array in zip(numpy_arrays, temp_arrays):
        for row in range(temp_array.shape[1]):
            for column in range(temp_array.shape[0]):
                temp_array[column, row] = array[
                    column * 5 : (column + 1) * 5, row * 5 : (row + 1) * 5
                ].mean()
    return temp_arrays


def test_average_numpy_arrays_wrong_shape(numpy_arrays_wrong_shape):
    """
    Given: an iterable of numpy arrays that are not all the same shape
    When: averaging arrays
    Then: an error is raised as the shapes are required to be the same
    """
    with pytest.raises(ValueError):
        average_numpy_arrays(numpy_arrays_wrong_shape)


def test_subtract_array_from_arrays_wrong_shape(numpy_arrays_wrong_shape, numpy_array):
    """
    Given: an iterable of numpy arrays that are not all the same shape
    When: subtracting arrays
    Then: an error is raised as the shapes are required to be the same
    """
    with pytest.raises(ValueError):
        list(subtract_array_from_arrays(numpy_arrays_wrong_shape, numpy_array))


def test_divide_arrays_by_array_wrong_shape(numpy_arrays_wrong_shape, numpy_array):
    """
    Given: an iterable of numpy arrays that are not all the same shape
    When: dividing arrays
    Then: an error is raised as the shapes are required to be the same
    """
    with pytest.raises(ValueError):
        list(divide_arrays_by_array(numpy_arrays_wrong_shape, numpy_array))


def test_average_numpy_arrays(multiple_test_arrays):
    """
    Given: an iterable of numpy arrays that are all the same shape
    When: calculating the average
    Then: a numpy array containing the average is returned
    """
    if isinstance(multiple_test_arrays, np.ndarray):
        desired_shape = multiple_test_arrays.shape
        desired_result = multiple_test_arrays
    else:
        desired_shape = multiple_test_arrays[0].shape
        desired_result = np.mean(np.array(multiple_test_arrays), axis=0)
    result = average_numpy_arrays(multiple_test_arrays)
    assert isinstance(result, np.ndarray)
    # Dividing an ndarray by an integer is a floating point division
    # and the result is always dtype=np.float64
    assert result.dtype == np.float64
    assert result.shape == desired_shape
    np.testing.assert_allclose(result, desired_result)


def test_average_numpy_arrays_empty_list(empty_list=[]):
    """
    Given: an empty iterable of numpy arrays
    When: calculating the average
    Then: an error is raised
    """
    with pytest.raises(ValueError):
        average_numpy_arrays(empty_list)


def test_subtract_array_from_arrays(multiple_test_arrays, numpy_array):
    """
    Given: an iterable of numpy arrays that are all the same shape
    When: subtracting a fixed array from each array in the iterable
    Then: an Generator of subtracted arrays is returned
    """
    if isinstance(multiple_test_arrays, np.ndarray):
        desired_shape = multiple_test_arrays.shape
        desired_result = [multiple_test_arrays - numpy_array]
    else:
        desired_shape = multiple_test_arrays[0].shape
        desired_result = multiple_test_arrays - numpy_array
    result = subtract_array_from_arrays(multiple_test_arrays, numpy_array)
    assert isinstance(result, Generator)
    for result_array, test_array in zip(result, desired_result):
        assert result_array.shape == desired_shape
        assert result_array.dtype == np.result_type(test_array)
        np.testing.assert_allclose(result_array, test_array)


def test_subtract_array_from_fits_access(multiple_test_fits_access, numpy_array):
    """
    Given: an iterable of or single FitsAccess object(s) with data
    When: subtracting an array from all input objects
    Then: a generator of FitsAccess objects is returned with correctly subtracted data
    """
    if isinstance(multiple_test_fits_access, FitsAccessBase):
        multiple_test_fits_access = [multiple_test_fits_access]

    desired_result = [i.data - numpy_array for i in multiple_test_fits_access]
    desired_header_val = [i.header["TEST"] for i in multiple_test_fits_access]

    result = subtract_array_from_fits_access(multiple_test_fits_access, numpy_array)
    assert isinstance(result, Generator)

    for result_obj, test_array, test_header_val in zip(result, desired_result, desired_header_val):
        assert result_obj.data.dtype == np.result_type(test_array)
        assert result_obj.header["TEST"] == test_header_val
        np.testing.assert_allclose(result_obj.data, test_array)


def test_divide_arrays_by_array(multiple_test_arrays, numpy_array):
    """
    Given: an iterable of numpy arrays that are all the same shape
    When: dividing each array in the iterable by a fixed array
    Then: an Generator of divided arrays is returned
    """
    if isinstance(multiple_test_arrays, np.ndarray):
        desired_shape = multiple_test_arrays.shape
        desired_result = [multiple_test_arrays / numpy_array]
    else:
        desired_shape = multiple_test_arrays[0].shape
        desired_result = multiple_test_arrays / numpy_array
    result = divide_arrays_by_array(multiple_test_arrays, numpy_array)
    assert isinstance(result, Generator)
    for result_array, test_array in zip(result, desired_result):
        assert result_array.shape == desired_shape
        assert result_array.dtype == np.result_type(test_array)
        np.testing.assert_allclose(result_array, test_array)


def test_divide_fits_access_by_array(multiple_test_fits_access, numpy_array):
    """
    Given: an iterable of or single FitsAccess object(s) with data
    When: dividing an array from all input objects
    Then: a generator of FitsAccess objects is returned with correctly subtracted data
    """
    if isinstance(multiple_test_fits_access, FitsAccessBase):
        multiple_test_fits_access = [multiple_test_fits_access]

    desired_result = [i.data / numpy_array for i in multiple_test_fits_access]
    desired_header_val = [i.header["TEST"] for i in multiple_test_fits_access]

    result = divide_fits_access_by_array(multiple_test_fits_access, numpy_array)
    assert isinstance(result, Generator)

    for result_obj, test_array, test_header_val in zip(result, desired_result, desired_header_val):
        assert result_obj.data.dtype == np.result_type(test_array)
        assert result_obj.header["TEST"] == test_header_val
        np.testing.assert_allclose(result_obj.data, test_array)


def test_bin_arrays(numpy_arrays, binned_arrays):
    """
    Given: an iterable of numpy_arrays
    When: binning an iterable of numpy_arrays
    Then: an Iterator of binned versions of the input arrays is returned
    """
    results = bin_arrays(numpy_arrays, (5, 5))
    for result, binned_array in zip(results, binned_arrays):
        np.testing.assert_allclose(result, binned_array)


def test_bin_arrays_single_array(numpy_array, binned_array):
    """
    Given: an single numpy_array
    When: binning an iterable of numpy_arrays
    Then: an Iterator containing the binned version of the input arrays is returned
    """
    result = next(bin_arrays(numpy_array, (5, 5)))
    np.testing.assert_allclose(result, binned_array)


def test_bin_arrays_bad_bin_factor(numpy_array):
    """
    Given: a single numpy array
    When: binning an array using a bad binning factor
    Then: an error is raised
    """
    with pytest.raises(ValueError):
        next(bin_arrays(numpy_array, (3, 3)))


def test_affine_transform_specify_matrix(numpy_array):
    """
    Given: a numpy_array
    When: applying the affine transform and specifying the full transformation matrix
    Then: an Iterator containing the transformed array is returned
    """
    angle = np.radians(90)
    # Create the Affine transform for the rotation
    rotation = transform.AffineTransform(rotation=angle)
    # Offset to the center of the array for the rotation
    p = np.array([4.5, 4.5])
    # Create the Affine transform for the translation
    trans = transform.AffineTransform(translation=p)
    # Create the composite transform matrix for the rotation about the center
    tform = trans.params @ rotation.params @ np.linalg.inv(trans.params)
    # Perform the transformation
    result = affine_transform_arrays(numpy_array, matrix=tform)
    # Compare against the same rotation computed with a different method.
    np.testing.assert_allclose(next(result), transform.rotate(numpy_array, -90, center=(4.5, 4.5)))


def test_affine_transform_specify_rotate(numpy_array):
    """
    Given: a numpy_array
    When: applying the affine transform and specifying a rotation angle and rotation point
    Then: an Iterator containing the rotated array is returned
    """
    angle = np.radians(90)
    rotation = transform.AffineTransform(rotation=angle)
    # Offset to the center of the array for the rotation
    p = np.array([4.5, 4.5, 0])
    # Transform the offset to rotated space
    o = p - np.dot(rotation.params, p)
    result = affine_transform_arrays(numpy_array, rotation=np.radians(90), translation=o[0:2])
    np.testing.assert_allclose(next(result), spnd.rotate(numpy_array, -90))


def test_affine_transform_specify_scale_x(numpy_array):
    """
    Given: a numpy_array
    When: applying the affine transform and specifying a scale factor for the X axis only
    Then: an Iterator containing the array scaled along the X axis is returned
    """

    num_rows = numpy_array.shape[0]
    num_cols = numpy_array.shape[1]
    desired_output = np.zeros_like(numpy_array)
    desired_output[0:num_rows, 0 : num_cols // 2] = numpy_array[0:num_rows, 0:num_cols:2]
    result = affine_transform_arrays(numpy_array, scale=(0.5, 1.0))
    np.testing.assert_allclose(next(result), desired_output)


def test_affine_transform_specify_scale_y(numpy_array):
    """
    Given: a numpy_array
    When: applying the affine transform and specifying a scale factor for the Y axis only
    Then: an Iterator containing the array scaled along the Y axis is returned
    """
    num_rows = numpy_array.shape[0]
    num_cols = numpy_array.shape[1]
    desired_output = np.zeros_like(numpy_array)
    desired_output[0 : num_rows // 2, 0:num_cols] = numpy_array[0:num_rows:2, 0:num_cols]
    result = affine_transform_arrays(numpy_array, scale=(1.0, 0.5))
    np.testing.assert_allclose(next(result), desired_output)


def test_affine_transform_specify_scale_both(numpy_array):
    """
    Given: a numpy_array
    When: applying the affine transform and specifying a scale factor for each axis
    Then: an Iterator containing the array scaled separately along each axis is returned
    """
    tform = transform.SimilarityTransform(scale=0.5)
    desired_output = transform.warp(numpy_array, tform.inverse)
    result = affine_transform_arrays(numpy_array, scale=(0.5, 0.5))
    np.testing.assert_allclose(next(result), desired_output)


def test_affine_transform_specify_scale_scalar(numpy_array):
    """
    Given: a numpy_array
    When: applying the affine transform and specifying a scalar scale factor to be applied to both axes
    Then: an Iterator containing the array scaled identically on each axis is returned
    """
    tform = transform.SimilarityTransform(scale=0.5)
    desired_output = transform.warp(numpy_array, tform.inverse)
    result = affine_transform_arrays(numpy_array, scale=0.5)
    np.testing.assert_allclose(next(result), desired_output)


def test_affine_transform_specify_shear(numpy_array):
    """
    Given: a numpy_array
    When: applying the affine transform and specifying a shear angle
    Then: an Iterator containing the sheared array is returned
    """
    shear_mat = np.array([[1, 0.1, 0], [0.2, 1, 0], [0, 0, 1]])
    shear_mat_inv = np.linalg.inv(shear_mat)
    desired_output = transform.warp(numpy_array, shear_mat_inv)
    result = affine_transform_arrays(numpy_array, shear=(0.1, 0.2))
    np.testing.assert_allclose(next(result), desired_output)


def test_affine_transform_specify_translate(numpy_array):
    """
    Given: a numpy_array
    When: applying the affine transform and specifying a translation vector
    Then: an Iterator containing the translated array is returned
    """
    result = affine_transform_arrays(numpy_array, translation=(2, 5))
    desired_output = spnd.shift(numpy_array, (5, 2))
    np.testing.assert_allclose(next(result), desired_output)


def test_affine_transform_all_params_none(numpy_array):
    """
    Given: a numpy_array
    When: applying the affine transform and specifying no parameters
    Then: an error is raised
    """
    with pytest.raises(ValueError):
        affine_transform_arrays(numpy_array)


def test_affine_transform_matrix_and_one_param(numpy_array):
    """
    Given: a numpy_array
    When: applying the affine transform and specifying both a full matrix and one or more transform parameters
    Then: an error is raised
    """
    with pytest.raises(ValueError):
        affine_transform_arrays(numpy_array, matrix=np.ones((2, 2)), shear=0.1)


def test_affine_transform_matrix_wrong_shape(numpy_array):
    """
    Given: a numpy_array
    When: applying the affine transform and specifying both a full matrix and one or more transform parameters
    Then: an error is raised
    """
    with pytest.raises(ValueError):
        affine_transform_arrays(numpy_array, matrix=np.ones((2, 2)))


def test_affine_transform_arrays(numpy_arrays):
    """
    Given: an iterable of numpy_arrays
    When: applying the affine transform
    Then: a Iterator containing the transformed arrays is returned
    """
    results = affine_transform_arrays(numpy_arrays, translation=(3, 7))
    desired_outputs = [spnd.shift(array, (7, 3)) for array in numpy_arrays]
    for result, desired_output in zip(results, desired_outputs):
        np.testing.assert_allclose(result, desired_output)


def test_affine_transform_arrays_single_array(numpy_array):
    """
    Given: a single numpy array
    When: applying the affine transform to an iterable of arrays
    Then: an Iterator containing the transformed array is returned
    """
    results = affine_transform_arrays(numpy_array, translation=(3, 2))
    result = next(results)
    desired_output = spnd.shift(numpy_array, (2, 3))
    np.testing.assert_allclose(result, desired_output)


def test_rotate_arrays_about_point(numpy_arrays):
    """
    Given: an iterable of numpy arrays
    When: rotating an iterable of arrays about a point
    Then: an Iterator containing the rotated arrays is returned
    """
    angle = -45
    p = np.array([5, 2])
    results = rotate_arrays_about_point(numpy_arrays, angle=np.radians(angle), point=p)
    desired_outputs = [transform.rotate(array, angle, center=p) for array in numpy_arrays]
    for result, desired_output in zip(results, desired_outputs):
        np.testing.assert_allclose(result, desired_output)


def test_rotate_arrays_about_point_single_array(numpy_array):
    """
    Given: a single numpy array
    When: rotating an iterable of arrays about a point
    Then: an Iterator containing the rotated array is returned
    """
    angle = -45
    p = np.array([5, 2])
    results = rotate_arrays_about_point(numpy_array, angle=np.radians(angle), point=p)
    result = next(results)
    desired_output = transform.rotate(numpy_array, angle, center=p)
    np.testing.assert_allclose(result, desired_output)


def test_translate_arrays(numpy_arrays):
    """
    Given: an iterable of numpy arrays
    When: translating an iterable of arrays by a vector
    Then: an Iterator containing the translated arrays is returned
    """
    results = translate_arrays(numpy_arrays, translation=(2, 5))
    desired_outputs = [spnd.shift(array, (5, 2)) for array in numpy_arrays]
    for result, desired_output in zip(results, desired_outputs):
        np.testing.assert_allclose(result, desired_output)


def test_translate_arrays_single_array(numpy_array):
    """
    Given: a single numpy array
    When: translating an iterable of arrays by a vector
    Then: an Iterator containing the translated array is returned
    """
    results = translate_arrays(numpy_array, translation=(2, 5))
    result = next(results)
    desired_output = spnd.shift(numpy_array, (5, 2))
    np.testing.assert_allclose(result, desired_output)


def test_scale_matrix(numpy_array):
    """
    Given: a single numpy array
    When: creating a scale matrix operator
    Then: a correct scale matrix is produced
    """
    scale_mat = scale_matrix((0.2, 0.4))
    desired_output = affine_transform_arrays(numpy_array, scale=(0.2, 0.4))
    result = affine_transform_arrays(numpy_array, matrix=scale_mat)
    np.testing.assert_allclose(next(result), next(desired_output))


def test_rotation_matrix(numpy_array):
    """
    Given: a single numpy array
    When: creating a rotation matrix operator
    Then: a correct rotation matrix is produced
    """
    angle = np.radians(30)
    rotation_mat = rotation_matrix(angle)
    desired_output = affine_transform_arrays(numpy_array, rotation=angle)
    result = affine_transform_arrays(numpy_array, matrix=rotation_mat)
    np.testing.assert_allclose(next(result), next(desired_output))


def test_shear_matrix(numpy_array):
    """
    Given: a single numpy array
    When: creating a shear matrix operator
    Then: a correct shear matrix is produced
    """
    shear = (0.1, 0.2)
    shear_mat = shear_matrix(shear)
    desired_shear_mat = np.array([[1, 0.1, 0], [0.2, 1, 0], [0, 0, 1]])
    np.testing.assert_allclose(shear_mat, desired_shear_mat)
    desired_output = affine_transform_arrays(numpy_array, shear=shear)
    result = affine_transform_arrays(numpy_array, matrix=shear_mat)
    np.testing.assert_allclose(next(result), next(desired_output))


def test_shear_matrix_scalar(numpy_array):
    """
    Given: a single numpy array
    When: creating a shear matrix operator
    Then: a correct shear matrix is produced
    """
    shear = 0.1
    shear_mat = shear_matrix(shear)
    desired_shear_mat = np.array([[1, 0.1, 0], [0.1, 1, 0], [0, 0, 1]])
    np.testing.assert_allclose(shear_mat, desired_shear_mat)
    desired_output = affine_transform_arrays(numpy_array, shear=shear)
    result = affine_transform_arrays(numpy_array, matrix=shear_mat)
    np.testing.assert_allclose(next(result), next(desired_output))


def test_translation_matrix(numpy_array):
    """
    Given: a single numpy array
    When: creating a translation matrix operator
    Then: a correct translation matrix is produced
    """
    trans = (2.3, 5.7)
    trans_mat = translation_matrix(trans)
    desired_output = affine_transform_arrays(numpy_array, translation=trans)
    result = affine_transform_arrays(numpy_array, matrix=trans_mat)
    np.testing.assert_allclose(next(result), next(desired_output))


def test_translation_matrix_scalar(numpy_array):
    """
    Given: a single numpy array
    When: creating a translation matrix operator
    Then: a correct translation matrix is produced
    """
    trans = 4.2
    trans_mat = translation_matrix(trans)
    desired_output = affine_transform_arrays(numpy_array, translation=trans)
    result = affine_transform_arrays(numpy_array, matrix=trans_mat)
    np.testing.assert_allclose(next(result), next(desired_output))


def test_matrix_compositions(numpy_array):
    """
    Given: a single numpy array
    When: creating a composition of transform matrices
    Then: a correct transform results from the composition
    """
    trans = (2.3, 5.7)
    trans_mat = translation_matrix(trans)
    shear = (0.1, 0.2)
    shear_mat = shear_matrix(shear)
    angle = np.radians(30)
    rotation_mat = rotation_matrix(angle)
    scale = (0.2, 0.4)
    scale_mat = scale_matrix(scale)
    # The order in which the transforms are applied reads right to left:
    composition = trans_mat @ rotation_mat @ scale_mat @ shear_mat
    result = affine_transform_arrays(numpy_array, matrix=composition)
    desired_output = affine_transform_arrays(
        numpy_array, scale=scale, shear=shear, rotation=angle, translation=trans
    )
    np.testing.assert_allclose(next(result), next(desired_output))


def test_make_binary_image(numpy_array):
    """
    Given: a single numpy array
    When: generating a binary image for values in the array below a threshold
    Then: a correct binary array results from the generation
    """
    result = make_binary(numpy_array)
    assert isinstance(result, np.ndarray)
    for i in range(len(result)):
        assert max(result[i]) == 1
        assert min(result[i]) == 0


def test_do_hough(numpy_array):
    """
    Given: a single numpy array
    When: performing a hough line transformation
    Then: return the correct hough space, array of angle values, and array of distance values
    """
    binary = make_binary(numpy_array)

    # Rho and Theta ranges
    thetas = np.linspace(-np.pi / 4, np.pi / 4, 1500)
    width, height = binary.shape
    diag_len = np.ceil(np.sqrt(width * width + height * height))  # max_dist
    diag_len = int(diag_len)
    rhos = np.linspace(-diag_len, diag_len, int(diag_len * 2.0))
    # Cache some reusable values
    cos_t = np.cos(thetas)
    sin_t = np.sin(thetas)
    num_thetas = len(thetas)
    # Hough accumulator array of theta vs rho
    accumulator = np.zeros((2 * diag_len, num_thetas), dtype=np.uint64)
    y_idxs, x_idxs = np.nonzero(binary)  # (row, col) indexes to edges
    for i in range(len(x_idxs)):
        x = x_idxs[i]
        y = y_idxs[i]
        for t_idx in range(num_thetas):
            # Calculate rho. diag_len is added for a positive index
            rho = round(x * cos_t[t_idx] + y * sin_t[t_idx]) + diag_len
            accumulator[rho, t_idx] += 1
    desired_H = accumulator
    desired_thetas = thetas
    desired_rhos = rhos
    assert isinstance(desired_H, np.ndarray)
    assert isinstance(desired_thetas, np.ndarray)
    assert isinstance(desired_rhos, np.ndarray)

    result_H, result_theta, result_rho = do_hough(binary, theta_min=-np.pi / 4, theta_max=np.pi / 4)
    assert isinstance(result_H, np.ndarray)
    assert isinstance(result_theta, np.ndarray)
    assert isinstance(result_rho, np.ndarray)

    np.testing.assert_allclose(result_H, desired_H)
    np.testing.assert_allclose(result_theta, desired_thetas)
    np.testing.assert_allclose(result_rho, desired_rhos)


def test_find_px_angles(numpy_array):
    """
    Given: a single numpy array
    When: finding the most significant angles in a hough transform
    Then: return the correct peak angle
    """

    theta = np.linspace(-np.pi / 4, np.pi / 4, 1500)

    def Gaussian(x, mu, sig):
        return np.exp(-np.power(x - mu, 2.0) / (2 * np.power(sig, 2.0)))

    mu = 0.1
    sigma = 0.2
    gaussian = Gaussian(theta, mu, sigma)

    H = np.zeros((20, 1500)) + gaussian[None, :]
    desired_peaktheta = np.array(mu)

    result_peaktheta = find_px_angles(H, theta)
    assert isinstance(result_peaktheta, np.ndarray)

    np.testing.assert_array_almost_equal(result_peaktheta, desired_peaktheta)
