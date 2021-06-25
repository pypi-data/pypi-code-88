import sys

sys.path.insert(0, "./")

import unittest

import numpy as np
import torch

from autonn import ResNet18
from autonn.dataset import (
    Base64DataSet,
    DataLoader,
    OssData,
    PublicData,
    make_dataloader,
    retrieve_manifest,
)


class TestData(unittest.TestCase):
    def setUp(self):
        self.prefix = "oss://aiexcelsior-shanghai-test.oss-cn-shanghai.aliyuncs.com/"

    def test_oss_data(self):
        urls = [
            "000000000000000000000000/603c5ab12ce3dd90cbe17c2f/31489.jpg",
            "000000000000000000000000/603c5ab12ce3dd90cbe17c2f/32180.jpg",
            "000000000000000000000000/603c5ab12ce3dd90cbe17c2f/32194.jpg",
            "000000000000000000000000/603c5ab12ce3dd90cbe17c2f/34297.jpg",
            "000000000000000000000000/603c5ab12ce3dd90cbe17c2f/35189.jpg",
            "000000000000000000000000/603c5ab12ce3dd90cbe17c2f/35823.jpg",
            "000000000000000000000000/603c5ab12ce3dd90cbe17c2f/35837.jpg",
            "000000000000000000000000/603c5ab12ce3dd90cbe17c2f/36480.jpg",
        ]
        urls = [self.prefix + _ for _ in urls]
        labels = list(map(str, np.random.randint(0, 3, len(urls))))
        data_iter = OssData(urls, labels, category="val")
        for _, __ in enumerate(data_iter):
            pass

    def test_oss_data_loader(self):
        # TODO: this test it too big..
        manifest = retrieve_manifest(
            self.prefix
            + "000000000000000000000000/603c5ab12ce3dd90cbe17c2f/artifacts/"
            + "manifests/ImageClassification.1615270927.MANIFEST"
        )
        category, urls, labels = [], [], []
        for item in manifest:
            category.append(item["category"])
            urls.append(item["source"])
            labels.append(item["labels"][0])

        data_train = make_dataloader(OssData(urls, labels, category="val"), batch_size=10)

        model = ResNet18()
        model.epochs = 1
        model.set_data(data_train=data_train).fit()

        data_test = make_dataloader(
            OssData(urls[:50], labels[:50], category="test"), batch_size=10
        )

        for _, inputs in enumerate(data_test):
            self.assertEqual(len(inputs), 10)
            output_ = model.predict(inputs)
            self.assertTrue(set(output_).issubset(data_train.dataset.classes))

    def test_base64_dataset(self):
        _test_img_7 = (
            "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/"
            "2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc"
            "5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMj"
            "IyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAcABwDAREAAhEBAxEB/8QAGAAAAwEBAAAAAAAAAAAAAAAAAA"
            "YHBAH/xAAqEAABAwMDAwMEAwAAAAAAAAABAgMEBREhAAYSBxNBMWGRFBUiMlFigf/EABQBAQAAAAAAAAA"
            "AAAAAAAAAAAD/xAAUEQEAAAAAAAAAAAAAAAAAAAAA/9oADAMBAAIRAxEAPwCAAEkAC5PjQNtY6b7uos"
            "lLEihy3ipAWFxWy8gg28pByL2toO07p5WZiz9a9TqMhIJKqrLSwRb+huv/AHjbB0Cs+z233G0rS4lCik"
            "LRcpVY+o9tA29L2qMvfkI15yKmGhK1JTLt2VucTwCycAXzn+NA2bl271UqVTk19tx2U244C2ujzgts"
            "C349tKVcrAWza/n30EuqMSfCqDrVTYkMzL8nEyUqSsk5ub5z630GHQGgokDaM2ftyLWNj1GZJlI"
            "QE1KntO8ZDLl/2SlJBU2T6eR82Bnlv1OD05qbPUl1Lsh9lP2iLKsZvcAIDnLKgkXzy9xi+QimgNBp"
            "hy5MOQHYkl6O6BhbKyhXyNASpUiXILsqQ6+4RlbqypXydBm0H//Z"
        )
        test_dataloader = make_dataloader(Base64DataSet([_test_img_7], category="test"))
        actual_img = next(iter(test_dataloader))
        self.assertIsInstance(actual_img, torch.Tensor)
        self.assertTupleEqual(tuple(actual_img.size()), (1, 3, 224, 224))

    def test_dataloader(self):
        test_dataloader = DataLoader(
            dataset=PublicData("cifar10", root="./data", download=True, category="train"),
            workers=16,
        )
        test_dataloader.set_params({"batch_size": 128}).fit()
        for step, (images, labels) in enumerate(test_dataloader):
            if step <= 5:
                images = images.cuda()
                self.assertTupleEqual(tuple(images.size()), (128, 3, 224, 224))
                self.assertEqual(labels.size()[0], 128)
            else:
                break


if __name__ == "__main__":
    unittest.main()
