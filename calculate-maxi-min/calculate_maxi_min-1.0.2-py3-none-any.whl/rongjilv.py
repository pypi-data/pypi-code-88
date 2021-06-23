# -*- encoding: utf-8 -*-
# @created_at: 2021/6/22 13:59

import re
import pandas as pd
from loguru import logger

regex = ['小于', '小于等于', '小于或等于', '大于1.0并且小于', '大于', '大于等于', '大于或等于', '不大于', '不小于', '等于', '不得大于', '不低于', '不高于',
                 '高于',
                 '低于', '不少于', '不超过', '以上', '以下', '以内', '＞', '>', '≧', '≥', '-', '—', '~', '=',
                 '>=', '＞＝', '≮', '大于1.0并且小于', '且', '并且', '＜', '<', '≦', '≤', '<=', '＜＝', '＝', '≯', '上限']
def calculate_maxi_min_rjl(data):
    try:
        lst = re.findall(r'[0-9]+[.][0-9]+', data)

        max_rongjilv = None
        min_rongjilv = None
        max_r = max(lst)
        min_r = min(lst)
        if max_r == min_r:

            if '小于' in data or '小于等于' in data or '小于或等于' in data or '不大于' in data or '等于' in data or '不得大于' in data or '不高于' in data or '低于' in data or '不超过' in data or '以下' in data or '以内' in data or '＜' in data or '<' in data or '≦' in data or '≤' in data or '<=' in data or '＜＝' in data or '＝' in data or '≯' in data or '上限' in data:
                min_rongjilv = None
                max_rongjilv=max_r
            elif '大于' in data or  '大于等于' in data or  '大于或等于' in data or '不小于' in data or '不低于' in data or '高于' in data or '不少于' in data or '以上' in data or '＞' in data or  '>' in data or  '≧' in data or  '≥' in data or '>=' in data or  '＞＝' in data or  '≮' in data:
                min_rongjilv=min_r
                max_rongjilv = None



        else:

            while lst:

                for j in regex:
                    if j + str(max_r) in data:
                        max_rongjilv = max_r
                        break
                for i in regex:
                    if str(min_r) + i in data:
                        min_rongjilv = min_r
                        break
                if max_rongjilv and min_rongjilv:
                    break
                elif max_rongjilv:
                    lst.remove(min_r)
                elif min_rongjilv:
                    lst.remove(max_r)
                else:
                    lst.remove(max_r)
                    lst.remove(min_r)

        return {'max_rongjilv':max_rongjilv, 'min_rongjilv':min_rongjilv}
    except Exception as e:
        print(e)
        logger.debug(f'{data}出现问题')

def calculate_maxi_min_lhl(data):
    try:
        lst = re.findall(r'[0-9|.]+%', data)
        lst1 = [float(str(i).replace('%', '')) for i in lst if i]
        max_lhl = int(max(lst1))
        min_lhl = int(min(lst1))
        if max_lhl == min_lhl:

            if '小于' in data or '小于等于' in data or '小于或等于' in data or '不大于' in data or '等于' in data or '不得大于' in data or '不高于' in data or '低于' in data or '不超过' in data or '以下' in data or '以内' in data or '＜' in data or '<' in data or '≦' in data or '≤' in data or '<=' in data or '＜＝' in data  or '≯' in data or '上限' in data:
                min_lhl = None
                max_lhl = max_lhl
            elif '大于' in data or '大于等于' in data or '大于或等于' in data or '不小于' in data or '不低于' in data or '高于' in data or '不少于' in data or '以上' in data or '＞' in data or '>' in data or '≧' in data or '≥' in data or '>=' in data or '＞＝' in data or '≮' in data or '＝' in data:
                min_lhl = max_lhl
                max_lhl = None
            else:
                min_lhl = max_lhl
                max_lhl = None
        else:

            while lst1:

                for j in regex:
                    if j + str(max_lhl) in data:
                        max_lhl = max_lhl
                        break
                for i in regex:
                    if str(min_lhl) + i in data:
                        min_lhl = min_lhl
                        break
                if max_lhl and min_lhl:
                    break
                elif max_lhl:
                    lst.remove(min_lhl)
                elif min_lhl:
                    lst.remove(max_lhl)
                else:
                    lst.remove(max_lhl)
                    lst.remove(min_lhl)

        return {'max_lhl':max_lhl, 'min_lhl':min_lhl}
    except Exception as e:
        print(e)
        print(data)
        logger.debug(f'{data}出现问题')
def calculate_maxi_min_jzmd(data):
    try:
        lst = re.findall(r'[0-9|.]+%', data)
        lst1 = [float(str(i).replace('%', '')) for i in lst if i]
        max_jzmd = int(max(lst1))
        min_jzmd = int(min(lst1))
        if max_jzmd == min_jzmd:

            if '小于' in data or '小于等于' in data or '小于或等于' in data or '不大于' in data or '等于' in data or '不得大于' in data or '不高于' in data or '低于' in data or '不超过' in data or '以下' in data or '以内' in data or '＜' in data or '<' in data or '≦' in data or '≤' in data or '<=' in data or '＜＝' in data  or '≯' in data or '上限' in data:
                min_jzmd = None
                max_jzmd = max_jzmd
            elif '大于' in data or '大于等于' in data or '大于或等于' in data or '不小于' in data or '不低于' in data or '高于' in data or '不少于' in data or '以上' in data or '＞' in data or '>' in data or '≧' in data or '≥' in data or '>=' in data or '＞＝' in data or '≮' in data or '＝' in data:
                min_jzmd = max_jzmd
                max_jzmd = None
            else:
                min_jzmd = max_jzmd
                max_jzmd = None
        else:

            while lst1:

                for j in regex:
                    if j + str(max_jzmd) in data:
                        max_jzmd = max_jzmd
                        break
                for i in regex:
                    if str(min_jzmd) + i in data:
                        min_jzmd = min_jzmd
                        break
                if max_jzmd and min_jzmd:
                    break
                elif max_jzmd:
                    lst.remove(min_jzmd)
                elif min_jzmd:
                    lst.remove(max_jzmd)
                else:
                    lst.remove(max_jzmd)
                    lst.remove(min_jzmd)

        return {'max_jzmd':max_jzmd, 'min_jzmd':min_jzmd}
    except Exception as e:
        print(e)
        print(data)
        logger.debug(f'{data}出现问题')

def read_csv():
    data_list = list()
    td = pd.read_csv('建筑密度.csv')

    for data in td['build_density_html']:
        new_dict = {
            'build_density_html': data,
            'new_greet_ratio_html': calculate_maxi_min_lhl(data)
        }
        data_list.append(new_dict)
    df = pd.DataFrame(data_list, columns=["build_density_html", "new_greet_ratio_html"])
    df.to_csv('xt_jzmd_data.csv')


if __name__ == '__main__':
    # print(calculate_maxi_min_lhl('20%'))
    read_csv()
