import sys
import unittest

sys.path.insert(0, "./")

from bayes_optim.search_space import Real

from autonn.fields import (
    DiscreteHyperParameter,
    IntegerHyperParameter,
    Parameter,
    RealHyperParameter,
)
from autonn.operator import AbstractOperator


class AOperator(AbstractOperator):
    x = RealHyperParameter([0, 100], 2)
    y = RealHyperParameter([-200, 200], 3)
    name = Parameter("A")


class BOperator(AbstractOperator):
    x = RealHyperParameter([0, 100], 2)
    y = RealHyperParameter([-200, 200], 3)
    name = Parameter("B")


class COperator(AbstractOperator):
    x = RealHyperParameter([0, 100])
    y = RealHyperParameter([-200, 200])
    name = Parameter("C")


class Model(AbstractOperator):
    x = IntegerHyperParameter([0, 10])
    y = RealHyperParameter([0.1, 0.5])
    name = Parameter("model")
    op1 = Parameter(default_value=AOperator())
    op2 = DiscreteHyperParameter(
        ["AOperator", "BOperator", "COperator"], default_value=AOperator()  # TODO: fix this!
    )


class Model2(AbstractOperator):
    name = Parameter("model in a higher level")
    op1 = Parameter(default_value=Model(x=1, y=2))


class TestOperator(unittest.TestCase):
    def test_recursive(self):
        m = Model2()
        hyper_parameters = [
            "op1.x",
            "op1.y",
            "op1.op1.x",
            "op1.op1.y",
            "op1.op2.x",
            "op1.op2.y",
            "op1.op2",
        ]
        self.assertListEqual(m.config_space.var_name, hyper_parameters)
        self.assertListEqual(list(m.get_hyper_params()), hyper_parameters)
        self.assertListEqual(
            list(m.get_params().keys()),
            ["name", "op1.name", "op1.op1.name", "op1.op1", "op1.op2.name", "op1"],
        )

    def test_set_params(self):
        m = Model(x=1, y=2)
        new_values = {"x": 5, "op1.x": 500, "op2": BOperator()}
        m.set_params(new_values)
        self.assertEqual(m.x, 5)
        self.assertEqual(m.op1.x, 500)
        self.assertEqual(m.op2.x, 2)
        self.assertEqual(m.op2.y, 3)

    def test_config_space(self):
        m = Model2(op1=Model(x=1, y=2, op1=AOperator(), op2=AOperator()))
        cs = m.config_space
        cs.remove("op1.x")
        cs.remove("op1.op2.y")
        m.config_space = cs

        self.assertNotIn("op1.x", m.config_space.var_name)
        self.assertIn("op1.x", m._default_config_space.var_name)

        self.assertNotIn("op1.op2.y", m.config_space.var_name)
        self.assertIn("op1.op2.y", m._default_config_space.var_name)

        cs = m.config_space
        cs[1] = Real([30, 50], name="op1.op1.x")
        m.config_space = cs
        self.assertEqual(m.get_variables()["op1.op1.x"].bounds[0], 30)


if __name__ == "__main__":
    unittest.main()
