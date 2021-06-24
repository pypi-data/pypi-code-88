import logging
from pathlib import Path

import numpy as np
from skimage.transform import AffineTransform, warp

from astropy.io import fits

from dkist.asdf_maker import headers_from_filenames as heads
from dkist.asdf_maker import references_from_filenames as refs
from vtfcal.reconstruction.speckle import calc_fried_param, run_speckle
from vtfcal.test_constants import TEST_DATA_SIZE
from vtfcal.utils import plotframes


def reconstruct(asdf_file):
    logger = logging.getLogger(__name__)
    # Not sure if I should be doing this one per modstate or not?

    r0 = calc_fried_param()
    # Things that should change here:
    # - autoget width and height (from a previous image I guess, or from run metadata)
    # - separate files into bursts (by timestamps? burst metadata) and repeat below for each burst
    # - autoget burst size from number of files
    # - use burst min/max timestamps to sort AO data for r0 calculation
    specframe = run_speckle(
        width=1024,
        height=1024,
        burst_directory="vtfTestImages",
        burst_prefix="cssSim_1024x1024",
        burst_suffix=".raw",
        burst_size=99,
        fixed_width=3,
        gpus=0,
        fried_parameter=r0,
    )

    outdir = asdf_file["support"]["data_dir"]
    fname = Path(outdir) / "speckle-output.FITS"

    imsize = np.array(specframe.shape)
    if (imsize != TEST_DATA_SIZE).any():
        logger.warning(
            "Speckle images do not match size of simulated VTF data - scaling to match."
        )
        scale = TEST_DATA_SIZE / imsize
        specframe = warp(
            specframe,
            AffineTransform(
                matrix=np.array([[scale, 0, 0], [0, scale, 0], [0, 0, 1]])
            ).inverse,
            output_shape=(TEST_DATA_SIZE),
            cval=specframe.mean(),
        )
    fits.writeto(fname, specframe, overwrite=True)
    headers = np.array(heads([specframe]))
    asdf_file["support"]["speckle"] = refs(specframe, headers, 1)
    asdf_file.update()

    plotframes(
        asdf_file, [("speckle", "Speckle-reconstructed broadband image",)], "speckle",
    )

    return asdf_file
