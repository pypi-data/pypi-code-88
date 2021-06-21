# modified from https://github.com/kekmodel/FixMatch-pytorch/blob/master/dataset/cifar.py
from PIL import Image
from typing import Dict

from torchvision.datasets import CIFAR10 as CIFAR10_pt
from gorilla import DATASETS

@DATASETS.register_module(force=True)
class CIFAR10(CIFAR10_pt):
    num_classes = 10
    def __getitem__(self, index: int) -> Dict:
        """
        Args:
            index (int): Index

        Return:
            item (dict): including "img" and "target", where target is index of the target class.
        """
        img, target = self.data[index], self.targets[index]
        img = Image.fromarray(img)
        item = {}
        if self.transform is not None:
            if isinstance(self.transform, dict):
                for key, transform in self.transform.items():
                    item.update({key: transform(img)})
            else:
                img = self.transform(img)
                item.update({"img": img})

        if self.target_transform is not None and target is not None:
            target = self.target_transform(target)

        item.update({"target": target})
        return item


@DATASETS.register_module(force=True)
class CIFAR100(CIFAR10):
    """`CIFAR100 <https://www.cs.toronto.edu/~kriz/cifar.html>`_ Dataset.

    This is a subclass of the `CIFAR10` Dataset.
    """
    base_folder = 'cifar-100-python'
    url = "https://www.cs.toronto.edu/~kriz/cifar-100-python.tar.gz"
    filename = "cifar-100-python.tar.gz"
    tgz_md5 = 'eb9058c3a382ffc7106e4002c42a8d85'
    train_list = [
        ['train', '16019d7e3df5f24257cddd939b257f8d'],
    ]

    test_list = [
        ['test', 'f0ef6b0ae62326f3e7ffdfab6717acfc'],
    ]
    meta = {
        'filename': 'meta',
        'key': 'fine_label_names',
        'md5': '7973b15100ade9c7d40fb424638fde48',
    }
    num_classes = 100
