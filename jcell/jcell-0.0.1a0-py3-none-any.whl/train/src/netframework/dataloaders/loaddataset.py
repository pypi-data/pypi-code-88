import json
import os
import numpy as np
from ..utils.utils import Decoder
from ..utils.utils import get_class
from importlib import import_module
from torch.utils.data import DataLoader, random_split
import torchvision.transforms as transforms
from torch.utils.data.sampler import SubsetRandomSampler, SequentialSampler
import torch


def loaddataset(
    datasetname,
    experimentparam,
    batch_size=1,
    worker=1,
    is_3D=False,
    config_file="defaults/dataconfig_train.json",
):
    # load dataset configuration (json)
    if datasetname == "" and not os.path.isabs(config_file):
        datasetname = "data3d" if is_3D else "data2d"

    path_config, config_file_name = os.path.split(config_file)
    automatic_split_required = False

    if config_file_name == "dataconfig_train.json":
        try:
            temp_data_props = get_data_path(
                name=datasetname,
                config_file=os.path.join(path_config, "dataconfig_dev.json"),
            )
        except Exception:
            automatic_split_required = True
            print("Using automatic data split in training and validation sets")

    data_props = get_data_path(name=datasetname, config_file=config_file)

    module = data_props.pop("module", "dataloaders.segdataset")

    for key, value in experimentparam.items():
        data_props[key] = value

    if "transform_parameter" in data_props:
        transformstr = data_props.pop("transform_parameter", "ToTensor()")
    else:
        raise ValueError(
            "Please define a default transform 'transform_parameter' behavior in "
            + config_file
        )

    # setup transforms
    tr = import_module(module + ".ctransforms")
    transformlist = transformstr.replace(" ", "").split("),")
    transformlist[-1] = transformlist[-1][:-1]
    transformstr = ""
    for transf in transformlist:
        transformstr += "tr." + transf + "," + str(is_3D) + "),"
    transformstr = transformstr.replace("(,", "(")

    transform = eval("transforms.Compose([" + transformstr + "])")

    cdataset = get_class(module + ".dataset.cdataset")
    data_props["is_3D"] = is_3D

    # dataset
    ddatasets = cdataset(**data_props, transform_parameter=transform)

    # loader
    tsampler = SubsetRandomSampler(np.random.permutation(len(ddatasets)))
    dloader = DataLoader(
        ddatasets,
        batch_size=batch_size,
        sampler=tsampler,
        num_workers=worker,
        pin_memory=True,
    )

    if automatic_split_required:
        val_len = max(min(int(len(ddatasets) * 0.1), 100), 1)
        train_len = len(ddatasets) - val_len
        ddatasets = random_split(
            ddatasets,
            [train_len, val_len],
            generator=torch.Generator().manual_seed(1),
        )

        dloader = list()
        dloader.append(
            DataLoader(
                ddatasets[0],
                batch_size=batch_size,
                num_workers=worker,
                pin_memory=True,
                shuffle=True,
            )
        )
        dloader.append(
            DataLoader(
                ddatasets[1],
                batch_size=batch_size,
                num_workers=worker,
                pin_memory=True,
                shuffle=False,
            )
        )

    return ddatasets, dloader, module, data_props["number_classes"]


def get_data_path(name, config_file="defaults/dataconfig_train.json"):
    data = json.load(open(config_file), cls=Decoder)
    if name == "":
        name = list(data.keys())[0]
    if name not in data:
        raise ValueError(
            "Dataset {} not found in {}. Please, change --dataset to one of the following {}".format(
                name, config_file, list(data.keys())
            )
        )
    if "dataconfig_train.json" in config_file:
        print(name)
    return data[name]
