import cv2 as cv
from PIL import Image
import numpy as np
import bbox_visualizer as bbv
from albumentations import PadIfNeeded


def make_color_wheel(bins=None):
    """Build a color wheel.

    Args:
        bins(list or tuple, optional): Specify the number of bins for each
            color range, corresponding to six ranges: red -> yellow,
            yellow -> green, green -> cyan, cyan -> blue, blue -> magenta,
            magenta -> red. [15, 6, 4, 11, 13, 6] is used for default
            (see Middlebury).

    Returns:
        ndarray: Color wheel of shape (total_bins, 3).
    """
    if bins is None:
        bins = [15, 6, 4, 11, 13, 6]
    assert len(bins) == 6

    RY, YG, GC, CB, BM, MR = tuple(bins)

    ry = [1, np.arange(RY) / RY, 0]
    yg = [1 - np.arange(YG) / YG, 1, 0]
    gc = [0, 1, np.arange(GC) / GC]
    cb = [0, 1 - np.arange(CB) / CB, 1]
    bm = [np.arange(BM) / BM, 0, 1]
    mr = [1, 0, 1 - np.arange(MR) / MR]

    num_bins = RY + YG + GC + CB + BM + MR

    color_wheel = np.zeros((3, num_bins), dtype=np.float32)

    col = 0
    for i, color in enumerate([ry, yg, gc, cb, bm, mr]):
        for j in range(3):
            color_wheel[j, col:col + bins[i]] = color[j]
        col += bins[i]

    return color_wheel.T


def imread(pathname):
    image = Image.open(pathname)
    image = cv.cvtColor(np.asarray(image, np.uint8), cv.COLOR_RGB2BGR)
    return image


def imwrite(pathname, image):
    image = Image.fromarray(cv.cvtColor(image, cv.COLOR_BGR2RGB))
    image.save(pathname)


def cv2pil(image):
    return Image.fromarray(cv.cvtColor(image, cv.COLOR_BGR2RGB))


def pil2cv(image):
    return cv.cvtColor(np.asarray(image, np.uint8), cv.COLOR_RGB2BGR)


def imshow(win_name: str,
           image,
           ratio,
           is_fixedsize=False,
           size=None):
    h, w, _ = image.shape

    if is_fixedsize:
        dst_w, dst_h = size
        ratio = min(dst_w / w, dst_h / h)
        w, h = int(ratio * w), int(ratio * h)

        img = cv.resize(image, (w, h))
        img = PadIfNeeded(dst_h, dst_w,
                          border_mode=cv.BORDER_CONSTANT,
                          value=(0, 0, 0),
                          always_apply=True)(image=img)['image']
    else:
        if ratio is not None:
            h = int(h * ratio)
            w = int(w * ratio)
        img = cv.resize(image, (w, h))

    cv.imshow(win_name, img)
    cv.waitKey()


def imshow_with_bbox(win_name: str,
                     image,
                     bboxes: np.ndarray,
                     classes,
                     is_show=True,
                     thickness=1,
                     is_opaque=False,
                     top=True):
    assert bboxes.shape[-1] == 5

    labels = bboxes[:, -1].tolist()
    labels = [classes[int(x)] for x in labels]
    image = bbv.draw_multiple_rectangles(image, bboxes[:, 0:4].tolist(), is_opaque=is_opaque, thickness=thickness)
    image = bbv.add_multiple_labels(image, labels, bboxes[:, 0:4].tolist(), top=top)

    if is_show:
        cv.imshow(win_name, image)
        cv.waitKey()

    return image
