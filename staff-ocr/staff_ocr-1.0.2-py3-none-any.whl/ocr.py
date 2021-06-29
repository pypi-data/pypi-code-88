import base64
import json
from io import BytesIO
from loguru import logger
import numpy as np
from PIL import Image
from .setting import *

from staff_ocr.model import OcrHandle
from functools import lru_cache

ocrhandle = OcrHandle()


@lru_cache()
def predict(image):
    if isinstance(image, str):
        return _predict_str(image)
    elif isinstance(image, bytes):
        return _predict_bytes(image)
    logger.warning('未知的参数类型，请注意检查')
    return []


def _predict_str(base64_str: str):
    img_b64 = base64_str
    if ',' in img_b64:
        img_b64 = img_b64.split(',')[1]
    raw_image = base64.b64decode(img_b64)
    img = Image.open(BytesIO(raw_image))
    return _predict_image(img)


def _predict_bytes(bs: bytes):
    img = Image.open(BytesIO(bs))
    return _predict_image(img)


def _predict_image(img):
    h, w, c = np.asarray(img).astype(np.uint8).shape
    if c == 4:
        scale_w = int(w * 2)
        scale_h = int(h * 2)
        bg = Image.new("RGB", (scale_w, scale_h), (255, 255, 255))
        bg.paste(img, ((int((scale_w - w) / 2)), int((scale_h - h) / 2)), img)
        img = bg
    try:
        if hasattr(img, '_getexif') and img._getexif() is not None:
            orientation = 274
            exif = dict(img._getexif().items())
            if orientation not in exif:
                exif[orientation] = 0
            if exif[orientation] == 3:
                img = img.rotate(180, expand=True)
            elif exif[orientation] == 6:
                img = img.rotate(270, expand=True)
            elif exif[orientation] == 8:
                img = img.rotate(90, expand=True)
    except Exception as ex:
        logger.exception(json.dumps({'msg': '产生了一点错误，请检查日志', 'err': str(ex)}))
        return []

    short_size = 128
    img_w, img_h = img.size
    if max(img_w, img_h) * (short_size * 1.0 / min(img_w, img_h)) > DBNET_MAX_SIZE:
        logger.error('图片尺寸过大')
        return []
    res = ocrhandle.text_predict(img, short_size)
    return [x[1] for x in res]
