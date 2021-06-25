import requests
import logging
from PIL import Image
import io
import os
from ic_slide.time_utils import timeit
from .auth import get_access_token
import numpy as np
from .api_urls import get_metadata_url,\
    get_tile_url
from .config import get_config
import functools
import math
import multiprocessing as mp

logger = logging.getLogger(__name__)

if mp.get_start_method(allow_none=True) != 'spawn':
    mp.set_start_method('spawn', force=True)


class SlideCloudStorage:

    def __init__(self) -> None:
        self.metadata_url = get_metadata_url()
        self.tile_url = get_tile_url()

    def get_metadata(self, slide_id):
        if not slide_id:
            raise ValueError('Invalid empty slide id')
        url = f'{self.metadata_url}/{slide_id}'
        access_token = get_access_token()
        headers = {"Authorization": f"Bearer {access_token}"}
        metadata = requests.get(url,
                                headers=headers).json()
        if 'error' in metadata:
            raise ValueError(metadata['error']['message'])

        result = Metadata(metadata)
        result.SlideId = slide_id
        return result

    @timeit
    @functools.lru_cache(maxsize=get_config('TILE_CACHE_MAX_SIZE'))
    def get_tile(self, slide_id, row, column, layer, lod):
        url = f'{self.tile_url}?id={slide_id}&Row={row}&Column={column}&Layer={layer}&LODLevel={lod}'
        access_token = get_access_token()
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(url, headers=headers)

        if response.status_code >= 200 and response.status_code <= 299:
            tile_url = response.content
        else:
            raise Exception(
                f"Can not get tile, {response.reason} {response.content}")
        response = requests.get(tile_url)
        if response.status_code >= 200 and response.status_code <= 299:
            return response.content
        return None


class Metadata(object):
    SlideId = ''
    Name = ''
    LayerCount = 0
    MinimumLODLevel = 0
    MaximumLODLevel = 0
    LODGaps = []
    QuickHash = ''
    Vendor = ''
    Version = None
    Comments = ''
    BackgroundColor = None
    HorizontalTileCount = 0
    VertialTileCount = 0
    LayerCount = 0
    TileSize = {}
    ContentRegion = {}
    HorizontalResolution = 0
    VeriticalResolution = 0
    AdditionalData = {}

    def __init__(self, metadata_dict):
        self.__dict__ = metadata_dict

    def get_default_layer(self):
        return 1 if self.LayerCount == 1 else 0

    def get_lod_to_world_scale(self, lod):
        if(lod < 0 or lod > self.MaximumLODLevel):
            raise ValueError(
                f'load {lod} out of range [0-{self.MaximumLODLevel}]')

        scale = 1.0

        if lod != 0:
            for gap in self.LODGaps:
                scale /= gap

        return scale


class Slide:
    def __init__(self, metadata, slide_storage):
        self.metadata = metadata
        self._slide_storage = slide_storage

    def get_lod_to_world_scale(self, lod_level):
        if lod_level == 0:
            return 1
        scale = 1
        for i in range(len(self.metadata.LODGaps)):
            if i > lod_level:
                continue
            scale /= self.metadata.LODGaps[i]
        return scale

    def read_region(self, x, y, width, height, layer=None, lod=None):
        final_layer = layer if layer else self.metadata.get_default_layer()
        final_lod = lod if lod else self.metadata.MinimumLODLevel
        scale_factor = self.get_lod_to_world_scale(final_lod)

        original_width = width
        original_height = height
        if scale_factor != 1:
            x = math.floor(x * scale_factor)
            y = math.floor(y * scale_factor)
            width = math.ceil(width * scale_factor)
            height = math.ceil(height * scale_factor)

        tile_width = self.metadata.TileSize['Width']
        tile_height = self.metadata.TileSize['Height']
        tile_index_left = int(x / tile_width)
        tile_index_top = int(y / tile_height)
        tile_index_right = int((x + width - 1) / tile_width)
        tile_index_bottom = int((y + height - 1)/tile_height)

        new_image = Image.new('RGB', (width, height), (255, 255, 255))

        offset_y = y
        # must +1 to include stop
        for row in range(tile_index_top, tile_index_bottom+1):
            tile_top = row * tile_height
            tile_bottom = (row+1) * tile_height
            offset_x = x
            area_y = offset_y - tile_top
            area_height = min(tile_bottom - offset_y, height - offset_y + y)
            # must +1 to include stop
            for column in range(tile_index_left, tile_index_right+1):
                tile_left = column * tile_width
                tile_right = (column+1) * tile_width
                area_x = offset_x - tile_left
                tile_data = self._slide_storage.get_tile(
                    self.metadata.SlideId, int(row), int(column), final_layer, final_lod)
                logger.debug(
                    f'get tile {row}-{column}-{final_layer}-{final_lod} data')
                area_width = min(tile_right - offset_x, width - offset_x + x)
                if tile_data:
                    with io.BytesIO(tile_data) as fp:
                        image = Image.open(fp)
                        image_valid_area = (area_x,
                                            area_y,
                                            area_width + area_x,
                                            area_height + area_y)
                        cropped_image = image.crop(image_valid_area)
                        # cropped_image.save(f"{image_valid_area}.jpg")
                        new_image.paste(
                            cropped_image, (offset_x - x, offset_y-y))
                offset_x += area_width
            offset_y += area_height

        if new_image.width != original_width or new_image.height != original_height:
            new_image = new_image.resize(
                [original_width, original_height], Image.ANTIALIAS)

        return new_image


def open_slide(slide_id):
    '''
    Open a cloud slide of coriander.

    Args:
        slide_id; the id of slide.

    Returns:
        slide (Slide): the slide.
    '''
    logger.info(f"open slide with slide id {slide_id}")
    slide_storage = SlideCloudStorage()
    metadata = slide_storage.get_metadata(slide_id)
    return Slide(metadata, slide_storage)


def enumerate_tiles(slide_id,
                    begin,
                    stop,
                    stride=(400, 400),
                    size=(512, 512),
                    auto_scaling=True):
    '''
    Get tiles of slide id with begin and end.

    Args:
        begin (list[2]): the begin location to the slide.

        end (list[2]): the end location to the slide.

        stride (tuple(int, int)): the stride to get tiles in Vertical/ Horizontal.

        size (tuple(int,int)): the size of tile image.

        auto-scaling (boolean): should unify slides in same standard by mpp.

    Returns:
        tiles (Generator[Image]): the tile images
    '''
    callbacks = enumerate_tile_funcs(
        slide_id, begin, stop, stride, size, auto_scaling)
    for callback in callbacks:
        yield callback()


def enumerate_tile_funcs(slide_id,
                         begin,
                         stop,
                         stride=(400, 400),
                         size=(512, 512),
                         auto_scaling=True):
    slide = open_slide(slide_id)
    logger.info(f"Enumerate slide {slide_id}  tiles.")
    return __enumerate_slide_tile_funcs(slide, begin, stop, stride, size, auto_scaling)


def enumerate_tiles_count(slide_id,
                          begin,
                          stop,
                          stride=(400, 400),
                          size=(512, 512),
                          auto_scaling=True):
    slide = open_slide(slide_id)
    logger.info(f"Enumerate slide {slide_id}  tiles.")
    begin, stop, stride, size, step, _ = __get_enumrate_parameters(
        slide, begin, stop, stride, size, auto_scaling)

    return step[0] * step[1]


class _StopToken:
    pass


class AsyncContext:
    def __init__(self, slide_id, stride=(400, 400), size=(512, 512), auto_scaling=True, number_of_producer=16):
        tile_callbacks = list(enumerate_content_tile_funcs(slide_id,
                                                           stride,
                                                           size,
                                                           auto_scaling))
        if number_of_producer <= 0:
            raise ValueError(number_of_producer)
        self.number_of_producer = number_of_producer

        tiles_count = len(tile_callbacks)
        split_sections = [int(tiles_count /
                              number_of_producer) * i for i in range(number_of_producer)]
        workers_tile_callbacks = np.split(
            tile_callbacks, split_sections[1:])

        self.workers = []
        self.tile_queue = mp.Queue(number_of_producer*8)
        for index, worker_tile_callbacks in enumerate(workers_tile_callbacks):
            process = mp.Process(target=produce_regions, args=(
                index,
                self.tile_queue,
                worker_tile_callbacks))
            self.workers.append(process)

    def start(self):
        for worker in self.workers:
            worker.start()

    def __call__(self):
        done_worker_count = 0
        while True:
            tile = self.tile_queue.get()
            if isinstance(tile, _StopToken):
                done_worker_count += 1
            else:
                yield tile
            if done_worker_count == self.number_of_producer:
                break
        self.tile_queue.close()


def produce_regions(index, tile_queue, tile_callbacks):
    try:
        logger.info(f"tile producer {index} started.")
        for tile_callback in tile_callbacks:
            tile = tile_callback()
            tile_queue.put(tile)
    except Exception as e:
        logger.warn(f"tile producer {index} error {e}")
    finally:
        tile_queue.put(_StopToken())
        logger.info(f"tile producer {index} finished.")


def get_enumerate_content_tiles_async_context(
        slide_id,
        stride=(400, 400),
        size=(512, 512),
        auto_scaling=True,
        number_of_producer=16):
    return AsyncContext(slide_id, stride, size, auto_scaling, number_of_producer)


def enumerate_content_tiles_async(slide_id, stride=(400, 400), size=(512, 512), auto_scaling=True, number_of_producer=16):
    tile_callbacks = list(enumerate_content_tile_funcs(slide_id,
                                                       stride,
                                                       size,
                                                       auto_scaling))
    if number_of_producer <= 0:
        raise ValueError(number_of_producer)

    tiles_count = len(tile_callbacks)
    split_sections = [int(tiles_count /
                          number_of_producer) * i for i in range(number_of_producer)]
    workers_tile_callbacks = np.split(
        tile_callbacks, split_sections[1:])

    workers = []
    tile_queue = mp.Queue(number_of_producer*8)
    for index, worker_tile_callbacks in enumerate(workers_tile_callbacks):
        process = mp.Process(target=produce_regions, args=(
            index,
            tile_queue,
            worker_tile_callbacks))
        workers.append(process)

    for worker in workers:
        worker.start()

    done_worker_count = 0
    while True:
        tile = tile_queue.get()
        if isinstance(tile, _StopToken):
            done_worker_count += 1
        else:
            yield tile
        if done_worker_count == number_of_producer:
            break
    tile_queue.close()
    for worker in workers:
        worker.join()


def enumerate_content_tiles(slide_id,
                            stride=(400, 400),
                            size=(512, 512),
                            auto_scaling=True,
                            is_async=False):
    '''
    Get tiles in the content area of slide

    Args:
        stride (tuple(int, int)): the stride to get tiles in Vertical/ Horizontal.

        size (tuple(int,int)): the size of tile image.

        auto-scaling (boolean): should unify slides in same standard by mpp.

        is_async(boolean): represent utilize multiple cpus cores to load tiles

    Returns:
        tiles (Generator[Image]): the tile images
    '''

    if is_async:
        cpu_count = os.cpu_count()
        return enumerate_content_tiles_async(slide_id, stride, size, auto_scaling, cpu_count)
    else:
        def enumerate_tile_callbacks():
            callbacks = enumerate_content_tile_funcs(slide_id,
                                                     stride,
                                                     size,
                                                     auto_scaling)
            for callback in callbacks:
                yield callback()
        return enumerate_tile_callbacks()


def enumerate_content_tile_funcs(slide_id, stride=(400, 400), size=(512, 512), auto_scaling=True):
    slide = open_slide(slide_id)
    logger.info(f"Enumerate slide {slide_id} content tiles .")
    begin = int(slide.metadata.ContentRegion['X']), int(
        slide.metadata.ContentRegion['Y'])

    stop = begin[0] + int(slide.metadata.ContentRegion["Width"]
                          ), begin[1]+int(slide.metadata.ContentRegion["Height"])
    return __enumerate_slide_tile_funcs(slide, begin, stop, stride, size, auto_scaling)


def enumerate_content_tiles_count(slide_id,
                                  stride=(400, 400),
                                  size=(512, 512),
                                  auto_scaling=True):
    slide = open_slide(slide_id)
    logger.info(f"Enumerate slide {slide_id} content tiles .")
    begin = int(slide.metadata.ContentRegion['X']), int(
        slide.metadata.ContentRegion['Y'])

    stop = begin[0] + int(slide.metadata.ContentRegion["Width"]
                          ), begin[1]+int(slide.metadata.ContentRegion["Height"])

    begin, stop, stride, size, step, scale = __get_enumrate_parameters(
        slide, begin, stop, stride, size, auto_scaling)

    return step[0] * step[1]


def __get_enumrate_parameters(slide,
                              begin,
                              stop,
                              stride=(400, 400),
                              size=(512, 512),
                              auto_scaling=True):
    if not slide:
        raise ValueError("Can not enumerate tiles with empty slide.")

    if not begin or len(begin) != 2:
        raise ValueError(f"Invalid begin value {begin}")

    if not stop or len(stop) != 2:
        raise ValueError(f"Invalid stop value {stop}.")

    if not stride or len(stride) != 2:
        raise ValueError(f"Invalid stride value {stride}.")

    if not size or len(size) != 2:
        raise ValueError(f"Invalide size value {size}.")
    scale = [1, 1]
    if auto_scaling:
        scale = __get_slide_scale(slide)
    begin = np.array(begin)
    stop = np.array(stop)
    stride = (np.array(stride) * scale).astype(int)
    size = (np.array(size) * scale).astype(int)

    step = ((stop - begin - size)/stride+1).astype(int)
    return (begin, stop, stride, size, step, scale)


class TileFuncWrapper(object):
    def __init__(self,
                 slide,
                 begin,
                 stride,
                 size,
                 scaling_size,
                 col,
                 row):
        self.slide = slide
        self.begin = begin
        self.stride = stride
        self.size = size
        self.scaling_size = scaling_size
        self.col = col
        self.row = row

    def __call__(self):
        x0, y0 = (self.begin + np.array((self.col, self.row))
                  * self.stride).astype(int)
        image = self.slide.read_region(
            x0, y0, self.scaling_size[0], self.scaling_size[1], None, None)
        if image.width != self.size[0] or image.height != self.size[1]:
            image = image.resize(self.size, Image.ANTIALIAS)
        return {
            'location': [x0, y0],
            'image': image,
            'size': list(self.size),
            'step': [self.col, self.row]
        }


def __enumerate_slide_tile_funcs(slide, begin, stop, stride, size, auto_scaling=True):
    begin, stop, stride, scaling_size, step, scale = __get_enumrate_parameters(
        slide, begin, stop, stride, size, auto_scaling)
    for row in range(step[1]):
        for col in range(step[0]):
            yield TileFuncWrapper(slide, begin, stride, size, scaling_size, col, row)


def __get_slide_scale(slide):
    mpp_x = get_config('MICRON_PER_PIXEL_X')
    mpp_y = get_config('MICRON_PER_PIXEL_Y')
    slide_metadata = slide.metadata
    if slide_metadata.HorizontalResolution and \
            slide_metadata.HorizontalResolution > 0 and \
            slide_metadata.VerticalResolution and \
            slide_metadata.VerticalResolution > 0:
        return mpp_x/slide_metadata.HorizontalResolution, \
            mpp_y/slide_metadata.VerticalResolution
    return [1, 1]
