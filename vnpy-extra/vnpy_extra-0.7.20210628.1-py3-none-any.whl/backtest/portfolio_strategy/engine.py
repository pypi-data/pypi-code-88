#! /usr/bin/env python3
"""
@author  : MG
@Time    : 2020/10/27 16:11
@File    : engine.py
@contact : mmmaaaggg@163.com
@desc    : 在 vnpy.app.portfolio_strategy.backtesting.BacktestingEngine 基础上继续拿修改
"""
import os
from collections import OrderedDict, defaultdict
from datetime import datetime, date
from multiprocessing import Lock
from typing import List, Dict, Union, Tuple, Optional

# noinspection PyUnresolvedReferences
import ffn  # NOQA
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
import talib
from ibats_utils.mess import date_2_str, dict_2_jsonable
from pandas import DataFrame
from plotly.basedatatypes import BaseTraceType
from plotly.subplots import make_subplots
from sklearn.linear_model import LinearRegression  # 线性回归
from vnpy.app.portfolio_strategy.backtesting import BacktestingEngine as BacktestingEngineBase, \
    PortfolioDailyResult as PortfolioDailyResultBase
from vnpy.trader.constant import Direction, Status, Interval, Offset
from vnpy.trader.object import TradeData, BarData

from vnpy_extra.backtest import CrossLimitMethod
from vnpy_extra.config import logging
from vnpy_extra.constants import SYMBOL_SIZE_DIC
from vnpy_extra.db.orm import TradeDataModel, TradeDateModel
from vnpy_extra.utils.enhancement import get_instrument_type

plt.switch_backend('Agg')


class PortfolioDailyResult(PortfolioDailyResultBase):

    def add_trade(self, trade: TradeData) -> None:
        """"""
        contract_result = self.contract_results[trade.vt_symbol.upper()]
        contract_result.add_trade(trade)


class BacktestingEngine(BacktestingEngineBase):

    def __init__(self):
        super().__init__()
        self.cross_limit_method: CrossLimitMethod = CrossLimitMethod.open_price
        self.logger = logging.getLogger(self.__class__.__name__)

    def calculate_result(self) -> None:
        """"""
        self.output("开始计算逐日盯市盈亏")

        if not self.trades:
            self.output("成交记录为空，无法计算")
            return

        # Add trade data into daily reuslt.
        for trade in self.trades.values():
            d = trade.datetime.date()
            daily_result = self.daily_results[d]
            daily_result.add_trade(trade)

        # Calculate daily result by iteration.
        pre_closes = {}
        start_poses = {}

        for daily_result in self.daily_results.values():
            daily_result.calculate_pnl(
                pre_closes,
                start_poses,
                self.sizes,
                self.rates,
                self.slippages,
            )

            pre_closes = daily_result.close_prices
            start_poses = daily_result.end_poses

        # Generate dataframe
        results = defaultdict(list)
        results["trades"] = []

        for daily_result in self.daily_results.values():
            fields = [
                "date", "trade_count", "turnover",
                "commission", "slippage", "trading_pnl",
                "holding_pnl", "total_pnl", "net_pnl"
            ]
            for key in fields:
                value = getattr(daily_result, key)
                results[key].append(value)

            temp_dic = {}
            for key, value in daily_result.contract_results.items():
                temp_dic[key] = value.trades
            results["trades"].append(temp_dic)

        self.daily_df = DataFrame.from_dict(results).set_index("date")

        self.output("逐日盯市盈亏计算完成")
        return self.daily_df

    def set_parameters(
            self,
            vt_symbols: List[str],
            interval: Interval,
            start: datetime,
            rates: Dict[str, float],
            slippages: Dict[str, float],
            sizes: Dict[str, float],
            priceticks: Dict[str, float],
            capital: int = 0,
            end: datetime = None,
            cross_limit_method: CrossLimitMethod = CrossLimitMethod.open_price
    ) -> None:
        """"""
        self.vt_symbols = [_.upper() for _ in vt_symbols]
        self.interval = interval

        self.rates = {k.upper(): v for k, v in rates.items()}
        self.slippages = {k.upper(): v for k, v in slippages.items()}
        self.sizes = {k.upper(): v for k, v in sizes.items()}
        self.priceticks = {k.upper(): v for k, v in priceticks.items()}

        self.start = start
        self.end = end
        self.capital = capital
        self.cross_limit_method = cross_limit_method
        if cross_limit_method not in CrossLimitMethod:
            raise ValueError(f"cross_limit_method={self.cross_limit_method} 无效")

    def cross_limit_order(self) -> None:
        """
        Cross limit order with last bar/tick data.
        """
        for order in list(self.active_limit_orders.values()):
            bar = self.bars[order.vt_symbol]

            long_cross_price = bar.low_price
            short_cross_price = bar.high_price
            if self.cross_limit_method == CrossLimitMethod.open_price:
                long_best_price = bar.open_price
                short_best_price = bar.open_price
            elif self.cross_limit_method == CrossLimitMethod.mid_price:
                long_best_price = (bar.open_price + bar.high_price + bar.low_price + bar.close_price) / 4
                short_best_price = (bar.open_price + bar.high_price + bar.low_price + bar.close_price) / 4
            elif self.cross_limit_method == CrossLimitMethod.worst_price:
                long_best_price = (bar.open_price * 4 + bar.high_price * 3 + bar.low_price * 2 + bar.close_price) / 10
                short_best_price = (bar.open_price * 4 + bar.high_price * 2 + bar.low_price * 3 + bar.close_price) / 10
            else:
                raise ValueError(f"cross_limit_method={self.cross_limit_method} 无效")

            # Push order update with status "not traded" (pending).
            if order.status == Status.SUBMITTING:
                order.status = Status.NOTTRADED
                self.strategy.update_order(order)

            # Check whether limit orders can be filled.
            long_cross = (
                    order.direction == Direction.LONG
                    and order.price >= long_cross_price > 0
            )

            short_cross = (
                    order.direction == Direction.SHORT
                    and order.price <= short_cross_price
                    and short_cross_price > 0
            )

            if not long_cross and not short_cross:
                continue

            # Push order update with status "all traded" (filled).
            order.traded = order.volume
            order.status = Status.ALLTRADED
            self.strategy.update_order(order)

            self.active_limit_orders.pop(order.vt_orderid)

            # Push trade update
            self.trade_count += 1

            if long_cross:
                trade_price = min(order.price, long_best_price)
            else:
                trade_price = max(order.price, short_best_price)

            trade = TradeData(
                symbol=order.symbol,
                exchange=order.exchange,
                orderid=order.orderid,
                tradeid=str(self.trade_count),
                direction=order.direction,
                offset=order.offset,
                price=trade_price,
                volume=order.volume,
                datetime=self.datetime,
                gateway_name=self.gateway_name,
            )

            self.strategy.update_trade(trade)
            self.trades[trade.vt_tradeid] = trade

    def update_daily_close(self, bars: Dict[str, BarData], dt: datetime) -> None:
        """"""
        d = dt.date()

        close_prices = {}
        for bar in bars.values():
            # 2021-02-06 bar.vt_symbol.upper() 行情数据中 vt_symbol 与 CTP接口中 vt_symbol 可能存在大小写不一致情况，
            # 导致后续计算出现KeyError，这里统一使用大写
            close_prices[bar.vt_symbol.upper()] = bar.close_price

        daily_result = self.daily_results.get(d, None)

        if daily_result:
            daily_result.update_close_prices(close_prices)
        else:
            self.daily_results[d] = PortfolioDailyResult(d, close_prices)

    def clear_data(self):
        super().clear_data()
        self.daily_df = None

    def calculate_by_trade(self, df: DataFrame = None):
        """
        按每笔交易计算指标（建仓后平仓为一次交易）
        :return {'indicator1':'value'}:返回指标dict
        """
        # 从df中获取trade_data，加入一个list中
        trades_dict_list_s = df["trades"]
        trade_data_list_dic: Dict[str, List[TradeDataModel]] = {key: [] for key in self.vt_symbols}
        for trades_dict in trades_dict_list_s:
            for key, value in trades_dict.items():
                trade_data_list_dic[key].extend(value)

        next_trade_date_dic, last_trade_date_dic = TradeDateModel.get_trade_date_dic()

        def create_empty_pos_status_dic():
            return dict(
                tradeid='',
                strategy_name=self.strategy.strategy_name,
                symbol='',
                exchange='',
                volume=0,
                avg_price=0,
                holding_pnl=0,
                offset_pnl=0,
                offset_daily_pnl=0,
                offset_acc_pnl=0,
                update_dt=datetime.now(),
            )

        def create_pos_status_dic_by_trade_data(data: TradeDataModel):
            return dict(
                tradeid=data.tradeid,
                strategy_name=self.strategy.strategy_name,
                symbol=data.symbol,
                exchange=data.exchange,
                trade_date=data.datetime.date(),
                trade_dt=data.datetime,
                direction=data.direction,
                avg_price=data.price,  # 平均持仓成本
                latest_price=data.price,  # 最新价格
                volume=0,  # 持仓量
                holding_pnl=0,  # holding profit and loss 持仓盈亏
                offset_pnl=0,  # offset profit and loss 平仓盈亏
                offset_daily_pnl=0,  # daily offset profit and loss 当日平仓盈亏
                offset_acc_pnl=0,  # accumulate offset profit and loss 累计平仓盈亏
                update_dt=datetime.now(),
            )

        result = {}

        for symbol in self.vt_symbols:
            instrument_type = get_instrument_type(symbol).upper()
            multiplier = SYMBOL_SIZE_DIC.setdefault(instrument_type, 10)

            offset_acc_pnl = 0
            pos_status_dict = create_empty_pos_status_dic()
            pos_status_dict['direction'] = trade_data_list_dic[symbol][0].direction.value
            trade_dt_last: Optional[datetime] = None

            pos_status_new_list: List[dict] = []
            holding_trade_data_list: List[TradeDataModel] = []  # 相当于一个先入先出队列，用于处理平仓后的价格信息
            curr_closing_trade_data: Optional[TradeDataModel] = None
            curr_closing_trade_data_vol_left = 0  # 按照先入先出原则，“正在被平仓的那一笔开仓交易记录”中剩余的持仓
            offset_daily_pnl = 0

            offset_pnl_list = []  # 每一笔平仓盈亏的列表
            offset_acc_pnl_list = []  # 当 volume 为0时累计平仓盈亏列表
            offset_acc_pnl_last = 0  # 上一次 volume 为0时的累计盈亏

            holding_start_dt: Optional[datetime.date] = None  # 持仓开始日期
            holding_end_dt: Optional[datetime.date] = None  # 持仓结束日期
            holding_days_list = []  # 持仓天数列表
            holding_profit_days_list = []  # 持仓盈利天数列表
            holding_loss_days_list = []  # 持仓亏损天数列表

            for trade_data in trade_data_list_dic[symbol]:
                if trade_data.volume == 0:
                    # 不明原因，但回测数据中存在部分 trade 开仓数据成交量为 0
                    continue
                # 检查是否到新的一个交易日，如果是，则 offset_daily_pnl 重置为 0
                # TODO: 还需要考虑周五夜盘12点以后的情况，周六凌晨的单子，应该是下周一的交易日。目前交易的品种不存在跨夜。
                #  目前不会出错。但以后需要考虑
                curr_trade_date = next_trade_date_dic[trade_data.datetime.date()] \
                    if trade_data.datetime.hour >= 21 else trade_data.datetime.date()

                if trade_dt_last is None:
                    offset_daily_pnl = 0
                    trade_dt_last = trade_data.datetime
                else:
                    # 计算上一个条交易记录的 交易日
                    trade_date_last = next_trade_date_dic[trade_dt_last.date()] \
                        if trade_dt_last.hour >= 21 else trade_dt_last.date()
                    if trade_date_last != curr_trade_date:
                        offset_daily_pnl = 0
                        trade_dt_last = trade_data.datetime

                if trade_data.offset.value == Offset.OPEN.value:
                    # 开仓，检查方向一致的情况下更数据，方向不一致，warning，同时忽略
                    if pos_status_dict['volume'] != 0 and pos_status_dict['direction'] != trade_data.direction.value:
                        self.logger.error(
                            "交易记录 %s [%s] %s %s %s %.0f 与当前持仓方向不一致，当前记录持仓状态 %s %.0f 剔除历史不一致数据，以最近成交记录为准",
                            self.strategy.strategy_name, trade_data.symbol,
                            trade_data.tradeid, trade_data.direction.value, trade_data.offset.value, trade_data.volume,
                            pos_status_dict['direction'], pos_status_dict['volume'],
                        )
                        pos_status_dict = create_empty_pos_status_dic()

                    volume = pos_status_dict['volume']
                    volume_new = trade_data.volume + volume
                    avg_price = pos_status_dict['avg_price']
                    avg_price_new = (trade_data.price * trade_data.volume + avg_price * volume) / volume_new
                    latest_price = trade_data.price

                    holding_pnl = volume_new * (latest_price - avg_price_new) * multiplier
                    trade_date = trade_data.datetime.date() if trade_data.datetime.hour < 21 else \
                        next_trade_date_dic[trade_data.datetime.date()]

                    # 更新持仓状态信息
                    pos_status_new_dict = dict(
                        tradeid=trade_data.tradeid,
                        strategy_name=self.strategy.strategy_name,
                        symbol=trade_data.symbol,
                        exchange=trade_data.exchange.value,
                        trade_date=trade_date,
                        trade_dt=trade_data.datetime,
                        direction=trade_data.direction.value,
                        avg_price=avg_price_new,
                        latest_price=latest_price,
                        volume=volume_new,
                        holding_pnl=holding_pnl,
                        offset_daily_pnl=offset_daily_pnl,
                        offset_acc_pnl=offset_acc_pnl,
                        update_dt=datetime.now(),
                    )
                    pos_status_new_list.append(pos_status_new_dict)
                    holding_trade_data_list.append(trade_data)

                else:
                    # 平仓，检查持仓是否0，如果是则 warning，同时忽略
                    volume = pos_status_dict["volume"]
                    if volume == 0:
                        self.logger.warning(
                            "交易记录 %s [%s] %s %s %s %.0f 没有对应的持仓数据，无法计算平仓收益，剔除历史数据，当前持仓状态将被重置",
                            self.strategy.strategy_name, trade_data.symbol, trade_data.tradeid,
                            trade_data.direction.value,
                            trade_data.offset.value, trade_data.volume)
                        # 重置持仓状态信息
                        pos_status_new_dict = create_pos_status_dic_by_trade_data(trade_data)
                    elif pos_status_dict['direction'] == trade_data.direction.value:
                        # 平仓，检查方向与持仓是否相反，如果方向一致，warning，同时忽略
                        self.logger.warning(
                            "交易记录 %s [%s] %s %s %s %.0f 与当前持仓方向一致，剔除历史数据，当前持仓状态将被重置",
                            self.strategy.strategy_name, trade_data.symbol,
                            trade_data.tradeid, trade_data.direction.value, trade_data.offset.value, trade_data.volume
                        )
                        # 重置持仓状态信息
                        pos_status_new_dict = create_pos_status_dic_by_trade_data(trade_data)
                    elif volume < trade_data.volume:
                        self.logger.warning(
                            "交易记录 %s [%s] %s %s %s %.0f 超过当前持仓 %.0f 手，剔除历史数据，当前持仓状态将被重置",
                            self.strategy.strategy_name, trade_data.symbol, trade_data.tradeid,
                            trade_data.direction.value,
                            trade_data.offset.value, trade_data.volume, pos_status_dict['volume'])
                        # 重置持仓状态信息
                        pos_status_new_dict = create_pos_status_dic_by_trade_data(trade_data)

                    else:
                        if len(holding_trade_data_list) == 0:
                            # 计算平仓盈亏
                            # 平仓逻辑分为两条线
                            # 1）按照最近一个持仓状态计算仓位及平均价格，当 holding_trade_data_list 为空的情况下(当前分支的逻辑）
                            # 2）按照先入先出队列进行计算仓位及平均价格等
                            close_vol = trade_data.volume
                            curr_closing_trade_data_vol_left = volume - close_vol
                            # trade_data.direction.value 为“多”，说明持仓是“空”，所以，价差 * -1
                            offset_pnl = close_vol * (trade_data.price - pos_status_dict["avg_price"]
                                                      ) * (
                                             -1 if trade_data.direction.value == Direction.LONG.value else 1)
                            # 平均价格不变
                            avg_price_new = pos_status_dict["avg_price"] if curr_closing_trade_data_vol_left != 0 else 0
                        else:
                            # 计算平仓盈亏
                            # 平仓逻辑分为两条线
                            # 1）按照最近一个持仓状态计算仓位及平均价格，当 holding_trade_data_list 为空的情况下
                            # 2）按照先入先出队列进行计算仓位及平均价格等(当前分支的逻辑）
                            offset_pnl = 0
                            # 根据先入先出原则处理检查平仓了多少个历史的交易订单
                            close_vol = trade_data.volume
                            if curr_closing_trade_data_vol_left >= close_vol:
                                curr_closing_trade_data_vol_left -= close_vol
                                offset_pnl += close_vol * (
                                        trade_data.price - curr_closing_trade_data.price
                                ) * (1 if curr_closing_trade_data.direction.value == Direction.LONG.value else -1)
                            else:
                                if curr_closing_trade_data_vol_left > 0:
                                    offset_pnl += curr_closing_trade_data_vol_left * (
                                            trade_data.price - curr_closing_trade_data.price
                                    ) * (1 if curr_closing_trade_data.direction.value == Direction.LONG.value else -1)
                                    close_vol = trade_data.volume - curr_closing_trade_data_vol_left
                                else:
                                    close_vol = trade_data.volume

                                for i in range(len(holding_trade_data_list)):
                                    # 先入先出，总是从第一个位置去交易数据
                                    curr_closing_trade_data = holding_trade_data_list.pop(0)
                                    curr_closing_trade_data_vol_left = curr_closing_trade_data.volume
                                    if curr_closing_trade_data_vol_left >= close_vol:
                                        offset_pnl += close_vol * (
                                                trade_data.price - curr_closing_trade_data.price
                                        ) * (
                                                          1 if curr_closing_trade_data.direction.value == Direction.LONG.value else -1)
                                        curr_closing_trade_data_vol_left -= close_vol
                                        break
                                    else:
                                        offset_pnl += curr_closing_trade_data_vol_left * (
                                                trade_data.price - curr_closing_trade_data.price
                                        ) * (
                                                          1 if curr_closing_trade_data.direction.value == Direction.LONG.value else -1)
                                        close_vol -= curr_closing_trade_data_vol_left
                                else:
                                    if close_vol > 0:
                                        if curr_closing_trade_data is None:
                                            self.logger.warning(
                                                "交易记录 %s [%s] '%s' %s %s %.0f 当前持仓 %.0f 手，缺少与当前持仓对应的开仓交易记录，"
                                                "计算将以当前持仓的平均价格为准进行计算。如果需要完整计算结果，"
                                                "可以清楚当前策略历史 position_status_model记录，进行重新计算。",
                                                self.strategy.strategy_name, trade_data.symbol,
                                                trade_data.tradeid, trade_data.direction.value, trade_data.offset.value,
                                                trade_data.volume, volume)
                                            offset_pnl += close_vol * (
                                                    trade_data.price - pos_status_dict['avg_price']
                                            ) * (1 if pos_status_dict['direction'] == Direction.LONG.value else -1)
                                        else:
                                            self.logger.warning(
                                                "交易记录 %s [%s] %s %s %s %.0f 当前持仓 %.0f 手，当前持仓全部订单不足以处理当前平仓，"
                                                "这种情况发生，说明当前持仓数据与交易数据的累加数字不一致，请检查数据是否缺失",
                                                self.strategy.strategy_name, trade_data.symbol,
                                                trade_data.tradeid, trade_data.direction.value, trade_data.offset.value,
                                                trade_data.volume, volume)
                                            offset_pnl += close_vol * (
                                                    trade_data.price - curr_closing_trade_data.price
                                            ) * (
                                                              1 if curr_closing_trade_data.direction.value == Direction.LONG.value else -1)

                            # 计算平均价格
                            tot_value = curr_closing_trade_data_vol_left * curr_closing_trade_data.price \
                                if curr_closing_trade_data is not None else 0
                            tot_value += sum([
                                _.price * _.volume for _ in holding_trade_data_list
                            ])
                            tot_vol = curr_closing_trade_data_vol_left + sum(
                                [_.volume for _ in holding_trade_data_list])
                            avg_price_new = (tot_value / tot_vol) if tot_vol != 0 else 0

                        # 平仓盈亏需要 × 乘数
                        offset_pnl *= multiplier
                        offset_daily_pnl += offset_pnl
                        offset_acc_pnl += offset_pnl

                        offset_pnl_list.append(offset_pnl)

                        # 计算持仓盈亏
                        latest_price = trade_data.price
                        volume = curr_closing_trade_data_vol_left + sum(
                            [_.volume for _ in holding_trade_data_list])
                        holding_pnl = curr_closing_trade_data_vol_left * (latest_price - avg_price_new) * multiplier * (
                            1 if pos_status_dict['direction'] == Direction.LONG.value else -1)

                        trade_date = trade_data.datetime.date() if trade_data.datetime.hour < 21 else \
                            next_trade_date_dic[trade_data.datetime.date()]

                        # 持仓方向
                        if trade_data.offset.value == Offset.OPEN:
                            direction = trade_data.direction.value
                        else:
                            direction = Direction.SHORT.value if trade_data.direction.value == Direction.LONG.value else Direction.LONG.value
                        # 更新持仓状态信息
                        pos_status_new_dict = dict(
                            tradeid=trade_data.tradeid,
                            strategy_name=self.strategy.strategy_name,
                            symbol=trade_data.symbol,
                            exchange=trade_data.exchange.value,
                            trade_date=trade_date,
                            trade_dt=trade_data.datetime,
                            direction=direction,
                            avg_price=avg_price_new,
                            latest_price=latest_price,
                            volume=volume,
                            holding_pnl=holding_pnl,
                            offset_pnl=offset_pnl,
                            offset_daily_pnl=offset_daily_pnl,
                            offset_acc_pnl=offset_acc_pnl,
                            update_dt=datetime.now(),
                        )

                    # 新的状态信息加入的列表
                    pos_status_new_list.append(pos_status_new_dict)

                # 更新最新的持仓状态
                pos_status_dict = pos_status_new_dict

                # 计算持仓时间
                if holding_start_dt is None and pos_status_dict['volume'] > 0:
                    holding_start_dt = pos_status_dict['trade_dt']
                if holding_start_dt is not None and pos_status_dict['volume'] == 0:
                    holding_end_dt = pos_status_dict['trade_dt']
                    holding_days_seconds = (holding_end_dt - holding_start_dt).total_seconds()
                    holding_days_list.append(holding_days_seconds)

                    # 初始化日期
                    holding_start_dt = None
                    holding_end_dt = None

                    # offset_acc_pnl_list.append(offset_acc_pnl)

                    # 判断持仓盈亏
                    if (offset_acc_pnl - offset_acc_pnl_last) > 0:
                        holding_profit_days_list.append(holding_days_seconds)
                        offset_acc_pnl_list.append(offset_acc_pnl - offset_acc_pnl_last)
                    elif (offset_acc_pnl - offset_acc_pnl_last) < 0:
                        holding_loss_days_list.append(holding_days_seconds)
                        offset_acc_pnl_list.append(offset_acc_pnl - offset_acc_pnl_last)

                    offset_acc_pnl_last = offset_acc_pnl

            offset_acc_pnl_s = pd.Series(offset_acc_pnl_list)
            # 平仓累计盈利/亏损
            offset_acc_profit = offset_acc_pnl_s[offset_acc_pnl_s > 0].sum()
            offset_acc_loss = offset_acc_pnl_s[offset_acc_pnl_s < 0].sum()
            # 总盈利 / 总亏损 （累计盈利亏损比）
            acc_profit_loss_ratio = np.nan if offset_acc_loss == 0 else abs(offset_acc_profit / offset_acc_loss)

            # 平均盈利 / 平均亏损
            win_len = len(offset_acc_pnl_s[offset_acc_pnl_s > 0])
            average_profit = np.nan if win_len == 0 else (offset_acc_profit / win_len)
            loss_len = len(offset_acc_pnl_s[offset_acc_pnl_s < 0])
            average_loss = np.nan if loss_len == 0 else (offset_acc_loss / loss_len)
            average_profit_loss_ratio = np.nan if np.isnan(average_loss) or average_loss == 0 else (
                abs(average_profit / average_loss))

            # 平均持仓天数
            holding_days_s = pd.Series(holding_days_list)
            average_holding_days = holding_days_s.mean() / 3600 / 24
            # 最长持仓天数
            max_holding_days = holding_days_s.max() / 3600 / 24
            # 平均盈利持仓时间
            holding_profit_days_s = pd.Series(holding_profit_days_list)
            average_holding_profit_days = holding_profit_days_s.mean() / 3600 / 24
            # 平均亏损持仓时间
            holding_loss_days_s = pd.Series(holding_loss_days_list)
            average_holding_loss_days = holding_loss_days_s.mean() / 3600 / 24

            result[symbol] = {
                "offset_acc_profit": offset_acc_profit,
                "offset_acc_loss": offset_acc_loss,
                "acc_profit_loss_ratio": acc_profit_loss_ratio,
                "average_profit": average_profit,
                "average_loss": average_loss,
                "average_profit_loss_ratio": average_profit_loss_ratio,
                "average_holding_days": average_holding_days,
                "max_holding_days": max_holding_days,
                "average_holding_profit_days": average_holding_profit_days,
                "average_holding_loss_days": average_holding_loss_days
            }

        return result

    def calculate_statistics(self, df: DataFrame = None, output=True) -> dict:
        """"""
        self.output("开始计算策略统计指标")

        # Check DataFrame input exterior
        if df is None:
            df = self.daily_df

        # stat daily
        # Check for init DataFrame
        if df is None:
            # Set all statistics to 0 if no trade.
            start_date = ""
            end_date = ""
            total_days = 0
            profit_days = 0
            loss_days = 0
            end_balance = 0
            max_drawdown = 0
            avg_drawdown = 0
            most_drawdown = 0
            lw_drawdown = 0
            max_dd_pct = 0
            avg_dd_pct = 0
            most_dd_pct = 0
            lw_dd_pct = 0
            avg_square_dd_pct = 0
            max_drawdown_duration = 0
            max_new_higher_duration = 0
            total_net_pnl = 0
            daily_net_pnl = 0
            total_commission = 0
            daily_commission = 0
            total_slippage = 0
            daily_slippage = 0
            total_turnover = 0
            daily_turnover = 0
            total_trade_count = 0
            daily_trade_count = 0
            total_return = 0
            annual_return = 0
            daily_return = 0
            return_std = 0
            sharpe_ratio = 0
            info_ratio = 0
            return_drawdown_ratio = 0
            return_most_drawdown_ratio = 0
            sortino_ratio = 0
            win_ratio = 0
            return_loss_ratio = 0
            return_risk_ratio = 0
            max_drawdown_end = None
            standard_deviation_ratio = 0
            kelly_index = 0
        else:
            # Calculate balance related time series data
            net_pnl_s = df["net_pnl"]
            df["balance"] = net_pnl_s.cumsum() + self.capital
            rr = df["balance"] / df["balance"].iloc[0]
            rr.index = pd.to_datetime(rr.index)
            stats = rr.calc_stats()

            df["return"] = np.log(df["balance"] / df["balance"].shift(1)).fillna(0)
            df["highlevel"] = (
                df["balance"].rolling(
                    min_periods=1, window=len(df), center=False).max()
            )
            df["drawdown"] = df["balance"] - df["highlevel"]
            df["ddpercent"] = df["drawdown"] / df["highlevel"] * 100

            # Calculate statistics value
            start_date = df.index[0]
            end_date = df.index[-1]

            total_days = len(df)
            profit_days = len(df[net_pnl_s > 0])
            loss_days = len(df[net_pnl_s < 0])

            end_balance = df["balance"].iloc[-1]
            # 回撤
            drawdown_s = df["drawdown"]
            max_drawdown = drawdown_s.min()
            max_drawdown_end = drawdown_s.idxmin()
            drawdown_net_s = drawdown_s[drawdown_s < 0]
            avg_drawdown = drawdown_net_s.mean()
            std_drawdown = drawdown_net_s.std()
            # 取极值回撤
            most_drawdown = avg_drawdown - std_drawdown * 2
            # 线性加权回撤
            lw_drawdown = talib.LINEARREG(-drawdown_s, drawdown_s.count())[-1]
            # 回撤率
            dd_pct_s = df["ddpercent"]
            dd_pct_net_s: pd.Series = dd_pct_s[dd_pct_s < 0]
            avg_dd_pct = dd_pct_net_s.mean()
            std_dd_pct = dd_pct_net_s.std()
            max_dd_pct = dd_pct_s.min()
            # 取极值回撤率
            most_dd_pct = avg_dd_pct - std_dd_pct * 2
            # 线性加权回撤率
            lw_dd_pct = talib.LINEARREG(-dd_pct_s, dd_pct_s.count())[-1]
            avg_square_dd_pct = (dd_pct_net_s ** 2).mean()

            if isinstance(max_drawdown_end, date):
                max_drawdown_start = df["balance"][:max_drawdown_end].idxmax()
                max_drawdown_duration = (max_drawdown_end - max_drawdown_start).days
            else:
                max_drawdown_duration = 0

            highlevel = df["highlevel"]
            max_new_higher_duration = highlevel.groupby(by=highlevel).count().max()

            total_net_pnl = net_pnl_s.sum()
            daily_net_pnl = total_net_pnl / total_days

            total_commission = df["commission"].sum()
            daily_commission = total_commission / total_days

            total_slippage = df["slippage"].sum()
            daily_slippage = total_slippage / total_days

            total_turnover = df["turnover"].sum()
            daily_turnover = total_turnover / total_days

            total_trade_count = df["trade_count"].sum()
            daily_trade_count = np.round(total_trade_count / total_days, 2)

            total_return = (end_balance / self.capital - 1) * 100
            annual_return = np.round(stats.cagr * 100, 2)  # total_return / total_days * 240
            daily_return = df["return"].mean() * 100
            return_std = df["return"].std() * 100

            if return_std:
                sharpe_ratio = np.round(stats.daily_sharpe, 2)  # daily_return / return_std * np.sqrt(240)
                sortino_ratio = np.round(stats.daily_sortino, 2)
            else:
                sharpe_ratio = 0
                sortino_ratio = 0

            # 计算 info ratio
            # 1. 计算资金曲线收益率
            rr_s = df["balance"] / df["balance"].iloc[0]
            # 2. 计算行情收益率
            # 记录 leg2的乘数
            if hasattr(self.strategy, "leg_fractions"):
                leg_fractions = getattr(self.strategy, "leg_fractions")
            else:
                leg_fractions = 1

            # build vt_symbols_close_df
            data_list = []
            index = []
            for d, result in self.daily_results.items():
                row_data = [result.close_prices[_] for _ in self.vt_symbols]
                index.append(d)
                data_list.append(row_data)

            vt_symbols_close_df = DataFrame(data_list, columns=self.vt_symbols, index=index).sort_index()
            if len(self.vt_symbols) == 2:
                # 计算 spread
                info_s = vt_symbols_close_df.iloc[:, 0] - vt_symbols_close_df.iloc[:, 1] * leg_fractions
            else:
                info_s = (vt_symbols_close_df.pct_change().sum(axis=1) + 1).cumprod()

            rr_info_s = info_s / info_s.iloc[0]
            rr_info_mdd_s = rr_info_s.calc_max_drawdown()
            if rr_info_mdd_s != 0:
                rr_info_s = rr_info_s * rr_s.calc_max_drawdown() / rr_info_s.calc_max_drawdown()
                info_ratio = np.round(rr_s.calc_information_ratio(rr_info_s), 2)
            else:
                info_ratio = 0

            win_ratio = profit_days / (profit_days + loss_days)
            abs_loss_pnl = abs(net_pnl_s[net_pnl_s < 0].sum())
            return_loss_ratio = np.round(net_pnl_s[net_pnl_s > 0].sum() / abs_loss_pnl, 2) \
                if abs_loss_pnl != 0 else np.nan
            # 卡玛比
            return_drawdown_ratio = np.round(stats.calmar, 2)  # 此处vnpy，原始函数计算有错误
            # 年化收益率 / most_dd_pct 该数值将会比 calmar 略高，但更具有普遍意义
            return_most_drawdown_ratio = np.round(-annual_return / most_dd_pct, 2)
            return_risk_ratio = np.nan if np.isnan(return_loss_ratio) or return_loss_ratio == 0 else \
                np.round(win_ratio - (1 - win_ratio) / return_loss_ratio, 4)

            # 标准离差率
            standard_deviation = df["balance"].var() ** 0.5
            standard_deviation_ratio = standard_deviation / df["balance"].mean()

            # 凯利指数
            kelly_index = return_risk_ratio

        # stat by trade
        # TODO 按照每笔交易计算，最终结果跟每天的有较大差距
        if df is None:
            indicator_by_trade_dic = {}

            for symbol in self.vt_symbols:
                indicator_by_trade_dic[symbol] = {
                    "offset_acc_profit": 0,
                    "offset_acc_loss": 0,
                    "acc_profit_loss_ratio": 0,
                    "average_profit": 0,
                    "average_loss": 0,
                    "average_profit_loss_ratio": 0,
                    "average_holding_days": 0,
                    "max_holding_days": 0,
                    "average_holding_profit_days": 0,
                    "average_holding_loss_days": 0
                }
        else:
            indicator_by_trade_dic = self.calculate_by_trade(df)

        statistics = OrderedDict([
            ("start_date", start_date),
            ("end_date", end_date),
            ("total_days", total_days),
            ("profit_days", profit_days),
            ("loss_days", loss_days),
            ("capital", self.capital),
            ("end_balance", end_balance),
            ("max_drawdown", max_drawdown),
            ("avg_drawdown", avg_drawdown),
            ("most_drawdown", most_drawdown),
            ("lw_drawdown", lw_drawdown),
            ("max_dd_pct", max_dd_pct),
            ("avg_dd_pct", avg_dd_pct),
            ("most_dd_pct", most_dd_pct),
            ("lw_dd_pct", lw_dd_pct),
            ("avg_square_dd_pct", avg_square_dd_pct),
            ("max_drawdown_duration", max_drawdown_duration),
            ("max_new_higher_duration", max_new_higher_duration),
            ("total_net_pnl", total_net_pnl),
            ("daily_net_pnl", daily_net_pnl),
            ("total_commission", total_commission),
            ("daily_commission", daily_commission),
            ("total_slippage", total_slippage),
            ("daily_slippage", daily_slippage),
            ("total_turnover", total_turnover),
            ("daily_turnover", daily_turnover),
            ("total_trade_count", total_trade_count),
            ("daily_trade_count", daily_trade_count),
            ("total_return", total_return),
            ("annual_return", annual_return),
            ("daily_return", daily_return),
            ("return_std", return_std),
            ("sortino_ratio", sortino_ratio),
            ("info_ratio", info_ratio),
            ("win_ratio", win_ratio),
            ("return_loss_ratio", return_loss_ratio),
            ("return_drawdown_ratio", return_drawdown_ratio),
            ("return_most_drawdown_ratio", return_most_drawdown_ratio),
            ("return_risk_ratio", return_risk_ratio),
            # ("available", not is_unavailable),
        ])

        if df is None:
            is_available = False
            score = 0
        else:
            # 计算有效性
            if hasattr(self.strategy, 'is_available'):
                is_available = self.strategy.is_available(statistics, df)
            else:
                is_available = not (
                        total_return <= 0
                        or daily_trade_count < 0.2  # 1/0.2 每一次交易平仓再开仓需要2次交易，因此相当于10天交易一次
                        or return_drawdown_ratio < 1.5
                        or max_new_higher_duration >= 180  # 最长不创新高周期<180
                        or max_new_higher_duration / total_days > 0.5  # 最长不创新高周期超过一半的总回测天数
                        or df is None  # 没有交易
                        or np.sum((df["balance"] - self.capital) <= 0) / total_days > 0.5  # 50%以上交易日处于亏损状态
                        # 最大回撤到最后一个交易日需要出现新高
                        or (np.all(df["drawdown"][max_drawdown_end:] < 0) if max_drawdown_end is not None else False)
                )

            # 计算综合打分成绩
            if hasattr(self.strategy, 'calc_score'):
                score = self.strategy.calc_score(statistics, df)
            else:
                # 线性收益 与 实际收益曲线之间的 std
                rr_s = df["balance"] / self.capital
                # 以最终收益率为终点
                # benchmark = np.linspace(rr_s.iloc[0], rr_s.iloc[-1], rr_s.shape[0])
                # 一元线性回归
                x = np.array(range(rr_s.shape[0])).reshape((-1, 1))
                model = LinearRegression(copy_X=False, n_jobs=-1)  # normalize=False
                model.fit(x, rr_s)
                # 比较直线与实际曲线的差距
                benchmark = model.predict(x)
                score = np.std(benchmark - rr_s) * (100 if rr_s.iloc[-1] > 1 else -100)

        statistics['score'] = score
        statistics['available'] = is_available

        indicator_dic = {
            "daily_stats_dic": {
                "start_date": str(start_date),
                "end_date": str(end_date),
                "total_days": total_days,
                "profit_days": profit_days,
                "loss_days": loss_days,
                "capital": self.capital,
                "end_balance": end_balance,
                "max_drawdown": max_drawdown,
                "avg_drawdown": avg_drawdown,
                "most_drawdown": most_drawdown,
                "lw_drawdown": lw_drawdown,
                "max_dd_pct": max_dd_pct,
                "avg_dd_pct": avg_dd_pct,
                "most_dd_pct": most_dd_pct,
                "lw_dd_pct": lw_dd_pct,
                "avg_square_dd_pct": avg_square_dd_pct,
                "max_drawdown_duration": max_drawdown_duration,
                "max_new_higher_duration": max_new_higher_duration,
                "total_net_pnl": total_net_pnl,
                "daily_net_pnl": daily_net_pnl,
                "total_commission": total_commission,
                "daily_commission": daily_commission,
                "total_slippage": total_slippage,
                "daily_slippage": daily_slippage,
                "total_turnover": total_turnover,
                "daily_turnover": daily_turnover,
                "total_trade_count": total_trade_count,
                "daily_trade_count": daily_trade_count,
                "total_return": total_return,
                "annual_return": annual_return,
                "daily_return": daily_return,
                "return_std": return_std,
                "sortino_ratio": sortino_ratio,
                "info_ratio": info_ratio,
                "win_ratio": win_ratio,
                "return_loss_ratio": return_loss_ratio,
                "return_drawdown_ratio": return_drawdown_ratio,
                "return_most_drawdown_ratio": return_most_drawdown_ratio,
                "return_risk_ratio": return_risk_ratio,
                "standard_deviation_ratio": standard_deviation_ratio,
                "kelly_index": kelly_index,
                "score": score,
                "available": is_available
            },
            "trade_stats_dic": indicator_by_trade_dic,
        }

        statistics['indicator_dic'] = indicator_dic
        statistics = dict_2_jsonable(statistics)

        # Output
        if output:
            self.output("-" * 30)
            self.output("|      指标    |     数值      |")
            self.output("|:-----------|------------:|")
            self.output(f"|首个交易日| \t{start_date}|")
            self.output(f"|最后交易日| \t{end_date}|")

            self.output(f"|总交易日| \t{total_days}|")
            self.output(f"|盈利交易日| \t{profit_days}|")
            self.output(f"|亏损交易日| \t{loss_days}|")

            self.output(f"|起始资金| \t{self.capital:,.2f}|")
            self.output(f"|结束资金| \t{end_balance:,.2f}|")

            self.output(f"|总收益率| \t{total_return:,.2f}%")
            self.output(f"|年化收益| \t{annual_return:,.2f}%")
            self.output(f"|最大回撤| \t{max_drawdown:,.2f}|")
            self.output(f"|百分比最大回撤| {max_dd_pct:,.2f}%")
            self.output(f"|最长回撤天数| \t{max_drawdown_duration}|")
            self.output(f"|最长再创新高周期| \t{max_new_higher_duration}|")

            self.output(f"|总盈亏| \t{total_net_pnl:,.2f}|")
            self.output(f"|总手续费| \t{total_commission:,.2f}|")
            self.output(f"|总滑点| \t{total_slippage:,.2f}|")
            self.output(f"|总成交金额| \t{total_turnover:,.2f}|")
            self.output(f"|总成交笔数| \t{total_trade_count}|")

            self.output(f"|日均盈亏| \t{daily_net_pnl:,.2f}|")
            self.output(f"|日均手续费| \t{daily_commission:,.2f}|")
            self.output(f"|日均滑点| \t{daily_slippage:,.2f}|")
            self.output(f"|日均成交金额| \t{daily_turnover:,.2f}|")
            self.output(f"|日均成交笔数| \t{daily_trade_count:,.3f}|")

            self.output(f"|日均收益率| \t{daily_return:,.2f}%|")
            self.output(f"|收益标准差| \t{return_std:,.2f}%|")
            self.output(f"|Sharpe Ratio| \t{sharpe_ratio:,.2f}|")
            self.output(f"|Info Ratio| \t{info_ratio:,.2f}|")
            self.output(f"|收益回撤比| \t{return_drawdown_ratio:,.2f}|")
            self.output(f"|标准离差率| \t{standard_deviation_ratio:,.4f}|")
            self.output(f"|凯利指数| \t{kelly_index:,.2f}|")
            self.output(f"|综合打分| \t{score:,.4f}|")

            self.output(f"|available| \t{is_available}|")

        # Filter potential error infinite value
        for key, value in statistics.items():
            if value in (np.inf, -np.inf):
                value = 0
            statistics[key] = np.nan_to_num(value)

        self.output("策略统计指标计算完成")
        return statistics

    def show_chart(self, df: DataFrame = None,
                   image_file_name=None, open_browser_4_charts=True,
                   show_indexes=None,
                   lock: Lock = None,
                   ) -> Dict[str, Dict[str, list]]:
        """"""
        charts_data = defaultdict(dict)
        # Check DataFrame input exterior
        if df is None:
            df = self.daily_df

        # Check for init DataFrame
        if df is None:
            return charts_data

        trace_type = Union[BaseTraceType, Tuple[BaseTraceType, bool]]
        title_traces_dic: Dict[str, Union[List[trace_type], trace_type]] = OrderedDict()
        title_traces_dic["Daily Price"] = []
        # build vt_symbols_close_df
        data_list = []
        index = []
        for d, result in self.daily_results.items():
            row_data = [result.close_prices[_] for _ in self.vt_symbols]
            index.append(d)
            data_list.append(row_data)

        columns = ['trade_date']
        columns.extend(self.vt_symbols)
        vt_symbols_close_df = DataFrame(data_list, columns=self.vt_symbols, index=index).sort_index()
        _data: List[List] = vt_symbols_close_df.reset_index().to_numpy().tolist()
        for row_data in _data:
            row_data[0] = date_2_str(row_data[0])

        charts_data["Daily Price"] = dict(
            title=columns,
            data=_data,
        )
        for vt_symbol in self.vt_symbols:
            close_line = go.Scatter(
                x=vt_symbols_close_df.index,
                y=vt_symbols_close_df[vt_symbol],
                mode="lines",
                name=vt_symbol
            )
            title_traces_dic["Daily Price"].append(close_line)

        if show_indexes is not None:
            # 目前仅支持 spread
            for index_name in show_indexes:
                if index_name == 'spread':
                    # 记录 leg2的乘数
                    if hasattr(self.strategy, "leg_fractions"):
                        leg_fractions = getattr(self.strategy, "leg_fractions")
                    else:
                        leg_fractions = 1

                    # 计算 spread
                    if len(self.vt_symbols) == 2:
                        # 计算 spread
                        info_s = vt_symbols_close_df.iloc[:, 0] - vt_symbols_close_df.iloc[:, 1] * leg_fractions
                        name = "spread"
                    else:
                        info_s = (vt_symbols_close_df.pct_change().sum(axis=1) + 1).cumprod()
                        name = "index"

                    spread_line = go.Scatter(
                        x=info_s.index,
                        y=info_s,
                        mode="lines",
                        name=name
                    )
                    title_traces_dic[index_name.upper()] = [spread_line]

        profit_s = df["balance"] - self.capital
        profit_line = go.Scatter(
            x=df.index,
            y=profit_s,
            mode="lines",
            name="profit",
            line=dict(color='rgba(255,0,0,1)'),  # ffb3a7
        )
        total_cost_s = (df["commission"] + df["slippage"]).cumsum()
        profit_without_cost_s = profit_s + total_cost_s
        profit_fee0_line = go.Scatter(
            x=df.index,
            y=profit_without_cost_s,
            mode="lines",
            name="profit without cost",
            line=dict(color='rgba(255,179,167,1)', dash='dashdot')  # ffb3a7
        )
        fee_line = go.Scatter(
            x=df.index,
            y=total_cost_s,
            mode="lines",
            name="total cost",
            line=dict(color='rgba(117,138,153,1)', dash='dashdot')  # 758a99
        )
        title_traces_dic["Daily Price"].extend([(fee_line, True), (profit_fee0_line, True), (profit_line, True)])
        # title_traces_dic["profit vs total cost"] = [fee_line, profit_fee0_line, profit_line]
        charts_data["profit vs total cost"] = dict(
            title=['trade_date', 'profit', "profit without cost", "total cost"],
            data=[[date_2_str(_[0]), _[1], _[2], _[3]] for _ in DataFrame(
                [profit_s, profit_without_cost_s, total_cost_s]).T.reset_index().to_numpy().tolist()],
        )

        drawdown_scatter = go.Scatter(
            x=df.index,
            y=df["drawdown"],
            fillcolor="red",
            fill='tozeroy',
            mode="lines",
            name="Drawdown"
        )
        title_traces_dic["Drawdown"] = [drawdown_scatter]
        charts_data["Drawdown"] = dict(
            title=['trade_date', 'drawdown'],
            data=[[date_2_str(_[0]), _[1]] for _ in df["drawdown"].reset_index().to_numpy().tolist()],
        )
        pnl_bar = go.Bar(y=df["net_pnl"], name="Daily Pnl")
        title_traces_dic["Daily Pnl"] = [pnl_bar]
        charts_data["Daily Pnl"] = dict(
            title=['trade_date', 'net_pnl'],
            data=[[date_2_str(_[0]), _[1]] for _ in df["net_pnl"].reset_index().to_numpy().tolist()],
        )
        bins = 100
        pnl_histogram = go.Histogram(x=df["net_pnl"], nbinsx=bins, name="Days")
        title_traces_dic["Pnl Distribution"] = [pnl_histogram]
        nums, bins_v, _ = plt.hist(df["net_pnl"], bins=bins)
        charts_data["Pnl Distribution"] = dict(
            title=['net_pnl', 'count'],
            data=[
                [(bins_v[_] + bins_v[_ + 1]) / 2 for _ in range(len(nums))],
                list(nums),
            ],
        )

        # 生成图表
        row_count = len(title_traces_dic)
        specs: List[List[dict]] = [[{}] for _ in range(row_count)]
        specs[0][0] = {
            'type': 'xy',
            'secondary_y': True
        }
        row_heights = [1 for _ in range(row_count)]
        row_heights[0] = 3
        fig = make_subplots(
            rows=row_count,
            cols=1,
            subplot_titles=list(title_traces_dic.keys()),
            vertical_spacing=0.04,
            horizontal_spacing=0.0,
            row_heights=row_heights,
            specs=specs,
        )
        for n, (title, traces) in enumerate(title_traces_dic.items(), start=1):
            for _ in traces:
                if isinstance(_, tuple):
                    trace, secondary_y = _
                else:
                    trace, secondary_y = _, False

                fig.add_trace(trace, secondary_y=secondary_y, row=n, col=1)

        _, file_name = os.path.split(image_file_name)
        file_name, _ = os.path.splitext(file_name)
        fig.update_layout(
            title=file_name,
            height=row_count * 300, width=1600,
        )
        if open_browser_4_charts:
            fig.show()

        if image_file_name is not None:

            if lock is not None:
                lock.acquire()  # 锁住共享变量

            try:
                # 如果组件环境变量这支不成功，可以考虑通过如下方式这是环境路径
                # plotly.io.orca.config.executable = '/path/to/orca'
                pio.write_image(fig, image_file_name)
            except ValueError:
                try:
                    try:
                        from kaleido.scopes.plotly import PlotlyScope
                        pio.write_image(fig, image_file_name, engine='orca')
                    except ImportError:
                        pio.write_image(fig, image_file_name, engine='kaleido')
                except ValueError:
                    self.logger.exception("save file to %s error", image_file_name)
            finally:
                if lock is not None:
                    lock.release()  # 释放共享变量

        return charts_data


if __name__ == "__main__":
    pass
