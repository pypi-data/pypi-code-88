import numpy as np
import dask.array as da
from dask.highlevelgraph import HighLevelGraph

from pyproj.crs import CRS
import rasterio
from rasterio.warp import Affine as A

import math

from .tools import (
    _tokenize,
    _boundary_from_shape_affine,
    _calc_chunks,
    _chunkshapes,
    _bandshapes_from_numblocks_bandchunks,
    _arr_locs,
    _coords_from_pts_affine,
    _offends_from_arrlocs,
    _shape_from_offend_pix,
    _sum_chunk_shapes,
    _chunks_from_shapes_numblocks,
    _add_coords_crs_tr_da
)


def _transform_xy_pts(pts, src_crs, dst_crs):
    xx, yy = list(zip(*pts))
    transformed = rasterio.warp.transform(src_crs, dst_crs, xx, yy)
    trans_pts = list(zip(*transformed))
    return trans_pts


def _affine_from_offsets_res(offsets, res):
    xoff, yoff = offsets
    resx, resy = res
    affine = A(resx, 0, xoff, 0, resy, yoff)
    return affine


def _calc_default_dst_shape_boundary(src_xy_shape, src_affine,
                                     src_crs, dst_crs):
    _, s_height = src_xy_shape

    s_offsets, s_endsets = _boundary_from_shape_affine(src_xy_shape,
                                                       src_affine)

    (s_xoff, s_yoff), (s_xend, s_yend) = s_offsets, s_endsets
    s_X, s_Y = s_xend - s_xoff, s_yoff - s_yend

    (d_xoff, d_yoff), (d_xend, d_yend) = d_offsets, d_endsets =\
        _transform_xy_pts([s_offsets, s_endsets], src_crs, dst_crs)
    d_X, d_Y = d_xend - d_xoff, d_yoff - d_yend
    d_XperY = d_X / d_Y

    d_height = ((abs(d_Y) / (d_X + d_Y)) / (abs(s_Y) / (s_X + s_Y))) * s_height
    d_width = d_height * d_XperY
    d_height, d_width = int(d_height), int(d_width)
    dst_shape = (d_height, d_width)

    return dst_shape, d_offsets, d_endsets


def _sbk_affine_pad_pix(offend_sets, res, src_shape, src_transform, padding):
    offsets, endsets = offend_sets

    rev_affine = ~src_transform
    p_offsets = rev_affine * offsets
    p_endsets = rev_affine * endsets
    p_offsets = [abs(int(pix)) for pix in p_offsets]
    p_endsets = [abs(int(math.ceil(pix))) for pix in p_endsets]

    b, h, w = src_shape

    p_offsets = [max(0, p_off - padding) for p_off in p_offsets]
    p_xend, p_yend = p_endsets
    p_xend, p_yend = min(w, p_xend + padding), min(h, p_yend + padding)
    p_endsets = [p_xend, p_yend]
    offsets_pad = src_transform * p_offsets

    affine = _affine_from_offsets_res(offsets_pad, res)

    return affine, p_offsets, p_endsets


def _add_layers(self, locs,
                src_crs, sbk_chunks, sbk_tot_shape,
                dst_shape, dst_chunks, dst_crs,
                band_kwargs=None, **kwargs):
    crop_name = _tokenize('crop_src')
    reproject_name = _tokenize('reproject')
    layers = {crop_name: {}, reproject_name: {}}

    keys = self.__dask_graph__().keys()
    for key in keys:
        if isinstance(key, tuple):
            input_key, *ii = key
            s_affine_pix_bd = locs[tuple(ii)][2]
            s_affine, s_pix0, s_pix1, bands_loc = s_affine_pix_bd
            s_x0, s_y0 = s_pix0
            s_x1, s_y1 = s_pix1
            b0, b1 = bands_loc

            def _crop(nparr, y0, y1, x0, x1, b0, b1):
                return self[b0:b1, y0:y1, x0:x1]
            layers[crop_name][(crop_name, *ii)] = (_crop,
                                                   (input_key, *ii),
                                                   s_y0, s_y1,
                                                   s_x0, s_x1,
                                                   b0, b1)
    crop_graph = HighLevelGraph.from_collections(crop_name,
                                                 layers[crop_name],
                                                 dependencies=[self])
    arr = da.Array(crop_graph, crop_name, chunks=sbk_chunks,
                   dtype=np.uint16, shape=sbk_tot_shape)

    arr_keys = list(layers[crop_name].keys())
    for key in arr_keys:
        if isinstance(key, tuple):
            input_key, *ii = key
            dbk_shape, dbk_affine, s_affine_pix_bd = locs[tuple(ii)]
            s_affine, *_pix_bd = s_affine_pix_bd
            band_idx = ii[0]
            if band_kwargs is not None and band_idx in band_kwargs:
                bd_kwargs = band_kwargs[band_idx]
                bk_kwargs = {**kwargs, **bd_kwargs}
            else:
                bk_kwargs = kwargs
            layers[reproject_name][(reproject_name, *ii)] =\
                (_block_reproject,
                 (input_key, *ii),
                 s_affine,
                 src_crs,
                 dbk_shape,
                 dbk_affine,
                 dst_crs,
                 bk_kwargs)

    graph = HighLevelGraph.from_collections(reproject_name,
                                            layers[reproject_name],
                                            dependencies=[arr])
    return da.Array(graph, reproject_name, chunks=dst_chunks,
                    dtype=np.uint16, shape=dst_shape)


def _block_reproject(src, src_transform, src_crs,
                     dst_shape, dst_transform, dst_crs, kwargs):
    dst = np.zeros(dst_shape, dtype=np.uint16)
    rasterio.warp.reproject(src,
                            dst,
                            src_transform=src_transform,
                            src_crs=src_crs,
                            dst_transform=dst_transform,
                            dst_crs=dst_crs,
                            **kwargs)
    return dst


def _np_reproject(src, src_transform, src_crs, dst_shape, dst_crs, **kwargs):

    if src.dtype == np.uint8:
        _src = src.astype(np.uint16)
    else:
        _src = src

    src_bands, src_height, src_width = src_shape = _src.shape

    src_res = src_transform.a, src_transform.e
    src_xy_shape = (src_width, src_height)

    if dst_shape is None:
        dst_shape, d_offsets, d_endsets =\
            _calc_default_dst_shape_boundary(src_xy_shape,
                                             src_transform,
                                             src_crs, dst_crs)
        dst_shape = (src_bands, *dst_shape)
    else:
        s_offsets, s_endsets = _boundary_from_shape_affine(src_xy_shape,
                                                           src_transform)
        d_offsets, d_endsets = _transform_xy_pts([s_offsets, s_endsets],
                                                 src_crs, dst_crs)

    d_bands, d_height, d_width = dst_shape

    d_xoff, d_yoff = d_offsets
    d_xend, d_yend = d_endsets

    d_resx, d_resy = (d_xend - d_xoff) / d_width,\
                     (d_yoff - d_yend) / -d_height

    d_bounds = (d_xoff, d_yoff, d_xend, d_yend)
    d_transform = A(d_resx, 0, d_xoff, 0, d_resy, d_yoff)

    s_offends = _transform_xy_pts((d_offsets, d_endsets),
                                  dst_crs, src_crs)
    s_affine, s_pix0, s_pix1 =\
        _sbk_affine_pad_pix(s_offends, src_res, src_shape,
                            src_transform, 0)
    s_x0, s_y0 = s_pix0
    s_x1, s_y1 = s_pix1
    src_crop = _src[:, s_y0:s_y1, s_x0:s_x1]
    reprojected_data = _block_reproject(src_crop, s_affine, src_crs,
                                        dst_shape, d_transform, dst_crs,
                                        kwargs)

    if _src.dtype != src.dtype:
        reprojected_data = reprojected_data.astype(np.uint8)

    reprojected_da = _add_coords_crs_tr_da(reprojected_data, d_bounds,
                                           dst_crs, d_transform)
    return reprojected_da


def _dask_reproject(src, src_transform, src_crs, dst_shape, dst_crs,
                    dst_chunks=None, numblocks=None, band_kwargs=None,
                    **kwargs):
    """
    Reprojection with dask by reprojecting chunk by chunk.

    Computes the destination chunks based on source chunks
    or specified chunks, then finds area in source raster
    that gives data for each chunk and then warps the chunks using
    rasterio.warp.reproject.

    Parameters:
    -----------
    src: source np or dask array

    src_transform: affine transform corresponding to
    source offsets, res

    src_crs: crs string; e.g. 'EPSG:4326'

    dst_shape: tuple(bands, width, height)

    dst_chunks: tuple of tuples

    dst_crs: destination crs string

    **kwargs:

    Returns:
    --------
    xarray DataArray wrapped over a dask array with
    coords set for dst offsets, res
    """
    if src.dtype == np.uint8:
        _src = src.astype(np.uint16)
    else:
        _src = src

    src_bands, src_height, src_width = _src.shape

    src_shape = _src.shape
    src_res = src_transform.a, src_transform.e
    src_xy_shape = (src_width, src_height)

    if dst_shape is None and dst_chunks is None:
        dst_shape, d_offsets, d_endsets =\
            _calc_default_dst_shape_boundary(src_xy_shape,
                                             src_transform,
                                             src_crs, dst_crs)
        dst_shape = (src_bands, *dst_shape)
    else:
        src_offsets, src_endsets = _boundary_from_shape_affine(src_xy_shape,
                                                               src_transform)
        d_offsets, d_endsets = _transform_xy_pts([src_offsets, src_endsets],
                                                 src_crs, dst_crs)

    if dst_chunks is not None or numblocks is not None:
        if numblocks is None:
            numblocks = tuple(len(dim_chunks) for dim_chunks in dst_chunks)
            if dst_shape is None:
                dst_shape = tuple(sum(dim_chunks) for dim_chunks in dst_chunks)
        if dst_chunks is None:
            dst_chunks = _calc_chunks(numblocks, dst_shape)

        if not isinstance(_src, da.Array):
            bandchunks = dst_chunks[0]
            chunks = tuple(int(math.ceil(src_shape[i]/numblocks[i]))
                           for i in range(len(numblocks)))
            chunks = (bandchunks, *chunks[1:])
            _src = da.from_array(_src, chunks=chunks)
        else:
            bandchunks = _src.chunks[0]
            dst_chunks = (bandchunks, *dst_chunks[1:])
    else:
        numblocks = _src.numblocks
        bandchunks = _src.chunks[0]
        # bands calculated math.ceil may not match src band chunking
        dst_chunks = (bandchunks, *_calc_chunks(numblocks, dst_shape)[1:])

    chunklocs = [i for i, j in np.ndenumerate(np.empty(numblocks))]

    band_chunklocs = [(locs[0],) for locs in chunklocs]
    bandshapes = _bandshapes_from_numblocks_bandchunks(numblocks, bandchunks)
    bandlocs = _arr_locs(band_chunklocs, bandshapes)

    dst_chunkshapes = _chunkshapes(dst_chunks)

    dst_arr_locs = _arr_locs(chunklocs, dst_chunkshapes)

    dbk_shapes_lists = [[shape] for shape in dst_chunkshapes]

    dst_bands, dst_height, dst_width = dst_shape

    d_xoff, d_yoff = d_offsets
    d_xend, d_yend = d_endsets
    d_X, d_Y = d_xend - d_xoff, d_yend - d_yoff
    d_resx, d_resy = dst_res = d_X / dst_width, d_Y / dst_height

    dst_bounds = (d_xoff, d_yoff, d_xend, d_yend)
    dst_affine = A(d_resx, 0, d_xoff, 0, d_resy, d_yoff)

    d_shp_tr_s_tr_pix_bd = dict(zip(chunklocs, dbk_shapes_lists))

    dbk_offend_sets = []

    for i in range(len(chunklocs)):
        chunkloc = chunklocs[i]
        d_alocs = dst_arr_locs[i]
        dbk_offend_pix = _offends_from_arrlocs(d_alocs)
        dbk_offend_set = _coords_from_pts_affine(dbk_offend_pix, dst_affine)
        dbk_offend_sets.extend(dbk_offend_set)

        dbk_affine = _affine_from_offsets_res(dbk_offend_set[0], dst_res)

        d_shp_tr_s_tr_pix_bd[chunkloc].append(dbk_affine)

    sbk_xpnd = _transform_xy_pts(dbk_offend_sets, dst_crs, src_crs)
    sbk_offend_sets = [(sbk_xpnd[i], sbk_xpnd[i + 1])
                       for i in range(0, len(sbk_xpnd), 2)]

    if 'padding' in kwargs:
        padding = kwargs.get('padding')
    else:
        padding = 0

    sbk_affines_pix = [_sbk_affine_pad_pix(sbk_offend_set, src_res, src_shape,
                                           src_transform, padding)
                       for sbk_offend_set in sbk_offend_sets]

    sbk_pix = []

    for i in range(len(chunklocs)):
        loc = chunklocs[i]
        sbk_affine_pix = sbk_affines_pix[i]
        sbk_bands = bandlocs[i][0]
        d_shp_tr_s_tr_pix_bd[loc].append((*sbk_affine_pix, sbk_bands))

        sbk_p = sbk_affine_pix[1:]
        sbk_pix.append(sbk_p)

    sbk_shapes_hw = [_shape_from_offend_pix(pix) for pix in sbk_pix]
    # not real shapes, but good for hw chunks calc
    sbk_shapes_pseudo = [(src_bands, *shape) for shape in sbk_shapes_hw]
    sbk_chunks_hw = _chunks_from_shapes_numblocks(sbk_shapes_pseudo, numblocks)
    sbk_chunks = (bandchunks, *sbk_chunks_hw)
    sbk_tot_shape_yx = _sum_chunk_shapes(sbk_shapes_hw, numblocks)
    sbk_tot_shape = (src_bands, *sbk_tot_shape_yx)

    reproject_dsk = _add_layers(_src, d_shp_tr_s_tr_pix_bd,
                                src_crs, sbk_chunks, sbk_tot_shape,
                                dst_shape, dst_chunks, dst_crs,
                                band_kwargs=band_kwargs, **kwargs)

    if _src.dtype != src.dtype:
        reproject_dsk = reproject_dsk.astype(np.uint8)

    reprojected_da = _add_coords_crs_tr_da(reproject_dsk, dst_bounds,
                                           dst_crs, dst_affine)
    return reprojected_da


def reproject(arr, dst_crs, dst_shape=None,
              chunks=None, numblocks=None,
              band_kwargs=None, **kwargs):
    """
    Reprojects spatially referenced rasters to desired crs.

    Takes in an xarray DataArray raster with source crs
    x and y coords and apatial ref coord and warps the shape
    to the desired crs, resetting the coords as well.
    Uses rasterio.warp.reproject. If no destination shape is provided
    then default shape is calculated based on the input and output crs
    and the starting shape. Works with dask and chunking,
    inluding multiband chunking.

    Parameters:
    -----------
    arr: xarray DataArray with crs and transform set in the coords
    in rioxarray compatible style

    dst_crs: str; input crs string; e.g. 'EPSG:4326'

    dst_shape(optional): tuple(bands, y, x); destination shape, if known;
    number of bands must match source

    chunks(optional): tuple of tuples defining destination chunks
    for a dask array; for example: ((1,), (120, 120), (240, 240))
    for a shape chunked 1, 2, 2 along bands, height, width;
    setting this will make reproject return a chunked dask array,
    even with np input.

    numblocks(optional): tuple(int(band_blocks), int(height_blocks),
    int(width_blocks)). Setting this will return a chunked dask array,
    even for np input. If used with chunks, must match

    **kwargs: additional keyword args, inlcuding padding for dask chunks
    and any others to be passed to rasterio.warp.reproject
        padding: int; number of pixels to pad
        each src block being reprojected

    Returns:
    --------
    arr: xarray DataArray with coords set according to dst crs,
    including spatial ref coord
    """
    src = arr.data
    src_crs = CRS(arr.spatial_ref.crs_wkt).to_string()
    src_transform = A.from_gdal(*[float(num) for num in
                                arr.spatial_ref.GeoTransform.split(' ')])
    if (isinstance(src, da.Array) or chunks is not None
       or numblocks is not None):
        reprojected_data = _dask_reproject(src, src_transform, src_crs,
                                           dst_shape, dst_crs,
                                           dst_chunks=chunks,
                                           numblocks=numblocks,
                                           band_kwargs=band_kwargs,
                                           **kwargs)
    elif isinstance(src, np.ndarray):
        reprojected_data = _np_reproject(src, src_transform, src_crs,
                                         dst_shape, dst_crs, **kwargs)
    return reprojected_data
