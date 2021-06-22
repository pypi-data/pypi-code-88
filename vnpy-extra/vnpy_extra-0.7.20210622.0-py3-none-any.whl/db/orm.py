"""
@author  : MG
@Time    : 2020/11/24 11:05
@File    : object.py
@contact : mmmaaaggg@163.com
@desc    : 用于创建数据库表结构

为方便调试 StrategyBacktestStats 使用，建议新建一个视图

CREATE
    ALGORITHM = UNDEFINED
    DEFINER = `root`@`localhost`
    SQL SECURITY DEFINER
VIEW `strategy_backtest_stats_view` AS
    SELECT
        `si`.`module_name` AS `module_name`,
        `si`.`strategy_class_name` AS `strategy_class_name`,
        `syi`.`symbols` AS `symbols`,
        `stats`.`stg_info_id` AS `stg_info_id`,
        `stats`.`symbols_info_id` AS `symbols_info_id`,
        `stats`.`id_name` AS `id_name`,
        `stats`.`cross_limit_method` AS `cross_limit_method`,
        `stats`.`short_name` AS `short_name`,
        `stats`.`shown_name` AS `shown_name`,
        `stats`.`strategy_settings` AS `strategy_settings`,
        `stats`.`engine_kwargs` AS `engine_kwargs`,
        `stats`.`backtest_status` AS `backtest_status`,
        `stats`.`available` AS `available`,
        `stats`.`update_dt` AS `update_dt`,
        `stats`.`start_date` AS `start_date`,
        `stats`.`end_date` AS `end_date`,
        `stats`.`total_days` AS `total_days`,
        `stats`.`profit_days` AS `profit_days`,
        `stats`.`loss_days` AS `loss_days`,
        `stats`.`capital` AS `capital`,
        `stats`.`end_balance` AS `end_balance`,
        `stats`.`total_return` AS `total_return`,
        `stats`.`annual_return` AS `annual_return`,
        `stats`.`max_drawdown` AS `max_drawdown`,
        `stats`.`max_ddpercent` AS `max_ddpercent`,
        `stats`.`max_drawdown_duration` AS `max_drawdown_duration`,
        `stats`.`max_new_higher_duration` AS `max_new_higher_duration`,
        `stats`.`total_net_pnl` AS `total_net_pnl`,
        `stats`.`total_commission` AS `total_commission`,
        `stats`.`total_slippage` AS `total_slippage`,
        `stats`.`total_turnover` AS `total_turnover`,
        `stats`.`total_trade_count` AS `total_trade_count`,
        `stats`.`daily_net_pnl` AS `daily_net_pnl`,
        `stats`.`daily_commission` AS `daily_commission`,
        `stats`.`daily_slippage` AS `daily_slippage`,
        `stats`.`daily_turnover` AS `daily_turnover`,
        `stats`.`daily_trade_count` AS `daily_trade_count`,
        `stats`.`daily_return` AS `daily_return`,
        `stats`.`return_std` AS `return_std`,
        `stats`.`sharpe_ratio` AS `sharpe_ratio`,
        `stats`.`info_ratio` AS `info_ratio`,
        `stats`.`return_drawdown_ratio` AS `return_drawdown_ratio`,
        `stats`.`image_file_path` AS `image_file_path`
    FROM
        ((`strategy_backtest_stats` `stats`
        LEFT JOIN `strategy_info` `si` ON ((`stats`.`stg_info_id` = `si`.`id`)))
        LEFT JOIN `symbols_info` `syi` ON ((`stats`.`symbols_info_id` = `syi`.`id`)))

"""
import enum
import json
import os
import re
import typing
from collections import defaultdict, OrderedDict
from datetime import datetime, date
from functools import lru_cache

import pandas as pd
from ibats_utils.mess import date_2_str, datetime_2_str, create_instance, dict_2_jsonable, load_class, is_linux_os
from peewee import (
    PrimaryKeyField,
    ForeignKeyField,
    CharField,
    SmallIntegerField,
    DateField,
    DateTimeField,
    DoubleField,
    BooleanField,
    IntegerField,
    Model,
    CompositeKey,
    fn,
    SQL,
    InternalError,
    IntegrityError,
    InterfaceError,
    DoesNotExist,
)
from playhouse.db_url import connect
# Peewee provides an alternate database implementation
# for using the mysql-connector driver.
# The implementation can be found in playhouse.mysql_ext.
from playhouse.mysql_ext import MySQLConnectorDatabase, JSONField, TextField
from vnpy.trader.constant import Offset
from vnpy.trader.setting import get_settings

from vnpy_extra.config import logging
from vnpy_extra.utils.enhancement import get_instrument_type

logger = logging.getLogger()


class AccountStrategyStatusEnum(enum.IntEnum):
    NotYet = -1
    Created = 0
    Initialized = 1
    RunPending = 2
    Running = 3
    StopPending = 4
    Stopped = 5


class StrategyBacktestStatusEnum(enum.IntEnum):
    Unavailable = 0  # 标记无效策略
    MaybeAvailable = 1  # 可能有效，需要进一步跟踪验证
    TrackingBacktest = 2  # 每日滚动更新回测状态，寻找合适的入场时机
    QuasiOnline = 3  # 准上线策略,策略的合约为"主连合约",因此,上线策略需要被转换为当期实际主力合约
    CompareTradeData = 4  # 策略已经启动，每日对比实盘交易数据与回测交易数据是否存在较大差异


def init_db():
    settings = get_settings("database.")
    keys = {"database", "user", "password", "host", "port"}
    settings = {k: v for k, v in settings.items() if k in keys}
    if is_linux_os():
        # Linux 环境下 MySQLConnectorDatabase 多进程链接失败
        # 错误提示: mysql.connector.errors.OperationalError: MySQL Connection not available.
        db = connect("mysql+pool://{user}:{password}@{host}:{port}/{database}".format(**settings))
    else:
        db = MySQLConnectorDatabase(**settings)

    return db


_USER_NAME: typing.Optional[str] = None
_BROKER_ID: typing.Optional[str] = None


def get_account() -> typing.Tuple[str, str]:
    global _USER_NAME, _BROKER_ID
    if _USER_NAME is None or _BROKER_ID is None:
        from vnpy.trader.utility import load_json
        filename: str = f"connect_ctp.json"
        connect_dic = load_json(filename)
        if len(connect_dic) == 0:
            _USER_NAME, _BROKER_ID = "test user", "0000"
        else:
            _USER_NAME = connect_dic["用户名"]
            _BROKER_ID = connect_dic["经纪商代码"]

        logger.info(f"user name='{_USER_NAME}', broker_id='{_BROKER_ID}'")

    return _USER_NAME, _BROKER_ID


def set_account(user_name, broker_id):
    global _USER_NAME, _BROKER_ID
    _USER_NAME, _BROKER_ID = user_name, broker_id


def set_account_backtest():
    user_name, broker_id = "test user", "0000"
    set_account(user_name, broker_id)


database = init_db()


class StrategyInfo(Model):
    module_name: str = CharField(max_length=150, help_text="策略的类名称")
    strategy_class_name: str = CharField(max_length=80, help_text="策略的类名称")
    backtest_folder_path: str = CharField(
        max_length=255, null=True,
        help_text="策略回测时，回测文件所在的根目录（不包含output目录）。"
                  "该目录与 StrategyBacktestStats 的 image_file_path 拼接可组成绝对路径",
    )

    class Meta:
        database = database
        legacy_table_names = False
        # table_settings = "ENGINE = MYISAM"
        indexes = (
            # 2021-02-22
            # 考虑到 strategy_class_name 相同可能会使得 StrategyInfo.get_cls_module_dic() 存在一对多的歧义情况，
            # 另外便于管理，因此，此处强制要求 strategy_class_name 必须唯一
            # create a unique on strategy_class_name
            # (('module_name', 'strategy_class_name'), True),
            (('strategy_class_name',), True),
        )

    @staticmethod
    def get_cls_id_dict() -> typing.Dict[str, int]:
        try:
            cls_id_dic = {
                stg_info.strategy_class_name: stg_info.id
                for stg_info in StrategyInfo.select().where(
                    StrategyInfo.module_name != '__main__'
                ).execute()
            }
            return cls_id_dic
        finally:
            StrategyInfo._meta.database.close()

    @staticmethod
    def get_cls_module_dic() -> typing.Dict[str, str]:
        try:
            cls_module_dic = {
                stg_info.strategy_class_name: stg_info.module_name
                for stg_info in StrategyInfo.select().where(
                    StrategyInfo.module_name != '__main__'
                ).execute()
            }
            return cls_module_dic
        finally:
            StrategyInfo._meta.database.close()

    @staticmethod
    @lru_cache()
    def get_strategy_class_by_name(strategy_class_name: str):
        obj: StrategyInfo = StrategyInfo.get(StrategyInfo.strategy_class_name == strategy_class_name)
        strategy_cls = load_class(obj.module_name, strategy_class_name)
        return strategy_cls


class SymbolsInfo(Model):
    id: int = PrimaryKeyField()
    symbols: str = TextField(
        help_text="合约列表，以数组形势进行存储，匹配原则是完全匹配，顺序也要保持一致")

    class Meta:
        database = database
        legacy_table_names = False
        # table_settings = "ENGINE = MYISAM"

    @staticmethod
    def get_symbols_id_dict() -> typing.Dict[str, int]:
        try:
            cls_id_dic = {
                obj.symbols.upper(): obj.id
                for obj in SymbolsInfo.select().execute()
            }
            return cls_id_dic
        finally:
            SymbolsInfo._meta.database.close()

    @staticmethod
    def get_or_create_curr_symbols(symbols: typing.Union[str, object, int]):
        """将合约转化为当期主力合约"""
        if isinstance(symbols, str):
            symbols_info = SymbolsInfo.get(symbols=symbols)
            symbols = symbols_info.symbols
        elif isinstance(symbols, SymbolsInfo):
            symbols = symbols.symbols
        elif isinstance(symbols, int):
            symbols_info_id = symbols
            symbols = SymbolsInfo.get_by_id(symbols_info_id).symbols
        else:
            raise ValueError(f'symbols={symbols} 无效')

        symbol_list = symbols.split('_')
        # is_portfolio = len(symbol_list) > 1
        symbols_curr_list = [FutureAdjFactor.change_curr_contract(_) for _ in symbol_list]
        symbols_curr = '_'.join(symbols_curr_list)
        symbols_info_curr, _ = SymbolsInfo.get_or_create(symbols=symbols_curr)
        return symbols_info_curr

    @staticmethod
    def get_instance(symbols):
        if isinstance(symbols, str):
            symbols_info, _ = SymbolsInfo.get_or_create(symbols=symbols)
        elif isinstance(symbols, SymbolsInfo):
            symbols_info = symbols
        elif isinstance(symbols, int):
            symbols_info = SymbolsInfo.get_by_id(symbols).symbols
        else:
            raise ValueError(f'symbols={symbols} 无效')

        return symbols_info


class FutureAdjFactor(Model):
    instrument_type: str = CharField(max_length=20, help_text="合约类型")
    trade_date = DateField(help_text="交易日")
    method: str = CharField(max_length=20, help_text="因子计算方法")
    instrument_id_main: str = CharField(null=True, max_length=50, help_text="主力合约名称")
    adj_factor_main: str = DoubleField(null=True, help_text="主力调整因子")
    instrument_id_secondary = CharField(null=True, max_length=50, help_text="次主力合约名称")
    adj_factor_secondary = DoubleField(null=True, help_text="次主力调整因子")

    class Meta:
        database = database
        table_name = 'wind_future_adj_factor'
        primary_key = CompositeKey('instrument_type', 'trade_date', 'method')

    @staticmethod
    def change_curr_contract(vt_symbol) -> str:
        """将当前合约替换为当期主力/次主力合约，如果 vt_symbol 的合约号码是 8888 则为次主力合约，其他情况均为主力合约"""
        instrument_type = get_instrument_type(vt_symbol)
        symbol, exchange = vt_symbol.split('.')
        symbol_num = symbol[len(instrument_type):]
        is_main = True
        # 如果不匹配，默认为主力合约
        if symbol_num == '8888':
            is_main = False
        elif symbol_num == '9999':
            is_main = True
        else:
            return vt_symbol

        obj = FutureAdjFactor.select(
        ).where(
            FutureAdjFactor.instrument_type == instrument_type
        ).order_by(-FutureAdjFactor.trade_date).get()
        vt_symbol_curr = obj.instrument_id_main if is_main else obj.instrument_id_secondary
        curr_contract = f"{vt_symbol_curr.split('.')[0]}.{exchange}"
        return curr_contract

    @staticmethod
    @lru_cache()
    def is_main(symbol: str) -> bool:
        symbol = symbol.upper()
        instrument_type = get_instrument_type(symbol)
        for obj in FutureAdjFactor.select().where(
                FutureAdjFactor.instrument_type == instrument_type
        ).order_by(-FutureAdjFactor.trade_date).execute():
            if obj.instrument_id_main.upper().startswith(symbol):
                is_main = True
                break
            elif obj.instrument_id_secondary.upper().startswith(symbol):
                is_main = False
                break
        else:
            raise ValueError(f'{symbol} 在 FutureAdjFactor 中找不到匹配的合约')

        return is_main


class AccountStrategyMapping(Model):
    """账户与策略对应关系"""
    user_name: str = IntegerField(help_text="用户名")
    broker_id: str = IntegerField(help_text="经纪商代码")
    stg_info: int = ForeignKeyField(StrategyInfo, on_delete='restrict', on_update='cascade',
                                    help_text="StrategyInfo 信息")
    # strategy_class_name: str = CharField(max_length=55, help_text="策略的类名称")
    symbols_info: int = ForeignKeyField(SymbolsInfo, on_delete='restrict', on_update='cascade',
                                        help_text="SymbolsInfo 信息")
    id_name: str = CharField(max_length=300, help_text="生成相关图片等文件时使用的文件名头部标示")
    strategy_settings = JSONField(help_text="策略创建时传入的 settings 参数")
    short_name: str = CharField(null=True, help_text="用于策略运行时使用的唯一标示名")
    shown_name: str = CharField(null=True, help_text="用于策略报表展示时使用的唯一标示名")
    update_dt = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], help_text="更新时间")

    class Meta:
        database = database
        legacy_table_names = False
        primary_key = CompositeKey('user_name', 'broker_id', 'stg_info', 'symbols_info', 'id_name')
        indexes = (
            # create a unique on short_name
            (('user_name', 'broker_id', 'short_name',), True),
            # create a unique on shown_name
            (('user_name', 'broker_id', 'shown_name',), True),
        )

    @staticmethod
    def get_by_account():
        user_name, broker_id = get_account()
        acc_stg_list = [_ for _ in AccountStrategyMapping.select().where(
            AccountStrategyMapping.user_name == user_name,
            AccountStrategyMapping.broker_id == broker_id
        ).execute()]
        return acc_stg_list


class StrategyBacktestStats(Model):
    # stg_info 与 StrategyInfo 外键关系在实际数据库中已经解除，但在逻辑关系中保留。
    # get_available_status_group_by_strategy 函数强烈依赖于该外键关系
    # ALTER TABLE `vnpy`.`strategy_backtest_stats`
    #   DROP FOREIGN KEY `strategy_backtest_stats_ibfk_2`,
    #   DROP FOREIGN KEY `strategy_backtest_stats_ibfk_1`;
    stg_info: int = ForeignKeyField(StrategyInfo, on_delete='restrict', on_update='cascade',
                                    help_text="StrategyInfo 信息")
    # stg_info 与 StrategyInfo 外键关系在实际数据库中已经解除
    symbols_info: int = ForeignKeyField(SymbolsInfo, on_delete='restrict', on_update='cascade',
                                        help_text="SymbolsInfo 信息")
    id_name: str = CharField(max_length=300, help_text="生成相关图片等文件时使用的文件名头部标示")
    cross_limit_method: int = SmallIntegerField(help_text="CrossLimitMethod：0:open_price 1:mid_price 2:worst_price")
    short_name: str = CharField(null=True, help_text="用于策略运行时使用的唯一标示名，[S]代表合约名称")
    shown_name: str = CharField(null=True, help_text="用于策略报表展示时使用的唯一标示名，[S]代表合约名称")
    backtest_status: int = SmallIntegerField(
        constraints=[SQL(f'DEFAULT {StrategyBacktestStatusEnum.Unavailable.value}')],
        help_text="手动标示该策略是否有效:0无效 1可能有效 2滚动更新状态 3对比实盘交易数据"
    )
    strategy_settings = JSONField(help_text="策略创建时传入的 settings 参数")
    engine_kwargs = JSONField(help_text="回测引擎创建时传入的参数")
    available = BooleanField(help_text="回测程序自动判断策略是否有效")
    update_dt = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], help_text="更新时间")
    start_date = DateField(null=True, help_text="首个交易日")
    end_date = DateField(null=True, help_text="最后交易日")
    total_days = IntegerField(null=True, help_text="总交易日")
    profit_days = IntegerField(null=True, help_text="盈利交易日")
    loss_days = IntegerField(null=True, help_text="亏损交易日")
    capital = DoubleField(null=True, help_text="起始资金")
    end_balance = DoubleField(null=True, help_text="结束资金")
    total_return = DoubleField(null=True, help_text="总收益率")
    annual_return = DoubleField(null=True, help_text="年化收益")
    max_drawdown = DoubleField(null=True, help_text="最大回撤")
    avg_drawdown = DoubleField(null=True, help_text="平均回撤")
    most_drawdown = DoubleField(null=True, help_text="取极值回撤（平均回撤-2*方差）")
    lw_drawdown = DoubleField(null=True, help_text="线性加权回撤")
    max_ddpercent = DoubleField(null=True, help_text="最大回撤百分比")
    max_dd_pct = DoubleField(null=True, help_text="最大回撤百分比")
    avg_dd_pct = DoubleField(null=True, help_text="平均回撤百分比")
    most_dd_pct = DoubleField(null=True, help_text="取极值回撤百分比")
    lw_dd_pct = DoubleField(null=True, help_text="线性加权回撤百分比")
    avg_square_dd_pct = DoubleField(null=True, help_text="均方回撤百分比")
    max_drawdown_duration = DoubleField(null=True, help_text="最长回撤天数")
    max_new_higher_duration = DoubleField(null=True, help_text="最长再创新高周期")
    total_net_pnl = DoubleField(null=True, help_text="总盈亏")
    total_commission = DoubleField(null=True, help_text="总手续费")
    total_slippage = DoubleField(null=True, help_text="总滑点")
    total_turnover = DoubleField(null=True, help_text="总成交金额")
    total_trade_count = IntegerField(null=True, help_text="总成交笔数")
    daily_net_pnl = DoubleField(null=True, help_text="日均盈亏")
    daily_commission = DoubleField(null=True, help_text="日均手续费")
    daily_slippage = DoubleField(null=True, help_text="日均滑点")
    daily_turnover = DoubleField(null=True, help_text="日均成交金额")
    daily_trade_count = DoubleField(null=True, help_text="日均成交笔数")
    daily_return = DoubleField(null=True, help_text="日均收益率")
    return_std = DoubleField(null=True, help_text="收益标准差")
    sharpe_ratio = DoubleField(null=True, help_text="Sharpe Ratio")
    sortino_ratio = DoubleField(null=True, help_text="Sortino Ratio")
    info_ratio = DoubleField(null=True, help_text="Info Ratio")
    win_ratio = DoubleField(null=True, help_text="日胜率")
    return_loss_ratio = DoubleField(null=True, help_text="盈亏比:所有盈利额占所有亏损额的比例")
    return_drawdown_ratio = DoubleField(null=True, help_text="收益回撤比")
    return_most_drawdown_ratio = DoubleField(
        null=True, help_text="取极值收益回撤比（年化收益率 / most_dd_pct 该数值将会比 calmar 略高，但更具有普遍意义）")
    return_risk_ratio = DoubleField(null=True, help_text="收益风险比 Q=win_ratio-(1-win_ratio)/return_loss_ratio")
    score = DoubleField(null=True, help_text="综合打分")
    image_file_path = CharField(null=True, max_length=1024, help_text="生成资金曲线图片路径")
    charts_data = JSONField(null=True, help_text="构建charts所需要的数据")
    indicator_dic = JSONField(null=True, help_text="所有指标的数据")

    class Meta:
        database = database
        legacy_table_names = False
        primary_key = CompositeKey('stg_info', 'symbols_info', 'id_name', 'cross_limit_method')
        indexes = (
            # create a unique on short_name
            (('stg_info', 'symbols_info', 'short_name',), True),
            # create a unique on shown_name
            (('stg_info', 'symbols_info', 'shown_name',), True),
        )

    @staticmethod
    def get_by_keys(strategy_class_name: str, symbols: str, id_name: str,
                    cross_limit_method: typing.Optional[int] = None):
        query = StrategyBacktestStats.select(
            StrategyBacktestStats, StrategyInfo, SymbolsInfo
        ).join(
            StrategyInfo, on=StrategyBacktestStats.stg_info_id == StrategyInfo.id
        ).join(
            SymbolsInfo, on=StrategyBacktestStats.symbols_info_id == SymbolsInfo.id
        ).where(
            StrategyInfo.strategy_class_name == strategy_class_name,
            SymbolsInfo.symbols == symbols,
            StrategyBacktestStats.id_name == id_name,
        )
        if cross_limit_method is not None:
            query = query.where(StrategyBacktestStats.cross_limit_method == cross_limit_method)

        for obj in query.execute():
            return obj

        return None

    @staticmethod
    @lru_cache(10)
    def get_set_by_stg(strategy_class_name: str, symbols: str, available: typing.Optional[bool] = None) -> set:
        """获取指定策略名称及合约的对应主键集合"""
        query = StrategyBacktestStats.select(
            StrategyBacktestStats, StrategyInfo, SymbolsInfo
        ).join(
            StrategyInfo, on=StrategyBacktestStats.stg_info_id == StrategyInfo.id
        ).join(
            SymbolsInfo, on=StrategyBacktestStats.symbols_info_id == SymbolsInfo.id
        ).where(
            StrategyInfo.strategy_class_name == strategy_class_name,
            SymbolsInfo.symbols == symbols,
        )
        if available is not None:
            query = query.where(
                StrategyBacktestStats.available == available,
            )

        result_set = set([
            (
                strategy_class_name,  # stats.stg_info.strategy_class_name
                symbols,  # stats.symbols_info.symbols
                stats.id_name,
                stats.cross_limit_method,
            ) for stats in query.execute()
        ])
        return result_set

    @staticmethod
    def is_existed(strategy_class_name, symbols: str, id_name: str, cross_limit_method: int, available=False) -> bool:
        """检查是否当前测试已经存在,默认之检查 available=False(无效策略) 的策略"""
        result_set = StrategyBacktestStats.get_set_by_stg(strategy_class_name, symbols, available)
        return (strategy_class_name, symbols, id_name, cross_limit_method) in result_set

    @staticmethod
    def update_stats(
            strategy_settings: dict, engine_kwargs: dict, statistics: dict,
            charts_data: dict,
            backtest_folder_path: typing.Optional[str] = None,
            old_id_name=None,
    ):
        """
        创建或更新策略回测统计数据
        :param strategy_settings:
        :param engine_kwargs:
        :param statistics:
        :param charts_data:
        :param backtest_folder_path:
        :param old_id_name: 默认为 None，如果有值则以id_name为key之一，进行更新操作
        :return:
        """
        if len(statistics) == 0 or ('total_days' in statistics and statistics['total_days'] == 0):
            return
        try:
            # 重连接：参考 https://blog.csdn.net/lluozh2015/article/details/78411884
            StrategyBacktestStats._meta.database.connection().ping(reconnect=True)

            # 更新参数
            module_name = statistics.pop('module_name')
            strategy_class_name = statistics['strategy_class_name']
            symbols = statistics['symbols']
            if backtest_folder_path is None:
                backtest_folder_path = os.path.abspath(os.path.curdir)

            stg_info, created = StrategyInfo.get_or_create(
                module_name=module_name, strategy_class_name=strategy_class_name,
                defaults=dict(backtest_folder_path=backtest_folder_path)
            )
            if (not created) and stg_info.backtest_folder_path != backtest_folder_path:
                stg_info.backtest_folder_path = backtest_folder_path
                stg_info.save()

            symbols_info, _ = SymbolsInfo.get_or_create(symbols=symbols)

            if old_id_name is not None and old_id_name != statistics['id_name']:
                # 删除旧数据，添加新记录
                # 部分情况更新将会导致主键冲突
                StrategyBacktestStats.delete().where(
                    StrategyBacktestStats.symbols_info_id == symbols_info.id,
                    StrategyBacktestStats.stg_info_id == stg_info.id,
                    StrategyBacktestStats.id_name == old_id_name,
                    StrategyBacktestStats.cross_limit_method == statistics['cross_limit_method']
                ).execute()

            StrategyBacktestStats.insert(
                stg_info_id=stg_info.id,
                symbols_info_id=symbols_info.id,
                strategy_settings=dict_2_jsonable(strategy_settings),
                engine_kwargs=dict_2_jsonable(engine_kwargs),
                charts_data=charts_data,
                update_dt=datetime.now(),
                **{k: v for k, v in statistics.items() if k not in (
                    'module_name', 'strategy_class_name', 'symbols', 'image_file_url',
                )}
            ).on_conflict(
                update=dict(
                    # stg_info_id=stg_info_id,
                    # symbols_info_id=symbols_curr_info.id,
                    strategy_settings=dict_2_jsonable(strategy_settings),
                    engine_kwargs=dict_2_jsonable(engine_kwargs),
                    charts_data=charts_data,
                    update_dt=datetime.now(),
                    **{k: v for k, v in statistics.items() if k not in (
                        'module_name', 'strategy_class_name', 'symbols', 'image_file_url',
                        'id_name', 'short_name', 'shown_name',
                    )}
                )
            ).execute()
        except:
            id_name = statistics['id_name'] if 'id_name' in statistics else ''
            logger.exception(
                "StrategyBacktestStats.update_stats 异常,不影响回测。"
                "\nid_name=%s\nstrategy_settings=%s\nengine_kwargs=%s",
                id_name, strategy_settings, engine_kwargs)
            folder_path = os.path.join('output', 'save_failed')
            os.makedirs(folder_path, exist_ok=True)
            file_name = f"{datetime_2_str(datetime.now(), '%Y-%m-%d_%H_%M_%S')}_pid_{os.getpid()}.json"
            file_path = os.path.join(folder_path, file_name)
            try:
                with open(file_path, 'w') as f:
                    json.dump(dict(
                        strategy_settings=dict_2_jsonable(strategy_settings),
                        engine_kwargs=dict_2_jsonable(engine_kwargs),
                        statistics=dict_2_jsonable(statistics),
                        charts_data=dict_2_jsonable(charts_data),
                        backtest_folder_path=backtest_folder_path,
                        old_id_name=old_id_name,
                    ), f)
            except:
                logger.exception(
                    "回测数据保存本地文件发生异常。\nfile_path=%s"
                    "\nid_name=%s\nstrategy_settings=%s\nengine_kwargs=%s",
                    file_path, id_name, strategy_settings, engine_kwargs)

        finally:
            StrategyBacktestStats._meta.database.close()

    @staticmethod
    def update_backtest_status(data_dic_list: typing.List[dict], check_account_mapping=False) -> int:
        """
        批量更新回测状态
        :param data_dic_list: 每个 item 至少包含如下字段 [
            'strategy_class_name', 'id_name', 'symbols', 'cross_limit_method', 'backtest_status',
             'short_name', 'shown_name']
        :param check_account_mapping: 检查 account_mapping 账户是否需要移除相应策略。
        :return:
        """
        if len(data_dic_list) == 0:
            return
        update_counter, del_counter = 0, 0
        try:
            cls_id_dic = StrategyInfo.get_cls_id_dict()
            symbols_id_dic = SymbolsInfo.get_symbols_id_dict()
            stg_short_num_dic = {}
            # 由于自动序号填充功能，导致无法启用 transaction
            # with database.atomic():
            for data_dic in data_dic_list:
                if 'index' in data_dic:
                    del data_dic['index']

                backtest_status = data_dic.pop("backtest_status")
                strategy_class_name = data_dic.pop('strategy_class_name')
                stg_info_id = cls_id_dic[strategy_class_name]
                symbols = data_dic.pop('symbols').upper()
                symbols_info_id = symbols_id_dic[symbols]
                short_name = data_dic.pop('short_name')
                shown_name = data_dic.pop('shown_name')
                cross_limit_method = data_dic['cross_limit_method']
                id_name = data_dic['id_name']
                if backtest_status == StrategyBacktestStatusEnum.QuasiOnline.value:
                    # 获取源对象
                    # stats_obj: StrategyBacktestStats = StrategyBacktestStats.select().where(
                    #     StrategyBacktestStats.id_name == data_dic['id_name'],
                    #     StrategyBacktestStats.stg_info_id == stg_info_id,
                    #     StrategyBacktestStats.symbols_info_id == symbols_info_id,
                    # ).get()
                    # stats_obj.backtest_status = backtest_status
                    # stats_obj.save()
                    # 插入主力合约，对应状态 StrategyBacktestStatusEnum.CompareTradeData.value
                    # 去除 short_name, shown_name 两个字段仅用于
                    # 当期主力合约 StrategyBacktestStatusEnum.CompareTradeData 的情况
                    if short_name is None or short_name == '' or pd.isna(short_name):
                        # raise ValueError(f'id_name={data_dic["id_name"]} on {symbols} short_name 不能为空')
                        # 2021-04-27 如果 short_name 为空，则自动命名，规则如下：
                        # 如果已经存在 shown_name 则继续使用
                        # 如果不存在，则以最大的数字开始递增
                        stats = StrategyBacktestStats.get(
                            StrategyBacktestStats.id_name == id_name,
                            StrategyBacktestStats.stg_info_id == stg_info_id,
                            StrategyBacktestStats.symbols_info_id == symbols_info_id,
                            StrategyBacktestStats.cross_limit_method == cross_limit_method
                        )
                        if stats.short_name is not None:
                            short_name = stats.short_name
                            logger.info(f'{strategy_class_name} [{symbols}] <{id_name}> '
                                        f'没有设置 short_name 沿用此前设置 {short_name}')
                        else:
                            key = (stg_info_id, symbols_info_id)
                            if key in stg_short_num_dic:
                                num = stg_short_num_dic[key]
                            else:
                                num = 0
                                for stats in StrategyBacktestStats.select().where(
                                        StrategyBacktestStats.stg_info_id == stg_info_id,
                                        StrategyBacktestStats.symbols_info_id == symbols_info_id,
                                        StrategyBacktestStats.short_name.is_null(False),
                                ).execute():
                                    try:
                                        tmp = int(stats.short_name.split('_')[-1])
                                    except ValueError:
                                        continue
                                    if num < tmp:
                                        num = tmp

                            # +1 作为最新的序号
                            num += 1
                            stg_short_num_dic[key] = num
                            short_name = f"[F]_{num}"
                            logger.warning(f'{strategy_class_name} [{symbols}] <{id_name}> '
                                           f'没有设置 short_name 将被自动设置为 {short_name}')

                    if shown_name is None or shown_name == '' or pd.isna(shown_name):
                        # 如果 shown_name 为空，则与 short_name 相同
                        shown_name = short_name

                # 仅更新 backtest_status 状态
                update_dic = dict(
                    backtest_status=backtest_status,
                    update_dt=datetime.now(),
                )
                if short_name is not None and not pd.isna(short_name) and shown_name != '':
                    update_dic['short_name'] = short_name

                if shown_name is not None and not pd.isna(shown_name) and shown_name != '':
                    update_dic['shown_name'] = shown_name

                update_count = StrategyBacktestStats.update(update_dic).where(
                    StrategyBacktestStats.id_name == id_name,
                    StrategyBacktestStats.stg_info_id == stg_info_id,
                    StrategyBacktestStats.symbols_info_id == symbols_info_id,
                    StrategyBacktestStats.cross_limit_method == cross_limit_method
                ).execute()
                update_counter += update_count
                if check_account_mapping and backtest_status < StrategyBacktestStatusEnum.QuasiOnline.value:
                    # 将当前策略从 account_mapping 账户中移除
                    del_count = AccountStrategyMapping.delete().where(
                        AccountStrategyMapping.symbols_info_id == symbols_info_id,
                        AccountStrategyMapping.stg_info_id == stg_info_id,
                        AccountStrategyMapping.id_name == id_name,
                    ).execute()
                    del_counter += del_count
                    logger.info(f"修改数据 {update_count} 条，删除账户映射记录 {del_count} 条")
                else:
                    logger.info(f"修改数据 {update_count} 条")

                if update_count == 0:
                    logger.warning(f'{strategy_class_name} [{symbols}] <{id_name}> 没有找到对应的记录')

            return update_counter
        finally:
            StrategyBacktestStats._meta.database.close()
            # <= 1 的情况下无需重复提示
            if update_counter > 1:
                if del_counter > 0:
                    logger.info(f"累计修改数据 {update_counter} 条，删除账户映射记录 {del_counter} 条")
                else:
                    logger.info(f"累计修改数据 {update_counter} 条")

    @staticmethod
    def get_available_status_group_by_strategy(
            symbols_list=None, strategy_class_name_list=None) -> typing.Dict[typing.Tuple[str, str], list]:
        ret_data = OrderedDict()
        try:
            query = StrategyBacktestStats.select(
                StrategyBacktestStats, StrategyInfo, SymbolsInfo
            ).join(
                StrategyInfo, on=StrategyBacktestStats.stg_info_id == StrategyInfo.id
            ).join(
                SymbolsInfo, on=StrategyBacktestStats.symbols_info_id == SymbolsInfo.id
            ).where(
                StrategyBacktestStats.backtest_status > StrategyBacktestStatusEnum.Unavailable.value
            ).order_by(
                StrategyBacktestStats.symbols_info_id,
                StrategyBacktestStats.stg_info_id,
                StrategyBacktestStats.short_name
            )
            if strategy_class_name_list is not None and len(strategy_class_name_list) > 0:
                query = query.where(StrategyInfo.strategy_class_name << strategy_class_name_list)
            if symbols_list is not None and len(symbols_list) > 0:
                query = query.where(SymbolsInfo.symbols << symbols_list)

            for obj in query.execute():
                key = (
                    obj.stg_info.module_name,
                    obj.stg_info.strategy_class_name,
                    obj.symbols_info.symbols
                )
                ret_data.setdefault(key, []).append(obj)

            return ret_data
        finally:
            StrategyBacktestStats._meta.database.close()

    @staticmethod
    def get_by_status(status: StrategyBacktestStatusEnum = StrategyBacktestStatusEnum.CompareTradeData.value
                      ) -> list:
        ret_data = []
        try:
            for obj in StrategyBacktestStats.select(
                    StrategyBacktestStats, StrategyInfo, SymbolsInfo
            ).join(
                StrategyInfo, on=StrategyBacktestStats.stg_info_id == StrategyInfo.id
            ).join(
                SymbolsInfo, on=StrategyBacktestStats.symbols_info_id == SymbolsInfo.id
            ).where(
                StrategyBacktestStats.backtest_status == status
            ).order_by(
                StrategyBacktestStats.short_name
            ).execute():
                ret_data.append(obj)

            return ret_data
        finally:
            StrategyBacktestStats._meta.database.close()

    @staticmethod
    def import_by_settings(stats_list: typing.List[dict]):
        try:
            with database.atomic():
                for stats in stats_list:
                    module_name = stats.pop('module_name')
                    strategy_class_name = stats.pop('strategy_class_name')
                    symbols = stats.pop('symbols')
                    stg_info, _ = StrategyInfo.get_or_create(
                        module_name=module_name, strategy_class_name=strategy_class_name)
                    symbols_str = '_'.join(symbols) if isinstance(symbols, list) else symbols
                    symbols_info, _ = SymbolsInfo.get_or_create(symbols=symbols_str)
                    id_name = stats.pop('id_name')
                    cross_limit_method = stats.pop('cross_limit_method')

                    StrategyBacktestStats.insert(
                        stg_info=stg_info,
                        symbols_info=symbols_info,
                        id_name=id_name,
                        cross_limit_method=cross_limit_method,
                        available=True,
                        update_dt=datetime.now(),
                        **stats
                    ).on_conflict(
                        update=dict(
                            available=True,
                            update_dt=datetime.now(),
                            **stats
                        )
                    ).execute()
        finally:
            StrategyBacktestStats._meta.database.close()

    def get_shown_name_with_symbol(self, symbols_info: typing.Union[str, SymbolsInfo, int], none_if_no_s_pattern=True):
        """将 shown_name 中的 [S] 替换为指定的 symbols"""
        return StrategyBacktestStats.replace_name_with_symbol(
            self.shown_name, symbols_info, none_if_no_s_pattern=none_if_no_s_pattern)

    def get_short_name_with_symbol(self, symbols_info: typing.Union[str, SymbolsInfo, int], none_if_no_s_pattern=True):
        """将 shown_name 中的 [S] 替换为指定的 symbols"""
        return StrategyBacktestStats.replace_name_with_symbol(
            self.short_name, symbols_info, none_if_no_s_pattern=none_if_no_s_pattern)

    @staticmethod
    def replace_name_with_symbol(name, symbols_info, none_if_no_s_pattern=True):
        if name is None or pd.isna(name) or name == '':
            raise ValueError(f"name={name} 无效")
        symbols_info = SymbolsInfo.get_instance(symbols_info)
        symbols = symbols_info.symbols
        if none_if_no_s_pattern and re.search(r'\[S]', name) is None:
            return None
        else:
            symbols_no_ex = '_'.join([_.split('.')[0] for _ in symbols.split('_')])
            return re.sub(r'\[S]', symbols_no_ex, name)

    def add_2_account_strategy_mapping(
            self,
            user_name: typing.Optional[typing.Union[str, int]] = None,
            broker_id: typing.Optional[typing.Union[str, int]] = None,
    ):
        """建立账户与策略的关联关系"""
        if user_name is None or broker_id is None:
            user_name, broker_id = get_account()

        user_name, broker_id = int(user_name), int(broker_id)
        symbols = self.symbols_info.symbols
        if self.shown_name is None or self.short_name is None:
            logger.warning(
                '%s[%s]  short_name=%s, shown_name=%s 无效，忽略该策略',
                self.stg_info.strategy_class_name, symbols,
                self.short_name, self.shown_name)
            return

        try:
            AccountStrategyMapping.insert(
                user_name=user_name,
                broker_id=broker_id,
                stg_info_id=self.stg_info_id,
                symbols_info_id=self.symbols_info_id,
                id_name=self.id_name,
                short_name=self.short_name,
                shown_name=self.shown_name,
                update_dt=datetime.now(),
                strategy_settings=self.strategy_settings,
            ).on_conflict(
                update=dict(
                    # stg_info_id=stg_info_id,
                    # symbols_info_id=symbols_info_id,
                    update_dt=datetime.now(),
                    short_name=self.short_name,
                    shown_name=self.shown_name,
                    strategy_settings=self.strategy_settings,
                )
            ).execute()
        except IntegrityError:
            logger.exception("%s[%s] 账户添加策略异常", user_name, broker_id)

    def apply_2_symbol(
            self, symbols_curr: typing.Optional[typing.Union[str, SymbolsInfo]] = None,
            ignore_no_s_pattern_record=False):
        """将当前策略应用到某一品种上，替换主力合约为当前品种，修改 shown_name, short_name 名字"""
        if symbols_curr is None:
            # 默认为当前主力合约
            symbols_info_curr = SymbolsInfo.get_or_create_curr_symbols(self.symbols_info.symbols)
        else:
            symbols_info_curr = SymbolsInfo.get_instance(symbols_curr)

        from vnpy_extra.backtest.portfolio_strategy.template import StrategyTemplate
        from vnpy_extra.backtest.cta_strategy.template import CtaTemplate
        strategy_class_name = self.stg_info.strategy_class_name
        symbols_curr = symbols_info_curr.symbols
        symbols_curr_list = symbols_curr.split('_')
        symbol_list = self.symbols_info.symbols.split('_')
        if symbols_curr_list == symbol_list:
            return None

        is_multi = len(symbols_curr_list) > 1
        if is_multi:
            stg_obj: typing.Union[StrategyTemplate, CtaTemplate] = create_instance(
                self.stg_info.module_name, strategy_class_name,
                strategy_engine=None, strategy_name=strategy_class_name, vt_symbols=symbols_curr_list,
                setting=self.strategy_settings.copy())
        else:
            stg_obj: typing.Union[StrategyTemplate, CtaTemplate] = create_instance(
                self.stg_info.module_name, strategy_class_name,
                cta_engine=None, strategy_name=strategy_class_name, vt_symbol=symbols_curr,
                setting=self.strategy_settings.copy())

        # 修改 shown_name, short_name 名字
        if hasattr(stg_obj, 'get_name_by_pattern'):
            # 新版本统一要实现 get_name_by_pattern 函数
            short_name = stg_obj.get_name_by_pattern(self.short_name)
            shown_name = stg_obj.get_name_by_pattern(self.shown_name)
        else:
            # 兼容旧版本
            short_name = self.get_short_name_with_symbol(
                symbols_info_curr, none_if_no_s_pattern=ignore_no_s_pattern_record)
            shown_name = self.get_shown_name_with_symbol(
                symbols_info_curr, none_if_no_s_pattern=ignore_no_s_pattern_record)

        if (not ignore_no_s_pattern_record) and (short_name is None or shown_name is None):
            raise ValueError(f'short_name={self.short_name}, shown_name={self.shown_name} 无效')

        # 修改 engine_kwargs
        engine_kwargs = self.engine_kwargs.copy()
        symbol_mapping_dic = dict(zip(symbol_list, symbols_curr_list))
        symbols_curr = '_'.join(symbols_curr_list)
        symbols_curr_info, _ = SymbolsInfo.get_or_create(symbols=symbols_curr)
        is_portfolio = len(symbol_list) > 1
        if is_portfolio:
            engine_kwargs["vt_symbols"] = symbols_curr_list
            for _ in ['rates', "sizes", "slippages", "priceticks"]:
                if _ in engine_kwargs:
                    item: dict = engine_kwargs[_].copy()
                    item_new = {symbol_mapping_dic[k]: v for k, v in item.items()}
                    engine_kwargs[_] = item_new

        else:
            engine_kwargs["vt_symbol"] = symbols_curr_list[0]

        # 添加策略
        StrategyBacktestStats.insert(
            stg_info=self.stg_info,
            symbols_info=symbols_info_curr,
            id_name=self.id_name,
            cross_limit_method=self.cross_limit_method,
            short_name=short_name,
            shown_name=shown_name,
            backtest_status=StrategyBacktestStatusEnum.CompareTradeData.value,
            strategy_settings=self.strategy_settings,
            engine_kwargs=engine_kwargs,
            available=True,
            update_dt=datetime.now(),
        ).on_conflict(
            update=dict(
                cross_limit_method=self.cross_limit_method,
                short_name=short_name,
                shown_name=shown_name,
                backtest_status=StrategyBacktestStatusEnum.CompareTradeData.value,
                strategy_settings=self.strategy_settings,
                engine_kwargs=engine_kwargs,
                available=True,
                update_dt=datetime.now(),
            )
        ).execute()
        try:
            new_obj = StrategyBacktestStats.get(
                StrategyBacktestStats.stg_info_id == self.stg_info,
                StrategyBacktestStats.symbols_info_id == symbols_info_curr,
                StrategyBacktestStats.id_name == self.id_name,
                StrategyBacktestStats.cross_limit_method == self.cross_limit_method,
            )
        except DoesNotExist:
            # 部分情况下可能由于 id_name 变更导致查不到数据的情况，因此使用 short_name 进行查找。
            new_obj = StrategyBacktestStats.get(
                StrategyBacktestStats.stg_info_id == self.stg_info,
                StrategyBacktestStats.symbols_info_id == symbols_info_curr,
                StrategyBacktestStats.short_name == short_name,
                StrategyBacktestStats.cross_limit_method == self.cross_limit_method,
            )
        return new_obj

    @staticmethod
    def add_mapping_all(strategy_class_name: typing.Optional[typing.Union[str, StrategyInfo, int]] = None,
                        symbols_info: typing.Optional[typing.Union[str, SymbolsInfo, int]] = None,
                        ignore_no_s_pattern_record=False
                        ):
        """将指定策略或品质的全部准生产策略加载到账户"""
        query = StrategyBacktestStats.select(StrategyBacktestStats, StrategyInfo, SymbolsInfo).join(
            StrategyInfo, on=StrategyBacktestStats.stg_info_id == StrategyInfo.id
        ).join(
            SymbolsInfo, on=StrategyBacktestStats.symbols_info_id == SymbolsInfo.id
        ).where(
            StrategyBacktestStats.backtest_status == StrategyBacktestStatusEnum.QuasiOnline.value,
            StrategyBacktestStats.short_name.is_null(False),
            StrategyBacktestStats.shown_name.is_null(False),
        )
        # 整理数据
        if strategy_class_name is not None:
            if isinstance(strategy_class_name, str):
                stg_info_id = StrategyInfo.get(strategy_class_name=strategy_class_name).id
            elif isinstance(strategy_class_name, StrategyInfo):
                stg_info_id = strategy_class_name.id
            elif isinstance(strategy_class_name, int):
                stg_info_id = strategy_class_name
            else:
                raise ValueError(f'strategy_class_name={strategy_class_name} 无效')
            query = query.where(
                StrategyBacktestStats.stg_info_id == stg_info_id
            )

        if symbols_info is not None:
            symbols_info = SymbolsInfo.get_instance(symbols_info)
            # symbols = symbols_info.symbols
            # symbols_info_id = symbols_info.id
            query = query.where(
                StrategyBacktestStats.symbols_info_id == symbols_info.id
            )

        # 批量加载
        with database.atomic():
            count = 0
            for stats_obj in query.execute():
                # 将当前合约转化为当期主力合约
                stats_obj_curr = stats_obj.apply_2_symbol()
                if stats_obj_curr is not None:
                    stats_obj_curr.add_2_account_strategy_mapping()
                    count += 1

        user_name, _ = get_account()
        logger.info("strategy_class_name=%s, symbols=%s %d 条策略加载到账户 %s",
                    strategy_class_name, symbols_info, count, user_name)

    @staticmethod
    def expire_stats(symbols_list: typing.List[str]):
        update_counter, del_counter = 0, 0
        try:
            for symbols in symbols_list:
                # -StrategyBacktestStats.backtest_status 被翻译为 `backtest_status` DESC 因此不能使用字段前面带 ’-‘ 的情况
                update_count = StrategyBacktestStats.update(
                    backtest_status=SQL('-backtest_status')
                ).where(
                    StrategyBacktestStats.backtest_status > 0,
                    StrategyBacktestStats.symbols_info_id == SymbolsInfo.select(
                        SymbolsInfo.id).where(SymbolsInfo.symbols == symbols)
                ).execute()
                update_counter += update_count

                del_count = AccountStrategyMapping.delete().where(
                    AccountStrategyMapping.symbols_info == SymbolsInfo.select(
                        SymbolsInfo.id).where(SymbolsInfo.symbols == symbols)
                ).execute()

                del_counter += del_count
                if del_count > 0:
                    logger.info(f"%s 合约已过期，%d 条策略标记为失效，删除账户映射记录 %d 条。",
                                symbols, update_count, del_count)
                else:
                    logger.info(f"%s 合约已过期，%d 条策略标记为失效。", symbols, update_count)
        finally:
            StrategyBacktestStats._meta.database.close()
            # <= 1 的情况下无需重复提示
            if len(symbols_list) > 1:
                if del_counter > 0:
                    logger.info("累计标记合约 %s 失效策略 %d 条，删除账户映射记录 %d 条。",
                                symbols_list, update_counter, del_counter)
                else:
                    logger.info("累计标记合约 %s 失效策略 %d 条。", symbols_list, update_counter)

    @staticmethod
    def set_strategy_unavailable(strategy_class_name: typing.Union[str, StrategyInfo, int],
                                 symbols_list: typing.List[str]):
        """设置某策略在某些合约上失效"""
        update_counter, del_counter = 0, 0
        try:
            if isinstance(strategy_class_name, str):
                stg_info_id = StrategyInfo.get(strategy_class_name=strategy_class_name).id
            elif isinstance(strategy_class_name, StrategyInfo):
                stg_info_id = strategy_class_name.id
            elif isinstance(strategy_class_name, int):
                stg_info_id = strategy_class_name
            else:
                raise ValueError(f'strategy_class_name={strategy_class_name} 无效')

            for symbols in symbols_list:
                # -StrategyBacktestStats.backtest_status 被翻译为 `backtest_status` DESC 因此不能使用字段前面带 ’-‘ 的情况
                update_count = StrategyBacktestStats.update(
                    backtest_status=SQL('-backtest_status')
                ).where(
                    StrategyBacktestStats.stg_info_id == stg_info_id,
                    StrategyBacktestStats.backtest_status > 0,
                    StrategyBacktestStats.symbols_info_id == SymbolsInfo.select(
                        SymbolsInfo.id).where(SymbolsInfo.symbols == symbols)
                ).execute()
                update_counter += update_count
                del_count = AccountStrategyMapping.delete().where(
                    AccountStrategyMapping.stg_info_id == stg_info_id,
                    AccountStrategyMapping.symbols_info == SymbolsInfo.select(
                        SymbolsInfo.id).where(SymbolsInfo.symbols == symbols)
                ).execute()
                del_counter += del_count
                if del_count > 0:
                    logger.info(f"%s %s 合约 %d 条策略标记为失效。删除账户映射记录 %d 条",
                                strategy_class_name, symbols, update_count, del_count)
                else:
                    logger.info(f"%s %s 合约 %d 条策略标记为失效。", strategy_class_name, symbols, update_count)
        finally:
            StrategyBacktestStats._meta.database.close()
            # <= 1 的情况下无需重复提示
            if len(symbols_list) > 1:
                if del_counter > 0:
                    logger.info("%s 累计标记合约 %s 失效策略 %d 条，删除账户映射记录 %d 条。",
                                strategy_class_name, symbols_list, update_counter, del_counter)
                else:
                    logger.info("%s 累计标记合约 %s 失效策略 %d 条。",
                                strategy_class_name, symbols_list, update_counter)


def _test_expire_stats():
    symbols_list = [
        'rb2105.SHFE', 'FG105.CZCE', 'SM105.CZCE', 'V2105.DCE', 'CY105.CZCE', 'j2105.DCE', 'MA105.CZCE', 'P2105.DCE',
        'SC2105.INE', 'SP2105.SHFE', 'UR105.CZCE',
        'AL2105.SHFE_AL2106.SHFE', 'CF105.CZCE_CF107.CZCE', 'EB2105.DCE_EB2106.DCE',
        'EB2105.DCE_EB2106.DCE', 'L2105.DCE_L2109.DCE', 'PB2105.SHFE_PB2106.SHFE', 'RR2106.DCE_RR2107.DCE',
        'CF105.CZCE_CF107.CZCE', 'rb2105.SHFE_hc2105.SHFE',

    ]
    StrategyBacktestStats.expire_stats(symbols_list=symbols_list)


class StrategyBacktestStatsArchive(StrategyBacktestStats):
    id: int = PrimaryKeyField()

    class Meta:
        database = database
        legacy_table_names = False
        # indexes = ((("strategy_class_name", "id_name", "symbols", "cross_limit_method"), True),)
        # table_settings = 'ENGINE = MYISAM'

    @staticmethod
    def archive(stats_list_dic: typing.Dict[typing.Tuple[str, str], typing.List[StrategyBacktestStats]]):
        """将现有 StrategyBacktestStats 中的策略统计数据进行归档"""
        try:
            with database.atomic():
                for stats_list in stats_list_dic.values():
                    if len(stats_list) == 0:
                        continue
                    fields = list(stats_list[0]._meta.fields.keys())
                    StrategyBacktestStatsArchive.insert_many(
                        [[getattr(stats, _) for _ in fields] for stats in stats_list],
                        fields=fields
                    ).execute()

        finally:
            StrategyBacktestStatsArchive._meta.database.close()

    @staticmethod
    def restore(strategy_class_name, symbols=None, id_name=None) -> int:
        try:
            count = 0
            with database.atomic():
                sub_query = StrategyBacktestStatsArchive.select(
                    fn.MAX(StrategyBacktestStatsArchive.id)
                ).join(
                    StrategyInfo, on=StrategyBacktestStatsArchive.stg_info == StrategyInfo.id
                ).join(
                    SymbolsInfo, on=StrategyBacktestStatsArchive.symbols_info == SymbolsInfo.id
                ).where(
                    StrategyInfo.strategy_class_name == strategy_class_name
                )
                if symbols is not None:
                    sub_query = sub_query.where(SymbolsInfo.symbols == symbols)

                if id_name is not None and id_name != '':
                    sub_query = sub_query.where(StrategyBacktestStatsArchive.id_name == id_name)

                sub_query = sub_query.group_by(
                    StrategyBacktestStatsArchive.stg_info_id,
                    StrategyBacktestStatsArchive.symbols_info_id,
                    StrategyBacktestStatsArchive.id_name
                )
                fields = list(StrategyBacktestStats._meta.fields.keys())
                for obj in StrategyBacktestStatsArchive.select(
                        StrategyBacktestStatsArchive, StrategyInfo, SymbolsInfo
                ).join(
                    StrategyInfo, on=StrategyBacktestStatsArchive.stg_info == StrategyInfo.id
                ).join(
                    SymbolsInfo, on=StrategyBacktestStatsArchive.symbols_info == SymbolsInfo.id
                ).where(
                    StrategyBacktestStatsArchive.id << sub_query  # StrategyBacktestStatsArchive.id.in_(sub_query)
                ).execute():
                    count += StrategyBacktestStats.insert(
                        **{_: getattr(obj, _) for _ in fields}
                    ).on_conflict_ignore().execute()

                return count
        finally:
            StrategyBacktestStatsArchive._meta.database.close()
            # pass


class StrategyStatus(Model):
    """
    策略状态信息
    * strategy_name 策略名称
    * status 策略状态
    """
    user_name: str = CharField(max_length=30)
    broker_id: str = CharField(max_length=20)
    strategy_name: str = CharField(max_length=180)
    shown_name: str = CharField(null=True, help_text="生成报告需要的对外展示用名，如果没有则使用 strategy_name")
    status: int = SmallIntegerField()
    symbols: str = CharField(max_length=255)
    strategy_settings = JSONField(null=True, help_text="策略创建时传入的 settings 参数")
    backtest_status: int = SmallIntegerField(default=StrategyBacktestStatusEnum.CompareTradeData.value)
    description: str = CharField(null=True)
    update_dt = DateTimeField()

    @staticmethod
    def is_table_exists():
        try:
            is_exists = StrategyStatus.table_exists()
            return is_exists
        except:
            return False
        finally:
            StrategyStatus._meta.database.close()

    @staticmethod
    def set_status(strategy_name, status: int):
        try:
            user_name, broker_id = get_account()
            ret_data = StrategyStatus.update(
                status=status, update_dt=datetime.now()
            ).where(
                StrategyStatus.user_name == user_name,
                StrategyStatus.broker_id == broker_id,
                StrategyStatus.strategy_name == strategy_name,
            ).execute()
            logger.debug("%s[%s] %s status=%d", user_name, broker_id, strategy_name, status)
        finally:
            StrategyStatus._meta.database.close()
        return ret_data

    @staticmethod
    def query_status(strategy_name) -> typing.Optional[int]:
        try:
            user_name, broker_id = get_account()
            ss: StrategyStatus = StrategyStatus.get_or_none(
                StrategyStatus.user_name == user_name,
                StrategyStatus.broker_id == broker_id,
                StrategyStatus.strategy_name == strategy_name,
            )
            if ss is None:
                status = -1
            else:
                status = ss.status

            logger.debug("%s[%s] %s status=%d", user_name, broker_id, strategy_name, status)
            return status
        except InterfaceError as exp:
            logger.exception(f"获取 {strategy_name} 策略状态时，数据库访问异常。{exp.args}")
            return None
        finally:
            StrategyStatus._meta.database.close()

    @staticmethod
    def register_strategy(strategy_name, status: int, symbols: str, strategy_settings: dict):
        try:
            user_name, broker_id = get_account()
            ret_data = StrategyStatus.insert(
                user_name=user_name, broker_id=broker_id,
                strategy_name=strategy_name, status=status, strategy_settings=strategy_settings,
                symbols=symbols, update_dt=datetime.now(),
                backtest_status=StrategyBacktestStatusEnum.CompareTradeData.value
            ).on_conflict(
                preserve=[StrategyStatus.user_name, StrategyStatus.broker_id, StrategyStatus.strategy_name],
                update={
                    StrategyStatus.status: status,
                    StrategyStatus.strategy_settings: strategy_settings,
                    StrategyStatus.update_dt: datetime.now(),
                    StrategyStatus.backtest_status: StrategyBacktestStatusEnum.CompareTradeData.value,
                }
            ).execute()
            logger.debug("%s[%s] %s status=%d", user_name, broker_id, strategy_name, status)
            return ret_data
        finally:
            StrategyStatus._meta.database.close()

    @staticmethod
    def query_all():
        user_name, broker_id = get_account()
        try:
            ret_data = [_ for _ in StrategyStatus.select().where(
                StrategyStatus.user_name == user_name,
                StrategyStatus.broker_id == broker_id,
            ).execute()]
        finally:
            StrategyStatus._meta.database.close()

        return ret_data

    class Meta:
        database = database
        legacy_table_names = False
        primary_key = CompositeKey('user_name', 'broker_id', 'strategy_name')
        table_settings = "ENGINE = MYISAM"
        # table_settings = "ENGINE = MEMORY"


class OrderDataModel(Model):
    """
    策略状态信息
    实际生产环境中 orderid 可以唯一确定
    但是，回测环境下，需要与策略名称，品种进行配合才行
    * strategy_name 策略名称
    """
    user_name: str = CharField(max_length=50)
    broker_id: str = CharField(max_length=20)
    strategy_name: str = CharField()
    orderid: str = CharField()
    symbol: str = CharField(max_length=20)
    exchange: str = CharField(max_length=20)
    order_type: str = CharField(max_length=20)
    direction: str = CharField(max_length=8)
    offset: str = CharField(max_length=8)
    price = DoubleField()
    volume = DoubleField()
    status: str = CharField(max_length=20)
    datetime = DateTimeField()

    class Meta:
        database = database
        legacy_table_names = False
        primary_key = CompositeKey('user_name', 'broker_id', 'strategy_name', 'orderid', 'symbol')
        # indexes = ((("strategy_name", "symbol"), True),)

    @staticmethod
    def bulk_replace(data_dic_list: typing.List[dict]):
        user_name, broker_id = get_account()
        try:
            with database.atomic():
                for data_dic in data_dic_list:
                    data_dic['user_name'] = user_name
                    data_dic['broker_id'] = broker_id
                    OrderDataModel.replace(**data_dic).execute()

        finally:
            OrderDataModel._meta.database.close()


class TradeDataModel(Model):
    """
    策略状态信息
    实际生产环境中 tradeid 可以唯一确定
    但是，回测环境下，需要与策略名称，品种进行配合才行
    * strategy_name 策略名称
    """
    user_name: str = CharField(max_length=50)
    broker_id: str = CharField(max_length=20)
    strategy_name: str = CharField()
    tradeid: str = CharField()
    symbol: str = CharField(max_length=20)
    exchange: str = CharField(max_length=20)
    orderid: str = CharField()
    direction: str = CharField(max_length=8)
    offset: str = CharField(max_length=8)
    price = DoubleField()
    volume = DoubleField()
    datetime = DateTimeField()

    class Meta:
        database = database
        legacy_table_names = False
        primary_key = CompositeKey('user_name', 'broker_id', 'strategy_name', 'tradeid', 'symbol')
        # indexes = ((("strategy_name", "symbol"), True),)

    @staticmethod
    def get_latest_trade_data_by_stg(strategy_name, vt_symbol):
        """
        获取各个策略最近的一笔开仓交易单
        """
        user_name, broker_id = get_account()
        symbol, exchange = vt_symbol.split('.')
        try:
            trade_data_open: TradeDataModel = TradeDataModel.select().where(
                TradeDataModel.user_name == user_name,
                TradeDataModel.broker_id == broker_id,
                TradeDataModel.strategy_name == strategy_name,
                TradeDataModel.symbol == symbol,
                TradeDataModel.offset == Offset.OPEN.value
            ).order_by(TradeDataModel.datetime.desc()).first()
            trade_data_close: TradeDataModel = TradeDataModel.select().where(
                TradeDataModel.user_name == user_name,
                TradeDataModel.broker_id == broker_id,
                TradeDataModel.strategy_name == strategy_name,
                TradeDataModel.symbol == symbol,
                TradeDataModel.offset != Offset.OPEN.value
            ).order_by(TradeDataModel.datetime.desc()).first()

        finally:
            TradeDataModel._meta.database.close()

        return trade_data_open, trade_data_close

    @staticmethod
    def get_latest_open_trade_data():
        """
        获取各个策略最近的一笔开仓交易单
        """
        user_name, broker_id = get_account()
        sql_str = """select trades.* from trade_data_model trades inner join (
            select strategy_name, max(`datetime`) dt from trade_data_model 
            where user_name=%s and broker_id=%s and offset=%s
            group by strategy_name) latest
            on trades.strategy_name = latest.strategy_name
            and trades.`datetime` = latest.dt
            where user_name=%s and broker_id=%s and offset=%s
            """
        strategy_symbol_latest_open_trade_data_dic = defaultdict(dict)
        try:
            for trade_data in TradeDataModel.raw(
                    sql_str, user_name, broker_id, Offset.OPEN.value,
                    user_name, broker_id, Offset.OPEN.value, ).execute():
                strategy_symbol_latest_open_trade_data_dic[trade_data.strategy_name][trade_data.symbol] = trade_data
        finally:
            TradeDataModel._meta.database.close()

        return strategy_symbol_latest_open_trade_data_dic

    @staticmethod
    def query_latest_n_trade_date_list(latest_n) -> typing.List[date]:
        user_name, broker_id = get_account()
        sql_str = f"select distinct Date(`datetime`) from trade_data_model" \
                  f" where user_name=%s and broker_id=%s" \
                  f" order by Date(`datetime`) desc limit {latest_n}"
        trade_date_list = []
        try:
            for trade_date in database.execute_sql(sql_str, [user_name, broker_id]):
                trade_date_list.append(trade_date[0])
        finally:
            database.close()

        return trade_date_list

    @staticmethod
    def query_trade_data_by_strategy_since(
            strategy_name: str = None, trade_dt: datetime = None
    ) -> typing.Dict[str, list]:
        """
        :param strategy_name
        :param trade_dt 可以为空，非空情况下，返回大于此（不包含）时间的全部交易数据
        """
        user_name, broker_id = get_account()
        strategy_symbol_trade_data_list_dic = defaultdict(list)
        try:
            if trade_dt is None:
                for _ in TradeDataModel.select().where(
                        TradeDataModel.user_name == user_name,
                        TradeDataModel.broker_id == broker_id,
                        TradeDataModel.strategy_name == strategy_name
                ).order_by(TradeDataModel.datetime, TradeDataModel.tradeid).execute():
                    strategy_symbol_trade_data_list_dic[_.symbol].append(_)
            else:
                for _ in TradeDataModel.select().where(
                        TradeDataModel.user_name == user_name,
                        TradeDataModel.broker_id == broker_id,
                        TradeDataModel.strategy_name == strategy_name,
                        TradeDataModel.datetime > trade_dt
                ).order_by(TradeDataModel.datetime, TradeDataModel.tradeid).execute():
                    strategy_symbol_trade_data_list_dic[_.symbol].append(_)
        finally:
            TradeDataModel._meta.database.close()

        return strategy_symbol_trade_data_list_dic

    @staticmethod
    def query_trade_data_by_strategy_symbol_since(
            strategy_name: str, symbol: str, trade_dt: datetime = None
    ) -> list:
        """
        :param strategy_name
        :param trade_dt 可以为空，非空情况下，返回大于此（不包含）时间的全部交易数据
        """
        user_name, broker_id = get_account()
        strategy_symbol_trade_data_list = []
        try:
            if trade_dt is None:
                for _ in TradeDataModel.select().where(
                        TradeDataModel.user_name == user_name,
                        TradeDataModel.broker_id == broker_id,
                        TradeDataModel.strategy_name == strategy_name,
                        TradeDataModel.symbol == symbol,
                ).order_by(TradeDataModel.datetime).execute():
                    strategy_symbol_trade_data_list.append(_)
            else:
                for _ in TradeDataModel.select().where(
                        TradeDataModel.user_name == user_name,
                        TradeDataModel.broker_id == broker_id,
                        TradeDataModel.strategy_name == strategy_name,
                        TradeDataModel.symbol == symbol,
                        TradeDataModel.datetime > trade_dt
                ).order_by(TradeDataModel.datetime).execute():
                    strategy_symbol_trade_data_list.append(_)
        finally:
            TradeDataModel._meta.database.close()

        return strategy_symbol_trade_data_list

    @staticmethod
    def query_trade_data_since(
            update_dt: datetime = None
    ) -> typing.Dict[str, typing.Dict[str, list]]:
        """
        :param update_dt 可以为空，非空情况下，返回大于此（不包含）时间的全部交易数据
        """
        user_name, broker_id = get_account()
        strategy_symbol_trade_data_list_dic = defaultdict(lambda: defaultdict(list))
        try:
            if update_dt is None:
                for _ in TradeDataModel.select().where(
                        TradeDataModel.user_name == user_name,
                        TradeDataModel.broker_id == broker_id,
                ).order_by(TradeDataModel.datetime).execute():
                    strategy_symbol_trade_data_list_dic[_.strategy_name][_.symbol].append(_)
            else:
                for _ in TradeDataModel.select().where(
                        TradeDataModel.user_name == user_name,
                        TradeDataModel.broker_id == broker_id,
                        TradeDataModel.datetime > update_dt
                ).order_by(TradeDataModel.datetime).execute():
                    strategy_symbol_trade_data_list_dic[_.strategy_name][_.symbol].append(_)
        finally:
            TradeDataModel._meta.database.close()

        return strategy_symbol_trade_data_list_dic

    @staticmethod
    def bulk_replace(data_dic_list: typing.List[dict]):
        user_name, broker_id = get_account()
        try:
            with database.atomic():
                for data_dic in data_dic_list:
                    data_dic['user_name'] = user_name
                    data_dic['broker_id'] = broker_id
                    TradeDataModel.replace(**data_dic).execute()

        finally:
            TradeDataModel._meta.database.close()

    @staticmethod
    def clear_by_strategy_name(strategy_name):
        user_name, broker_id = get_account()
        try:
            TradeDataModel.delete().where(
                TradeDataModel.user_name == user_name,
                TradeDataModel.broker_id == broker_id,
                TradeDataModel.strategy_name == strategy_name).execute()
        except InternalError:
            logger.exception("strategy_name='%s' and use_name='%s' clean exception", strategy_name, user_name)
        finally:
            TradeDataModel._meta.database.close()


class LatestTickPriceModel(Model):
    """
    策略状态信息
    * symbol 产品名称
    """
    symbol: str = CharField(max_length=20, primary_key=True)
    exchange: str = CharField(max_length=20)
    price = DoubleField()
    volume = DoubleField()
    datetime = DateTimeField()

    class Meta:
        database = database
        legacy_table_names = False
        # primary_key = CompositeKey('symbol')
        table_settings = "ENGINE = MEMORY"

    @staticmethod
    def query_latest_price(symbol):
        """
        获取各个策略最近的一笔开仓交易单
        """
        try:
            data: LatestTickPriceModel = LatestTickPriceModel.get_or_none(LatestTickPriceModel.symbol == symbol)
        finally:
            LatestTickPriceModel._meta.database.close()

        return data

    @staticmethod
    def query_all_latest_price() -> dict:
        """
        获取各个策略最近的一笔开仓交易单
        """
        try:
            symbol_tick_dic: typing.Dict[str, LatestTickPriceModel] = {
                _.symbol: _ for _ in LatestTickPriceModel.select()}
        finally:
            LatestTickPriceModel._meta.database.close()

        return symbol_tick_dic


class PositionStatusModel(Model):
    """
    策略持仓信息
    * strategy_name 策略名称
    """
    user_name: str = CharField(max_length=50)
    broker_id: str = CharField(max_length=20)
    tradeid: str = CharField()
    strategy_name: str = CharField()
    symbol: str = CharField(max_length=20)
    exchange: str = CharField(max_length=20)
    trade_date = DateField()
    trade_dt = DateTimeField()
    direction: str = CharField(max_length=8)
    avg_price = DoubleField()  # 平均持仓成本
    latest_price = DoubleField()  # 最新价格
    volume = DoubleField()
    holding_gl = DoubleField()  # holding gain and loss 持仓盈亏
    offset_gl = DoubleField()  # offset gain and loss 平仓盈亏
    offset_daily_gl = DoubleField()  # daily offset gain and loss 平仓盈亏
    offset_acc_gl = DoubleField()  # accumulate offset gain and loss 平仓盈亏
    update_dt = DateTimeField()

    class Meta:
        database = database
        legacy_table_names = False
        primary_key = CompositeKey('user_name', 'broker_id', 'tradeid', 'strategy_name', 'symbol')

    @staticmethod
    def query_position_status_list_until(trade_date) -> list:
        user_name, broker_id = get_account()
        sql_str = """select symbols, strategy_class_name, pos.* 
            from position_status_model pos 
            inner join (
                select pos.strategy_name, pos.symbol, max(pos.tradeid) tradeid, latest_dt.trade_dt latest_trade_dt
                from position_status_model pos 
                inner join (
                    select strategy_name, max(trade_dt) trade_dt 
                    from position_status_model 
                    where user_name=%s and broker_id=%s
                    and trade_date <= %s
                    group by strategy_name, symbol
                ) latest_dt
                on pos.strategy_name = latest_dt.strategy_name
                and pos.trade_dt = latest_dt.trade_dt
                group by pos.strategy_name, pos.symbol, latest_dt.trade_dt
            ) latest
            on pos.strategy_name = latest.strategy_name
            and pos.trade_dt = latest.latest_trade_dt
            and pos.tradeid = latest.tradeid
            -- left join strategy_backtest_stats_view stats
            inner join strategy_backtest_stats_view stats
            on stats.short_name = pos.strategy_name
            where user_name=%s and broker_id=%s"""

        try:
            position_status_list = [
                _ for _ in PositionStatusModel.raw(
                    sql_str, user_name, broker_id, date_2_str(trade_date), user_name, broker_id
                ).execute()]
        finally:
            PositionStatusModel._meta.database.close()

        return position_status_list

    @staticmethod
    def query_latest_position_status() -> typing.Dict[str, dict]:
        """
        获取各个策略最近的一笔开仓交易单
        """
        user_name, broker_id = get_account()
        sql_str = """select pos.* from position_status_model pos inner join (
            select strategy_name, max(trade_dt) trade_dt from position_status_model 
            where user_name=%s and broker_id=%s
            group by strategy_name, symbol) latest
            on pos.strategy_name = latest.strategy_name
            and pos.trade_dt = latest.trade_dt
            where user_name=%s and broker_id=%s"""
        strategy_symbol_pos_status_dic = defaultdict(dict)
        try:
            for pos_status in PositionStatusModel.raw(
                    sql_str, user_name, broker_id, user_name, broker_id).execute():
                strategy_symbol_pos_status_dic[pos_status.strategy_name][pos_status.symbol] = pos_status
        finally:
            PositionStatusModel._meta.database.close()

        return strategy_symbol_pos_status_dic

    @staticmethod
    def query_strategy_symbol_count_dic(
            from_date, to_date) -> typing.Dict[typing.Tuple[str, str], typing.Tuple[int, int, int]]:
        user_name, broker_id = get_account()
        sql_str = """select strategy_name, symbol, CEIL(count(1)) tot_count, 
                sum(offset_gl>0) win_count, sum(offset_gl<=0) loss_count 
            from position_status_model pos 
            where user_name=%s and broker_id=%s and trade_date between %s and %s
            group by strategy_name, symbol"""
        strategy_symbol_count_dic = {}
        try:
            for strategy_name, symbol, tot_count, win_count, loss_count in database.execute_sql(
                    sql_str, params=[user_name, broker_id, from_date, to_date]):
                strategy_symbol_count_dic[(strategy_name, symbol)] = (tot_count, int(win_count), int(loss_count))
        finally:
            PositionStatusModel._meta.database.close()

        return strategy_symbol_count_dic

    @staticmethod
    def bulk_replace(pos_status_new_list: typing.List[dict]):
        user_name, broker_id = get_account()
        try:
            with database.atomic():
                for data_dic in pos_status_new_list:
                    data_dic['user_name'] = user_name
                    data_dic['broker_id'] = broker_id
                    PositionStatusModel.replace(**data_dic).execute()

        finally:
            PositionStatusModel._meta.database.close()


class PositionDailyModel(Model):
    """
    策略持仓信息
    * strategy_name 策略名称
    """
    user_name: str = CharField(max_length=50)
    broker_id: str = CharField(max_length=20)
    strategy_name: str = CharField()
    symbol: str = CharField(max_length=20)
    exchange: str = CharField(max_length=20)
    trade_date = DateField()
    trade_dt = DateTimeField()
    direction: str = CharField(max_length=8)
    avg_price = DoubleField()  # 平均持仓成本
    latest_price = DoubleField()  # 最新价格
    volume = DoubleField()
    holding_gl = DoubleField()  # holding gain and loss 持仓盈亏
    offset_gl = DoubleField()  # offset gain and loss 平仓盈亏
    offset_daily_gl = DoubleField()  # daily offset gain and loss 平仓盈亏
    offset_acc_gl = DoubleField()  # accumulate offset gain and loss 平仓盈亏
    update_dt = DateTimeField()

    class Meta:
        database = database
        legacy_table_names = False
        primary_key = CompositeKey('user_name', 'broker_id', 'strategy_name', 'symbol', 'trade_date')

    @staticmethod
    def bulk_replace(position_daily_list: typing.List[dict]):
        user_name, broker_id = get_account()
        try:
            with database.atomic():
                for data_dic in position_daily_list:
                    data_dic['user_name'] = user_name
                    data_dic['broker_id'] = broker_id
                    PositionDailyModel.replace(**data_dic).execute()

        finally:
            PositionDailyModel._meta.database.close()

    @staticmethod
    def query_latest_position_daily() -> typing.Dict[str, dict]:
        """
        获取各个策略最近的一笔开仓交易单
        """
        user_name, broker_id = get_account()
        sql_str = """select pos.* from position_daily_model pos inner join (
            select strategy_name, max(trade_date) trade_date from position_daily_model 
            where user_name=%s and broker_id=%s
            group by strategy_name, symbol) latest
            on pos.strategy_name = latest.strategy_name
            and pos.trade_date = latest.trade_date
            where user_name=%s and broker_id=%s"""
        strategy_symbol_pos_daily_dic = defaultdict(dict)
        try:
            for pos_status in PositionDailyModel.raw(
                    sql_str, user_name, broker_id, user_name, broker_id).execute():
                strategy_symbol_pos_daily_dic[pos_status.strategy_name][pos_status.symbol] = pos_status
        finally:
            PositionDailyModel._meta.database.close()

        return strategy_symbol_pos_daily_dic


class TradeDateModel(Model):
    """
    策略状态信息
    * strategy_name 策略名称
    * status 策略状态
    """
    trade_date = DateField(primary_key=True)

    class Meta:
        database = database
        legacy_table_names = False
        table_settings = "ENGINE = MYISAM"

    @staticmethod
    def get_latest_trade_date():
        try:
            obj: TradeDateModel = TradeDateModel.select(fn.MAX(TradeDateModel.trade_date)).first()
        finally:
            TradeDateModel._meta.database.close()

        return None if obj.trade_date is None else obj.trade_date

    @staticmethod
    def bulk_replace(data_dic_list: typing.List[dict]):
        try:
            with database.atomic():
                for data_dic in data_dic_list:
                    TradeDateModel.replace(**data_dic).execute()

        finally:
            TradeDateModel._meta.database.close()

    @staticmethod
    @lru_cache()
    def get_trade_date_dic() -> typing.Tuple[typing.Dict[date, date], typing.Dict[date, date]]:
        trade_date_df = pd.read_sql("SELECT * FROM trade_date_model order by trade_date", database)
        trade_date_df['trade_date_next'] = trade_date_df['trade_date'].shift(-1)
        trade_date_df['trade_date_last'] = trade_date_df['trade_date'].shift(1)
        next_trade_date_dic = trade_date_df.set_index('trade_date')['trade_date_next'].to_dict()
        last_trade_date_dic = trade_date_df.set_index('trade_date')['trade_date_last'].to_dict()
        return next_trade_date_dic, last_trade_date_dic


def init_models():
    logger.info("开始初始化数据库表")
    database.connect()
    database.create_tables([
        StrategyStatus, OrderDataModel, TradeDataModel,
        LatestTickPriceModel, PositionStatusModel, PositionDailyModel,
        TradeDateModel,
        StrategyInfo, SymbolsInfo, AccountStrategyMapping,
        StrategyBacktestStats, StrategyBacktestStatsArchive,
        FutureAdjFactor
    ])
    # import inspect
    # import peewee
    # models = [
    #     obj for name, obj in inspect.getmembers(
    #         "__main__", lambda obj: type(obj) == type and issubclass(obj, peewee.Model)
    #     )
    # ]
    # peewee.create_model_tables(models)
    logger.info("数据库表建立完成")


def _test_record_strategy_status():
    strategy_name = 'asdf11'
    user_name, broker_id = get_account()
    status = AccountStrategyStatusEnum.Running
    StrategyStatus.register_strategy(
        strategy_name=strategy_name, status=status.value, symbols='rb2101.SHFE',
        strategy_settings={})
    ss: StrategyStatus = StrategyStatus.get_or_none(
        StrategyStatus.user_name == user_name, StrategyStatus.broker_id == broker_id,
        StrategyStatus.strategy_name == strategy_name)
    assert ss.status == status.value
    assert ss.description == ''
    StrategyStatus.set_status(strategy_name=strategy_name, status=status.value)
    ss: StrategyStatus = StrategyStatus.get_or_none(
        StrategyStatus.user_name == user_name, StrategyStatus.broker_id == broker_id,
        StrategyStatus.strategy_name == strategy_name)
    ss.status = AccountStrategyStatusEnum.Stopped.value
    ss.update()
    ss._meta.database.close()


def _test_apply_2_symbol():
    obj = StrategyBacktestStats.get(
        StrategyBacktestStats.stg_info_id == 4,
        StrategyBacktestStats.symbols_info_id == 1,
        StrategyBacktestStats.short_name.is_null(False)
    )
    new_obj = obj.apply_2_symbol()


def _test_add_mapping_all():
    StrategyBacktestStats.add_mapping_all()


if __name__ == "__main__":
    # init_models()
    # _test_record_strategy_status()
    # _test_apply_2_symbol()
    # _test_add_mapping_all()
    _test_expire_stats()
