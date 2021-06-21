"""
Image reconstruction


See Also
--------
Optional

Notes
-----
Optional

References
----------
Optional, use if references are cited in Notes

Examples
--------
Optional
"""

import logging
from os.path import join
from pathlib import Path

import dask.array as da
import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft2, fftshift, ifft2, ifftshift

import asdf

from dkist.asdf_maker import headers_from_filenames as heads
from dkist.asdf_maker import references_from_filenames as refs
from dkist.io import DaskFITSArrayContainer as DFAC
from dkist.io.fits import AstropyFITSLoader as Loader
from vtfcal.test_constants import TEST_WL_IDX
from vtfcal.utils import correct_darks


def apod_filter(image, width):
    x, y = image.shape[-2:]
    xx, yy = np.mgrid[:x, :y]
    r = np.hypot(xx, yy)
    apod = 0.5 * (1 - np.cos(np.pi * r / width))
    apod[width:-width, width:-width] = 1

    return image * apod


def fft_chunks(image):
    return fftshift(fft2(apod_filter(image, 8)))
    # return fft2(image)


def calc_noise(fft_bb, fsum, bsum):
    return np.abs(fft_bb * (fsum / bsum)) ** 2


def calc_im(fft_bb, nsum, bsum):
    # Really not sure if this should be fft_bb or fftspeck_bb, but I'm doing this for now to make it
    # actually run
    # recon_im = fftspeck_bb * (nsum / bsum)
    return fft_bb * (nsum / bsum)


def calc_power(recon_im):
    # Summing actually breaks the algorithm and I need to figure out why and what to do about it
    return (np.abs(recon_im) ** 2)  #.sum()


def calc_optfilter(recon_noise, data_power):
    opt_filter = (data_power - recon_noise) / data_power
    # Shift interesting parts of the spectrum to the centre
    # opt_filter = fftshift(opt_filter)
    # smooth optimum_filter

    return opt_filter


def reconstruct_image(recon_im, opt_filter):
    filtered_im = recon_im * opt_filter
    recon_nb = ifft2(ifftshift(filtered_im))
    # recon_nb = ifft2(filtered_im)

    return recon_nb


def reconstruct(data_tree, bb_tree=None):
    """
    Function to reconstruct VTF science data

    Loads science frames from the input directory specified by `data_tree` and reconstructs them by
    applying the process described in the VTF algorithm document [1]_.

    Parameters
    ----------
    data_trees : string or :class:`pathlib.Path`
        Paths to :class:`~asdf.AsdfFile`s defining the calibration data structure, including input and output
        data directories, and file references to prepared science data. See
        :meth:`commands.init_data_tree` for generating appropriate files.

    Examples
    --------

    References
    ----------
    .. _[1] VTF/DKIST data pipeline - The algorithm structure
    """
    logger = logging.getLogger(__name__)

    asdf_file = asdf.open(data_tree, mode="rw")
    bb_tree = asdf.open(bb_tree, mode="rw")
    if asdf_file["mode"] == "narrowband" and not bb_tree:
        raise ValueError(
            "Location of broadband data structure must be provided for reconstruction of narrowband data."
        )
    if asdf_file["mode"] != "narrowband":
        raise ValueError(
            f'Unrecognised data mode in asdf tree: {asdf_file["mode"]} '
            '- "mode" keyword should be either "broadband" or "narrowband".'
        )

    # Dark-correct speckle calibration files
    # I assume I need this but I'm not sure if I need to do flats as well
    if "speckle" not in list(bb_tree["support"].keys()):
        logger.warning(
            "Speckle output file not found. Falling back to pre-calculated file."
        )
        speckfile = Path(bb_tree["raw"]["data_dir"]) / "speckle-output.FITS"
        headers = np.array(heads([speckfile]))
        bb_tree["support"]["speckle"] = refs(speckfile, headers, 1)
        bb_tree.update()
    asdf_file = correct_darks(bb_tree, "support", "speckle")

    # polstate = get_polarisation_state()

    # These also obviously need changing to work for all modstates
    nb = DFAC(
        asdf_file["support"]["corrected flat-corrected data modstate0"], loader=Loader
    ).array
    bb = DFAC(
        bb_tree["support"]["corrected flat-corrected data modstate0"], loader=Loader
    ).array
    # flat = DFAC(asdf_file["support"]["corrected wl_shifted flats"], loader=Loader).array
    flat = DFAC(
        asdf_file["support"]["corrected dark-corrected flats modstate0"], loader=Loader
    ).array
    # This likely won't be where the speckle files end up
    logger.debug(bb_tree["support"].keys())
    speckled_bb = DFAC(
        bb_tree["support"]["corrected dark-corrected speckle"], loader=Loader
    ).array
    chunksize = (32, 32)
    overlap = {0: 0, 1: 8, 2: 8}
    nb = da.rechunk(nb, (1, *chunksize))
    bb = da.rechunk(bb, (1, *chunksize))
    flat = da.rechunk(flat, (1, *chunksize))
    speckled_bb = da.rechunk(speckled_bb, chunksize)
    fftspeck_bb = speckled_bb.map_overlap(fft_chunks, depth=(overlap[1], overlap[2]))
    fftspeck_bb = da.rechunk(
        fftspeck_bb.reshape(1, *fftspeck_bb.shape), (1, *chunksize)
    )

    plt.close("all")

    fft_bb = bb.map_overlap(fft_chunks, depth=overlap)
    fft_nb = nb.map_overlap(fft_chunks, depth=overlap)
    fft_flat = flat.map_overlap(fft_chunks, depth=overlap)

    conjugate = fft_bb.conj()
    bsum = (fft_bb * conjugate).real
    nsum = (fft_nb * conjugate).real
    fsum = (fft_flat * conjugate).real

    recon_noise = da.map_overlap(calc_noise, fft_bb, fsum, bsum, depth=overlap)
    recon_im = da.map_overlap(calc_im, fftspeck_bb, nsum, bsum, depth=overlap)
    data_power = recon_im.map_overlap(calc_power, depth=overlap)

    optimum_filter = da.map_overlap(
        calc_optfilter, recon_noise, data_power, depth=overlap
    )

    recon_nb = da.map_overlap(
        reconstruct_image, recon_im, optimum_filter, depth=overlap
    ).compute()
    img = recon_nb[TEST_WL_IDX].real
    logger.debug(f"{img.min()}, {img.mean()}, {img.max()}, {img.std()}")

    logger.debug(f"{nb.shape}, {recon_nb.shape}")
    fig, ax = plt.subplots(1, 2, figsize=(12, 4))
    ax[0].imshow(nb[TEST_WL_IDX].compute())
    vmin = img.mean() - img.std()
    vmax = img.mean() + img.std()
    ax[1].imshow(img)  # , vmin=vmin, vmax=vmax)
    plt.savefig(Path(asdf_file["plots"]) / "reconstructed-narrowband")
    plt.close()
