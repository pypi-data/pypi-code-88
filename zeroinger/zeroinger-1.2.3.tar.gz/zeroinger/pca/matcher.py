from typing import List
from zeroinger.text import TextFile
from zeroinger.file import PathUtil
import ahocorasick
from collections import defaultdict
from logzero import logger
from .area import Area, AreaPrediction, AreaWithStreetVillage
from .adcode_loader import AdcodeLoader
import json
from .alias_builder import AliasBuilder


class PcaMatcher:
    ac = None
    adcode2area_dict = None
    adcode2stree_village = None

    def __init__(self):
        self.ac = None
        self.alias_builder = AliasBuilder()
        self._overall_build()
        pass

    def _overall_build(self):

        if PcaMatcher.ac is None or PcaMatcher.adcode2area is None:
            logger.info("PcaMatcher|build index|start")
            PcaMatcher.ac = ahocorasick.Automaton()
            loader = AdcodeLoader()
            area_list = loader.load()
            self._build(area_list)
            logger.info("PcaMatcher|build index|end")
            pass
        self.ac = PcaMatcher.ac

    def _build(self, area_list: List[Area]):
        # 构造前缀书匹配 省市区
        name2area_list = defaultdict(list)
        for area in area_list:
            name_list = self.alias_builder.build_alias(area)
            for name in name_list:
                name2area_list[name].append(area)
        for k, v in name2area_list.items():
            PcaMatcher.ac.add_word(k, (k, v))
        PcaMatcher.ac.make_automaton()
        # 构造adcode查询区域名称
        PcaMatcher.adcode2area_dict = {}
        for area in area_list:
            PcaMatcher.adcode2area_dict[area.adcode] = area
        # 构造根据adcode查询下属的街道村镇信息
        freader = open(PathUtil.path2code(__file__, 'area2street_village.json'), encoding='utf-8')
        PcaMatcher.adcode2stree_village = json.load(freader)
        freader.close()

    def _match_without_comb(self, text: str) -> List[AreaPrediction]:
        """
        给定一个文本预测其结果
        1. 去除其中重叠的预测结果，序列中靠前的优先级高
        2. 从前向后组合可能的地址
        :param text:
        :return:
        """
        list_ret = []
        for end_index, value in self.ac.iter(text):
            list_ret.append([end_index - len(value[0]) + 1, end_index, value[0], value[1]])
        list_ret = self._process_overlap(text, list_ret)
        ret = []
        for item in list_ret:
            start, end, name, ent_list = item
            pred = AreaPrediction()
            pred.set_prediction(ent_list)
            level = ent_list[0].level()
            if level == 'AREA':
                pred.set_raw_info(area_text=name, area_pos=start)
            if level == 'CITY':
                pred.set_raw_info(city_text=name, city_pos=start)
            if level == 'PROV':
                pred.set_raw_info(prov_text=name, prov_pos=start)
            ret.append(pred)
        return ret

    def match(self, text: str, enable_comb: bool = True) -> List[AreaPrediction]:
        """
        匹配文本中的省市区信息
        :param text 文本
        :param enable_comb 是否对匹配出对片段进行组合
        :return
        """

        pred_list = self._match_without_comb(text)
        if enable_comb:
            return self._process_comb(text, pred_list)
        else:
            return pred_list

    def adcode2area(self, adcode: str) -> Area:
        """
        通过adcode查找
        """
        return PcaMatcher.adcode2area_dict.get(adcode, None)

    def list_street_village_by_name(self, area_name: str) -> List[AreaWithStreetVillage]:
        """
        通过获取当前省市区下的街道村镇列表
        """
        area_pred_list = self.match(area_name, enable_comb=True)
        ret = []
        for area_pred in area_pred_list:

            if area_pred.area_list is not None and len(area_pred.area_list) > 0:
                for area in area_pred.area_list:
                    code = area.adcode
                    ret.extend(self.list_street_village_by_adcode(code))
        return ret

    def list_street_village_by_adcode(self, adcode: str) -> List[AreaWithStreetVillage]:
        ret = []
        # 省份
        if adcode.endswith('0000'):
            for k, v in PcaMatcher.adcode2stree_village.items():
                if k[:2] == adcode[:2]:
                    ret.append(AreaWithStreetVillage(self.adcode2area(k), v))
        # 城市
        elif adcode.endswith('00'):
            for k, v in PcaMatcher.adcode2stree_village.items():
                if k[:4] == adcode[:4]:
                    ret.append(AreaWithStreetVillage(self.adcode2area(k), v))
        # 区域
        else:
            area = self.adcode2area(adcode)
            data = PcaMatcher.adcode2stree_village.get(adcode, None)
            if data is not None:
                ret.append(AreaWithStreetVillage(area, data))
        return ret

    def _process_overlap(self, text: str, list_ret: list) -> list:
        """
        处理重叠的问题
        1.完全包含的关系，保留最长的
        2.不完全重叠，保留靠前的
        :param text:
        :param list_ret:
        :return:
        """
        # 删除完全被包含的元素
        overlap_cache = []
        for i in range(len(list_ret)):
            start = list_ret[i][0]
            end = list_ret[i][1]
            skip_mark = False
            for j in range(len(list_ret)):
                if i == j:
                    continue
                if start >= list_ret[j][0] and end <= list_ret[j][1]:
                    skip_mark = True
                    break
            if not skip_mark:
                overlap_cache.append(list_ret[i])
                # print(list_ret[i])
        # 删除和前面元素重叠的部分
        ret = []
        for i in range(len(overlap_cache)):
            # 如果我是第一个直接跳过
            if len(ret) == 0:
                ret.append(overlap_cache[i])
                continue
            if overlap_cache[i][0] > ret[-1][1]:
                ret.append(overlap_cache[i])
            else:
                continue
        return ret

        pass

    def _process_comb(self, text: str, pred_list: List[AreaPrediction]) -> List[AreaPrediction]:
        """
        对地址序列进行组装
        0. 数据结构转换为预测结果类型
        1. 对相邻的前后两个列表进行组合枚举
        2. 判断每一个枚举是否能够形成组合关系，
        :param text:
        :param pred_list:
        :return:
        """
        ret = []
        if len(pred_list) <= 1:
            return pred_list
        last_pred = pred_list[0]
        for i in range(1, len(pred_list)):
            cur_pred = pred_list[i]
            if self._can_merge4text(last_pred, cur_pred):
                area_can = False
                for j in range(len(last_pred.area_list)):
                    if area_can:
                        break
                    area_a = last_pred.area_list[j]
                    for k in range(len(cur_pred.area_list)):
                        area_b = cur_pred.area_list[k]
                        can, area_new = self._can_merge4area(area_a, area_b)
                        if can:
                            area_can = True
                            last_pred.area_list = [area_new]
                            break
                    if area_can:
                        break
                if area_can:
                    if self._is_empty(last_pred.prov_text):
                        last_pred.prov_text = cur_pred.prov_text
                        last_pred.prov_pos = cur_pred.prov_pos
                    if self._is_empty(last_pred.city_text):
                        last_pred.city_text = cur_pred.city_text
                        last_pred.city_pos = cur_pred.city_pos
                    if self._is_empty(last_pred.area_text):
                        last_pred.area_text = cur_pred.area_text
                        last_pred.area_pos = cur_pred.area_pos
                    continue
            ret.append(last_pred)
            last_pred = cur_pred
        ret.append(last_pred)
        return ret

    def _is_empty(self, text: str) -> bool:
        return text is None or text == ''

    def _can_merge4area(self, area_a: Area, area_b: Area):
        """
        判断两个区域信息是否可以合并
        :param area_a:
        :param area_b:
        :return:
        """
        text_a = '{}{}{}'.format(area_a.prov, area_a.city, area_a.area)
        text_b = '{}{}{}'.format(area_b.prov, area_b.city, area_b.area)

        if text_a in text_b:
            return True, area_b
        if text_b in text_a:
            return True, area_a
        return False, None

    def _can_merge4text(self, pred_a: AreaPrediction, pred_b: AreaPrediction):
        """
        判断省市区的描述信息是否重复，比如都描述了xx省，则不适宜合并
        :param pred_a:
        :param pred_b:
        :return:
        """
        if not self._is_empty(pred_a.prov_text) and not self._is_empty(pred_b.prov_text):
            return False
        if not self._is_empty(pred_a.city_text) and not self._is_empty(pred_b.city_text):
            return False
        if not self._is_empty(pred_a.area_text) and not self._is_empty(pred_b.area_text):
            return False
        return True
        pass


def test_alias_builder():
    loader = AdcodeLoader()
    area_list = loader.load()
    alias_builder = AliasBuilder()
    for area in area_list:
        text, level = alias_builder._find_name(area)
        mark = False
        for k in ['自治', '盟', '旗']:
            if k in text:
                mark = True
        if mark:
            print(area, alias_builder.build_alias(area))
