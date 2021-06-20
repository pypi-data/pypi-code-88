#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2021/6/18 5:36 下午
# @Author  : similarface
# @Site    : 
# @File    : pool.py
# @Software: PyCharm

import os
import baostock as bao
from anack.synchronizer.stock.dataset.base import TradingStockPoolData


class HS300(TradingStockPoolData):

    def __init__(self, data_dir: str = None):
        super(HS300, self).__init__(data_dir)

    def file_path(self) -> str:
        """
        返回保存数据的csv文件路径
        :return:
        """
        return os.path.join(self.data_dir, 'stock_pool', 'hs300.csv')

    def bao_stocks(self):
        return self.get_bao_stocks(bao.query_hs300_stocks)


class ZZ500(TradingStockPoolData):

    def __init__(self, data_dir: str = None):
        super(ZZ500, self).__init__(data_dir)

    def file_path(self) -> str:
        """
        返回保存数据的csv文件路径
        :return:
        """
        return os.path.join(self.data_dir, 'stock_pool', 'zz500.csv')

    def bao_stocks(self):
        return self.get_bao_stocks(bao.query_zz500_stocks)


class SZ50(TradingStockPoolData):

    def __init__(self, data_dir: str = None):
        super(SZ50, self).__init__(data_dir)

    def file_path(self) -> str:
        """
        返回保存数据的csv文件路径
        :return:
        """
        return os.path.join(self.data_dir, 'stock_pool', 'sz50.csv')

    def bao_stocks(self):
        return self.get_bao_stocks(bao.query_sz50_stocks)
