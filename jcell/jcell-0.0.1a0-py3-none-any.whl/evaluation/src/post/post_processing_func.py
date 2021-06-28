import numpy as np
from skimage.morphology import label, remove_small_objects
from scipy import ndimage
from skimage.segmentation import find_boundaries, watershed

from ...src import save_defaults, load_defaults


def prob42prob3(prob, assign="back"):
    if prob.shape[-1] == 4:
        if assign == "max":
            # assign gap to max
            map3 = np.argmax((prob[..., :3] * 255).astype(int), axis=-1)
            for m3i in range(3):
                prob[..., m3i] = prob[..., m3i] + prob[..., 3] * (
                    map3 == m3i
                ).astype(int)
            prob = prob[..., :3]

        elif assign == "back":
            # assign gap to back
            prob[..., 0] = prob[..., 0] + prob[..., 3]
            prob = prob[..., :3]

        elif assign == "unif":
            # distribute gap to equally
            for m3i in range(3):
                prob[..., m3i] = prob[..., m3i] / (
                    1 - prob[..., 3] + np.finfo(float).eps
                )
            prob = prob[..., :3]

    return prob


def sem2inst(output):
    prediction = np.array(output == 1).astype(int)
    predictionlb = label(prediction, background=0, connectivity=None)
    back = 1 - np.array(output == 0).astype(int)

    pmf = predictionlb
    if output.max() > 1:
        change = True
        pmf = predictionlb
        while change:
            mf = ndimage.maximum_filter(pmf, size=3)
            mf = mf * back
            chg = (pmf != mf) & (pmf != 0)
            mf[chg] = pmf[chg]
            dif = np.sum(np.abs(mf - pmf))
            pmf = mf
            change = dif > 0

    return pmf


def inst2sem(label):
    touch = np.zeros_like(label)

    fore = np.array(label > 0).astype(np.uint8)
    contour_in = fore - ndimage.binary_erosion(fore)

    touch = find_boundaries(
        label, mode="inner", background=0, connectivity=2
    ).astype(np.uint8) * (1 - contour_in).astype(np.uint8)
    touch = remove_small_objects(touch == 1, 10, connectivity=1).astype(
        np.uint8
    )
    touch = ndimage.binary_dilation(touch) * np.array(label != 0).astype(
        np.uint8
    )

    region3 = np.array(label > 0).astype(np.uint8) + touch
    region = np.array(label > 0).astype(np.uint8) - touch

    return region, region3


def fix_prob2(prob4):
    bic_cell = 0.1  # bias coefficient
    bic = 0.98  # bias coefficient
    eps = 1e-4

    bg = prob4[..., 0]
    cell = prob4[..., 1]
    touch = prob4[..., 2]
    gap = prob4[..., 3]
    MAP = np.argmax(prob4, axis=-1)

    bg_bias = bg + gap
    cd1 = (bg_bias > 0.5) | ((bg_bias > bic * cell) & (bg_bias > bic * touch))
    bg[cd1] = 1.0
    gap[cd1] = 0
    cell[cd1] = 0
    touch[cd1] = 0
    MAP[cd1] = 0

    cd2 = ((MAP == 2) & ((bg_bias - cell) > eps)) & (~cd1)
    bg[cd2] = 1.0
    gap[cd2] = 0
    cell[cd2] = 0
    touch[cd2] = 0
    MAP[cd2] = 0

    cd3 = (((MAP == 1) & (touch > bic_cell)) | (touch > 0.5)) & (~(cd1 & cd2))
    bg[cd3] = 0
    gap[cd3] = 0
    cell[cd3] = 0
    touch[cd3] = 1
    MAP[cd3] = 2

    res = np.concatenate(
        (
            bg[..., np.newaxis],
            cell[..., np.newaxis],
            touch[..., np.newaxis],
            gap[..., np.newaxis],
        ),
        axis=-1,
    )
    return res


class TH_post(object):
    def __init__(self, cellclass=1, diviclass=2):
        self.cellclass = cellclass
        self.diviclass = diviclass

    @save_defaults
    @load_defaults
    def __call__(
        self,
        output,
        thresh_cell=0.49,
        thresh_div=0.05,
        morph_se=0,
        prob4="back",
        min_area=0,
    ):
        _argmax = np.argmax(output, axis=-1).astype(np.uint8)
        morph, thresh, threshdiv = morph_se, thresh_cell, thresh_div
        output = prob42prob3(output, prob4)

        if output.shape[-1] > 1:
            cellsprob = output[..., self.cellclass]
        else:
            cellsprob = output

        prediction = np.array(cellsprob >= thresh).astype(int)
        diff = np.zeros_like(prediction)
        if morph > 0:
            se = (
                np.ones((morph, morph))
                if prediction.ndim == 2
                else np.ones((morph, morph, morph))
            )
            prediction1 = ndimage.binary_opening(
                prediction, structure=se, iterations=2
            ).astype(int)
            diff = prediction - prediction1
            prediction = prediction1

        if output.shape[-1] > 2:
            divis = output[..., self.diviclass]
            divis = np.array(divis >= threshdiv).astype(int) + diff
            prediction[divis.astype(bool)] = 0
            divis[prediction.astype(bool)] = 0
            prediction = self.cellclass * prediction + self.diviclass * divis

        predictionlb = sem2inst(prediction)
        if min_area > 0:
            predictionlb = remove_small_objects(
                predictionlb, min_area, connectivity=1, in_place=True
            ).astype(int)
        region, prediction = inst2sem(predictionlb)

        return predictionlb, prediction, region, output, _argmax


class MAP_post(object):
    def __init__(self, cellclass=1, diviclass=2):
        self.cellclass = cellclass
        self.diviclass = diviclass

    @save_defaults
    @load_defaults
    def __call__(self, output, morph_se=0, prob4="back", min_area=0):
        _argmax = np.argmax(output, axis=-1).astype(np.uint8)
        fsize, morph = min_area, morph_se
        output = fix_prob2(output)
        output = prob42prob3(output, prob4)

        MAP = np.argmax(output, axis=-1)
        prediction = (MAP == self.cellclass).astype(int)
        diff = np.zeros_like(prediction)
        if morph > 0:
            se = (
                np.ones((morph, morph))
                if prediction.ndim == 2
                else np.ones((morph, morph, morph))
            )
            prediction1 = ndimage.binary_opening(
                prediction, structure=se, iterations=2
            ).astype(int)
            diff = prediction - prediction1
            prediction = prediction1

        if output.shape[-1] > 2:
            divis = (MAP == self.diviclass).astype(int) + diff
            MAP[divis == 1] = self.diviclass

        predictionlb = sem2inst(MAP)
        if fsize > 0:
            predictionlb = remove_small_objects(
                predictionlb, fsize, connectivity=1, in_place=True
            ).astype(int)
        region, MAP = inst2sem(predictionlb)

        return predictionlb, MAP, region, output, _argmax


class WTS_post(object):
    def __init__(self, cellclass=1, diviclass=2):
        self.cellclass = cellclass
        self.diviclass = diviclass

    @save_defaults
    @load_defaults
    def __call__(
        self,
        output,
        thresh_background=0.9,
        thresh_foreground=0.95,
        prob4="back",
        min_area=0,
    ):
        _argmax = np.argmax(output, axis=-1).astype(np.uint8)
        output = prob42prob3(output, prob4)

        if output.shape[-1] > 2:
            cellsprob = output[..., self.cellclass]
            backprop = output[..., 0]
            divisprop = output[..., self.diviclass]
        else:
            cellsprob = output
            backprop = 1 - output
            divisprop = np.zeros_like(cellsprob)

        foreground_seed = np.array(cellsprob > thresh_foreground).astype(int)
        background_seed = np.array(backprop > thresh_background).astype(int)
        markers = ndimage.label(foreground_seed)[0]

        distance = cellsprob - divisprop
        distance[distance < 0] = 0
        distance = (distance * 255).astype(int)

        predictionlb = watershed(
            -distance, markers, mask=(background_seed != 1)
        )
        if min_area > 0:
            predictionlb = remove_small_objects(
                predictionlb, min_area, connectivity=1, in_place=True
            ).astype(int)
        region, prediction = inst2sem(predictionlb)

        return predictionlb, prediction, region, output, _argmax
