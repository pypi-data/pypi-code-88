"""
    This module contains a base class that is responsible for generating time series data from
    https://www.timeseriesclassification.com that are passed to the 'SeqClu' algorithm.
"""

from abc import ABC
from typing import List, Dict, Tuple, Union
import os

from fastdtw import fastdtw
import numpy as np
from numpy import ndarray
from scipy.spatial.distance import euclidean
from sktime.utils.data_io import load_from_tsfile_to_dataframe

from seqclupv.library.interfaces.data_generator import IDataGenerator
from seqclupv.library.utilities.construct_stream import constructStream
from seqclupv.library.utilities.hash_sequence import hashSequence


class TimeSeriesClassificationBase(IDataGenerator, ABC):

    # STATIC METHODS #

    @staticmethod
    def loadData(path: str, filenames: List[str]) -> Tuple[List[ndarray], List[str]]:
        """
            This method loads the data from a given path to some directory and file name.

            :param path: The path to some directory, relative to the current working directory.
            :param filenames: The names of the files that should be loaded.
            :return: The data that was loaded from all of the files.
        """
        dataPath = os.path.join(os.getcwd(), path)

        data: List[ndarray] = []
        labels = np.array([])

        for filename in filenames:
            newData, newLabels = load_from_tsfile_to_dataframe(os.path.join(dataPath, filename))
            newData = newData["dim_0"]
            for x in newData:
                xArray = x.to_numpy()
                data.append(xArray)
            labels = np.concatenate((labels, newLabels))

        return data, labels

    # CONSTRUCTOR

    def __init__(self, numPrototypes: int, computeDistances: bool) -> None:
        """
            This method initializes the data generator given the number of prototypes that are drawn from the data set
            and a boolean value indicating whether or not the pair-wise distances between items in the data set should
            be computed.

            :param numPrototypes: The number of prototypes that should be drawn from the data set.
            :param computeDistances: A boolean value indicating whether or not the pair-wise distances between items in
            the data set should be computed.
        """
        super().__init__(numPrototypes)
        self._computeDistances = computeDistances

    # PRIVATE METHODS #

    def _generateData(self, data: List[ndarray], labels: List[str],
                      classes: List[str]) -> Tuple[List[Union[ndarray, list]], Dict[str, str]]:
        """
            This method creates the required data structures from the loaded data, labels and classes.

            :param data: The data that were loaded from one of the data files.
            :param labels: The labels of the data that were loaded from one of the data files.
            :param classes: All the classes that are present in the data set.
            :return: The constructed data stream and the labels of the data ordered according to
            the ordering of the items in the data stream.
        """
        labelResult = {}
        for i, label in enumerate(labels):
            if label in classes:
                labelResult[hashSequence(data[i])] = label

        clustersDict: Dict[str, List[ndarray]] = {}
        for clusterIdentifier in classes:
            clustersDict[clusterIdentifier] = []

        for i, sequence in enumerate(data):
            label = labels[i]
            if label in classes:
                clustersDict[label].append(sequence)

        clusters = []
        classDictionary: Dict[str, int] = {}
        for i, clusterIdentifier in enumerate(classes):
            clusters.append(clustersDict[clusterIdentifier])
            classDictionary[clusterIdentifier] = i

        self._classes = classes
        self._classDictionary = classDictionary

        trajectory, randomList = constructStream(clusters, self.classes, self.numPrototypes)

        self._data = [x for (x, y) in trajectory]  # Data: This is a list of sequences.
        self._indices = [x for x, y in enumerate(self.data)]  # IDs: This is a list of indices of the samples in X.
        self._labels = [y for (x, y) in trajectory]  # classes: This is a list of labels assigned to the samples in X.

        if self.computeDistances:
            distances = [-1] * len(self.data)
            distances = [[-1] * len(self.data) for _ in distances]

            for i in range(len(self.data)):
                for j in range(i + 1):
                    _d = None
                    if i == j:
                        distances[i][j] = 0.0
                    elif i > j:
                        _d = fastdtw(self.data[i], self.data[j], dist=euclidean)[0]
                        distances[i][j] = _d
                        distances[j][i] = _d

            self._distances = distances
        else:
            self._distances = None

        return self.data, labelResult
