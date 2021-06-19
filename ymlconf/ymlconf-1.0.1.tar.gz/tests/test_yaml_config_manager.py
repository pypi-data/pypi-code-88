#!/usr/bin/env python3
import ymlconf
from tests.base_test_case import TestCaseWithTempTestDataDir


class A(ymlconf.YamlConfigManager):
    attr1 = ymlconf.Attribute()
    attr2 = ymlconf.Attribute()
    attr3 = ymlconf.Attribute()
    attr4 = ymlconf.Attribute()


class B(ymlconf.YamlConfigManager):
    _KEY = "B.b1"

    attr1 = ymlconf.Attribute()
    attr2 = ymlconf.Attribute()


class C(ymlconf.YamlConfigManager):
    _KEY = "C.c1.c11"

    attr1 = ymlconf.Attribute()
    attr2 = ymlconf.Attribute()


class TestYamlConfigManager(TestCaseWithTempTestDataDir):
    def test_simple_case(self):
        a = A(self.path_a)

        a.attr1 = "modified_attr_a"

        a.flush()

    def test_nested_case(self):
        b = B(self.path_b)

        b.attr1 = "modified attr b"

        b.flush()

    def test_3_nested_case(self):
        c = C(self.path_c)

        print(c.__dict__)

        c.attr1 = "modified attr c"
        c.attr2 = 123555

        c.flush()
