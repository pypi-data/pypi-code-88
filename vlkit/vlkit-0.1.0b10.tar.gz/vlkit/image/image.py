import numpy as np
from PIL import Image
import os, sys
from os.path import join, split, splitext, isdir, isfile, abspath
import skimage

__img_ext__ = ['jpg', 'jpeg', 'png', 'bmp']

def isimg(path):
    path = path.lower()
    return any(path.endswith(ext) for ext in __img_ext__)

def traverse_folder(path):
    """
    traverse a given folder to find image files
    input:  path to traverse for images
    return: a list containing all image paths
    """
    images = []
    for p in os.listdir(path):
        p1 = abspath(join(path, p))
        if isdir(p1):
            images += traverse_folder(p1)
        elif isimg(p1):
            images.append(p1)
        else:
            continue

    return images

def gray2rgb(x):
    if x.ndim == 3 and x.shape[2] ==3:
        return x
    elif x.ndim == 2:
        H, W = x.shape
        x = x.reshape((H, W, 1))
        x = np.repeat(x, 3, 2)
        return x
    else:
        raise ValueError("Unsupported shape: %s" % str(x.shape))

def norm01(x):
    """
    Normalize input image into range [0, 1]
    """
    assert isinstance(x, np.ndarray)
    x = x.astype(np.float32)

    if x.max() == x.min():
        return x - x.min()

    x -= x.min()
    x /= x.max()

    return x

def norm255(x):
    """
    Normalize input image into range [0, 1]
    """
    assert isinstance(x, np.ndarray)
    x = x.astype(np.float32)

    if x.max() == x.min():
        x[...] = 0
        return x
    x = norm01(x)

    return (x * 255).astype(np.uint8)

def hwc2nchw(image):
    """
    Convert an image (or a list of images of the same size) to
    [N C H W] style batch data
    
    Input:
        --- image: numpy.ndarray or list of numpy.ndarray
    """
    assert isinstance(image, np.ndarray) or isinstance(image, list)
    H, W, C, N = 0, 0, 0, 0
    if isinstance(image, np.ndarray):
        assert image.ndim == 3
        H, W, C = image.shape
        N = 1
    else:
        for i, im in enumerate(image):
            assert im.ndim == 3
            assert isinstance(im, np.ndarray)
            if i == 0:
                pre_shape = im.shape
            else:
                assert im.shape == pre_shape
        H, W, C = image[0].shape
        N = len(image)
    data = np.zeros((N, C, H, W), dtype=np.float32)

    if isinstance(image, np.ndarray):
        data[0, :, :, :] = image.transpose((2, 0, 1))
    else:
        for i, im in enumerate(image):
            data[i, :, :, :] = im.transpose((2, 0, 1))

    return data

def overlay(img, mask, color=[255, 0, 0], alpha=0.5):
    img = skimage.img_as_float(img)
    mask = mask.astype(bool)
    color = np.array(color).reshape((1, 1, 3))
    color_mask = np.zeros_like(img)
    color_mask[mask, :] = color

    img_hsv = skimage.color.rgb2hsv(img)
    color_mask_hsv = skimage.color.rgb2hsv(color_mask)

    img_hsv[mask, 0] = color_mask_hsv[mask, 0]
    img_hsv[mask, 1] = color_mask_hsv[mask, 1] * alpha

    img = skimage.color.hsv2rgb(img_hsv)
    img /= img.max()
    img *= 255
    img = img.astype(np.uint8)

    return img


if __name__ == "__main__":
    import matplotlib
    import matplotlib.pyplot as plt
    img = skimage.data.astronaut()
    H, W, _ = img.shape
    mask = np.zeros((H, W), dtype=bool)
    mask[100:150, :] = 1

    img = overlay(img, mask)
    mask = np.zeros((H, W), dtype=bool)
    mask[200:250, :] = 1
    img = overlay(img, mask, color=[0, 255, 0])

    plt.imshow(img)
    plt.show()
