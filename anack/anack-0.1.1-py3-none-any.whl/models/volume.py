#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2021/6/15 10:47 下午
# @Author  : similarface
# @Site    : 
# @File    : warning.py
# @Software: PyCharm
from anack.utils.stock import get_lately_month_stock_data
from anack.utils.base import pre_n_day_str
import pandas as pd


def get_pre_day_volume_mean(dataset: pd.DataFrame, pre_day=30):
    """
    获取max(dataset.date) pre_day  以来 成交量的均值
    :param dataset:
    :param pre_day:
    :return:
    """
    dataset = dataset[dataset['date'] > pre_n_day_str(pre_day)]
    return dataset['volume'].mean()


def get_pre_n_item_volume_mean(dataset: pd.DataFrame, pre_item=30):
    """
    获取max(dataset.date) pre_n_item 条 以来 成交量的均值
    :param dataset:
    :param pre_item:
    :return:
    """
    return dataset.sort_values("date", ascending=False).head(pre_item)['volume'].mean()


code = 'sz.002938'
k = 3

df = get_lately_month_stock_data(code=code)

base = get_pre_n_item_volume_mean(df, 30)

max_k = 3*base

#print(max_k)

df2 = get_lately_month_stock_data(code=code,frequency='15',lately_month=1)
print(df2.head())