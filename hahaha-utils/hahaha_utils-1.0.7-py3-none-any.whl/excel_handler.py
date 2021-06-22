# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File:           excel_handler.py
   Description:
   Author:        
   Create Date:    2020/06/23
-------------------------------------------------
   Modify:
                   2020/06/23:
-------------------------------------------------
"""
import pandas as pd

class ExcelHandler(object):
    def __init__(self):
        pass

    def read_excel_file(self, file_path, *args, **kwargs):
        """

        :param file_path:
        :param args:
        :param kwargs:
        :return:
        """
        self.file_content = pd.read_excel(file_path, **kwargs)
        return self.file_content

    def write_excel_file(self, file_path, data_list, columns, *args, **kwargs):
        """

        :param file_path:
        :param data_list:
        :param columns:
        :param args:
        :param kwargs:
        :return:
        """
        df = pd.DataFrame(data_list, columns=columns)
        df.to_excel(file_path, **kwargs)
        return 1

if __name__ == '__main__':
    eh = ExcelHandler()
    file_content = eh.read_excel_file("E:\\Users\\Danny\\Desktop\\test.xlsx")
    print(file_content)