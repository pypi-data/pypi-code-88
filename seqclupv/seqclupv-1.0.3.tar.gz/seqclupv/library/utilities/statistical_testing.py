"""
    This module contains a command-line interface for carrying out a statistical test on two provided samples of data.
    The function to carry out a statistical test on two provided samples is contained in this module as well.
"""

import json
import sys
from typing import List

from numpy import ndarray
from scipy.stats import wilcoxon, mannwhitneyu


def statistical_test(sampleOne: ndarray, sampleTwo: ndarray, testName: str) -> None:
    """
        This method carries out some statistical test, identified by its name, on two given samples.

        :param sampleOne: The first sample that should be used in the statistical test.
        :param sampleTwo: The second sample that should be used in the statistical test.
        :param testName: The name of the statistical test that should be used.
        :return: void
    """
    if testName == "wilcoxon":
        _, p = wilcoxon(sampleOne, sampleTwo)
    elif testName == "mannwhitneyu":
        _, p = mannwhitneyu(sampleOne, sampleTwo)
    else:
        raise ValueError("[StatTestCLI] Invalid test name provided.")

    if p > 0.05:
        print(f"[StatTestCLI] H0: There is no significant difference (p-value {p}).")
    else:
        print(f"[StatTestCLI] H1: There is a significant difference (p-value {p}).")


def main(argv: List[str]) -> None:
    """
        This method is the command-line interface for the statistical test program.

        :param argv: The arguments that are passed to the statistical test program.
        :return: void
    """
    if len(argv) != 4:
        print("[StatTestCLI] Too few or too many arguments. Shutting down.")
        return
    samplesOne = json.loads(argv[1])
    samplesTwo = json.loads(argv[2])
    test = argv[3]

    for sampleOne, sampleTwo in zip(samplesOne, samplesTwo):
        statistical_test(sampleOne, sampleTwo, test)


if __name__ == "__main__":
    main(sys.argv)
