# -*- encoding: utf-8 -*-
# @created_at: 2021/6/22 13:59

import re
import pandas as pd
from loguru import logger


regex = ['小于', '小于等于', '小于或等于', '大于1.0并且小于', '大于', '大于等于', '大于或等于',  '等于', '不得大于',
         '高于',
         '低于', '不超过', '以上', '以下', '以内', '＞', '>', '≧', '≥', '-', '—', '~', '=',
           '≮', '大于1.0并且小于', '且', '并且', '＜', '<', '≦', '≤',  '＝', '≯', '上限','超过','不低']
min_regex=['大于1.0并且小于', '大于', '大于等于', '大于或等于',  '等于','高于',
          '以上',   '＞', '>', '≧', '≥', '-', '—', '~', '=',
           '≮', '大于1.0并且小于', '且', '并且',   '＝',  '超过']
def calculate_maxi_min_rjl(data):
    if data is None or data == '' or str(data)=='nan':
        return {'max_rongjilv': '', 'min_rongjilv': ''}
    if '地下' in data:
        data=data.split('地下')[0]
    if '（' in data:
        data = re.sub('（.*?）', '', data)

    lst = re.findall(r'[0-9|.]+', data)
    for _ in range(len(lst)):

        if '不大于' in data:
            data = data.replace('不大于', '小于')
        elif '小于等于' in data:
            data = data.replace('小于等于', '小于')
        elif '不低于' in data:
            data = data.replace('不低于', '大于')
        elif '不高于' in data:
            data = data.replace('不高于', '小于')
        elif '不少于' in data:
            data = data.replace('不少于', '大于')
        elif '>=' in data:
            data = data.replace('>=', '>')
        elif '＞＝' in data:
            data = data.replace('＞＝', '＞')
        elif '<=' in data:
            data = data.replace('<=', '<')
        elif '＜＝' in data:
            data = data.replace('＜＝', '＜')
        elif '不小于' in data:
            data = data.replace('不小于', '大于')
        elif '不超过' in data:
            data = data.replace('不超过', '超过')
        elif '大于或等于' in data:
            data = data.replace('大于或等于', '大于')
        elif '大于等于' in data:
            data = data.replace('大于等于', '大于')
        elif '小于或等于' in data:
            data = data.replace('小于或等于', '小于')





    try:
        lst = re.findall(r'[0-9|.]+', data)
        max_rongjilv = None
        min_rongjilv = None
        max_r = max(lst)
        min_r = min(lst)
        if max_r == min_r:
            if '小于' in data or '小于等于' in data or '小于或等于' in data or '不大于' in data  or '等于' in data or '不得大于' in data or '不高于' in data or '低于' in data or '不超过' in data or '以下' in data or '以内' in data or '＜' in data or '<' in data or '≦' in data or '≤' in data or '<=' in data or '＜＝' in data or '≯' in data or '上限' in data:
                min_rongjilv = ''
                max_rongjilv = max_r
            elif '大于' in data or '大于等于' in data or '大于或等于' in data or '不小于' in data or '不低于' in data or '高于' in data or '不少于' in data or '以上' in data or '＞' in data or '>' in data or '≧' in data or '≥' in data or '>=' in data or '＞＝' in data or '≮' in data or '＝' in data or '不低' in data:
                min_rongjilv = min_r
                max_rongjilv = ''
            else:
                min_rongjilv = max_r
                max_rongjilv = max_r





        else:

            while lst:

                max_r = max(lst)
                min_r = min(lst)
                for j in regex:
                    if j + str(max_r) in data:
                        max_rongjilv = max_r
                        break
                for i in regex:
                    if i+str(min_r) in data or str(min_r) + i in data:
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

        return {'max_rongjilv': max_rongjilv, 'min_rongjilv': min_rongjilv}
    except Exception as e:
        print(e)
        logger.debug(f'解析失败数据为：{data}')
        return data


def calculate_maxi_min_lhl(data):
    if data is None or data == '' or str(data)=='nan':
        return {'max_lhl': '', 'min_lhl': ''}
    lst = re.findall(r'[0-9|.]+[%]?', data)

    for _ in range(len(lst)):

        if '不大于' in data:
            data = data.replace('不大于', '小于')
        elif '小于等于' in data:
            data = data.replace('小于等于', '小于')
        elif '不低于' in data:
            data = data.replace('不低于', '大于')
        elif '不高于' in data:
            data = data.replace('不高于', '小于')
        elif '不少于' in data:
            data = data.replace('不少于', '大于')
        elif '>=' in data:
            data = data.replace('>=', '>')
        elif '＞＝' in data:
            data = data.replace('＞＝', '＞')
        elif '<=' in data:
            data = data.replace('<=', '<')
        elif '＜＝' in data:
            data = data.replace('＜＝', '＜')
        elif '不小于' in data:
            data = data.replace('不小于', '大于')
        elif '不超过' in data:
            data = data.replace('不超过', '超过')
        elif '大于或等于' in data:
            data = data.replace('大于或等于', '大于')
        elif '大于等于' in data:
            data = data.replace('大于等于', '大于')
        elif '小于或等于' in data:
            data = data.replace('小于或等于', '小于')
    try:

        lst = re.findall(r'[0-9|.]+[%]?', data)
        lst1 = [(str(i).replace('%', '')) for i in lst if i]

        max_lhl = max(lst1)
        min_lhl = min(lst1)
        if max_lhl == min_lhl:


            if '小于' in data or '小于等于' in data or '小于或等于' in data or '不大于' in data  or '等于' in data or '不得大于' in data or '不高于' in data or '低于' in data or '不超过' in data or '以下' in data or '以内' in data or '＜' in data or '<' in data or '≦' in data or '≤' in data or '<=' in data or '＜＝' in data or '≯' in data or '上限' in data:
                min_lhl = ''
                max_lhl = max_lhl
            elif '大于' in data or '大于等于' in data or '大于或等于' in data or '不小于' in data or '不低于' in data or '高于' in data or '不少于' in data or '以上' in data or '＞' in data or '>' in data or '≧' in data or '≥' in data or '>=' in data or '＞＝' in data or '≮' in data or '＝' in data or '不低' in data:
                min_lhl = min_lhl
                max_lhl = ''
            else:
                min_lhl = min_lhl
                max_lhl = ''
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
                    lst1.remove(min_lhl)
                elif min_lhl:
                    lst1.remove(max_lhl)
                else:
                    lst1.remove(max_lhl)
                    lst1.remove(min_lhl)

        return {'max_lhl': max_lhl, 'min_lhl': min_lhl}
    except Exception as e:
        logger.debug(f'解析失败数据为：{data}')
        return data


def calculate_maxi_min_jzmd(data):
    if data is None or data == '' or str(data)=='nan':
        return {'max_jzmd': '', 'min_jzmd': ''}

    lst = re.findall(r'[0-9|.]+[%]?', data)
    if lst==[]:
        return {'max_jzmd': '', 'min_jzmd': ''}
    for _ in range(len(lst)):
        for _ in range(len(lst)):

            if '不大于' in data:
                data = data.replace('不大于', '小于')
            elif '小于等于' in data:
                data = data.replace('小于等于', '小于')
            elif '不低于' in data:
                data = data.replace('不低于', '大于')
            elif '不高于' in data:
                data = data.replace('不高于', '小于')
            elif '不少于' in data:
                data = data.replace('不少于', '大于')
            elif '>=' in data:
                data = data.replace('>=', '>')
            elif '＞＝' in data:
                data = data.replace('＞＝', '＞')
            elif '<=' in data:
                data = data.replace('<=', '<')
            elif '＜＝' in data:
                data = data.replace('＜＝', '＜')
            elif '不小于' in data:
                data = data.replace('不小于', '大于')
            elif '不超过' in data:
                data = data.replace('不超过', '超过')
            elif '大于或等于' in data:
                data = data.replace('大于或等于', '大于')
            elif '大于等于' in data:
                data = data.replace('大于等于', '大于')
            elif '小于或等于' in data:
                data = data.replace('小于或等于', '小于')
    try:
        lst = re.findall(r'[0-9|.]+[%]?', data)
        lst1 = [str(i).replace('%', '') for i in lst if i]
        max_jzmd = max(lst1)
        min_jzmd = min(lst1)
        if max_jzmd == min_jzmd:

            if '小于' in data or '小于等于' in data or '小于或等于' in data or '不大于' in data or '等于' in data or '不得大于' in data or '不高于' in data or '低于' in data or '不超过' in data or '以下' in data or '以内' in data or '＜' in data or '<' in data or '≦' in data or '≤' in data or '<=' in data or '＜＝' in data or '≯' in data or '上限' in data:
                min_jzmd = ''
                max_jzmd = max_jzmd
            elif '大于' in data or '大于等于' in data or '大于或等于' in data or '不小于' in data or '不低于' in data or '高于' in data or '不少于' in data or '以上' in data or '＞' in data or '>' in data or '≧' in data or '≥' in data or '>=' in data or '＞＝' in data or '≮' in data or '＝' in data:
                min_jzmd = max_jzmd
                max_jzmd = ''
            else:
                min_jzmd = ''
                max_jzmd = max_jzmd
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

        return {'max_jzmd': max_jzmd, 'min_jzmd': min_jzmd}
    except Exception as e:
        logger.debug(f'解析失败数据为：{data}')
        return data


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
    # data=['20%＜绿地率','绿地率≥25%','0.9> 小于1.0','1.0<容积率＜3.0，容积率≯2.0, 容积率>4.0','居住用地  ≤2.6；  商业用地  ≤2.5', '小于1.6、S2;小于1.8大于1.0', '小于1.8大于1.0、S2;小于1.6', 'S1：不大于1.8不小于1.0、S2;不大于1.6']
    data=['35.13','1.49','≧32.64％','≥35.2','绿地率≥32.5%','≥32.5%']
    print(calculate_maxi_min_rjl(data[1]))
