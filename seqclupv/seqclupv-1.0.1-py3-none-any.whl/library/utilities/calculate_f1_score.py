"""
    This module contains a method that calculates the F1-score given sets of true labels and predicted labels.
"""

from typing import Dict, Union

import numpy as np
from sklearn.metrics import f1_score


def calculate_f1_score(trueLabels: Dict[str, Union[chr, int]],
                       predictedLabels: Dict[str, Union[chr, int]], average: str) -> float:
    """
        This method calculates the F1-score given a set of true labels and predicted labels as well as the averaging
        procedure that decides the type of F1-score.

        :param trueLabels: The correct labels of the data as a dictionary where the keys are the hashes of the sequences
        and the values are the labels.
        :param predictedLabels: The predicted labels of the data as a dictionary where the keys are the hashes of the
        sequences and the values are the labels.
        :param average: The averaging procedure used in the statistical test. The averaging procedure decides the type
        of F1-score, this can be the micro, macro or weighted F1-score.
        :return: The F1-score for the given sets of true labels and predicted labels.
    """
    length = len(trueLabels)
    assert length == len(predictedLabels)

    trueLabelsArray = np.empty((length,), dtype=object)
    predictedLabelsArray = np.empty((length,), dtype=object)

    for i, key in enumerate(trueLabels):
        trueLabelsArray[i] = trueLabels[key]
        predictedLabelsArray[i] = predictedLabels[key]

    return f1_score(trueLabelsArray, predictedLabelsArray, average=average)
