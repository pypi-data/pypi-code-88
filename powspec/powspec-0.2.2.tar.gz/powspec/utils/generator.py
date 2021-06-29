import numpy as np
from copy import deepcopy

from astropy.convolution import Kernel2D, convolve_fft
from astropy.convolution.kernels import _round_up_to_odd_integer

__all__ = ["Pk", "gen_pkfield"]


def Pk(k, alpha=-11.0 / 3, fknee=1):
    """Simple power law formula"""
    return (k / fknee) ** alpha


def gen_pkfield(npix=32, alpha=-11.0 / 3, fknee=1, res=1):
    """Generate a gaussian field with (k/k_0)^alpha law.

    Parameters
    ----------
    npix : int, optional
        number of pixels for the map, by default 32
    alpha : [float], optional
        the power law index, by default -11.0/3
    fknee : float or ~astropy.units.Quantity, optional
        the knee frequency in 1/res unit, where P(k) = 1, by default 1
    res : float or ~astropy.units.Quantity, optional
        size of a pixel, by default 1

    Returns
    -------
    data : ndarray, shape(n_pix, n_pix)
        the requested gaussian field
    """
    ufreq = np.fft.fftfreq(npix, d=res)
    kfreq = np.sqrt(ufreq[:, np.newaxis] ** 2 + ufreq ** 2)

    with np.errstate(divide="ignore"):
        psd = 2 * Pk(kfreq, alpha=alpha, fknee=fknee)
    psd[0, 0] = 0

    pha = np.random.uniform(low=-np.pi, high=np.pi, size=(npix, npix))

    fft_img = np.sqrt(psd) * (np.cos(pha) + 1j * np.sin(pha))
    return np.real(np.fft.ifft2(fft_img)) * npix / res ** 2


def gen_psffield(positions, fluxes=None, shape=(32, 32), kernel=None, factor=None):
    """Generate a point spread function field given a catalog of point source.

    Fourier method

    Parameters
    ----------
    positions : array_like, shape (2, M)
        x, y positions in pixel coordinates
    fluxes : array_like, shape (M,)
        corresponding peak fluxes
    shape : int or [int, int], optional
        the output image shape
    kernel : ~astropy.convolution.Kernel2D, optional
        the 2D kernel to be used for the PSF
    factor : [int], optional
        a overpixelization factor used for the projection before smoothing, by default None

    Returns
    -------
    array : ndarray, shape(nx, ny)
        The corresponding map
    """

    if factor is None:
        factor = 1
    if fluxes is None:
        fluxes = np.ones(positions.shape[1])

    if isinstance(shape, (int, np.int)):
        shape = [shape, shape]

    _shape = np.array(shape) * factor
    _positions = (np.asarray(positions) + 0.5) * factor - 0.5

    if kernel is not None:
        # Upscale the kernel with factor
        kernel = deepcopy(kernel)
        for param in ["x_stddev", "y_stddev", "width", "radius", "radius_in"]:
            if param in kernel._model.param_names:
                getattr(kernel._model, param).value *= factor

        Kernel2D.__init__(
            kernel,
            x_size=_round_up_to_odd_integer(kernel.shape[1] * factor),
            y_size=_round_up_to_odd_integer(kernel.shape[0] * factor),
        ),

    # Range are maximum bins edges
    hist2d_kwd = {"bins": _shape, "range": ((-0.5, _shape[0] - 0.5), (-0.5, _shape[1] - 0.5))}

    # reverse the _positions because it needs to be y x
    array = np.histogram2d(*_positions[::-1], weights=fluxes, **hist2d_kwd)[0]

    # Remove nan if present
    array[np.isnan(array)] = 0

    if kernel is not None:
        kernel.normalize("peak")
        array = convolve_fft(array, kernel, normalize_kernel=False, boundary="wrap") / factor ** 2

    # Average rebinning onto the input shape
    array = array.reshape((shape[0], factor, shape[1], factor)).sum(-1).sum(1)
    return array


def gen_psffield_direct(positions, fluxes=None, shape=(32, 32), kernel=None, factor=None):
    """Generate a point spread function field given a catalog of point source.

    Direct method

    Parameters
    ----------
    positions : array_like, shape (2, M)
        x, y positions in pixel coordinates
    fluxes : array_like, shape (M,)
        corresponding peak fluxes
    shape : int or [int, int], optional
        the output image shape
    kernel : ~astropy.convolution.Kernel2D, optional
        the 2D kernel to be used for the PSF
    factor : [int], optional
        a overpixelization factor used for the projection before smoothing, by default None

    Returns
    -------
    array : ndarray, shape(nx, ny)
        The corresponding map
    """
    if factor is None:
        factor = 1
    if fluxes is None:
        fluxes = np.ones(positions.shape[1])

    if isinstance(shape, (int, np.int)):
        shape = [shape, shape]

    _shape = np.array(shape) * factor
    # _positions = (np.asarray(positions) + 0.5) * factor - 0.5

    if kernel is not None:
        # Upscale the kernel with factor
        kernel = deepcopy(kernel)
        for param in ["x_stddev", "y_stddev", "width", "radius", "radius_in"]:
            if param in kernel._model.param_names:
                getattr(kernel._model, param).value *= factor

        Kernel2D.__init__(
            kernel,
            x_size=_round_up_to_odd_integer(kernel.shape[1] * factor),
            y_size=_round_up_to_odd_integer(kernel.shape[0] * factor),
        ),

    xx, yy = np.meshgrid(np.arange(_shape[1]), np.arange(_shape[0]))
    array = np.zeros(_shape)
    for position, flux in zip(positions.T, fluxes):
        kernel._model.x_mean = position[0]
        kernel._model.y_mean = position[1]
        kernel._model.amplitude = flux
        array += kernel._model(xx, yy)

    array = array.reshape((shape[0], factor, shape[1], factor)).sum(-1).sum(1)
    return array
