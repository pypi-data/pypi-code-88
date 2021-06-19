"""
    This module contains the class that stores the prototypes of some baseline. This class can be used
    to compare the prototypes obtained at the end of the online 'Seqclu' algorithm, where the number of identical
    prototypes divided by the total number of prototypes can be used as evaluation metric.
"""

from typing import List, Optional

from seqclupv.library.interfaces.baseline_prototypes import IBaselinePrototypes


class BasicBaselinePrototypes(IBaselinePrototypes):

    @staticmethod
    def getPrototypes(experimentName: str) -> Optional[List[List[str]]]:
        """
            This method returns the prototypes that were obtained after executing some baseline algorithm.
            These prototypes can be compared to the prototypes obtained at the end of the online 'SeqClu' algorithm,
            where the number of identical prototypes divided by the total number of prototypes
            can be used as evaluation metric.

            :param experimentName: The name of the experiment for which the prototypes need to be retrieved.
            :return: The prototypes obtained after executing some experiment identified by the experiment name.
        """
        if experimentName == "o29":
            return [['6756bc76', 'c64b021a', '5ac133ba', '7420af12', 'ff24fe7c', '2a64efc4', '6756bc76', '9c479a03'],
                    ['24acc8e9', '93a1ddc9', '482fed89', '89234e21', '482fed89', '76c30e17', '472b7fc1', '1332e09f'],
                    ['f418fa11', '4ccb3dd9', 'fa61df8d', '8ac4d5be', '69a451fd', '0dd66cc3', '69a451fd', '52eafac6']]
        if experimentName == "plaid":
            return None
        if experimentName == "pebbleTrain":
            return [['98c4a0e6', '237257d8', '4a9bf0ec', 'b81e204e', 'c456b122', '9fb22e3e'],
                    ['cfad21a6', 'fb45fb48', '930a101b', 'ce12103c', 'fff19865', '71ac95d0'],
                    ['1acf5df8', '98ebccea', '96dc73ce', '217f530d', '84ea0475', '8ba68fda'],
                    ['6b15001d', 'ac6f77f6', '93dcdf97', '638bb9d1', '2d0a0851', '6b50cf7b'],
                    ['fefa5265', '91a94be5', 'ee3b07c1', 'fa18a9a2', '00687b90', '2fba8027'],
                    ['c5b27ba8', '96b7bca0', 'a321ebc1', '59fed255', 'd725f213', '34a33aae']]
        if experimentName == "pebbleFull":
            return [['98ebccea', '2b4dcbd7', '96dc73ce', '0e6736c8', '84ea0475', '8ba68fda', '1acf5df8', '2b8eddc3'],
                    ['55ec131f', 'fb45fb48', 'eb219134', '03e1ae20', 'd524d948', '7db3fc75', '71ac95d0', 'cfad21a6'],
                    ['66f79f6b', '37b9d58e', '9497aaca', 'b81e204e', 'edf82d6b', 'ef47c484', 'ce0adac4', '886b30b1'],
                    ['6b15001d', 'ac6f77f6', '93dcdf97', '4f4bef57', '8211b5a0', '6cc481dc', '390acf90', 'af4c46ee'],
                    ['c794f77a', '2d21381c', 'f2b940ba', 'c4fc00b2', '919ee3a0', '54051a09', '4ea28372', 'c7b67231'],
                    ['3ee65e8f', '34107bcd', '8a5d1fe9', '6b50888c', 'c607d911', 'b92298a7', 'fa18a9a2', '906d7bc4']]
        if experimentName == "o295w":
            return [['6756bc76', 'ff24fe7c', '5ac133ba', '7420af12', '7e1a26ed', '2a64efc4', '9c479a03', 'c64b021a'],
                    ['482fed89', '7b8a937e', '76c30e17', '472b7fc1', '1a525726', '24acc8e9', '1332e09f', '93a1ddc9'],
                    ['69a451fd', '2e06ec79', '52eafac6', '6e6e22ef', 'fa61df8d', '4ccb3dd9', 'dfec2275', '0dd66cc3'],
                    ['8ac4d5be', '6b2cde41', '2ef44daf', '3ead38b7', '3f0aa84b', '0b371e7d', 'ba6e7c4a', 'f418fa11'],
                    ['89a684ef', '78ae25b3', '7a2e4832', '449dbb2e', '4f8ec214', '7c4cd0d9', '4cd6f30f', '349725c2']]
        if experimentName == "charFull":
            return None
        return None
