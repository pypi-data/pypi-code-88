import logging
from vtfcal.utils import correct_darks

def reduce_prefilter(data_tree):
    """
    """

    logger = logging.getLogger(__name__)

    asdf_file = asdf.open(data_tree, mode="rw")

    # Dark correct prefilter frames
    asdf_file = correct_darks(asdf_file, "raw", "prefilter")
    corrected_frames = asdf_file["support"]["corrected dark-corrected prefilter"]
    # Average across accumulations
    # Correct wavelength shift in prefilter frames
    # Build scan curve - average over x, y for each frame to just leave lambda
    # Align FTS atlas spectrum with scan curve
    # Divide scan by FTS spectrum
    # Fit double-Gaussian
