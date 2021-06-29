import numpy as np
from PIL import Image


class LimbFrame:
    def __init__(self, arr: np.ndarray):
        self._raw_arr = arr
        self.arr = arr

    def as_pillow(self) -> Image:
        img = Image.fromarray(self.arr.astype(np.uint8))
        return img

    def as_array(self):
        return self.arr

    def postprocess_normed(self,
                           dither_strength: float,
                           arr_min: float = None,
                           arr_ptp: float = None, ):
        arr = self._raw_arr.ravel()
        if arr_min is None:
            arr_min = arr.min(0)
        if arr_ptp is None:
            arr_ptp = arr.ptp(0)
        arr = (arr - arr_min) / (arr_ptp + 1e-10)
        arr = arr + (np.random.random(arr.size) - 0.5) * (dither_strength / 256)
        arr[arr > 1] = 1
        arr[arr < 0] = 0
        arr = arr.reshape(*self._raw_arr.shape)
        arr = (arr * 255).astype(np.uint8)
        self.arr = arr

    def postprocess_binning(self, dither_strength: float):
        arr = self._raw_arr.ravel()
        arr = arr + (np.random.random(arr.size) - 0.5) * (dither_strength / 256)
        splits = np.array_split(np.sort(arr), 510)
        cutoffs = [x[-1] for x in splits][:-1]
        discrete = np.digitize(arr, cutoffs, right=True)
        arr = discrete.reshape(*self._raw_arr.shape)
        arr = np.abs(255 - arr % 510)
        arr = arr.astype(np.uint8)
        self.arr = arr
