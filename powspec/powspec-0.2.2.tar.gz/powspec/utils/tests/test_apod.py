import pytest

import numpy as np
import numpy.testing as npt


def test_shrink_mask():

    from ..apod import shrink_mask

    kernel_size = 3
    mask_size = 48

    mask = np.ones((2 * mask_size, 2 * mask_size), bool)
    center_slice = slice(mask_size - mask_size // 3, mask_size + mask_size // 3)
    mask[center_slice, center_slice] = False

    result = np.ones((2 * mask_size, 2 * mask_size), bool)
    center_slice = slice(mask_size - mask_size // 3 + kernel_size, mask_size + mask_size // 3 - kernel_size)
    result[center_slice, center_slice] = False

    xx = np.arange(2 * kernel_size + 1) - kernel_size
    kernel = np.exp(-(xx ** 2 + xx[:, np.newaxis] ** 2) / 2)
    kernel /= kernel.sum()

    shrinked_mask = shrink_mask(mask, kernel)

    assert np.all(result == shrinked_mask)


def test_fft_2d_hanning_assertion():

    from ..apod import fft_2d_hanning

    shape = 5
    mask = np.ones((shape, shape), dtype=bool)

    with pytest.raises(AssertionError):
        fft_2d_hanning(mask, size=2)

    with pytest.raises(AssertionError):
        fft_2d_hanning(mask, size=1)


def test_fft_2d_hanning():

    from ..apod import fft_2d_hanning

    # Min hann filter is 5 x 5
    shape = 15
    size = 5
    apod_size = 2

    mask = np.ones((shape, shape), dtype=bool)
    islice = slice(((shape - 1) - (size - 1)) // 2, ((shape - 1) + (size - 1)) // 2 + 1)
    mask[islice, islice] = False

    apod = fft_2d_hanning(mask, size=apod_size)
    # Nothing outside the mask
    assert np.all((apod > 1e-15) == ~mask)
    # Only unchanged pixel at the center
    unchanged = slice(
        ((shape - 1) - (size - 1) + (apod_size * 2 + 1 - 1)) // 2,
        ((shape - 1) + (size - 1) - (apod_size * 2 + 1 - 1)) // 2 + 1,
    )

    npt.assert_allclose(apod[unchanged, unchanged], 1)

    shape = 45
    size = 15
    apod_size = 2

    mask = np.ones((shape, shape), dtype=bool)
    islice = slice(((shape - 1) - (size - 1)) // 2, ((shape - 1) + (size - 1)) // 2 + 1)
    mask[islice, islice] = False
    apod = fft_2d_hanning(mask, size=2)

    assert np.all((apod > 1e-15) == ~mask)
    unchanged = slice(
        ((shape - 1) - (size - 1) + (apod_size * 2 + 1 - 1)) // 2,
        ((shape - 1) + (size - 1) - (apod_size * 2 + 1 - 1)) // 2 + 1,
    )
    npt.assert_allclose(apod[unchanged, unchanged], 1)
