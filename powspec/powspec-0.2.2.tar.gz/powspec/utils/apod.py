import numpy as np
from scipy import signal

from astropy.convolution import CustomKernel, convolve_fft

__all__ = ["shrink_mask", "fft_2d_hanning"]


def shrink_mask(mask, kernel):
    """Shrink mask wrt to a kernel

    Parameters
    ----------
    mask : 2D boolean array_like
        the mask to be shrinked by...
    kernel : 2D float array_like
        ... the corresponding array

    Returns
    -------
    2D boolean array
        the corresponding shrunk mask

    Notes
    -----
    The kernel sum must be normalized
    """
    return ~np.isclose(signal.fftconvolve(~mask, kernel, mode="same"), 1)


def fft_2d_hanning(mask, size=2):

    assert np.min(mask.shape) > size * 2 + 1
    assert size > 1

    idx = np.linspace(-0.5, 0.5, size * 2 + 1, endpoint=True)
    xx, yy = np.meshgrid(idx, idx)
    n = np.sqrt(xx ** 2 + yy ** 2)
    hann_kernel = (1 + np.cos(2 * np.pi * n)) / 2
    hann_kernel[n > 0.5] = 0

    hann_kernel = CustomKernel(hann_kernel)
    hann_kernel.normalize("integral")

    # Reduce mask size to apodize on the edge
    apod = ~shrink_mask(mask, hann_kernel)

    # Final convolution goes to 0 on the edge
    apod = convolve_fft(apod, hann_kernel)

    return apod
