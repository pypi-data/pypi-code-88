"""Module containing datasets' custom errors."""


__all__ = [
    # Class exports
    'InvalidTimeframeError',
    'OHLCVFetchError',
    'UnknownTimeframeUnitError',
]


class InvalidTimeframeError(ValueError):
    """This error is raised when the input timeframe is invalid.

    This error is also raised if the `Timeframe` class can't
    automagically extrapolate the values from the input."""


class UnknownTimeframeUnitError(ValueError):
    """This error is raised when the input timeframe unit is unknown."""


class OHLCVFetchError(Exception):
    """This error is raised when we failed to fetch OHLCV from DB."""
