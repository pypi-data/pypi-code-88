"""
    This module is an implementation of an evaluator that measures the accuracy of the results obtained from the
    'SeqClu' algorithm as well as various other metrics such as the silhouette score, the number of distance
    computations that were made and the time taken to execute the algorithm.
"""
import time
from typing import Dict, List, Optional, Union

from seqclupv.SeqClu import SeqClu
from seqclupv.SeqCluBaselineOnline import SeqCluBaselineOnline
from seqclupv.SeqCluBaselineOffline import SeqCluBaselineOffline
from seqclupv.library.data_source import FakeDataSource
from seqclupv.library.distance.dynamic_time_warping import DynamicTimeWarping
from seqclupv.library.interfaces.evaluator import IEvaluator
from seqclupv.library.utilities.calculate_f1_score import calculate_f1_score
from seqclupv.library.utilities.hash_sequence import hashSequence


class BasicEvaluator(IEvaluator):

    # PROPERTIES #

    @property
    def actualLabels(self) -> Dict[str, Union[chr, int]]:
        """
            This property stores the correct labels of the data processed by the 'SeqClu' algorithm in a dictionary
            where the keys are the hashes of the data.

            :return: A dictionary where the keys are the hashes of the data and the values are the correct labels of the
            data processed by the 'SeqClu' algorithm.
        """
        return self._actualLabels

    @property
    def baselinePrototypes(self) -> Optional[List[List[str]]]:
        """
            This property stores the prototypes of the baseline that are used in the evaluator.

            :return: The prototypes of the baseline that are used in the evaluator.
        """
        return self._baselinePrototypes

    @property
    def fakeDataSource(self) -> FakeDataSource:
        """
            This property stores the fake data source that is used in the evaluator.

            :return: The fake data source that is used in the evaluator.
        """
        return self._fakeDataSource

    @property
    def distanceMeasure(self) -> DynamicTimeWarping:
        """
            This property stores the distance measure that is used in the 'SeqClu' algorithm.

            :return: The distance measure that is used in the 'SeqClu' algorithm.
        """
        return self._distanceMeasure

    @property
    def seqClu(self) -> Optional[SeqClu]:
        """
            This property stores the 'SeqClu' algorithm that is used in the evaluator.

            :return: The 'SeqClu' algorithm that is used in the evaluator.
        """
        return self._seqClu

    @property
    def seqCluBaselineOffline(self) -> Optional[SeqCluBaselineOffline]:
        """
            This property stores the offline baseline variant of the 'SeqClu' algorithm that is used in the evaluator.

            :return: The offline baseline variant of the 'SeqClu' algorithm that is used in the evaluator.
        """
        return self._seqCluBaselineOffline

    @property
    def seqCluBaselineOnline(self) -> Optional[SeqCluBaselineOnline]:
        """
            This property stores the online baseline variant of the 'SeqClu' algorithm that is used in the evaluator.

            :return: The online baseline variant of the 'SeqClu' algorithm that is used in the evaluator.
        """
        return self._seqCluBaselineOnline

    # CONSTRUCTOR #

    def __init__(self, fakeDataSource: FakeDataSource,
                 distanceMeasure: DynamicTimeWarping,
                 seqClu: Optional[SeqClu],
                 seqCluBaselineOnline: Optional[SeqCluBaselineOnline],
                 seqCluBaselineOffline: Optional[SeqCluBaselineOffline],
                 baselinePrototypes: Optional[List[List[str]]]) -> None:
        """
            This method initializes the evaluator.

            :param fakeDataSource: The fake data source that is used in the evaluator.
            :param distanceMeasure: The distance measure that is used in the 'SeqClu' algorithm.
            :param seqClu: The 'SeqClu' algorithm that is used in the evaluator.
            :param seqCluBaselineOnline: The online baseline variant of the 'SeqClu' algorithm that is used in the evaluator.
            :param seqCluBaselineOffline: The offline baseline variant of the 'SeqClu' algorithm that is used in the evaluator.
            :param baselinePrototypes: The prototypes of the baseline that are used in the evaluator.
            :return: void
        """
        self._actualLabels = fakeDataSource.actualLabels
        self._baselinePrototypes = baselinePrototypes
        self._fakeDataSource = fakeDataSource
        self._distanceMeasure = distanceMeasure
        self._seqClu = seqClu
        self._seqCluBaselineOffline = seqCluBaselineOffline
        self._seqCluBaselineOnline = seqCluBaselineOnline

    # PUBLIC METHODS #

    def evaluate(self) -> None:
        """
            This method evaluates the performance of the variants of the 'SeqClu' algorithm.

            :return: void
        """
        if self.seqCluBaselineOnline is not None:
            startTime = time.perf_counter()
            self.seqCluBaselineOnline.execute()
            endTime = time.perf_counter()
            timeTaken = endTime - startTime
            seqCluBaselineOnlineResult = self.seqCluBaselineOnline.finalLabels
            prototypeKeys = []
            for prototypeDict in self.seqCluBaselineOnline.prototypes:
                prototypeKeys.append(list(prototypeDict.keys()))
            self._printResults(seqCluBaselineOnlineResult, "SeqCluBaselineOnline", timeTaken, prototypeKeys)

            correct = 0
            if self.baselinePrototypes is not None:
                for i, baselineClusterPrototypes in enumerate(self.baselinePrototypes):
                    prototypes = self.seqCluBaselineOnline.clusters[i]
                    correct += len(set(prototypes).intersection(set(baselineClusterPrototypes)))
            prototypeAccuracy = correct / (self.seqClu.numPrototypes * self.seqClu.numClusters)
            print(f"[SeqClu] PrototypeAccuracy {prototypeAccuracy}")

        if self.seqCluBaselineOffline is not None:
            startTime = time.perf_counter()
            self.seqCluBaselineOffline.execute()
            endTime = time.perf_counter()
            timeTaken = endTime - startTime + self.seqCluBaselineOffline.time
            _, seqCluBaselineOfflineResult = self.seqCluBaselineOffline.finalLabels
            prototypeKeys = []
            for i, cluster in enumerate(self.seqCluBaselineOffline.clusters):
                prototypeKeysItem = []
                for prototypeIdx in cluster:
                    prototypeHash = hashSequence(self.seqCluBaselineOffline.data[prototypeIdx])
                    prototypeKeysItem.append(prototypeHash)
                prototypeKeys.append(prototypeKeysItem)
            self._printResults(seqCluBaselineOfflineResult, "SeqCluBaselineOffline", timeTaken, prototypeKeys)

        if self.seqClu is not None:
            startTime = time.perf_counter()
            self.seqClu.execute()
            endTime = time.perf_counter()
            timeTaken = endTime - startTime
            seqCluResult = self.seqClu.finalLabels
            prototypeKeys = []
            for cluster in self.seqClu.clusters:
                prototypeKeys.append(list(cluster.prototypes.prototypes.keys()))
            print(f"[SeqClu] Buffered sequences are {self.seqClu.bufferedSequences}")
            print(f"[SeqClu] Sequences clustered by approximation are {self.seqClu.clusteredByApproximation}")
            self._printResults(seqCluResult, "SeqClu", timeTaken, prototypeKeys)
            correctSimple = 0
            correctComplex = 0
            wrongComplex = 0
            total = len(self.seqClu.clusteredByApproximation)
            for sequenceHash in self.seqClu.clusteredByApproximation:
                actualLabel = self.actualLabels[sequenceHash]
                if self.seqClu.finalLabels[sequenceHash] == actualLabel:
                    correctSimple += 1
                    if self.seqCluBaselineOnline is not None and self.seqCluBaselineOnline.finalLabels[sequenceHash] != actualLabel:
                        correctComplex += 1
                elif self.seqCluBaselineOnline is not None and self.seqCluBaselineOnline.finalLabels[sequenceHash] == actualLabel:
                    wrongComplex += 1
            if total > 0:
                accuracySimple = correctSimple / total
                accuracyComplex = correctComplex / total
                accuracyWrongComplex = wrongComplex / total
                print(f"[SeqClu] Approximation: {accuracySimple},{accuracyComplex},{accuracyWrongComplex}")

            correct = 0
            if self.baselinePrototypes is not None:
                for i, baselineClusterPrototypes in enumerate(self.baselinePrototypes):
                    prototypes = self.seqClu.clusters[i].prototypes.prototypes
                    correct += len(set(prototypes.keys()).intersection(set(baselineClusterPrototypes)))
            prototypeAccuracy = correct / (self.seqClu.numPrototypes * self.seqClu.numClusters)
            print(f"[SeqClu] PrototypeAccuracy {prototypeAccuracy}")

            if self.seqCluBaselineOnline is not None:
                correctSimple = 0
                correctComplex = 0
                wrongComplex = 0
                total = len(self.seqClu.bufferedSequences)
                for sequenceHash in self.seqClu.bufferedSequences:
                    actualLabel = self.actualLabels[sequenceHash]
                    if self.seqClu.finalLabels[sequenceHash] == actualLabel:
                        correctSimple += 1
                        if self.seqCluBaselineOnline is not None and self.seqCluBaselineOnline.finalLabels[sequenceHash] != actualLabel:
                            correctComplex += 1
                    elif self.seqCluBaselineOnline is not None and self.seqCluBaselineOnline.finalLabels[sequenceHash] == actualLabel:
                        wrongComplex += 1
            else:
                correctSimple = 0
                correctComplex = 0
                wrongComplex = 0
            if total > 0:
                accuracySimple = correctSimple / total
                accuracyComplex = correctComplex / total
                accuracyWrongComplex = wrongComplex / total
                print(f"[SeqClu] Buffering: {accuracySimple},{accuracyComplex},{accuracyWrongComplex}.")
                print(f"[SeqClu] Buffering correctSimple, correctComplex, wrongComplex, "
                      f"total {correctSimple}, {correctComplex}, {wrongComplex}, {total}")

    # PRIVATE METHODS #

    def _printResults(self, result: Dict[str, Union[chr, int]], algorithmName: str,
                      timeTaken: float, prototypeHashes: List[List[str]]) -> None:
        """
            This method prints the results of one of the variants of the 'SeqClu' algorithm.

            :param result: The result obtained at the end of executing the variant of the 'SeqClu' algorithm.
            The result is a dictionary of the hashes of the sequences paired with the label of the sequence.
            :param algorithmName: The name of the variant of the 'SeqClu' algorithm.
            :param timeTaken: The time taken to execute the variant of the 'SeqClu' algorithm.
            :param prototypeHashes: The hashes of the prototypes obtained at the end
            of executing the variant of the 'SeqClu' algorithm.
            :return: void
        """
        print(f"[{algorithmName}] The results of the implementation of {algorithmName} are as follows.")
        print(f"[{algorithmName}] The result provided by the \'{algorithmName}\' algorithm is as follows.")
        print(result)
        print(f"[{algorithmName}] The amount of labels provided is {len(result)}.")
        seqCluResultSet = set(result.items())
        correct = len(seqCluResultSet.intersection(set(self.actualLabels.items())))
        print(f"[{algorithmName}] The amount of correct predictions is {correct}.")
        mistakes = self.fakeDataSource.dataSize - correct
        dataSize = self.fakeDataSource.dataSize
        accuracy = correct / self.fakeDataSource.dataSize
        timesCalled = self.distanceMeasure.timesCalled
        f1macro = calculate_f1_score(self.actualLabels, result, 'macro')
        f1micro = calculate_f1_score(self.actualLabels, result, 'micro')
        f1weighted = calculate_f1_score(self.actualLabels, result, 'weighted')
        print(f"[SeqClu] The algorithm made {mistakes} out "
              f"of {dataSize} mistakes.")
        print(f"[SeqClu] The amount of times the distance computation has been called is "
              f"{timesCalled}.")
        print(f"[SeqClu] the {algorithmName} algorithm took {timeTaken} seconds to complete.")
        print(f"[SeqClu] The clustering accuracy is therefore {accuracy}")
        print(f"[SeqClu] The F1 score (macro) is {f1macro}")
        print(f"[SeqClu] The F1 score (micro) is {f1micro}")
        print(f"[SeqClu] The F1 score (weighted) is {f1weighted}")
        print(f"[SeqClu] The prototype hashes are {prototypeHashes}")
        print(f"[SeqCluCSV] {timesCalled},{timeTaken},{accuracy},{f1macro},{f1micro},{f1weighted}")
        self.distanceMeasure.reset()
        self.fakeDataSource.reset()
