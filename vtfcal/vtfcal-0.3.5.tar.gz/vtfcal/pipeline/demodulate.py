import logging

import asdf

from vtfcal.calibration.demodulate import demod
from vtfcal.utils import plotframes


def demodulate(data_tree, input_data_key="calibrated aligned data"):
    """
    """

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    asdf_file = asdf.open(data_tree, mode="rw")
    outdir = asdf_file["support"]["data_dir"]

    asdf_file = demod(asdf_file, input_data_key=input_data_key)
    asdf_file.update()

    titles = [r"$I_0$", r"$I_1$", r"$I_2$", r"$I_3$", r"$I$", r"$Q$", r"$U$", r"$V$"]
    keys = [f"{input_data_key} modstate{m}" for m in range(4)] + [
        f"calibrated demodulated data modstate{m}" for m in range(4)
    ]
    plotframes(asdf_file, list(zip(keys, titles)), "05-demodulated-data")
