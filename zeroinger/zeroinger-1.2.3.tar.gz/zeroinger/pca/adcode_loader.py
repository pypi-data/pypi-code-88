from typing import List
from zeroinger.file import PathUtil
import csv
from zeroinger.pca.area import Area


class AdcodeLoader:
    def __init__(self):
        pass

    def load(self):
        area_list = []
        NAME = '中文名'
        CITY_CODE = 'citycode'
        ADCODE = 'adcode'
        black_token = ['中华人民共和国', '外国']
        freader = open(PathUtil.path_relative_to_code(__file__, 'adcode.tsv'), 'r', encoding='utf-8')
        reader = csv.DictReader(freader,delimiter='\t')
        last_adcode, last_citycode = None, None
        for data in reader:
            skip_mark = False
            for t in black_token:
                if t in data[NAME]:
                    skip_mark = True
                    break
            if skip_mark:
                continue
            # 省份
            if data[CITY_CODE] is None or data[ADCODE].endswith('0000'):
                if '香港' in data[NAME] or '澳门' in data[NAME]:
                    # 特别行政区
                    area = self.load_city(data[NAME], data[NAME], data[ADCODE], data[CITY_CODE])
                else:
                    # 一个新的省份/直辖市
                    area = self.load_province(data[NAME], data[ADCODE])
                area_list.append(area)
            elif self.is_new_city(area_list, data[CITY_CODE]) or data[ADCODE].endswith('00'):
                prov = self.find_prov4city(area_list, data[ADCODE])
                if prov is None:
                    # 直辖市
                    area = self.load_city(data[NAME], data[NAME], data[ADCODE], data[CITY_CODE])
                else:
                    if data[ADCODE].endswith('00'):
                        # 普通的市区
                        area = self.load_city(prov, data[NAME], data[ADCODE], data[CITY_CODE])
                    else:
                        # 省级直辖县
                        area = self.load_area(prov, '', data[NAME], data[ADCODE], data[CITY_CODE])

                area_list.append(area)
            else:
                if '辖区' in data[NAME] and not data[ADCODE].endswith('00'):
                    continue
                # 区县
                city_area = self.find_city4area(area_list, data[CITY_CODE])
                if city_area is None:
                    print(area_list[-30:])
                    print(data)
                    raise Exception('区县解析异常，未找到对应的城市')
                area = self.load_area(city_area.prov, city_area.city, data[NAME], data[ADCODE], data[CITY_CODE])
                area_list.append(area)

            last_citycode = data[CITY_CODE]
            last_adcode = data[ADCODE]
        freader.close()
        area_list = self.remove_direct_city(area_list)
        return area_list

    def is_new_city(self, area_list: List[Area], citycode: str):
        for area in area_list:
            if area.citycode == citycode:
                return False
        return True

    def find_prov4city(self, area_list: List[Area], adcode: str):
        for area in area_list:
            if area.adcode is not None and area.adcode != '' and area.adcode[:2] == adcode[:2]:
                return area.prov
        return None

    def find_city4area(self, area_list: List[Area], citycode: str):
        for area in area_list:
            if area.citycode is not None and area.citycode != '' and area.citycode == citycode:
                return area
        return None

    def load_province(self, name: str, adcode: str):
        """
        载入省份
        :param name:
        :param adcode:
        :return:
        """
        return Area(name, '', '', adcode)

    def load_city(self, prov: str, city: str, adcode: str, citycode: str):
        """
        直辖市
        :param name:
        :param adcode:
        :param citycode
        :return:
        """
        if '辖区' in city:
            city = prov
        return Area(prov, city, '', adcode, citycode)

    def load_area(self, prov: str, city: str, area: str, adcode: str, citycode: str):
        """

        :param prov:
        :param city:
        :param area:
        :param adcode:
        :return:
        """
        return Area(prov, city, area, adcode, citycode)

    def remove_direct_city(self, area_list: List[Area]):
        """
        对于直辖市，删除其省级标记，否则会出现省份/城市两级重名
        :param area_list:
        :return:
        """
        same_list = set()
        for area in area_list:
            if area.city == area.prov:
                same_list.add(area.prov)
        ret = []
        for area in area_list:
            if (area.city == '' or area.city == None) and area.prov in same_list:
                continue
            ret.append(area)
        return ret


if __name__ == '__main__':
    o = AdcodeLoader()
    o.load()
