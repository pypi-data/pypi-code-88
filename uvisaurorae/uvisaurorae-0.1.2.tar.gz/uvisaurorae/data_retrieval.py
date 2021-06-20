import bz2
import datetime as dt
import logging
import re
import uuid
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union

import importlib_resources
import numpy as np
import requests

logger = logging.getLogger(__name__)


class DataRetrievalError(Exception):
    def __init__(self, msg: Optional[str] = None):
        super(DataRetrievalError, self).__init__(msg)


def list_all_spice_kernels() -> Tuple[
    List[str], Dict[str, List[Union[str, dt.datetime]]]
]:
    """Return all SPICE kernels required to cover the Cassini Saturn tour.

    :return: A list of general SPICE kernels which are always required, and a dict containing information about
        time-dependent SPICE kernels. This dict has the keys:

            * ``kernel``: List of kernel names
            * ``start``: List of kernel start datetimes
            * ``stop``: List of kernel stop datetimes

    """
    kernel_list = importlib_resources.files("uvisaurorae.resources").joinpath(
        "spice_cassini_standard_kernels.txt"
    )  # type: ignore
    all_kernels = np.genfromtxt(kernel_list, dtype=str)

    static_kernels = []
    timed_kernels: Dict[str, List[Union[str, dt.datetime]]] = dict(
        kernel=[],
        start=[],
        stop=[],
    )
    for kernel in all_kernels:
        try:
            date_str = re.findall(r"\d{5}_\d{5}", kernel)[0]
        except IndexError:
            static_kernels.append(kernel)
        else:
            start, stop = date_str.split("_")
            timed_kernels["kernel"].append(kernel)
            timed_kernels["start"].append(dt.datetime.strptime(start, "%y%j"))
            timed_kernels["stop"].append(
                dt.datetime.strptime(stop, "%y%j") + dt.timedelta(days=1)
            )
    return static_kernels, timed_kernels


def list_required_spice_kernels(uvis_file_name: str) -> List[str]:
    """Return a list of SPICE kernels required to process a UVIS file.

    :param uvis_file_name: UVIS file name.
    :return: A list of required SPICE kernels.
    :raise uvisaurorae.data_retrieval.DataRetrievalError: If ``uvis_file_name`` does not contain a date in the
        format ``YYYY_DOY``.
    """
    try:
        date_str = re.findall(r"\d{4}_\d{3}", uvis_file_name)[0]
    except IndexError:
        raise DataRetrievalError(
            "UVIS filename does not contain date in format YYYY_DOY, required SPICE kernels could not be determined."
        )
    date = dt.datetime.strptime(date_str, "%Y_%j")
    static_kernels, timed_kernels = list_all_spice_kernels()
    intersecting_idx = np.where(
        (np.array(timed_kernels["stop"]) > date - dt.timedelta(days=1))
        & (np.array(timed_kernels["start"]) < date + dt.timedelta(days=1))
    )[0]
    required_kernels = np.append(
        static_kernels, np.array(timed_kernels["kernel"])[intersecting_idx]
    )
    return list(required_kernels)


def download_spice_kernels(
    kernels: List[str], save_dir: Path, overwrite: bool = False
) -> None:
    """Download a list of SPICE kernels from the NAIF PDS node for Cassini at
    https://naif.jpl.nasa.gov/pub/naif/pds/data/co-s_j_e_v-spice-6-v1.0/cosp_1000/data.

    :param kernels: List of SPICE kernels to download.
    :param save_dir: Path to the directory where downloaded SPICE data is to be stored.
    :param overwrite: Whether existing data files in ``save_dir`` should be re-downloaded and overwritten.
    :raise uvisaurorae.data_retrieval.DataRetrievalError: If a kernel cannot be downloaded.
    """
    naif_root = "https://naif.jpl.nasa.gov/pub/naif/pds/data/co-s_j_e_v-spice-6-v1.0/cosp_1000/data"
    for kernel in kernels:
        save_file = save_dir / kernel
        if save_file.is_file() and not overwrite:
            logger.debug(f"Found existing SPICE kernel {str(kernel)}")
            continue
        if not save_file.parent.exists():
            save_file.parent.mkdir(parents=True)

        logger.info(f"Downloading SPICE kernel {str(kernel)}")
        data = requests.get(naif_root + "/" + kernel)
        if not data.status_code == 200:
            raise DataRetrievalError(f"Download of kernel {kernel} failed.")

        with open(save_file, "wb") as f:
            f.write(data.content)
        logger.info(f"Successfully downloaded SPICE kernel {str(kernel)}")
    return


def make_metakernel(kernel_dir: Path, kernels: Optional[List[str]] = None) -> Path:
    """Create a uniquely-named SPICE metakernel in ``kernel_dir`` and return its path. If ``kernels`` is `None`, this
    function searches ``kernel_dir`` recursively and creates a metakernel containing all kernels found (except for
    other metakernels with file ending `.tm`). If ``kernels`` is given, this function creates a metakernel with all
    kernels contained in this input, whether they exist or not.

    :param kernel_dir: Main SPICE kernel directory, typically containing subdirectories for each kernel type
        (`fk`, `ck`, ...).
    :param kernels: List of kernels to include in the metakernel this function creates.
    :returns: Full path of the newly created metakernel file.
    """
    if not kernel_dir.exists():
        Path.mkdir(kernel_dir, parents=True)
    metakernel_file = kernel_dir / (uuid.uuid4().hex + ".tm")
    if kernels:
        list_kernels: List[Path] = [kernel_dir / k for k in kernels]
    else:
        list_kernels = list(kernel_dir.glob("*/*"))
    with open(metakernel_file, "w") as f:
        f.write("KPL/MK\n")
        f.write("\\begindata\n")
        f.write("PATH_VALUES=('" + str(kernel_dir) + "',)\n")
        f.write("PATH_SYMBOLS=('A',)\n")
        if list_kernels:
            f.write("KERNELS_TO_LOAD=(\n")
            for k in list_kernels:
                if ".tm" in str(k):
                    continue
                f.write("'$A/" + str(k.relative_to(kernel_dir)) + "',\n")
            f.write(")\n")
        f.write("\\begintext\n")
    return metakernel_file


def download_uvis_data(
    uvis_file_name: str,
    release_number: int,
    save_dir: Path,
    overwrite: bool = False,
    compress: bool = True,
) -> Path:
    """Download a UVIS file from the PDS UVIS repository at https://pds-rings.seti.org/holdings/volumes/COUVIS_0xxx/
    and save it in ``save_dir``. Automatically compresses the downloaded data file using
    `bzip2 <https://docs.python.org/3/library/bz2.html>`_ before saving unless ``compress`` is set to `False`. Also
    downloads the ``.LBL`` metadata file alongside the ``.DAT`` file containing the actual raw data. The metadata file is
    never compressed.

    :param uvis_file_name: Name of the UVIS file to download.
    :param release_number: Number of the UVIS PDS release this file is part of.
    :param save_dir: Path to the directory where downloaded UVIS data is to be stored.
    :param overwrite: Whether existing data files in ``save_dir`` should be re-downloaded and overwritten.
    :param compress: Whether downloaded data files should be saved with compression.
    :returns: Full path of the downloaded UVIS data file.
    """
    pds_uvis_root = "https://pds-rings.seti.org/holdings/volumes/COUVIS_0xxx/"
    try:
        date_str = re.findall(r"\d{4}_\d{3}", uvis_file_name)[0]
    except IndexError:
        raise DataRetrievalError(
            "UVIS filename does not contain date in format YYYY_DOY, cannot identify remote file location"
        )
    full_link = pds_uvis_root + "COUVIS_{:04d}/DATA/D{}".format(
        release_number, date_str
    )

    for suffix in [".LBL", ".DAT"]:
        this_file = uvis_file_name + suffix
        save_file = save_dir / this_file
        if compress and suffix == ".DAT":
            save_file = save_file.parent / (save_file.name + ".bz2")

        if save_file.is_file() and not overwrite:
            logger.debug(f"Found existing UVIS file {this_file}")
            continue
        if not save_file.parent.exists():
            save_file.parent.mkdir(parents=True)

        logger.info(f"Downloading UVIS file {this_file}")
        data = requests.get(full_link + "/" + this_file)
        if not data.status_code == 200:
            raise DataRetrievalError(f"Download of UVIS file {this_file} failed")
        if compress and suffix == ".DAT":
            logger.info(f"Compressing UVIS file {this_file}")
            with bz2.open(save_file, "wb") as f_comp:
                f_comp.write(data.content)
        else:
            with open(save_file, "wb") as f:
                f.write(data.content)
        logger.info(f"Successfully downloaded UVIS file {this_file}")
    return save_file


def download_data(
    uvis_file_name: str,
    release_number: int,
    uvis_dir: Path,
    spice_dir: Path,
    overwrite: bool = False,
    compress: bool = True,
) -> Path:
    """
    Download all data required to process the UVIS file ``uvis_file_name``. This includes the raw UVIS data file itself
    as well as the accompanying metadata file, plus all SPICE kernels needed to cover the exposure of the observation.

    :param uvis_file_name: Name of the UVIS file to download.
    :param release_number: Number of the UVIS PDS release this file is part of.
    :param uvis_dir: Path to the directory where downloaded UVIS data is to be stored.
    :param spice_dir: Path to the directory where downloaded SPICE data is to be stored.
    :param overwrite: Whether existing data files in ``save_dir`` should be re-downloaded and overwritten.
    :param compress: Whether downloaded UVIS data files should be saved with compression.
    :return: Full path of the downloaded UVIS data file.
    """
    # Get SPICE kernels
    required_kernels = list_required_spice_kernels(uvis_file_name)
    download_spice_kernels(required_kernels, spice_dir, overwrite=overwrite)

    # Get UVIS data
    uvis_file = download_uvis_data(
        uvis_file_name, release_number, uvis_dir, overwrite=overwrite, compress=compress
    )

    return uvis_file
