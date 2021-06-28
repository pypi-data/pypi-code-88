import math
import numpy as np
from skimage.transform import resize

from .unetpad import unetpad
from .unet3pad import unet3pad
from .unet3pad3 import unet3pad3


def get_architecture(name, inchannels, n_classes):
    """
    create architecture.
    Use processing_dimensions for defining if an architecture is able to process [2D, 3D] images.
    """
    # Backward compatibility
    if name == "unetpad4":
        name = "unetpad"

    network = _get_architecture_instance(name)
    processing_dimensions = [True, True]

    if name == "unet":
        model = network(
            n_classes=n_classes,
            is_batchnorm=False,
            in_channels=inchannels,
            is_deconv=False,
        )
        processing_dimensions = [True, False]
    elif name == "unetpad":
        model = network(
            n_classes=n_classes,
            is_batchnorm=False,
            in_channels=inchannels,
            is_deconv=False,
        )
        processing_dimensions = [True, False]
    elif name == "unet3pad" or name == "unet3pad3":
        model = network(
            n_classes=n_classes,
            is_batchnorm=False,
            in_channels=inchannels,
            is_deconv=False,
        )
        processing_dimensions = [False, True]
    else:
        raise ValueError("Unrecognize network architecture {}".format(name))

    model.eval()

    return model, name, processing_dimensions


def _get_architecture_instance(name):
    return {
        "unetpad": unetpad,
        "unet3pad": unet3pad,
        "unet3pad3": unet3pad3,
    }[name]


def get_size(name, original_size, free_memory=None, is_3D=None):
    hash_size = {
        "unetpad": {
            256: [128, 128],
            512: [128, 128],
            1024: [512, 512],
            2048: [1024, 1024],
            4096: [1024, 1024],
            8192: [1024, 2048],
            16384: [2048, 2048],
            32768: [2048, 2048],
        },
        "unet3pad": {
            256: [64, 64, 64],
            512: [64, 64, 64],
            1024: [64, 64, 64],
            2048: [64, 64, 64],
            4096: [128, 128, 128],
            8192: [128, 128, 128],
            16384: [128, 128, 256],
            32768: [256, 256, 256],
        },
        "unet3pad3": {
            256: [64, 64, 64],
            512: [64, 64, 64],
            1024: [64, 64, 64],
            2048: [64, 64, 64],
            4096: [128, 128, 128],
            8192: [128, 128, 128],
            16384: [128, 128, 256],
            32768: [256, 256, 256],
        },
    }
    max_size = [
        -1,
    ]
    if name == "unetpad" and is_3D:
        name == "unet3pad"
    if not (free_memory is None):
        free_memory = 2 ** np.floor(np.log2(free_memory)).astype(int)
        if free_memory < 256:
            free_memory = 256
        if free_memory not in hash_size[name].keys():
            free_memory = 4096
        max_size = hash_size[name][free_memory]

    imcropsize = np.array(original_size)

    if name == "unetpad" or name == "unet3pad" or name == "unet3pad3":
        # find nearest power of two
        lower_power = 2 ** np.floor(np.log2(imcropsize)).astype(int)
        upper_power = 2 ** np.ceil(np.log2(imcropsize)).astype(int)
        lower_diff = np.abs(original_size - lower_power)
        upper_diff = np.abs(original_size - upper_power)

        imcropsize = [
            upper_power[i] if diff > 0 else lower_power[i]
            for i, diff in enumerate(list(lower_diff - upper_diff))
        ]

    else:
        raise ValueError(
            "A resizing policy was not found for architecture {}".format(name)
        )

    if name == "unet3pad" or name == "unet3pad3":
        imcropsize = [imcropsize[0], imcropsize[1], imcropsize[3]]

    imcropsize = [
        size if size < maximum else maximum
        for size, maximum in zip(imcropsize, max_size)
    ]

    return imcropsize
