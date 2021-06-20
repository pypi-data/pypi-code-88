"""
    This package contains implementations of distance measures that are used in the 'SeqClu' algorithm to compute the
    distance between two incoming data points.
"""

from .dynamic_time_warping import DynamicTimeWarping


__all__ = ["DynamicTimeWarping"]
