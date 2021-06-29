# -*- coding: UTF-8 -*-
"""
导入依赖包
opencv读取图片
Image读取图片
图片保存
图片展示
"""

import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def read_image_opencv(path):
    """
    利用opencv读取图片，打开图片是BGR格式，支持中英文路径

    :param path: 图片路径
    :return: 读取的图片
    """
    for c in path:
        if ord(c) > 127:
            image = cv2.imdecode(np.fromfile(path, dtype=np.uint8), 1)
            return image
    image = cv2.imread(path)
    return image


def read_image_image(path):
    """
    利用pil中得Image读取图片，打开图片是RGB格式

    :param path:
    :return:
    """
    image = Image.open(path)
    return image


def image_save(image, path, num='1', mode='jpg'):
    """
    保存打开的图片到指定路径下

    :param image: 开的图片
    :param path: 保存的路径
    :param num:  图片序号
    :param mode: 图片格式，支持jpeg,tif,jpg,BMP,GIF
    :return: 0
    """
    cv2.imencode('.jpg', np.float32(image))[1].tofile(path + num + '.' + mode)
    return 0


def display_image(image, threshold1=700, threshold2=700):
    """
    显示opencv、Image打开的图片

    :param image:
    :return:
    """
    if isinstance(image, np.ndarray):
        threshold1, threshold2 = image.shape
        cv2.namedWindow('image', 0)
        cv2.resizeWindow('image', threshold2, threshold1)
        cv2.imshow('image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        plt.imshow(image)
        plt.title("image")
        plt.show()
