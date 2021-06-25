import os
import shutil
import sys
import unittest

sys.path.insert(0, "./")

import numpy as np
import torch

from autonn import ResNet18
from autonn.dataset import PublicData


class TestResNet(unittest.TestCase):
    def setUp(self):
        self.model = ResNet18()
        data = PublicData(dataset="cifar10", root="./data", download=True)
        self.data = torch.utils.data.Subset(data, np.random.randint(0, len(data) - 1, 100))

    def tearDown(self):
        os.remove("test.pth")
        os.remove("test.dump")
        os.remove("log")
        shutil.rmtree("data")

    def step1(self):
        kwargs = {
            "input_kernel": 2,
            "width_per_group": 30,
            "expansion": 2,
            "block": "bottle_neck",
            "pre_train": True,
        }
        self.model.set_params(kwargs)

    def step2(self):
        data_train = torch.utils.data.DataLoader(
            self.data, batch_size=20, shuffle=False, num_workers=0
        )
        self.model.set_random_seed(42).set_logger("./log").set_params(
            {"epochs": 1, "num_classes": 10}
        ).set_data(
            data_train=data_train  # test without validation set
        )
        self.assertEqual(self.model.epochs, 1)
        self.assertEqual(self.model.num_classes, 10)

    def step3(self):
        self.model.fit()
        self.assertTrue(hasattr(self.model, "_model"))

    def step4(self):
        self.model.save("test")
        model_ = ResNet18.load("test")
        parameters = getattr(self.model, "_model").parameters()
        parameters_ = getattr(model_, "_model").parameters()
        try:
            while True:
                # NOTE: make sure the model parameters are the same
                self.assertTrue(
                    np.all(
                        next(parameters).detach().numpy().ravel()
                        == next(parameters_).detach().numpy().ravel()
                    )
                )
        except StopIteration:
            pass

        self.assertEqual(self.model.get_hyper_params(), model_.get_hyper_params())

    def step5(self):
        data_val = torch.utils.data.DataLoader(
            self.data, batch_size=20, shuffle=False, num_workers=0
        )
        for _, inputs in enumerate(data_val):
            images = inputs[0]
            output = self.model.predict_prob(images)
            self.assertTrue(isinstance(output, np.ndarray))
            self.assertEqual(output.shape, (len(images), self.model.num_classes))
            self.assertTrue(np.all(np.isclose(output.sum(axis=1), 1)))
            output_ = self.model.predict(images)
            self.assertTrue(set(output_).issubset(self.data.dataset.classes))

    def _steps(self):
        for name in dir(self):
            if name.startswith("step"):
                yield name, getattr(self, name)

    def test_steps(self):
        for name, step in self._steps():
            try:
                step()
            except Exception as e:
                self.fail(f"{name} failed ({type(e)}: {e})")


if __name__ == "__main__":
    unittest.main()
