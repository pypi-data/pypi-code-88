# -*- coding:utf-8 -*-
"""
文件和目录相关操作
"""
import os



def file_exist(file_path):
    """
    检测文件是否存在
    :param file_path:
    :return:
    """
    if os.path.isfile(file_path):
        return True
    else:
        return False