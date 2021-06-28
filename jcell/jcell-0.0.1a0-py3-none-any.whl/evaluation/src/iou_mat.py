import numpy as np


def overlap_bbox(bbox1, bbox2):
    min1, max1 = np.array(bbox1[:2]), np.array(bbox1[2:])
    min2, max2 = np.array(bbox2[:2]), np.array(bbox2[2:])
    if any(min2 > max1):
        return False
    if any(max2 < min1):
        return False
    return True


def iou_mat(result, target):
    ur = np.unique(result)
    ut = np.unique(target)

    lur = len(ur)
    lut = len(ut)

    iou = np.zeros((lur, lut))

    coord_ur = []
    for i in range(1, lur):
        IR = (result == ur[i]).astype(np.uint8)
        x, y = np.where(IR != 0)
        coord_ur += [(min(x), min(y), max(x), max(y))]

    coord_ut = []
    for i in range(1, lut):
        IT = (target == ut[i]).astype(np.uint8)
        x, y = np.where(IT != 0)
        coord_ut += [(min(x), min(y), max(x), max(y))]

    for i in range(1, lur):
        for j in range(1, lut):
            if overlap_bbox(coord_ur[i - 1], coord_ut[j - 1]):
                IR = (result == ur[i]).astype(np.uint8)
                IT = (target == ut[j]).astype(np.uint8)
                intersect = ((IR + IT) == 2).astype(np.double)
                union = ((IR + IT) >= 1).astype(np.double)
                iou[i, j] = intersect.sum() / union.sum()

    iou = iou[1:, 1:]
    return iou
