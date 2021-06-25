import sys
import unittest

sys.path.insert(0, "./")

from autonn._optimizer import SGD, Adam
from autonn.resnet import ResNet18


class TestOptimizers(unittest.TestCase):
    def test_sgd(self):
        names = ["lr", "momentum", "dampening", "weight_decay", "nesterov"]
        values = [0.001, 1e-05, 1, 1e-05, False]
        opt = SGD(dampening=1)
        self.assertListEqual(opt.get_default_config_space().var_name, names)
        self.assertListEqual(list(opt.get_hyper_params().values()), values)

    def test_condition(self):
        opt = SGD(nesterov=True)
        self.assertEqual(opt.get_hyper_params()["dampening"], 0)
        self.assertTrue(opt.get_hyper_params()["momentum"] > 0)

    def test_adam(self):
        names = ["lr", "beta1", "beta2", "eps", "weight_decay", "amsgrad"]
        values = [0.001, 0.9, 0.999, 1e-08, 1e-10, False]
        opt = Adam()
        self.assertListEqual(opt.get_default_config_space().var_name, names)
        self.assertListEqual(list(opt.get_hyper_params().values()), values)

    def test_config_space(self):
        model = ResNet18()
        cs = model.get_default_config_space()
        cs.random_seed = 42
        self.assertIn("optimizer.lr", cs.var_name)

        params = {cs.var_name[i]: v for i, v in enumerate(cs.sample(1)[0])}
        model.set_params(params)
        _params = model.get_hyper_params()
        self.assertDictEqual(params, _params)


if __name__ == "__main__":
    unittest.main()
