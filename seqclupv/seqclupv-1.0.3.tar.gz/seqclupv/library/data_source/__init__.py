"""
    This package contains all implementations of data sources that are used by the 'SeqClu' algorithm to request
    data at every tick.
"""
from .fake_data_source import FakeDataSource


__all__ = ["FakeDataSource"]
