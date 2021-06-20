#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2021/6/18 1:54 下午
# @Author  : similarface
# @Site    : 
# @File    : data_provider.py
# @Software: PyCharm
import logging
from functools import wraps
import baostock as bao
import colorama
import tushare as ts
import pandas as pd
from tushare.pro.client import DataApi


def ts_pro_api() -> DataApi:
    return ts.pro_api(ts_token())


def ts_token() -> str:
    return 'f96b1eeee9c8fddd357f2299cdedc1c88b2bb2a30ae1f772cf810dea'


def bao_login():
    login_result = bao.login()
    if login_result.error_code == '0':
        logging.info(colorama.Fore.GREEN + 'baostock login %s' % login_result.error_msg)
    else:
        logging.warning(colorama.Fore.GREEN + 'baostock login %s' % login_result.error_msg)
        raise Exception(login_result.error_msg)


def bao_logout():
    bao.logout()
    logging.info(colorama.Fore.GREEN + 'baostock logout success!')


def ts_code(code: str) -> str:
    """
    转换证券代码为 tushare 标准格式
    :param code:
    :return:
    """
    if len(code) != 9:
        raise Exception('无效的证券代码: 长度不符')
    stock_code = code.upper()
    if stock_code.endswith('.SZ') or stock_code.endswith('.SH'):
        return stock_code
    elif stock_code.startswith('SZ.') or stock_code.startswith('SH.'):
        return '%s.%s' % (stock_code[3:], stock_code[0:2])
    else:
        raise Exception('无效的证券代码: %s' % code)


def bao_code(code: str) -> str:
    """
    转换证券代码为 baostock 标准格式
    :param code:
    :return:
    """
    if len(code) != 9:
        raise Exception('无效的证券代码: 长度不符')
    stock_code = code.lower()
    if stock_code.startswith('sz.') or stock_code.startswith('sh.'):
        return stock_code
    elif stock_code.endswith('.sz') or stock_code.endswith('.sh'):
        return '%s.%s' % (stock_code[0:6], stock_code[7:])
    else:
        raise Exception('无效的证券代码: %s' % code)


def need_update_by_trade_date(df: pd.DataFrame, column_name: str) -> bool:
    """
    根据DataFrame中指定的交易日期的最后记录的值, 如果在最近的交易日之前, 则说明需要更新
    :param df:
    :param column_name: 交易日期对应的字段名称
    :return:
    """
    if df.empty:
        # 如果DataFrame为空, 说明没有数据在本地, 需要更新
        return True
    else:
        from anack.synchronizer.stock.factory import StockData
        return df.iloc[-1].loc[column_name].date() < StockData().trade_calendar.latest_trade_day()


def bao_auth(func):
    @wraps(func)
    def wrap_func(*args, **kwargs):
        bao_login()
        func(*args, **kwargs)
        bao_logout()

    return wrap_func
