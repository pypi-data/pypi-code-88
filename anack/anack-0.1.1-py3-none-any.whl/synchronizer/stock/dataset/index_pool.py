#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2021/6/18 9:24 下午
# @Author  : similarface
# @Site    : 
# @File    : index_pool.py
# @Software: PyCharm


import os
from datetime import date, timedelta
import logging
import colorama
from typing import List
import pandas as pd
import baostock as bao
from anack.synchronizer.tools.data_provider import need_update_by_trade_date
from anack.synchronizer.stock.dataset.base import TradingSingStockData
from anack.synchronizer.tools.data_provider import ts_code
from anack.synchronizer.stock.factory import StockData


class IndexDaily(TradingSingStockData):
    """
    baostock 获取指数 index_pool
    """

    def __init__(self, data_dir: str, index_code: str):
        super(IndexDaily, self).__init__(index_code, data_dir)
        self.index_name = '-'
        self.index_code = self.stock_code

    def file_path(self) -> str:
        """
        返回保存数据的csv文件路径
        :return:
        """
        return os.path.join(self.data_dir, 'index', 'index_daily', '%s.csv' % self.index_code)

    def should_update(self) -> bool:
        """
        如果数据文件的最后修改日期, 早于最近的一个交易日, 则需要更新数据
        如果文件不存在, 直接返回 True
        :return:
        """
        if not os.path.exists(self.file_path()):
            return True

        self.prepare()

        return need_update_by_trade_date(self.dataframe, 'date')

    def load(self) -> pd.DataFrame:
        if os.path.exists(self.data_path):
            self.dataframe = pd.read_csv(
                filepath_or_buffer=self.data_path,
                parse_dates=['date']
            )
            self.dataframe.set_index(keys='date', drop=False, inplace=True)
            self.dataframe.sort_index(inplace=True)
        else:
            logging.warning(colorama.Fore.RED + '本地 [%s 日线] 数据文件不存在,请及时下载更新' % self.index_name)
            self.dataframe = pd.DataFrame()

        return self.dataframe

    def start_date(self) -> date:
        """
        计算本次更新的起始日期
        :return:
        """
        if self.dataframe is None:
            self.load()

        if self.dataframe.empty:
            return self.base_date
        else:
            return self.dataframe.iloc[-1].loc['date'].date() + timedelta(days=1)

    def update(self):
        self._setup_dir_()
        self.prepare()

        if self.should_update():
            start_date: date = self.start_date()
            end_date: date = start_date
            last_trade_day = StockData().trade_calendar.latest_trade_day()
            df_list: List[pd.DataFrame] = [self.dataframe]
            step_days = timedelta(days=1000)

            while start_date <= last_trade_day:
                end_date = start_date + step_days
                end_date = min(end_date, last_trade_day)
                rs = bao.query_history_k_data_plus(
                    code=self.index_code,
                    start_date=str(start_date),
                    end_date=str(end_date),
                    frequency='d',
                    fields='date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,peTTM,psTTM,pcfNcfTTM,pbMRQ,isST',
                    adjustflag='3'
                )
                df = rs.get_data()
                if not df.empty:
                    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
                    df['is_open'] = df['isST'].apply(lambda x: str(x) == '1')
                    df['code'] = df['code'].apply(lambda x: ts_code(x))
                    df.set_index(keys='date', drop=False, inplace=True)
                    logging.debug(
                        colorama.Fore.YELLOW + '下载 [%s 日线] 数据, 从 %s 到 %s' % (
                            self.index_name, str(start_date), str(end_date)))

                    df_list.append(df)
                start_date = end_date + timedelta(days=1)
            self.dataframe = pd.concat(df_list).drop_duplicates()
            self.dataframe.sort_index(inplace=True)
            self.dataframe.to_csv(
                path_or_buf=self.file_path(),
                index=False
            )
            logging.info(
                colorama.Fore.YELLOW + '[%s 日线] 数据更新到: %s path: %s' % (
                    self.index_name, str(end_date), self.file_path()))
        else:
            logging.info(colorama.Fore.BLUE + '[%s 日线] 数据无须更新' % self.index_name)
