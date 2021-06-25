# coding=utf-8
import numpy as np

try:
    from pyfftw.interfaces.numpy_fft import rfftn, irfftn, fftshift
except ImportError:
    from numpy.fft import rfftn, irfftn, fftshift


def convolve_nd_valid(cube, psf, compute_fourier=True):
    """
    using fft convolution of n-dim arrays M & N
    Returns a cube of dimensions (M-N+1)³
    """

    if compute_fourier:
        s1 = np.array(cube.shape)
        s2 = np.array(psf.shape)
    else:
        s1 = np.array(cube.shape)
        s2 = np.array(cube.shape) - np.array(psf.shape) + 1

    size_valid = s1 - s2 + 1

    axes = np.arange(s1.size)
    mdslice = list(axes * 0)  # empty list

    fsize = 2 ** np.ceil(np.log2(s1))
    padsize = fsize.astype('int32')  # must be integer
    mshape = fsize

    #output valid slices
    for i in axes:
        #mdslice[i]=slice(s1[i]-pad.shape[i]-size_valid[i],s1[i]-pad.shape[i])
        mdslice[i] = slice(s1[i] - padsize[i] - size_valid[i], s1[i] - padsize[i])

    if compute_fourier:
        fft_psf = rfftn(psf, s=mshape)
    else:
        fft_psf = psf

    res = irfftn(rfftn(cube, s=mshape) * fft_psf).real[mdslice]

    return res, fft_psf


def convolve_3d_same(cube, psf, compute_fourier=True):
    """
    Convolve a 3D cube with PSF & LSF.
    PSF can be the PSF data or its Fourier transform.
    if compute_fourier then compute the fft transform of the PSF.
    if False then assumes that the fft is given.

    This convolution has edge effects (and is slower when using numpy than pyfftw).

    cube: The cube we want to convolve
    psf: The Point Spread Function or its Fast Fourier Transform
    """

    # Pad to power of 2
    padded_cube, cube_slices = padding(cube, axes=[0, 1, 2])

    size = np.array(np.shape(padded_cube)[slice(0, 3)])

    if compute_fourier:
        padded_psf, psf_slices = padding(psf, axes=[0, 1, 2])
        fft_psf = rfftn(padded_psf, s=size, axes=[0, 1, 2])
    else:
        fft_psf = psf

    fft_img = rfftn(padded_cube, s=size, axes=[0, 1, 2])

    # Convolution
    fft_cube = np.real(fftshift(irfftn(fft_img * fft_psf, s=size, axes=[0, 1, 2]), axes=[0, 1, 2]))

    # Remove padding
    cube_conv = fft_cube[cube_slices]

    return cube_conv, fft_psf


def convolve_3d_xy(cube, psf, compute_fourier=True):
    """
    Convolve 3D cube along spatial directions only,
    using provided Point Spread Function.
    """

    # Compute needed padding
    cubep, boxcube = padding(cube, axes=[1, 2])

    size = np.array(np.shape(cubep)[slice(1, 3)])

    if compute_fourier:
        psfp, boxpsf = padding(psf, axes=[1, 2])
        fftpsf = np.fft.rfftn(psfp, s=size, axes=[1, 2])

    else:
        fftpsf = psf

    fftimg = np.fft.rfftn(cubep, s=size, axes=[1, 2])

    #Convolution
    fft = np.fft.fftshift(np.fft.irfftn(fftimg * fftpsf, s=size, axes=[1, 2]), axes=[1, 2]).real

    # Remove padding
    cube_conv = fft[boxcube]

    return cube_conv, fftpsf


def convolve_2d(image, psf, compute_fourier=True):
    """
    Compute fft of image And of PSF
    Accepts fftPSF already computed with do_PSF=False
    Reproduces Matt's convolution with PSF
    """

    # Compute needed padding
    cubep, boxcube = padding(image)

    if compute_fourier:
        psfp, boxpsf = padding(psf)
        fftpsf = np.fft.rfft2(psfp)
    else:
        fftpsf = psf

    fftimg = np.fft.rfft2(cubep)

    # Convolution
    fft = np.fft.fftshift(np.fft.irfft2(fftimg * fftpsf)).real

    # Remove padding
    cube_conv = fft[boxcube]

    return cube_conv, fftpsf


def convolve_1d(data, psf, compute_fourier=True, axis=0):
    """
    Convolve data with PSF only along one dimension specified by axis (default: 0)
    PSF can be the PSF data or its Fourier transform
    if compute_fourier then compute the fft transform of the PSF.
    if False then assumes that the fft is given.
    """

    axis = np.array([axis])

    # Compute needed padding
    cubep, boxcube = padding(data, axes=axis)

    # Get the size of the axis
    size = np.array(np.shape(cubep)[slice(axis, axis + 1)])

    if compute_fourier:
        psfp, boxpsf = padding(psf, axes=axis)
        fftpsf = np.fft.rfftn(psfp, s=size, axes=axis)
    else:
        fftpsf = psf

    fftimg = np.fft.rfftn(cubep, s=size, axes=axis)

    # Convolution
    fft = np.fft.fftshift(np.fft.irfftn(fftimg * fftpsf, s=size, axes=axis), axes=axis).real

    # Remove padding
    cube_conv = fft[boxcube]

    return cube_conv, fftpsf


def padding(cube, axes=None):
    """
    Computes padding needed for a cube to make sure it has
    a power of 2 shape along dimensions of passed axes (default [0,1])
    Returns padded cube and cube slices,
    which are the indices of the actual data in the padded cube.
    """

    if axes is None:
        axes = [0, 1]

    # Compute padding size for each axis
    old_shape = np.shape(cube)
    new_shape = np.array(old_shape)
    for axis in axes:
        zdim = cube.shape[axis]
        s = np.binary_repr(zdim - 1)
        s = s[:-1] + '0'
        new_shape[axis] = 2 ** len(s)

    cube_padded = np.zeros(new_shape)
    #cube_slices = np.empty(len(old_shape), slice).tolist()
    cube_slices = [None for i in range(len(old_shape))]

    for i, v in enumerate(old_shape):
        cube_slices[i] = slice(0, old_shape[i])

    for axis in axes:
        diff = new_shape[axis] - old_shape[axis]
        if (diff & 1):
            half = diff // 2 + 1
        else:
            half = diff // 2
        cube_slices[axis] = slice(half, old_shape[axis] + half)

    cube_slices = tuple(cube_slices)
    # Copy cube contents into padded cube
    cube_padded[cube_slices] = cube.copy()

    return cube_padded, cube_slices
