"""
    This module contains the interface for the class that stores the prototypes of some baseline. This class can be used
    to compare the prototypes obtained at the end of the online 'Seqclu' algorithm, where the number of identical
    prototypes divided by the total number of prototypes can be used as evaluation metric.
"""

from abc import ABC, abstractmethod
from typing import List, Optional


class IBaselinePrototypes(ABC):

    @staticmethod
    @abstractmethod
    def getPrototypes(experimentName: str) -> Optional[List[List[str]]]:
        """
            This method returns the prototypes that were obtained after executing some baseline algorithm.
            These prototypes can be compared to the prototypes obtained at the end of the online 'SeqClu' algorithm,
            where the number of identical prototypes divided by the total number of prototypes
            can be used as evaluation metric.

            :param experimentName: The name of the experiment for which the prototypes need to be retrieved.
            :return: The prototypes obtained after executing some experiment identified by the experiment name.
        """
        pass
