import bz2
import datetime as dt
import logging
import re
import tempfile
from pathlib import Path
from typing import Any, Dict, Optional, Tuple, Union

import importlib_resources
import numpy as np
import spiceypy as spice
from astropy.io import fits
from scipy.interpolate import interp1d

from uvisaurorae import calibration

logger = logging.getLogger(__name__)


class UVISDataError(Exception):
    def __init__(self, msg: Optional[str] = None):
        super(UVISDataError, self).__init__(msg)


# Load leap second kernel if not loaded already
lsk = importlib_resources.files("uvisaurorae.resources").joinpath("naif0012.tls")  # type: ignore
try:
    spice.kinfo(str(lsk))
except spice.stypes.SpiceyError:
    spice.furnsh(str(lsk))

uvis_cal = calibration.UVISCalibrator()


def read_metadata(label_file: Union[Path, str]) -> Dict[str, Any]:
    """
    Read some metadata from a UVIS label file.

    :param label_file: Path to the label file.
    :return: Dictionary with some important or useful metadata items (``FILE_RECORDS``, ``START_TIME``, ``STOP_TIME``,
        ``INTEGRATION_DURATION``, ``SLIT_STATE``, ``CORE_ITEMS``, ``UL_CORNER_LINE``, ``UL_CORNER_BAND``,
        ``LR_CORNER_LINE``, ``LR_CORNER_BAND``, ``BAND_BIN``, ``LINE_BIN``).
    :raise UVISDataError: If the label file does not contain all required metadata items or the item
        ``INTEGRATION_DURATION`` is not a number.
    """
    metalabels = [
        "FILE_RECORDS",
        "START_TIME",
        "STOP_TIME",
        "INTEGRATION_DURATION",
        "SLIT_STATE",
        "CORE_ITEMS",
        "UL_CORNER_LINE",
        "UL_CORNER_BAND",
        "LR_CORNER_LINE",
        "LR_CORNER_BAND",
        "BAND_BIN",
        "LINE_BIN",
    ]

    metadata = dict()

    with open(label_file, "r") as lf:
        line = "true"
        while line:
            if "=" not in line:
                line = lf.readline().strip("\n")
                continue
            for label in metalabels:
                if label in line:
                    value = line.split("=")[-1].replace("<SECOND>", "")
                    value = re.sub(r'[\n="()]', "", value)
                    try:
                        metadata[label] = (
                            float(value)
                            if label == "INTEGRATION_DURATION"
                            else int(value)
                        )
                    except ValueError:
                        metadata[label] = value  # type: ignore
                    break
            line = lf.readline().strip("\n")

    missing = [i for i in metalabels if i not in [*metadata]]
    if len(missing):
        raise UVISDataError(f"Could not load required metadata items {missing}.")
    if type(metadata["INTEGRATION_DURATION"]) != float:
        raise UVISDataError("INTEGRATION_DURATION is not a number.")

    for item in ["START_TIME", "STOP_TIME"]:
        metadata[item] = dt.datetime.strptime(
            metadata[item].strip(), "%Y-%jT%H:%M:%S.%f"  # type: ignore
        )

    metadata["CORE_ITEMS"] = [int(iii) for iii in metadata["CORE_ITEMS"].split(", ")]  # type: ignore

    return metadata


def load_integrated_data(
    data_file: Union[Path, str],
    label_file: Union[Path, str],
    integration_method: str = "GUSTIN_2016",
) -> Tuple[Dict[str, Any], np.ndarray, np.ndarray]:
    """
    Load calibrated and wavelength-integrated UVIS data.

    :param data_file: Path to the compressed or uncompressed UVIS data file.
    :param label_file: Path to the accompanying label file.
    :param integration_method: Which method to use for wavelength integration - the only sensible option for auroral
        imagery is currently ``"GUSTIN_2016"``, referring to the integration method described in
        http://dx.doi.org/10.1016/j.icarus.2015.12.048.
    :return: Dictionary containing some metadata scraped from the label file, 1-D array listing the exposure start time
        of each record, 2-D array of shape (# of records, # of pixels per record).
    """
    metadata = read_metadata(label_file)
    et_times = np.array(
        [
            spice.datetime2et(metadata["START_TIME"])
            + i * metadata["INTEGRATION_DURATION"]
            for i in range(metadata["FILE_RECORDS"] + 1)
        ]
    )

    slit_width = 1 if "LOW" in metadata["SLIT_STATE"] else 2

    window_def = [
        metadata["UL_CORNER_BAND"],
        metadata["UL_CORNER_LINE"],
        metadata["LR_CORNER_BAND"],
        metadata["LR_CORNER_LINE"],
    ]
    bin_def = [metadata["BAND_BIN"], metadata["LINE_BIN"]]

    wavelength, calibration_matrix, _ = uvis_cal.get_interpolated_calibration(
        et_times[0], slit_width, window_def, bin_def
    )

    # Get size of array
    data_size = metadata["CORE_ITEMS"]
    if len(data_size) != 3:
        raise UVISDataError("CORE_ITEMS indicates data is not 3D.")
    if not data_size[-1] == metadata["FILE_RECORDS"]:
        raise UVISDataError("FILE_RECORDS does not fit array dimensions")

    # Get valid band indices
    band_min = 0
    band_max = int(
        np.ceil(
            (metadata["LR_CORNER_BAND"] - metadata["UL_CORNER_BAND"] + 1)
            / metadata["BAND_BIN"]
        )
    )

    # Data starts at UL_CORNER, and fills LR_CORNER+1-UL_CORNER following pixels
    line_min = metadata["UL_CORNER_LINE"]
    line_num = int(
        np.ceil(
            (metadata["LR_CORNER_LINE"] - metadata["UL_CORNER_LINE"] + 1)
            / metadata["LINE_BIN"]
        )
    )
    line_max = line_min + line_num

    # Read data file
    data_fmt = f">({data_size[-1]},{data_size[-2]},{data_size[-3]})u2"
    if str(data_file).endswith(".bz2"):
        with bz2.open(str(data_file), "rb") as f_comp:
            content = f_comp.read()
        with tempfile.TemporaryDirectory() as temp_dir:
            tmp_file = Path(temp_dir) / "tmp.dat"
            with open(tmp_file, "wb") as f:
                f.write(content)
            data = np.squeeze(np.fromfile(tmp_file, dtype=data_fmt, count=-1))
    else:
        data = np.squeeze(np.fromfile(str(data_file), dtype=data_fmt, count=-1))
    valid_data = data[:, line_min:line_max, band_min:band_max]

    # Perform calibration
    valid_data = np.array(valid_data, dtype=np.float32)
    valid_data /= metadata["INTEGRATION_DURATION"]
    calibrated_data = valid_data * np.tile(
        calibration_matrix, (valid_data.shape[0], 1, 1)
    )

    # Integrate over desired wavelength range (A)
    if integration_method == "GUSTIN_2016":
        min_lim = 1550
        max_lim = 1620
    elif integration_method == "DAYGLOW":
        min_lim = 1250
        max_lim = 1550
    elif integration_method == "REFL_SUNLIGHT":
        min_lim = 1650
        max_lim = 1800
    else:
        raise UVISDataError("Unknown integration method.")
    # Interpolate to find out which wavelength bins we need
    f_int = interp1d(wavelength, np.arange(len(wavelength)))
    min_bin = f_int(min_lim)
    max_bin = f_int(max_lim)
    # For each bin, find out which fraction overlaps with the desired wavelength range
    bin_numbers = np.arange(len(wavelength))
    left = bin_numbers - 0.5
    left[left < min_bin] = min_bin
    right = bin_numbers + 0.5
    right[right > max_bin] = max_bin
    multipliers = right - left
    multipliers[multipliers < 0] = 0
    multipliers = np.tile(multipliers, tuple(calibrated_data.shape[:-1]) + (1,))

    # Get band width of each band bin (linear scale)
    band_diff = np.mean(np.diff(wavelength))

    integrated_data = np.sum(calibrated_data * multipliers * band_diff, axis=-1)

    if integration_method == "GUSTIN_2016":
        # Following Gustin 2016 Jupiter paper, conversion factor to get full UV range 700-1700 A
        integrated_data *= 8.1

    # Find bad records and pixels and nan them
    is_bad_record = (
        np.nansum(integrated_data <= 0, axis=1) / integrated_data.shape[1]
    ) > 0.8
    if is_bad_record.any():
        for i in np.where(is_bad_record)[0]:
            integrated_data[i, :] = np.nan

    is_bad_pixel = (
        np.nansum(integrated_data <= 0, axis=0) / integrated_data.shape[0]
    ) > 0.8
    if is_bad_pixel.any():
        for i in np.where(is_bad_pixel)[0]:
            integrated_data[:, i] = np.nan

    return metadata, et_times, integrated_data


def set_fits_header(
    hdr: fits.PrimaryHDU.header,
    creator: str,
    metadata: Dict[str, Any],
    integration_method: str,
) -> str:
    """
    Set the header of a FITS file with metadata information.

    :param hdr: FITS header to set.
    :type hdr: FITS header
    :param creator: Name of the file creator.
    :param metadata: Metadata dictionary scraped from a UVIS PDS label file.
    :param integration_method: Name of the integration method used.
    :return: Name of the hemisphere on which the projection is located.
    """
    time_fmt = "%Y-%m-%d %H:%M:%S"
    hdr.set(
        "DATE",
        dt.datetime.now(dt.timezone.utc).strftime(time_fmt),
        "Creation UTC of FITS header",
    )
    hdr.set("CREATOR", creator, "Creator of this FITS file")
    hdr.set(
        "STARTUTC",
        metadata["START_TIME"].strftime(time_fmt),
        "Start time of observation",
    )
    hdr.set(
        "STOPUTC", metadata["STOP_TIME"].strftime(time_fmt), "End time of observation"
    )
    hdr.set(
        "TOTALEXP",
        metadata["TOTAL_EXPOSURE"],
        "Total exposure time of the observation (s)",
    )
    hdr.set(
        "RECORDS",
        metadata["FILE_RECORDS"],
        "Number of file records included in this image",
    )
    pos, _ = spice.spkpos(
        "CASSINI",
        spice.datetime2et(metadata["START_TIME"]),
        "CASSINI_KSMAG",
        "NONE",
        "SATURN",
    )
    hemisphere = "North" if pos[-1] > 0 else "South"
    hdr.set("HEMSPH", hemisphere, "Observed hemisphere")
    hdr.set("INTMET", integration_method, "Integration method")
    hdr.set("AXIS1", "-90..90", "Latitude axis definition")
    hdr.set("AXIS2", "0..360", "Longitude axis definition")
    return hemisphere


def save_to_fits(
    save_dir: Union[str, Path],
    proj: np.ndarray,
    proj_min_angles: np.ndarray,
    creator: str,
    metadata: Dict[str, Any],
    integration_method: str = "GUSTIN_2016",
) -> Tuple[Path, str]:
    """
    Save a UVIS projection to a FITS file.

    :param save_dir: Path to target directory.
    :param proj: Projection array.
    :param proj_min_angles: Minimum Cassini elevation angle array.
    :param creator: Name of the file creator.
    :param metadata: Metadata dictionary scraped from a UVIS PDS label file.
    :param integration_method: Name of the integration method used.
    :return: Path to saved FITS file, name of the hemisphere on which the projection is located.
    """
    save_dir = Path(save_dir)
    if not save_dir.exists():
        save_dir.mkdir(parents=True)

    hdu = fits.PrimaryHDU(proj)
    hdu_angles = fits.ImageHDU(proj_min_angles)
    hemisphere = set_fits_header(hdu.header, creator, metadata, integration_method)

    time_fmt = "%Y_%jT%H_%M_%S"
    file_name = save_dir / (metadata["START_TIME"].strftime(time_fmt) + ".fits")

    hdul = fits.HDUList([hdu, hdu_angles])
    hdul.writeto(file_name, overwrite=True)
    logger.info(f"Successfully saved file {file_name}")
    return file_name, hemisphere
