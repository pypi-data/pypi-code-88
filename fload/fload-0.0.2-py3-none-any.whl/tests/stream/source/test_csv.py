import os
import unittest
from fload.stream.source.csv import CSVSource

class CSVSourceTest(unittest.TestCase):
    def test_start(self):
        csv_file = os.path.join(os.path.dirname(__file__), 'people.csv')
        target = CSVSource()
        CSVSource.csv_file = csv_file
        ret = target.start()
        ret_list = list(ret)
        self.assertEqual(3, len(ret_list))
