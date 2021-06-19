"""
    This package contains classes that are responsible for storing information that is relevant to the clustering
    process that is part of the 'SeqClu' algorithm. The relevant information includes a set of candidate prototypes,
    a set of clusters and a set of prototypes for some cluster.
"""

from .candidates import CandidateStore
from .cluster import ClusterStore
from .prototype_frequencies import PrototypeFrequencyStore
from .prototypes import PrototypeStore
from .sequences import SequenceStore


__all__ = ["CandidateStore",
           "ClusterStore",
           "PrototypeFrequencyStore",
           "PrototypeStore",
           "SequenceStore"]
