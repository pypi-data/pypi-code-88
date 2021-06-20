#!/usr/bin/env python3


from tests.base_test_case import TestCaseWithTempTestDataDir
from ymlconf import common


class TestCommon(TestCaseWithTempTestDataDir):
    def test_dump_and_load_list(self):
        data = [1, 2, 3]

        filename = self.test_data_dir / "list_data.yaml"

        common.dump_yaml(data, filename)

        reload_data = common.load_yaml(filename)

        assert isinstance(reload_data, list)

    def test_dump_and_load_tuple(self):
        data = (1, 2, 3)

        filename = self.test_data_dir / "tuple_data.yaml"

        common.dump_yaml(data, filename)

        reload_data = common.load_yaml(filename)

        assert isinstance(reload_data, list)

    def test_dump_and_load_dict_tuple(self):
        data = {"tuple": (1, 2, 3)}

        filename = self.test_data_dir / "dict_tuple_data.yaml"

        common.dump_yaml(data, filename)

        reload_data = common.load_yaml(filename)

        assert isinstance(reload_data, dict)
