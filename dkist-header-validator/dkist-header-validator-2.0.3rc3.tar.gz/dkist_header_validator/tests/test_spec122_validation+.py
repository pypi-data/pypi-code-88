from io import BytesIO
from pathlib import Path

import numpy as np
import pytest
from astropy.io import fits

from dkist_header_validator import spec122_validator


def test_spec122(valid_spec_122_header):
    """
    Validates a fits header against the SPEC-122 schema
    Given: A valid SPEC-122 fits header
    When: Validating headers
    Then: return validated HDUList and do not raise an exception
    """
    # raises exception on failure
    spec122_validator.validate(valid_spec_122_header, extra=False)


def test_spec122_return_dictionary(valid_spec_122_header):
    """
    Validates a fits header against the SPEC-122 schema
    Given: A valid SPEC-122 fits header
    When: Validating headers
    Then: return validated dictionary and do not raise an exception
    """
    # raises exception on failure
    spec122_validator.validate(valid_spec_122_header, return_type=dict, extra=False)


def test_spec122_return_fits_header(valid_spec_122_header):
    """
    Validates a fits header against the SPEC-122 schema
    Given: A valid SPEC-122 fits header
    When: Validating headers
    Then: return validated fits.header.Header object and do not raise an exception
    """
    # raises exception on failure
    spec122_validator.validate(valid_spec_122_header, return_type=fits.header.Header, extra=False)


def test_spec122_return_BytesIO(valid_spec_122_file):
    """
    Validates a fits header against the SPEC-122 schema
    Given: A valid SPEC-122 fits header
    When: Validating headers
    Then: return validated BytesIO object and do not raise an exception
    """
    # raises exception on failure
    spec122_validator.validate(valid_spec_122_file, return_type=BytesIO, extra=False)


def test_spec122_return_HDU(valid_spec_122_file):
    """
    Validates a fits header against the SPEC-122 schema
    Given: A valid SPEC-122 fits header
    When: Validating headers
    Then: return validated PrimaryHDU object and do not raise an exception
    """
    # raises exception on failure
    spec122_validator.validate(valid_spec_122_file, return_type=fits.PrimaryHDU, extra=False)


def test_spec122_return_file(valid_spec_122_file):
    """
    Validates a fits header against the SPEC-122 schema
    Given: A valid SPEC-122 fits header
    When: Validating headers
    Then: return validated file and do not raise an exception
    """
    # raises exception on failure
    spec122_validator.validate(valid_spec_122_file, return_type=Path, extra=False)


@pytest.fixture(scope="module")
def max_headers(tmpdir_factory):
    headers = {
        "SIMPLE": True,
        "BITPIX": 16,
        "NAXIS": 3,
        "NAXIS1": 1,
        "NAXIS2": 1,
        "NAXIS3": 1,
        "BUNIT": "adu",
        "DATE": "2017-05-30T17:28:21.996",
        "DATE-OBS": "2017-05-30T00:46:13.952",
        "DATE-BGN": "2017-05-30T00:46:13.618",
        "DATE-END": "2017-05-30T00:46:13.718",
        "ORIGIN": "National Solar Observatory",
        "TELESCOP": "Daniel K. Inouye Solar Telescope",
        "OBSERVAT": "Haleakala High Altitude Observatory Site",
        "NETWORK": "NSF-DKIST",
        "INSTRUME": "VBI",
        "WAVELNTH": 430.0,
        "OBSERVER": "8QN27LDFC7EQHKK4B3WDIN4FY7VG16",
        "OBJECT": "sunspot",
        "CHECKSUM": "33989WFLS3IVX0LLYTQW3U1PT8AKFG",
        "DATASUM": "9WNO5RGILE66C2VLRJ45RQEBFL1IHU",
        "WCSAXES": 2,
        "WCSNAME": "Helioprojective",
        "CRPIX1": 2048.0,
        "CRPIX2": 2048.0,
        "CRDATE1": "2035-03-31T09:38:56.668",
        "CRDATE2": "2035-03-31T09:38:56.668",
        "CRVAL1": -304.9906422447552,
        "CRVAL2": -658.9384652992346,
        "CDELT1": 0.07,
        "CDELT2": 0.07,
        "CUNIT1": "arcsec",
        "CUNIT2": "arcsec",
        "CTYPE1": "HPLN-TAN",
        "CTYPE2": "HPLT-TAN",
        "PC1_1": 0.9231997511186788,
        "PC1_2": -0.3843204646312885,
        "PC2_1": 0.3843204646312885,
        "PC2_2": 0.9231997511186788,
        "LONPOLE": 180.0,
        "TAZIMUTH": 618993.1279034158,
        "TELEVATN": 819.9173809486648,
        "TELTRACK": "Standard Differential Rotation Tracking",
        "TELSCAN": "Raster",
        "TTBLANGL": 295548.0744481586,
        "TTBLTRCK": "fixed coude table angle",
        "DKIST001": "Manual",
        "DKIST002": "Full",
        "DKIST003": "observe",
        "DKIST004": "observe",
        "DKIST005": "9CVKTL2JWMH1LHU6G3O2UPE2SO9SUW",
        "DKIST006": "Good",
        "DKIST007": False,
        "DKIST008": 999562,
        "DKIST009": 5750,
        "DKIST010": 295882.0,
        "ID___001": "73QYTMXIMDLCNZUEBELYY6TZ8QGYKV",
        "ID___002": "YVPS4YRBSXUT9Z17Z4HRH3VIH7T6KO",
        "ID___003": "POLETJWHTN2PMM1ZPPLPWQ1KBAKIUF",
        "ID___004": "MY50PNI7QUGSKLW5D8XB9N4SDKFDZ4",
        "ID___005": "59ULPBE5GG9S93M9IG63FCWMV63WAD",
        "ID___006": "7VWWG70RLGVD9AC1J9X6Y937EJIQNV",
        "ID___007": "U8M3EWALJLU5F5B96WB4QL3SN0Z1C8",
        "ID___008": "JX3O8NXFI6FGTVZ1D7G7U8OVUWDZQL",
        "ID___009": "XV64I6WTJEJ93202Z5ZJ15MDBBBPRE",
        "ID___010": "KKWSIWJD2NKL11J03X51ZZR0C6FSHG",
        "ID___011": "OB6PYAI9XC3PTXLLY4I1LV26RTDEGS",
        "ID___012": "1XXPIDR5CEXMZ0SQ8LT3HMF83FW4HJ",
        "ID___013": "4L6XY2SM39CNQTOO4L04Y3RV0H2MTW",
        "ID___014": "UX4QYSNNFC1O99JD3TVPAGUU4XR0JB",
        "CAM__001": "ODJIY4RO6SG7T6YVHT4QVNJPVYGQW7",
        "CAM__002": "JRA5H1LSKENNLLWUZNHW9X93Z9J6G0",
        "CAM__003": 206077,
        "CAM__004": 553109.1055738949,
        "CAM__005": 931934.0145101176,
        "CAM__006": 336899.9459380526,
        "CAM__007": 450499,
        "CAM__008": 105605,
        "CAM__009": 278167,
        "CAM__010": 45681,
        "CAM__011": 882899,
        "CAM__012": 849283,
        "CAM__013": 191847,
        "CAM__014": 859469,
        "CAM__015": 208276,
        "CAM__016": 71858,
        "CAM__017": 540083,
        "CAM__018": 462616,
        "CAM__019": 763903,
        "CAM__020": 626497,
        "PAC__001": "open",
        "PAC__002": "Clear",
        "PAC__003": "Undefined",
        "PAC__004": "clear",
        "PAC__005": "186BGJFTFDVEOECZ80ENVCKM5RZL4U",
        "PAC__006": "clear",
        "PAC__007": "some string",
        "PAC__008": "FieldStop (2.8arcmin)",
        "PAC__009": "2.8arcmin",
        "PAC__010": "open",
        "PAC__011": 228814.6368968824,
        "WS___001": "CYWKXJOAROTHYHNBZOD8Z7VGJITI23",
        "WS___002": 516056.5759472652,
        "WS___003": 180,
        "WS___004": 943419.0784243871,
        "WS___005": 282679.0410177523,
        "WS___006": 348537.5489154414,
        "WS___007": 870761.4045310392,
        "CRPIX3": 15.6,
        "CRVAL3": 18.6,
        "CDELT3": 78.8,
        "CUNIT3": "deg",
        "CTYPE3": "z",
        "PC1_3": 13.5,
        "PC3_2": 13.5,
        "PC2_3": 13.5,
        "PC3_1": 13.5,
        "PC3_3": 13.5,
        "HISTORY": "Old History",
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


def test_validate_maxheaders(max_headers):
    """
    Validates a spec122 compliant header with a large number of keywords
    Given: A spec122 compliant fits file with many header keywords
    When: Validating headers
    Then: return a validated HDUList  and do not raise an exception
    """
    spec122_validator.validate(max_headers)


def test_compressed_spec122_valid(valid_compressed_spec_122_header):
    """
    Validates a compressed spec122 compliant file
    Given: A valid compressed SPEC-0122 file
    When: Validating headers
    Then: return valid HDUList and do not raise an exception
    """
    spec122_validator.validate(valid_compressed_spec_122_header)


def test_visp_spec122(valid_visp_122_header):
    """
    Validates a visp fits header against the SPEC-122 schema
    Given: A valid visp SPEC-122 fits header
    When: Validating headers
    Then: return validated HDUList and do not raise an exception
    """
    # raises exception on failure
    spec122_validator.validate(valid_visp_122_header, extra=False)


def test_datainsecondHDU(valid_spec_122_header_datainsecondHDU):
    """
    Validates headers with data stored in second HDU
    Given: A valid SPEC-122 file or with data stored in second HDU
    When: Validating headers
    Then: Raise an exception
    """
    # raises exception on failure
    spec122_validator.validate(valid_spec_122_header_datainsecondHDU, return_type=Path)
