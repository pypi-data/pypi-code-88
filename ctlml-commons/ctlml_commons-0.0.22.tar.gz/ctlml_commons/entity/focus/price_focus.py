from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from datetime import datetime
from logging import Logger
from typing import Any, Dict, List, Tuple

from ctlml_commons.entity.candle import Candle
from ctlml_commons.entity.focus.focus import Focus
from ctlml_commons.entity.lot import Lot
from ctlml_commons.entity.news import News
from ctlml_commons.entity.range_window import RangeWindow
from ctlml_commons.util.date_utils import to_est


@dataclass(frozen=True)
class PriceFocus(Focus):
    """Price up/down based investment strategy."""

    """Per share price window range"""
    per_share_price_window: RangeWindow

    """Total lot profit/loss threshold"""
    total_threshold: float

    """Number of periods to consider for purchase decisions"""
    num_periods: int

    """If should sell at the end of day"""
    sell_at_end_of_day: bool

    def evaluate_buy(
        self, symbol: str, news: List[News], current_price: float, candles: Dict[str, Candle], logger: Logger
    ) -> Tuple[bool, str]:
        if not candles:
            return False, "Not enough data"

        is_up_last_periods, message = self.up_last(candle_data=candles, a_time=to_est(), periods=self.num_periods)

        if not is_up_last_periods:
            not_up_message: str = f"Not up: price: {current_price}, open: {candles[list(candles.keys())[-1]].open}"
            logger.debug(not_up_message)
            return False, not_up_message

        return True, message

    def evaluate_sell(
        self, lot: Lot, news: List[News], current_price: float, candles: Dict[str, Candle], logger: Logger
    ) -> Tuple[bool, str]:
        per_share_diff: float = current_price - lot.purchase_price
        lot_diff: float = per_share_diff * lot.shares

        if lot_diff >= self.total_threshold:
            message: str = f"Win over threshold by {lot_diff} vs {self.total_threshold}"
            logger.debug(message)
            return True, message

        elif lot_diff <= -self.total_threshold:
            message: str = f"Loss over threshold by {lot_diff} vs {-self.total_threshold}"
            logger.debug(message)
            return True, message

        elif per_share_diff >= self.per_share_price_window.ceiling:
            message: str = f"Win over per share price by {per_share_diff} vs {self.per_share_price_window.ceiling}"
            logger.debug(message)
            return True, message

        elif per_share_diff <= -self.per_share_price_window.floor:
            message: str = f"Loss under per share price by {per_share_diff} vs {-self.per_share_price_window.floor}"
            logger.debug(message)
            return True, message

        message: str = f"Wait...lot_diff: {lot_diff}. per_share: {per_share_diff}"
        logger.debug(message)
        return False, message

    @classmethod
    def up_last(cls, candle_data: Dict[str, Candle], a_time: datetime, periods: int) -> Tuple[bool, str]:

        period_names: List[str] = cls._get_periods(a_time=a_time, periods=periods)
        if not cls._all_exists(periods=period_names, candle_data=candle_data):
            return False, f"Not enough correct periods: {period_names} vs {candle_data.keys()}"

        ups: List[bool] = cls._get_ups(periods=period_names, candle_data=candle_data)
        return all(ups), cls._get_ups_msg(periods=period_names, candle_data=candle_data)

    @classmethod
    def _get_ups(cls, periods: List[str], candle_data: Dict[str, Candle]) -> List[bool]:
        return [candle_data[period].close > candle_data[period].open for period in periods]

    @classmethod
    def _get_ups_msg(cls, periods: List[str], candle_data: Dict[str, Candle]) -> str:
        return f"{cls._get_ups(periods, candle_data)} " + "; ".join(
            [f"{period}: {candle_data[period].close} > {candle_data[period].open}" for period in periods]
        )

    def serialize(self) -> Dict[str, Any]:
        data = deepcopy(self.__dict__)
        data["per_share_price_window"] = self.per_share_price_window.serialize()
        data["focus_type"] = self.__class__.__name__
        return data

    @classmethod
    def deserialize(cls, input_data: Dict[str, Any]) -> PriceFocus:
        data = deepcopy(input_data)

        del data["focus_type"]
        data["per_share_price_window"] = RangeWindow.deserialize(data["per_share_price_window"])

        return cls(**data)
