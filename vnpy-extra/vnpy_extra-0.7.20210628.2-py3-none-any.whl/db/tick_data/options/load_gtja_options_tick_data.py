"""
@author  : MG
@Time    : 2021/6/23 13:35
@File    : load_gtja_options_tick_data.py
@contact : mmmaaaggg@163.com
@desc    : 用于将国泰君安提供的期权tick数据合成分钟线数据导入到数据库中
"""
import logging
import os
import re
import zipfile
from typing import Dict, Optional

import pandas as pd
from ibats_utils.path import get_file_name_iter
from vnpy.trader.constant import Exchange
from vnpy.trader.database import database_manager
from vnpy.trader.object import TickData

from vnpy_extra.utils.enhancement import BarGenerator

logger = logging.getLogger(__name__)


def find_df(file_name_no_ext: str, structure_dic: Dict[str, pd.DataFrame]) -> Optional[pd.DataFrame]:
    for key, val in structure_dic.items():
        if file_name_no_ext.find(key) != -1:
            return val

    return None


def load_tick_data_from_zip(file_path, structure_dic: Dict[str, pd.DataFrame], chunk_size=1000):
    csv_tick_name_mapping = {
        'Symbol': 'symbol',
        # 'TradingDate': 'trade_date',
        'TradingTime': 'datetime',
        'LastPrice': 'last_price',
        'TradeVolume': 'last_volume',
        # 'PriceUpLimit': 'limit_up',
        # 'PriceDownLimit': 'limit_down',
        'TotalPosition': 'open_interest',
        'TotalVolume': 'volume',  # bg tick 数据合成分钟线时的 volume 是累计成交量
        'Market': 'market',
    }
    gateway_name = 'CSV'
    tick_data_param_names = (
        'symbol', 'volume', 'open_interest', 'last_price', 'last_volume',
        # 'limit_up', 'limit_down',
    )
    use_col_names = csv_tick_name_mapping.keys()
    saved_file_names = set()
    try:
        with open('saved_file_names.txt', 'r') as f:
            for line in f.readlines():
                saved_file_name = line.split(',')[0]
                if saved_file_name == '':
                    continue
                saved_file_names.add(saved_file_name)
    except FileNotFoundError:
        pass

    zf = zipfile.ZipFile(file_path, 'r')
    for z_info in zf.filelist:
        try:
            with open('stop.txt', 'r') as f:
                line = f.readline()
                if line.startswith('stop'):
                    logger.warning("终止处理")
                    break
        except FileNotFoundError:
            pass

        if z_info.is_dir():
            continue
        file_name = z_info.filename
        if file_name in saved_file_names:
            logger.warning(f"{file_name} 文件已经处理过,跳过")
            continue

        logger.info(f"{file_name} 开始进行处理")
        file_name_no_ext, _ = os.path.splitext(os.path.split(file_name)[-1])
        structure_df: pd.DataFrame = find_df(file_name_no_ext, structure_dic)
        if structure_df is None:
            raise KeyError(f"{file_name_no_ext} 没有找到对应的数据字典文件")

        use_cols = [int(_) - 1 for _, name in structure_df['字段名'].items() if name in use_col_names]
        idx_name_mapping = {_: csv_tick_name_mapping[label] for _, label in zip(use_cols, use_col_names)}
        datetime_idx = None
        for _, label in zip(use_cols, use_col_names):
            tick_data_name = csv_tick_name_mapping[label]
            idx_name_mapping[_] = tick_data_name
            if datetime_idx is None and tick_data_name == 'datetime':
                datetime_idx = _

        # 根据文件名判断 exchange
        exchange = Exchange.DCE
        bars = []
        bg = BarGenerator(on_bar=lambda bar: bars.append(bar))
        # data = zf.read(file_name)
        symbol = None
        tick_count = 0
        with zf.open(file_name, "r") as fp:
            data_df = pd.read_csv(fp, chunksize=chunk_size, encoding="GBK", header=None, usecols=use_cols,
                                  parse_dates=[datetime_idx])
            for chunk_df in data_df:
                chunk_df.rename(columns=idx_name_mapping, inplace=True)
                for dic in chunk_df.to_dict('records'):
                    if symbol is None:
                        symbol = dic['symbol']
                    tick = TickData(
                        exchange=exchange, gateway_name=gateway_name,
                        datetime=dic['datetime'].to_pydatetime(),
                        **{k: v for k, v in dic.items() if k in tick_data_param_names})
                    bg.update_tick(tick)
                    tick_count += 1

        # 保存数据
        bar_count = len(bars)
        database_manager.save_bar_data(bars)
        logger.info(f"{symbol} {tick_count} tick数据 合成 {bar_count} 笔 1分钟数据 已被保存")
        with open('saved_file_names.txt', 'a') as f:
            f.write(f"{file_name},{tick_count},{bar_count}\n")


def load_tick_data_from_dir(dir_path, structure_file_dir):
    structure_dic = load_structure_data(structure_file_dir)
    count = 0
    for file_path in get_file_name_iter(dir_path, '*.zip', recursive=True):
        count += load_tick_data_from_zip(file_path, structure_dic)


def load_structure_data(structure_file_dir) -> Dict[str, pd.DataFrame]:
    """加载数据字典文件,返回字典:key为文件头,value为df"""
    structure_dic = {}
    for num, structure_file_path in enumerate(get_file_name_iter(structure_file_dir, '*.xlsx', recursive=True)):
        file_name_no_ext = os.path.splitext(os.path.split(structure_file_path)[-1])[0]
        ret1 = re.split(r"(\w+)(?:SYMBOL_YYYYMM|MINFreq_YYYYMM)", file_name_no_ext)
        ret2 = re.split(r"(\w+BASICINFO_)(?:ALL_)?(?=YYYYMM)", file_name_no_ext)
        if len(ret1) < 3 and len(ret2) < 3:
            logger.warning('%d) 无法解析 %s 文件', num, file_name_no_ext)
            continue
        header_str = ret1[1] if len(ret1) >= 3 else file_name_no_ext[:-len('YYYYMM')]
        logger.info('%d) 匹配 %s', num, header_str)
        structure_dic[header_str] = pd.read_excel(structure_file_path).set_index(['序号'])

    return structure_dic


def _test_load_tick_data_from_zip():
    file_path = r'f:\downloads\截止2020年历史期权tick数据\商品期权CO\GTA_COL1_TAQ_201703.zip'
    structure_file_dir = r'.\新高频数据说明'
    structure_dic = load_structure_data(structure_file_dir)
    load_tick_data_from_zip(file_path, structure_dic)


if __name__ == "__main__":
    # load_tick_data_from_dir(r"f:\downloads\截止2020年历史期权tick数据\商品期权CO")
    _test_load_tick_data_from_zip()
