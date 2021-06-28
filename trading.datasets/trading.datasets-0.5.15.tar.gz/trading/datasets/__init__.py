"""Trading Datasets Library."""

from trading.datasets import exchange
from trading.datasets import utils
from trading.datasets import errors

from trading.datasets.dataset_info import OHLCVMetadata
from trading.datasets.dataset_info import Timeframe
from trading.datasets.dataset_info import TimeframeUnit

from trading.datasets.ohlcv import OHLCV


__all__ = [
    # Module exports
    'errors',
    'exchange',
    'utils',

    # Class exports
    'OHLCV',
    'OHLCVMetadata',
    'Timeframe',
    'TimeframeUnit',
]


# Don't expose core module in public package
# but expect name error from linting and tests
try:
    del dataset_info
    del ohlcv
except NameError:  # pragma: no cover
    pass
