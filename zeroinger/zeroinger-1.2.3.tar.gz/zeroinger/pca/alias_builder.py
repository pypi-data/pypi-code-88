from typing import List
from zeroinger.text import TextFile
from zeroinger.file import PathUtil
from .area import Area


class AliasBuilder:
    def __init__(self):
        # 特殊的简写,主要是几个少数民族自治区
        self.special_abbre = {
            "内蒙古自治区": "内蒙古",
            "广西壮族自治区": "广西",
            "西藏自治区": "西藏",
            "新疆维吾尔自治区": "新疆",
            "宁夏回族自治区": "宁夏",
            "香港特别行政区": "香港",
            "澳门特别行政区": "澳门"
        }
        self.nations = TextFile.load_lines(PathUtil.path_relative_to_code(__file__, 'nations.txt'))
        self.prov_list = '北京@天津@河北@山西@内蒙古@辽宁@吉林@黑龙江@上海@江苏@浙江省@安徽@福建@江西@山东@河南@湖北@湖南@广东@广西@海南@重庆@四川@贵州@云南@西藏@陕西@甘肃省@青海@宁夏@新疆@台湾@香港特别行政区@澳门@香港@'.split(
            '@')

        self.black_alias = {'互助'}

        pass

    def build_alias(self, area: Area) -> List[str]:
        """
        生成区域简称
        1.特别行政区 + 自治区
        2.省份、城市  直接去除后缀
        3.区县 不去除后缀，因为太容易重名
        4.自治县、盟
        :param area:
        :return:
        """
        name, level = self._find_name(area)
        ret = []
        # 原始名称加入
        ret.append(name)
        # 几个省级自治区 + 特别行政区
        if name in self.special_abbre:
            ret.append(self.special_abbre[name])
        else:
            mark = False
            for k in ['自治', '盟', '旗']:
                if k in name:
                    mark = True
            if mark:
                ret.extend(self._build4nation(name))
        if name.endswith('省') or name.endswith('市'):
            ret.append(name.strip('省').strip('市'))
        new_ret = []
        # 删除过短的名称
        for x in ret:
            if len(x) == 1:
                continue
            if x in self.black_alias:
                continue
            new_ret.append(x)
        # if '互助' in ret:
        #     print(ret, area, new_ret, self.black_alias)
        return list(set(new_ret))

        pass

    def _build4nation(self, name) -> List[str]:
        """
        少数民族处理
        1. AB族自治X
        2. XX盟
        :param name:
        :return:
        """
        ret = []
        if name.endswith('自治县') or name.endswith('自治州'):
            text = name[:-3]
            new_text = text
            while True:
                for x in self.nations:
                    if new_text.endswith(x):
                        new_text = new_text[:-len(x)]
                if text == new_text:
                    break
                text = new_text
            ret.append(text)
            if len(text) > 1:
                ret.append(text + name[-3:])
                ret.append(text + name[-1:])

            pass

        if name.endswith('盟'):
            ret.append(name[:-1])
        for x in ret:
            if x in self.prov_list:
                ret.remove(x)
        return ret

        pass

    def _find_name(self, area: Area) -> (str, int):
        if not self.is_empty(area.area):
            return area.area, 3
        if not self.is_empty(area.city):
            return area.city, 2
        return area.prov, 1

    def is_empty(self, text: str):
        return text is None or text == ''
