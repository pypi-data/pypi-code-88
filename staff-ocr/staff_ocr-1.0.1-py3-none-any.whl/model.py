import copy
import os.path
import traceback

import numpy as np
from PIL import Image
from .setting import *
from .angnet import AngleNetHandle

from .crnn import CRNNHandle
from .dbnet.dbnet_infer import DBNET
from staff_ocr.util.common_util import sorted_boxes, get_rotate_crop_image
from .util import io_util


def rgba_to_rgb(rgba, background=(255, 255, 255)):
    row, col, ch = rgba.shape

    if ch == 3:
        return rgba

    assert ch == 4, 'RGBA image has 4 channels.'

    # 生成一个三维画布图片
    rgb = np.zeros((row, col, 3), dtype='float32')

    # 获取图片每个通道数据
    r, g, b, a = rgba[:, :, 0], rgba[:, :, 1], rgba[:, :, 2], rgba[:, :, 3]

    # 把 alpha 通道的值转换到 0-1 之间
    a = np.asarray(a, dtype='float32') / 255.0

    # 得到想要生成背景图片每个通道的值
    R, G, B = background

    # 将图片 a 绘制到另一幅图片 b 上，如果有 alpha 通道，那么最后覆盖的结果值将是 c = a * alpha + b * (1 - alpha)
    rgb[:, :, 0] = r * a + (1.0 - a) * R
    rgb[:, :, 1] = g * a + (1.0 - a) * G
    rgb[:, :, 2] = b * a + (1.0 - a) * B

    # 把最终数据类型转换成 uint8
    return np.asarray(rgb, dtype='uint8')


class OcrHandle(object):
    def __init__(self):
        path = io_util.get_resource(CACHE_SERVER)
        self.text_handle = DBNET(os.path.join(path, DBNET_MODEL))
        self.crnn_handle = CRNNHandle(os.path.join(path, CRNN_MODEL))
        if ANGLE_DETECT:
            self.angle_handle = AngleNetHandle(os.path.join(path, ANGLE_MODEL))

    def crnn_rec_with_box(self, im, boxes_list, score_list):
        """
        crnn模型，ocr识别
        @@model,
        @@converter,
        @@im:Array
        @@text_recs:text box
        @@ifIm:是否输出box对应的img

        """
        results = []
        boxes_list = sorted_boxes(np.array(boxes_list))

        line_imgs = []
        for index, (box, score) in enumerate(zip(boxes_list[:ANGLE_DETECT_NUM], score_list[:ANGLE_DETECT_NUM])):
            tmp_box = copy.deepcopy(box)
            part_img_array = get_rotate_crop_image(im, tmp_box.astype(np.float32))
            part_img = Image.fromarray(part_img_array).convert("RGB")
            line_imgs.append(part_img)
        angle_res = False
        if ANGLE_DETECT:
            angle_res = self.angle_handle.predict_rbgs(line_imgs)

        count = 1
        for index, (box, score) in enumerate(zip(boxes_list, score_list)):

            tmp_box = copy.deepcopy(box)
            part_img_array = get_rotate_crop_image(im, tmp_box.astype(np.float32))

            part_img = Image.fromarray(part_img_array).convert("RGB")

            if ANGLE_DETECT and angle_res:
                part_img = part_img.rotate(180)

            if not IS_RGB:
                part_img = part_img.convert('L')

            try:
                if IS_RGB:
                    sim_pred = self.crnn_handle.predict_rbg(part_img)
                else:
                    sim_pred = self.crnn_handle.predict(part_img)
            except Exception as e:
                print(traceback.format_exc())
                continue

            if sim_pred.strip() != '':
                results.append([tmp_box, sim_pred, score])
                count += 1

        return results

    def text_predict(self, img, short_size):
        rgb_img = np.asarray(img).astype(np.uint8)
        boxes_list, score_list = self.text_handle.process(rgb_img, short_size=short_size)
        result = self.crnn_rec_with_box(np.array(img), boxes_list, score_list)
        return result
