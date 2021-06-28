import math
import numpy as np
import torch
from scipy import ndimage
from scipy.ndimage import rotate
from skimage.transform import resize
import itertools
from .grid_sample import grid_sample
from torch.autograd import Variable
from .tps_grid_gen import TPSGridGen
from skimage.filters.rank import median

from netframework import load_defaults, save_defaults


class NormalizePercentile(object):
    @save_defaults
    @load_defaults
    def __init__(self, is_3D=False):
        self.is_3D = is_3D

    def __call__(self, sample):
        image = sample["image"]
        image = image.astype(np.float)
        minp = np.percentile(image, 1)
        maxp = np.percentile(image, 99)
        if (
            "".join(
                [
                    chr(item)
                    for item in image[:, :, 0].astype("int").flatten()[0:4]
                ]
            )
            == "norm"
        ):
            minp = image[:, :, 0].flatten()[4]
            maxp = image[:, :, 0].flatten()[5]

        image = (image - minp) / (maxp - minp)

        sample["image"] = image
        return sample

    def __repr__(self):
        return "NormalizePercentile(is_3D={})".format(self.is_3D)


class Normalize(object):
    @save_defaults
    @load_defaults
    def __init__(self, is_3D=False):
        self.is_3D = is_3D

    def __call__(self, sample):
        image = sample["image"]
        scale = 65535.0 if image.dtype == np.dtype("uint16") else 255.0

        image = image.astype(np.float) / scale

        sample["image"] = image
        return sample

    def __repr__(self):
        return "Normalize(is_3D={})".format(self.is_3D)


class ToTensor(object):
    @save_defaults
    @load_defaults
    def __init__(self, is_3D=False):
        self.is_3D = is_3D

    def __repr__(self):
        return "ToTensor(is_3D={})".format(self.is_3D)

    def __call__(self, sample):
        image, label = sample["image"], sample["label"]

        scale = (
            65535.0
            if image.dtype == np.dtype("uint16")
            else (255.0 if image.dtype == np.dtype("uint8") else 1.0)
        )

        if self.is_3D:
            if image.ndim == 3:
                image = image[:, :, np.newaxis, :]

            image = np.array((image.astype(np.float) / scale)).transpose(
                (2, 3, 0, 1)
            )
            label = np.rint(np.array(label)).transpose((2, 0, 1))
        else:

            image = np.array(
                (image.astype(np.float) / scale).transpose((2, 0, 1))
            )
            if label.ndim == 3:
                label = label[..., 0]
            label = np.rint(np.array(label))

        output = {
            "image": torch.from_numpy(image).float(),
            "label": torch.from_numpy(label).long(),
        }

        if "weight" in sample:
            weight = np.array(sample["weight"])
            if self.is_3D:
                weight = weight.transpose((2, 0, 1))

            output["weight"] = torch.from_numpy(weight).float()

        return output


class Warping(object):
    @save_defaults
    @load_defaults
    def __init__(self, size_grid, deform, is_3D=False):
        self.size_grid = size_grid
        self.deform = deform
        self.is_3D = is_3D

    def __repr__(self):
        return "Warping(size_grid={}, deform={}, is_3D={})".format(
            self.size_grid, self.deform, self.is_3D
        )

    def __call__(self, sample):
        assert (
            not self.is_3D
        ), "Warping transformation is only supported for 2D"
        size_grid = self.size_grid
        deforma = self.deform

        image, label = sample["image"], sample["label"]
        target_width, target_height = image.size(1), image.size(2)
        target_control_points = torch.Tensor(
            list(
                itertools.product(
                    torch.arange(-1.0, 1.00001, 2.0 / (size_grid - 1)),
                    torch.arange(-1.0, 1.00001, 2.0 / (size_grid - 1)),
                )
            )
        )
        source_control_points = target_control_points + torch.Tensor(
            target_control_points.size()
        ).uniform_(-deforma, deforma)
        tps = TPSGridGen(target_height, target_width, target_control_points)
        source_coordinate = tps(
            Variable(torch.unsqueeze(source_control_points, 0))
        )
        grid = source_coordinate.view(1, target_height, target_width, 2)
        wimage = grid_sample(torch.unsqueeze(image, 0), grid)
        wlabel = grid_sample(
            torch.unsqueeze(torch.unsqueeze(label.float(), 0), 0), grid
        ).round()

        output = {
            "image": wimage.squeeze(0),
            "label": wlabel.squeeze(0).squeeze(0),
        }

        if "weight" in sample:
            weight = np.array(sample["weight"])
            wweight = grid_sample(
                torch.unsqueeze(torch.unsqueeze(weight, 0), 0), grid
            )
            output["weight"] = wweight.squeeze(0).squeeze(0)

        return output


class Rotation(object):
    @save_defaults
    @load_defaults
    def __init__(self, angle, is_3D=False):
        self.angle = angle
        self.is_3D = is_3D

    def __repr__(self):
        return "Rotation(angle={}, is_3D={})".format(self.angle, self.is_3D)

    def __call__(self, sample):
        image, label = sample["image"], sample["label"]

        angle_rand = np.random.uniform(-self.angle, self.angle)
        if self.is_3D:
            axes = tuple(np.random.permutation(3)[:2])
            axes_images = axes
            if image.ndim != 3:
                axes_images = tuple(
                    [ax if ax != 2 else 3 for ax in list(axes_images)]
                )
        else:
            axes = (1, 0)
            axes_images = axes

        rot_image = rotate(
            image, angle=angle_rand, axes=axes_images, reshape=False
        )
        rot_label = rotate(
            label, angle=angle_rand, axes=axes, reshape=False, order=0
        )

        output = {"image": rot_image, "label": rot_label}

        if "weight" in sample:
            weight = np.array(sample["weight"])
            rot_weight = rotate(
                weight, angle=angle_rand, axes=axes, reshape=False
            )
            output["weight"] = rot_weight

        return output


class RandomFlip(object):
    @save_defaults
    @load_defaults
    def __init__(self, prob, is_3D=False):
        self.prob = prob
        self.is_3D = is_3D

    def __repr__(self):
        return "RandomFlip(prob={}, is_3D={})".format(self.prob, self.is_3D)

    def __call__(self, sample):
        image, label = sample["image"], sample["label"]

        if np.random.rand(1) < self.prob:
            if self.is_3D:
                axis = np.random.randint(3)
                axis_images = axis
                if image.ndim != 3 and axis == 2:
                    axis_images = 3
            else:
                axis = np.random.randint(2)
                axis_images = axis

            image = np.flip(image, axis=axis_images)
            label = np.flip(label, axis=axis)

            output = {"image": image, "label": label}

            if "weight" in sample:
                weight = np.array(sample["weight"])
                weight = np.flip(weight, axis=axis)
                output["weight"] = weight
        else:
            output = sample

        return output


class RandomCrop(object):
    @save_defaults
    @load_defaults
    def __init__(self, output_size, is_3D=False):
        assert isinstance(output_size, (int, tuple))
        if isinstance(output_size, int):
            self.output_size = (output_size, output_size, output_size)
        else:
            assert (
                len(output_size) == 3 or len(output_size) == 2
            ), "RandomCrop size is expected to have length two or three"
            self.output_size = output_size

        if len(self.output_size) == 2:
            self.output_size += (min(self.output_size),)
        self.is_3D = is_3D

    def __repr__(self):
        return "RandomCrop(output_size={}, is_3D={})".format(
            self.output_size, self.is_3D
        )

    def __call__(self, sample):
        new_h, new_w, new_z = self.output_size
        image, label = sample["image"], sample["label"]

        if not self.is_3D:
            image = image[..., np.newaxis]
            label = label[..., np.newaxis]
            new_z = 1

        h, w, z = label.shape[:3]
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
        label = np.lib.pad(
            label,
            (
                (math.floor(self.pad_sizeh), math.ceil(self.pad_sizeh)),
                (math.floor(self.pad_sizew), math.ceil(self.pad_sizew)),
                (math.floor(self.pad_sizez), math.ceil(self.pad_sizez)),
            ),
            "constant",
            constant_values=0,
        )
        h, w, z = label.shape[:3]

        new_h = h if new_h >= h else new_h
        new_w = w if new_w >= w else new_w
        new_z = z if new_z >= z else new_z

        top = np.random.randint(0, h - new_h + 1)
        left = np.random.randint(0, w - new_w + 1)
        depth = np.random.randint(0, z - new_z + 1)

        image = image[
            top : top + new_h, left : left + new_w, :, depth : depth + new_z
        ]
        label = label[
            top : top + new_h, left : left + new_w, depth : depth + new_z
        ]

        if not self.is_3D:
            image = image[..., 0]
            label = label[..., 0]

        output = {"image": image, "label": label}

        if "weight" in sample:
            weight = np.array(sample["weight"])
            if not self.is_3D:
                weight = weight[..., np.newaxis]

            weight = np.lib.pad(
                weight,
                (
                    (math.floor(self.pad_sizeh), math.ceil(self.pad_sizeh)),
                    (math.floor(self.pad_sizew), math.ceil(self.pad_sizew)),
                    (math.floor(self.pad_sizez), math.ceil(self.pad_sizez)),
                ),
                "constant",
                constant_values=0,
            )
            weight = weight[
                top : top + new_h,
                left : left + new_w,
                depth : depth + new_z,
            ]
            if not self.is_3D:
                weight = weight[..., 0]
            output["weight"] = weight

        return output


class TouchAugment(object):
    @save_defaults
    @load_defaults
    def __init__(self, gamma=None, is_3D=False):
        self.gamma = gamma
        self.is_3D = is_3D

    def __repr__(self):
        return "TouchAugment(gamma={}, is_3D={})".format(
            self.gamma, self.is_3D
        )

    def __call__(self, sample):
        assert not self.is_3D, "Touch Augmentation not supported for 3D"
        image, label = (sample["image"], sample["label"])

        image = image[:, :, 0]
        if image.dtype == np.dtype("uint16"):
            scale = 65535.0
        else:
            scale = 255.0
        image = image.astype("float") / scale

        touch = ndimage.binary_dilation(
            label == 2, structure=np.ones((3, 3))
        ).astype("float") * (1 - (label == 0).astype("float"))

        cell = (label == 1).astype("float")

        mc = (
            median(image, np.ones((7, 7)), mask=cell) * touch / scale
            + 0.015 * np.random.normal(size=touch.shape) * touch
        )
        mb = np.median(image[label == 0]) + 0.2

        if self.gamma is None:
            gamma = np.random.rand() * 2 - 1
        else:
            a, b = self.gamma
            gamma = np.random.rand() * (b - a) + a

        a = gamma * mc
        m = (1 - gamma) * np.ones(a.shape)

        J = image.copy()
        touch = touch == 1
        J[touch] = m[touch] * image[touch] + a[touch]
        J[J < mb] = image[J < mb]
        J[J > 1] = 1

        if image.dtype == np.dtype("uint16"):
            image = (J * 65535).astype("uint16")
        else:
            image = (J * 255).astype("uint8")

        image = np.repeat(image[:, :, np.newaxis], 3, axis=2)

        output = {"image": image, "label": label}
        if "weight" in sample:
            output["weight"] = sample["weight"]

        return output


class GammaAugment(object):
    @save_defaults
    @load_defaults
    def __init__(self, gamma=None, is_3D=False):
        self.gamma = gamma
        self.is_3D = is_3D

    def __repr__(self):
        return "GammaAugment(gamma={}, is_3D={})".format(
            self.gamma, self.is_3D
        )

    def __call__(self, sample):
        image, label = (
            sample["image"],
            sample["label"],
        )

        if image.dtype == np.dtype("uint16"):
            scale = 65535.0
        else:
            scale = 255.0
        image = image.astype("float") / scale

        if self.gamma is None:
            if np.random.rand() < 0.5:
                gamma = np.random.rand() * 0.5 + 0.3
            else:
                gamma = np.random.rand() * 1 + 1
        else:
            gamma = self.gamma

        if image.dtype == np.dtype("uint16"):
            image = (65535 * (image ** gamma)).astype("uint16")
        else:
            image = (255 * (image ** gamma)).astype("uint8")

        output = {"image": image, "label": label}
        if "weight" in sample:
            output["weight"] = sample["weight"]

        return output