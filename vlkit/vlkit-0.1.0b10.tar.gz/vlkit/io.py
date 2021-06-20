import cv2
import numpy as np
from PIL import Image
from os.path import isfile
from .image import isimg
import pickle

def imread(path, backend="pil", grayscale=False):
    assert isfile(path) and isimg(path)
    if backend == "pil":
        im = Image.open(path)
        if grayscale:
            im = im.convert("L")
        return np.array(im)
    elif backend == "cv2":
        return cv2.imread(path, int(not grayscale))
    else:
        raise ValueError("Invalid backend %s. (Valid options are ['pil', 'cv2'])" % backend)

def imwrite(im, path, backend="pil"):
    assert isinstance(im, np.ndarray)
    assert isimg(path)
    if backend == "pil":
        Image.fromarray(im).save(path)
    elif backend == "cv2":
        cv2.imwrite(path, im)
    else:
        raise ValueError("Invalid backend %s. (Valid options are ['pil', 'cv2'])" % backend)

def pickle_save(object, path):
    f = open(path, "wb")
    pickle.dump(object, f)
    f.close()
    return path

def pickle_load(path):
    f = open(path, "rb")
    return pickle.load(f)
