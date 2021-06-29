import numpy as np
import astropy.units as u

from .utils.apod import fft_2d_hanning

__all__ = ["power_spectral_density", "cross_spectral_density"]


def img_to_array(img, apod_size=None):
    """Drop potential unit and mask from input.

    Parameters
    ----------
    img : array_like or :class:`~astropy.units.quantity.Quantity`
        the input (2D) image
    apod_size: int
        size of the hanning apodization function (in pixel)

    Returns
    -------
    img : array
    img_unit : potential image unit or 1
    """
    img_unit = 1

    if isinstance(img, u.Quantity):
        img_unit = img.unit
        img = img.to(img_unit).value
    elif isinstance(img, np.ma.MaskedArray):
        # TODO: apodization will change the absolute level of the powerspectra,
        # check how to correct
        if apod_size is not None:
            img *= fft_2d_hanning(img.mask, apod_size)

        if isinstance(img.data, u.Quantity):
            img_unit = img.data.unit
            img = np.ma.array(img.data.to(img_unit).value, mask=img.mask)

        img = img.filled(0)

    return img, img_unit


def k_bin_edges(shape, res=1, bins=None, range=None):
    """Generate proper bins for power spectra.

    Parameters
    ----------
    shape : [type]
        the shape of the image
    res : float or :class:`~astropy.units.quantity.Quantity`, optional
        the resolution elements of the image
    bins : int or sequence of scalars, optional
        If `bins` is an int, it defines the number of equal-width
        bins in the given range (10, by default). If `bins` is a
        sequence, it defines the bin edges, including the rightmost
        edge, allowing for non-uniform bin widths. (see `~numpy.histogram`)
    range : (float, float) or str, optional
        The lower and upper range of the bins.  If not provided, range
        is simply ``(a.min(), a.max())``. (see `~numpy.histogram`).
        If `range` is a string from the list below, `k_bin_edges`
        will use the method choosen to calculate the bins :

        'tight'
            largest and nyquist scale returned, all method to calculate optimal
            bin width with `numpy.histogram_bin_edges`.

        'tight-linear'
            linear spacing between the largest and nyquist scale

        'tight-log'
            log spacing between the largest and nyquist scale

    Returns
    -------
    bins : int or sequence of scalars
        the corresponding bins
    range: (float, float) or None
        the corresponding range
    """
    nyquist = u.Quantity(1 / (2 * res))
    largest_scale = u.Quantity(1 / (np.array(shape).max() * res))

    if range == "tight":
        return bins, u.Quantity((largest_scale, nyquist))
    elif range == "tight-linear":
        unit = largest_scale.unit
        return np.linspace(largest_scale.to(unit).value, nyquist.to(unit).value, bins + 1, endpoint=True) * unit, None
    elif range == "tight-log":
        unit = largest_scale.unit
        return np.logspace(np.log10(largest_scale.to(unit).value),
                           np.log10(nyquist.to(unit).value),
                           bins + 1, endpoint=True) * unit, None
    else:
        return bins, range


def power_spectral_density(img, res=1, bins=100, range=None, apod_size=None):
    """Return the bin averaged power spectral density of an image

    Parameters
    ----------
    img : array_like or :class:`~astropy.units.quantity.Quantity`
        the input (2D) image
    res : float or :class:`~astropy.units.quantity.Quantity`, optional
        the resolution elements of the image
    bins : int or sequence of scalars or str, optional
        If `bins` is an int, it defines the number of equal-width
        bins in the given range (10, by default). If `bins` is a
        sequence, it defines the bin edges, including the rightmost
        edge, allowing for non-uniform bin widths. (see `~numpy.histogram`)
    range : (float, float) or str, optional
        The lower and upper range of the bins.  If not provided, range
        is simply ``(a.min(), a.max())``. (see `~numpy.histogram`).
        If `range` is a string, it defines the method used to calculate the
        bins, as defined by `k_bin_edges`.

    Returns
    -------
    powspec_k : array or :class:`~astropy.units.quantity.Quantity`
        The value of the power spectrum, optionnaly with a units
    bin_edges : array of dtype float or :class:`~astropy.units.quantity.Quantity`
        Return the bin edges ``(length(hist)+1)``.

    Notes
    -----
    If img as a unit of Jy/beam and res is in arcsec, the resulting
    unit is Jy**2 / beam**2 arcsec**2, by dividing the result per
    the square of the beam area (in say arcsec**2 / beam), one obtain
    Jy**2 / arcsec**2

    """
    img_unit, pix_unit = 1, 1

    # Dropping units here to be backward compatible with astropy<4.0
    # See nikamap #16
    img, img_unit = img_to_array(img, apod_size=apod_size)

    bins, range = k_bin_edges(img.shape, res=res, bins=bins, range=range)

    if isinstance(res, u.Quantity):
        pix_unit = res.unit
        res = res.to(pix_unit).value
        if range is not None:
            assert isinstance(range, u.Quantity), "range must be a Quantity when res has is a Quantity"
            range = range.to(1 / pix_unit).value

        if isinstance(bins, u.Quantity):
            bins = bins.to(1 / pix_unit).value

    npix_x, npix_y = img.shape

    # numpy foward fft does not normalize by 1/N see
    # http://docs.scipy.org/doc/numpy/reference/routines.fft.html#implementation-details
    # Also see the definition of Power Spectral density
    # https://en.wikipedia.org/wiki/Spectral_density
    # Note that the factor 2 is accounted for the fact that we count each
    # frequency twice...
    pow_sqr = np.absolute(np.fft.fft2(img) ** 2 * res ** 2 / (npix_x * npix_y))

    # Define corresponding fourier modes
    u_freq = np.fft.fftfreq(npix_x, d=res)
    v_freq = np.fft.fftfreq(npix_y, d=res)

    k_freq = np.sqrt(u_freq[:, np.newaxis] ** 2 + v_freq ** 2)

    norm, bin_edges = np.histogram(k_freq, bins=bins, range=range)
    hist, bin_edges = np.histogram(k_freq, bins=bin_edges, weights=pow_sqr)
    with np.errstate(invalid="ignore"):
        hist /= norm

    # we drop units in histogram so put it back here
    hist = hist * img_unit ** 2 * pix_unit ** 2
    bin_edges = bin_edges * pix_unit ** -1

    return hist, bin_edges


def cross_spectral_density(img1, img2, res=1, bins=100, range=None, apod_size=None):
    """Return the bin averaged cross power spectral density of two images

    Parameters
    ----------
    img1 : array_like or :class:`~astropy.units.quantity.Quantity`
        the first (2D) image
    img1 : array_like or :class:`~astropy.units.quantity.Quantity`
        the second (2D) image
    res : float or :class:`~astropy.units.quantity.Quantity`, optional
        the resolution elements of the two images
    bins : int or sequence of scalars or str, optional
        If `bins` is an int, it defines the number of equal-width
        bins in the given range (10, by default). If `bins` is a
        sequence, it defines the bin edges, including the rightmost
        edge, allowing for non-uniform bin widths. (see `~numpy.histogram`)
    range : (float, float) or str, optional
        The lower and upper range of the bins.  If not provided, range
        is simply ``(a.min(), a.max())``. (see `~numpy.histogram`).
        If `range` is a string, it defines the method used to calculate the
        bins, as defined by `k_bin_edges`.

    Returns
    -------
    powspec_k : array or :class:`~astropy.units.quantity.Quantity`
        The value of the power spectrum, optionnaly with a units
    bin_edges : array of dtype float or :class:`~astropy.units.quantity.Quantity`
        Return the bin edges ``(length(hist)+1)``.

    Notes
    -----
    If img1 and/or img2 as a unit of Jy/beam and res is in arcsec, the resulting
    unit is Jy**2 / beam**2 arcsec**2, by dividing the result per
    the square of the beam area (in say arcsec**2 / beam), one obtain
    Jy**2 / arcsec**2

    Both images should share the same resolution element `res` and the same shape

    If one image has unit, the other one should also provide units.
    """
    img1_unit, img2_unit, pix_unit = 1, 1, 1

    # Dropping units here to be backward compatible with astropy<4.0
    img1, img1_unit = img_to_array(img1, apod_size=apod_size)
    img2, img2_unit = img_to_array(img2, apod_size=apod_size)

    assert isinstance(
        img1_unit, type(img2_unit)
    ), "img2 must be a quantity or a masked quantity when img1 is a quantity or masked quantity"
    assert img1.shape == img2.shape, "img1 & img2 should have the same shape"

    bins, range = k_bin_edges(img1.shape, res=res, bins=bins, range=range)

    if isinstance(res, u.Quantity):
        pix_unit = res.unit
        res = res.to(pix_unit).value
        if range is not None:
            assert isinstance(range, u.Quantity), "range must be a Quantity when res has is a Quantity"
            range = range.to(1 / pix_unit).value

        if isinstance(bins, u.Quantity):
            bins = bins.to(1 / pix_unit).value

    npix_x, npix_y = img1.shape

    # numpy foward fft does not normalize by 1/N see
    # http://docs.scipy.org/doc/numpy/reference/routines.fft.html#implementation-details
    # Also see the definition of Power Spectral density
    # https://en.wikipedia.org/wiki/Spectral_density
    # Note that the factor 2 is accounted for the fact that we count each
    # frequency twice...
    pow_sqr = np.real(np.fft.fft2(img1) * np.conjugate(np.fft.fft2(img2)) * res ** 2 / (npix_x * npix_y))

    # Define corresponding fourier modes
    u_freq = np.fft.fftfreq(npix_x, d=res)
    v_freq = np.fft.fftfreq(npix_y, d=res)

    k_freq = np.sqrt(u_freq[:, np.newaxis] ** 2 + v_freq ** 2)

    hist, bin_edges = np.histogram(k_freq, bins=bins, range=range, weights=pow_sqr)
    norm, _ = np.histogram(k_freq, bins=bins, range=range)
    with np.errstate(invalid="ignore"):
        hist /= norm

    # we drop units in histogram so put it back here
    hist = hist * img1_unit * img2_unit * pix_unit ** 2
    bin_edges = bin_edges * pix_unit ** -1

    return hist, bin_edges
