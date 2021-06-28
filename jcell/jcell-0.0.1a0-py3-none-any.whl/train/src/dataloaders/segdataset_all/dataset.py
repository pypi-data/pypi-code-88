import os

import numpy as np
from torch.utils import data
import random

from netframework.dataloaders.imageutl import segmentationProvider
from netframework import save_defaults, load_defaults


class cdataset(data.Dataset):
    @save_defaults
    @load_defaults
    def __init__(
        self,
        dataset_folder="",
        split="",
        image_folder="",
        label_folder="",
        transform_parameter=None,
        number_classes=4,
        rep=1,
        is_3D=False,
    ):
        self.__initialization__(
            dataset_folder,
            split,
            image_folder,
            label_folder,
            "",
            transform_parameter,
            number_classes,
            rep,
            is_3D,
        )

    def __initialization__(
        self,
        dataset_folder_list="",
        split="",
        image_folder="",
        label_folder="",
        weight_folder="",
        transform_parameter=None,
        number_classes=4,
        rep=1,
        is_3D=False,
    ):
        if not isinstance(dataset_folder_list, list):
            dataset_folder_list = [dataset_folder_list]
        self.root = dataset_folder_list  # root path
        self.n_classes = number_classes  # number of classes
        self.transform_param = transform_parameter  # transforms
        self.dataprov = dict()
        self.split = split
        self.image_folder = image_folder
        self.label_folder = label_folder
        self.weight_folder = weight_folder
        self.len = 0
        self.number_datasets = len(self.root)
        for i in range(self.number_datasets):
            self.dataprov[i] = segmentationProvider(
                os.path.join(self.root[i], split, image_folder),
                os.path.join(self.root[i], split, label_folder),
            )
            if i == 0:
                self.len = len(self.dataprov[i])
            else:
                self.len = max(self.len, len(self.dataprov[i]))
        self.rep = rep
        self.is_3D = is_3D
        self.pattern = 0
        self.accesing_dataset = np.ones((self.number_datasets,))

    def __len__(self):
        return self.len * self.rep

    def __getitem__(self, index):
        np.random.seed(random.randint(0, 2 ** 32))
        current_pattern = index % self.number_datasets

        len_dataset = len(self.dataprov[current_pattern])
        index = random.randint(0, len_dataset)

        img, lbl = self.dataprov[current_pattern][index % len_dataset]

        if not self.is_3D and img.ndim == 2:
            img = np.repeat(img[..., np.newaxis], 3, axis=2)
        elif self.is_3D and img.ndim == 3:
            img = np.repeat(img[..., np.newaxis], 3, axis=3)
        elif not self.is_3D and img.ndim == 3 and img.shape[2] == 1:
            img = np.repeat(img, 3, axis=2)
        elif self.is_3D and img.ndim == 4 and img.shape[3] == 1:
            img = np.repeat(img, 3, axis=3)

        if self.is_3D and img.ndim == 4 and img.shape[2] > img.shape[3]:
            img = img.transpose((0, 1, 3, 2))

        if (not self.is_3D and lbl.ndim == 3) or (
            self.is_3D and lbl.ndim == 4
        ):
            lbl = lbl[..., 0].squeeze()

        sample = {"image": img, "label": lbl}

        normalization = "max_norm"
        if self.transform_param is not None:
            sample = self.transform_param(sample)
            if "NormalizePercentile" in repr(self.transform_param):
                normalization = "percentile_norm"

        sample["idx"] = index
        sample["normalization"] = normalization
        return sample


def warp_Variable(sample, device):
    images, labels = sample["image"], sample["label"]
    images = images.to(device)
    labels = labels.to(device)

    output = {
        "image": images,
        "label": labels,
        "idx": sample["idx"],
    }

    if "weight" in sample:
        weight = sample["weight"]
        weight = weight.to(device)
        output["weight"] = weight

    return output
