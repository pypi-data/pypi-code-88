# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 17:46:58 2020

@author: wuhaoyu
"""
import os
from datetime import datetime


def get_file_list(file_path):
    """
    按照创建日期对file_path下的文件进行排序

    Parameters
    ----------
    file_path : TYPE
        DESCRIPTION.

    Returns
    -------
    dir_list : TYPE
        DESCRIPTION.

    """
    dir_list = os.listdir(file_path)
    if not dir_list:
        return
    else:
        # 注意，这里使用lambda表达式，将文件按照最后修改时间顺序升序排列
        # os.path.getmtime() 函数是获取文件最后修改时间
        # os.path.getctime() 函数是获取文件最后创建时间
        dir_list = sorted(dir_list, key=lambda x: os.path.getctime(os.path.join(file_path, x)))
        return dir_list
    
    
def file_clean(file_folder, n=2):
    """
    清除file_folder目录下n年前历史文件

    Parameters
    ----------
    n : TYPE, optional
        DESCRIPTION. The default is 50.
    """
    if get_file_list(file_folder):
        file_list = [os.path.join(file_folder, i) for i in get_file_list(file_folder)]
    
        clean_list = filter(lambda x: datetime.fromtimestamp(os.path.getctime(x)).year == (datetime.now().year - n), file_list)
        for i in clean_list:
            os.remove(i)
