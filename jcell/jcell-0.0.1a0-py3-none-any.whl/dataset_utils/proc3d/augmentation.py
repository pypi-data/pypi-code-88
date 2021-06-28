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
    volume,
    label,
    outpath,
    block_size_x=0,
    block_size_y=0,
    block_size_z=0,
    gamma_transform=True,
    ignore_empty=True,
    regexpr="",
):
    """
    Data augmentation for 3D image segmentation
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

    transpose_volume = False
    if volume.shape[2] <= 3:
        volume = volume.transpose((0, 1, 3, 2))
        transpose_volume = True

    transpose_label = False
    if label.shape[2] <= 3:
        label = label.transpose((0, 1, 3, 2))
        transpose_label = True

    num_rows = block_size_x if block_size_x > 0 else volume.shape[0]
    num_cols = block_size_y if block_size_y > 0 else volume.shape[1]
    samples = block_size_z if block_size_z > 0 else volume.shape[2]
    volume_shape = list(volume.shape)

    obj = 0
    for k in range(math.ceil(volume_shape[2] / samples)):
        for j in range(math.ceil(volume_shape[1] / num_cols)):
            for x in range(math.ceil(volume_shape[0] / num_rows)):
                for flipc in range(8):
                    xr = x * num_rows
                    yr = j * num_cols
                    zr = k * samples
                    offsetx = (
                        volume_shape[0] - (xr + num_rows)
                        if (xr + num_rows) > volume_shape[0]
                        else 0
                    )
                    offsety = (
                        volume_shape[1] - (yr + num_cols)
                        if (yr + num_cols) > volume_shape[1]
                        else 0
                    )
                    offsetz = (
                        volume_shape[2] - (zr + samples)
                        if (zr + samples) > volume_shape[2]
                        else 0
                    )
                    xr += offsetx
                    yr += offsety
                    zr += offsetz

                    volume_crop = volume[
                        xr : xr + num_rows,
                        yr : yr + num_cols,
                        zr : zr + samples,
                        ...,
                    ]
                    label_crop = label[
                        xr : xr + num_rows,
                        yr : yr + num_cols,
                        zr : zr + samples,
                        ...,
                    ]

                    if label_crop.sum() == 0 and ignore_empty:
                        continue

                    flip_comb = int(bin(flipc)[2:])
                    flip_x = flip_comb % 10
                    flip_comb = flip_comb // 10
                    flip_y = flip_comb % 10
                    flip_comb = flip_comb // 10
                    flip_z = flip_comb % 10

                    if flip_x == 1:
                        volume_crop = np.flip(volume_crop, 0)
                        label_crop = np.flip(label_crop, 0)
                    if flip_y == 1:
                        volume_crop = np.flip(volume_crop, 1)
                        label_crop = np.flip(label_crop, 1)
                    if flip_z == 2:
                        volume_crop = np.flip(volume_crop, 2)
                        label_crop = np.flip(label_crop, 2)

                    if gamma_transform > 1:
                        if random.random() < 0.5:
                            gamma = random.random() * 0.5 + 0.3
                        else:
                            gamma = random.random() + 1

                        if volume_crop.dtype == np.dtype("uint8"):
                            volume_crop = (
                                ((volume_crop.astype("float") / 255) ** gamma)
                                * 255
                            ).astype("uint8")
                        elif volume_crop.dtype == np.dtype("uint16"):
                            volume_crop = (
                                (
                                    (volume_crop.astype("float") / 65535)
                                    ** gamma
                                )
                                * 65535
                            ).astype("uint16")
                        else:
                            warnings.warn(
                                "{} not supported. Skipping gamma augmentation".format(
                                    volume_crop.dtype
                                )
                            )

                    if transpose_volume:
                        volume_crop = volume_crop.transpose((0, 1, 3, 2))

                    if transpose_label:
                        label_crop = label_crop.transpose((0, 1, 3, 2))

                    saveimage(
                        volume_crop,
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
