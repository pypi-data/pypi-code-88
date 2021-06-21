from enum import Enum
import wizzi_utils.misc as mt
from wizzi_utils.open_cv.labels_bank import PASCAL_VOC_2012_21_LABELS
from wizzi_utils.open_cv.labels_bank import PASCAL_VOC_2012_20_LABELS
from wizzi_utils.open_cv.labels_bank import COCO_YOLO_80_LABELS
from wizzi_utils.open_cv.labels_bank import ILSVRC2016_201_LABELS
from wizzi_utils.open_cv.labels_bank import COCO_183_LABELS
from wizzi_utils.open_cv.labels_bank import COCO_182_LABELS


# from wizzi_utils_test.downloaded_models.labels_bank import IMAGENET


class Jobs(Enum):
    OBJECT_DETECTION = 'object_detection'
    SEGMENTATION = 'segmentation'
    OPEN_POSE = 'openpose'
    CLASSIFICATION = 'classification'


class DnnFamily(Enum):
    Caffe = 'Caffe'
    Darknet = 'Darknet'
    TF = 'TensorFlow'


class DownloadStyle(Enum):
    Direct = 'Direct'
    Tar = 'tar'
    Zip = 'zip'


test_fps_od_image_url = 'https://raw.githubusercontent.com/pjreddie/darknet/master/data/dog.jpg'
test_fps_od_iters = 10
test_fps_computer_info = 'AMD64, Intel64 Family 6 Model 158 Stepping 9, GenuineIntel, ' + \
                         'Physical cores 4, Total cores 8, Frequency 3601.00Mhz, CPU Usage 13.6%)'

fps_info = '({} iterations, the above cfg, on image {} on {})'.format(test_fps_od_iters, test_fps_od_image_url,
                                                                      test_fps_computer_info)
# see wu.cvt.test.fps_models_test()

# models from: https://github.com/opencv/opencv_extra/tree/master/testdata/dnn
MODELS_DNN_OBJECT_DETECTION_META_DATA = {
    # see wu.cvt.get_all_object_detection_models_info(ack=True)
    'yolov4': {  # checked
        'job': Jobs.OBJECT_DETECTION.value,
        'family': DnnFamily.Darknet.value,
        # 'in_dims': (320, 320),
        # 'in_dims': (416, 416),
        # 'in_dims': (512, 512),
        'in_dims': (608, 608),
        # 'scalefactor': 1 / 255,
        'scalefactor': 1 / 127.5,
        'mean': (0, 0, 0),
        'swapRB': True,
        'crop': False,
        'default_threshold': 0.2,
        'default_nms_threshold': 0.4,
        'labels_dict': COCO_YOLO_80_LABELS,
        'URL': {
            'cfg': 'https://raw.githubusercontent.com/opencv/opencv_extra/master/testdata/dnn/yolov4.cfg',
            'weights': 'https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.weights',
            'cfg_download_style': DownloadStyle.Direct.value,
            'weights_download_style': DownloadStyle.Direct.value,
        },
        'info': {
            'web_name': 'yolov4.weights',
            'size': 'weights({}), cfg({})'.format(mt.add_color('245.78 MB', ops='c'),
                                                  mt.add_color('11.94 KB', ops='c')),
            'fps': '{} {}'.format(mt.add_color('1.44 FPS'), fps_info),
            'info': 'TODO',
        },
    },
    'yolov3': {  # checked
        'job': Jobs.OBJECT_DETECTION.value,
        'family': DnnFamily.Darknet.value,
        'in_dims': (416, 416),
        'scalefactor': 1 / 255,
        'mean': (0, 0, 0),
        'swapRB': True,
        'crop': False,
        'default_threshold': 0.2,
        'default_nms_threshold': 0.4,
        'labels_dict': COCO_YOLO_80_LABELS,
        'URL': {
            'cfg': 'https://raw.githubusercontent.com/opencv/opencv_extra/master/testdata/dnn/yolov3.cfg',
            'weights': 'https://pjreddie.com/media/files/yolov3.weights',
            'cfg_download_style': DownloadStyle.Direct.value,
            'weights_download_style': DownloadStyle.Direct.value,
        },
        'info': {
            'web_name': 'yolov3.weights',
            'size': 'weights({}), cfg({})'.format(mt.add_color('236.52 MB', ops='c'), mt.add_color('8.22 KB', ops='c')),
            'fps': '{} {}'.format(mt.add_color('3.24 FPS'), fps_info),
            'info': 'TODO',
        },
    },
    'yolov3-ssp': {  # checked
        'job': Jobs.OBJECT_DETECTION.value,
        'family': DnnFamily.Darknet.value,
        'in_dims': (608, 608),
        'scalefactor': 1 / 127.5,
        'mean': (0, 0, 0),
        'swapRB': True,
        'crop': False,
        'default_threshold': 0.2,
        'default_nms_threshold': 0.4,
        'labels_dict': COCO_YOLO_80_LABELS,
        'URL': {
            'cfg': 'https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3-spp.cfg',
            'weights': 'https://github.com/ultralytics/yolov3/releases/download/v8/yolov3-spp.weights',
            'cfg_download_style': DownloadStyle.Direct.value,
            'weights_download_style': DownloadStyle.Direct.value,
        },
        'info': {
            'web_name': 'yolov3-spp.weights',
            'size': 'weights({}), cfg({})'.format(mt.add_color('240.53 MB', ops='c'), mt.add_color('8.4 KB', ops='c')),
            'fps': '{} {}'.format(mt.add_color('1.67 FPS'), fps_info),
            'info': 'TODO',
        },
    },
    'yolo-voc': {  # checked
        'job': Jobs.OBJECT_DETECTION.value,
        'family': DnnFamily.Darknet.value,
        'in_dims': (416, 416),
        'scalefactor': 1 / 255,
        'mean': (127.5, 127.5, 127.5),
        'swapRB': True,
        'crop': False,
        'default_threshold': 0.2,
        'default_nms_threshold': 0.4,
        'labels_dict': PASCAL_VOC_2012_20_LABELS,
        'URL': {
            'cfg': 'https://raw.githubusercontent.com/opencv/opencv_extra/master/testdata/dnn/yolo-voc.cfg',
            'weights': 'https://pjreddie.com/media/files/yolo-voc.weights',
            'cfg_download_style': DownloadStyle.Direct.value,
            'weights_download_style': DownloadStyle.Direct.value,
        },
        'info': {
            'web_name': 'yolo-voc.weights',
            'size': 'weights({}), cfg({})'.format(mt.add_color('193.31 MB', ops='c'), mt.add_color('2.66 KB', ops='c')),
            'fps': '{} {}'.format(mt.add_color('7.48 FPS'), fps_info),
            'info': 'TODO',
        },
    },
    'MobileNetSSD_deploy': {  # checked
        'job': Jobs.OBJECT_DETECTION.value,
        'family': DnnFamily.Caffe.value,
        'in_dims': (800, 600),
        'scalefactor': 1 / 127.5,
        'mean': (127.5, 127.5, 127.5),
        'swapRB': False,
        'crop': False,
        'default_threshold': 0.2,
        'default_nms_threshold': 0.4,
        'labels_dict': PASCAL_VOC_2012_21_LABELS,
        'URL': {
            'prototxt': 'https://raw.githubusercontent.com/chuanqi305/MobileNet-SSD/' +
                        'daef68a6c2f5fbb8c88404266aa28180646d17e0/MobileNetSSD_deploy.prototxt',
            'caffemodel': 'https://drive.google.com/uc?export=download&id=0B3gersZ2cHIxRm5PMWRoTkdHdHc',
            'prototxt_download_style': DownloadStyle.Direct.value,
            'caffemodel_download_style': DownloadStyle.Direct.value,
        },
        'info': {
            'web_name': 'MobileNetSSD_deploy',
            'size': 'caffemodel({}), prototxt({})'.format(mt.add_color('22.08 MB', ops='c'),
                                                          mt.add_color('28.67 KB', ops='c')),
            'fps': '{} {}'.format(mt.add_color('13.28 FPS'), fps_info),
            'info': 'https://www.programmersought.com/article/569030384/',
        },
    },
    'yolov4-tiny': {  # checked
        'job': Jobs.OBJECT_DETECTION.value,
        'family': DnnFamily.Darknet.value,
        'in_dims': (608, 608),
        'scalefactor': 1 / 127.5,
        'mean': (0, 0, 0),
        'swapRB': True,
        'crop': False,
        'default_threshold': 0.2,
        'default_nms_threshold': 0.4,
        'labels_dict': COCO_YOLO_80_LABELS,
        'URL': {
            'cfg': 'https://raw.githubusercontent.com/opencv/opencv_extra/master/testdata/dnn/yolov4-tiny.cfg',
            'weights': 'https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-tiny.weights',
            'cfg_download_style': DownloadStyle.Direct.value,
            'weights_download_style': DownloadStyle.Direct.value,
        },
        'info': {
            'web_name': 'yolov4-tiny.weights',
            'size': 'weights({}), cfg({})'.format(mt.add_color('23.13 MB', ops='c'), mt.add_color('2.96 KB', ops='c')),
            'fps': '{} {}'.format(mt.add_color('11.33 FPS'), fps_info),
            'info': 'TODO',
        },
    },
    'yolov3_tiny': {  # checked
        'job': Jobs.OBJECT_DETECTION.value,
        'family': DnnFamily.Darknet.value,
        'in_dims': (512, 512),
        'scalefactor': 1 / 127.5,
        'mean': (0, 0, 0),
        'swapRB': True,
        'crop': False,
        'default_threshold': 0.2,
        'default_nms_threshold': 0.4,
        'labels_dict': COCO_YOLO_80_LABELS,
        'URL': {
            'cfg': 'https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3-tiny.cfg',
            'weights': 'https://github.com/ultralytics/yolov3/releases/download/v8/yolov3-tiny.weights',
            'cfg_download_style': DownloadStyle.Direct.value,
            'weights_download_style': DownloadStyle.Direct.value,
        },
        'info': {
            'web_name': 'yolov3-tiny.weights',
            'size': 'weights({}), cfg({})'.format(mt.add_color('33.79 MB', ops='c'), mt.add_color('1.87 KB', ops='c')),
            'fps': '{} {}'.format(mt.add_color('18.56 FPS'), fps_info),
            'info': 'TODO',
        },
    },
    'yolov2-tiny-voc': {  # checked
        'job': Jobs.OBJECT_DETECTION.value,
        'family': DnnFamily.Darknet.value,
        'in_dims': (416, 416),
        'scalefactor': 1 / 127.5,
        'mean': (0, 0, 0),
        'swapRB': True,
        'crop': False,
        'default_threshold': 0.2,
        'default_nms_threshold': 0.4,
        'labels_dict': PASCAL_VOC_2012_20_LABELS,
        'URL': {
            'cfg': 'https://raw.githubusercontent.com/opencv/opencv_extra/master/testdata/dnn/tiny-yolo-voc.cfg',
            'weights': 'https://pjreddie.com/media/files/yolov2-tiny-voc.weights',
            'cfg_download_style': DownloadStyle.Direct.value,
            'weights_download_style': DownloadStyle.Direct.value,
        },
        'info': {
            'web_name': 'yolov2-tiny-voc.weights',
            'size': 'weights({}), cfg({})'.format(mt.add_color('60.53 MB', ops='c'), mt.add_color('1.38 KB', ops='c')),
            'fps': '{} {}'.format(mt.add_color('24.61 FPS'), fps_info),
            'info': 'TODO',
        },
    },
    'VGG_ILSVRC2016_SSD_300x300_deploy': {  # checked
        'job': Jobs.OBJECT_DETECTION.value,
        'family': DnnFamily.Caffe.value,
        'in_dims': (300, 300),
        'scalefactor': 1,
        'mean': (127, 127, 127),
        'swapRB': False,
        'crop': False,
        'default_threshold': 0.2,
        'default_nms_threshold': 0.4,
        'labels_dict': ILSVRC2016_201_LABELS,
        'URL': {
            'prototxt': 'https://raw.githubusercontent.com/opencv/opencv_extra/master/testdata/dnn/ssd_vgg16.prototxt',
            'caffemodel': 'https://www.dropbox.com/s/8apyk3uzk2vl522/' +
                          'VGG_ILSVRC2016_SSD_300x300_iter_440000.caffemodel?dl=1',
            'prototxt_download_style': DownloadStyle.Direct.value,
            'caffemodel_download_style': DownloadStyle.Direct.value,
        },
        'info': {
            'web_name': 'VGG_ILSVRC2016_SSD_300x300_iter_440000.caffemodel',
            'size': 'caffemodel({}), prototxt({})'.format(mt.add_color('192.06 MB', ops='c'),
                                                          mt.add_color('23.93 KB', ops='c')),
            'fps': '{} {}'.format(mt.add_color('2.58'), fps_info),
            'info': 'TODO',
        },
    },
    'VGG_ILSVRC_16_layers': {  # checked
        'job': Jobs.OBJECT_DETECTION.value,
        'family': DnnFamily.Caffe.value,
        'in_dims': (800, 600),
        'scalefactor': 1,
        'mean': (102.9801, 115.9465, 122.7717),
        'swapRB': False,
        'crop': False,
        'default_threshold': 0.2,
        'default_nms_threshold': 0.4,
        'labels_dict': PASCAL_VOC_2012_21_LABELS,
        'need_normalize': 'normalize output needed',
        'URL': {
            'prototxt': 'https://raw.githubusercontent.com/opencv/opencv_extra/master/testdata/dnn/' +
                        'faster_rcnn_vgg16.prototxt',
            'caffemodel': 'https://dl.dropboxusercontent.com/s/o6ii098bu51d139/faster_rcnn_models.tgz?dl=0',
            'prototxt_download_style': DownloadStyle.Direct.value,
            'caffemodel_download_style': DownloadStyle.Tar.value,
            'caffemodel_name': 'VGG16_faster_rcnn_final.caffemodel',
        },
        'info': {
            'web_name': 'VGG16_faster_rcnn_final.caffemodel',
            'size': 'caffemodel({}), prototxt({})'.format(mt.add_color('522.92 MB', ops='c'),
                                                          mt.add_color('8.45 KB', ops='c')),
            'fps': '{} {}'.format(mt.add_color('0.21 FPS'), fps_info),
            'info': 'TODO',
        },
    },
    'rfcn_pascal_voc_resnet50': {  # checked
        'job': Jobs.OBJECT_DETECTION.value,
        'family': DnnFamily.Caffe.value,
        'in_dims': (800, 600),
        'scalefactor': 1,
        'mean': (102.9801, 115.9465, 122.7717),
        'swapRB': False,
        'crop': False,
        'default_threshold': 0.2,
        'default_nms_threshold': 0.4,
        'labels_dict': PASCAL_VOC_2012_21_LABELS,
        'need_normalize': 'normalize output needed',
        'URL': {
            'prototxt': 'https://raw.githubusercontent.com/opencv/opencv_extra/master/testdata/dnn/' +
                        'rfcn_pascal_voc_resnet50.prototxt',
            'caffemodel': 'https://onedrive.live.com/download?' +
                          'cid=10B28C0E28BF7B83&resid=10B28C0E28BF7B83%215317&authkey=%21AIeljruhoLuail8',
            'prototxt_download_style': DownloadStyle.Direct.value,
            'caffemodel_download_style': DownloadStyle.Tar.value,
            'caffemodel_name': 'resnet50_rfcn_final.caffemodel',
        },
        'info': {
            'web_name': 'resnet50_rfcn_final.caffemodel',
            'size': 'caffemodel({}), prototxt({})'.format(mt.add_color('121.58 MB', ops='c'),
                                                          mt.add_color('62.8 KB', ops='c')),
            'fps': '{} {}'.format(mt.add_color('1.28 FPS'), fps_info),
            'info': 'TODO',
        },
    },
    'faster_rcnn_zf': {  # checked
        'job': Jobs.OBJECT_DETECTION.value,
        'family': DnnFamily.Caffe.value,
        'in_dims': (800, 600),
        'scalefactor': 1,
        'mean': (102.9801, 115.9465, 122.7717),
        'swapRB': False,
        'crop': False,
        'default_threshold': 0.4,
        'default_nms_threshold': 0.0,
        'labels_dict': PASCAL_VOC_2012_21_LABELS,
        'need_normalize': 'normalize output needed',
        'URL': {
            'prototxt': 'https://raw.githubusercontent.com/opencv/opencv_extra/master/testdata/dnn/' +
                        'faster_rcnn_zf.prototxt',
            'caffemodel': 'https://dl.dropboxusercontent.com/s/o6ii098bu51d139/' +
                          'faster_rcnn_models.tgz?dl=0',
            'prototxt_download_style': DownloadStyle.Direct.value,
            'caffemodel_download_style': DownloadStyle.Tar.value,
            'caffemodel_name': 'ZF_faster_rcnn_final.caffemodel',
        },
        'info': {
            'web_name': 'ZF_faster_rcnn_final',
            'size': 'caffemodel({}), prototxt({})'.format(mt.add_color('226.19 MB', ops='c'),
                                                          mt.add_color('7.1 KB', ops='c')),
            'fps': '{} {}'.format(mt.add_color('0.84 FPS'), fps_info),
            'info': 'TODO',
        },
    },
    'ssd_inception_v2_coco_2017_11_17': {  # checked
        'job': Jobs.OBJECT_DETECTION.value,
        'family': DnnFamily.TF.value,
        'in_dims': (800, 600),
        'scalefactor': 1,
        'mean': (0, 0, 0),
        'swapRB': True,
        'crop': False,
        'default_threshold': 0.2,
        'default_nms_threshold': 0.4,
        'labels_dict': COCO_183_LABELS,
        'URL': {
            'pbtxt': 'https://raw.githubusercontent.com/opencv/opencv_extra/master/testdata/dnn/' +
                     'ssd_inception_v2_coco_2017_11_17.pbtxt',
            'pb': 'http://download.tensorflow.org/models/object_detection/ssd_inception_v2_coco_2017_11_17.tar.gz',
            'pbtxt_download_style': DownloadStyle.Direct.value,
            'pb_download_style': DownloadStyle.Tar.value,
            'pb_name': 'frozen_inference_graph.pb',
        },
        'info': {
            'web_name': 'ssd_inception_v2_coco_2017_11_17',
            'size': 'pb({}), pbtxt({})'.format(mt.add_color('97.26 MB', ops='c'), mt.add_color('114.77 KB', ops='c')),
            'fps': '{} {}'.format(mt.add_color('3.78 FPS'), fps_info),
            'info': 'TODO',
        },
    },
    'ssd_mobilenet_v1_coco': {  # checked
        'job': Jobs.OBJECT_DETECTION.value,
        'family': DnnFamily.TF.value,
        'in_dims': (416, 416),
        'scalefactor': 1 / 127.5,
        'mean': (0, 0, 0),
        'swapRB': True,
        'crop': False,
        'default_threshold': 0.4,
        'default_nms_threshold': 0.4,
        'labels_dict': COCO_183_LABELS,
        'URL': {
            'pbtxt': 'https://raw.githubusercontent.com/opencv/opencv_extra/master/testdata/dnn/' +
                     'ssd_mobilenet_v1_coco.pbtxt',
            'pb': 'http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v1_coco_11_06_2017.tar.gz',
            'pbtxt_download_style': DownloadStyle.Direct.value,
            'pb_download_style': DownloadStyle.Tar.value,
            'pb_name': 'frozen_inference_graph.pb',
        },
        'info': {
            'web_name': 'ssd_mobilenet_v1_coco_11_06_2017',
            'size': 'pb({}), pbtxt({})'.format(mt.add_color('27.76 MB', ops='c'), mt.add_color('62.08 KB', ops='c')),
            'fps': '{} {}'.format(mt.add_color('27.13 FPS'), fps_info),
            'info': 'TODO',
        },
    },
    'faster_rcnn_inception_v2_coco_2018_01_28': {  # checked
        'job': Jobs.OBJECT_DETECTION.value,
        'family': DnnFamily.TF.value,
        'in_dims': (800, 600),
        'scalefactor': 1,
        'mean': (0, 0, 0),
        'swapRB': True,
        'crop': False,
        'default_threshold': 0.4,
        'default_nms_threshold': 0.4,
        'labels_dict': COCO_182_LABELS,
        'URL': {
            'pbtxt': 'https://raw.githubusercontent.com/opencv/opencv_extra/master/testdata/dnn/' +
                     'faster_rcnn_inception_v2_coco_2018_01_28.pbtxt',
            'pb': 'http://download.tensorflow.org/models/object_detection/' +
                  'faster_rcnn_inception_v2_coco_2018_01_28.tar.gz',
            'pbtxt_download_style': DownloadStyle.Direct.value,
            'pb_download_style': DownloadStyle.Tar.value,
            'pb_name': 'frozen_inference_graph.pb',
        },
        'info': {
            'web_name': 'faster_rcnn_inception_v2_coco_2018_01_28',
            'size': 'pb({}), pbtxt({})'.format(mt.add_color('54.51 MB', ops='c'), mt.add_color('112.92 KB', ops='c')),
            'fps': '{} {}'.format(mt.add_color('2.51 FPS'), fps_info),
            'info': 'TODO',
        },
    },
    'faster_rcnn_resnet50_coco_2018_01_28': {  # checked
        'job': Jobs.OBJECT_DETECTION.value,
        'family': DnnFamily.TF.value,
        'in_dims': (800, 600),
        'scalefactor': 1,
        'mean': (0, 0, 0),
        'swapRB': True,
        'crop': False,
        'default_threshold': 0.2,
        'default_nms_threshold': 0.4,
        'labels_dict': COCO_182_LABELS,
        # 'need_normalize': '??? normalize output needed',
        'URL': {
            'pbtxt': 'https://raw.githubusercontent.com/opencv/opencv_extra/master/testdata/dnn/' +
                     'faster_rcnn_resnet50_coco_2018_01_28.pbtxt',
            'pb': 'http://download.tensorflow.org/models/object_detection/faster_rcnn_resnet50_coco_2018_01_28.tar.gz',
            'pbtxt_download_style': DownloadStyle.Direct.value,
            'pb_download_style': DownloadStyle.Tar.value,
            'pb_name': 'frozen_inference_graph.pb',
        },
        'info': {
            'web_name': 'faster_rcnn_resnet50_coco_2018_01_28',
            'size': 'pb({}), pbtxt({})'.format(mt.add_color('114.97 MB', ops='c'), mt.add_color('88.76 KB', ops='c')),
            'fps': '{} {}'.format(mt.add_color('0.84 FPS'), fps_info),
            'info': 'TODO',
        },
    },
    'ssd_mobilenet_v1_coco_2017_11_17': {  # checked
        'job': Jobs.OBJECT_DETECTION.value,
        'family': DnnFamily.TF.value,
        'in_dims': (300, 300),
        'scalefactor': 1,
        'mean': (0, 0, 0),
        'swapRB': True,
        'crop': False,
        'default_threshold': 0.2,
        'default_nms_threshold': 0.4,
        'labels_dict': COCO_183_LABELS,
        'URL': {
            'pbtxt': 'https://raw.githubusercontent.com/opencv/opencv_extra/master/testdata/dnn/' +
                     'ssd_mobilenet_v1_coco_2017_11_17.pbtxt',
            'pb': 'http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v1_coco_2017_11_17.tar.gz',
            'pbtxt_download_style': DownloadStyle.Direct.value,
            'pb_download_style': DownloadStyle.Tar.value,
            'pb_name': 'frozen_inference_graph.pb',
        },
        'info': {
            'web_name': 'ssd_mobilenet_v1_coco_2017_11_17',
            'size': 'pb({}), pbtxt({})'.format(mt.add_color('27.76 MB', ops='c'), mt.add_color('62.08 KB', ops='c')),
            'fps': '{} {}'.format(mt.add_color('46.28 FPS'), fps_info),
            'info': 'TODO',
        },
    },
    'ssd_mobilenet_v1_ppn_coco': {  # checked
        'job': Jobs.OBJECT_DETECTION.value,
        'family': DnnFamily.TF.value,
        'in_dims': (300, 300),
        'scalefactor': 1,
        'mean': (127.5, 127.5, 127.5),
        'swapRB': False,
        'crop': False,
        'default_threshold': 0.4,
        'default_nms_threshold': 0.4,
        'labels_dict': COCO_183_LABELS,
        'URL': {
            'pbtxt': 'https://raw.githubusercontent.com/opencv/opencv_extra/master/testdata/dnn/' +
                     'ssd_mobilenet_v1_ppn_coco.pbtxt',
            'pb': 'http://download.tensorflow.org/models/object_detection/' +
                  'ssd_mobilenet_v1_ppn_shared_box_predictor_300x300_coco14_sync_2018_07_03.tar.gz',
            'pbtxt_download_style': DownloadStyle.Direct.value,
            'pb_download_style': DownloadStyle.Tar.value,
            'pb_name': 'frozen_inference_graph.pb',
        },
        'info': {
            'web_name': 'ssd_mobilenet_v1_ppn_shared_box_predictor_300x300_coco14_sync_2018_07_03',
            'size': 'pb({}), pbtxt({})'.format(mt.add_color('10.29 MB', ops='c'), mt.add_color('67.4 KB', ops='c')),
            'fps': '{} {}'.format(mt.add_color('38.72 FPS'), fps_info),
            'info': 'TODO',
        },
    },
    'ssd_mobilenet_v2_coco_2018_03_29': {
        'job': Jobs.OBJECT_DETECTION.value,
        'family': DnnFamily.TF.value,
        'in_dims': (800, 600),
        'scalefactor': 1,
        'mean': (0, 0, 0),
        'swapRB': True,
        'crop': False,
        'default_threshold': 0.2,
        'default_nms_threshold': 0.4,
        'labels_dict': COCO_183_LABELS,
        'URL': {
            'pbtxt': 'https://raw.githubusercontent.com/opencv/opencv_extra/master/testdata/dnn/' +
                     'ssd_mobilenet_v2_coco_2018_03_29.pbtxt',
            'pb': 'http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v2_coco_2018_03_29.tar.gz',
            'pbtxt_download_style': DownloadStyle.Direct.value,
            'pb_download_style': DownloadStyle.Tar.value,
            'pb_name': 'frozen_inference_graph.pb',
        },
        'info': {
            'web_name': 'ssd_mobilenet_v2_coco_2018_03_29',
            'size': 'pb({}), pbtxt({})'.format(mt.add_color('66.46 MB', ops='c'), mt.add_color('112.89 KB', ops='c')),
            'fps': '{} {}'.format(mt.add_color('6.57 FPS'), fps_info),
            'info': 'TODO',
        },
    },
}
MODELS_DNN_SEGMENTATION_META_DATA = {
    'fcn8s-heavy-pascal': {
        'job': Jobs.SEGMENTATION.value,
        'family': DnnFamily.Caffe.value,
        'in_dims': 'x',
        'scalefactor': 'x',
        'mean': 'x',
        'swapRB': False,
        'crop': False,
        'default_threshold': 0,
        'default_nms_threshold': 0,
        'labels_dict': 'x',
        'need_normalize': '??? normalize output needed',
        'URL': {
            'prototxt': 'https://raw.githubusercontent.com/opencv/opencv_extra/master/testdata/dnn/' +
                        'fcn8s-heavy-pascal.prototxt',
            'caffemodel': 'http://dl.caffe.berkeleyvision.org/fcn8s-heavy-pascal.caffemodel',
            'prototxt_download_style': DownloadStyle.Direct.value,
            'caffemodel_download_style': DownloadStyle.Direct.value,
        },
        'info': {
            'web_name': 'TODO',
            'size': 'TODO',
            'fps': 'TODO {}'.format(fps_info),
            'info': 'TODO',
        },
    },
}
MODELS_DNN_CLASSIFICATION_META_DATA = {

}
MODELS_OPEN_POSE_META_DATA = {
    'openpose_pose_mpi': {
        'job': Jobs.OPEN_POSE.value,
        'family': DnnFamily.Caffe.value,
        'in_dims': 'x',
        'scalefactor': 'x',
        'mean': 'x',
        'swapRB': False,
        'crop': False,
        'default_threshold': 0,
        'default_nms_threshold': 0,
        'labels_dict': 'x',
        'need_normalize': '??? normalize output needed',
        'URL': {
            'prototxt': 'https://raw.githubusercontent.com/opencv/opencv_extra/master/testdata/dnn/' +
                        'openpose_pose_mpi.prototxt',
            'caffemodel': 'http://posefs1.perception.cs.cmu.edu/OpenPose/models/pose/mpi/pose_iter_160000.caffemodel',
            'prototxt_download_style': DownloadStyle.Direct.value,
            'caffemodel_download_style': DownloadStyle.Direct.value,
        },
        'info': {
            'web_name': 'TODO',
            'size': 'TODO',
            'fps': 'TODO {}'.format(fps_info),
            'info': 'https://www.programmersought.com/article/3282857837/',
        },
    },
    'openpose_pose_coco': {
        'job': Jobs.OPEN_POSE.value,
        'family': DnnFamily.Caffe.value,
        'in_dims': 'x',
        'scalefactor': 'x',
        'mean': 'x',
        'swapRB': False,
        'crop': False,
        'default_threshold': 0,
        'default_nms_threshold': 0,
        'labels_dict': 'x',
        'need_normalize': '??? normalize output needed',
        'URL': {
            'prototxt': 'https://raw.githubusercontent.com/opencv/opencv_extra/master/testdata/dnn/' +
                        'openpose_pose_coco.prototxt',
            'caffemodel': 'http://posefs1.perception.cs.cmu.edu/OpenPose/models/pose/coco/pose_iter_440000.caffemodel',
            'prototxt_download_style': DownloadStyle.Direct.value,
            'caffemodel_download_style': DownloadStyle.Direct.value,
            'info1': 'https://github.com/CMU-Perceptual-Computing-Lab/openpose',
        },
        'info': {
            'web_name': 'TODO',
            'size': 'TODO',
            'fps': 'TODO {}'.format(fps_info),
            'info': 'https://github.com/CMU-Perceptual-Computing-Lab/openpose',
        },
    },
    'opencv_face_detector': {
        'job': Jobs.OPEN_POSE.value,
        'family': DnnFamily.Caffe.value,
        'in_dims': 'x',
        'scalefactor': 'x',
        'mean': 'x',
        'swapRB': False,
        'crop': False,
        'default_threshold': 0,
        'default_nms_threshold': 0,
        'labels_dict': 'x',
        'need_normalize': '??? normalize output needed',
        'URL': {
            'prototxt': 'https://raw.githubusercontent.com/opencv/opencv_extra/master/testdata/dnn/' +
                        'opencv_face_detector.prototxt',
            'caffemodel': 'https://github.com/opencv/opencv_3rdparty/raw/dnn_samples_face_detector_20170830/' +
                          'res10_300x300_ssd_iter_140000.caffemodel',
            'prototxt_download_style': DownloadStyle.Direct.value,
            'caffemodel_download_style': DownloadStyle.Direct.value,
            'info1': 'https://www.programmersought.com/article/16544476883/',
        },
        'info': {
            'web_name': 'TODO',
            'size': 'TODO',
            'fps': 'TODO {}'.format(fps_info),
            'info': 'https://www.programmersought.com/article/16544476883/',
        },
    },
}
