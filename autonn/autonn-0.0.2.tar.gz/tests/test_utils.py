import os
import sys
import unittest

sys.path.insert(0, "./")
from autonn import ResNet18
from autonn.utils import create_cmd_parser_from_operator, create_partial_yaml_from_operator


class TestUtils(unittest.TestCase):
    def test_gen_parser(self):
        model = ResNet18()
        parser = create_cmd_parser_from_operator(model)
        # NOTE: `parse_known_args` is needed othewise an error would arise
        # since we are using 'coverage run -m unittest discover' for the test
        kwargs = getattr(parser.parse_known_args()[0], "_get_kwargs")()
        hyper_params = dict(model.get_hyper_params())
        kwargs = {k: v for k, v in kwargs}
        self.assertTrue(set(kwargs.keys()).issuperset(set(hyper_params.keys())))
        for k, v in hyper_params.items():
            self.assertEqual(v, kwargs[k])

    def test_parser_data_type(self):
        model = ResNet18()
        parser = create_cmd_parser_from_operator(model)
        args = [
            "--block=bottle_neck",
            "--expansion=4",
            "--input_kernel=3",
            "--optimizer.dampening=1.886035594871104e-10",
            "--optimizer.lr=0.007916522657454655",
            "--optimizer.momentum=0.0003523056624560434",
            "--optimizer.nesterov=True",
            "--optimizer.weight_decay=1.524485758539801e-09",
            "--scheduler.gamma=1.3698523029504707e-06",
            "--width_per_group=64",
        ]
        args = getattr(parser.parse_args(args), "_get_kwargs")()
        args = {k: v for k, v in args}
        params = dict(model.get_hyper_params())
        for k, v in params.items():
            self.assertEqual(type(v), type(args[k]))

    def test_gen_yaml(self):
        model = ResNet18()
        out = create_partial_yaml_from_operator(model, yaml_file="image-classification.yaml")
        self.assertEqual(
            set([d["name"] for d in out["parameters"]]), set(model.get_hyper_params().keys())
        )
        os.remove("image-classification.yaml")


if __name__ == "__main__":
    unittest.main()
