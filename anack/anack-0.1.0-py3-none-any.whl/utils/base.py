#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2021/6/15 10:19 下午
# @Author  : similarface
# @Site    : 
# @File    : base.py
# @Software: PyCharm
import datetime


def pre_n_day_str(pre_n: int = 7, f: str = "%Y-%m-%d") -> str:
    """
    当前日期前 n 天的日期字符串 e.g. 2020-01-01
    :param pre_n:
    :param f: format
    :return:
    """
    today = datetime.date.today()
    pre_day = today - datetime.timedelta(days=pre_n)
    return pre_day.strftime(f)


def today_str(f: str = "%Y-%m-%d") -> str:
    return datetime.date.today().strftime(f)


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
