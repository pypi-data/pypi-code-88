import os
import numpy as np
from scipy.ndimage import (
    generic_filter,
    binary_dilation,
    binary_closing,
)

from skimage.morphology import ball

try:
    from llc import jit_filter_function
except Exception:

    def jit_filter_function(filter_function):
        return filter_function


try:
    from ..imageutl import saveimage
except Exception:
    from imageutl import saveimage


def inst2sem(L, se1_radius, se2_radius, output=None):
    """
    3D Instance to 4-classes semantic label transformation.
    The label file is expected to be an 8bit/16bits 1-channel volume with where each
    object has their own identifier.
    The output will be an 8bits 1-channel volume with semantic classes.
    """
    if L.ndim == 4:
        L = L[:, :, 0, :].squeeze()

    H = inst2sem3d(L, se1_radius)
    if se2_radius > 0:
        H = sem32sem43d(H, se2_radius)

    if output is not None:
        output, name = os.path.split(output)
        name, ext = os.path.splitext(name)
        if not os.path.isdir(output):
            raise ValueError("{} does not exist".format(output))
        if not name:
            raise ValueError("Please, specify a valid file name")
        if not ext:
            ext = ".tif"

        saveimage(H.astype("uint8"), os.path.join(output, name + ext))

    return H.astype(np.uint8)


def sem32sem43d(S, se):
    """
    3 semantic classes to 4 semantic classes transformation
    """
    S = np.lib.pad(
        S, ((se, se), (se, se), (se, se)), "constant", constant_values=0
    )

    B = 1 - (S == 0).astype("uint8")
    B = binary_closing(B, structure=ball(se)).astype("uint8") - B
    S[B == 1] = 3

    if se > 0:
        S = S[se:-se, se:-se, se:-se]
    return S


def inst2sem3d(inst, se=3):
    """
    3D Instance to 3 classes semantic label transformation
    """
    inst = np.lib.pad(
        inst, ((se, se), (se, se), (se, se)), "constant", constant_values=0
    )
    gt = (inst > 0).astype("uint16")

    @jit_filter_function
    def filter(neigh):
        center = len(neigh) // 2
        return (
            (neigh[center] != 0) * (neigh[center] != neigh) * (neigh != 0)
        ).sum()

    se2 = se if se >= 3 else 3
    I2 = generic_filter(inst, filter, size=se2)
    I2[I2 > 0] = 1
    if se > 0:
        I2 = binary_dilation(I2 > 0, structure=ball(se))
    gt[I2 > 0] = 2

    if se > 0:
        gt = gt[se:-se, se:-se, se:-se]
    return gt
