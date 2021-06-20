from PIL import Image
import cv2
from . import __all_backends__
import random


pil_interpolations = {"bilinear": Image.BILINEAR, "bicubic": Image.BICUBIC, "lanczos": Image.LANCZOS}
cv2_interpolations = {"bilinear": cv2.INTER_LINEAR, "bicubic": cv2.INTER_CUBIC, "area": cv2.INTER_AREA, "lanczos": cv2.INTER_LANCZOS4}

__shared_interpolations__ = ["bilinear", "bicubic", "lanczos"]
__all_interpolations__ = list(pil_interpolations) + list(cv2_interpolations)



def get_interp(interpolation="bilinear", backend="pil"):
    assert interpolation.lower() in __shared_interpolations__
    assert backend.lower() in __all_backends__

    if backend == "cv2":
        return cv2_interpolations[interpolation]
    else:
        return pil_interpolations[interpolation]

def get_random_interp(backend="pil"):
    if backend == "pil":
        interp = pil_interpolations
    elif backend == "cv2":
        interp = cv2_interpolations
    return random.choice(list(interp.values()))

