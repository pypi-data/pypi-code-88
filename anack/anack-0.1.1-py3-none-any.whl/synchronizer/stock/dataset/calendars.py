#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2021/6/18 2:08 下午
# @Author  : similarface
# @Site    : 
# @File    : calendar.py
# @Software: PyCharm
# @desc: 该类用于生成交易日是否开盘的信息

import logging
import os
import colorama
import numpy
import pandas as pd
from pandas import Timestamp
from datetime import date
from typing import List, Union, Iterable
from anack.synchronizer.tools.data_provider import ts_pro_api
from anack.synchronizer.conf import ts_rate_limiter

from anack.synchronizer.stock.dataset.base import TradingStockData


class TradeCalendar(TradingStockData):

    def __init__(self, data_dir: str=None):
        super(TradeCalendar, self).__init__(data_dir)

    def update(self):
        self._setup_dir_()
        self.load()
        df_list: List[pd.DataFrame] = [self.dataframe]

        for year in range(2000, Timestamp.today().year + 1):
            check_date = f'{year}-01-01'
            df_tmp: pd.DataFrame = self.dataframe.loc[check_date:check_date]
            if df_tmp.empty:
                # 说明 year 对应年份的日历不在本地数据文件中
                df_list.append(self.ts_trade_cal(
                    start_date=self.first_date(year),
                    end_date=self.end_date(year)
                ))

        if len(df_list) > 1:
            self.dataframe: pd.DataFrame = pd.concat(df_list).drop_duplicates(subset='cal_date').sort_index()
            self.dataframe.to_csv(
                path_or_buf=self.data_path,
                index=False
            )

    def file_path(self, *args, **kwargs):
        """
        返回保存交易日历的csv文件路径
        :return:
        """
        return os.path.join(self.data_dir, 'trade_calendar', 'trade_calendar.csv')

    def load(self) -> pd.DataFrame:
        """
        从数据文件加载交易日历
        :return:
        """
        print(self.data_path)
        if os.path.exists(self.data_path):
            self.dataframe = pd.read_csv(
                filepath_or_buffer=self.data_path,
                dtype={'is_open': int},
                parse_dates=['cal_date', 'pretrade_date']
            )
            self.dataframe.set_index(keys='cal_date', drop=False, inplace=True)
            self.dataframe.sort_index(inplace=True)
        else:
            self.dataframe = pd.DataFrame(columns=['cal_date', 'is_open', 'pretrade_date'])

        return self.dataframe

    def latest_trade_day(self) -> date:
        """
        返回距离当天之前最近的一个交易日的日期. 如果当天是交易日,则返回当天
        :return:
        """
        self.prepare()
        today = date.today()
        row = self.dataframe.loc[numpy.datetime64(today)]
        if row.loc['is_open']:
            return today
        else:
            return row.loc['pretrade_date'].date()

    def next_n_trade_day(self, base_date: date, n: int, last_date: Union[None, date] = None) -> date:
        """
        返回 base_date 后第n个交易日的日期.
        :param last_date:
        :param base_date:
        :param n:
        :return:
        """
        self.prepare()
        df: pd.DataFrame = self.dataframe
        df = df[(df['cal_date'] >= str(base_date)) & (df['is_open'] == True)]
        rows_count = df.shape[0]
        row_index = min(rows_count - 1, n)
        day = df.iloc[row_index].loc['cal_date'].date()
        if last_date is None:
            return day
        else:
            latest_day = self.latest_trade_day()
            if day <= latest_day:
                return day
            else:
                return latest_day

    def trade_day_between(self, from_date: date, to_date: date) -> Iterable[date]:
        """
        返回指定起始日期之间(包含起始日期)所有交易日的日期
        :param from_date:
        :param to_date:
        :return:
        """
        self.prepare()
        df: pd.DataFrame = self.dataframe
        df = df[(df['cal_date'] >= str(from_date)) & (df['cal_date'] <= str(to_date)) & (df['is_open'] == True)]
        for index, value in df['cal_date'].iteritems():
            yield value.date()

    @staticmethod
    @ts_rate_limiter
    def ts_trade_cal(start_date: str, end_date: str) -> pd.DataFrame:
        """
        返回 是否是交易日
        ```
        cal_date        日期
        is_open         是否是交易日
        pretrade_date   当前的上一个交易日

        ```
        :param start_date: 开始日期
        :param end_date: 结束日期
        :return:
        """
        df: pd.DataFrame = ts_pro_api().trade_cal(
            exchange='SSE',
            start_date=start_date,
            end_date=end_date,
            fields=','.join(['cal_date', 'is_open', 'pretrade_date'])
        )
        df['cal_date'] = pd.to_datetime(df['cal_date'], format='%Y%m%d')
        df['pretrade_date'] = pd.to_datetime(df['pretrade_date'], format='%Y%m%d')
        df.set_index(keys='cal_date', drop=False, inplace=True)
        df.sort_index(inplace=True)
        logging.info(colorama.Fore.YELLOW + f'下载交易日历数据: {start_date} --to--> {end_date}')
        return df


if __name__ == '__main__':
    TradeCalendar(data_dir="/tmp/").update()
