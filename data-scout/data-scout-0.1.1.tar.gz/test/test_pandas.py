import unittest

from data_scout.executor import PandasExecutor, CodeExecutor
from data_scout.scout import Scout


class TestPandas(unittest.TestCase):
    """
    Test the Pandas transformations.
    """

    def setUp(self) -> None:
        """
        Set up required parts.
        :return:
        """
        self.scout = Scout()
        self.executor = PandasExecutor({"source": "CSV", "kwargs": {
            "filename": "test/data/test.csv",
            "delimiter": ",",
            "encoding": "utf-8",
            "has_header": True
        }}, [{"transformation": "data-convert", "kwargs": {"field": "column1", "to": "int"}}], self.scout)

    def test_to_int(self) -> None:
        """
        Test if column 1 is indeed of data type int
        :return:
        """
        data, _ = self.executor()
        self.assertIsInstance(data[0]["column1"], int)


if __name__ == "__main__":
    test = TestPandas()
    test.setUp()
    test.test_to_int()
