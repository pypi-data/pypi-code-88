import os
import pdf2txt.doc_analyzer.img as iu
from pdf2txt.doc_analyzer.imageprocessor import ImageProcessor
from pdf2txt.doc_analyzer.text_segmenter import TextSegmenter
import cv2
import numpy as np

from pdf2txt.doc_analyzer.connected_components import get_connected_components
from pdf2txt.doc_analyzer.region import RegionExtractor


class PageAnalyzer:
    def __init__(self, page, debug=False):

        self.__page=page
        self.__raw_image=page.page_image.copy()
        self.__page.page_image=cv2.cvtColor(np.asarray(page.page_image), code=cv2.COLOR_RGB2BGR)
        self.__src = self.__page.page_image.copy()
        self.__preprocessor = ImageProcessor(self.__page, debug)
        self.__processed = self.__preprocessor.preprocess()
        self.__img_text = None
        self.__ccs_text = None
        self.__ccs_non_text = []
        self.__debug = debug
        self.__img_name = "image"
        self.__region_extractor=RegionExtractor(self.__processed)

    @property
    def image(self):
        return self.__src
    @property
    def raw_image(self):
        return self.__raw_image

    def analyze_page(self):
        self.__ccs_text = get_connected_components(self.__processed)
        self.__image_blocks=TextSegmenter(self.__processed, self.__ccs_text,
                             self.__src, self.__debug).segment_text()

        for text_block in self.__page.text_lines:
            if "value" in text_block:
                if text_block['value']=="▪" or text_block["width"]<=3 or text_block["top"]>self.__page.page_image.shape[0]/5:
                    continue
                if text_block['value'].strip()=="":
                    continue
            x, y, w, h = int(text_block["left"]),int(text_block["top"]),int(text_block["width"]),int(text_block["height"])


            cv2.rectangle(self.__image_blocks, (x, y+2), (x + w, y + h-2), (255, 0, 0), -1)

    def extract_regions(self):

        if not hasattr(self, '__image_blocks'):
            self.analyze_page()

        if self.__debug:
            iu.show_and_wait('Before Regions', self.__image_blocks)
        all_regions= self.__region_extractor.regions_from_spaces(self.__image_blocks)


        if self.__debug:
            for regions in all_regions:
                    for region in regions:
                        cv2.rectangle(self.__src, (region.left, region.top), (region.right, region.bottom), (255, 0, 0), 4)
    #            if self.__debug:
            iu.show_and_wait('Regions', self.__src)

        return all_regions


