from __future__ import annotations

import base64
import copy
import json
import os
import random
import re
from abc import abstractmethod
from io import BytesIO
from typing import List, Tuple, Union

import numpy as np
import torch
from PIL import Image
from torch.utils.data import DataLoader as th_Dataloader
from torch.utils.data import Dataset as th_Dataset
from torchvision import datasets as thv_Dataset
from torchvision import transforms as thv_Transform

from .fields import OrdinalHyperParameter
from .operator import AbstractOperator
from .oss import OSSConfig

__authors__ = ["Hao Wang", "Yuanhao Guo"]


def retrieve_manifest(url: str) -> List[dict]:
    """download a manifest (meta-data) of a data source from OSS"""
    bucket, key = OSSConfig()(url)
    data = bucket.get_object(key).read().decode("UTF-8").split("\n")
    return [json.loads(s) for s in data if len(s) > 0]


# TODO: also wrapper/implement `torch.utils.data.Subset` in this class
class PytorchDataSet(th_Dataset):
    """Data Set base class"""

    def __init__(
        self,
        data_src: Union[Tuple, List],
        labels: Tuple[int, str, List[str]] = (),
        category: str = "train",
        task: str = "cls",
        augmentation: bool = False,
        img_size: Union[Tuple[int, int]] = (224, 224),
        **kwargs,
    ):
        """Data Set base class

        Parameters
        ----------
        data_src : Union[Tuple, List]
            an iterable of sources (e.g., paths, URIs) to the data set.
        labels : Tuple[str], optional
            target labels of the data, by default (). It can be skipped for testing data.
        num_classes : int
            the number of classes of labels, by default None.
            It must be provided when `category` = 'train'
        category : str, optional
            'train', 'val', or 'test', by default 'train'
        task : str, optional
            the modeling task taking values in ['cls', 'seg'], by default 'cls'
        transform : bool, optional
            whether data augmentation should be applied, by default False
        img_size : Union[Tuple[int, int]], optional
            (height, width) of the desired output size after resizing, by default (224, 224)
        """
        PytorchDataSet._check_input(**locals())
        super().__init__()

        self.category = category
        self.augmentation = (category == "train") and augmentation
        self.img_size = img_size
        self.task = task
        self.data_src = list(copy.copy(data_src))

        self._set_targets(labels)
        self._set_transformer()

    def _check_input(self, **kwargs):
        assert kwargs["category"] in ["train", "val", "test"]
        assert kwargs["task"] in ["cls", "seg"]
        if kwargs["category"] in ["train", "val"]:
            assert len(kwargs["data_src"]) == len(kwargs["labels"])

    def _set_targets(self, labels):
        """Set the targets, the classes, and aux. variables"""
        if self.task == "cls":
            # NOTE: support multi-label classification
            _labels = [
                tuple(e) if hasattr(e, "__iter__") and not isinstance(e, str) else tuple([e])
                for e in labels
            ]
            N = np.array([len(_) for _ in _labels])
            # NOTE: `np.unique` is ~10x faster than `set`
            self.classes = tuple(np.unique(sum(_labels, ())))
            self.num_classes = len(self.classes)
            # map from label/class name to integer index
            self.class_to_idx = {_class: i for i, _class in enumerate(self.classes)}
            # always output int-valued target labels
            if np.all(N == 1):  # single-label
                self.targets = tuple([self.class_to_idx[e[0]] for e in _labels])
            else:  # multi-label
                self.targets = tuple([tuple([self.class_to_idx[i] for i in e]) for e in _labels])

        elif self.task == "seg":
            # TODO: discuss how to handle this properly
            self.targets = copy.copy(labels)

    def _set_transformer(self):
        ops = [
            thv_Transform.Resize(self.img_size),
            thv_Transform.Grayscale(num_output_channels=3),
            thv_Transform.ToTensor(),
            thv_Transform.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225)),
        ]
        if self.augmentation:
            ops = [
                thv_Transform.RandomHorizontalFlip(),
                thv_Transform.RandomVerticalFlip(),
            ] + ops

        if self.task == "seg":
            # TODO: implement this
            pass
        self._transformer = thv_Transform.Compose(ops)

    def __getitem__(self, index):
        X = self._transformer(self._retrieve_one(self.data_src[index]))
        if self.category in ["train", "val"]:
            return X, self._get_target(index)
        else:
            return X

    def _get_target(self, index):
        if self.task == "cls":
            return self._get_target_cls(index)
        elif self.task == "seg":
            return self._get_target_seg(index)

    def _get_target_cls(self, index):
        # TODO: is `long` type necessary?
        return torch.tensor(self.targets[index]).long()

    def _get_target_seg(self, index):
        pass

    @abstractmethod
    def _retrieve_one(self, path: str):
        """get one data record from `path`"""
        pass

    def __len__(self):
        return len(self.data_src)


class OssData(PytorchDataSet):
    """Data Sets from 's OSS"""

    def __init__(self, *args, **kwargs):
        """Aliyun's OSS data source"""
        super().__init__(*args, **kwargs)
        self._oss_config = OSSConfig()
        self._process = None
        # TODO: this should be implemented in a check_params method in the parent class
        if len(self.img_size) == 2:
            h, w = self.img_size
            self._process = f"image/resize,w_{w},h_{h}"

    def _retrieve_one(self, path: str):
        bucket, key = self._oss_config(path)
        return Image.open(bucket.get_object(key, process=self._process)).convert(
            "RGB"
        )  # always convert to 3-channel images

    def _check_input(self):
        super()._check_input()
        # TODO: the following ones might take too much time..
        # for i, url in enumerate(self.urls):
        #     try:
        #         oss_conf, key = create_oss_config_from_oss_url(url)
        #         oss_conf.get_bucket().get_object(key)
        #     except oss2.exceptions.NoSuchKey:
        #         # delete the data url and labels if cannot be retrieved
        #         self.urls.pop(i)
        #         self.labels.pop(i)


class Base64DataSet(PytorchDataSet):
    """Data Sets for base64 encoded images"""

    def __init__(self, *args, **kwargs):
        """Base64 encoded images data source

        Parameters
        ----------
        """
        super().__init__(*args, **kwargs)

    def _retrieve_one(self, path: str):
        img = self._base64_to_image(path)
        # always convert to 3-channel images
        return img.convert("RGB")

    def _base64_to_image(self, base64_encoded_img: str):
        sanitized = re.sub("^data:image/.+;base64,", "", base64_encoded_img)
        decoded = base64.b64decode(sanitized)
        image_bytes = BytesIO(decoded)
        return Image.open(image_bytes)


class LocalDataFromMeta(PytorchDataSet):
    """Prepare a `PytorchDataSet` from a local meta-data file"""

    def __init__(self, meta_file: str, **kwargs):
        """
        Parameters
        ----------
        meta_file : str
            a space-separated text file containing image path and labels, whose format
            reads, for image classification,
                image1_path 0
                image2_path 1
                image3_path 3

            and for segmentation
                image1_path mask1_path
                image2_path mask2_path
                image3_path mask3_path
        """
        if not os.path.exists(meta_file):
            raise ValueError(f"File {meta_file} does not exist!")

        self._meta_file = meta_file
        with open(self._meta_file, "r") as file:
            lines = file.readlines()

        info = [line.strip("\n").rstrip().split(" ") for line in lines]
        data_src, labels = list(zip(*info))
        # just in case `data_src` and `data_src` are fed in..
        kwargs.update({"data_src": data_src, "labels": labels})
        super().__init__(**kwargs)

    def _retrieve_one(self, path: str):
        return Image.open(path)

    def _get_target_seg(self, index):
        return Image.open(self.targets[index])


class _TorchVisionWrapper(PytorchDataSet):
    """Wrapper for Torch Vision's datasets"""

    def __init__(
        self,
        dataset: str,
        category: str = "train",
        augmentation: bool = False,
        img_size: Union[int, Tuple[int, int]] = (224, 224),
        **kwargs,
    ):
        assert category in ["train", "val", "test"]
        self.category = category
        self.augmentation = augmentation
        self.img_size = img_size

        self._create_dataset(dataset, **kwargs)
        self.targets = self._dataset.targets
        self.classes = self._dataset.classes
        self.num_classes = len(self.classes)
        self.class_to_idx = self._dataset.class_to_idx

    def _retrieve_one(self, path: str):
        pass

    @abstractmethod
    def _create_dataset(self, *args, **kwargs):
        pass

    def __getitem__(self, index):
        X, y = self._dataset[index]
        return (X if self.category == "test" else X, y)


class PublicData(_TorchVisionWrapper):
    """Prepare a `PytorchDataSet` from online official repositories"""

    _public_data = {
        "mnist": (thv_Dataset.MNIST, "cls"),
        "cifar10": (thv_Dataset.CIFAR10, "cls"),
        "cifar100": (thv_Dataset.CIFAR100, "cls"),
    }

    def __init__(self, dataset: str, root: str = "./", download: bool = False, **kwargs):
        """
        Parameters
        ----------
        dataset : str
            The name of the data set
        root : str, optional
            base directory to store the downloaded data set, by default './'
        download : bool, optional
            whether to download this public data set or not, which must be `True` when
            the public data set cannot be found under `root`.
        """
        super().__init__(dataset, root=root, download=download)

    def _create_dataset(self, dataset: str, root: str = "./", download: bool = False, **kwargs):
        assert dataset in self._public_data.keys()
        self.dataset_name = dataset
        self.task = self._public_data[self.dataset_name][1]
        self._set_transformer()
        self._dataset = self._public_data[self.dataset_name][0](
            root, train=self.category, transform=self._transformer, download=download
        )
        self.data_src = self._dataset.data


class LocalDataFromFolder(_TorchVisionWrapper):
    """Prepare a `PytorchDataSet` from online official repositories"""

    def _create_dataset(self, dataset: str, **kwargs):
        assert os.path.isdir(dataset)
        self.dataset_name = dataset
        self.task = "cls"
        self._set_transformer()
        self._dataset = thv_Dataset.ImageFolder(dataset, transform=self._transformer)
        self.data_src = self._dataset


# TODO: TO FIX AND TEST IT
class DataLoader(th_Dataloader, AbstractOperator):
    batch_size = OrdinalHyperParameter([16, 32, 64, 128, 256], 256)

    def __init__(
        self, dataset: PytorchDataSet, workers: int = 0, random_seed: int = None, **kwargs
    ):
        AbstractOperator.__init__(self)
        self.random_seed = random_seed
        self.shuffle = dataset.category == "train"
        self.drop_last = dataset.category == "train"
        self.dataset = dataset
        self.workers = workers

    def fit(self) -> DataLoader:
        # the batch size should not be larger than its total size
        self.batch_size = min(self.batch_size, len(self.dataset))
        # worker_init_fn = self._worker_init_fn if self.workers > 0 else None
        super().__init__(
            dataset=self.dataset,
            batch_size=self.batch_size,
            shuffle=self.shuffle,
            num_workers=self.workers,
            drop_last=self.drop_last
            # worker_init_fn=worker_init_fn
        )
        return self

    @staticmethod
    def _worker_init_fn(worker_id: int):
        worker_seed = torch.initial_seed() % 2 ** 32
        np.random.seed(worker_seed)
        random.seed(worker_seed)


def seed_worker(worker_id: int):
    worker_seed = torch.initial_seed() % 2 ** 32
    np.random.seed(worker_seed)
    random.seed(worker_seed)


def make_dataloader(dataset: PytorchDataSet, batch_size: int = 8, workers: int = 0):
    """Wrapper for torch's DataLoader

    Parameters
    ----------
    dataset : PytorchDataSet
        data set
    batch_size : int, optional
        the batch size, by default 8
    workers : int, optional
        number of workers running in parallel, by default 0 (sequential mode)
    """
    shuffle = dataset.category == "train"
    drop_last = dataset.category == "train"
    # the batch size should not be larger than its total size
    batch_size = min(batch_size, len(dataset))
    worker_init_fn = seed_worker if workers > 0 else None
    # TODO: fix `num_workers`
    return th_Dataloader(
        dataset,
        batch_size=batch_size,
        shuffle=shuffle,
        num_workers=workers,
        drop_last=drop_last,
        worker_init_fn=worker_init_fn,
    )
