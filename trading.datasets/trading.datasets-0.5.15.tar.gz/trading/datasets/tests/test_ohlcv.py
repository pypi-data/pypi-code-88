"""Tests for trading.datasets.dataset_info."""
# pylint: disable=missing-class-docstring,missing-function-docstring

import pandas as pd

from trading.datasets import ohlcv as ohlcv_lib


class TestOHLCV:

    def test_initialization(self):
        ohlcv = ohlcv_lib.OHLCV([1, 2, 3], columns=['col1'])
        assert issubclass(type(ohlcv), pd.DataFrame)
        assert isinstance(ohlcv, ohlcv_lib.OHLCV)
        assert isinstance(ohlcv['col1'], ohlcv_lib.OHLCVSeries)

    def test_cache_filepath_generation(self):
        assert ohlcv_lib.OHLCV._generate_cache_filepath(
            'A', 'B', 'C', extension='D').name == 'A_B_C.ohlcv.D'

    def test_timeframe_detection(self):
        ohlcv = ohlcv_lib.OHLCV(
            [['2010-01-01', 1], ['2010-01-02', 2]],
            columns=['col1', 'col2'])
        ohlcv['col1'] = pd.to_datetime(ohlcv['col1'])
        ohlcv = ohlcv.set_index('col1')
        assert ohlcv.timeframe == '1d'

        # Force timeframe, skip detection
        ohlcv.timeframe = '1m'
        assert ohlcv.timeframe == '1m'

        # Only one row of data, detection is not possible
        ohlcv = ohlcv_lib.OHLCV([['2010-01-01', 1]], columns=['col1', 'col2'])
        ohlcv['col1'] = pd.to_datetime(ohlcv['col1'])
        ohlcv = ohlcv.set_index('col1')
        assert ohlcv.timeframe == None

        # Lowest timeframe is one minute
        ohlcv = ohlcv_lib.OHLCV(
            [['2010-01-01 00:00:05', 1], ['2010-01-02 00:00:06', 2]],
            columns=['col1', 'col2'])
        ohlcv['col1'] = pd.to_datetime(ohlcv['col1'])
        ohlcv = ohlcv.set_index('col1')
        assert ohlcv.timeframe == None
