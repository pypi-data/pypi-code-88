import cv2 as cv
import itertools
import numpy as np
import pdf2txt.doc_analyzer.img as iu


from pdf2txt.doc_analyzer.connected_components import get_connected_components
from pdf2txt.doc_analyzer.connected_components import intersection_percentage
from pdf2txt.doc_analyzer.connected_components import union, list_contains_tuple


class TextSegmenter:
    def __init__(self, img, ccs_text, src=None, debug=False):
        super().__init__()
        self.__img = img.copy()
        self.__ccs_text = ccs_text.copy()
        self.src = src.copy()
        self.__debug = debug

    def segment_text(self):
        text_blocks = self.__get_text_blocks()

        return text_blocks


    def __get_text_blocks(self):
        ccs = self.__group_intersected_regions(self.__img)
        text_blocks = ccs.copy()

        if self.__debug:
            src_copy = self.src.copy()
            for text_block in text_blocks:
                x, y, w, h = text_block.get_rect()
                cv.rectangle(src_copy, (x, y), (x + w, y + h), (255, 0, 0), 1)
            iu.show_and_wait('Text Blocks', src_copy)


        text_blocks=self.__remove_small_areas(text_blocks)

        if self.__debug:
            img_blocks = self.src.copy()
            for text_block in text_blocks:
                x, y, w, h = text_block.get_rect()
                cv.rectangle(img_blocks, (x, y), (x + w, y + h), (255, 0, 0), 1)
            iu.show_and_wait('Remove small blocks ', img_blocks)

        text_block_rects=self.__combine_blocks(text_blocks)

        if self.__debug:
            img_blocks = self.src.copy()
            for text_block in text_block_rects:
                x, y, w, h = text_block
                cv.rectangle(img_blocks, (x, y), (x + w, y + h), (255, 0, 0), 1)
            iu.show_and_wait('Combined blocks ', img_blocks)

        blank = np.zeros(self.__img.shape[0:2], np.uint8)
        for text_line in text_block_rects:
            x, y, w, h = text_line
            cv.rectangle(blank, (x, y), (x + w, y + h), 255, -1)


        if self.__debug:
            # img_blocks = self.src.copy()
            # for text_block in text_block_rects:
            #     x, y, w, h = text_block
            #     cv.rectangle(img_blocks, (x, y), (x + w, y + h), (255, 0, 0), 4)
            iu.show_and_wait('CombinedText Blocks mask', blank)

        return blank

    def __remove_small_areas(self, areas):
        return [a for a in areas if a.get_area() >100]

    def __group_intersecterd_blocks(self, text_blocks):

        for blok1 in text_blocks:
            for blok2 in text_blocks:
                if intersection_percentage(blok1, blok2)>0:
                    rects_union = union(blok1.get_rect(), blok2.get_rect())
                    text_blocks.remove(blok2)
                    blok1.__rect=rects_union

        return text_blocks


    def __combine2(self, text_blocks):

        merged = [text_blocks[0]]
        for current in text_blocks[1:]:
            intersection_found=False
            for i, b in enumerate(merged):
                if intersection_percentage(current, merged[i]):
                    merged[i] = union(current, merged[i])
                    intersection_found = True
            if not intersection_found and not list_contains_tuple(merged,current):
                merged.append(current)
        return merged

    def __fix_overlapping(self, text_blocks):
        for i, b1 in enumerate(text_blocks):
            for j in range(0, i):
                if intersection_percentage(text_blocks[i],text_blocks[j]):
                    text_blocks[i]=union(text_blocks[i], text_blocks[j])
                    text_blocks.remove(text_blocks[j])

                    return self.__fix_overlapping(text_blocks)
        return text_blocks

    def __combine_blocks(self, text_blocks):
        merged=[b.get_rect() for b in text_blocks]
        return self.__fix_overlapping(merged)



    def __intersect_wilh_one(self, boxa, list_boxes):
        for boxb in list_boxes:
            return intersection_percentage(boxa, boxb)>0

    def __group_intersected_regions(self, img_text):

        img_text = img_text.copy()

        closing = cv.morphologyEx(img_text, cv.MORPH_CLOSE, (1,1), iterations=2)
        ccs_text = get_connected_components(closing, external=True)
        img_text = np.zeros(img_text.shape, np.uint8)

        cv.drawContours(img_text, [cc.get_contour() for cc in ccs_text], -1, 255, -1)

        if self.__debug:
            iu.show_and_wait('Before Group Intersected', img_text)

        ccs_text = get_connected_components(img_text, external=True)

        for text_block in ccs_text:
            x, y, w, h = text_block.get_rect()
            cv.rectangle(img_text, (x, y), (x + w, y + h), (255, 0, 0), 1)

        if self.__debug:
            iu.show_and_wait('Show Rectangles (Morph-Close)', img_text)

        return ccs_text

