# code in this file is adpated from
# https://github.com/ildoonet/pytorch-randaugment/blob/master/RandAugment/augmentations.py
# https://github.com/google-research/fixmatch/blob/master/third_party/auto_augment/augmentations.py
# https://github.com/google-research/fixmatch/blob/master/libml/ctaugment.py
# https://github.com/kekmodel/FixMatch-pytorch/blob/master/dataset/randaugment.py
import random

import numpy as np
from PIL import ImageOps, ImageEnhance, ImageDraw, Image


MAX_LEVEL = 10

# TODO: update this file by merging YbZhang's code in Transfer-Learn repository to let RandAug support Domain Adaptation task
def AutoContrast(img, **kwarg):
    # some function don't need v and max_v, so use kwargs as a placeholder
    return ImageOps.autocontrast(img)


def Brightness(img, level, max_v, bias=0):
    v = _float_parameter(level, max_v) + bias
    return ImageEnhance.Brightness(img).enhance(v)


def Color(img, level, max_v, bias=0):
    v = _float_parameter(level, max_v) + bias
    return ImageEnhance.Color(img).enhance(v)


def Contrast(img, level, max_v, bias=0):
    v = _float_parameter(level, max_v) + bias
    return ImageEnhance.Contrast(img).enhance(v)


def Cutout(img, level, max_v, bias=0):
    if level == 0:
        return img
    v = _float_parameter(level, max_v) + bias
    v = int(v * min(img.size))
    return CutoutAbs(img, v)


def CutoutAbs(img, v):
    w, h = img.size
    x0 = np.random.uniform(0, w)
    y0 = np.random.uniform(0, h)
    x0 = int(max(0, x0 - v / 2.))
    y0 = int(max(0, y0 - v / 2.))
    x1 = int(min(w, x0 + v))
    y1 = int(min(h, y0 + v))
    xy = (x0, y0, x1, y1)
    # gray
    color = (127, 127, 127)
    img = img.copy()
    ImageDraw.Draw(img).rectangle(xy, color)
    return img


def Equalize(img, **kwarg):
    return ImageOps.equalize(img)


def Identity(img, **kwarg):
    return img


def Invert(img, **kwarg):
    return ImageOps.invert(img)


def Posterize(img, level, max_v, bias=0):
    v = _int_parameter(level, max_v) + bias
    return ImageOps.posterize(img, v)


def Rotate(img, level, max_v, bias=0):
    v = _int_parameter(level, max_v) + bias
    if random.random() < 0.5:
        v = -v
    return img.rotate(v)


def Sharpness(img, level, max_v, bias=0):
    v = _float_parameter(level, max_v) + bias
    return ImageEnhance.Sharpness(img).enhance(v)


def ShearX(img, level, max_v, bias=0):
    v = _float_parameter(level, max_v) + bias
    if random.random() < 0.5:
        v = -v
    return img.transform(img.size, Image.AFFINE, (1, v, 0, 0, 1, 0))


def ShearY(img, level, max_v, bias=0):
    v = _float_parameter(level, max_v) + bias
    if random.random() < 0.5:
        v = -v
    return img.transform(img.size, Image.AFFINE, (1, 0, 0, v, 1, 0))


def Solarize(img, level, max_v, bias=0):
    v = _int_parameter(level, max_v) + bias
    return ImageOps.solarize(img, 256 - v)


def SolarizeAdd(img, level, max_v, bias=0, threshold=128):
    v = _int_parameter(level, max_v) + bias
    if random.random() < 0.5:
        v = -v
    img_np = np.array(img).astype(np.int)
    img_np = img_np + v
    img_np = np.clip(img_np, 0, 255)
    img_np = img_np.astype(np.uint8)
    img = Image.fromarray(img_np)
    return ImageOps.solarize(img, threshold)


def TranslateX(img, level, max_v, bias=0):
    v = _float_parameter(level, max_v) + bias
    if random.random() < 0.5:
        v = -v
    v = int(v * img.size[0])
    return img.transform(img.size, Image.AFFINE, (1, 0, v, 0, 1, 0))


def TranslateY(img, level, max_v, bias=0):
    v = _float_parameter(level, max_v) + bias
    if random.random() < 0.5:
        v = -v
    v = int(v * img.size[1])
    return img.transform(img.size, Image.AFFINE, (1, 0, 0, 0, 1, v))


def _float_parameter(level, max_v):
    r"""
    Args:
        level (integer): discretized magnitude level of variable ranging in [0, MAX_LEVEL]
        max_v (float): max value of variable
    Return:
        actual variable value range in [0, max_v]
    """
    return float(level) * max_v / MAX_LEVEL


def _int_parameter(v, max_v):
    return int(v * max_v / MAX_LEVEL)


def fixmatch_augment_pool():
    # Table 12 in paper: FixMatch: Simplifying Semi-Supervised Learning with Consistency and Confidence
    augs = [(AutoContrast, None, None),
            (Brightness, 0.9, 0.05),  # [0.05, 0.95]
            (Color, 0.9, 0.05),       # [0.05, 0.95]
            (Contrast, 0.9, 0.05),    # [0.05, 0.95]
            (Equalize, None, None),
            (Identity, None, None),
            (Posterize, 4, 4),        # [4, 8]
            (Rotate, 30, 0),          # [-30, 30]
            (Sharpness, 0.9, 0.05),   # [0.05, 0.95]
            (ShearX, 0.3, 0),         # [-0.3, 0.3]
            (ShearY, 0.3, 0),         # [-0.3, 0.3]
            (Solarize, 256, 0),       # [0, 256]
            (TranslateX, 0.3, 0),     # [-0.3, 0.3]
            (TranslateY, 0.3, 0)]     # [-0.3, 0.3]

    return augs


class RandAugment(object):
    def __init__(self, n, m, cutout_size=112):
        r"""Author: zhang.haojian
        RandAugment with image cutout (that is to say, FixMatch version of RandAugment)
        Args:
            n (int): number of transforms
            m (int): number of variable value level
            cutout_size (int): maximum cutout size of an image. It should be less than min(img.shape) // 2
        """
        assert n >= 1
        assert 1 <= m <= 10
        self.n = n
        self.m = m
        self.cutout_size = cutout_size
        self.augment_pool = fixmatch_augment_pool()

    def __call__(self, img):
        # apply different transformation for each image, rather than the same transformation for a batch
        ops = random.choices(self.augment_pool, k=self.n)
        for op, max_v, bias in ops:
            # default setting in official implementation is to discretize the parameter space like here
            level = np.random.randint(0, self.m + 1)
            # NOTE: in official implementation there is an equivalent `prob_to_apply`
            if random.random() < 0.5:
                img = op(img, level=level, max_v=max_v, bias=bias)
        # we follow fixmatch version where RandAugment includes cutout, while the one in original paper not
        img = CutoutAbs(img, self.cutout_size)
        return img
