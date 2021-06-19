"""
    This module contains a command-line interface that can be used to run experiments on the HPC cluster.
"""
import json
import sys

from seqclupv.SeqClu import SeqClu
from seqclupv.SeqCluBaselineOnline import SeqCluBaselineOnline
from seqclupv.SeqCluBaselineOffline import SeqCluBaselineOffline
from seqclupv.library.data_generator.sine_curve_generator import CurveGenerator
from seqclupv.library.data_generator.handwritten_character_generator import HandwrittenCharacterGenerator
from seqclupv.library.data_generator.pebble_generator import GesturePebbleGenerator
from seqclupv.library.data_generator.plaid_generator import PLAIDGenerator
from seqclupv.library.data_source import FakeDataSource
from seqclupv.library.distance.dynamic_time_warping import DynamicTimeWarping
from seqclupv.library.evaluation.basic_evaluator import BasicEvaluator
from seqclupv.library.evaluation.basic_baseline_prototypes import BasicBaselinePrototypes
from seqclupv.library.heuristics.linear_prototype_value import LinearPrototypeValue


def areCurveParameters(parameters: list) -> bool:
    """
        This method verifies whether or not a list of parameters has the format of parameters that are used to
        generate a data set of sequences from a sine curve.

        :param parameters: A list of parameters for which needs to be verified whether or not it has the format of
        parameters that are used to generate a data set of sequences from a sine curve.
        :return: A boolean value indicating whether or not the given list of parameters has the format of parameters
        that are used to generate a data set of sequences from a sine curve.
    """
    if len(parameters) != 6:
        return False
    return type(parameters[0]) == int and type(parameters[1]) == float and type(parameters[2]) == float \
           and type(parameters[3]) == int and type(parameters[4]) == float and type(parameters[5]) == int


def areStringParameters(parameters: list) -> bool:
    """
        This method verifies whether or not all values in the list are strings.

        :param parameters: A list of parameters for which needs to be verified whether or not all values in it
        are strings.
        :return: A boolean value indicating whether or not all values in the given list of parameters are strings.
    """
    for parameter in parameters:
        if type(parameter) != str:
            return False
    return True


def areSeqCluParameters(parameters: list) -> bool:
    """
        This method verifies whether or not a list of parameters has the format of parameters that are used to
        configure the 'SeqClu-PV' algorithm.

        :param parameters: A list of parameters for which needs to be verified whether or not it has the format of
        parameters that are used to configure the 'SeqClu-PV' algorithm.
        :return: A boolean value indicating whether or not the given list of parameters has the format of parameters
        that are used to configure the 'SeqClu-PV' algorithm.
    """
    if len(parameters) != 5:
        return False
    return type(parameters[0]) == int and type(parameters[1]) == float \
           and type(parameters[2]) == float and type(parameters[3]) == bool and type(parameters[4]) == bool


def areTimeSeriesClassificationParameters(parameters: list) -> bool:
    """
        This method verifies whether or not a list of parameters has the format of parameters that are used to
        load a data set of sequences from data files downloaded from TimeSeriesClassification.com.

        :param parameters: A list of parameters for which needs to be verified whether or not it has the format of
        parameters that are used to load a data set of sequences from data files downloaded from
        TimeSeriesClassification.com.
        :return: A boolean value indicating whether or not the given list of parameters has the format of parameters
        that are used to load a data set of sequences from data files downloaded from TimeSeriesClassification.com.
    """
    if len(parameters) != 2:
        return False
    return type(parameters[0]) == bool and type(parameters[1]) == str


def parseBool(string: str) -> bool:
    """
        This method parses a string to a boolean.

        :param string: The string that needs to be parsed to a boolean.
        :return: The boolean equivalent of the passed string.
    """
    if string == "False":
        return False
    if string == "True":
        return True
    raise ValueError("Invalid argument passed to boolean constructor.")


def main(argv) -> None:
    """
        This method is the main method for the command-line interface of 'SeqClu-PV'. All arguments for the algorithm
        are passed via 'argv' and the algorithm is then configured and run.

        :param argv: The parameters that are required to configure the algorithm.
        :return: void
    """
    if len(argv) != 10:
        print("[SeqCluCLI] Too few or too many arguments. Shutting down.")
        return
    print(f"[SeqCluCLI] Passed arguments are {argv[1:]}.")
    numPrototypes = int(argv[1])
    numRepresentativePrototypes = int(argv[2])
    maxPerTick = int(argv[3])
    dataSourceParameters = json.loads(argv[4])
    seqCluParameters = json.loads(argv[5])
    maxIter = int(argv[6])
    online = parseBool(argv[7])
    onlySeqClu = parseBool(argv[8])
    experimentName = argv[9]
    computeDistances = not online and not onlySeqClu

    numClusters = len(dataSourceParameters)

    if type(dataSourceParameters) != list:
        raise ValueError("Data source parameters must be stored in a list.")
    if len(dataSourceParameters) == 0:
        raise ValueError("Data source parameters cannot be empty.")

    if type(seqCluParameters) != list:
        raise ValueError("SeqClu parameters must be stored in a list.")
    if len(seqCluParameters) == 0:
        seqClu = False
    elif areSeqCluParameters(seqCluParameters):
        seqClu = True
    else:
        raise ValueError("SeqClu parameters are not in the right format.")

    # 'areStringParameters' can be interpreted as 'areHandwrittenParameters'.
    if areStringParameters(dataSourceParameters):
        classes = dataSourceParameters
        dataGenerator = HandwrittenCharacterGenerator(classes, numPrototypes, computeDistances)
        fakeDataSource = FakeDataSource(maxPerTick, [dataGenerator], numPrototypes, classes)
    elif areTimeSeriesClassificationParameters(dataSourceParameters):
        computeDistribution = dataSourceParameters[0]
        dataSetName = dataSourceParameters[1]
        if dataSetName == "pebble":
            dataGenerator = GesturePebbleGenerator(numPrototypes, computeDistribution)
        elif dataSetName == "plaid":
            dataGenerator = PLAIDGenerator(numPrototypes, computeDistribution)
        else:
            raise ValueError("Invalid data set name provided.")
        dataGenerator.generateData()
        numClusters = len(dataGenerator.classes)
        fakeDataSource = FakeDataSource(maxPerTick, [dataGenerator], numPrototypes, dataGenerator.classes)
    elif all(areCurveParameters(elem) for elem in dataSourceParameters):
        dataGenerators = []
        for parameters in dataSourceParameters:
            dataGenerators.append(CurveGenerator(parameters[0], (parameters[1], parameters[2]),
                                                 parameters[3], parameters[4], parameters[5], numPrototypes,
                                                 computeDistances))
        classes = list(range(numClusters))
        fakeDataSource = FakeDataSource(maxPerTick, dataGenerators, numPrototypes, classes)
    else:
        raise ValueError("Data source parameters are not handwritten character or curve generator parameters.")

    if fakeDataSource.data is None:
        fakeDataSource.generateData()
    labels = fakeDataSource.labels
    print("[SeqCluCLI] Labels provided by data set are as follows.")
    print(labels)
    print("[SeqCluCLI] Labels including sequence hashes provided by fake data source are as follows.")
    print(fakeDataSource.actualLabels)

    distanceMeasure = DynamicTimeWarping()

    if seqClu:
        bufferSize = int(seqCluParameters[0])
        minimumRepresentativeness = float(seqCluParameters[1])
        prototypeScale = float(seqCluParameters[2])
        clusterAssignment = bool(seqCluParameters[3])
        buffering = bool(seqCluParameters[4])

        prototypeValue = LinearPrototypeValue(prototypeScale)
        seqClu = SeqClu(fakeDataSource, distanceMeasure, numClusters, numRepresentativePrototypes, numPrototypes,
                        bufferSize, minimumRepresentativeness, prototypeValue,
                        clusterAssignment, buffering)
    else:
        seqClu = None

    if not onlySeqClu:
        if online:
            seqCluBaselineOnline = SeqCluBaselineOnline(fakeDataSource, distanceMeasure, numClusters, numPrototypes)
            seqCluBaselineOffline = None
        else:
            seqCluBaselineOnline = None
            seqCluBaselineOffline = SeqCluBaselineOffline(fakeDataSource, distanceMeasure,
                                                          numClusters, numPrototypes, maxIter)
    else:
        seqCluBaselineOnline = None
        seqCluBaselineOffline = None
    BasicEvaluator(fakeDataSource, distanceMeasure, seqClu, seqCluBaselineOnline,
                   seqCluBaselineOffline, BasicBaselinePrototypes.getPrototypes(experimentName)).evaluate()


if __name__ == "__main__":
    main(sys.argv)
