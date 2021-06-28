import json

from .imageutl import loadimage, saveimage, imageProvider
from .segdataset import (
    SplitImage,
    ToTensorImage,
    Normalize,
    NormalizePercentile,
)


def get_data_path(name, config_file="dataconfig.json"):
    data = json.load(open(config_file))
    return (
        data[name]["data_path"],
        data[name]["test_data_path"],
        data[name]["image_ext"],
        data[name]["label_ext"],
        data[name]["image_folder"],
        data[name]["label_folder"],
        data[name]["weight_folder"],
        data[name]["n_classes"],
    )
