"""
Dark frame reduction

Average collected dark frames as appropriate to reduce to the smallest number required to calibrate
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

from os.path import join

import asdf

from vtfcal.utils import HeaderTracker


def init_data_tree(indir, legacy_spec0122=False):
    """
    Initiate a set of data trees for describing the calibration data structure.

    Creates and saves an :class:`~asdf.AsdfFile` for each VTF camera and initialises them with
    `inidir` and `outdir` as input and output directories, respectively. Also defines for each file
    whether the data are broadband or narrowband images.

    \b
    Parameters
    ----------
    indir : str or :class:`pathlib.Path`
        Directory in which raw input is stored.

    \b
    outdir : str or :class:`pathlib.Path`
        Directory to which intermediate and final output files will be saved.
    """

    channels = [("bb", "broadband"), ("nb1", "narrowband1"), ("nb2", "narrowband2")]

    for short, long_ in channels:
        tree = {
            # Would use pathlib for these but asdf can't represent it
            "raw": {"data_dir": join(indir, "raw")},
            "support": {"data_dir": join(indir, "support", long_)},
            "processed": {"data_dir": join(indir, "processed", long_)},
            "polarization": {"data_dir": join(indir, "raw", "polarization")},
            "plots": join(indir, "plots", long_),
            "mode": "broadband" if short == "bb" else "narrowband",
            "speckle": {"data_dir": join(indir, "raw", "speckle")},
        }

        f = join(indir, f"{short}_data_tree")
        asdf_file = asdf.AsdfFile(tree, uri=f)
        headers = HeaderTracker(asdf_file)
        asdf_file = headers.add_to_asdf("darks", {"DKIST003": "dark"}, raw=True)
        asdf_file = headers.add_to_asdf("flats", {"DKIST003": "gain"}, raw=True)
        # Header key indicating channel isn't in the format I'm using for tracking files
        chankey = short.upper().replace("1", "+").replace("2", "-")
        # for dkey, head_kw in zip(["flats", "data"], ["gain", "observe"]):
        dkey = "data"
        head_kw = "observe"
        for m in range(4):
            search_keys = (
                {"VTF__002": chankey, "VTF_031": m, "DKIST003": head_kw}
                if legacy_spec0122
                else {"VTF_002": chankey, "VTF__021": m, "DKIST003": head_kw}
            )
            asdf_file = headers.add_to_asdf(
                f"{dkey} modstate{m}", search_keys, raw=True
            )
