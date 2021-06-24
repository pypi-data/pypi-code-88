import numpy as np
import cv2
from scipy import ndimage
from pdf2txt.core.tree import Node
import pdf2txt.doc_analyzer.img as iu
from pdf2txt.utils import BoundingBox, is_ovarlaping_with_objects

DEFAULT_X_SEPARATOR_WIDTH_RATIO=0.004
DEFAULT_Y_SEPARATOR_HEIGHT_RATIO=0.0035
MIN_HEADER_FOOTER_HEIGHT=0.08
MIN_AREA_HIEGHT_RATIO=0.06
MIN_AREA_WIDTH_RATIO=0.24

class RegionExtractor:
    h_separator_size = DEFAULT_X_SEPARATOR_WIDTH_RATIO
    v_separator_size = DEFAULT_Y_SEPARATOR_HEIGHT_RATIO

    def __init__(self, src, min_area_height=MIN_AREA_HIEGHT_RATIO, min_area_width=MIN_AREA_WIDTH_RATIO):

        self.min_area_height = min_area_height
        self.min_area_width = min_area_width
        self.objects = None
        self.__src=src


    def regions_from_spaces(self, image, vertical_separator_width=DEFAULT_X_SEPARATOR_WIDTH_RATIO, horizental_separator_width=DEFAULT_Y_SEPARATOR_HEIGHT_RATIO):

        bbox = BoundingBox(top=0, left=0, right=image.shape[1], bottom=image.shape[0])

        if vertical_separator_width:
            self.v_separator_size = int(vertical_separator_width * image.shape[1]+1)
        if horizental_separator_width:
            self.h_separator_size = int(horizental_separator_width*image.shape[0]+1)

        self.__src=image
        splits = self.first_canvas_split(page=image, bbox=bbox)
        regions=[]

        for split in splits:
            sub_regions = []
            if split:
                sub_regions.extend(self.split_tree_of_rectangles(image, split).get_leaf_nodes())
            if sub_regions:
                regions.append(sub_regions)
        return regions

    def split_tree_of_rectangles(self, page, bbox, split_direction='all', method='pixels', step=0):
        # possible values for split_direction: 'all',  'horizental', 'vertical'
        tree = Node(bbox)

        split_vertical = False
        split_horizental = False

        if split_direction == 'all':
            split_vertical = True
            split_horizental = True
        elif split_direction in ['vertical', 'v']:
            split_vertical = True
        elif split_direction in ['horizental', 'h']:
            split_horizental = True
        else:
            raise Exception("split_direction have to be either 'all', 'vertical' , 'v  'horizental' or 'h'")
        split = (None, None)
        if split_vertical:
            split = self._split_region_vertical(page, area=bbox, min_width=int(MIN_AREA_WIDTH_RATIO*page.shape[1]))

        if split == (None, None):
            if split_horizental:
                split = self._split_region_horizental(page, area=bbox, min_height=int(MIN_AREA_HIEGHT_RATIO*page.shape[0]), split_by_largest_gap=True)

        if split != (None, None):
            if split[0]:
                tree.left = self.split_tree_of_rectangles(page, split[0], split_direction, method, step + 1)
            if split[1]:
                tree.right = self.split_tree_of_rectangles(page, split[1], split_direction, method, step + 1)
        return tree

    def first_canvas_split(self, page, bbox):
        # possible values for split_direction: 'all',  'horizental', 'vertical'
        tree = Node(bbox)
        splits = self._split_region_vertical(page, area=bbox, min_width=int(MIN_AREA_WIDTH_RATIO*page.shape[1]))

        if splits !=(None, None):
            return splits

        splits = self._split_region_horizental(page, area=bbox, min_height=int(MIN_HEADER_FOOTER_HEIGHT*page.shape[0]))
        if splits != (None, None):
            splits2=self._split_region_horizental(page, area=splits[1], min_height=int((MIN_HEADER_FOOTER_HEIGHT*page.shape[0])/2))

            if splits2 !=(None, None):
                splits=list(splits)
                splits[1]=splits2[0]
                splits.append(splits2[1])


#        iu.show_and_wait('After split', self.__src)

        return tuple(splits)

    def _compute_pixel_count(self, page, region, axis=1, method='pixels'):
        if method=='pixels':
            region = page[region.top:region.bottom, region.left:region.right]
            return np.sum(region, axis=axis)
        elif method=='objects':
            nb_overlaps=[]
            if axis==1:
                for top in range(int(region.top), int(region.bottom)):
                    separator = BoundingBox(left=region.left, right=region.right, top=top, bottom=top+1)
                    nb_overlaps.append(is_ovarlaping_with_objects(separator, self.objects))
            elif axis==0:
                for left in range(int(region.left), int(region.right)):
                    right = left + 1
                    separator = BoundingBox(left=left, right=right, top=region.top, bottom=region.bottom)
                    nb_overlaps.append(is_ovarlaping_with_objects(separator, self.objects))

            return np.array([int(val) for val in nb_overlaps])
        else:
            raise Exception("Split method should be either 'pixels' or 'objects ")

    def _split_region_horizental(self, page, area, min_height, split_by_largest_gap=False, bottom_up=False):

        r1 = None
        r2 = None

        if bottom_up:
            page=cv2.flip(page, 0)

        pixel_counts = self._compute_pixel_count(page, area, axis=1, method='pixels')
        i=1
        while pixel_counts[-i] == 0:
            pixel_counts[-i] = 16*255
            i+=1
        i=0
        while pixel_counts[i] == 0:
            pixel_counts[i] = 16*255
            i+=1

        split_indices, labels, s = self.get_gaps_by_largest(pixel_counts, sort_by_largest=split_by_largest_gap)
        if len(split_indices) > 0:
            indices = np.where(labels == split_indices[0] + 1)
            i=0
            split_y = indices[0][int(len(indices[0]) / 2)]
            height_above=split_y
            height_below=area.bottom-(area.top+split_y)

            while (i < len(split_indices)) and(len(indices[0]) < self.h_separator_size or (height_above<min_height or height_below<min_height)):
                indices = np.where(labels == split_indices[i] + 1)
                split_y = indices[0][int(len(indices[0]) / 2)]
                height_above = split_y
                height_below = area.bottom - (area.top + split_y)
                i+=1
            if i==len(split_indices) and (len(indices[0]) >= self.h_separator_size and (height_above>=min_height and height_below>=min_height)):
                pass
            elif i>= len(split_indices):
                return r1, r2



            r1 = BoundingBox(top=area.top, left=area.left, right=area.right,
                                                      bottom=area.top + split_y)
            r2 = BoundingBox(top=area.top + split_y, left=area.left, right=area.right,
                                                      bottom=area.bottom)

        return r1, r2

    def _split_region_vertical(self, page, area, min_width):
        from pdf2txt.core.page import Region

        r1 = None
        r2 = None
#        print(area)
        pixel_counts = self._compute_pixel_count(page, area, axis=0, method='pixels')

        i=1
        while pixel_counts[-i] == 0:
            pixel_counts[-i] = 16*255
            i+=1
        i=0
        while pixel_counts[i] == 0:
            pixel_counts[i] = 16*255
            i+=1


        split_indices, labels, s = self.get_gaps_by_largest(pixel_counts, sort_by_largest=True)

        if len(split_indices) > 0:
            i=0
            indices = np.where(labels == split_indices[i] + 1)
            split_x = indices[0][int(len(indices[i]) / 2)]

            width_left=split_x
            width_right=area.right-(area.left+split_x)
            while (i < len(split_indices)) and (len(indices[0]) < self.h_separator_size or (width_left<min_width-int(len(indices[0])/2) or  width_right<min_width-int(len(indices[0])/2))):
                indices = np.where(labels == split_indices[i] + 1)
                split_x = indices[0][int(len(indices[0]) / 2)]
                width_left = split_x
                width_right = area.right - (area.left + split_x)
                i+=1


            if i==len(split_indices) and (len(indices[0]) >= self.h_separator_size and (width_left>=min_width-int(len(indices[0])/2) and  width_right>=min_width-int(len(indices[0])/2))):
                pass
            elif i>= len(split_indices):
                return r1, r2


            r1 = BoundingBox(top=area.top, left=area.left, right=area.left + split_x, bottom=area.bottom)
            r2 = BoundingBox(top=area.top, left=area.left + split_x, right=area.right, bottom=area.bottom)




        return r1, r2

    def get_gaps_by_largest(self, arr, sort_by_largest=False):
        labels, num_label = ndimage.label(arr == 0)
        sizes = np.bincount(labels.ravel())
        biggest_labels=list(range(len(sizes[1:])))
        if sort_by_largest:
            biggest_labels = (-sizes[1:]).argsort()
        return biggest_labels, labels, sizes
