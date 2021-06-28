import os
import math
import random
import warnings

import numpy as np

try:
    from ..imageutl import saveimage
except Exception:
    from imageutl import saveimage


def augmentation(
    image,
    label,
    outpath,
    block_size_x=0,
    block_size_y=0,
    gamma_transform=True,
    ignore_empty=True,
    regexpr="",
):
    """
    Data augmentation for 2D image segmentation
    """
    outpath, image_name = os.path.split(outpath)
    image_name, image_ext = os.path.splitext(image_name)
    if not os.path.isdir(outpath):
        raise ValueError("{} does not exist".format(outpath))
    if not image_name:
        raise ValueError("Please, specify a valid file name")
    if not image_ext:
        image_ext = ".tif"

    if not os.path.exists(os.path.join(outpath, "images")):
        os.mkdir(os.path.join(outpath, "images"))
    if not os.path.exists(os.path.join(outpath, "labels")):
        os.mkdir(os.path.join(outpath, "labels"))

    image_shape = list(image.shape)
    num_rows = block_size_x if block_size_x > 0 else image.shape[0]
    num_cols = block_size_y if block_size_y > 0 else image.shape[1]

    obj = 0
    for j in range(math.ceil(image_shape[1] / num_cols)):
        for x in range(math.ceil(image_shape[0] / num_rows)):
            for flipc in range(4):
                xr = x * num_rows
                yr = j * num_cols
                offsetx = (
                    image_shape[0] - (xr + num_rows)
                    if (xr + num_rows) > image_shape[0]
                    else 0
                )
                offsety = (
                    image_shape[1] - (yr + num_cols)
                    if (yr + num_cols) > image_shape[1]
                    else 0
                )
                xr += offsetx
                yr += offsety

                image_crop = image[xr : xr + num_rows, yr : yr + num_cols, ...]
                label_crop = label[xr : xr + num_rows, yr : yr + num_cols, ...]

                if label_crop.sum() == 0 and ignore_empty:
                    continue

                flip_comb = int(bin(flipc)[2:])
                flip_x = flip_comb % 10
                flip_comb = flip_comb // 10
                flip_y = flip_comb % 10

                if flip_x == 1:
                    image_crop = np.flip(image_crop, 0)
                    label_crop = np.flip(label_crop, 0)
                if flip_y == 1:
                    image_crop = np.flip(image_crop, 1)
                    label_crop = np.flip(label_crop, 1)

                if gamma_transform:
                    if random.random() < 0.5:
                        gamma = random.random() * 0.5 + 0.3
                    else:
                        gamma = random.random() + 1
                    if image_crop.dtype == np.dtype("uint8"):
                        image_crop = (
                            ((image_crop.astype("float") / 255) ** gamma) * 255
                        ).astype("uint8")
                    elif image_crop.dtype == np.dtype("uint16"):
                        image_crop = (
                            ((image_crop.astype("float") / 65535) ** gamma)
                            * 65535
                        ).astype("uint16")
                    else:
                        warnings.warn(
                            "{} not supported. Skipping gamma augmentation".format(
                                image_crop.dtype
                            )
                        )

                saveimage(
                    image_crop,
                    os.path.join(
                        outpath,
                        "images",
                        ("{}_{:0" + regexpr + "d}{}").format(
                            image_name, obj, image_ext
                        ),
                    ),
                )
                saveimage(
                    label_crop,
                    os.path.join(
                        outpath,
                        "labels",
                        ("{}_{:0" + regexpr + "d}{}").format(
                            image_name, obj, image_ext
                        ),
                    ),
                )
                obj += 1
