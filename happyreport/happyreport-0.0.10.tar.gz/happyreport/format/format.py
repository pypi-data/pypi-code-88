# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 17:26:16 2020

@author: wuhaoyu

@description: 标准报表样式
"""

import pandas as pd
import numpy as np


def get_columns_name(index):
    carry = index // 26
    carry = chr(65 + carry - 1) if carry else ''
    remainder = index % 26
    return carry + chr(65 + remainder)


def adaptive_column_width(data):
    """
    获取data最优列宽列表

    Parameters
    ----------
    data : TYPE
        待计算列宽的数据框
    Returns
    -------
    widths : TYPE
        对应列的最优列宽列表
    """
    widths = list(map(lambda c: max(np.median(list(map(len, map(str, data[c])))), len(c)) + 5, data))  
    return widths


def excel_format(data_tuple, filename, sheetname_tuple=None):
    """
    将传入的DataFrame元组按照模板的样式保存到指定路径filename

    Parameters
    ----------
    data_tuple : DataFrame的元组
        待保存的DataFrame.
    filename ：文件保存路径
        最终保存的工作簿
    sheetname_tuple : STR的元组
        最终保存的Sheet名.

    Returns
    -------
    None.

    """
    if not sheetname_tuple:
        sheetname_tuple = tuple(f"sheet{i+1}" for i in range(len(data_tuple)))
    with pd.ExcelWriter(filename) as writer:
        workbook = writer.book
        
        # 通用格式
        fmt = workbook.add_format({'font_name': '微软雅黑',
                                    'font_size': 10,
                                    'valign': 'vcenter',
                                    'align': 'center',
                                    })
        
        # 标题格式
        hfmt = workbook.add_format({'font_name': '微软雅黑',
                                    'font_size': 10,
                                    'align': 'vcenter',
                                    'valign': 'center',
                                    'bg_color': '#AED6F1',
                                    'bold': True,
                                    'text_wrap': True,
                                    'border': 1
                                    })
        
        # 数据写入工作表
        for data, sheetname in zip(data_tuple, sheetname_tuple):
            if len(data):
                datetime_columns = data.select_dtypes(['datetime']).columns
                data[datetime_columns] = data[datetime_columns].applymap(lambda x : str(x))
                data.to_excel(writer, sheet_name=sheetname, index=False)
                worksheet = writer.sheets[sheetname]
                
                # 自动调整列宽
                widths = adaptive_column_width(data)
                lens = len(widths)
                for i in range(lens):
                    worksheet.set_column(f'{get_columns_name(lens)}:{get_columns_name(lens)}', widths[i], fmt)

                # 修改标题格式
                for col_num, value in enumerate(data.columns.values):
                    worksheet.write(0, col_num, value, hfmt)