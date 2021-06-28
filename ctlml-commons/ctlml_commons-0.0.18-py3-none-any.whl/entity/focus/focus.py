from __future__ import annotations

from abc import ABCMeta, abstractmethod
from logging import Logger
from typing import Any, Dict, List, Tuple

from ctlml_commons.entity.candle import Candle
from ctlml_commons.entity.lot import Lot
from ctlml_commons.entity.news import News
from ctlml_commons.util.date_utils import timeoffset_as_str


class Focus(metaclass=ABCMeta):
    @abstractmethod
    def serialize(self) -> Dict[str, Any]:
        """Serialize a investment focus.

        Returns:
            serialized investment focus
        """

    @abstractmethod
    def evaluate_buy(
            self, symbol: str, news: List[News], current_price: float, candles: Dict[str, Candle], logger: Logger
    ) -> Tuple[bool, str]:
        """If a symbol should be bought based on price trends.

        Args:
            symbol: symbol
            news: news
            current_price: current price
            candles: candle data
            logger: logger

        Returns:
            if symbol should be bought and a reason
        """

    def evaluate_sell(
            self, lot: Lot, news: List[News], current_price: float, candles: Dict[str, Candle], logger: Logger
    ) -> Tuple[bool, str]:
        """If a lot should be sold based on price trends.

        Args:
            lot: owned lot
            news: news
            current_price: current symbol price
            candles: candle data
            logger: logger

        Returns:
            if lot should be sold and a reason
        """

    @classmethod
    def _get_periods(cls, a_time, periods: int) -> List[str]:
        period_names = []

        mins = 0
        for i in range(periods):
            period_names.append(timeoffset_as_str(mins * 60, a_time))
            mins += 1

        period_names.reverse()
        return period_names[:-1]

    @classmethod
    def _all_exists(cls, periods: List[str], candle_data: Dict[str, Candle]) -> bool:
        return set(periods).issubset(candle_data.keys())
