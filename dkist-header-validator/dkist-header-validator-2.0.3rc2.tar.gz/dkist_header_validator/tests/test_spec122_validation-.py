from io import BytesIO
from pathlib import Path

import numpy as np
import pytest
from astropy.io import fits

from dkist_header_validator import spec122_validator
from dkist_header_validator import Spec122ValidationException
from dkist_header_validator.exceptions import ReturnTypeException
from dkist_header_validator.exceptions import ValidationException


@pytest.fixture(
    scope="function",
    params=[
        "valid_spec_122_dict",
        "valid_HDUList",
        "valid header",
    ],
)
def valid_spec_122_header_no_data(request, valid_spec_122_headers):
    yield valid_spec_122_headers[request.param]


def test_spec122_return_BytesIO_without_data(valid_spec_122_header_no_data):
    """
    Validates a fits header against the SPEC-122 schema
    Given: A valid SPEC-122 fits header, no data attached
    When: Validating headers
    Then: Raise return type exception
    """
    # raises exception on failure
    with pytest.raises(ReturnTypeException):
        spec122_validator.validate(valid_spec_122_header_no_data, return_type=BytesIO, extra=False)


def test_spec122_return_file_without_data(valid_spec_122_header_no_data):
    """
    Validates a fits header against the SPEC-122 schema
    Given: A valid SPEC-122 fits header, no data attached
    When: Validating headers
    Then: raise a return type exception
    """
    # raises exception on failure
    with pytest.raises(ReturnTypeException):
        spec122_validator.validate(valid_spec_122_header_no_data, return_type=Path, extra=False)


@pytest.fixture(scope="module")
def invalid_spec_122_headers(tmpdir_factory):
    """
    Create a dict of invalid spec 122 headers to be used in failing
    header tests below.
    """
    invalid_spec_122_dict = {
        "NAXIS": 2,
        "BITPIX": 16,
        "NAXIS1": 1,
        "NAXIS2": 1,
        "WAVELNTH": "NOTSUPPOSEDTOBEASTRING",
        "DATE-OBS": "2017-05-30T00:46:13.952",
        "ID___002": "YVPS4YRBSXUT9Z17Z4HRH3VIH7T6KO",
        "ID___003": "POLETJWHTN2PMM1ZPPLPWQ1KBAKIUF",
        "ID___012": "1XXPIDR5CEXMZ0SQ8LT3HMF83FW4HJ",
        "DKIST003": "OSZ4FBHWKXRWQGOVG9BJNUWNG5795B",
        "DKIST004": "Observation",
        "HISTORY": 1.3,
    }

    temp_dir = tmpdir_factory.mktemp("invalid spec_122_headers_temp")
    file_name = temp_dir.join("tmp_fits_file.fits")
    temp_array = np.ones((1, 1, 1), dtype=np.int16)
    invalid_hdu = fits.PrimaryHDU(temp_array)
    # Use the invalid_spec_122_dict from above to overwrite the default header
    for (key, value) in invalid_spec_122_dict.items():
        invalid_hdu.header[key] = value
    invalid_hdu_list = fits.HDUList([invalid_hdu])
    invalid_hdu_list.writeto(str(file_name))

    yield {
        "invalid_dkist_hdr.fits": Path(file_name),
        "invalid_spec_122_dict": invalid_spec_122_dict,
        "invalid_HDUList": invalid_hdu_list,
        "invalid header": invalid_hdu.header,
    }


@pytest.fixture(
    scope="function",
    params=[
        "invalid_dkist_hdr.fits",
        "invalid_spec_122_dict",
        "invalid_HDUList",
        "invalid header",
    ],
)
def invalid_spec_122_header(request, invalid_spec_122_headers):
    yield invalid_spec_122_headers[request.param]


def test_spec122_invalid_headers(invalid_spec_122_header):
    """
    Validates an invalid fits header against the SPEC-0122 schema
    Given: A invalid SPEC-0122 fits header
    When: Validating headers
    Then: raise a Spec122ValidationException
    """

    with pytest.raises(Spec122ValidationException):
        spec122_validator.validate(invalid_spec_122_header)


@pytest.fixture(scope="module")
def invalid_file_params(tmpdir_factory):
    """
    Create a dict of invalid file params to be used in failing
    tests below.
    """
    temp_dir = tmpdir_factory.mktemp("invalid_file_params_temp")
    non_existent_file_name = temp_dir.join("tmp_fits_file.fits")
    non_fits_file_name = temp_dir.join("tmp_this_is_not_a_fits_file.dat")
    temp_array = np.ones(1, dtype=np.int16)
    temp_array.tofile(str(non_fits_file_name))
    yield {"file not found": non_existent_file_name, "file_not_fits": non_fits_file_name}


@pytest.fixture(scope="function", params=["file not found", "file_not_fits"])
def invalid_file_param(request, invalid_file_params):
    yield invalid_file_params[request.param]


def test_file_errors(invalid_file_param):
    """
    Validates an invalid file spec
    Given: A invalid file specification: non-existent file or non-fits file
    When: Validating headers
    Then: raise a Spec122ValidationException
    """

    with pytest.raises(ValidationException):
        spec122_validator.validate(invalid_file_param)


@pytest.fixture(scope="module")
def spec_122_headers_toomanyHDUs(tmpdir_factory):
    """
    Create a dict of valid spec 122 headers.
    """
    valid_spec_122_dict = {
        "NAXIS": 3,
        "BITPIX": 16,
        "NAXIS1": 1,
        "NAXIS2": 1,
        "NAXIS3": 1,
        "INSTRUME": "VBI-BLUE",
        "WAVELNTH": 430.0,
        "DATE-BGN": "2017-05-29T12:00:13.345",
        "DATE-END": "2017-05-30T20:00:13.345",
        "CHECKSUM": "POLETJWHTN2PMM1ZPPLPWQ1KBAKIUF",
        "DATE-OBS": "2017-05-30T00:46:13.952",
        "ID___002": "YVPS4YRBSXUT9Z17Z4HRH3VIH7T6KO",
        "ID___008": "JX3O8NXFI6FGTVZ1D7G7U8OVUWDZQL",
        "ID___012": "1XXPIDR5CEXMZ0SQ8LT3HMF83FW4HJ",
        "ID___013": "2KJBWEFB4OUUBSFUIB5JKBSDF8JBSK",
        "DKIST003": "OSZ4FBHWKXRWQGOVG9BJNUWNG5795B",
        "DKIST004": "Observation",
        "WCSAXES": 3,
        "WCSNAME": "Helioprojective Cartesian",
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
        "BUNIT": "ct",
        "DATE": "2017-05-30T00:46:13.952",
        "ORIGIN": "4L6XY2SM39CNQTOO4L04Y3RV0H2MTW",
        "TELESCOP": "DKIST",
        "OBSERVAT": "NSO",
        "NETWORK": "ABCD",
        "OBJECT": "SUNSPOT N62",
        "DATASUM": "E5O2YIVIP04EOEL59NGM",
    }

    temp_dir = tmpdir_factory.mktemp("valid spec_122_headers_temp")
    file_name = temp_dir.join("tmp_fits_file.fits")
    temp_array = np.ones((1, 1, 1), dtype=np.int16)
    valid_hdu = fits.PrimaryHDU(temp_array)
    image_hdu1 = fits.ImageHDU(temp_array)
    image_hdu2 = fits.ImageHDU(temp_array)
    # Use the valid_spec_122_dict from above to overwrite the default header
    for (key, value) in valid_spec_122_dict.items():
        valid_hdu.header[key] = value
        image_hdu1.header[key] = value
        image_hdu2.header[key] = value
    valid_hdu_list = fits.HDUList([valid_hdu, image_hdu1, image_hdu2])
    valid_hdu_list.writeto(str(file_name))

    yield {
        "valid_dkist_hdr_toomanyHDUs.fits": Path(file_name),
        "valid_HDUList_toomanyHDUs": valid_hdu_list,
    }


@pytest.fixture(
    scope="function",
    params=[
        "valid_dkist_hdr_toomanyHDUs.fits",
        "valid_HDUList_toomanyHDUs",
    ],
)
def spec_122_header_toomanyHDUs(request, spec_122_headers_toomanyHDUs):
    yield spec_122_headers_toomanyHDUs[request.param]


def test_toomanyHDUs_translate_to_214_l0(spec_122_header_toomanyHDUs):
    """
    Validates headers with too many (more than 2) HDUs
    Given: A valid SPEC-122 file or HDUList with more than two headers
    When: Validating and translating headers
    Then: Raise an exception
    """
    # raises exception on failure
    with pytest.raises(ValidationException):
        spec122_validator.validate_and_translate_to_214_l0(spec_122_header_toomanyHDUs)


def test_toomanyHDUs_translate_to_214(spec_122_header_toomanyHDUs):
    """
    Validates headers with too many (more than 2) HDUs
    Given: A valid SPEC-122 file or HDUList with more than two headers
    When: Validating and translating headers
    Then: Raise an exception
    """
    # raises exception on failure
    with pytest.raises(ValidationException):
        spec122_validator.validate_and_translate_to_214(spec_122_header_toomanyHDUs)


def test_toomanyHDUs_validate(spec_122_header_toomanyHDUs):
    """
    Validates headers with too many (more than 2) HDUs
    Given: A valid SPEC-122 file or HDUList with more than two headers
    When: Validating headers
    Then: Raise an exception
    """
    # raises exception on failure
    with pytest.raises(ValidationException):
        spec122_validator.validate(spec_122_header_toomanyHDUs)
