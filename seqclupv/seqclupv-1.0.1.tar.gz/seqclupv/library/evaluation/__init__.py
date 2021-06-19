"""
    This package contains implementations of evaluators that can assess the performance of the variants of the 'SeqClu'
    algorithm.
"""

from .basic_baseline_prototypes import BasicBaselinePrototypes
from .basic_evaluator import BasicEvaluator


__all__ = ["BasicBaselinePrototypes",
           "BasicEvaluator"]
