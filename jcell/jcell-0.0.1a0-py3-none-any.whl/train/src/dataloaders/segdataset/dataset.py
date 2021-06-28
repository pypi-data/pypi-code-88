import os

import numpy as np
from torch.utils import data

from netframework.dataloaders.imageutl import (
    segmentationProvider,
    matProvider,
)

from netframework import load_defaults, save_defaults


class cdataset(data.Dataset):
    @load_defaults
    @save_defaults
    def __init__(
        self,
        dataset_folder="",
        split="",
        image_folder="",
        label_folder="",
        weight_folder="",
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
            weight_folder,
            transform_parameter,
            number_classes,
            rep,
            is_3D,
        )

    def __initialization__(
        self,
        dataset_folder="",
        split="",
        image_folder="",
        label_folder="",
        weight_folder="",
        transform_parameter=None,
        number_classes=4,
        rep=1,
        is_3D=False,
    ):
        self.root = dataset_folder  # root path
        self.n_classes = number_classes  # number of classes
        self.transform_param = transform_parameter  # transforms
        self.split = split
        self.image_folder = image_folder
        self.label_folder = label_folder
        self.weight_folder = weight_folder
        self.dataprov = segmentationProvider(
            os.path.join(self.root, split, image_folder),
            os.path.join(self.root, split, label_folder),
        )
        self.rep = rep
        self.is_3D = is_3D

        load_weight = False if weight_folder == "" else True

        self.load_weight = load_weight
        if self.load_weight:
            self.weightprov = matProvider(
                os.path.join(self.root, split, weight_folder)
            )

    def __len__(self):
        return self.dataprov._num * self.rep

    def __getitem__(self, index):
        img, lbl = self.dataprov[index % self.dataprov._num]

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

        if self.load_weight:
            wht = self.weightprov[index % self.dataprov.num]
            if not self.is_3D and wht.ndim == 3:
                wht = np.squeeze(wht[..., 0], axis=2)
            elif self.is_3D and wht.ndim == 4:
                wht = np.squeeze(wht[..., 0], axis=3)
            sample["weight"] = wht

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
