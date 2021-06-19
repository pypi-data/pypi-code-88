"""
    This package contains all interfaces that are used in the 'SeqClu' framework.
"""

from .baseline_prototypes import IBaselinePrototypes
from .candidate_store import ICandidateStore
from .data_generator import IDataGenerator
from .data_source import IDataSource
from .distance_measure import IDistanceMeasure
from .evaluator import IEvaluator
from .fake_data_source import IFakeDataSource
from .heuristics import IPrototypeValue
from .seqclu import ISeqClu

__all__ = ["IBaselinePrototypes",
           "ICandidateStore",
           "IDataGenerator",
           "IDataSource",
           "IDistanceMeasure",
           "IEvaluator",
           "IFakeDataSource",
           "IPrototypeValue",
           "ISeqClu"]
