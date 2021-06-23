from io import BytesIO
from pathlib import Path

import pytest
from astropy.io import fits

from dkist_header_validator import spec214_validator
from dkist_header_validator.exceptions import ValidationException


def test_translate_spec214_to_spec214_l0(valid_spec_214_header):
    """
    Validates and tries to translate a fits header against the SPEC-0214 schema
    Given: A valid SPEC-0214 fits header
    When: Validating headers
    Then: return translated HDUList and do not raise an exception
    """
    # raises exception on failure
    spec214_validator.validate_and_translate_to_214_l0(valid_spec_214_header)


def test_translate_spec214_to_spec214(valid_spec_214_header):
    """
    Validates and tries to translate a fits header against the SPEC-0214 schema
    Given: A valid SPEC-0214 fits header
    When: Validating headers
    Then: return translated HDUList and do not raise an exception
    """
    # raises exception on failure
    spec214_validator.validate_and_translate_to_214(valid_spec_214_header)


def test_translate_spec214_to_214_l0_return_dictionary(valid_spec_214_header):
    """
    Validates and tries to translate a fits header against the SPEC-0214 schema
    Given: A valid SPEC-0214 fits header
    When: Validating headers
    Then: return translated dictionary and do not raise an exception
    """
    # raises exception on failure
    spec214_validator.validate_and_translate_to_214_l0(valid_spec_214_header, return_type=dict)


def test_translate_spec214_to_214_return_dictionary(valid_spec_214_header):
    """
    Validates and tries to translate a fits header against the SPEC-0214 schema
    Given: A valid SPEC-0214 fits header
    When: Validating headers
    Then: return translated dictionary and do not raise an exception
    """
    # raises exception on failure
    spec214_validator.validate_and_translate_to_214(valid_spec_214_header, return_type=dict)


def test_translate_spec214_to_214_l0_return_fits_header(valid_spec_214_header):
    """
    Validates and tries to translate a fits header against the SPEC-0214 schema
    Given: A valid SPEC-0214 fits header
    When: Validating headers
    Then: return translated fits.header.Header object and do not raise an exception
    """
    # raises exception on failure
    spec214_validator.validate_and_translate_to_214_l0(
        valid_spec_214_header, return_type=fits.header.Header
    )


def test_translate_spec214_to_214_return_fits_header(valid_spec_214_header):
    """
    Validates and tries to translate a fits header against the SPEC-0214 schema
    Given: A valid SPEC-0214 fits header
    When: Validating headers
    Then: return translated fits.header.Header object and do not raise an exception
    """
    # raises exception on failure
    spec214_validator.validate_and_translate_to_214(
        valid_spec_214_header, return_type=fits.header.Header
    )


def test_translate_spec214_to_214_l0_return_HDU(valid_spec_214_file):
    """
    Validates and tries to translate a fits header against the SPEC-0214 schema
    Given: A valid SPEC-0214 fits header
    When: Validating headers
    Then: return translated fits.PrimaryHDU object and do not raise an exception
    """
    # raises exception on failure
    spec214_validator.validate_and_translate_to_214_l0(
        valid_spec_214_file, return_type=fits.PrimaryHDU
    )


def test_translate_spec214_to_214_return_HDU(valid_spec_214_file):
    """
    Validates and tries to translate a fits header against the SPEC-0214 schema
    Given: A valid SPEC-0214 fits header
    When: Validating headers
    Then: return translated fits.PrimaryHDU object and do not raise an exception
    """
    # raises exception on failure
    spec214_validator.validate_and_translate_to_214(
        valid_spec_214_file, return_type=fits.PrimaryHDU
    )


def test_translate_spec214_to_214_l0_return_BytesIO(valid_spec_214_file):
    """
    Validates and tries to translate a fits header against the SPEC-0214 schema
    Given: A valid SPEC-0214 fits header
    When: Validating headers
    Then: return translated BytesIO object and do not raise an exception
    """
    # raises exception on failure
    spec214_validator.validate_and_translate_to_214_l0(valid_spec_214_file, return_type=BytesIO)


def test_translate_spec214_to_214_return_BytesIO(valid_spec_214_file):
    """
    Validates and tries to translate a fits header against the SPEC-0214 schema
    Given: A valid SPEC-0214 fits header
    When: Validating headers
    Then: return translated BytesIO object and do not raise an exception
    """
    # raises exception on failure
    spec214_validator.validate_and_translate_to_214(valid_spec_214_file, return_type=BytesIO)


def test_and_translate_spec214_to_214_l0_return_file(valid_spec_214_file):
    """
    Validates and tries to translate a fits header against the SPEC-0214 schema
    Given: A valid SPEC-0214 fits header
    When: Validating headers
    Then: return translated file object and do not raise an exception
    """
    # raises exception on failure
    spec214_validator.validate_and_translate_to_214_l0(valid_spec_214_file, return_type=Path)


def test_and_translate_spec214_to_214_return_file(valid_spec_214_file):
    """
    Validates and tries to translate a fits header against the SPEC-0214 schema
    Given: A valid SPEC-0214 fits header
    When: Validating headers
    Then: return translated file object and do not raise an exception
    """
    # raises exception on failure
    spec214_validator.validate_and_translate_to_214(valid_spec_214_file, return_type=Path)


def test_translate_to_214_l0_toomanyHDUs(valid_spec_214_header_toomanyHDUs):
    """
    Validates headers with too many (more than 2) HDUs
    Given: A valid SPEC-214 file or HDUList with more than two headers
    When: Validating and translating headers
    Then: Raise an exception
    """
    # raises exception on failure
    with pytest.raises(ValidationException):
        spec214_validator.validate_and_translate_to_214_l0(valid_spec_214_header_toomanyHDUs)


def test_translate_to_214_toomanyHDUs(valid_spec_214_header_toomanyHDUs):
    """
    Validates headers with too many (more than 2) HDUs
    Given: A valid SPEC-214 file or HDUList with more than two headers
    When: Validating and translating headers
    Then: Raise an exception
    """
    # raises exception on failure
    with pytest.raises(ValidationException):
        spec214_validator.validate_and_translate_to_214(valid_spec_214_header_toomanyHDUs)


def test_translate_to_214_l0_datainsecondHDU(valid_spec_214_header_datainsecondHDU):
    """
    Validates headers with data stored in second HDU
    Given: A valid SPEC-214 file or with data stored in second HDU
    When: Validating and translating headers
    Then: Raise an exception
    """
    # raises exception on failure
    spec214_validator.validate_and_translate_to_214_l0(
        valid_spec_214_header_datainsecondHDU, return_type=Path
    )


def test_translate_to_214_datainsecondHDU(valid_spec_214_header_datainsecondHDU):
    """
    Validates headers with data stored in second HDU
    Given: A valid SPEC-214 file or with data stored in second HDU
    When: Validating and translating headers
    Then: Raise an exception
    """
    # raises exception on failure
    spec214_validator.validate_and_translate_to_214(
        valid_spec_214_header_datainsecondHDU, return_type=Path
    )


@pytest.fixture(scope="module")
def spec_214_headers(tmpdir_factory):
    """
    Create a dict of valid spec 214 headers to be used in successful
    header tests below.
    """
    spec_214_dict = {
        "NAXIS": 3,
        "BITPIX": 16,
        "NAXIS1": 1,
        "NAXIS2": 1,
        "NAXIS3": 1,
        "INSTRUME": "VBI",
        "LINEWAV": 430.0,
        "CHECKSUM": "POLETJWHTN2PMM1ZPPLPWQ1KBAKIUF",
        "OBSPR_ID": "JX3O8NXFI6FGTVZ1D7G7U8OVUWDZQL",
        "EXPER_ID": "1XXPIDR5CEXMZ0SQ8LT3HMF83FW4HJ",
        "PROP_ID": "4L6XY2SM39CNQTOO4L04Y3RV0H2MTW",
        "ORIGIN": "National Solar Observatory",
        "DSETID": "4WBVMF7WZOBND165QRPQ",
        "FRAMEVOL": 13.2,
        "PROCTYPE": "L1",
        "RRUNID": 123456,
        "RECIPEID": 78910,
        "RINSTID": 13141516,
        "DATASUM": "E5O2YIVIP04EOEL59NGM",
        "DNAXIS": 3,
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
        "HISTORY": "Old History",
        "COMMENT": "A comment",
        "DKISTVER": "NEWESTVERSION",
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

    temp_dir = tmpdir_factory.mktemp("spec_214_headers_temp")
    file_name = temp_dir.join("tmp_fits_file.fits")
    temp_array = np.ones((1, 1, 1), dtype=np.int16)
    valid_hdu = fits.PrimaryHDU(temp_array)
    # Use the spec_214_dict from above to overwrite the default header
    for (key, value) in spec_214_dict.items():
        valid_hdu.header[key] = value
    valid_hdu_list = fits.HDUList([valid_hdu])
    valid_hdu_list.writeto(str(file_name))
    yield {
        "spec_214_dict": spec_214_dict,
    }


@pytest.fixture(
    scope="function",
    params=[],
)
def spec_214_header(request, spec_214_headers):
    yield spec_214_headers[request.param]


def test_translate_spec214_l0_check_remaining_214_keys(spec_214_header):
    """
    Validates and tries to translate a fits header against the SPEC-0214 schema
    Checks to make sure that no original 214 keys were dropped.
    Given: A valid SPEC-0214 fits header
    When: Validating headers
    Then: return translated HDUList and do not raise an exception
    """
    # raises exception on failure
    hdr = spec214_validator.validate_and_translate_to_214_l0(spec_214_header, return_type=dict)
    for key in spec_214_header.keys():
        if key not in hdr.keys():
            raise KeyError(f" Keyword {key!r} from original header dropped during translation!")


def test_translate_spec214_check_remaining_214_keys(spec_214_header):
    """
    Validates and tries to translate a fits header against the SPEC-0214 schema
    Checks to make sure that no original 214 keys were dropped.
    Given: A valid SPEC-0214 fits header
    When: Validating headers
    Then: return translated HDUList and do not raise an exception
    """
    # raises exception on failure
    hdr = spec214_validator.validate_and_translate_to_214(spec_214_header, return_type=dict)
    for key in spec_214_header.keys():
        if key not in hdr.keys():
            raise KeyError(f" Keyword {key!r} from original header dropped during translation!")
