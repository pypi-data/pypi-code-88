from io import BytesIO
from pathlib import Path

import numpy as np
import pytest
from astropy.io import fits

from dkist_header_validator import spec214_validator
from dkist_header_validator import Spec214ValidationException
from dkist_header_validator.exceptions import ReturnTypeException
from dkist_header_validator.exceptions import ValidationException


@pytest.fixture(
    scope="function",
    params=[
        "valid_spec_214_dict",
        "valid_HDUList",
        "valid header",
    ],
)
def valid_spec_214_header_no_data(request, valid_spec_214_headers):
    yield valid_spec_214_headers[request.param]


def test_spec214_return_BytesIO_without_data(valid_spec_214_header_no_data):
    """
    Validates a fits header against the SPEC-0214 schema
    Given: A valid SPEC-0214 fits header
    When: Validating headers
    Then: Raise return type exception
    """
    # raises exception on failure
    with pytest.raises(ReturnTypeException):
        spec214_validator.validate(valid_spec_214_header_no_data, return_type=BytesIO, extra=False)


def test_spec214_return_file_without_data(valid_spec_214_header_no_data):
    """
    Validates a fits header against the SPEC-0214 schema
    Given: A valid SPEC-0214 fits header
    When: Validating headers
    Then: raise a return type exception
    """
    # raises exception on failure
    with pytest.raises(ReturnTypeException):
        spec214_validator.validate(valid_spec_214_header_no_data, return_type=Path, extra=False)


@pytest.fixture(scope="module")
def invalid_spec_214_headers(tmpdir_factory):
    """
    Create a dict of invalid spec 214 headers to be used in failing
    header tests below.
    """
    invalid_spec_214_dict = {
        "NAXIS": 2,
        "BITPIX": 16,
        "NAXIS1": 1,
        "NAXIS2": 1,
        "LINEWAV": "NOTSUPPOSEDTOBEASTRING",
        "ID___002": "YVPS4YRBSXUT9Z17Z4HRH3VIH7T6KO",
        "ID___003": "POLETJWHTN2PMM1ZPPLPWQ1KBAKIUF",
        "ID___012": "1XXPIDR5CEXMZ0SQ8LT3HMF83FW4HJ",
        "DKIST003": "OSZ4FBHWKXRWQGOVG9BJNUWNG5795B",
        "DKIST004": "Observation",
        "DAAXES": 15,
        "DEAXES": 16,
        "HISTORY": "Old History",
        "COMMENT": 12.3,
        "DATE-OBS": "2017-05-30T00:46:13.952",
        "WAVELNTH": 582.3,
        "ID___008": "opexecutionid",
        "ID___013": "proposalid",
    }

    temp_dir = tmpdir_factory.mktemp("invalid spec_214_headers_temp")
    file_name = temp_dir.join("tmp_fits_file.fits")
    temp_array = np.ones((1, 1, 1), dtype=np.int16)
    invalid_hdu = fits.PrimaryHDU(temp_array)
    # Use the invalid_spec_122_dict from above to overwrite the default header
    for (key, value) in invalid_spec_214_dict.items():
        invalid_hdu.header[key] = value
    invalid_hdu_list = fits.HDUList([invalid_hdu])
    invalid_hdu_list.writeto(str(file_name))

    yield {
        "invalid_dkist_hdr.fits": Path(file_name),
        "invalid_spec_214_dict": invalid_spec_214_dict,
        "invalid_HDUList": invalid_hdu_list,
        "invalid header": invalid_hdu.header,
    }


@pytest.fixture(
    scope="function",
    params=[
        "invalid_dkist_hdr.fits",
        "invalid_spec_214_dict",
        "invalid_HDUList",
        "invalid header",
    ],
)
def invalid_spec_214_header(request, invalid_spec_214_headers):
    yield invalid_spec_214_headers[request.param]


def test_spec214_invalid_headers(invalid_spec_214_header):
    """
    Validates an invalid fits header against the SPEC-214 schema
    Given: A invalid SPEC-214 fits header
    When: Validating headers
    Then: raise a Spec214ValidationException
    """

    with pytest.raises(Spec214ValidationException):
        spec214_validator.validate(invalid_spec_214_header)


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
    Then: raise a Spec214ValidationException
    """

    with pytest.raises(ValidationException):
        spec214_validator.validate(invalid_file_param)


@pytest.fixture(scope="module")
def invalid_compressed_spec_214_headers(tmpdir_factory):
    """
    Create a dict of invalid (non-fits compliant)
    compressed spec 214 headers to be used in
    header tests below.
    """
    invalid_comp_214_dict = {
        "NAXIS": 3,
        "BITPIX": 16,
        "NAXIS1": 1,
        "NAXIS2": 1,
        "NAXIS3": 1,
        "INSTRUME": "VBI-BLUE",
        "CHECKSUM": "POLETJWHTN2PMM1ZPPLPWQ1KBAKIUF",
        "OBSPR_ID": "JX3O8NXFI6FGTVZ1D7G7U8OVUWDZQL",
        "ID___008": "JX3O8NXFI6FGTVZ1D7G7U8OVUWDZQL",
        "EXPER_ID": "1XXPIDR5CEXMZ0SQ8LT3HMF83FW4HJ",
        "ID___012": "1XXPIDR5CEXMZ0SQ8LT3HMF83FW4HJ",
        "PROP_ID": "4L6XY2SM39CNQTOO4L04Y3RV0H2MTW",
        "ID___013": "4L6XY2SM39CNQTOO4L04Y3RV0H2MTW",
        "ORIGIN": "4L6XY2SM39CNQTOO4L04Y3RV0H2MTW",
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
        "TELESCOP": "DKIST",
        "NETWORK": "ABCD",
        "OBJECT": "SUNSPOT N62",
        "BUNIT": "ct",
        "OBSERVAT": "NSO",
        "DATE-OBS": "2017-05-30T00:46:13.952",
        "WAVELNTH": 582.3,
        "ID___002": "fileid",
        "DKIST003": "observe",
        "DKIST004": "dark",
    }

    temp_dir = tmpdir_factory.mktemp("invalid comp_214_headers_temp")
    file_name = temp_dir.join("tmp_invalid_comp_fits_file.fits")
    temp_array = np.ones((1, 1, 1), dtype=np.int16)
    primary_hdu = fits.PrimaryHDU(temp_array)
    invalid_comp_hdu = fits.CompImageHDU(temp_array)
    c = fits.Card.fromstring("P.I. = 'DKIST'")
    invalid_comp_hdu.header.append(c)
    # Use the invalid_spec_214_dict from above to overwrite the default header
    for (key, value) in invalid_comp_214_dict.items():
        invalid_comp_hdu.header[key] = value
    invalid_comp_hdu_list = fits.HDUList([primary_hdu, invalid_comp_hdu])
    invalid_comp_hdu_list.writeto(str(file_name), output_verify="ignore")

    yield {
        "invalid_compressed_hdr.fits.fz": Path(file_name),
    }


@pytest.fixture(
    scope="function",
    params=[
        "invalid_compressed_hdr.fits.fz",
    ],
)
def invalid_compressed_spec_214_header(request, invalid_compressed_spec_214_headers):
    yield invalid_compressed_spec_214_headers[request.param]


def test_invalid_compressed_spec214(invalid_compressed_spec_214_header):
    """
    Validates an invalid compressed spec214 compliant file
    Given: An invalid compressed SPEC-0214 file
    When: Validating headers
    Then: Catch a warning and raise an exception
    """
    with pytest.raises(Spec214ValidationException):
        spec214_validator.validate(invalid_compressed_spec_214_header)


def test_validate_toomanyHDUs(valid_spec_214_header_toomanyHDUs):
    """
    Validates headers with too many (more than 2) HDUs
    Given: A valid SPEC-214 file or HDUList with more than two headers
    When: Validating headers
    Then: Raise an exception
    """
    # raises exception on failure
    with pytest.raises(ValidationException):
        spec214_validator.validate(valid_spec_214_header_toomanyHDUs)
