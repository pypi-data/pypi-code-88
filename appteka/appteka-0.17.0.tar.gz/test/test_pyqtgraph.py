import unittest
import warnings


class TestImport(unittest.TestCase):
    def test_phasor(self):
        with warnings.catch_warnings(record=True):
            warnings.simplefilter("always")
            from appteka.pyqtgraph.phasor import PhasorDiagram
            from appteka.pyqtgraph.phasor import PhasorDiagramUI

    def test_wavefrom(self):
        with warnings.catch_warnings(record=True):
            warnings.simplefilter("always")
            from appteka.pyqtgraph.waveform import TimeStampAxisItem
            from appteka.pyqtgraph.waveform import Waveform
            from appteka.pyqtgraph.waveform import MultiWaveform
