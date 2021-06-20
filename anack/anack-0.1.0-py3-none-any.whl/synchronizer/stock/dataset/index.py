#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2021/6/18 5:39 下午
# @Author  : similarface
# @Site    : 
# @File    : idnex.py
# @Software: PyCharm
# @Desc 指数信息基本信息

import os
from datetime import date, timedelta
import logging
import colorama
from typing import List
import pandas as pd
import baostock as bao
from anack.synchronizer.stock.dataset.base import TradingStockData
from anack.synchronizer.conf import ts_rate_limiter
from anack.synchronizer.tools.data_provider import ts_pro_api
from anack.synchronizer.tools.base import to_datetime64
from anack.synchronizer.tools.data_provider import need_update_by_trade_date
from anack.synchronizer.stock.dataset.base import TradingSingStockData
from anack.synchronizer.tools.data_provider import ts_code


class IndexBasic(TradingStockData):
    index_markets = {
        'MSCI': 'MSCI指数',
        'CSI': '中证指数',
        'SSE': '上交所指数',
        'SZSE': '深交所指数',
        'CICC': '中金所指数',
        'SW': '申万指数',
        'OTH': '其他指数'
    }

    def __init__(self, data_dir: str = None):
        super(IndexBasic, self).__init__(data_dir)

    def file_path(self) -> str:
        """
        返回保存数据文件的csv文件路径
        :return:
        """
        return os.path.join(self.data_dir, 'index', 'index_basic.csv')

    def load(self) -> pd.DataFrame:
        if os.path.exists(self.data_path):
            self.dataframe = pd.read_csv(
                filepath_or_buffer=self.data_path,
                parse_dates=['list_date', 'exp_date']
            )
            self.dataframe.set_index(keys='ts_code', drop=False, inplace=True)
            self.dataframe.sort_index(inplace=True)
        else:
            self.dataframe = pd.DataFrame()

        return self.dataframe

    @ts_rate_limiter
    def ts_index_basic(self, market_code: str) -> pd.DataFrame:
        df: pd.DataFrame = ts_pro_api().index_basic(
            market=market_code,
            fields='ts_code,name,fullname,market,publisher,index_type,category,base_date,base_point,list_date,weight_rule,desc,exp_date'
        )
        df['list_date'] = df['list_date'].apply(lambda x: to_datetime64(x))
        df['exp_date'] = df['exp_date'].apply(lambda x: to_datetime64(x))
        return df

    def update(self):
        self._setup_dir_()

        if self.should_update():
            df_list: List[pd.DataFrame] = []
            for market_code, market_name in self.index_markets.items():
                df = self.ts_index_basic(market_code)
                df_list.append(df)

            self.dataframe = pd.concat(df_list).drop_duplicates()

            self.dataframe.to_csv(
                path_or_buf=self.file_path(),
                index=False
            )
            logging.info(colorama.Fore.YELLOW + '[指数基本信息] 数据已经更新到最新. path: %s' % self.file_path())
        else:
            logging.info(colorama.Fore.YELLOW + '[指数基本信息] 数据无须更新')

    def name_of_index(self, index_code: str) -> str:
        """
        根据指数的代码, 查询指数的名称
        :param index_code:
        :return:
        """
        self.prepare()
        df = self.dataframe
        df = df[df['ts_code'] == index_code]
        if df.empty:
            raise Exception("找不到该指数代码: %s" % index_code)
        else:
            return df.iloc[0].loc['fullname']

    @staticmethod
    def default_index_pool() -> List[str]:
        """
        默认关注的指数代码列表
        :return:
        """
        code_list = [
            '000001.SH',
            '000002.SH',
            '000003.SH',
            '000004.SH',
            '000005.SH',
            '000006.SH',
            '000007.SH',
            '000008.SH',
            '000009.SH',
            '000010.SH',
            '000011.SH',
            '000012.SH',
            '000013.SH',
            '000015.SH',
            '000016.SH',
            '399001.SZ',
            '399002.SZ',
            '399003.SZ',
            '399004.SZ',
            '399005.SZ',
            '399006.SZ',
            '399007.SZ',
            '399008.SZ',
            '399107.SZ',
            '399108.SZ',
            '399300.SZ',
        ]

        return code_list



if __name__ == '__main__':
    IndexBasic().update()
