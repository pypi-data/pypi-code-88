import os
import re
import shutil
import logging
import tempfile
import configparser as cfp
from pathlib import Path

import numpy as np
from skimage.transform import AffineTransform, warp

from astropy.io import fits

from vtfcal import utils


def process(data_dir=utils.DATA, raw_data_dir=utils.DATA, dataset_id=None):
    """"""
    logger = logging.getLogger(__name__)
    logger.setLevel("INFO")
    # This bit just to convert raw speckle calibration burst into fits
    # Probably no longer necessary
    specburst = raw_data_dir / "speckle"
    specburst_files = specburst.rglob("*.raw")
    for fname in specburst_files:
        img = np.fromfile(fname, dtype="int16").reshape((1024, 1024))
        newf = raw_data_dir / "broadband" / f"speckle_{fname.stem}.FITS"
        fits.writeto(str(newf), img, overwrite=True)

    cfg = cfp.ConfigParser()
    cfg.read("vtf-calibration-config.cfg")
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    dataset_dir = (
        data_dir / dataset_id if dataset_id else Path(tempfile.mkdtemp(dir=data_dir))
    )
    if dataset_id:
        s = dataset_dir / "support"
        oldfiles = s.rglob("*.FITS")
        [os.remove(f) for f in oldfiles]

    allfiles = raw_data_dir.rglob("*.FITS")

    chankeys = {"broadband": "BB", "narrowband1": "NB+", "narrowband2": "NB-"}
    for channel in ["broadband", "narrowband1", "narrowband2", "polarization"]:
        subdirs = ["raw", "processed", "support", "polarization", "plots"]
        for subdir in subdirs:
            s = dataset_dir / subdir
            if not os.path.exists(s):
                os.makedirs(s)
            if subdir != "plots":
                for m in range(4):
                    s2 = s / f"modstate{m}"
                    if not os.path.exists(s2):
                        os.makedirs(s2)

    for rawfile in allfiles:
        rawpath = rawfile.relative_to(raw_data_dir).parent
        newfile = str(dataset_dir / "raw" / rawpath / f"{rawfile.stem}.FITS")
        channel = utils.get_channel(rawfile)

        if (rawfile.name == "target.FITS") or (channel is None):
            shutil.copy2(rawfile, newfile)
        else:
            # TODO Take out the hard-coded image sizes here and use TEST_IMAGE_SIZE instead
            raw_image = fits.open(rawfile)[0]
            img = raw_image.data
            rot = cfg.getfloat("camera-rotations", channel)
            scale = 512 / np.array(img.shape)
            c = np.cos(np.deg2rad(rot))
            s = np.sin(np.deg2rad(rot))
            rmatrix = np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])
            array_centre = np.array(utils.TEST_DATA_SIZE) / 2.0
            displacement = np.dot(rmatrix[:2, :2], array_centre) - array_centre
            rmatrix[:2, 2] = -displacement
            rmatrix[:2, :2] *= scale
            tform = AffineTransform(matrix=rmatrix)
            new_image = warp(
                img, tform.inverse, output_shape=utils.TEST_DATA_SIZE, cval=img.mean()
            )
            new_image = utils.mask_aperture(new_image)

            # Raw simulation data don't distinguish between channels at the moment
            # TODO double check that they do distinguish between modstates
            new_header = raw_image.header
            new_header["VTF__002"] = chankeys[channel]

            fits.writeto(newfile, new_image, header=new_header, overwrite=True)

    return dataset_dir
