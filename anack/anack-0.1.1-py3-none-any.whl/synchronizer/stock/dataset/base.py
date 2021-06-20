#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2021/6/18 3:29 下午
# @Author  : similarface
# @Site    : 
# @File    : base.py
# @Software: PyCharm

import abc
import os
import pandas as pd
from typing import Union, Iterable
from datetime import date
from anack.synchronizer.conf import DATA_SAVE_BASE_DIR
from anack.synchronizer.tools.data_provider import ts_code


class TradingDataAbs(abc.ABC):
    base_dir = DATA_SAVE_BASE_DIR

    @abc.abstractmethod
    def update(self, *args, **kwargs):
        """
        更新数据
        :param args:
        :param kwargs:
        :return:
        """

    @abc.abstractmethod
    def load(self, *args, **kwargs):
        """
        加载数据
        :param args:
        :param kwargs:
        :return:
        """

    @abc.abstractmethod
    def file_path(self, *args, **kwargs):
        """ 保存数据的路径 """

    @property
    def data_path(self):
        return self.file_path()

    def _setup_dir_(self):
        """
        初始化数据目录
        :return:
        """
        os.makedirs(os.path.dirname(self.data_path), exist_ok=True)

    def prepare(self):
        if self.dataframe is None:
            self.load()
        return self

    @staticmethod
    def end_date(year: str) -> str:
        """
        当前日期的最后一天
        :return:
        """
        if year:
            return f'{year}1231'
        else:
            return f'{date.today().year}1231'

    @staticmethod
    def first_date(year: str, format='%Y%m%d') -> str:
        """
        当前日期的最后一天
        :return:
        """
        if year:
            return f'{year}0101'
        else:
            return f'{date.today().year}0101'

    @staticmethod
    def need_update(fpath: str, outdate_days: int) -> bool:
        """
        根据指定的数据文件的最后修改时间, 判断是否需要进行更新
        :param fpath: 数据文件路径
        :param outdate_days:
        :return: 需要更新时返回 True
        """
        if not os.path.exists(fpath):
            return True
        else:
            modify_date = date.fromtimestamp(os.stat(fpath).st_mtime)
            today = date.today()
            diff_days = (today - modify_date).days
            if diff_days > outdate_days:
                # 距离上次更新时间,超过指定天数
                return True
            else:
                return False


class TradingStockData(TradingDataAbs):
    def __init__(self, data_dir: str):
        self.data_dir: str = data_dir or self.base_dir
        self.dataframe: Union[pd.DataFrame, None] = None

    def load(self, *args, **kwargs):
        if os.path.exists(self.data_path):
            self.dataframe = pd.read_csv(filepath_or_buffer=self.data_path)
        else:
            self.dataframe = pd.DataFrame()

    def file_path(self, *args, **kwargs):
        return self.data_dir

    def update(self, *args, **kwargs):
        pass

    def should_update(self) -> bool:
        """
        判断数据是否需要更新.(更新频率: 每周更新)
        :return:
        """
        return self.need_update(self.data_path, 7)


from anack.synchronizer.tools.data_provider import need_update_by_trade_date


class TradingSingStockData(TradingStockData):
    base_date = date(year=2006, month=1, day=1)

    def __init__(self, stock_code, data_dir: str = None):
        super(TradingSingStockData, self).__init__(data_dir)
        self.stock_code = ts_code(stock_code)

    def should_update(self) -> bool:
        """
        如果数据文件的最后修改日期, 早于最近的一个交易日, 则需要更新数据
        如果文件不存在, 直接返回 True
        :return:
        """
        if not os.path.exists(self.data_path):
            return True

        self.prepare()

        return need_update_by_trade_date(self.dataframe, 'date')


class TradingStockPoolData(TradingStockData):

    def load(self) -> pd.DataFrame:
        if os.path.exists(self.file_path()):
            self.dataframe = pd.read_csv(
                filepath_or_buffer=self.data_path,
                parse_dates=['updateDate']
            )
            self.dataframe.set_index(keys='code', drop=False, inplace=True)
            self.dataframe.sort_index(inplace=True)
        else:
            self.dataframe = pd.DataFrame()
        return self.dataframe

    def stock_codes(self) -> Iterable[str]:
        self.prepare()
        for index, value in self.dataframe['code'].items():
            yield value

    def update(self):
        self._setup_dir_()

        if self.should_update():
            df = self.bao_stocks()
            df.to_csv(
                path_or_buf=self.data_path,
                index=False
            )
            self.prepare()

    @staticmethod
    def get_bao_stocks(func):
        df = func().get_data()
        df['code'] = df['code'].apply(lambda x: ts_code(x))
        df.set_index(keys='code', drop=False, inplace=True)
        return df
