"""
    This package contains all source code that is used in the variants of the 'SeqClu' algorithm that are contained in
    this framework.
"""

from .data_generator import HandwrittenCharacterGenerator, GesturePebbleGenerator, PLAIDGenerator, CurveGenerator
from .data_source import FakeDataSource
from .distance import DynamicTimeWarping
from .evaluation import BasicBaselinePrototypes, BasicEvaluator
from .heuristics import LinearPrototypeValue
from .interfaces import IBaselinePrototypes, ICandidateStore, IDataGenerator, IDataSource, IDistanceMeasure, \
    IEvaluator, IFakeDataSource, IPrototypeValue, ISeqClu
from .storage import CandidateStore, ClusterStore, PrototypeFrequencyStore, PrototypeStore, SequenceStore
from .utilities import calculate_f1_score, constructStream, isHashInKey, hashSequence, statistical_test
from .visualization import Visualizer


__all__ = ["HandwrittenCharacterGenerator",
           "GesturePebbleGenerator",
           "PLAIDGenerator",
           "CurveGenerator",
           "FakeDataSource",
           "DynamicTimeWarping",
           "BasicBaselinePrototypes",
           "BasicEvaluator",
           "LinearPrototypeValue",
           "IBaselinePrototypes",
           "ICandidateStore",
           "IDataGenerator",
           "IDataSource",
           "IDistanceMeasure",
           "IEvaluator",
           "IFakeDataSource",
           "IPrototypeValue",
           "ISeqClu",
           "CandidateStore",
           "ClusterStore",
           "PrototypeFrequencyStore",
           "PrototypeStore",
           "SequenceStore",
           "calculate_f1_score",
           "constructStream",
           "isHashInKey",
           "hashSequence",
           "statistical_test",
           "Visualizer"]
