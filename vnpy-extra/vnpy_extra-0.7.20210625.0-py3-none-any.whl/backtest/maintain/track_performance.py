"""
@author  : MG
@Time    : 2021/1/20 9:31
@File    : track_performance.py
@contact : mmmaaaggg@163.com
@desc    : 用于对有效策略每日持续更新绩效表现
"""
import logging
import os
import re
from concurrent.futures import ThreadPoolExecutor
from datetime import date, timedelta
from typing import List, Dict, Tuple, Iterator

import numpy as np
import pandas as pd
from ibats_utils.mess import load_class, get_first
from tqdm import tqdm
from vnpy.trader.constant import Interval

from vnpy_extra.backtest import CrossLimitMethod
from vnpy_extra.backtest.commons import bulk_backtest_with_backtest_params_iter, set_default_root_folder_name, \
    run_backtest
from vnpy_extra.backtest.cta_strategy.engine import BacktestingEngine as CtaBacktestingEngine
from vnpy_extra.backtest.portfolio_strategy.engine import BacktestingEngine as PortfolioBacktestingEngine
from vnpy_extra.db.orm import StrategyBacktestStats, StrategyBacktestStatsArchive, StrategyInfo

logger = logging.getLogger(__name__)


def get_backtest_params_iter_from_stats_list(
        stats_list: List[StrategyBacktestStats]
) -> Tuple[List[str], Iterator[Tuple[dict, list, StrategyBacktestStats]]]:
    """
    整理 StrategyBacktestStats 列表，重新设置回测日期区间，返回参数名称及 回测引擎及参数迭代器
    """
    param_name_list = None
    engine_kwargs_list, param_values_list = [], []
    for stats in stats_list:
        if stats.strategy_settings is None:
            stats.strategy_settings = {}

        if param_name_list is None:
            param_name_list = list(stats.strategy_settings.keys())

        engine_kwargs = stats.engine_kwargs
        # 整理回测日期区间
        engine_kwargs['end'] = date.today()
        engine_kwargs['start'] = date.today() - timedelta(days=365 * 3)
        engine_kwargs['cross_limit_method'] = CrossLimitMethod(stats.cross_limit_method)
        if 'interval' in engine_kwargs:
            interval = engine_kwargs['interval']
            engine_kwargs['interval'] = Interval(interval) if interval is not None else Interval.MINUTE
        engine_kwargs_list.append(engine_kwargs)
        param_values_list.append([stats.strategy_settings[_] for _ in param_name_list if _ in stats.strategy_settings])

    return param_name_list, zip(engine_kwargs_list, param_values_list, stats_list)


def backtest_all_strategies(
        symbols_list=None, strategy_class_name_list=None, root_folder_name=None, author_list=None, pool_size=3,
        output_path_has_strategy_class_name=False):
    """每日策略自动回测"""
    set_default_root_folder_name(root_folder_name)
    stats_list_dic: Dict[Tuple[str, str], List[StrategyBacktestStats]] = \
        StrategyBacktestStats.get_available_status_group_by_strategy(
            symbols_list=symbols_list, strategy_class_name_list=strategy_class_name_list)
    StrategyBacktestStatsArchive.archive(stats_list_dic)
    if len(stats_list_dic) <= 1:
        pool_size = 0

    if pool_size <= 1:
        pool = None
    else:
        pool = ThreadPoolExecutor(max_workers=pool_size, thread_name_prefix="backtest_")

    for (module_name, strategy_class_name, symbols), stats_list in stats_list_dic.items():
        try:
            strategy_cls = load_class(module_name, strategy_class_name)
        except ModuleNotFoundError:
            logger.warning(f"{module_name}.{strategy_class_name} 不存在，忽略")
            continue
        if author_list is not None and getattr(strategy_cls, 'author', None) not in author_list:
            continue

        multi_symbols = len(symbols.split('_')) > 1
        if multi_symbols:
            from vnpy_extra.backtest.portfolio_strategy.run import default_engine_param_key_func
        else:
            from vnpy_extra.backtest.cta_strategy.run import default_engine_param_key_func

        param_name_list, backtest_params_iter = get_backtest_params_iter_from_stats_list(stats_list)
        bulk_backtest_kwargs = dict(
            multi_symbols=multi_symbols,
            param_name_list=param_name_list,
            backtest_params_iter=backtest_params_iter,
            engine_param_key_func=default_engine_param_key_func,
            output_available_only=False,
            open_browser_4_charts=False,
            save_stats=True,
            enable_collect_data=False,
            output_path_has_strategy_class_name=output_path_has_strategy_class_name,
            output_separate_by_backtest_status=True
        )
        if pool_size <= 1:
            try:
                bulk_backtest_with_backtest_params_iter(strategy_cls=strategy_cls, **bulk_backtest_kwargs)
            except:
                logging.exception("%s 追踪回测异常", strategy_cls.__name__)

        else:
            future = pool.submit(bulk_backtest_with_backtest_params_iter, **bulk_backtest_kwargs)

    if pool is not None:
        pool.shutdown(wait=True)


def backtest_by_warning_log(log_file_path, xls_dir, encoding='utf-8', output_path_has_strategy_class_name=True):
    """更加日至中 '没有找到对应的记录' 的警告日志对当前测试进行补充测试，并将测试结果补充到数据库，同时，调整相应状态"""
    folder_name_list = os.listdir(xls_dir)
    # 读 log 寻找 WARNING *** 没有找到对应的记录 的记录，并将 策略类名称，合约名称，id_name 记录下来
    pattern = re.compile(r'WARNING (\w+) \[([\w\.]+)\] <(\w+)> 没有找到对应的记录')
    stg_cls_vt_symbol_id_name_tuple_xls_name_dic: Dict[Tuple[str, str, str], str] = {}
    with open(log_file_path, 'r', encoding=encoding) as f:
        line_str = f.readline()
        while line_str != "":
            ret = pattern.search(line_str)
            if ret is not None:
                stg_cls_vt_symbol_id_name_tuple: Tuple[str, str, str] = ret.groups()
                cls_name, vt_symbol, id_name = stg_cls_vt_symbol_id_name_tuple
                xls_name_header = f'{cls_name}_{vt_symbol}'
                # 从 xlsx 目录中找到相应的文件
                xls_name = get_first(folder_name_list, lambda x: x.startswith(xls_name_header))
                if xls_name is None:
                    logger.warning("%s 没有找的对应的文件，对应 id_name=%s", xls_name_header, id_name)
                else:
                    stg_cls_vt_symbol_id_name_tuple_xls_name_dic[stg_cls_vt_symbol_id_name_tuple] = xls_name

            line_str = f.readline()

    # get_cls_module_dic
    cls_module_dic = StrategyInfo.get_cls_module_dic()
    # 建立engine dic
    xls_df_dict = {}
    # 针对每一条 stg_cls, vt_symbol, id_name tuple 进行循环
    backtest_params_iter = tqdm(
        enumerate(stg_cls_vt_symbol_id_name_tuple_xls_name_dic.items()),
        total=len(stg_cls_vt_symbol_id_name_tuple_xls_name_dic),
    )
    # 回测统计结果列表
    data_dic_list = []
    # engine 列表
    engine_dic = {}
    for num, ((strategy_class_name, vt_symbol, id_name), xls_name) in backtest_params_iter:
        # 打开 xlsx 文件 找到相应的 记录
        if xls_name not in xls_df_dict:
            xls_df_dict[xls_name] = df = pd.read_excel(os.path.join(xls_dir, xls_name), index_col='id_name')
        else:
            df = xls_df_dict[xls_name]
        if id_name not in df.index:
            logger.warning("%s %s %s 在 %s 中没有找到相应记录", strategy_class_name, vt_symbol, id_name, xls_name)
            continue
        record: pd.Series = df.loc[id_name, :]
        # 读取相应参数，并整理成dic 同时记录 backtest_status 加入回测列表
        multi_symbols = vt_symbol.find('_') >= 0
        strategy_kwargs = {}
        # 构建 strategy_kwargs
        for key, value in record.items():
            if key == '新高周期':
                break
            if isinstance(value, np.int64) or isinstance(value, np.int32):
                value = int(value)
            elif isinstance(value, np.float64) or isinstance(value, np.float32) or isinstance(value, np.float16):
                value = float(value)
            strategy_kwargs[key] = value

        backtest_status_from_xls = record['backtest_status']
        short_name = record['short_name']
        shown_name = record['shown_name']
        cross_limit_method = CrossLimitMethod(record['cross_limit_method'])
        if backtest_status_from_xls == 0:
            logger.warning("%s %s %s backtest_status == 0 无需回测", strategy_class_name, vt_symbol, id_name)
            continue

        # 建立相应 engine
        if multi_symbols not in engine_dic:
            engine_dic[
                multi_symbols] = engine = PortfolioBacktestingEngine() if multi_symbols else CtaBacktestingEngine()
        else:
            engine = engine_dic[multi_symbols]

        # 建立 engine_kwargs
        if multi_symbols:
            engine_kwargs = {
                "vt_symbols": vt_symbol.split('_'),
                "cross_limit_method": cross_limit_method,
            }
        else:
            engine_kwargs = {
                "vt_symbol": vt_symbol,
                "cross_limit_method": cross_limit_method,
            }

        # 逐条回测
        strategy_cls = StrategyInfo.get_strategy_class_by_name(strategy_class_name)
        statistics = run_backtest(
            strategy_cls,
            multi_symbols,
            engine_kwargs,
            strategy_kwargs,
            engine=engine,
            save_stats=True,
            output_path_has_strategy_class_name=output_path_has_strategy_class_name,
        )

        if statistics is None:
            continue
        backtest_status = statistics.setdefault('backtest_status', 0)
        # 如果回测状态 backtest_status == 0 且 backtest_status_from_xls > 0 则需要更新状态，否则直接跳过
        if not (backtest_status == 0 and backtest_status_from_xls > 0):
            continue

        statistics['backtest_status'] = backtest_status_from_xls
        if statistics.setdefault('short_name', short_name) is None:
            statistics['short_name'] = short_name

        if statistics.setdefault('shown_name', shown_name) is None:
            statistics['shown_name'] = shown_name

        data_dic_list.append(statistics)
        id_name_new = statistics['id_name']
        if id_name_new != id_name:
            logger.warning(f"{strategy_class_name} {vt_symbol} {id_name} -> {id_name_new} 状态将被修改 "
                           f"{backtest_status} -> {backtest_status_from_xls}")
        else:
            logger.warning(f"{strategy_class_name} {vt_symbol} {id_name} 状态将被修改 "
                           f"{backtest_status} -> {backtest_status_from_xls}")

    StrategyBacktestStats.update_backtest_status(data_dic_list)


if __name__ == "__main__":
    backtest_all_strategies(
        # strategy_class_name_list=['DoubleMA4Test'],
        # symbols_list=['rb9999.shfe', 'hc9999.shfe'],
        author_list={'MG'},
        pool_size=0
    )
