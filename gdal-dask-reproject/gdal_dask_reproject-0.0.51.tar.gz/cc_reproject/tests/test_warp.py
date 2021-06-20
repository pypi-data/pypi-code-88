from dask.array.routines import isin
from cc_reproject.warp import reproject
import rioxarray
from rasterio.warp import Resampling
import numpy as np
import xarray as xr
import dask.array as da
from pyproj.crs import CRS


dst_crs = 'EPSG:3857'

elev_ll = rioxarray.open_rasterio('../resources/elev_rgb2.tif')
elev_ll_dsk = elev_ll.chunk(((1, 2), (120, 120), (255, 255)))


def test_np_reproject():
    reprojected_np = reproject(elev_ll, dst_crs)
    assert reprojected_np.data.shape == (3, 338, 411)
    assert isinstance(reprojected_np.data, np.ndarray)
    assert CRS(reprojected_np.spatial_ref.crs_wkt).to_string() == dst_crs
    assert isinstance(reprojected_np, xr.DataArray)


def test_np_reproject_kwargs():
    repr_np_kwargs = reproject(elev_ll, dst_crs, resampling=Resampling.min)
    assert repr_np_kwargs.data.shape == (3, 338, 411)
    assert isinstance(repr_np_kwargs.data, np.ndarray)
    assert CRS(repr_np_kwargs.spatial_ref.crs_wkt).to_string() == dst_crs
    assert isinstance(repr_np_kwargs, xr.DataArray)


def test_np_to_dsk():
    repr_np_dsk = reproject(elev_ll, dst_crs, chunks=((1, 2), (169, 169), (206, 205)))
    repr_np_dsk_2 = reproject(elev_ll, dst_crs, numblocks=(2, 2, 2))
    assert repr_np_dsk.data.shape == (3, 338, 411)
    assert repr_np_dsk_2.data.shape == (3, 338, 411)
    assert isinstance(repr_np_dsk.data, da.Array)
    assert isinstance(repr_np_dsk_2.data, da.Array)


def test_reproject_dsk():
    reprojected_dsk = reproject(elev_ll_dsk, dst_crs)
    assert isinstance(reprojected_dsk.data, da.Array)
    assert isinstance(reprojected_dsk, xr.DataArray)
    assert reprojected_dsk.data.shape == (3, 338, 411)


def test_repr_dsk_kwargs():
    repr_dsk_kwargs = reproject(elev_ll_dsk, dst_crs, resmapling=Resampling.min)
    repr_dsk_bnd_kwargs = reproject(elev_ll_dsk, dst_crs, band_kwargs={0: {'resampling': Resampling.min}}, resampling=Resampling.bilinear)

