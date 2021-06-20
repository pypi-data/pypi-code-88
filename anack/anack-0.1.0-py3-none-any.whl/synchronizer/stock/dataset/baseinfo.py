#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2021/6/18 3:45 下午
# @Author  : similarface
# @Site    : 
# @File    : stock.py
# @Software: PyCharm
# Desc: 获取A股票基本信息，包含code，中文名字、那个板块等基础信息               d

import logging
import os
import colorama
import pandas as pd
from datetime import date
from anack.synchronizer.tools.data_provider import ts_pro_api
from anack.synchronizer.conf import ts_rate_limiter

from anack.synchronizer.stock.dataset.base import TradingStockData


class StockBasic(TradingStockData):

    def __init__(self, data_dir: str = None):
        super(StockBasic, self).__init__(data_dir)

    def update(self):
        self._setup_dir_()
        self.prepare()
        if self.should_update():
            df = self.ts_stock_basic()
            df.to_csv(
                path_or_buf=self.data_path,
                index=False
            )

    def file_path(self, *args, **kwargs):
        return os.path.join(self.data_dir, 'stock_basic', 'stock_basic.csv')

    def load(self) -> pd.DataFrame:
        if os.path.exists(self.data_path):
            self.dataframe = pd.read_csv(
                filepath_or_buffer=self.data_path,
                dtype={'symbol': str},
                parse_dates=['list_date', 'delist_date']
            )
            self.dataframe.set_index(keys='ts_code', drop=False, inplace=True)
            self.dataframe.sort_index(inplace=True)
        else:
            logging.warning(colorama.Fore.RED + '[股票列表基础信息] 本地数据文件不存在,请及时下载更新')
            self.dataframe = pd.DataFrame()

        return self.dataframe

    def list_date_of(self, ts_code: str) -> date:
        """
        返回指定证券的上市日期
        :param ts_code:
        :return:
        """
        self.prepare()
        return self.dataframe.loc[ts_code].loc['list_date'].date()

    def name_of(self, ts_code: str) -> str:
        """
        返回指定证券的名称
        :param ts_code:
        :return:
        """
        self.prepare()
        return self.dataframe.loc[ts_code].loc['name']

    @staticmethod
    @ts_rate_limiter
    def ts_stock_basic() -> pd.DataFrame:
        df: pd.DataFrame = ts_pro_api().stock_basic(
            exchange='',
            list_status='L',
            fields='ts_code,symbol,name,area,industry,fullname,market,exchange,list_status,list_date,delist_date,is_hs'
        )
        df['list_date'] = pd.to_datetime(df['list_date'], format='%Y%m%d')
        df['delist_date'] = pd.to_datetime(df['delist_date'], format='%Y%m%d')
        logging.info(colorama.Fore.YELLOW + '下载 [股票列表基础信息] 数据')
        return df


if __name__ == '__main__':
    StockBasic("/tmp").update()
