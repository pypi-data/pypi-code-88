import logging
import numpy as np

from albumentations.core.transforms_interface import ImageOnlyTransform


class Normalize(ImageOnlyTransform):
    """Normalization is applied by the formula: `img = (img - mean) / std`
    Args:
        mean (float, list of float): mean values
        std  (float, list of float): std values
        max_pixel_value (float): maximum possible pixel value
    Targets:
        image
    Image types:
        uint8, float32
    """
    def __init__(self, mean=(0.485, 0.456, 0.406),
        std=(0.229, 0.224, 0.225), always_apply=False, p=1.0):
        super(Normalize, self).__init__(always_apply, p)
        self.mean = np.array(mean, dtype=np.float32)
        self.std = np.array(std, dtype=np.float32)
    
    def apply(self, image, **params):
        denominator = np.reciprocal(self.std, dtype=np.float32)
        
        img = np.array(image,dtype=np.float32)
        img -= self.mean
        img *= denominator
        
        return img

    def get_transform_init_args_names(self):
        return ("mean", "std")
        
