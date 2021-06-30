"""Module containing the OrderBook class."""

from __future__ import annotations

import datetime as dtlib

from trading.datasets import dataset_info
from trading.datasets import errors
from trading.datasets import exchange as exchangelib


__all__ = [
    # Class exports
    'OrderBook',
]


class OrderBook:

    @classmethod
    def load(
        cls,
        exchange_name: str,
        symbol: str,
        start: dtlib.datetime | str | int | None = None,
        end: dtlib.datetime | str | int | None = None,
    ) -> OrderBook:

        """Returns an instance of a DataFrame based on the given parameters.

        Arguments:
            exchange_name: Name of the crypto asset exchange.
            symbol: Ticker symbol of the crypto asset.
            start: Starting datetime of the data to be fetched.
                The input argument can be a string indicating a
                valid datetime-like string or a number indicating the
                timestamp in milliseconds.
            end: Ending timestamp of the data to be fetched.
                The input argument can be a string indicating a
                valid datetime-like string or a number indicating the
                timestamp in milliseconds.

        Returns:
            An instance of a `DataFrame` containing the data of the
            given input parameters.
        """

        # Validate and convert the exchange name into an exchange instance
        exchange = exchangelib.get(exchange_name)()

        # Validate and standardize the symbol before using it
        symbol = exchange.get_valid_symbol(symbol)

        # Make sure that the start and end times are valid
        timeframe = dataset_info.Timeframe('1d')
        start, end = exchange.get_valid_start_end(start, end, timeframe)

        return cls._generate_db_query(exchange.name, symbol, start, end)

    @staticmethod
    def _generate_db_query(
        exchange_name: str,
        symbol: str,
        start: dtlib.datetime,
        end: dtlib.datetime,
    ) -> str:

        return (exchange_name, symbol, start, end)
