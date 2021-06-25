import logging
from os.path import join, split
from pathlib import Path
from itertools import groupby
from collections import defaultdict

import numpy as np

import asdf
import ccdproc
from astropy.io import fits

from dkist.asdf_maker import headers_from_filenames as heads
from dkist.asdf_maker import references_from_filenames as refs


def get_wavelength_step(filepath):
    logger = logging.getLogger(__name__)
    logger.setLevel("INFO")
    header = fits.getheader(filepath)
    try:
        l = header["VTF__014"]
        return int(l)
    except KeyError:
        logger.warning(
            f"Header keyword 'VTF__014' not found for file {filepath}. Assuming spectral step == 0."
        )
        return 0


def get_modstate(filepath):
    header = fits.getheader(filepath)
    m = header["VTF__021"]
    return f"modstate{int(m)}"


def get_channel(filepath):
    channels = defaultdict(lambda: None)
    channels["BB"] = "broadband"
    channels["NB1"] = "narrowband1"
    channels["NB2"] = "narrowband2"
    header = fits.getheader(filepath)
    if "VTF__002" in list(header.keys()):
        c = header["VTF__002"]
        if c != "default":
            return channels[c]

    for c in ["broadband", "narrowband1", "narrowband2"]:
        if c in filepath.parts:
            return c


def mask_aperture(arr):
    x, y = arr.shape
    x0, y0 = np.array((x, y)) / 2
    xx, yy = np.mgrid[:x, :y]
    r = np.hypot(xx - x0, yy - y0)
    maxr = min(x0, y0) * 0.98
    arr[r > maxr] = np.nan

    return arr


def average_by_wavelength(asdf_file, filekey):
    """
    Function to average VTF flat frames

    Loads specified flat frames, groups them by wavelength position and averages them, producing one
    averaged flat per wavelength step for the narrowband channels and one master flat for the
    broadband channel. Input files should all be for the same line scan and VTF channel. Reduced
    frames are saved to the output directory specified by `data_tree` and references to the files
    are added to the tree for use later in the calibration process.

    Parameters
    ----------
    data_tree : string or `Path<https://docs.python.org/3/library/pathlib.html#pathlib.Path>`_
        Path to an `AsdfFile` defining the calibration data structure, including input and output
        data directories. See :meth:`vtf-pipeline.commands.init_data_tree` for generating an
        appropriate file.

    Returns
    -------
    new_asdf : :class:`asdf.AsdfFile`
        Updated :class:`asdf.AsdfFile` containing the same information as `data_tree` plus file
        references to the averaged flat frames.

    Examples
    --------

    """
    logger = logging.getLogger(__name__)
    logger.setLevel("INFO")

    # TODO This is always going to be something that needs ensuring, so consider making a decorator for it
    if asdf_file["mode"] not in ["broadband", "narrowband"]:
        raise ValueError(
            f'Unrecognised data mode in asdf tree: {asdf_file["mode"]} '
            '- "mode" keyword should be either "broadband" or "narrowband".'
        )

    raw_dir = asdf_file["raw"]["data_dir"]
    logger.debug(f"{raw_dir}")
    outdir = asdf_file["support"]["data_dir"]
    logger.debug(f"{outdir}")

    # This is not especially robust
    fnames = [str(f.fileuri) for f in asdf_file["raw"][filekey]]
    logger.debug(f"Found the following raw {filekey} files: {fnames}")

    fnames = sorted(fnames, key=get_modstate)
    filegroups = groupby(fnames, key=get_modstate)
    for modstate, files in filegroups:
        logger.debug(f"{modstate} {files}")
        averaged_frames = []
        filelist = list(files)
        modfiles = refs(filelist, np.array(heads(filelist)), len(filelist))
        # TODO rewrite the above as a dict comprehension using the walrus operator (requires py3.8)
        # files_by_modstate = {modstate: refs(flist:=list(files), np.array(heads(flist)), len(flist)) for modstate, files in groupby(sorted(fnames, key=get_modstate), key=get_modstate)}

        fnames = groupby(modfiles, key=lambda x: split(x.fileuri)[-1])
        for out_fname, files in fnames:
            # TODO: consider using ImageFileCollection here instead
            frames = [
                ccdproc.CCDData.read(f.fileuri, format="fits", unit="adu")
                for f in list(files)
            ]
            outfile = join(outdir, modstate, out_fname)
            logger.debug(f"Averaging {filekey} to {outfile}")
            ccdproc.combine(frames, output_file=outfile)
            averaged_frames.append(outfile)
        averaged_frames.sort()
        logger.debug(averaged_frames)

        headers = np.array(heads(averaged_frames))
        data_key = f"reduced averaged {filekey}" + f" {modstate}"
        logger.debug(f"Inserting frames into data tree as '{data_key}'")
        asdf_file["support"][data_key] = refs(
            averaged_frames, headers, len(averaged_frames)
        )

    asdf_file.update()

    return asdf_file


def average_all(asdf_file, filekey):
    """
    Function to average VTF flat frames

    Loads specified flat frames, groups them by wavelength position and averages them, producing one
    averaged flat per wavelength step for the narrowband channels and one master flat for the
    broadband channel. Input files should all be for the same line scan and VTF channel. Reduced
    frames are saved to the output directory specified by `data_tree` and references to the files
    are added to the tree for use later in the calibration process.

    Parameters
    ----------
    data_tree : string or `Path<https://docs.python.org/3/library/pathlib.html#pathlib.Path>`_
        Path to an `AsdfFile` defining the calibration data structure, including input and output
        data directories. See :meth:`vtf-pipeline.commands.init_data_tree` for generating an
        appropriate file.

    Returns
    -------
    new_asdf : :class:`asdf.AsdfFile`
        Updated :class:`asdf.AsdfFile` containing the same information as `data_tree` plus file
        references to the averaged flat frames.

    Examples
    --------

    """
    logger = logging.getLogger(__name__)
    logger.setLevel("INFO")

    # TODO This is always going to be something that needs ensuring, so consider making a decorator for it
    if asdf_file["mode"] not in ["broadband", "narrowband"]:
        raise ValueError(
            f'Unrecognised data mode in asdf tree: {asdf_file["mode"]} '
            '- "mode" keyword should be either "broadband" or "narrowband".'
        )

    raw_dir = asdf_file["raw"]["data_dir"]
    outdir = asdf_file["support"]["data_dir"]
    logger.debug(f"{outdir}")

    frames = [
        ccdproc.CCDData.read(f.fileuri, format="fits", unit="adu")
        for f in asdf_file["raw"][filekey]
    ]
    outfile = join(outdir, f"{filekey[:-1]}.FITS")
    logger.debug(f"Averaging {filekey} to {outfile}")
    ccdproc.combine(frames, output_file=outfile)

    headers = np.array(heads([outfile]))
    data_key = f"reduced averaged {filekey}"
    logger.debug(f"Inserting frames into data tree as '{data_key}'")
    asdf_file["support"][data_key] = refs(outfile, headers, 1)

    asdf_file.update()

    return asdf_file


class HeaderTracker:
    def __init__(self, asdf_file):
        self.asdf_file = asdf_file
        rawpath = Path(asdf_file["raw"]["data_dir"])
        supportpath = Path(asdf_file["support"]["data_dir"])

        raw_fnames = list(rawpath.rglob("*.FITS"))
        support_fnames = list(supportpath.rglob("*.FITS"))

        self.raw_headers = dict(zip(raw_fnames, heads(raw_fnames)))
        self.support_frames = dict(zip(support_fnames, heads(support_fnames)))

    def files_with_keyword(self, keyword, value, raw):
        logger = logging.getLogger(__name__)
        logger.setLevel("INFO")
        headers = self.raw_headers if raw else self.support_headers
        files = []

        logger.debug(f"Checking for keyword {keyword} = {value}")
        for fname, header in headers.items():
            if keyword in header.keys() and header[keyword] == value:
                files.append(fname)
        logger.debug(f"Found {len(files)} files")

        return files

    def add_to_asdf(self, dkey, kw_dict, raw=False):
        logger = logging.getLogger(__name__)
        logger.setLevel("INFO")
        logger.debug(f"Finding files with keywords {kw_dict}")
        keybase = "raw" if raw else "support"
        allfiles = None
        for keyword in kw_dict.keys():
            files = self.files_with_keyword(keyword, kw_dict[keyword], raw)
            # filter by overlap with previous files
            if allfiles:
                allfiles = list(set(files) & set(allfiles))
            else:
                allfiles = files
        allfiles = sorted(allfiles)

        logger.debug(f"Selected {len(allfiles)} files")
        self.asdf_file[keybase][dkey] = refs(
            allfiles, np.array(heads(allfiles)), len(allfiles)
        )

        try:
            self.asdf_file.update()
        except ValueError:
            f = self.asdf_file.uri
            self.asdf_file.write_to(f)
            self.asdf_file.close()
            self.asdf_file = asdf.open(f, mode="rw")

        return self.asdf_file
