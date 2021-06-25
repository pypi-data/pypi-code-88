import itertools
import shutil
import sys
import unittest

sys.path.insert(0, "./")
import numpy as np
import torch
from bayes_optim.search_space import Discrete, Ordinal

from autonn import ResNet18
from autonn.dataset import PublicData


class TestResNetConfigSpace(unittest.TestCase):
    def setUp(self):
        self.model = ResNet18()
        data = PublicData(dataset="cifar10", root="./data", download=True)
        data = torch.utils.data.Subset(data, np.random.randint(0, len(data) - 1, 10))
        data_train = torch.utils.data.DataLoader(data, batch_size=10, shuffle=False, num_workers=0)

        cs = self.model.get_default_config_space()
        self.categories = [
            list(var.bounds) for var in cs.data if isinstance(var, (Ordinal, Discrete))
        ]
        self.names = [var.name for var in cs.data if isinstance(var, (Ordinal, Discrete))]
        self.model.set_random_seed(42).set_params({"epochs": 1}).set_data(
            data_train=data_train  # test without validation set
        )

    def tearDown(self):
        shutil.rmtree("data")

    def test_ResNet18(self):
        # test for all combinations of categorical/ordinal parameters
        # on a simple training task
        for element in itertools.product(*self.categories):
            kwargs = {n: element[i] for i, n in enumerate(self.names)}
            print(kwargs)
            self.model.set_params(kwargs).fit()


if __name__ == "__main__":
    unittest.main()
