"""
Flat frame reduction

Average collected flat frames as appropriate to reduce to the smallest number required to calibrate
the science data.

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
from multiprocessing.pool import ThreadPool

import dask
import dask.array as da
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np
from dask.distributed import Client

import asdf
from astropy.io import fits

from dkist.asdf_maker import headers_from_filenames as heads
from dkist.asdf_maker import references_from_filenames as refs
from dkist.io import DaskFITSArrayContainer as DFAC
from dkist.io.fits import AstropyFITSLoader as Loader
from vtfcal.reduction.flats import average_flats, calculate_wl_shift, correct_wl_shift
from vtfcal.test_constants import TEST_PIXEL, TEST_WL_IDX
from vtfcal.utils import correct_darks, plotframes, plotprofile

# Set up dask for threading of intensive tasks.
# Need this here because Client doesn't like being instantiated not in __main__.
if __name__ == "__main__":
    client = Client()
    dask.config.set(pool=ThreadPool())


def reduce_flats(
    data_tree, input_flats_key="reduced averaged flats", correction=True, fourier=True,
):
    """
    Function to reduce VTF flat frames

    Loads flat frames from the input directory specified by `data_tree` and reduces them by applying
    the following steps:

    - Group frames by wavelength position and average them
    - Correct for darks
    - Calculate and correct for wavelength shift
    - Normalise images by scaling each frame by its average value [still needs implementing]

    Reduced flats are saved to the output directory specified by `data_tree` and references to the
    files are added to the tree for use later in the calibration process.

    Parameters
    ----------
    data_tree : string or :class:`pathlib.Path`
        Path to an :class:`~asdf.AsdfFile` defining the calibration data structure, including input
        and output data directories, and file references to averaged darks. See
        :meth:`commands.init_data_tree` for generating an appropriate file.

    Examples
    --------

    """
    logger = logging.getLogger(__name__)
    logger.setLevel("INFO")

    asdf_file = asdf.open(data_tree, mode="rw")
    outdir = asdf_file["support"]["data_dir"]

    asdf_file = average_flats(asdf_file)
    if asdf_file["mode"] not in ["broadband", "narrowband"]:
        raise ValueError(
            f'Unrecognised data mode in asdf tree: {asdf_file["mode"]} '
            '- "mode" keyword should be either "broadband" or "narrowband".'
        )
    for modstate in ["modstate0", "modstate1", "modstate2", "modstate3"]:
        asdf_file = correct_darks(asdf_file, "support", f"{input_flats_key} {modstate}")
        dark_corrected_files = asdf_file["support"][
            f"corrected dark-corrected flats {modstate}"
        ]
        dark_corrected_flats = DFAC(dark_corrected_files, loader=Loader).array

        plotframes(
            asdf_file,
            [
                (f"{input_flats_key} {modstate}", "Averaged flat frames"),
                (f"reduced averaged darks", "Averaged dark frame"),
                (
                    f"corrected dark-corrected flats {modstate}",
                    "Dark-corrected flat frame",
                ),
            ],
            "01aii-flat-correction",
        )

        plotprofile(
            asdf_file,
            [
                (f"{input_flats_key} {modstate}", "Raw flats"),
                (f"corrected dark-corrected flats {modstate}", "Dark-corrected flats"),
            ],
            f"01bii-averaged-vs-corrected-profiles-{modstate}",
            linestyle=[":", "--"],
            color=["red", "blue"],
        )

        if asdf_file["mode"] == "broadband":
            continue

        if not correction:
            norm_frames = (
                dark_corrected_flats
                / np.nanmean(dark_corrected_flats, axis=(1, 2))[
                    :, np.newaxis, np.newaxis
                ]
            )
            norm_fnames = []
            for wl, frame in enumerate(norm_frames):
                fname = Path(outdir) / modstate / f"normalised_flat_l{wl:02}a0.FITS"
                fits.writeto(fname, frame.compute(), overwrite=True)
                norm_fnames.append(fname)
            asdf_file["support"]["corrected normalised flats " + modstate] = refs(
                norm_fnames, np.array(heads(norm_fnames)), len(norm_fnames)
            )
            asdf_file.update()

            mean_profile = np.nanmean(dark_corrected_flats, axis=(1, 2))
            plotprofile(
                asdf_file,
                [
                    (f"{input_flats_key} {modstate}", "Raw flats"),
                    (
                        f"corrected dark-corrected flats {modstate}",
                        "Dark-corrected flats",
                    ),
                    (mean_profile.reshape(len(norm_frames)), "Average profile"),
                    (f"corrected normalised flats {modstate}", "Normalised flats"),
                ],
                f"profile-comparison-{modstate}",
                linestyle=["-.", ":", "--", None],
                color=["black", "red", "blue", "green"],
            )

            continue

        asdf_file, dark_corrected_flats = calculate_wl_shift(
            asdf_file, modstate, fourier=fourier
        )

        wl_shift_map = fits.open(
            asdf_file["support"]["calibration wl-shift-map " + modstate][0].fileuri
        )[0].data
        shifted_flats = correct_wl_shift(
            dark_corrected_flats, wl_shift_map, fourier=fourier,
        )

        shifted_files = []
        for wl, frame in enumerate(shifted_flats):
            filename = Path(outdir) / modstate / f"wl_shifted_flat_l{wl:02}a0.FITS"
            fits.writeto(filename, frame.compute(), overwrite=True)
            shifted_files.append(filename)
        asdf_file["support"]["corrected wl-shifted flats " + modstate] = refs(
            shifted_files, np.array(heads(shifted_files)), len(shifted_files)
        )

        plotframes(
            asdf_file,
            [
                (
                    f"corrected dark-corrected flats {modstate}",
                    "Dark-corrected flat frame",
                ),
                (f"calibration wl-shift-map {modstate}", r"$\lambda$-shift map"),
                (
                    f"corrected wl-shifted flats {modstate}",
                    r"$\lambda$-shifted flat frame",
                ),
            ],
            f"01g-wl-shift-comparison",
        )

        logger.debug(shifted_flats.shape)

        mean_shifted_profile = da.nanmean(shifted_flats, axis=(1, 2))
        unshifted_mean = correct_wl_shift(
            mean_shifted_profile[:, np.newaxis, np.newaxis],
            -wl_shift_map,
            fourier=fourier,
        )
        norm_frames = dark_corrected_flats / unshifted_mean
        norm_fnames = []
        for wl, frame in enumerate(norm_frames):
            fname = Path(outdir) / modstate / f"normalised_flat_l{wl:02}a0.FITS"
            fits.writeto(fname, frame.compute(), overwrite=True)
            norm_fnames.append(fname)
        asdf_file["support"]["corrected normalised flats " + modstate] = refs(
            norm_fnames, np.array(heads(norm_fnames)), len(norm_fnames)
        )
        asdf_file.update()

        plotframes(
            asdf_file,
            [
                (
                    f"corrected wl-shifted flats {modstate}",
                    r"$\lambda$-shifted flat frame",
                ),
                (
                    f"corrected normalised flats {modstate}",
                    "Normalised shifted flat frame",
                ),
            ],
            "01h-normalisation-comparison",
        )

        plotprofile(
            asdf_file,
            [
                (
                    f"corrected wl-shifted flats {modstate}",
                    r"$Mean \lambda$-shifted profile",
                ),
                (
                    f"corrected dark-corrected flats {modstate}",
                    "Dark-corrected profile",
                ),
                (f"corrected normalised flats {modstate}", "Normalised flats"),
            ],
            f"01i-normalisation-comparison-{modstate}",
            plot_mean=[True, False, False],
            linestyle=[":", "--", None],
            color=["black", "blue", "green"],
        )
