import numpy as np
import xarray as xr
from pyproj.crs import CRS
import math


def _tokenize(name: str):
    return f'{name}-{np.random.randint(0, 0xFFFFFFFF)}'


def _boundary_from_shape_affine(xy_shape, affine):
    xoff, yoff = affine.c, affine.f
    xend, yend = affine * xy_shape
    x_offsets, x_endsets = (xoff, yoff), (xend, yend)
    return (x_offsets, x_endsets)


def _calc_chunks(numblocks, shape):
    chunks = []
    for i in range(len(numblocks)):
        chunks.append([])
        for j in range(numblocks[i]):
            chunk_dim = int(math.ceil(shape[i]/numblocks[i]))
            chunks[i].append(chunk_dim)
    diffs = [shape[i] - sum(chunks[i]) for i in range(len(chunks))]
    for i in range(len(diffs)):
        if diffs[i] != 0:
            # perhaps add splitting adjustment into next chunk
            chunks[i][-1] += diffs[i]
    chunks = tuple(tuple(dim) for dim in chunks)
    return chunks


def _chunkshapes(chunks):
    chunkshapes = []
    for i in range(len(chunks[0])):
        for j in range(len(chunks[1])):
            for k in range(len(chunks[2])):
                chunkshapes.append((chunks[0][i], chunks[1][j], chunks[2][k]))
    return chunkshapes


def _bandshapes_from_numblocks_bandchunks(numblocks, bandchunks):
    blocks_hw = numblocks[1:]
    tot_hw_blocks = np.prod(blocks_hw)
    bandshapes = [(chunk,) * tot_hw_blocks for chunk in bandchunks]
    bandshapes = [(sh,) for shape in bandshapes for sh in shape]
    return bandshapes


def _arr_locs(chunklocs, chunkshapes):
    locs_shapes = dict(zip(chunklocs, chunkshapes))
    arr_locs = []
    for i in range(len(chunkshapes)):
        arr_locs.append([])
        for j in range(len(chunklocs[0])):
            start_pos = 0
            dim_position = chunklocs[i][j]
            prev_len = 0
            for num in range(dim_position):
                itera = [0] * (len(chunklocs[0]))
                itera[j] = num
                itera = tuple(itera)
                prev_shape = locs_shapes[itera]
                prev_shape_dim_len = prev_shape[j]
                prev_len += prev_shape_dim_len
            start_pos += prev_len
            end_pos = start_pos + chunkshapes[i][j]
            arr_locs[i].append((start_pos, end_pos))
    return arr_locs


def _coords_from_pts_affine(pts, affine):
    xy_pts = [affine * pt for pt in pts]
    return xy_pts


def _offends_from_arrlocs(locs):
    Y, X = locs[1:]
    p_xoff, p_xend = X
    p_yoff, p_yend = Y
    return (p_xoff, p_yoff), (p_xend, p_yend)


def _shape_from_offend_pix(offends):
    p_offsets, p_endsets = offends
    p_x0, p_y0 = p_offsets
    p_x1, p_y1 = p_endsets
    p_height = p_y1 - p_y0
    p_width = p_x1 - p_x0
    shape = (p_height, p_width)
    return shape


def _sum_chunk_shapes(shapes, numblocks):
    num_dims = len(shapes[0])
    nparr = np.asarray(shapes).reshape(*numblocks, num_dims)
    first_col_index = ((slice(None),) * (len(numblocks) - 1) +
                       (0,))
    first_col = nparr[first_col_index]
    heights_index = ((slice(None),) * (len(first_col.shape) - 1) +
                     (num_dims - 2,))
    heights = first_col[heights_index]
    tot_height = sum(heights.flatten())
    first_row_index = ((slice(None),) * (len(numblocks) - 2) +
                       (0,))
    first_row = nparr[first_row_index]
    widths_index = ((slice(None),) * (len(first_row.shape) - 1) +
                    (num_dims - 1,))
    widths = first_row[widths_index]
    tot_width = sum(widths.flatten())
    return (tot_height, tot_width)


def _chunks_from_shapes_numblocks(shapes, numblocks):
    # num_dims redundant; rewrite for bands in shapes if true 3d resample
    num_dims = len(numblocks)
    nparr = np.asarray(shapes).reshape(*numblocks, num_dims)
    first_col_index = ((slice(None),) * (num_dims - 1) +
                       (0,))
    first_col = nparr[first_col_index]
    heights_index = ((slice(None),) * (len(first_col.shape) - 1) +
                     (num_dims - 2,))
    heights = first_col[heights_index]
    heights_chunk = tuple(heights.flatten().tolist())
    first_row_index = ((slice(None),) * (num_dims - 2) +
                       (0,))
    first_row = nparr[first_row_index]
    widths_index = ((slice(None),) * (len(first_row.shape) - 1) +
                    (num_dims - 1,))
    widths = first_row[widths_index]
    widths_chunk = tuple(widths.flatten().tolist())
    return (heights_chunk, widths_chunk)


def _sp_ref_coords(crs_cf):
    np_arr = np.array(0, dtype=np.int64)
    xr_da = xr.DataArray(np_arr, name='spatial_ref')
    xr_da.coords['spatial_ref'] = np_arr
    xr_da.attrs = crs_cf
    return xr_da


def _make_coords(shape, bounds):
    b, h, w = shape

    bands = np.array(range(1, b + 1), dtype=np.int64)
    bands_da = xr.DataArray(bands, name='band', dims=('band'))
    bands_da.coords['band'] = bands

    xmin, ymin, xmax, ymax = bounds
    X, Y = xmax - xmin, ymax - ymin
    resx, resy = X / w, Y / h
    xs = np.arange(w) * resx + (xmin + resx / 2)
    ys = np.arange(h) * resy + (ymin + resy / 2)
    xs_da = xr.DataArray(xs, dims=('x'))
    xs_da.coords['x'] = xs
    ys_da = xr.DataArray(ys, dims=('y'))
    ys_da.coords['y'] = ys
    coords = dict(x=xs_da, y=ys_da, band=bands_da)
    return coords


def _add_coords_crs_tr_da(nparr, bounds, input_crs, transform):
    shape = nparr.shape

    coords = _make_coords(shape, bounds)

    xr_da = xr.DataArray(nparr, dims=('band', 'y', 'x'))

    for coord in coords:
        xr_da.coords[coord] = coords[coord]

    crs = CRS(input_crs)
    crs_cf = crs.to_cf()
    GeoTransform = ' '.join([str(num) for num in transform.to_gdal()])
    crs_cf['GeoTransform'] = GeoTransform

    spatial_ref = _sp_ref_coords(crs_cf)
    xr_da.coords['spatial_ref'] = spatial_ref
    xr_da.attrs['grid_mapping'] = 'spatial_ref'

    return xr_da
