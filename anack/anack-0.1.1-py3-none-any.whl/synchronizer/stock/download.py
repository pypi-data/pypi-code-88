#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2021/6/18 1:56 下午
# @Author  : similarface
# @Site    : 
# @File    : main.py
# @Software: PyCharm

import logging
import colorama
from anack.synchronizer.tools.data_provider import bao_auth
from anack.synchronizer.stock.factory import StockData
from anack.synchronizer.conf import DATA_SAVE_BASE_DIR

from datetime import datetime, timedelta
from anack.synchronizer.stock.dataset.index_pool import IndexDaily
from anack.synchronizer.stock.dataset.single import StockDaily, StockWeekly

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)-15s] [%(threadName)s] [%(levelname)s] %(message)s"
)

colorama.init(autoreset=True)


def update_for_stock(stock_code: str):
    # 下载股票日K线数据
    StockDaily(data_dir=StockData().data_dir, stock_code=stock_code).update()
    # 更新股票周K线数据
    StockWeekly(data_dir=StockData().data_dir, stock_code=stock_code).update()
    # 更新啊股票5分组K线数据
    # 个股资金流向数
    # 十大持仓股东
    # 十大流通股东
    # 股东增减持
    # 股权质押明细
    # 停复牌信息


def update():
    start_time = datetime.now()
    # 更新股票日历信息 ，当天是否开盘
    StockData().trade_calendar.update()
    # 更新股票基本信息 包含股票代码
    StockData().stock_basic.update()
    # 更新股票公司基本信息
    StockData().stock_company.update()
    # 中证500的集合
    StockData().zz500.update()
    # 沪深300的集合
    StockData().hs300.update()
    # 上证50的集合
    StockData().sz50.update()
    # 更新指数信息
    for index_code in StockData().index_basic.default_index_pool():
        IndexDaily(data_dir=StockData().data_dir, index_code=index_code).update()
    # 下载hs300 和 zz500的股票K线信息
    stock_list = []
    stock_list.extend(StockData().hs300.stock_codes())
    stock_list.extend(StockData().zz500.stock_codes())
    total_count = len(stock_list)
    finished_count = 0

    for stock_code in stock_list:
        update_for_stock(stock_code)
        finished_count += 1
        logging.debug(colorama.Fore.LIGHTGREEN_EX + '股票 %s 更新完毕, 进度: (%s/%s) %.2f %%' %
                      (StockData().stock_basic.name_of(ts_code=stock_code),
                       finished_count,
                       total_count,
                       finished_count / total_count * 100))
    end_time = datetime.now()
    logging.info(colorama.Fore.YELLOW + '本次更新总共耗时: %s' % (end_time - start_time))


@bao_auth
def download_data(data_dir: str = None):
    data_dir = data_dir or DATA_SAVE_BASE_DIR
    print(f"download data to {data_dir}")
    StockData().setup(data_dir=data_dir or DATA_SAVE_BASE_DIR)
    update()


if __name__ == '__main__':
    download_data()
