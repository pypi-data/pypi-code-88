#!/usr/bin/env python3

import shutil
import unittest
from pathlib import Path


class TestCaseWithTempTestDataDir(unittest.TestCase):
    def setUp(self) -> None:
        self.test_data_dir = Path(f"temp-test-data-of-{self.__class__.__name__}")
        if self.test_data_dir.is_dir():
            shutil.rmtree(self.test_data_dir, ignore_errors=True)

        shutil.copytree(
            (Path(__file__).parent / "./test-data").resolve(), self.test_data_dir
        )

        self.path_a = self.test_data_dir / "a.yaml"
        self.path_b = self.test_data_dir / "b.yaml"
        self.path_c = self.test_data_dir / "c.yaml"

    def tearDown(self) -> None:
        shutil.rmtree(self.test_data_dir, ignore_errors=True)
