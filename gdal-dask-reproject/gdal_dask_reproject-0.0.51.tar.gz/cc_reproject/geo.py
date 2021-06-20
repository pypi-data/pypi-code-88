import xarray
from .warp import reproject


@xarray.register_dataarray_accessor('geo')
class CCRasterArray:

    def __init__(self, xarray_obj):
        self._obj = xarray_obj

    def reproject(self, dst_crs, dst_shape=None,
                  chunks=None, numblocks=None, **kwargs):
        return reproject(self._obj, dst_crs,
                         dst_shape=dst_shape, chunks=chunks,
                         numblocks=numblocks, band_kwargs=None,
                         **kwargs)
