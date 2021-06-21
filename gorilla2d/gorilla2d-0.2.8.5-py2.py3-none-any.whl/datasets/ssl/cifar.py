# Copyright (c) Gorilla-Lab. All rights reserved.
import os

import numpy as np

from ..cls import CIFAR10, CIFAR100

class CIFAR10SSL(CIFAR10):
    def __init__(self, root, train=True,
                 transform=None, target_transform=None,
                 download=False, seed=1, num_labeled_per_class=4):
        r"""Author: zhang.haojian
            Args:
                seed (int): random seed for data spliting
                num_labeled_per_class (int): number of labeled samples per class
                other parameters is the same as the original CIFAR10.
        """
        super().__init__(root, train=train,
                         transform=transform,
                         target_transform=target_transform,
                         download=download)
        indexes_file = os.path.join(root, "indexes_list", f"seed{seed}_labeled{num_labeled_per_class}.txt")
        with open(indexes_file, "r") as fp:
            indexes = [int(ind) for ind in fp.read().split(" ")]
        self.data = self.data[indexes]
        self.targets = np.array(self.targets)[indexes]


class CIFAR100SSL(CIFAR100):
    def __init__(self, root, indexes, train=True,
                 transform=None, target_transform=None,
                 download=False, seed=1, num_labeled_per_class=4):
        r"""Author: zhang.haojian
            Args:
                seed (int): random seed for data spliting
                num_labeled_per_class (int): number of labeled samples per class
                other parameters is the same as the original CIFAR10.
        """
        super().__init__(root, train=train,
                         transform=transform,
                         target_transform=target_transform,
                         download=download)
        if indexes is not None:
            self.data = self.data[indexes]
            self.targets = np.array(self.targets)[indexes]
        indexes_file = os.path.join(root, "indexes_list", f"seed{seed}_labeled{num_labeled_per_class}.txt")
        with open(indexes_file, "r") as fp:
            indexes = [int(ind) for ind in fp.read().splitlines()]
        self.data = self.data[indexes]
        self.targets = np.array(self.targets)[indexes]
