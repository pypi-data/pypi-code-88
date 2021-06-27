from PIL import Image
import cv2 as cv
import numpy as np
from pathlib import Path


def visualize_aug(transforms, labels: dict or None, img_paths: list, duplicate_nums=None, backend='albumentations',
                  show_size=(960, 540)):
    for img_path in img_paths:
        img_name = Path(img_path).name

        if backend == 'albumentations':
            img = np.asarray(Image.open(img_path))

            if labels is not None:
                pass

            assert duplicate_nums != 0
            duplicate_nums = 1 if duplicate_nums is None else duplicate_nums

            _img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
            _img = cv.resize(_img, show_size)
            cv.imshow(f'{img_name}-origin', _img)
            cv.waitKey()
            for i in range(duplicate_nums):
                transformed = transforms(image=img)
                _img = transformed['image']
                _img = cv.cvtColor(_img, cv.COLOR_RGB2BGR)

                _img = cv.resize(_img, show_size)
                cv.imshow(f'{img_name}-NO.{i + 1}', _img)
                cv.waitKey()
            cv.destroyAllWindows()
