#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2021/6/18 4:03 下午
# @Author  : similarface
# @Site    : 
# @File    : company.py
# @Software: PyCharm
# @Desc: 获取股票相关公司的基础信息
import logging
import os
import colorama
import pandas as pd
from anack.synchronizer.tools.data_provider import ts_pro_api
from anack.synchronizer.conf import ts_rate_limiter
from anack.synchronizer.stock.dataset.base import TradingStockData


class StockCompany(TradingStockData):

    def __init__(self, data_dir: str = None):
        super(StockCompany, self).__init__(data_dir)

    def file_path(self) -> str:
        """
        返回保存交易日历的csv文件路径
        :return:
        """
        return os.path.join(self.data_dir, 'stock_basic', 'stock_company.csv')

    def update(self):
        self._setup_dir_()
        if self.should_update():
            df = self.ts_stock_basic()
            df.to_csv(
                path_or_buf=self.data_path,
                index=False
            )

    def should_update(self) -> bool:
        """
        判断 stock_basic 数据是否需要更新.(更新频率: 每周更新)
        :return:
        """
        return self.need_update(self.data_path, 7)

    def load(self) -> pd.DataFrame:
        if os.path.exists(self.data_path):
            self.dataframe = pd.read_csv(
                filepath_or_buffer=self.data_path,
                parse_dates=['setup_date']
            )
            self.dataframe.set_index(keys='ts_code', drop=False, inplace=True)
            self.dataframe.sort_index(inplace=True)
        else:
            logging.warning(colorama.Fore.RED + 'StockCompany 本地数据文件不存在,请及时下载更新')
            self.dataframe = pd.DataFrame()

        return self.dataframe

    @staticmethod
    @ts_rate_limiter
    def ts_stock_basic() -> pd.DataFrame:
        df: pd.DataFrame = ts_pro_api().stock_company(
            exchange='',
            fields=','.join(['ts_code', 'exchange', 'chairman', 'manager', 'secretary', 'reg_capital', 'setup_date',
                             'province', 'city', 'introduction', 'website', 'email', 'office', 'employees',
                             'main_business', 'business_scope'])
        )
        df['setup_date'] = pd.to_datetime(df['setup_date'], format='%Y%m%d')
        logging.info(colorama.Fore.YELLOW + '下载股票上市公司基本信息数据')
        return df


if __name__ == '__main__':

    StockCompany().update()
