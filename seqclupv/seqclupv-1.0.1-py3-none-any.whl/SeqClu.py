"""
    This class can be used to process a stream of data in a separate thread while some other thread performs work.
    The data stream is clustered using the 'SeqClu' algorithm and the labels of items that have already been seen can
    be requested real-time.
"""

from copy import deepcopy
from typing import Dict, List, Optional, Set, Tuple, Union

import numpy as np
from numpy import ndarray

from seqclupv.library.interfaces.data_source import IDataSource
from seqclupv.library.interfaces.distance_measure import IDistanceMeasure
from seqclupv.library.interfaces.heuristics.prototype_value import IPrototypeValue
from seqclupv.library.interfaces.seqclu import ISeqClu
from seqclupv.library.storage.candidates import CandidateStore
from seqclupv.library.storage.cluster import ClusterStore
from seqclupv.library.storage.sequences import SequenceStore
from seqclupv.library.utilities.hash_sequence import hashSequence


class SeqClu(ISeqClu):

    # STATIC METHODS #

    @staticmethod
    def assignToCluster(clusters: List[ClusterStore], sequence: Tuple[Optional[str], Optional[ndarray]],
                        distances: List[Tuple[int, float, float]], clusterAssignment: bool) -> Tuple[int, bool]:
        """
            This method assigns a sequence to one of the provided clusters using a dictionary of pair-wise distances.

            :param clusters: The clusters that the sequence can be assigned to.
            :param sequence: The sequence that needs to be assigned to one of the clusters.
            :param distances: The pair-wise distances stored in a dictionary identified by a tuple of prototype hashes
            that identify the two prototypes.
            :param clusterAssignment: A boolean value indicating whether or not to approximate the distance to the
            cluster.
            :return: A tuple containing the index of the cluster that the sequence was assigned to and a boolean value
            indicating whether or not the distances used to make the cluster assignment decision were approximated.
        """
        distances.sort(key=lambda x: x[1])
        if not clusterAssignment:
            return distances[0][0], False
        assignedClusterIdx, distance, error = distances[0]
        result: Set[int] = set([])
        result.add(assignedClusterIdx)
        for i in range(1, len(distances)):
            otherClusterIdx, otherDistance, otherError = distances[i]
            if SeqClu.isAmbiguous((distance, error), (otherDistance, otherError)):
                result.add(otherClusterIdx)
        if len(result) == 1:
            return assignedClusterIdx, True
        ambiguousClusters = list(map(lambda x: clusters[x], list(result)))
        return SeqClu.assignToClusterAccurate(ambiguousClusters, sequence), False

    @staticmethod
    def assignToClusterAccurate(clusters: List[ClusterStore], sequence: Tuple[Optional[str], Optional[ndarray]]) -> int:
        """
            This method assigns a sequence to one of the provided clusters using accurate distances.

            :param clusters: The clusters that the sequence can be assigned to.
            :param sequence: The sequence that needs to be assigned to one of the clusters.
            :return: The index of the cluster that the sequence was assigned to.
        """
        label = -1
        minDistance = np.inf
        for cluster in clusters:
            distance = cluster.sumOfDistancesOf(sequence, False)
            if distance < minDistance:
                label = cluster.identifier
                minDistance = distance
        return label

    @staticmethod
    def computeDistanceToClusters(clusters: List[ClusterStore], sequence: Tuple[Optional[str], Optional[ndarray]],
                                  clusterAssignment: bool) -> List[Tuple[int, float, float]]:
        """
            This method computes the distance of a sequence to all clusters.

            :param clusters: The clusters for which the distance to the sequence needs to be computed.
            :param sequence: The sequence for which the distance to the clusters needs to be computed.
            :param clusterAssignment: A boolean value indicating whether or not to approximate the distance to the
            cluster.
            :return: A list of tuples containing the index of a cluster, the computed distance and the error made in
            this computation. For accurate distances, this error is 0.
        """
        result: List[Tuple[int, float, float]] = []
        for cluster in clusters:
            assert cluster.prototypes.fullyInitialized
            distance = cluster.computeAverageDistance(sequence, clusterAssignment)
            if clusterAssignment:
                error = cluster.error
            else:
                error = 0
            result.append((cluster.identifier, distance, error))
        return result

    @staticmethod
    def determineCandidacy(candidates: CandidateStore,
                           clusters: List[ClusterStore],
                           sequence: Tuple[Optional[str], Optional[ndarray]],
                           minimumRepresentativeness: float,
                           clusterAssignment: bool) \
            -> Tuple[List[Tuple[int, float, float]], Set[int]]:
        """
            This method determines for which clusters a given sequence is a candidate.

            :param candidates: The buffer of candidate prototypes.
            :param clusters: The clusters that the given sequence could become a prototype for.
            :param sequence: The sequence for which needs to be determined whether or not it is a candidate to become
            a prototype for the clusters.
            :param minimumRepresentativeness: The minimum representativeness that the prototypes should have in order
            for approximation of the distance to the cluster to be used. If the prototypes are not representative
            enough, the accurate distance to the cluster is computed instead.
            :param clusterAssignment: A boolean value indicating whether or not to approximate the distance to the
            cluster.
            :return: A tuple containing a list of tuples that each contain the index of some cluster, the computed
            distance and the error made in this computation, as well as the indices of the clusters that the sequence
            is a candidate for.
        """
        # This function returns a list of tuples containing the cluster identifier, an approximation of the average
        # distance from the incoming sequence to the cluster and the upper bound of the error of the approximation.
        result: List[Tuple[int, float, float]] = []
        candidateFor = set([])
        sequenceHash, _ = sequence
        for cluster in clusters:
            assert cluster.prototypes.fullyInitialized
            distance, candidacy, isApproximation = cluster.isCandidate(sequence, minimumRepresentativeness,
                                                                       clusterAssignment)
            if isApproximation:
                error = cluster.error
            else:
                error = 0
            result.append((cluster.identifier, distance, error))
            if sequenceHash in cluster.prototypes.prototypes or sequenceHash in candidates.candidates:
                continue
            if candidacy:
                candidateFor.add(cluster.identifier)
        return result, candidateFor

    @staticmethod
    def initializeClusters(numClusters: int, numRepresentativePrototypes: int,
                           numPrototypes: int, distanceMeasure: IDistanceMeasure,
                           tick: int) -> List[ClusterStore]:
        """
            This method initializes the clusters that are used in the algorithm.

            :param numClusters: The number of clusters that need to be initialized.
            :param numRepresentativePrototypes: The number of representative prototypes each cluster needs to have.
            :param numPrototypes: The number of prototypes each cluster needs to have.
            :param distanceMeasure: The distance measure that is used in the algorithm.
            :param tick: The tick at which the clusters are initialized.
            :return: The resulting list of initialized clusters.
        """
        result: List[ClusterStore] = []
        for identifier in range(numClusters):
            result.append(ClusterStore(identifier, numRepresentativePrototypes, numPrototypes, distanceMeasure, tick))
        return result

    @staticmethod
    def isAmbiguous(distanceAndErrorOne: Tuple[float, float],
                    distanceAndErrorTwo: Tuple[float, float]) -> bool:
        """
            This method determines whether or not two computed distances given their errors are relatively too close
            to each other and are therefore ambiguous.

            :param distanceAndErrorOne: The distance and error that resulted from some distance computation.
            :param distanceAndErrorTwo: The distance and error that resulted from another distance computation.
            :return: A boolean value indicating whether or not the pair of distance computations is ambiguous.
        """
        distanceOne, errorOne = distanceAndErrorOne
        distanceTwo, errorTwo = distanceAndErrorTwo
        difference = abs(distanceOne - distanceTwo)
        return difference <= max(errorOne, errorTwo)

    @staticmethod
    def processCandidatesForCluster(cluster: ClusterStore, candidates: List[Tuple[str, ndarray]],
                                    numPrototypes: int, numRepresentativePrototypes: int,
                                    prototypeValue: IPrototypeValue, tick: int) -> Set[str]:
        """
            This method processes the candidate prototypes for a given cluster. The method decides whether or not
            the candidates are actually of high enough quality to become a prototype and if so, promotes these
            sequences to prototypes.

            :param cluster: The cluster for which the candidate prototypes should be processed.
            :param candidates: The candidate prototypes that should be processed.
            :param numPrototypes: The number of prototypes of all clusters.
            :param numRepresentativePrototypes: The number of representative prototypes of all clusters.
            :param prototypeValue: The heuristic function that is used to compute the value of a prototype.
            :param tick: The tick at which the candidate prototypes were processed.
            :return: The hashes of the prototypes that were discarded after processing all candidate prototypes.
        """
        prototypeValues: List[Tuple[Union[int, str], float]] = []
        prototypes = cluster.prototypes.prototypes

        # This set of statements should calculate the pair-wise distances between candidates and current prototypes.
        for i, candidate in enumerate(candidates):
            representativeness = cluster.representativenessOfSequence(candidate)
            prototypeValues.append((i, prototypeValue.evaluate(representativeness, 0)))

        # This set of statements should calculate the pair-wise distances between prototypes and prototypes.
        for (prototypeHash, prototype) in prototypes.items():
            representativeness = cluster.representativenessOfSequence((prototypeHash, prototype))
            weight = cluster.prototypeFrequencies.getWeight(prototypeHash)
            prototypeValues.append((prototypeHash, prototypeValue.evaluate(representativeness, weight)))

        # Sort the list to retrieve the p most representative prototypes from the set of candidateStore and prototypes.
        prototypeValues.sort(key=lambda x: x[1])

        newPrototypes: Dict[str, ndarray] = dict(
            list(map(lambda x: candidates[x[0]] if type(x[0]) == int else (x[0], prototypes[x[0]]),
                     prototypeValues[-numPrototypes:])))
        newRepresentativePrototypeHashes: Set[str] = set(map(lambda x: candidates[x[0]][0] if type(x[0]
                                                                                                   ) == int else x[0],
                                                             prototypeValues[-numRepresentativePrototypes:]))
        newOtherPrototypeHashes: Set[str] = set(map(lambda x: candidates[x[0]][0] if type(x[0]) == int else x[0],
                                                    prototypeValues[-numPrototypes:
                                                                    -numRepresentativePrototypes]))
        return cluster.updatePrototypes(newPrototypes, newOtherPrototypeHashes,
                                        newRepresentativePrototypeHashes, tick)

    # PROPERTIES #

    @property
    def bufferedSequences(self) -> Set[str]:
        """
            This property stores the sequences that were buffered by the algorithm.

            :return: The set of sequences that were buffered by the algorithm.
        """
        return self._bufferedSequences

    @property
    def buffering(self) -> bool:
        """
            This property stores a boolean value indicating whether or not the buffering feature is enabled.

            :return: A boolean value indicating whether or not the buffering feature is enabled.
        """
        return self._buffering

    @property
    def bufferFull(self) -> bool:
        """
            This method is a property that returns a boolean indicating whether or not the set of candidateStore has
            reached the maximum allowed size and is therefore full.

            :return: A boolean indicating whether or not the set of candidateStore has reached
            the maximum allowed size and is therefore full.
        """
        return len(self.candidateStore.candidates) + len(self.sequenceStore.sequences) >= self.bufferSize

    @property
    def bufferSize(self) -> int:
        """
            This method is a property that returns the maximum size of the buffer of candidateStore and ambiguous
            sequenceStore.

            :return: The maximum size of the buffer of candidateStore and ambiguous sequenceStore.
        """
        return self._bufferSize

    @property
    def candidateStore(self) -> CandidateStore:
        """
            This property stores the buffer of candidate prototypes.

            :return: The buffer of candidate prototypes.
        """
        return self._candidates

    @property
    def classes(self) -> List[Union[chr, int]]:
        """
            Tis property stores the classes that are present in the data set that is processed by the algorithm.

            :return: The classes that are present in the data set that is processed by the algorithm.
        """
        return self._classes

    @property
    def clusterAssignment(self) -> bool:
        """
            This property stores a boolean value indicating whether or not approximation of the distance to clusters
            is enabled in the algorithm.

            :return: A boolean value indicating whether or not approximation of the distance to clusters
            is enabled in the algorithm.
        """
        return self._clusterAssignment

    @property
    def clusteredByApproximation(self) -> Set[str]:
        """
            This property stores the sequences that were clustered by approximation by the algorithm.

            :return: The set of sequences that were clustered by approximation by the algorithm.
        """
        return self._clusteredByApproximation

    @property
    def clusters(self) -> List[ClusterStore]:
        """
            This property stores the clusters that the algorithm needs to work with.

            :return: The clusters that the algorithm needs to work with.
        """
        return self._clusters

    @property
    def finalLabels(self) -> Dict[str, int]:
        """
            This property stores the correct labels as a dictionary where the keys are the hashes of the sequences
            and the values are the correct labels.

            :return: The correct labels as a dictionary where the keys are the hashes of the sequences
            and the values are the correct labels.
        """
        labelsCopied = self.labels.copy()
        for cluster in self.clusters:
            for prototypeHash in cluster.prototypes.prototypes:
                labelsCopied[prototypeHash] = self.classes[cluster.identifier]
        return labelsCopied

    @property
    def fullyInitialized(self) -> bool:
        """
            This property stores a boolean value indicating whether or not the prototypes of all clusters are fully
            initialized.

            :return: A boolean value indicating whether or not the prototypes of all clusters are fully
            initialized.
        """
        for cluster in self.clusters:
            if not cluster.prototypes.fullyInitialized:
                return False
        return True

    @property
    def labels(self) -> Dict[str, int]:
        """
            This property stores the predicted labels of all sequences except for those that are prototypes.

            :return: The predicted labels of all sequences except for those that are prototypes.
        """
        return self._labels

    @property
    def minimumRepresentativeness(self) -> float:
        """
            This property stores the minimum representativeness that the prototypes should have in order
            for approximation of the distance to the cluster to be used. If the prototypes are not representative
            enough, the accurate distance to the cluster is computed instead.

            :return: The minimum representativeness that the prototypes should have in order
            for approximation of the distance to the cluster to be used. If the prototypes are not representative
            enough, the accurate distance to the cluster is computed instead.
        """
        assert 0 <= self._minimumRepresentativeness <= 1
        return self._minimumRepresentativeness

    @property
    def numFullyProcessed(self) -> int:
        """
            This property stores the number of sequences that were fully processed by the algorithm.

            :return: An integer representing the number of sequences that were fully processed by the algorithm.
        """
        return self._numFullyProcessed

    @property
    def numRepresentativePrototypes(self) -> int:
        """
            This property stores the number of representative prototypes of all clusters that are used by the algorithm.

            :return: An integer representing the number of representative prototypes
            of all clusters that are used by the algorithm.
        """
        return self._numRepresentativePrototypes

    @property
    def prototypeValueHeuristic(self) -> IPrototypeValue:
        """
            This property stores the heuristic function that is used to compute the value of a prototype.

            :return: The heuristic function that is used to compute the value of a prototype.
        """
        return self._prototypeValueHeuristic

    @property
    def sequenceStore(self) -> SequenceStore:
        """
            This property stores the buffer of sequences that is currently not used in the algorithm, but could be used
            in the future to store sequences that are likely to be assigned incorrectly.

            :return: The buffer of sequences that is currently not used in the algorithm, but could be used
            in the future to store sequences that are likely to be assigned incorrectly.
        """
        return self._sequences

    # CONSTRUCTOR #

    def __init__(self, dataSource: IDataSource, distanceMeasure: IDistanceMeasure,
                 numClusters: int, numRepresentativePrototypes: int, numPrototypes: int,
                 bufferSize: int, minimumRepresentativeness: float, prototypeValueHeuristic: IPrototypeValue,
                 clusterAssignment: bool, buffering: bool) -> None:
        """
            This method initializes the 'SeqClu' algorithm with a data source, distance measure, number of clusters
            and number of prototypes.

            :param dataSource: The data source that should be used in the 'SeqClu' algorithm.
            :param distanceMeasure: The distance measure that should be used in the 'SeqClu' algorithm.
            :param numClusters: The number of clusters that should be used in the 'SeqClu' algorithm.
            :param numRepresentativePrototypes: The number of representative prototypes.
            :param numPrototypes: The number of prototypes that should be used in the 'SeqClu' algorithm.'
            :param bufferSize: The maximum size of the buffer.
            :param minimumRepresentativeness: The minimum representativeness that the prototypes should have in order
            for approximation of the distance to the cluster to be used. If the prototypes are not representative
            enough, the accurate distance to the cluster is computed instead.
            :param prototypeValueHeuristic: The heuristic function that is used to compute the value of a prototype.
            :param clusterAssignment: A boolean value indicating whether or not to approximate the distance to the
            cluster.
            :param buffering: A boolean value indicating whether or not the buffering feature should be used.
            :return: void
        """
        super().__init__(dataSource, distanceMeasure, numClusters, numPrototypes)
        self._bufferedSequences = set([])
        self._buffering = buffering
        self._bufferSize = bufferSize
        self._candidates = CandidateStore(numRepresentativePrototypes, numPrototypes, -1)
        self._classes = dataSource.classes
        self._clusterAssignment = clusterAssignment
        self._clusteredByApproximation = set([])
        self._sequences = SequenceStore(-1)
        self._clusters = SeqClu.initializeClusters(numClusters, numRepresentativePrototypes, numPrototypes,
                                                   distanceMeasure, -1)
        self._labels = {}
        self._minimumRepresentativeness = minimumRepresentativeness
        self._numClusters = numClusters
        self._numFullyProcessed = 0
        self._numPrototypes = numPrototypes
        self._numRepresentativePrototypes = numRepresentativePrototypes
        self._prototypeValueHeuristic = prototypeValueHeuristic

    # PUBLIC METHODS #

    def alreadyProcessed(self, sequenceHash: str) -> bool:
        """
            This method determines if a sequence, identified by its hash, was already processed in the past.

            :param sequenceHash: The hash of the sequence for which needs to be determined whether or not it was already
            processed in the past.
            :return: A boolean value indicating whether or not the sequence was already processed in the past.
        """
        # Check if the sequence is already stored as a prototype of any of the clusters or as a candidate.
        for cluster in self.clusters:
            if sequenceHash in cluster.prototypes.prototypes:
                return True
        return sequenceHash in self.candidateStore.candidates

    def execute(self) -> None:
        """
            This method executes the 'SeqClu' algorithm from start to finish. The main loop over the data is
            implemented in here.

            :return: void
        """
        iteration = 0
        while not self.finish:
            iteration += 1
            print(f"[SeqClu] Iteration {iteration}.")
            finish = self._advanceTick()
            if finish:
                print("[SeqClu] The algorithm finished executing. Processing the buffer and returning...")
                break
        if self.buffering:
            # This if statement should not be necessary due to the nature of this function assuming the buffer is empty.
            self.forceProcessBuffer(True, self.tick)

    def forceProcessBuffer(self, persist: bool, tick: int) -> List[ClusterStore]:
        """
            This method forcefully processes the buffer of candidate prototypes. The buffer is then empty again and can
            fill up over time in the ticks that are to come.

            :param persist: A boolean value indicating whether or not to persist this action. If this value is set to
            false, the resulting list of clusters is returned, but all other data structures remain the same as before
            executing this method.
            :param tick: The tick at which the buffer is forcefully processed.
            :return: The clusters that are obtained after forcefully processing the buffer.
        """
        # This function forcefully empties the candidateStore and assigns all sequenceStore in it to a cluster.
        if persist:
            clusters = self.clusters
            candidates = self.candidateStore
        else:
            clusters = deepcopy(self.clusters)
            candidates = deepcopy(self.candidateStore)

        self._processCandidates(clusters, candidates, self.numClusters, self.numPrototypes,
                                self.numRepresentativePrototypes, tick)

        return clusters

    def processSequence(self, sequence: Tuple[str, ndarray], considerCandidacy: bool) -> None:
        """
            This method processes one sequence of the data set that is processed in the 'SeqClu' algorithm.

            :param sequence: The sequence that should be processed in the 'SeqClu' algorithm.
            :param considerCandidacy: A boolean value indicating whether or not the algorithm should consider if the
            sequence could be a prototype for any of the clusters.
            :return: void
        """
        if self.alreadyProcessed(sequence[0]):
            return
        if not self.fullyInitialized:
            for cluster in self.clusters:
                if not cluster.prototypes.fullyInitialized:
                    if not cluster.prototypes.representativePrototypesInitialized:
                        cluster.prototypes.addPrototype(sequence, True, self.tick, None)
                        cluster.prototypeFrequencies.initializePrototype(sequence[0])
                        return
                    else:
                        cluster.prototypes.addPrototype(sequence, False, self.tick, None)
                        cluster.prototypeFrequencies.initializePrototype(sequence[0])
                        return
        else:
            if considerCandidacy:
                averageDistances, candidateFor = SeqClu.determineCandidacy(self.candidateStore,
                                                                           self.clusters, sequence,
                                                                           self.minimumRepresentativeness,
                                                                           self.clusterAssignment)
                print(f"[SeqClu] Candidacy determined {list(candidateFor)}.")

                # If the incoming sequence is a candidate for any of the clusters, add the sequence to the buffer of candidateStore.
                if len(candidateFor) > 0:
                    if self.buffering:
                        sequenceHash, sequenceData = sequence
                        if sequenceHash is None:
                            sequenceHash = hashSequence(sequenceData)
                        self.bufferedSequences.add(sequenceHash)
                    self.candidateStore.addToCandidates(sequence, candidateFor, self.tick)
                    if self.bufferFull or not self.buffering:
                        print(f"[SeqClu] Forcefully emptying buffer...")
                        self.forceProcessBuffer(True, self.tick)
                    return
            else:
                averageDistances = SeqClu.computeDistanceToClusters(self.clusters, sequence, self.clusterAssignment)

            self._labelSequence(self.clusters, sequence, averageDistances)

    # PRIVATE METHODS #

    def _labelSequence(self, clusters: List[ClusterStore], sequence: Tuple[Optional[str], Optional[ndarray]],
                       averageDistances: List[Tuple[int, float, float]]) -> None:
        """
            This method labels a sequence based on the information that is available.

            :param clusters: The clusters at the given tick.
            :param sequence: The sequence that needs to be labeled.
            :param averageDistances: The average distance from the sequence to all clusters, represented as a list of
            tuples containing the index of some cluster, the average distance to that cluster and the error made in the
            distance computation for that cluster.
            :return: void
        """
        sequenceHash, sequenceData = sequence
        assignedCluster, byApproximation = SeqClu.assignToCluster(clusters, sequence,
                                                                  averageDistances, self.clusterAssignment)
        if byApproximation:
            if sequenceHash is None:
                sequenceHash = hashSequence(sequenceData)
            self.clusteredByApproximation.add(sequenceHash)
        self.labels[sequenceHash] = self.classes[assignedCluster]
        # TODO: Shouldn't this be called for all cluster instances?
        self.clusters[assignedCluster].processSequenceIndefinitely(sequenceHash)
        self._numFullyProcessed += 1

    def _processCandidates(self, clusters: List[ClusterStore], candidateStore: CandidateStore, numClusters: int,
                           numPrototypes: int, numRepresentativePrototypes: int, tick: int) -> None:
        """
            This method processes all the candidate prototypes in the buffer of candidate prototypes. This method is
            called when the buffer is forcefully processed.

            :param clusters: The clusters at the given tick.
            :param candidateStore: The buffer of candidate prototypes at the given tick.
            :param numClusters: The number of clusters that should be used in the 'SeqClu' algorithm.
            :param numPrototypes: The number of prototypes that should be used in the 'SeqClu' algorithm.
            :param numRepresentativePrototypes: The number of representative prototypes that should be used in the
            'SeqClu' algorithm.
            :param tick: The tick at which the buffer is forcefully processed.
            :return: The clusters that are obtained after forcefully processing the buffer.
        """
        for clusterIdx in range(numClusters):
            candidatesForCluster: List[Tuple[str, ndarray]] = list(map(lambda item: (item[0], item[1][0]),
                                                                       filter(lambda item: clusterIdx in item[1][1],
                                                                              candidateStore.candidates.items())))
            if len(candidatesForCluster) > 0:
                removedPrototypeHashes = SeqClu.processCandidatesForCluster(clusters[clusterIdx], candidatesForCluster,
                                                                            numPrototypes, numRepresentativePrototypes,
                                                                            self.prototypeValueHeuristic, tick)
                # Assumption that the removed prototype is still assigned to the cluster.
                for removedPrototypeHash in removedPrototypeHashes:
                    self.labels[removedPrototypeHash] = self.classes[clusterIdx]
                # TODO: Break should be added here, first fix and then verify if the performance remains the same.
        # All candidates have been processed, therefore we should empty the buffer.
        for candidateHash in list(candidateStore.candidates.keys()):
            isCandidate = False
            for cluster in clusters:
                # We assume here that candidates are never assigned to two clusters. TODO: Maybe ensure this?
                if candidateHash in cluster.prototypes.prototypes:
                    self.labels[candidateHash] = self.classes[cluster.identifier]
                    isCandidate = True
                    break
            if not isCandidate:
                candidate = (candidateHash, candidateStore.candidates[candidateHash][0])
                averageDistances = SeqClu.computeDistanceToClusters(clusters, candidate, self.clusterAssignment)
                self._labelSequence(clusters, candidate, averageDistances)
            candidateStore.removeFromCandidates(candidateHash)
