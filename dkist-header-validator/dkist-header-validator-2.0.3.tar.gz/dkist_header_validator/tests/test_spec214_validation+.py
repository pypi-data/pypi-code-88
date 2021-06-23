from io import BytesIO
from pathlib import Path

import numpy as np
import pytest
from astropy.io import fits

from dkist_header_validator import spec214_l0_validator
from dkist_header_validator import spec214_validator


def test_spec214(valid_spec_214_header):
    """
    Validates a fits header against the SPEC-0214 schema
    Given: A valid SPEC-0214 fits header
    When: Validating headers
    Then: return validated HDUList and do not raise an exception
    """
    # raises exception on failure
    spec214_validator.validate(valid_spec_214_header, extra=False)


def test_spec214_return_dictionary(valid_spec_214_header):
    """
    Validates a fits header against the SPEC-0214 schema
    Given: A valid SPEC-0214 fits header
    When: Validating headers
    Then: return validated dictionary and do not raise an exception
    """
    # raises exception on failure
    spec214_validator.validate(valid_spec_214_header, return_type=dict, extra=False)


def test_spec214_return_fits_header(valid_spec_214_header):
    """
    Validates a fits header against the SPEC-0214 schema
    Given: A valid SPEC-0214 fits header
    When: Validating headers
    Then: return validated fits.header.Header object and do not raise an exception
    """
    # raises exception on failure
    spec214_validator.validate(valid_spec_214_header, return_type=fits.header.Header, extra=False)


def test_spec214_return_HDU(valid_spec_214_file):
    """
    Validates a fits header against the SPEC-0214 schema
    Given: A valid SPEC-0214 fits header
    When: Validating headers
    Then: return validated fits.PrimaryHDU object and do not raise an exception
    """
    # raises exception on failure
    spec214_validator.validate(valid_spec_214_file, return_type=fits.PrimaryHDU, extra=False)


def test_spec214_return_BytesIO(valid_spec_214_file):
    """
    Validates a fits header against the SPEC-0214 schema
    Given: A valid SPEC-0214 fits header
    When: Validating headers
    Then: return validated BytesIO object and do not raise an exception
    """
    # raises exception on failure
    spec214_validator.validate(valid_spec_214_file, return_type=BytesIO, extra=False)


def test_spec214_return_file(valid_spec_214_file):
    """
    Validates a fits header against the SPEC-0214 schema
    Given: A valid SPEC-0214 fits header
    When: Validating headers
    Then: return validated file and do not raise an exception
    """
    # raises exception on failure
    spec214_validator.validate(valid_spec_214_file, return_type=Path, extra=False)


@pytest.fixture(scope="module")
def valid_spec_214_extraheaders(tmpdir_factory):
    """
    Create a dict of valid spec 214 headers to be used in successful
    header tests below.
    """
    valid_spec_214_dict_extraheaders = {
        "NAXIS": 3,
        "BITPIX": 16,
        "NAXIS1": 1,
        "NAXIS2": 1,
        "NAXIS3": 1,
        "INSTRUME": "VBI",
        "LINEWAV": 430.0,
        "CHECKSUM": "POLETJWHTN2PMM1ZPPLPWQ1KBAKIUF",
        "OBSPR_ID": "JX3O8NXFI6FGTVZ1D7G7U8OVUWDZQL",
        "ID___008": "JX3O8NXFI6FGTVZ1D7G7U8OVUWDZQL",
        "EXPER_ID": "1XXPIDR5CEXMZ0SQ8LT3HMF83FW4HJ",
        "ID___012": "1XXPIDR5CEXMZ0SQ8LT3HMF83FW4HJ",
        "PROP_ID": "4L6XY2SM39CNQTOO4L04Y3RV0H2MTW",
        "ID___013": "4L6XY2SM39CNQTOO4L04Y3RV0H2MTW",
        "ORIGIN": "National Solar Observatory",
        "DSETID": "4WBVMF7WZOBND165QRPQ",
        "FRAMEVOL": 13.2,
        "PROCTYPE": "L1",
        "RRUNID": 123456,
        "RECIPEID": 78910,
        "RINSTID": 13141516,
        "DATASUM": "E5O2YIVIP04EOEL59NGM",
        "DNAXIS": 2,
        "DNAXIS1": 2,
        "DNAXIS2": 2,
        "DTYPE1": "SPATIAL",
        "DTYPE2": "SPECTRAL",
        "DPNAME1": "4O9HXEFZ8T113T56H5XC",
        "DPNAME2": "4O9HXEFZ8T113T56ABCD",
        "DWNAME1": "XZ1AI0MXQPPQ8BFEXOQB",
        "DWNAME2": "ABCDI0MXQPPQ8BFEXOQB",
        "DUNIT1": "deg",
        "DUNIT2": "deg",
        "DAAXES": 12,
        "DEAXES": 13,
        "DINDEX13": 14,
        "DINDEX25": 14,
        "DINDEX22": 14,
        "DINDEX15": 14,
        "DINDEX19": 14,
        "DINDEX23": 14,
        "DINDEX24": 14,
        "DINDEX21": 14,
        "DINDEX14": 14,
        "DINDEX16": 14,
        "DINDEX20": 14,
        "DINDEX18": 14,
        "DINDEX17": 14,
        "LEVEL": 1,
        "FILE_ID": "AWE6T1QV0KNCFPL1JAB1",
        "WCSAXES": 1,
        "WCSNAME": "VNSNETLCAJ33XKUOFDGD",
        "CRPIX1": 13.4,
        "CRPIX2": 14.6,
        "CRPIX3": 15.6,
        "CRVAL1": 16.7,
        "CRVAL2": 18.5,
        "CRVAL3": 18.6,
        "CDELT1": 20.4,
        "CDELT2": 67.8,
        "CDELT3": 78.8,
        "CUNIT1": "deg",
        "CUNIT2": "deg",
        "CUNIT3": "deg",
        "CTYPE1": "x",
        "CTYPE2": "y",
        "CTYPE3": "z",
        "PC1_1": 13.5,
        "PC1_2": 13.5,
        "PC2_1": 13.5,
        "PC2_2": 13.5,
        "PC1_3": 13.5,
        "PC3_2": 13.5,
        "PC2_3": 13.5,
        "PC3_1": 13.5,
        "PC3_3": 13.5,
        "DATE-BEG": "2017-05-30T00:46:13.952",
        "DATE-AVG": "2017-05-30T00:46:13.952",
        "DATE-END": "2017-05-30T00:46:13.952",
        "DATE": "2017-05-30T00:46:13.952",
        "TELESCOP": "Daniel K. Inouye Solar Telescope",
        "NETWORK": "NSF-DKIST",
        "OBJECT": "quietsun",
        "BUNIT": "ct",
        "FRAMEWAV": 430.0,
        "BTYPE": "This is a data array",
        "TELAPSE": 0.46,
        "NBIN1": 12,
        "NBIN2": 13,
        "NBIN3": 13,
        "NBIN": 15,
        "SOLARNET": 1.0,
        "OBS_HDU": 1,
        "OBSGEO-X": 5327395.9638,
        "OBSGEO-Y": -1719170.4876,
        "OBSGEO-Z": 3051490.766,
        "EXTNAME": "observation",
        "POINT_ID": "4WBVMF7WZOBND165QRPQ",
        "DATEREF": "2017-05-30T00:46:13.952",
        "FILENAME": "fits_001.fits",
        "OBSRVTRY": "Haleakala High Altitude Observatory Site",
        "DATE-OBS": "2017-05-30T00:46:13.952",
        "WAVELNTH": 582.3,
        "ID___002": "fileid",
        "DKIST003": "observe",
        "DKIST004": "dark",
        "ID___004": "LKNDFPONP93HR08BG",
        "DKISTVER": "NEWESTVERSION",
        "ID___001": "NEWESTVERSION",
        "CAMERA": "CAMERA 1",
        "WAVEUNIT": -9,
        "SPECSYS": "obs frame",
        "VELOSYS": True,
        "WAVEREF": "Air",
        "WAVEMAX": 123.4,
        "WAVEMIN": 126.8,
        "TEXPOSUR": 13.2,
        "OBS_VR": 13.2,
        "NSUMEXP": 3,
        "XPOSURE": 13.2,
    }

    temp_dir = tmpdir_factory.mktemp("valid spec_214_extraheaders_temp")
    file_name = temp_dir.join("tmp_fits_file.fits")
    temp_array = np.ones((1, 1, 1), dtype=np.int16)
    valid_hdu_extraheaders = fits.PrimaryHDU(temp_array)
    # Use the valid_spec_214_dict_extraheaders from above to overwrite the default header
    for (key, value) in valid_spec_214_dict_extraheaders.items():
        valid_hdu_extraheaders.header[key] = value
    valid_hdu_list_extraheaders = fits.HDUList([valid_hdu_extraheaders])
    valid_hdu_list_extraheaders.writeto(str(file_name))
    yield {
        "valid_dkist_hdr_extraheaders.fits": Path(file_name),
        "valid_spec_214_dict_extraheaders": valid_spec_214_dict_extraheaders,
        "valid_HDUList_extraheaders": valid_hdu_list_extraheaders,
        "valid header extra headers": valid_hdu_extraheaders.header,
    }


@pytest.fixture(
    scope="function",
    params=[
        "valid_dkist_hdr_extraheaders.fits",
        "valid_spec_214_dict_extraheaders",
        "valid_HDUList_extraheaders",
        "valid header extra headers",
    ],
)
def valid_spec_214_extraheader(request, valid_spec_214_extraheaders):
    yield valid_spec_214_extraheaders[request.param]


def test_spec214_extraheaders_allowed(valid_spec_214_extraheader):
    """
    Validates a fits header against the SPEC-0214 schema
    Given: A valid SPEC-0214 fits header
    When: Validating headers
    Then: return validated HDUList and do not raise an exception
    """
    # raises exception on failure
    spec214_validator.validate(valid_spec_214_extraheader)


@pytest.fixture(scope="module")
def max_headers(tmpdir_factory):
    headers = {
        "FRIEDVAL": 3.0,
        "AO___001": 3.0,
        "LOCKSTAT": True,
        "AO___002": 0,
        "AO_LOCKX": 123.4,
        "AO___003": 123.4,
        "AO_LOCKY": 567.8,
        "AO___004": 567.8,
        "WFSLOCKX": 910.1,
        "AO___005": 910.1,
        "WFSLOCKY": 112.1,
        "AO___006": 112.1,
        "LIMBRPOS": 3.1,
        "AO___007": 3.1,
        "LIMBRATE": 4.2,
        "AO___008": 4.2,
        "CAM_ID": "OQCFZCK6LJ",
        "CAM__001": "OQCFZCK6LJ",
        "CAM_NAME": "7O766RG4TP",
        "CAM__002": "7O766RG4TP",
        "PIXDEPTH": 4,
        "CAM__003": 4,
        "FPA_EXPO": 13.2,
        "CAM__004": 13.2,
        "CAM_EXPO": 14.5,
        "CAM__005": 14.5,
        "CAM_FPS": 16.8,
        "CAM__006": 16.8,
        "CHIPDIMX": 14,
        "CAM__007": 14,
        "CHIPDIMY": 14,
        "CAM__008": 14,
        "HWBINX": 1,
        "CAM__009": 1,
        "HWBINY": 1,
        "CAM__010": 1,
        "SWBINX": 1,
        "CAM__011": 1,
        "SWBINY": 1,
        "CAM__012": 1,
        "CAM__013": 2,
        "F_IN_FPA": 12,
        "CAM__014": 12,
        "CAM__015": 1,
        "ROIN": 2,
        "CAM__016": 2,
        "ROI1ORIX": 32,
        "CAM__017": 32,
        "ROI1ORIY": 32,
        "CAM__018": 32,
        "ROI1SIZX": 32,
        "CAM__019": 32,
        "ROI1SIZy": 32,
        "CAM__020": 32,
        "ROI2ORIX": 32,
        "CAM__021": 32,
        "ROI2ORIY": 32,
        "CAM__022": 32,
        "ROI2SIZX": 32,
        "CAM__023": 32,
        "ROI2SIZY": 32,
        "CAM__024": 32,
        "ROI3ORIX": 32,
        "CAM__025": 32,
        "ROI3ORIY": 32,
        "CAM__026": 32,
        "ROI3SIZX": 32,
        "CAM__027": 32,
        "ROI3SIZY": 32,
        "CAM__028": 32,
        "ROI4ORIX": 32,
        "CAM__029": 32,
        "ROI4ORIY": 32,
        "CAM__030": 32,
        "ROI4SIZX": 32,
        "CAM__031": 32,
        "ROI4SIZY": 32,
        "CAM__032": 32,
        "DSETID": "4WBVMF7WZOBND165QRPQ",
        "FRAMEVOL": 13.2,
        "PROCTYPE": "L1",
        "RRUNID": 123456,
        "RECIPEID": 78910,
        "RINSTID": 13141516,
        "DATASUM": "E5O2YIVIP04EOEL59NGM",
        "DNAXIS": 2,
        "DNAXIS1": 2,
        "DNAXIS2": 2,
        "DNAXIS3": 2,
        "DTYPE1": "SPATIAL",
        "DTYPE2": "SPECTRAL",
        "DTYPE3": "SPECTRAL",
        "DPNAME1": "4O9HXEFZ8T113T56H5XC",
        "DPNAME2": "4O9HXEFZ8T113T56ABCD",
        "DPNAME3": "4O9HXEFZ8T113T56ABCD",
        "DWNAME1": "XZ1AI0MXQPPQ8BFEXOQB",
        "DWNAME2": "ABCDI0MXQPPQ8BFEXOQB",
        "DWNAME3": "ABCDI0MXQPPQ8BFEXOQB",
        "DUNIT1": "deg",
        "DUNIT2": "deg",
        "DUNIT3": "deg",
        "DAAXES": 12,
        "DEAXES": 13,
        "DINDEX3": 14,
        "DINDEX4": 14,
        "DINDEX5": 14,
        "DINDEX13": 14,
        "LINEWAV": 430.0,
        "FRAMEWAV": 13.2,
        "LEVEL": 1,
        "OCS_CTRL": "Manual",
        "DKIST001": "Manual",
        "DKIST002": "Full",
        "DKIST003": "observe",
        "DKIST004": "dark",
        "FIDO_CFG": "9CVKTL2JWMH1LHU6G3O2UPE2SO9SUW",
        "DKIST005": "9CVKTL2JWMH1LHU6G3O2UPE2SO9SUW",
        "DSHEALTH": "Good",
        "DKIST006": "OG4Y0R39WGGB3N0R7VIDQG7VQYD79N",
        "DKIST007": False,
        "DKIST008": 999562,
        "DKIST009": 5750,
        "LIGHTLVL": 295882.0,
        "DKIST010": 295882,
        "ID___001": "73QYTMXIMDLCNZUEBELYY6TZ8QGYKV",
        "ID___002": "YVPS4YRBSXUT9Z17Z4HRH3VIH7T6KO",
        "ID___003": "POLETJWHTN2PMM1ZPPLPWQ1KBAKIUF",
        "ID___004": "MY50PNI7QUGSKLW5D8XB9N4SDKFDZ4",
        "ID___005": "59ULPBE5GG9S93M9IG63FCWMV63WAD",
        "ID___006": "7VWWG70RLGVD9AC1J9X6Y937EJIQNV",
        "ID___007": "U8M3EWALJLU5F5B96WB4QL3SN0Z1C8",
        "ID___009": "XV64I6WTJEJ93202Z5ZJ15MDBBBPRE",
        "ID___010": "KKWSIWJD2NKL11J03X51ZZR0C6FSHG",
        "ID___011": "OB6PYAI9XC3PTXLLY4I1LV26RTDEGS",
        "ID___014": "UX4QYSNNFC1O99JD3TVPAGUU4XR0JB",
        "OBSPR_ID": "JX3O8NXFI6FGTVZ1D7G7U8OVUWDZQL",
        "ID___008": "JX3O8NXFI6FGTVZ1D7G7U8OVUWDZQL",
        "EXPER_ID": "1XXPIDR5CEXMZ0SQ8LT3HMF83FW4HJ",
        "ID___012": "1XXPIDR5CEXMZ0SQ8LT3HMF83FW4HJ",
        "PROP_ID": "4L6XY2SM39CNQTOO4L04Y3RV0H2MTW",
        "ID___013": "4L6XY2SM39CNQTOO4L04Y3RV0H2MTW",
        "FILE_ID": "2UROTJKM48",
        "SIMPLE": True,
        "BITPIX": 16,
        "NAXIS": 3,
        "NAXIS1": 1,
        "NAXIS2": 1,
        "NAXIS3": 1,
        "BUNIT": "adu",
        "DATE": "2017-05-30T17:28:21.996",
        "DATE-BEG": "2017-05-30T00:46:13.618",
        "DATE-AVG": "2017-05-30T00:46:13.618",
        "DATE-END": "2017-05-30T00:46:13.718",
        "ORIGIN": "National Solar Observatory",
        "TELESCOP": "Daniel K. Inouye Solar Telescope",
        "OBSERVAT": "Haleakala High Altitude Observatory Site",
        "NETWORK": "NSF-DKIST",
        "INSTRUME": "VBI",
        "OBJECT": "quietsun",
        "CHECKSUM": "33989WFLS3IVX0LLYTQW3U1PT8AKFG",
        "GOS_STAT": "open",
        "PAC__001": "Open",
        "LVL3STAT": "Clear",
        "PAC__002": "Clear",
        "LAMPSTAT": "On",
        "PAC__003": "On",
        "LVL2STAT": "clear",
        "PAC__004": "Clear",
        "POLANGLE": "186BGJFTFDVEOECZ80ENVCKM5RZL4U",
        "PAC__005": "186BGJFTFDVEOECZ80ENVCKM5RZL4U",
        "LVL1STAT": "clear",
        "PAC__006": "clear",
        "RETANGLE": "some string",
        "PAC__007": "some string",
        "LVL0STAT": "FieldStop (2.8arcmin)",
        "PAC__008": 332880.8796027036,
        "APERTURE": "2.8arcmin",
        "PAC__009": 2.8,
        "LGOSSTAT": "open",
        "PAC__010": "open",
        "GOS_TEMP": 228814.6368968824,
        "PAC__011": 228814.6368968824,
        "POL_NOIS": 0.001,
        "POL_SENS": 0.001,
        "WCSAXES": 3,
        "WCSAXESA": 3,
        "WCSNAME": "Helioprojective",
        "WCSNAMEA": "Equatorial",
        "CRPIX1": 2.5,
        "CRPIX1A": 2.5,
        "CRPIX2": 2.5,
        "CRPIX2A": 2.5,
        "CRPIX3": 2.5,
        "CRPIX3A": 2.5,
        "CRDATE1": "2017-05-30T00:46:13.952",
        "CRDATE1A": "2017-05-30T00:46:13.952",
        "CRDATE2": "2017-05-30T00:46:13.952",
        "CRDATE2A": "2017-05-30T00:46:13.952",
        "CRDATE3": "2017-05-30T00:46:13.952",
        "CRDATE3A": "2017-05-30T00:46:13.952",
        "CRVAL1": 1323.3,
        "CRVAL1A": 1323.3,
        "CRVAL2": 1323.3,
        "CRVAL2A": 1323.3,
        "CRVAL3": 1323.3,
        "CRVAL3A": 1323.3,
        "CDELT1": 1243.5,
        "CDELT1A": 1243.5,
        "CDELT2": 1243.5,
        "CDELT2A": 1243.5,
        "CDELT3": 1243.5,
        "CDELT3A": 1243.5,
        "CUNIT1": "deg",
        "CUNIT1A": "deg",
        "CUNIT2": "deg",
        "CUNIT2A": "deg",
        "CUNIT3": "deg",
        "CUNIT3A": "deg",
        "CTYPE1": "Spatial",
        "CTYPE2": "Spectral",
        "CTYPE3": "Temporal",
        "CTYPE1A": "Spatial",
        "CTYPE2A": "Spectral",
        "CTYPE3A": "Temporal",
        "PC1_1": 13.4,
        "PC1_2": 13.4,
        "PC1_3": 13.4,
        "PC2_1": 13.4,
        "PC2_2": 13.4,
        "PC2_3": 13.4,
        "PC3_1": 13.4,
        "PC3_2": 13.4,
        "PC3_3": 13.4,
        "PC1_1A": 13.4,
        "PC1_2A": 13.4,
        "PC1_3A": 13.4,
        "PC2_1A": 13.4,
        "PC2_2A": 13.4,
        "PC2_3A": 13.4,
        "PC3_1A": 13.4,
        "PC3_2A": 13.4,
        "PC3_3A": 13.4,
        "LONPOLE": 180.0,
        "LONPOLEA": 180.0,
        "LATPOLE": 180.0,
        "LATPOLEA": 180.0,
        "TAZIMUTH": 618993.1279034158,
        "TELEVATN": 819.9173809486648,
        "TELTRACK": "Standard Differential Rotation Tracking",
        "TELSCAN": "Raster",
        "TTBLANGL": 295548.0744481586,
        "TTBLTRCK": "fixed coude table angle",
        "WSSOURCE": "CYWKXJOAROTHYHNBZOD8Z7VGJITI23",
        "WS___001": "CYWKXJOAROTHYHNBZOD8Z7VGJITI23",
        "WIND_SPD": 516056.5759472652,
        "WS___002": 516056.5759472652,
        "WIND_DIR": 180,
        "WS___003": 180,
        "WS_TEMP": 943419.0784243871,
        "WS___004": 943419.0784243871,
        "WS_HUMID": 282679.0410177523,
        "WS___005": 282679.0410177523,
        "WS_DEWPT": 348537.5489154414,
        "WS___006": 348537.5489154414,
        "WS_PRESS": 870761.4045310392,
        "WS___007": 870761.4045310392,
        "SKYBRIGT": 70761.4045310392,
        "WS___008": 870761.4045310392,
        "DINDEX17": 14,
        "DINDEX14": 14,
        "DINDEX20": 14,
        "DINDEX25": 14,
        "DINDEX18": 14,
        "DINDEX24": 14,
        "DINDEX15": 14,
        "DINDEX23": 14,
        "DINDEX21": 14,
        "DINDEX19": 14,
        "DINDEX22": 14,
        "DINDEX16": 14,
        "BTYPE": "This is a data array",
        "TELAPSE": 0.46,
        "NBIN1": 12,
        "NBIN2": 13,
        "NBIN3": 13,
        "NBIN": 15,
        "SOLARNET": 1.0,
        "OBS_HDU": 1,
        "OBSGEO-X": 5327395.9638,
        "OBSGEO-Y": -1719170.4876,
        "OBSGEO-Z": 3051490.766,
        "EXTNAME": "observation",
        "POINT_ID": "4WBVMF7WZOBND165QRPQ",
        "DATEREF": "2017-05-30T00:46:13.952",
        "FILENAME": "fits_001.fits",
        "OBSRVTRY": "Haleakala High Altitude Observatory Site",
        "DATE-OBS": "2017-05-30T00:46:13.952",
        "WAVELNTH": 582.3,
        "DKISTVER": "NEWESTVERSION",
        "ID___001": "NEWESTVERSION",
        "CAMERA": "CAMERA 1",
        "WAVEUNIT": -9,
        "SPECSYS": "obs frame",
        "VELOSYS": True,
        "WAVEREF": "Air",
        "WAVEMAX": 123.4,
        "WAVEMIN": 126.8,
        "TEXPOSUR": 13.2,
        "OBS_VR": 13.2,
        "NSUMEXP": 3,
        "XPOSURE": 13.2,
    }

    temp_dir = tmpdir_factory.mktemp("max_headers_temp")
    file_name = temp_dir.join("tmp_fits_file.fits")
    temp_array = np.ones((1, 1, 1), dtype=np.int16)
    valid_hdu = fits.PrimaryHDU(temp_array)
    # Use the valid_header dict from above to overwrite the default header
    for (key, value) in headers.items():
        valid_hdu.header[key] = value
    valid_hdu_list = fits.HDUList([valid_hdu])
    valid_hdu_list.writeto(str(file_name))

    yield Path(str(file_name))


def test_maxheaders(max_headers):
    """
    Validates a spec214 compliant header with a large number of keywords
    Given: A spec214 compliant fits file with many header keywords
    When: Validating headers
    Then: return a valid HDUList and do not raise an exception
    """
    spec214_validator.validate(max_headers)


@pytest.fixture(scope="module")
def valid_compressed_spec_214_headers(tmpdir_factory):
    """
    Create a dict of valid compressed spec 214 headers
    to be used in successful header tests below.
    """
    valid_comp_214_dict = {
        "NAXIS": 3,
        "BITPIX": 16,
        "NAXIS1": 1,
        "NAXIS2": 1,
        "NAXIS3": 1,
        "INSTRUME": "VBI",
        "CHECKSUM": "POLETJWHTN2PMM1ZPPLPWQ1KBAKIUF",
        "OBSPR_ID": "JX3O8NXFI6FGTVZ1D7G7U8OVUWDZQL",
        "ID___008": "JX3O8NXFI6FGTVZ1D7G7U8OVUWDZQL",
        "EXPER_ID": "1XXPIDR5CEXMZ0SQ8LT3HMF83FW4HJ",
        "ID___012": "1XXPIDR5CEXMZ0SQ8LT3HMF83FW4HJ",
        "PROP_ID": "4L6XY2SM39CNQTOO4L04Y3RV0H2MTW",
        "ID___013": "4L6XY2SM39CNQTOO4L04Y3RV0H2MTW",
        "ORIGIN": "National Solar Observatory",
        "DSETID": "4WBVMF7WZOBND165QRPQ",
        "FRAMEVOL": 13.2,
        "PROCTYPE": "RAW",
        "RRUNID": 123456,
        "RECIPEID": 78910,
        "RINSTID": 13141516,
        "DATASUM": "E5O2YIVIP04EOEL59NGM",
        "DNAXIS": 2,
        "DNAXIS1": 2,
        "DNAXIS2": 2,
        "DNAXIS3": 2,
        "DTYPE1": "SPATIAL",
        "DTYPE2": "SPECTRAL",
        "DTYPE3": "SPECTRAL",
        "DPNAME1": "4O9HXEFZ8T113T56H5XC",
        "DPNAME2": "4O9HXEFZ8T113T56ABCD",
        "DPNAME3": "4O9HXEFZ8T113T56ABCD",
        "DWNAME1": "XZ1AI0MXQPPQ8BFEXOQB",
        "DWNAME2": "ABCDI0MXQPPQ8BFEXOQB",
        "DWNAME3": "ABCDI0MXQPPQ8BFEXOQB",
        "DUNIT1": "deg",
        "DUNIT2": "deg",
        "DUNIT3": "deg",
        "DAAXES": 12,
        "DEAXES": 13,
        "DINDEX3": 14,
        "DINDEX4": 14,
        "DINDEX5": 14,
        "DINDEX13": 14,
        "DINDEX21": 14,
        "DINDEX24": 14,
        "DINDEX16": 14,
        "DINDEX14": 14,
        "DINDEX15": 14,
        "DINDEX20": 14,
        "DINDEX17": 14,
        "DINDEX19": 14,
        "DINDEX25": 14,
        "DINDEX23": 14,
        "DINDEX22": 14,
        "DINDEX18": 14,
        "LINEWAV": 430.0,
        "LEVEL": 1,
        "FILE_ID": "AWE6T1QV0KNCFPL1JAB1",
        "WCSAXES": 1,
        "WCSNAME": "VNSNETLCAJ33XKUOFDGD",
        "CRPIX1": 13.4,
        "CRPIX2": 14.6,
        "CRPIX3": 15.6,
        "CRVAL1": 16.7,
        "CRVAL2": 18.5,
        "CRVAL3": 18.6,
        "CDELT1": 20.4,
        "CDELT2": 67.8,
        "CDELT3": 78.8,
        "CUNIT1": "deg",
        "CUNIT2": "deg",
        "CUNIT3": "deg",
        "CTYPE1": "x",
        "CTYPE2": "y",
        "CTYPE3": "z",
        "PC1_1": 13.5,
        "PC1_2": 13.5,
        "PC2_1": 13.5,
        "PC2_2": 13.5,
        "PC1_3": 13.5,
        "PC3_2": 13.5,
        "PC2_3": 13.5,
        "PC3_1": 13.5,
        "PC3_3": 13.5,
        "DATE-BEG": "2017-05-30T00:46:13.952",
        "DATE-END": "2017-05-30T00:46:13.952",
        "DATE-AVG": "2017-05-30T00:46:13.952",
        "FRAMEWAV": 430.0,
        "DATE": "2017-05-30T00:46:13.952",
        "TELESCOP": "Daniel K. Inouye Solar Telescope",
        "NETWORK": "NSF-DKIST",
        "OBJECT": "quietsun",
        "BUNIT": "ct",
        "OBSERVAT": "NSO",
        "BTYPE": "This is a data array",
        "TELAPSE": 0.46,
        "NBIN1": 12,
        "NBIN2": 13,
        "NBIN3": 13,
        "NBIN": 15,
        "SOLARNET": 1.0,
        "OBS_HDU": 1,
        "OBSGEO-X": 5327395.9638,
        "OBSGEO-Y": -1719170.4876,
        "OBSGEO-Z": 3051490.766,
        "EXTNAME": "observation",
        "POINT_ID": "4WBVMF7WZOBND165QRPQ",
        "DATEREF": "2017-05-30T00:46:13.952",
        "FILENAME": "fits_001.fits",
        "OBSRVTRY": "Haleakala High Altitude Observatory Site",
        "DATE-OBS": "2017-05-30T00:46:13.952",
        "WAVELNTH": 582.3,
        "ID___002": "fileid",
        "DKIST003": "observe",
        "DKIST004": "dark",
        "ID___004": "LKNDFPONP93HR08BG",
        "DKISTVER": "NEWESTVERSION",
        "ID___001": "NEWESTVERSION",
        "CAMERA": "CAMERA 1",
        "WAVEUNIT": -9,
        "SPECSYS": "obs frame",
        "VELOSYS": True,
        "WAVEREF": "Air",
        "WAVEMAX": 123.4,
        "WAVEMIN": 126.8,
        "TEXPOSUR": 13.2,
        "OBS_VR": 13.2,
        "NSUMEXP": 3,
        "XPOSURE": 13.2,
    }

    temp_dir = tmpdir_factory.mktemp("valid comp_214_headers_temp")
    file_name = temp_dir.join("tmp__comp_fits_file.fits")
    temp_array = np.ones((1, 1, 1), dtype=np.int16)
    valid_comp_hdu = fits.PrimaryHDU(temp_array)
    # Use the valid_spec_214_dict from above to overwrite the default header
    for (key, value) in valid_comp_214_dict.items():
        valid_comp_hdu.header[key] = value
    valid_comp_hdu_list = fits.HDUList([valid_comp_hdu])
    valid_comp_hdu_list.writeto(str(file_name))

    yield {
        "valid_compressed_hdr.fits.fz": Path(file_name),
    }


@pytest.fixture(
    scope="function",
    params=[
        "valid_compressed_hdr.fits.fz",
    ],
)
def valid_compressed_spec_214_header(request, valid_compressed_spec_214_headers):
    yield valid_compressed_spec_214_headers[request.param]


def test_compressed_spec214(valid_compressed_spec_214_header):
    """
    Validates a compressed spec214 compliant file
    Given: A valid compressed SPEC-0214 file
    When: Validating headers
    Then: return validated HDUList and do not raise an exception
    """
    spec214_validator.validate(valid_compressed_spec_214_header)


def test_validate_datainsecondHDU(valid_spec_214_header_datainsecondHDU):
    """
    Validates headers with data stored in second HDU
    Given: A valid SPEC-214 file or with data stored in second HDU
    When: Validating headers
    Then: Raise an exception
    """
    # raises exception on failure
    spec214_validator.validate(valid_spec_214_header_datainsecondHDU, return_type=Path)


@pytest.fixture(scope="module")
def valid_l0_spec_214_headers(tmpdir_factory):
    """
    Create a dict of valid l0 spec 214 headers
    to be used in successful header tests below.
    """
    valid_l0_214_dict = {
        "NAXIS": 3,
        "BITPIX": 16,
        "NAXIS1": 1,
        "NAXIS2": 1,
        "NAXIS3": 1,
        "BUNIT": "ct",
        "INSTRUME": "VBI",
        "ID___008": "JX3O8NXFI6FGTVZ1D7G7U8OVUWDZQL",
        "PROP_ID": "4L6XY2SM39CNQTOO4L04Y3RV0H2MTW",
        "OBSPR_ID": "JX3O8NXFI6FGTVZ1D7G7U8OVUWDZQL",
        "DKIST004": "dark",
        "WAVELNTH": 582.3,
        "LINEWAV": 582.3,
        "EXPER_ID": "1XXPIDR5CEXMZ0SQ8LT3HMF83FW4HJ",
        "ID___012": "1XXPIDR5CEXMZ0SQ8LT3HMF83FW4HJ",
        "OBJECT": "quietsun",
        "ORIGIN": "National Solar Observatory",
        "DKISTVER": "NEWESTVERSION",
        "OBSERVAT": "Haleakala High Altitude Observatory Site",
        "DKIST003": "observe",
        "DATASUM": "E5O2YIVIP04EOEL59NGM",
        "OBSRVTRY": "Haleakala High Altitude Observatory Site",
        "ID___002": "fileid",
        "TELESCOP": "Daniel K. Inouye Solar Telescope",
        "ID___013": "4L6XY2SM39CNQTOO4L04Y3RV0H2MTW",
        "DATE-OBS": "2017-05-30T00:46:13.952",
        "NETWORK": "NSF-DKIST",
        "DATE-BEG": "2017-05-30T00:46:13.952",
        "DATE": "2017-05-30T00:46:13.952",
        "CHECKSUM": "POLETJWHTN2PMM1ZPPLPWQ1KBAKIUF",
        "WCSAXES": 1,
        "WCSNAME": "VNSNETLCAJ33XKUOFDGD",
        "CRPIX1": 13.4,
        "CRPIX2": 14.6,
        "CRPIX3": 15.6,
        "CRDATE1": "2017-05-30T00:46:13.952",
        "CRDATE2": "2017-05-30T00:46:13.952",
        "CRDATE3": "2017-05-30T00:46:13.952",
        "CRVAL1": 16.7,
        "CRVAL2": 18.5,
        "CRVAL3": 18.6,
        "CDELT1": 20.4,
        "CDELT2": 67.8,
        "CDELT3": 78.8,
        "CUNIT1": "deg",
        "CUNIT2": "deg",
        "CUNIT3": "deg",
        "CTYPE1": "x",
        "CTYPE2": "y",
        "CTYPE3": "z",
        "PC1_1": 13.5,
        "PC1_2": 13.5,
        "PC2_1": 13.5,
        "PC2_2": 13.5,
        "PC1_3": 13.5,
        "PC3_2": 13.5,
        "PC2_3": 13.5,
        "PC3_1": 13.5,
        "PC3_3": 13.5,
        "LONPOLE": 180.0,
        "LATPOLE": 180.0,
        "TAZIMUTH": 618993.1279034158,
        "TELEVATN": 819.9173809486648,
        "TELTRACK": "Standard Differential Rotation Tracking",
        "TELSCAN": "Raster",
        "TTBLANGL": 295548.0744481586,
        "TTBLTRCK": "fixed coude table angle",
        "ELEV_ANG": 819.9173809486648,
        "ID___001": "NEWESTVERSION",
        "CAMERA": "CAMERA 1",
        "TEXPOSUR": 13.2,
        "NSUMEXP": 3,
        "XPOSURE": 13.2,
        "CAM__002": "CAMERA 1",
        "CAM__005": 126.3,
        "CAM__004": 13.2,
        "CAM__014": 3,
        "FILE_ID": "RANDOMSTRING",
    }

    temp_dir = tmpdir_factory.mktemp("valid l0_214_headers_temp")
    file_name = temp_dir.join("tmp__l0_fits_file.fits")
    temp_array = np.ones((1, 1, 1), dtype=np.int16)
    valid_l0_hdu = fits.PrimaryHDU(temp_array)
    # Use the valid_spec_214_dict from above to overwrite the default header
    for (key, value) in valid_l0_214_dict.items():
        valid_l0_hdu.header[key] = value
    valid_l0_hdu_list = fits.HDUList([valid_l0_hdu])
    valid_l0_hdu_list.writeto(str(file_name))

    yield {
        "valid_l0_hdr.fits": Path(file_name),
        "valid_l0_spec_214_dict": valid_l0_214_dict,
        "valid_l0_HDUList": valid_l0_hdu_list,
        "valid l0 header": valid_l0_hdu.header,
    }


@pytest.fixture(
    scope="function",
    params=[
        "valid_l0_hdr.fits",
        "valid_l0_spec_214_dict",
        "valid_l0_HDUList",
        "valid l0 header",
    ],
)
def valid_l0_spec_214_header(request, valid_l0_spec_214_headers):
    yield valid_l0_spec_214_headers[request.param]


def test_spec214_level0(valid_l0_spec_214_header):
    """
    Validates a fits header against the 'Level 0' SPEC-0214 schema
    Given: A valid L0 SPEC-0214 fits header
    When: Validating headers
    Then: return validated HDUList and do not raise an exception
    """
    # raises exception on failure
    spec214_l0_validator.validate(valid_l0_spec_214_header, extra=False)
