#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2021/6/18 4:26 下午
# @Author  : similarface
# @Site    : 
# @File    : single.py
# @Software: PyCharm

import logging
import os
from typing import List

import baostock as bao
import colorama
import pandas as pd

from datetime import date, timedelta
from anack.synchronizer.stock.dataset.base import TradingSingStockData
from anack.synchronizer.tools.data_provider import need_update_by_trade_date
from anack.synchronizer.stock.factory import StockData
from anack.synchronizer.tools.data_provider import ts_code


class StockDaily(TradingSingStockData):
    """
    baostock 能获取2006-01-01至当前时间的数据
    """

    def __init__(self, stock_code: str, data_dir: str = None):
        super(StockDaily, self).__init__(stock_code, data_dir)

    def file_path(self) -> str:
        """
        返回保存数据的csv文件路径
        :return:
        """
        return os.path.join(self.data_dir, 'stocks', self.stock_code, 'day.csv')

    def load(self) -> pd.DataFrame:
        if os.path.exists(self.data_path):
            self.dataframe = pd.read_csv(
                filepath_or_buffer=self.data_path,
                parse_dates=['date']
            )
            self.dataframe.set_index(keys='date', drop=False, inplace=True)
            self.dataframe.sort_index(inplace=True)
        else:
            logging.warning(colorama.Fore.RED + '本地 [%s 日线] 数据文件不存在,请及时下载更新' % self.stock_code)
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
        if self.dataframe is None:
            self.load()

        if self.should_update():
            start_date: date = max(self.start_date(), StockData().stock_basic.list_date_of(self.stock_code))
            end_date: date = start_date
            last_trade_day = StockData().trade_calendar.latest_trade_day()
            df_list: List[pd.DataFrame] = [self.dataframe]
            step_days = timedelta(days=1000)

            while start_date <= last_trade_day:
                end_date = start_date + step_days
                end_date = min(end_date, last_trade_day)
                rs = bao.query_history_k_data_plus(
                    code=self.stock_code,
                    start_date=str(start_date),
                    end_date=str(end_date),
                    frequency='d',
                    fields='date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,peTTM,psTTM,pcfNcfTTM,pbMRQ,isST',
                    adjustflag='3'
                )
                df = rs.get_data()
                if not df.empty:
                    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
                    df['code'] = df['code'].apply(lambda x: ts_code(x))
                    df.set_index(keys='date', drop=False, inplace=True)
                    logging.debug(
                        colorama.Fore.YELLOW + f'下载 [{self.stock_code} 日线] 数据, 从 {start_date} 到 {end_date} 共 {df.shape[0]} 条')
                    df_list.append(df)

                start_date = end_date + timedelta(days=1)

            self.dataframe = pd.concat(df_list).drop_duplicates()
            self.dataframe.sort_index(inplace=True)

            self.dataframe.to_csv(
                path_or_buf=self.data_path,
                index=False
            )
            logging.info(colorama.Fore.YELLOW + f'[{self.stock_code} 日线] 数据更新到: {end_date} path: {self.data_path}')
        else:
            logging.info(colorama.Fore.BLUE + f'[{self.stock_code} 日线] 数据无须更新')


class StockWeekly(TradingSingStockData):
    """
    baostock 能获取2006-01-01至当前时间的数据
    """

    def __init__(self, stock_code: str, data_dir: str = None):
        super(StockWeekly, self).__init__(stock_code, data_dir)

    def file_path(self) -> str:
        """
        返回保存数据的csv文件路径
        :return:
        """
        return os.path.join(self.data_dir, 'stocks', self.stock_code, 'week.csv')

    def load(self) -> pd.DataFrame:
        if os.path.exists(self.data_path):
            try:
                self.dataframe = pd.read_csv(
                    filepath_or_buffer=self.data_path,
                    parse_dates=['date']
                )
                self.dataframe.set_index(keys='date', drop=False, inplace=True)
                self.dataframe.sort_index(inplace=True)
            except Exception:
                self.dataframe = pd.DataFrame()
        else:
            logging.warning(colorama.Fore.RED + '本地 [%s 周线] 数据文件不存在,请及时下载更新' % self.stock_code)
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
        if self.dataframe is None:
            self.load()

        if self.should_update():
            start_date: date = max(self.start_date(), StockData().stock_basic.list_date_of(self.stock_code))
            end_date: date = start_date
            last_trade_day = StockData().trade_calendar.latest_trade_day()
            df_list: List[pd.DataFrame] = [self.dataframe]
            step_days = timedelta(days=1000)

            while start_date <= last_trade_day:
                end_date = start_date + step_days
                end_date = min(end_date, last_trade_day)
                rs = bao.query_history_k_data_plus(
                    code=self.stock_code,
                    start_date=str(start_date),
                    end_date=str(end_date),
                    frequency='w',
                    fields="date,code,open,high,low,close,volume,amount,adjustflag,turn,pctChg",
                    adjustflag='3'
                )
                df = rs.get_data()
                if not df.empty:
                    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
                    df['code'] = df['code'].apply(lambda x: ts_code(x))
                    df.set_index(keys='date', drop=False, inplace=True)
                    logging.debug(
                        colorama.Fore.YELLOW + f'下载 [{self.stock_code} 周线] 数据, 从 {start_date} 到 {end_date} 共 {df.shape[0]} 条')
                    df_list.append(df)

                start_date = end_date + timedelta(days=1)

            self.dataframe = pd.concat(df_list).drop_duplicates()
            self.dataframe.sort_index(inplace=True)

            self.dataframe.to_csv(
                path_or_buf=self.data_path,
                index=False
            )
            logging.info(colorama.Fore.YELLOW + f'[{self.stock_code} 周线] 数据更新到: {end_date} path: {self.data_path}')
        else:
            logging.info(colorama.Fore.BLUE + f'[{self.stock_code} 周线] 数据无须更新')
