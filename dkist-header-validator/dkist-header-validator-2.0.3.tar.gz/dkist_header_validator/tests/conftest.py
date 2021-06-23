from pathlib import Path

import numpy as np
import pytest
from astropy.io import fits


@pytest.fixture(scope="module")
def valid_spec_122_headers(tmpdir_factory):
    """
    Create a dict of valid spec 122 headers to be used in successful
    header tests below.
    """
    valid_spec_122_dict = {
        "NAXIS": 3,
        "BITPIX": 16,
        "NAXIS1": 1,
        "NAXIS2": 1,
        "NAXIS3": 1,
        "INSTRUME": "VBI",
        "WAVELNTH": 430.0,
        "DATE-BGN": "2017-05-29T12:00:13.345",
        "DATE-END": "2017-05-30T20:00:13.345",
        "CHECKSUM": "POLETJWHTN2PMM1ZPPLPWQ1KBAKIUF",
        "DATE-OBS": "2017-05-30T00:46:13.952",
        "ID___002": "YVPS4YRBSXUT9Z17Z4HRH3VIH7T6KO",
        "ID___008": "JX3O8NXFI6FGTVZ1D7G7U8OVUWDZQL",
        "ID___012": "1XXPIDR5CEXMZ0SQ8LT3HMF83FW4HJ",
        "ID___013": "2KJBWEFB4OUUBSFUIB5JKBSDF8JBSK",
        "DKIST003": "observe",
        "DKIST004": "observe",
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
        "ORIGIN": "National Solar Observatory",
        "TELESCOP": "Daniel K. Inouye Solar Telescope",
        "OBSERVAT": "Haleakala High Altitude Observatory Site",
        "NETWORK": "NSF-DKIST",
        "OBJECT": "quietsun",
        "DATASUM": "E5O2YIVIP04EOEL59NGM",
        "HISTORY": "Old History",
        "COMMENT": "A comment",
        "ID___004": "LKNDFPONP93HR08BG",
        "ID___001": "NEWESTVERSION",
        "CAM__002": "CAMERA 1",
        "CAM__005": 126.3,
        "CAM__004": 13.2,
        "CAM__014": 3,
        "TAZIMUTH": 3.0,
        "TELTRACK": "None",
    }

    temp_dir = tmpdir_factory.mktemp("valid spec_122_headers_temp")
    file_name = temp_dir.join("tmp_fits_file.fits")
    temp_array = np.ones((1, 1, 1), dtype=np.int16)
    valid_hdu = fits.PrimaryHDU(temp_array)
    # Use the valid_spec_122_dict from above to overwrite the default header
    for (key, value) in valid_spec_122_dict.items():
        valid_hdu.header[key] = value
    valid_hdu_list = fits.HDUList([valid_hdu])
    valid_hdu_list.writeto(str(file_name))

    yield {
        "valid_dkist_hdr.fits": Path(file_name),
        "valid_spec_122_dict": valid_spec_122_dict,
        "valid_HDUList": valid_hdu_list,
        "valid header": valid_hdu.header,
    }


@pytest.fixture(
    scope="function",
    params=[
        "valid_dkist_hdr.fits",
        "valid_spec_122_dict",
        "valid_HDUList",
        "valid header",
    ],
)
def valid_spec_122_header(request, valid_spec_122_headers):
    yield valid_spec_122_headers[request.param]


@pytest.fixture(
    scope="function",
    params=[
        "valid_dkist_hdr.fits",
    ],
)
def valid_spec_122_file(request, valid_spec_122_headers):
    yield valid_spec_122_headers[request.param]


@pytest.fixture(scope="module")
def valid_compressed_spec_122_headers(tmpdir_factory):
    """
    Create a dict of valid compressed spec 122 headers
    to be used in successful header tests below.
    """
    valid_comp_122_dict = {
        "NAXIS": 3,
        "BITPIX": 16,
        "NAXIS1": 1,
        "NAXIS2": 1,
        "NAXIS3": 1,
        "BZERO": 0.0,
        "BSCALE": 1.0,
        "INSTRUME": "VBI",
        "WAVELNTH": 430.0,
        "DATE-END": "2017-05-30T00:46:13.718",
        "CHECKSUM": "POLETJWHTN2PMM1ZPPLPWQ1KBAKIUF",
        "DATASUM": "POLETJWHTN2PMM1ZPPLPWQ1KBAKIZY",
        "DATE-OBS": "2017-05-30T00:46:13.952",
        "DATE-BGN": "2017-05-30T00:46:13.952",
        "ID___002": "YVPS4YRBSXUT9Z17Z4HRH3VIH7T6KO",
        "ID___008": "JX3O8NXFI6FGTVZ1D7G7U8OVUWDZQL",
        "ID___012": "1XXPIDR5CEXMZ0SQ8LT3HMF83FW4HJ",
        "ID___013": "06VMAW1QQX7YYI5W3BZTAFCGX9I83Q",
        "DKIST003": "observe",
        "DKIST004": "observe",
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
        "ORIGIN": "National Solar Observatory",
        "TELESCOP": "Daniel K. Inouye Solar Telescope",
        "OBSERVAT": "Haleakala High Altitude Observatory Site",
        "NETWORK": "NSF-DKIST",
        "OBJECT": "quietsun",
        "HISTORY": "Old history",
        "COMMENT": "a comment",
        "ID___004": "LKNDFPONP93HR08BG",
        "DKISTVER": "NEWESTVERSION",
        "ID___001": "NEWESTVERSION",
        "CAM__002": "CAMERA 1",
        "CAM__005": 126.3,
        "CAM__004": 13.2,
        "CAM__014": 3,
    }

    temp_dir = tmpdir_factory.mktemp("valid comp_122_headers_temp")
    file_name = temp_dir.join("tmp__comp_fits_file.fits")
    temp_array = np.ones((1, 1, 1), dtype=np.int16)
    primary_hdu = fits.PrimaryHDU()
    valid_comp_hdu = fits.CompImageHDU(temp_array)
    # Use the valid_spec_122_dict from above to overwrite the default header
    for (key, value) in valid_comp_122_dict.items():
        valid_comp_hdu.header[key] = value
    valid_comp_hdu_list = fits.HDUList([primary_hdu, valid_comp_hdu])
    valid_comp_hdu_list.writeto(str(file_name), checksum=True)

    yield {
        "valid_compressed_hdr.fits.fz": Path(file_name),
    }


@pytest.fixture(
    scope="function",
    params=[
        "valid_compressed_hdr.fits.fz",
    ],
)
def valid_compressed_spec_122_header(request, valid_compressed_spec_122_headers):
    yield valid_compressed_spec_122_headers[request.param]


@pytest.fixture(scope="module")
def valid_visp_122_headers(tmpdir_factory):
    """
    Create a dict of valid visp spec 122 headers to be used in successful
    header tests below.
    """
    valid_visp_122_dict = {
        "NAXIS": 3,
        "BITPIX": 16,
        "NAXIS1": 1,
        "NAXIS2": 1,
        "NAXIS3": 1,
        "INSTRUME": "VBI",
        "WAVELNTH": 430.0,
        "DATE-BGN": "2017-05-29T12:00:13.345",
        "DATE-END": "2017-05-30T20:00:13.345",
        "CHECKSUM": "POLETJWHTN2PMM1ZPPLPWQ1KBAKIUF",
        "DATE-OBS": "2017-05-30T00:46:13.952",
        "VISP_001": 3,
        "VISP_002": 32.0,
        "VISP_003": 45.6,
        "VISP_004": "string",
        "VISP_005": 31.9,
        "ID___002": "YVPS4YRBSXUT9Z17Z4HRH3VIH7T6KO",
        "ID___008": "JX3O8NXFI6FGTVZ1D7G7U8OVUWDZQL",
        "ID___012": "1XXPIDR5CEXMZ0SQ8LT3HMF83FW4HJ",
        "ID___013": "2KJBWEFB4OUUBSFUIB5JKBSDF8JBSK",
        "DKIST003": "observe",
        "DKIST004": "observe",
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
        "ORIGIN": "National Solar Observatory",
        "TELESCOP": "Daniel K. Inouye Solar Telescope",
        "OBSERVAT": "Haleakala High Altitude Observatory Site",
        "NETWORK": "NSF-DKIST",
        "OBJECT": "quietsun",
        "DATASUM": "E5O2YIVIP04EOEL59NGM",
        "ID___004": "LKNDFPONP93HR08BG",
        "ID___001": "NEWESTVERSION",
        "CAM__002": "CAMERA 1",
        "CAM__005": 126.3,
        "CAM__004": 13.2,
        "CAM__014": 3,
    }

    temp_dir = tmpdir_factory.mktemp("valid visp_122_headers_temp")
    file_name = temp_dir.join("tmp_fits_file.fits")
    temp_array = np.ones((1, 1, 1), dtype=np.int16)
    valid_hdu = fits.PrimaryHDU(temp_array)
    # Use the valid_visp_122_dict from above to overwrite the default header
    for (key, value) in valid_visp_122_dict.items():
        valid_hdu.header[key] = value
    valid_hdu_list = fits.HDUList([valid_hdu])
    valid_hdu_list.writeto(str(file_name))

    yield {
        "valid_visp_hdr.fits": Path(file_name),
        "valid_visp_122_dict": valid_visp_122_dict,
        "valid_visp_HDUList": valid_hdu_list,
        "valid visp header": valid_hdu.header,
    }


@pytest.fixture(
    scope="function",
    params=[
        "valid_visp_hdr.fits",
        "valid_visp_122_dict",
        "valid_visp_HDUList",
        "valid visp header",
    ],
)
def valid_visp_122_header(request, valid_visp_122_headers):
    yield valid_visp_122_headers[request.param]


@pytest.fixture(scope="module")
def valid_spec_122_headers_datainsecondHDU(tmpdir_factory):
    """
    Create a dict of valid spec 122 headers.
    """
    valid_spec_122_dict = {
        "NAXIS": 3,
        "BITPIX": 16,
        "NAXIS1": 1,
        "NAXIS2": 1,
        "NAXIS3": 1,
        "INSTRUME": "VBI",
        "WAVELNTH": 430.0,
        "DATE-BGN": "2017-05-29T12:00:13.345",
        "DATE-END": "2017-05-30T20:00:13.345",
        "CHECKSUM": "POLETJWHTN2PMM1ZPPLPWQ1KBAKIUF",
        "DATE-OBS": "2017-05-30T00:46:13.952",
        "ID___002": "YVPS4YRBSXUT9Z17Z4HRH3VIH7T6KO",
        "ID___008": "JX3O8NXFI6FGTVZ1D7G7U8OVUWDZQL",
        "ID___012": "1XXPIDR5CEXMZ0SQ8LT3HMF83FW4HJ",
        "ID___013": "2KJBWEFB4OUUBSFUIB5JKBSDF8JBSK",
        "DKIST003": "observe",
        "DKIST004": "observe",
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
        "ORIGIN": "National Solar Observatory",
        "TELESCOP": "Daniel K. Inouye Solar Telescope",
        "OBSERVAT": "Haleakala High Altitude Observatory Site",
        "NETWORK": "NSF-DKIST",
        "OBJECT": "quietsun",
        "DATASUM": "E5O2YIVIP04EOEL59NGM",
        "ID___004": "LKNDFPONP93HR08BG",
        "ID___001": "NEWESTVERSION",
        "CAM__002": "CAMERA 1",
        "CAM__005": 126.3,
        "CAM__004": 13.2,
        "CAM__014": 3,
    }

    temp_dir = tmpdir_factory.mktemp("valid spec_122_headers_temp")
    file_name = temp_dir.join("tmp_fits_file.fits")
    temp_array = np.ones((1, 1, 1), dtype=np.int16)
    valid_hdu = fits.PrimaryHDU()
    image_hdu1 = fits.ImageHDU(temp_array)
    # Use the valid_spec_122_dict from above to overwrite the default header
    for (key, value) in valid_spec_122_dict.items():
        valid_hdu.header[key] = value
        image_hdu1.header[key] = value
    valid_hdu_list = fits.HDUList([valid_hdu, image_hdu1])
    valid_hdu_list.writeto(str(file_name))

    yield {
        "valid_dkist_hdr_datainsecondHDU.fits": Path(file_name),
    }


@pytest.fixture(
    scope="function",
    params=[
        "valid_dkist_hdr_datainsecondHDU.fits",
    ],
)
def valid_spec_122_header_datainsecondHDU(request, valid_spec_122_headers_datainsecondHDU):
    yield valid_spec_122_headers_datainsecondHDU[request.param]


@pytest.fixture(scope="module")
def valid_spec_214_headers(tmpdir_factory):
    """
    Create a dict of valid spec 214 headers to be used in successful
    header tests below.
    """
    valid_spec_214_dict = {
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

    temp_dir = tmpdir_factory.mktemp("valid spec_214_headers_temp")
    file_name = temp_dir.join("tmp_fits_file.fits")
    temp_array = np.ones((1, 1, 1), dtype=np.int16)
    valid_hdu = fits.PrimaryHDU(temp_array)
    # Use the valid_spec_214_dict from above to overwrite the default header
    for (key, value) in valid_spec_214_dict.items():
        valid_hdu.header[key] = value
    valid_hdu_list = fits.HDUList([valid_hdu])
    valid_hdu_list.writeto(str(file_name))
    yield {
        "valid_dkist_hdr.fits": Path(file_name),
        "valid_spec_214_dict": valid_spec_214_dict,
        "valid_HDUList": valid_hdu_list,
        "valid header": valid_hdu.header,
    }


@pytest.fixture(
    scope="function",
    params=[
        "valid_dkist_hdr.fits",
        "valid_spec_214_dict",
        "valid_HDUList",
        "valid header",
    ],
)
def valid_spec_214_header(request, valid_spec_214_headers):
    yield valid_spec_214_headers[request.param]


@pytest.fixture(
    scope="function",
    params=[
        "valid_dkist_hdr.fits",
    ],
)
def valid_spec_214_file(request, valid_spec_214_headers):
    yield valid_spec_214_headers[request.param]


@pytest.fixture(scope="module")
def valid_spec_214_headers_toomanyHDUs(tmpdir_factory):
    """
    Create a dict of valid spec 214 headers to be used in successful
    header tests below.
    """
    valid_spec_214_dict = {
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
        "DATE-OBS": "2017-05-30T00:46:13.952",
        "WAVELNTH": 582.3,
        "ID___002": "fileid",
        "ID___008": "opexecutionid",
        "ID___013": "proposalid",
        "DKIST003": "observe",
        "DKIST004": "dark",
        "ID___004": "LKNDFPONP93HR08BG",
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

    temp_dir = tmpdir_factory.mktemp("valid spec_214_headers_temp")
    file_name = temp_dir.join("tmp_fits_file.fits")
    temp_array = np.ones((1, 1, 1), dtype=np.int16)
    valid_hdu = fits.PrimaryHDU(temp_array)
    image_hdu1 = fits.ImageHDU(temp_array)
    image_hdu2 = fits.ImageHDU(temp_array)
    # Use the valid_spec_214_dict from above to overwrite the default header
    for (key, value) in valid_spec_214_dict.items():
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
def valid_spec_214_header_toomanyHDUs(request, valid_spec_214_headers_toomanyHDUs):
    yield valid_spec_214_headers_toomanyHDUs[request.param]


@pytest.fixture(scope="module")
def valid_spec_214_headers_datainsecondHDU(tmpdir_factory):
    """
    Create a dict of valid spec 214 headers to be used in successful
    header tests below.
    """
    valid_spec_214_dict = {
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
        "DATE-OBS": "2017-05-30T00:46:13.952",
        "WAVELNTH": 582.3,
        "ID___002": "fileid",
        "ID___008": "opexecutionid",
        "ID___013": "proposalid",
        "DKIST003": "observe",
        "DKIST004": "dark",
        "ID___004": "LKNDFPONP93HR08BG",
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

    temp_dir = tmpdir_factory.mktemp("valid spec_214_headers_temp")
    file_name = temp_dir.join("tmp_fits_file.fits")
    temp_array = np.ones((1, 1, 1), dtype=np.int16)
    valid_hdu = fits.PrimaryHDU()
    image_hdu1 = fits.ImageHDU(temp_array)
    # Use the valid_spec_214_dict from above to overwrite the default header
    for (key, value) in valid_spec_214_dict.items():
        valid_hdu.header[key] = value
        image_hdu1.header[key] = value
    valid_hdu_list = fits.HDUList([valid_hdu, image_hdu1])
    valid_hdu_list.writeto(str(file_name))
    yield {
        "valid_dkist_hdr_datainsecondHDU.fits": Path(file_name),
    }


@pytest.fixture(
    scope="function",
    params=[
        "valid_dkist_hdr_datainsecondHDU.fits",
    ],
)
def valid_spec_214_header_datainsecondHDU(request, valid_spec_214_headers_datainsecondHDU):
    yield valid_spec_214_headers_datainsecondHDU[request.param]
