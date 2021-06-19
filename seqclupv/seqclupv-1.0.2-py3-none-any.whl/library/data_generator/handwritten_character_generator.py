"""
    This module contains a class that is responsible for generating handwritten character data that are passed to the
    'SeqClu' algorithm.

    Link to the 'UJI Pen Character' data set
    https://archive.ics.uci.edu/ml/datasets/UJI+Pen+Characters

    NOTE: The characters that are contained in the data set are as follows.
    ['C', 'U', 'V', 'W', 'S', 'O', '1', '2', '3', '5', '6', '8', '9']
"""

import glob
import os
import re
from typing import Dict, List, Tuple, Union

import matplotlib.pyplot as plt
import numpy as np
from numpy import ndarray
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw

from seqclupv.library.interfaces.data_generator import IDataGenerator
from seqclupv.library.utilities.construct_stream import constructStream


def parseFile(lines: List[str]) -> Dict[str, List[Tuple[int, int]]]:
    """
        This method parses a file containing a data set of sequences. The lines in this file are processed in the
        method to obtain a dictionary in which the keys represent the name of some class and the values represent
        a list of sequences that belong to this class.

        :param lines: The lines that are present in some file containing a data set of sequences.
        :return: A dictionary in which the keys represent the name of some class and the values represent
        a list of sequences that belong to this class.
    """
    points: Dict[str, List[Tuple[int, int]]] = dict()
    newChar = False
    cont = False
    point = []
    sequenceClass = None

    for line in lines[1:]:
        if '.COMMENT' in line and 'Class' in line and '[' in line and '#' not in line:
            b = re.findall('.*?\.COMMENT\s+Class\s+\[(.*?)\]', line)
            sequenceClass = b[0]
            newChar = True
            point = []
            continue
        if '.PEN_UP' in line:
            cont = False
            if sequenceClass not in points.keys():
                points[sequenceClass] = []
            points[sequenceClass].append(point)
        if '.PEN_DOWN' in line:
            cont = True
            continue
        if newChar and cont:
            b = re.findall('.*?(\d+)\s+([-\d]+).*', line)
            xy = b[0]
            point.append((int(xy[0]), int(xy[1])))

    return points


class HandwrittenCharacterGenerator(IDataGenerator):

    # CONSTRUCTOR #

    def __init__(self, classes: List[chr], numPrototypes: int, computeDistances: bool) -> None:
        """
            This method initializes the data generator with a given list of classes that the
            generated data set should contain.

            :param classes: The classes that are present in the data set as a list of characters.
            :param numPrototypes: The number of prototypes that will be used in the 'SeqClu' algorithm.
            :param computeDistances: A boolean value indicating whether or not the pair-wise distances between items
            in the data set should be computed.
            :return: void
        """
        super().__init__(numPrototypes, computeDistances)
        self._classes = classes

    # PUBLIC METHODS #

    def generateData(self) -> List[Union[ndarray, list]]:
        """
            This method generates a data set that is used in the 'SeqClu' algorithm or one of its extensions as
            a list of sequences.

            :return: A data set that is used in the 'SeqClu' algorithm or one of its extensions as
            a list of sequences.
        """
        self._classDictionary = {k: v for v, k in enumerate(self.classes)}

        segments = dict()
        files = glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../data/handwriting/*"))
        for f in files:
            f_ = open(f, 'r')
            lines = f_.readlines()
            content = parseFile(lines)
            for classIdentifier, segment in content.items():
                if classIdentifier not in self.classes:
                    continue
                if classIdentifier not in segments.keys():
                    segments[classIdentifier] = []
                for sequence in segment:
                    sequenceArray = np.array(sequence)
                    identical = False
                    for otherSequence in segments[classIdentifier]:
                        if np.array_equal(sequenceArray, otherSequence):
                            identical = True
                            break
                    if not identical:
                        segments[classIdentifier].append(sequence)
            f_.close()

        clusters = []
        for classIdentifier in self.classes:
            clusters.append(segments[classIdentifier])

        # Visualize input characters
        for classIdentifier in segments.keys():
            print(f"[SeqCluCLI] Class \'{classIdentifier}\': {len(segments[classIdentifier])} instances.")
            fig, ax = plt.subplots()
            plt.title("Character: " + classIdentifier)

            for segment in segments[classIdentifier]:
                plt.plot([x[0] for x in segment], [x[1] for x in segment])
            ax.set_ylim(ax.get_ylim()[1], ax.get_ylim()[0])

        trajectory, randomList = constructStream(clusters, self.classes, self.numPrototypes)

        print(f"[SeqCluCLI] The number of incoming sequences is {len(randomList)}.")
        print(f"[SeqCluCLI] The total number of sequences is {len(trajectory)}.")

        self._data = [x for (x, y) in trajectory]  # Data: This is a list of sequences.
        self._transformDataToArray()
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

        return self.data

    # PRIVATE METHODS #

    def _transformDataToArray(self) -> None:
        """
            This method transforms all the data stored in the 'data' property to a list of NumPy arrays.

            :return: void
        """
        result = []
        for sequence in self.data:
            arr = np.empty((len(sequence), 2))
            for i, (itemOne, itemTwo) in enumerate(sequence):
                arr[i][0] = itemOne
                arr[i][1] = itemTwo
            result.append(arr)
        self._data = result
