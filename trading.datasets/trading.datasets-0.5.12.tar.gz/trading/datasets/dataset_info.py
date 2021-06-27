"""Module containing dataset info and metadata classes."""

from __future__ import annotations

from dateutil import relativedelta

from trading.datasets import errors
from trading.datasets.utils import string_utils


__all__ = [
    # Class exports
    'OHLCVMetadata',
    'Timeframe',
    'TimeframeUnit',
]


class OHLCVMetadata:
    """Data class for OHLCV-related metadata."""

    def __init__(
        self,
        exchange: OHLCVMetadata | str | None = None,
        symbol: str | None = None,
    ):

        # The first parameter is an OHLCVMetadata instance
        # let's ignore other parameters and use that
        # input as the metadata itself
        if isinstance(exchange, OHLCVMetadata):
            self.exchange = exchange.exchange
            self.symbol = exchange.symbol

        else:
            self.exchange = exchange
            self.symbol = symbol

    def __repr__(self):
        properties = ['exchange', 'symbol']
        return string_utils.class_repr(self, __class__.__name__, properties)

    def __bool__(self):
        return bool(self.exchange and self.symbol)

    def __eq__(self, other):
        return repr(self) == repr(other)

    @property
    def exchange(self):
        return self._exchange

    @exchange.setter
    def exchange(self, value):
        if value:
            self._exchange = str(value)
        else:
            self._exchange = None

    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, value):
        if value:
            self._symbol = str(value)
        else:
            self._symbol = None


class Timeframe:
    """Data class for timeframes."""

    def __init__(
        self,
        interval: Timeframe | str | int | float | None = None,
        unit: str | None = None,
    ):

        if not interval and interval != 0:
            self.interval = None
            self.unit = None

        elif isinstance(interval, Timeframe):
            self.interval = interval.interval
            self.unit = interval.unit

        elif isinstance(interval, str):

            # Input interval is the whole timeframe, ignore unit argument
            if not interval.isdigit():
                # Special case for millisecond which has two
                # characters as the unit
                if interval.endswith(TimeframeUnit.MILLISECOND):
                    self.interval = interval[:-2]
                    self.unit = interval[-2:]
                else:
                    self.interval = interval[:-1]
                    self.unit = interval[-1:]

            # Input interval is just the interval, use the unit argument
            else:
                self.interval = interval
                self.unit = unit

        elif isinstance(interval, (int, float)):
            self.interval = interval
            self.unit = unit

        else:
            raise errors.InvalidTimeframeError(f'{interval!r}, {unit!r}')

    def __repr__(self):
        properties = ['interval', 'unit']
        return string_utils.class_repr(self, __class__.__name__, properties)

    def __str__(self):
        return (f'{self.interval if self.interval else 0}'
                f'{self.unit if self.unit else ""}')

    def __bool__(self):
        return bool(self.interval and self.unit and self.interval != 0)

    def __eq__(self, other):
        return str(self) == str(other)

    @property
    def interval(self):
        return self._interval

    @interval.setter
    def interval(self, value):
        if not value and value != 0:
            self._interval = None
        else:
            try:
                self._interval = int(float(value))
            except (TypeError, ValueError):
                self._interval = None

    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        self._unit = TimeframeUnit(value)

    def get_duration(self, unit: str = 'ms') -> float | int:
        """Converts the given timeframe into a duration in the target unit.

        Arguments:
            unit: The target unit of time that we want the duration
                in. Valid input values are `'y'`, `'M'`, `'w'`, `'d'`,
                `'h'`, `'m'`, `'s'`, and `'ms'`.

        Raises:
            UnknownTimeframeUnitError: Raised if the target unit is unknown.

        Return:
            A floating number representing the duration of the timeframe
            in the target unit of time. If the target unit is "milliseconds"
            then the return type is an integer.
        """
        if not self.interval or not self.unit:
            return 0

        duration_in_seconds = self.unit.to_seconds()
        duration_in_seconds *= self.interval

        # Convert target unit to our standard class
        target_unit = TimeframeUnit(unit)

        duration_in_target_unit = target_unit.to_seconds()
        duration_in_target_unit = 1 / duration_in_target_unit
        duration_in_target_unit *= duration_in_seconds

        # Type casting function
        type_fn = int if unit == TimeframeUnit.MILLISECOND else float

        return type_fn(duration_in_target_unit)

    def to_pandas_timeframe(self):
        """Returns the equivalent timeframe in Pandas's own units."""
        if bool(self):
            return f'{self.interval}{self.unit.to_pandas_unit()}'
        return None

    def to_offset_timeframe(self):
        """Returns the equivalent timeframe in the context of offsets."""
        if bool(self):
            return f'{self.interval}{self.unit.to_offset_unit()}'
        return None

    def to_timedelta(self):
        """Returns the equivalent timedelta object of the Timeframe object."""

        # Month and year is not accepted as timedelta key arguments
        # so we need to cover them specifically. Note that these timedeltas
        # are not accurate because we don't take into account leap years
        # and all those edge cases.
        if self.unit == TimeframeUnit.MONTH:
            return relativedelta.relativedelta(days=30.4167 * self.interval)

        if self.unit == TimeframeUnit.YEAR:
            return relativedelta.relativedelta(days=365 * self.interval)

        if self.unit == TimeframeUnit.MILLISECOND:
            return relativedelta.relativedelta(
                microseconds=1000 * self.interval)

        return relativedelta.relativedelta(**{
                self.unit.to_word(): self.get_duration(unit=self.unit)
            })


class TimeframeUnit:
    """Data class for timeframe units."""

    YEAR = 'y'
    MONTH = 'M'
    WEEK = 'w'
    DAY = 'd'
    HOUR = 'h'
    MINUTE = 'm'
    SECOND = 's'
    MILLISECOND = 'ms'

    UNIT_TO_SECONDS_MAPPING = {
        YEAR: 60 * 60 * 24 * 365,  # 31536000
        MONTH: 60 * 60 * 24 * 30,  # 2592000
        WEEK: 60 * 60 * 24 * 7,    # 604800
        DAY: 60 * 60 * 24,         # 86400
        HOUR: 60 * 60,             # 3600
        MINUTE: 60,                # 60
        SECOND: 1,                 # 1
        MILLISECOND: 1 / 1000,     # 0.001
    }

    # Create an inverse dictionary of conversion
    SECONDS_TO_UNIT_MAPPING = {
        v: k for k, v in UNIT_TO_SECONDS_MAPPING.items()
    }

    _PANDAS_UNITS_MAPPING = {
        YEAR: 'Y',
        MONTH: 'MS',
        WEEK: 'W',
        DAY: 'D',
        HOUR: 'H',
        MINUTE: 'T',
        SECOND: 'S',
        MILLISECOND: 'L',
    }

    _OFFSET_UNITS_MAPPING = {
        YEAR: 'y',
        MONTH: 'm',
        WEEK: 'w',
        DAY: 'd',
        HOUR: 'h',
        MINUTE: 'min',
        SECOND: 's',
        MILLISECOND: 'ms',
    }

    WORD_UNITS_MAPPING = {
        YEAR: 'years',
        MONTH: 'months',
        WEEK: 'weeks',
        DAY: 'days',
        HOUR: 'hours',
        MINUTE: 'minutes',
        SECOND: 'seconds',
        MILLISECOND: 'milliseconds',
    }

    def __init__(self, unit: TimeframeUnit | str | None = None):
        if not unit:
            self._unit = None

        elif str(unit) not in self.UNIT_TO_SECONDS_MAPPING:
            raise errors.UnknownTimeframeUnitError(unit)

        else:
            self._unit = str(unit)

    def __repr__(self):
        return repr(self._unit)

    def __str__(self):
        return str(self._unit)

    def __bool__(self):
        return bool(self._unit)

    def __eq__(self, other):
        return str(self) == str(other)

    def to_seconds(self):
        if not self._unit:
            return 0
        return self.UNIT_TO_SECONDS_MAPPING[self._unit]

    def to_pandas_unit(self):
        if not self._unit:
            return None
        return self._PANDAS_UNITS_MAPPING[self._unit]

    def to_offset_unit(self):
        if not self._unit:
            return None
        return self._OFFSET_UNITS_MAPPING[self._unit]

    def to_word(self):
        if not self._unit:
            return None
        return self.WORD_UNITS_MAPPING[self._unit]
