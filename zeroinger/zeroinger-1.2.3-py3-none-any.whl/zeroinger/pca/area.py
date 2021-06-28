from dataclasses import dataclass
from typing import List


class Area:
    def __init__(self, prov: str = '', city: str = '', area: str = '', adcode: str = '', citycode: str = ''):
        """

        :param prov:
        :param city:
        :param area:
        :param area_code:
        """
        self.prov = prov
        self.city = city
        self.area = area
        self.adcode = adcode
        self.citycode = citycode

    def level(self):
        if not self.is_empty_str(self.area):
            return 'AREA'
        if not self.is_empty_str(self.city):
            return 'CITY'
        if not self.is_empty_str(self.prov):
            return 'PROV'

    def is_empty_str(self, text: str):
        return text is None or text == ''

    def __str__(self):
        return '{}_{}_{}'.format(self.prov, self.city, self.area)

    def __repr__(self):
        return str(self)


class AreaPrediction:
    """
    存储单条地址预测结果
    """

    def __init__(self, ):
        # 匹配结果在原文中对原始文本及位置
        self.prov_text, self.prov_pos = '', -1
        self.city_text, self.city_pos = '', -1
        self.area_text, self.area_pos = '', -1
        # 结构化结果
        self.certain: bool = True
        self.area_list: List[Area] = []
        pass

    def set_raw_info(self, prov_text: str = '', prov_pos: int = -1, city_text: str = '', city_pos: int = -1,
                     area_text: str = '', area_pos: int = -1):
        """
        :param prov_text:
        :param prov_pos:
        :param city_text:
        :param city_pos:
        :param area_text:
        :param area_pos:
        :return:
        """
        self.prov_text = prov_text
        self.prov_pos = prov_pos
        self.city_text = city_text
        self.city_pos = city_pos
        self.area_text = area_text
        self.area_pos = area_pos

        pass

    def set_prediction(self, area_list: List[Area]):
        self.area_list = area_list
        if len(area_list) > 1:
            self.certain = False
        else:
            self.certain = True

    def __str__(self):
        box = []
        for item in self.area_list:
            box.append(str(item))
        return '@'.join(box)
        pass

    def __repr__(self):
        return str(self)

@dataclass
class AreaWithStreetVillage:
    area: Area
    street2village: dict
