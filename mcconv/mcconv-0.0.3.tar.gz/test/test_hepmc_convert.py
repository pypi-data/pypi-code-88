from mcconv import GenericTextReader, UnparsedTextEvent, hepmc_write

import os
import unittest
from mcconv import detect_mc_type, McFileTypes



class TestGenericTextReader(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def _data_path(self, file_name):
        """Gets data file path"""
        dir_path = os.path.dirname(os.path.realpath(__file__))
        return os.path.join(dir_path, 'data', file_name)

    def _tmp_path(self, file_name):
        """Gets output temporary file path"""

        return os.path.join(os.path.dirname(os.path.realpath(__file__)), 'tmp', file_name)

    def test_convert_file(self):
        """Test detecting BeaGLE file type"""

        hepmc_write(self._data_path('gemc-lund.3evt.txt'),
                    self._tmp_path('tmp/lund-convert.hepmc'),
                    McFileTypes.PYTHIA_GEMC, "hepmc3")
