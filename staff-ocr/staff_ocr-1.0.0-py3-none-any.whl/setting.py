# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from staff_ocr import __version__

ANGLE_MODEL = 'angle_net.onnx'
CRNN_MODEL = 'crnn_lite_lstm.onnx'
DBNET_MODEL = 'dbnet.onnx'

CACHE_SERVER = f'http://139.224.213.4:3000/zhangji/staff_ocr_model/archive/v{__version__}.zip'

# dbnet 参数
DBNET_MAX_SIZE = 6000  # 长边最大长度

# crnn参数
CRNN_LITE = True
IS_RGB = True

# angle
ANGLE_DETECT = True
ANGLE_DETECT_NUM = 30
