from collections import defaultdict
from typing import Dict, List

from .base import MatchBase
# from base import MatchBase


class SundayMatch(MatchBase):
    
    def index(self, probe: str) -> int:
        """Exact match"""
        # 模板字符串和探针字符串的长度
        template = self.template
        nt = len(template)
        np = len(probe)
        # 统计 probe 中所有字符出现的最大索引位置
        char_pos = {}
        for idx, char in enumerate(probe):
            char_pos[char] = idx
        
        index = 0 # 母串上与子串首字符比较的位置
        while index <= nt - np:
            is_matched = True
            for i, pi in enumerate(probe):
                # 子串第i个字符与母串第index+i个字符不匹配时
                if template[index+i] != pi:
                    is_matched = False
                    # 下一个移动位置超过母串长度时，匹配失败
                    if index + np >= probent:
                        return -1
                    # 可以继续移动子串 #
                    # 判断母串上下一个移动位置的字符是否在子串中
                    pos = char_pos.get(template[index + np])
                    if pos is None:
                        index += np + 1
                    else:
                        index += np - pos
                    break
            if is_matched:
                return index
        return -1

    def blurry_index(self, probe: str, allowed_mismatches: int) -> int:
        """Blurry match"""
        # 模板字符串和探针字符串的长度
        template = self.template
        nt = len(template)
        np = len(probe)
        # 统计 probe 中所有字符出现的最大索引位置
        char_pos = {}
        for idx, char in enumerate(probe):
            char_pos[char] = idx
        
        index = 0 # 母串上与子串首字符比较的位置
        while index <= nt - np:
            num_mismatches = 0 # 当前位置下的错配数
            for i, pi in enumerate(probe):
                # 子串第i个字符与母串第index+i个字符不匹配时
                if template[index+i] != pi:
                    num_mismatches += 1
                    # 当错配数超过阈值时考虑移动子串
                    if num_mismatches > allowed_mismatches:
                        # 下一个移动位置超过母串长度时，匹配失败
                        if index + np >= nt:
                            return -1
                        # 否则可以继续移动子串
                        pos = char_pos.get(template[index + np])
                        if pos is None:
                            index += np + 1
                        else:
                            index += np - pos
                        break
            if num_mismatches <= allowed_mismatches:
                return index
        return -1


if __name__ == '__main__':
    template = "this is a simple example"
    probe =             'example'
    print(SundayMatch(template).blurry_index(probe, 0))
    print(SundayMatch(template).blurry_index(probe, 1))
    print(SundayMatch(template).blurry_index(probe, 2))
    print(SundayMatch(template).blurry_index(probe, 3))