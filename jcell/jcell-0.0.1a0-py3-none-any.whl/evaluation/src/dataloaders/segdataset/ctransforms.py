import math
import torch
import numpy as np
from tqdm import tqdm

from ....src import save_defaults, load_defaults


class SplitImage(object):
    """
    Chunking image according to a given patch size
    """

    @save_defaults
    @load_defaults
    def __init__(self, output_size, overlapping=5, is_3D=False):
        assert isinstance(
            output_size, (int, tuple, list)
        ), "Chunk image size must be given as an int, tuple, or list"
        if isinstance(output_size, int):
            self.output_size = (output_size, output_size, output_size)
        else:
            assert (
                len(output_size) == 2 or len(output_size) == 3
            ), "Chunk image size must have either two or three integers"
            self.output_size = output_size
        self.step = math.floor(min(self.output_size) * 0.1)  # overlapping
        self.is_3D = is_3D

    def __call__(self, image):
        new_h, new_w = self.output_size[:2]

        if not self.is_3D:
            image = image[..., np.newaxis]
            new_z = 1

        h, w, c, z = image.shape[:4]

        if self.is_3D and len(self.output_size) == 2:
            self.output_size += [z]

        if self.is_3D:
            new_z = self.output_size[2]

        # Do zero padding if size smaller than required
        self.pad_sizeh = (new_h - h) / 2 if h < new_h else 0
        self.pad_sizew = (new_w - w) / 2 if w < new_w else 0
        self.pad_sizez = (new_z - z) / 2 if z < new_z else 0
        image = np.lib.pad(
            image,
            (
                (math.floor(self.pad_sizeh), math.ceil(self.pad_sizeh)),
                (math.floor(self.pad_sizew), math.ceil(self.pad_sizew)),
                (0, 0),
                (math.floor(self.pad_sizez), math.ceil(self.pad_sizez)),
            ),
            "constant",
            constant_values=0,
        )
        h, w, c, z = image.shape[:4]

        # Set overlapping
        stepx = h if new_h == h else new_h - self.step
        stepy = w if new_w == w else new_w - self.step
        stepz = z if new_z == z else new_z - self.step

        nblockx = int(np.ceil(float(h) / stepx))
        nblocky = int(np.ceil(float(w) / stepy))
        nblockz = int(np.ceil(float(z) / stepz))

        nimage = np.zeros(
            (nblockx * nblocky * nblockz, new_h, new_w, c, new_z),
            dtype=image.dtype,
        )

        if nblocky * nblockx * nblockz > 1:
            pbar = tqdm(
                total=nblocky * nblockx * nblockz,
                desc="Splitting image",
                position=1,
                leave=False,
            )
        for k in range(nblockz):
            for j in range(nblocky):
                for i in range(nblockx):
                    offsetx = (
                        h - (i * stepx + new_h) if i * stepx + new_h > h else 0
                    )
                    offsety = (
                        w - (j * stepy + new_w) if j * stepy + new_w > w else 0
                    )
                    offsetz = (
                        z - (k * stepz + new_z) if k * stepz + new_z > z else 0
                    )

                    nimage[
                        k * nblockx * nblocky + j * nblockx + i, ...
                    ] = image[
                        i * stepx + offsetx : i * stepx + new_h + offsetx,
                        j * stepy + offsety : j * stepy + new_w + offsety,
                        :,
                        k * stepz + offsetz : k * stepz + new_z + offsetz,
                    ]
                    if nblocky * nblockx * nblockz > 1:
                        pbar.update()

        if nblocky * nblockx * nblockz > 1:
            pbar.close()

        self.nblockx, self.nblocky, self.nblockz = nblockx, nblocky, nblockz
        self.h, self.w, self.z = h, w, z

        if not self.is_3D:
            nimage = nimage[..., 0]

        return nimage

    def uncall(self, nimage):
        new_h, new_w = self.output_size[:2]
        if not self.is_3D:
            nimage = nimage[:, :, np.newaxis, :, :]
            new_z = 1
        else:
            new_z = self.output_size[2]

        c = nimage.shape[1]

        nblockx, nblocky, nblockz = self.nblockx, self.nblocky, self.nblockz

        h, w, z = self.h, self.w, self.z
        stepx = h if new_h == h else new_h - self.step
        stepy = w if new_w == w else new_w - self.step
        stepz = z if new_z == z else new_z - self.step

        image = np.zeros((c, z, h, w))
        indimage = np.zeros((c, z, h, w))

        if nblocky * nblockx * nblockz > 1:
            pbar = tqdm(
                total=nblocky * nblockx * nblockz,
                desc="Merging image",
                position=1,
                leave=False,
            )
        for k in range(nblockz):
            for j in range(nblocky):
                for i in range(nblockx):
                    offsetx = (
                        h - (i * stepx + new_h) if i * stepx + new_h > h else 0
                    )
                    offsety = (
                        w - (j * stepy + new_w) if j * stepy + new_w > w else 0
                    )
                    offsetz = (
                        z - (k * stepz + new_z) if k * stepz + new_z > z else 0
                    )
                    oblock = nimage[
                        k * nblockx * nblocky + j * nblockx + i, :, :, :, :
                    ]

                    indimage[
                        :,
                        k * stepz + offsetz : k * stepz + new_z + offsetz,
                        i * stepx + offsetx : i * stepx + new_h + offsetx,
                        j * stepy + offsety : j * stepy + new_w + offsety,
                    ] += 1
                    iblock = indimage[
                        :,
                        k * stepz + offsetz : k * stepz + new_z + offsetz,
                        i * stepx + offsetx : i * stepx + new_h + offsetx,
                        j * stepy + offsety : j * stepy + new_w + offsety,
                    ]
                    mblock = image[
                        :,
                        k * stepz + offsetz : k * stepz + new_z + offsetz,
                        i * stepx + offsetx : i * stepx + new_h + offsetx,
                        j * stepy + offsety : j * stepy + new_w + offsety,
                    ]

                    image[
                        :,
                        k * stepz + offsetz : k * stepz + new_z + offsetz,
                        i * stepx + offsetx : i * stepx + new_h + offsetx,
                        j * stepy + offsety : j * stepy + new_w + offsety,
                    ] = (oblock + self.minus1(iblock) * mblock) / iblock

                    if nblocky * nblockx * nblockz > 1:
                        pbar.update()

        if nblocky * nblockx * nblockz > 1:
            pbar.close()

        image = image[np.newaxis, ...]
        if self.pad_sizeh != 0:
            image = image[
                :,
                :,
                :,
                math.floor(self.pad_sizeh) : -math.ceil(self.pad_sizeh),
                :,
            ]
        if self.pad_sizew != 0:
            image = image[
                :,
                :,
                :,
                :,
                math.floor(self.pad_sizew) : -math.ceil(self.pad_sizew),
            ]
        if self.pad_sizez != 0:
            image = image[
                :,
                :,
                math.floor(self.pad_sizez) : -math.ceil(self.pad_sizez),
                :,
                :,
            ]

        if not self.is_3D:
            image = image[:, :, 0, :, :]

        return torch.from_numpy(image).float()

    def minus1(self, vol):
        return (vol - 1) + (vol <= 1).astype(int)


class NormalizePercentile(object):
    @save_defaults
    @load_defaults
    def __init__(self, is_3D=False):
        self.is_3D = is_3D

    def __call__(self, image):
        image = image.astype(np.float)
        if self.is_3D:
            minp = np.percentile(image, 1)
            maxp = np.percentile(image, 99)
            image = (image - minp) / (maxp - minp)
        else:
            minp = np.percentile(image, 1)
            maxp = np.percentile(image, 99)
            image = (image - minp) / (maxp - minp)

        return image


class Normalize(object):
    @save_defaults
    @load_defaults
    def __init__(self, is_3D=False):
        self.is_3D = is_3D

    def __call__(self, image):
        scale = 65535.0 if image.dtype == np.dtype("uint16") else 255.0

        image = image.astype(np.float) / scale

        return image


class ToTensorImage(object):
    @save_defaults
    @load_defaults
    def __init__(self, is_3D=False):
        self.is_3D = is_3D

    def __call__(self, image):
        if self.is_3D:
            image = (
                np.array((image).transpose((0, 3, 4, 1, 2)))
                if len(image.shape) == 5
                else np.array((image).transpose((2, 3, 0, 1)))
            )
        else:
            image = (
                np.array((image).transpose((0, 3, 1, 2)))
                if len(image.shape) == 4
                else np.array((image).transpose((2, 0, 1)))
            )

        return torch.from_numpy(image).float()
