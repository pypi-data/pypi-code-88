"""
Science data preparation

Functions to perform dark corrections on raw science data as part of the preparation for more
rigourous image reconstruction using those data.

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

import numpy as np

import asdf
import ccdproc

from dkist.asdf_maker import headers_from_filenames as heads
from dkist.asdf_maker import references_from_filenames as refs
from dkist.io import DaskFITSArrayContainer as DFAC
from dkist.io.fits import AstropyFITSLoader as Loader
from vtfcal.correction.flat_correction import flat_correct
from vtfcal.test_constants import TEST_PIXEL, TEST_WL_IDX
from vtfcal.utils import plotframes, plotprofile


def correct_flats(
    data_tree, input_flat_key=None, input_data_key="corrected dark-corrected data"
):
    """
    Apply flat correction to data frames.

    Loads dark-corrected data frames specified by `data_tree` and corrects them for flat-field
    effects using the reduced flats calculated using :meth:`commands.reduce_flats`. Corrected frames
    are saved to the output directory specified by `data_tree` and references to the files are added
    to the tree for use later in the calibration process.

    Parameters
    ----------
    data_tree : string or :class:`pathlib.Path`
        Path to an :class:`~asdf.AsdfFile` defining the calibration data structure, including input
        and output data directories, and file references to reduced flats. See
        :meth:`commands.init_data_tree` for generating an appropriate file.

    Examples
    --------

    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    asdf_file = asdf.open(data_tree, mode="rw")
    mode = asdf_file["mode"]
    if not input_flat_key:
        input_flat_key = (
            "corrected dark-corrected flats"
            if mode == "broadband"
            else "corrected normalised flats"
        )

    for modstate in ["modstate0", "modstate1", "modstate2", "modstate3"]:
        datafiles = asdf_file["support"][f"{input_data_key} {modstate}"]
        outdir = asdf_file["support"]["data_dir"]

        if asdf_file["mode"] == "broadband":
            allflats = asdf_file["support"][f"{input_flat_key} {modstate}"]
            flats = [
                ccdproc.CCDData.read(f.fileuri, format="fits", unit="adu")
                for f in allflats
            ]
        else:
            ## REFACTOR: rewrite whatever saves the stack to do it as fits files and as part of the asdf
            flat_data = DFAC(
                asdf_file["support"][f"{input_flat_key} {modstate}"], loader=Loader,
            ).array
            flats = [
                ccdproc.CCDData(frame.compute(), unit="adu") for frame in flat_data
            ]
        corrected_frames = flat_correct(datafiles, flats)
        headers = np.array(heads(corrected_frames))
        asdf_file["support"][f"corrected flat-corrected data {modstate}"] = refs(
            corrected_frames, headers, len(corrected_frames)
        )

        plotframes(
            asdf_file,
            [
                (
                    f"corrected flat-corrected data {modstate}",
                    "Flat-corrected data frame",
                )
            ],
            "02b-flat-corrected-data",
        )

        if mode != "broadband":
            plotprofile(
                asdf_file,
                [
                    (
                        f"corrected dark-corrected data {modstate}",
                        "Dark-corrected data",
                    ),
                    (f"corrected normalised flats {modstate}", "Normalised flats"),
                    (
                        f"corrected flat-corrected data {modstate}",
                        "Flat-corrected data",
                    ),
                ],
                f"02c-flat-correction-comparison-{modstate}",
                linestyle=[":", "--", None],
                color=["black", "blue", "green"],
            )

    asdf_file.update()
