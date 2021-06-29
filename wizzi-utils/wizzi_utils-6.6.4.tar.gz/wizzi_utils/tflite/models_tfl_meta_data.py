import wizzi_utils.misc as mt
from wizzi_utils.open_cv.models_dnn_meta_data import Jobs
from wizzi_utils.open_cv.models_dnn_meta_data import DownloadStyle
from wizzi_utils.open_cv.labels_bank import COCO_80_RAW

# from wizzi_utils.open_cv.labels_bank import COCO_YOLO_80_LABELS
# from wizzi_utils.open_cv.models_dnn_meta_data import DownloadStyle
# from wizzi_utils.open_cv.labels_bank import PASCAL_VOC_2012_21_LABELS
# from wizzi_utils.open_cv.labels_bank import PASCAL_VOC_2012_20_LABELS
# from wizzi_utils.open_cv.labels_bank import ILSVRC2016_201_LABELS
# from wizzi_utils.open_cv.labels_bank import COCO_183_LABELS
# from wizzi_utils.open_cv.labels_bank import COCO_182_LABELS
# from wizzi_utils_test.downloaded_models.labels_bank import IMAGENET


# TODO check rpi guide
# https://www.tensorflow.org/lite/guide/python
# to move to mvs virtual env:
# cp -r /usr/lib/python3/dist-packages/tflite_runtime* ~/.virtualenvs/mvs/lib/python3.7/site-packages/
# TODO op1:
# $ wget "https://raw.githubusercontent.com/PINTO0309/TensorflowLite-bin/main/2.5.0/
#           download_tflite_runtime-2.5.0-cp37-none-linux_armv7l.whl.sh"
# $ ./download_tflite_runtime-2.5.0-cp37-none-linux_armv7l.whl.sh
# $ sudo pip3 install --upgrade tflite_runtime-2.5.0-cp37-none-linux_armv7l.whl
# from tflite_runtime.interpreter import Interpreter
# interpreter = Interpreter(model_path="foo.tflite", num_threads=4)

# https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi/blob/master/Raspberry_Pi_Guide.md
# https://blog.paperspace.com/tensorflow-lite-raspberry-pi/

# TODO more models:
# TODO: https://www.tensorflow.org/lite/guide/hosted_models
# TODO: https://github.com/tensorflow/models/blob/master/research/
#           object_detection/g3doc/tf1_detection_zoo.md#mobile-models  # m1-m4
# TODO: https://www.tensorflow.org/lite/guide/https://github.com/PINTO0309/PINTO_model_zoo
# ssd_mobilenet_coco -
# quick access to tflite models that were designed for devices such as raspberry pi, android and so on
# as far as i know all are ssd_mobilenet models that were trained on coco data set
test_fps_od_image_url = 'https://raw.githubusercontent.com/pjreddie/darknet/master/data/dog.jpg'
test_fps_od_iters = 10
test_fps_computer_info = 'AMD64, Intel64 Family 6 Model 158 Stepping 9, GenuineIntel, ' + \
                         'Physical cores 4, Total cores 8, Frequency 3601.00Mhz, CPU Usage 13.6%)'

fps_info = '({} iterations, the above cfg, on image {} on {})'.format(test_fps_od_iters, test_fps_od_image_url,
                                                                      test_fps_computer_info)

MODELS_TFL_META_DATA = {
    # see wu.tflt.get_all_object_detection_models_info(ack=True)
    'ssd_mobilenet_v3_small_coco_2020_01_14': {
        'job': Jobs.OBJECT_DETECTION.value,
        'default_threshold': 0.2,
        'default_nms': {
            'score_threshold': 0.4,
            'nms_threshold': 0.4,
        },
        'labels_dict': COCO_80_RAW,  # TODO labels are not correct
        'URL': {
            'tflite': 'http://download.tensorflow.org/models/object_detection/' +
                      'ssd_mobilenet_v3_small_coco_2020_01_14.tar.gz',
            'tflite_download_style': DownloadStyle.Tar.value,
            'tflite_name': 'model.tflite',
            'info': 'https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/'
                    + 'tf1_detection_zoo.md#mobile-models'
        },
        'info': {
            'web_name': 'TODO',
            'size': 'tflite({})'.format(mt.add_color('6.86 MB', ops='c')),
            'fps': '{} {}'.format(mt.add_color('21.96 FPS'), fps_info),
            'info': 'TODO',
        },
    },
    'ssd_mobilenet_v3_large_coco_2020_01_14': {
        'job': Jobs.OBJECT_DETECTION.value,
        'default_threshold': 0.2,
        'default_nms': {
            'score_threshold': 0.4,
            'nms_threshold': 0.4,
        },
        'labels_dict': COCO_80_RAW,
        'URL': {
            'tflite': 'http://download.tensorflow.org/models/object_detection/' +
                      'ssd_mobilenet_v3_large_coco_2020_01_14.tar.gz',
            'tflite_download_style': DownloadStyle.Tar.value,
            'tflite_name': 'model.tflite',
            'info': 'https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/'
                    + 'tf1_detection_zoo.md#mobile-models'
        },
        'info': {
            'web_name': 'TODO',
            'size': 'tflite({})'.format(mt.add_color('12.42 MB', ops='c')),
            'fps': '{} {}'.format(mt.add_color('12.94 FPS'), fps_info),
            'info': 'TODO',
        },
    },
    'ssd_mobilenet_v2_mnasfpn': {
        'job': Jobs.OBJECT_DETECTION.value,
        'default_threshold': 0.2,
        'default_nms': {
            'score_threshold': 0.4,
            'nms_threshold': 0.4,
        },
        'labels_dict': COCO_80_RAW,
        'URL': {
            'tflite': 'http://download.tensorflow.org/models/object_detection/' +
                      'ssd_mobilenet_v2_mnasfpn_shared_box_predictor_320x320_coco_sync_2020_05_18.tar.gz',
            'tflite_download_style': DownloadStyle.Tar.value,
            'tflite_name': 'model.tflite',
            'info': 'https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/'
                    + 'tf1_detection_zoo.md#mobile-models'
        },
        'info': {
            'web_name': 'TODO',
            'size': 'tflite({})'.format(mt.add_color('9.68 MB', ops='c')),
            'fps': '{} {}'.format(mt.add_color('5.65 FPS'), fps_info),
            'info': 'TODO',
        },
    },
    'ssdlite_mobiledet_cpu_320x320_coco_2020_05_19': {
        'job': Jobs.OBJECT_DETECTION.value,
        'default_threshold': 0.2,
        'default_nms': {
            'score_threshold': 0.4,
            'nms_threshold': 0.4,
        },
        'labels_dict': COCO_80_RAW,
        'URL': {
            'tflite': 'http://download.tensorflow.org/models/object_detection/' +
                      'ssdlite_mobiledet_cpu_320x320_coco_2020_05_19.tar.gz',
            'tflite_download_style': DownloadStyle.Tar.value,
            'tflite_name': 'model.tflite',
            'info': 'https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/'
                    + 'tf1_detection_zoo.md#mobile-models'
        },
        'info': {
            'web_name': 'TODO',
            'size': 'tflite({})'.format(mt.add_color('15.97 MB', ops='c')),
            'fps': '{} {}'.format(mt.add_color('11.01 FPS'), fps_info),
            'info': 'TODO',
        },
    },
    'ssd_mobilenet_v1_1_metadata_1': {
        'job': Jobs.OBJECT_DETECTION.value,
        'default_threshold': 0.2,
        'default_nms': {
            'score_threshold': 0.4,
            'nms_threshold': 0.4,
        },
        'labels_dict': COCO_80_RAW,
        'URL': {
            'tflite': 'https://tfhub.dev/tensorflow/lite-model/ssd_mobilenet_v1/1/metadata/1?lite-format=tflite',
            'tflite_download_style': DownloadStyle.Direct.value,
            'info': 'https://www.tensorflow.org/lite/examples/object_detection/overview'
        },
        'info': {
            'web_name': 'TODO',
            'size': 'tflite({})'.format(mt.add_color('3.99 MB', ops='c')),
            'fps': '{} {}'.format(mt.add_color('4.43 FPS'), fps_info),
            'info': 'TODO',
        },
    },
    'ssdlite_mobilenet_v2_coco_300_integer_quant_with_postprocess': {
        'job': Jobs.OBJECT_DETECTION.value,
        'default_threshold': 0.2,
        'default_nms': {
            'score_threshold': 0.4,
            'nms_threshold': 0.4,
        },
        'labels_dict': COCO_80_RAW,
        'URL': {
            'tflite': 'https://drive.google.com/' +
                      'uc?export=download&confirm=${CODE}&id=1LjTqn5nChAVKhXgwBUp00XIKXoZrs9sB',
            'tflite_download_style': DownloadStyle.Direct.value,
            'info': 'https://github.com/PINTO0309/PINTO_model_zoo/tree/main/006_mobilenetv2-ssdlite/01_coco/'
                    + '03_integer_quantization'
        },
        'info': {
            'web_name': 'TODO',
            'size': 'tflite({})'.format(mt.add_color('5.09 MB', ops='c')),
            'fps': '{} {}'.format(mt.add_color('0.63 FPS'), fps_info),
            'info': 'TODO',
        },
    },
    'coco_ssd_mobilenet_v1_1_0_quant_2018_06_29': {
        'job': Jobs.OBJECT_DETECTION.value,
        'default_threshold': 0.2,
        'default_nms': {
            'score_threshold': 0.4,
            'nms_threshold': 0.4,
        },
        'labels_dict': COCO_80_RAW,
        'URL': {
            'tflite': 'http://storage.googleapis.com/download.tensorflow.org/models/tflite/' +
                      'coco_ssd_mobilenet_v1_1.0_quant_2018_06_29.zip',
            'tflite_download_style': DownloadStyle.Zip.value,
            'tflite_name': 'detect.tflite',
            'info': 'https://gist.github.com/iwatake2222/e4c48567b1013cf31de1cea36c4c061c'
        },
        'info': {
            'web_name': 'TODO',
            'size': 'tflite({})'.format(mt.add_color('3.99 MB', ops='c')),
            'fps': '{} {}'.format(mt.add_color('5.10 FPS'), fps_info),
            'info': 'TODO',
        },
    },
    # 'pose_detection': {  # NOT TESTED
    #     'job': Jobs.OBJECT_DETECTION.value,
    #     'threshold': 0.2,
    #     'joint_names': [],
    #     'URL': {
    #         'tflite': 'https://github.com/google/mediapipe/raw/master/mediapipe/modules/pose_detection/' +
    #                   'pose_detection.tflite',
    #         'tflite_download_style': DownloadStyle.Direct.value,
    #         'info': 'https://github.com/google/mediapipe/tree/master/mediapipe/modules/pose_detection'
    #     },
    #     'info': {
    #         'web_name': 'TODO',
    #         'size': 'tflite({})'.format(mt.add_color('xxxx MB', ops='c')),
    #         'fps': '{} {}'.format(mt.add_color('xxxx FPS'), fps_info),
    #         'info': 'TODO',
    #     },
    # },
    'pose_landmark_lite': {
        'job': Jobs.OPEN_POSE.value,
        'threshold': 0.2,
        'joint_names': [
            'nose',  # 0
            'leftEyeInside',  # 1
            'leftEye',  # 2
            'leftEyeOutside',  # 3
            'rightEyeInside',  # 4
            'rightEye',  # 5
            'rightEyeOutside',  # 6
            'leftEar',  # 7
            'rightEar',  # 8
            'leftMouth',  # 9
            'rightMouth',  # 10
            'leftShoulder',  # 11
            'rightShoulder',  # 12
            'leftElbow',  # 13
            'rightElbow',  # 14
            'leftWrist',  # 15
            'rightWrist',  # 16
            'leftPalm',  # 17
            'rightPalm',  # 18
            'leftIndex',  # 19
            'rightIndex',  # 20
            'leftPinky',  # 21
            'rightPinky',  # 22
            'leftHip',  # 23
            'rightHip',  # 24
            'leftKnee',  # 25
            'rightKnee',  # 26
            'leftAnkle',  # 27
            'rightAnkle',  # 28
            'leftHeel',  # 29
            'rightHeel',  # 30
            'leftFoot',  # 31
            'rightFoot',  # 32
            # 'midHip',  # 33  # dont think it's supported
            # 'forehead',  # 34
            # 'leftThumb',  # 35
            # 'leftHand',  # 36
            # 'rightThumb',  # 37
            # 'rightHand',  # 38
        ],
        'connect_groups': [
            ['leftEar', 'leftEyeOutside', 'leftEye', 'leftEyeInside', 'nose', 'leftMouth', 'rightMouth', 'nose',
             'rightEyeInside', 'rightEye', 'rightEyeOutside', 'rightEar'],
            ['leftPalm', 'leftWrist', 'leftElbow', 'leftShoulder'],
            ['rightPalm', 'rightWrist', 'rightElbow', 'rightShoulder'],
            ['leftHip', 'leftKnee', 'leftAnkle', 'leftHeel', 'leftFoot'],
            ['rightHip', 'rightKnee', 'rightAnkle', 'rightHeel', 'rightFoot'],
            ['leftHip', 'rightHip', 'rightShoulder', 'leftShoulder', 'leftHip']
        ],
        'URL': {
            'tflite': 'https://github.com/google/mediapipe/raw/master/mediapipe/modules/pose_landmark/' +
                      'pose_landmark_lite.tflite',
            'tflite_download_style': DownloadStyle.Direct.value,
            'info': 'https://github.com/google/mediapipe/tree/master/mediapipe/modules/pose_landmark',
            'info2': 'https://github.com/vladmandic/blazepose/tree/fe647445507e37469d96da6fde5c8b0980f745bc'
        },
        'info': {
            'web_name': 'TODO',
            'size': 'tflite({})'.format(mt.add_color('xxxx MB', ops='c')),
            'fps': '{} {}'.format(mt.add_color('xxxx FPS'), fps_info),
            'info': 'TODO',
        },
    },
    'pose_landmark_full': {
        'job': Jobs.OPEN_POSE.value,
        'threshold': 0.2,
        'joint_names': [
            'nose',  # 0
            'leftEyeInside',  # 1
            'leftEye',  # 2
            'leftEyeOutside',  # 3
            'rightEyeInside',  # 4
            'rightEye',  # 5
            'rightEyeOutside',  # 6
            'leftEar',  # 7
            'rightEar',  # 8
            'leftMouth',  # 9
            'rightMouth',  # 10
            'leftShoulder',  # 11
            'rightShoulder',  # 12
            'leftElbow',  # 13
            'rightElbow',  # 14
            'leftWrist',  # 15
            'rightWrist',  # 16
            'leftPalm',  # 17
            'rightPalm',  # 18
            'leftIndex',  # 19
            'rightIndex',  # 20
            'leftPinky',  # 21
            'rightPinky',  # 22
            'leftHip',  # 23
            'rightHip',  # 24
            'leftKnee',  # 25
            'rightKnee',  # 26
            'leftAnkle',  # 27
            'rightAnkle',  # 28
            'leftHeel',  # 29
            'rightHeel',  # 30
            'leftFoot',  # 31
            'rightFoot',  # 32
            # 'midHip',  # 33  # dont think it's supported
            # 'forehead',  # 34
            # 'leftThumb',  # 35
            # 'leftHand',  # 36
            # 'rightThumb',  # 37
            # 'rightHand',  # 38
        ],
        'connect_groups': [
            ['leftEar', 'leftEyeOutside', 'leftEye', 'leftEyeInside', 'nose', 'leftMouth', 'rightMouth', 'nose',
             'rightEyeInside', 'rightEye', 'rightEyeOutside', 'rightEar'],
            ['leftPalm', 'leftWrist', 'leftElbow', 'leftShoulder'],
            ['rightPalm', 'rightWrist', 'rightElbow', 'rightShoulder'],
            ['leftHip', 'leftKnee', 'leftAnkle', 'leftHeel', 'leftFoot'],
            ['rightHip', 'rightKnee', 'rightAnkle', 'rightHeel', 'rightFoot'],
            ['leftHip', 'rightHip', 'rightShoulder', 'leftShoulder', 'leftHip']
        ],
        'URL': {
            'tflite': 'https://github.com/google/mediapipe/raw/master/mediapipe/modules/pose_landmark/' +
                      'pose_landmark_full.tflite',
            'tflite_download_style': DownloadStyle.Direct.value,
            'info': 'https://github.com/google/mediapipe/tree/master/mediapipe/modules/pose_detection',
            'info2': 'https://github.com/vladmandic/blazepose/tree/fe647445507e37469d96da6fde5c8b0980f745bc'
        },
        'info': {
            'web_name': 'TODO',
            'size': 'tflite({})'.format(mt.add_color('xxxx MB', ops='c')),
            'fps': '{} {}'.format(mt.add_color('xxxx FPS'), fps_info),
            'info': 'TODO',
        },
    },
    'pose_landmark_heavy': {
        'job': Jobs.OPEN_POSE.value,
        'threshold': 0.2,
        'joint_names': [
            'nose',  # 0
            'leftEyeInside',  # 1
            'leftEye',  # 2
            'leftEyeOutside',  # 3
            'rightEyeInside',  # 4
            'rightEye',  # 5
            'rightEyeOutside',  # 6
            'leftEar',  # 7
            'rightEar',  # 8
            'leftMouth',  # 9
            'rightMouth',  # 10
            'leftShoulder',  # 11
            'rightShoulder',  # 12
            'leftElbow',  # 13
            'rightElbow',  # 14
            'leftWrist',  # 15
            'rightWrist',  # 16
            'leftPalm',  # 17
            'rightPalm',  # 18
            'leftIndex',  # 19
            'rightIndex',  # 20
            'leftPinky',  # 21
            'rightPinky',  # 22
            'leftHip',  # 23
            'rightHip',  # 24
            'leftKnee',  # 25
            'rightKnee',  # 26
            'leftAnkle',  # 27
            'rightAnkle',  # 28
            'leftHeel',  # 29
            'rightHeel',  # 30
            'leftFoot',  # 31
            'rightFoot',  # 32
            # 'midHip',  # 33  # dont think it's supported
            # 'forehead',  # 34
            # 'leftThumb',  # 35
            # 'leftHand',  # 36
            # 'rightThumb',  # 37
            # 'rightHand',  # 38
        ],
        'connect_groups': [
            ['leftEar', 'leftEyeOutside', 'leftEye', 'leftEyeInside', 'nose', 'leftMouth', 'rightMouth', 'nose',
             'rightEyeInside', 'rightEye', 'rightEyeOutside', 'rightEar'],
            ['leftPalm', 'leftWrist', 'leftElbow', 'leftShoulder'],
            ['rightPalm', 'rightWrist', 'rightElbow', 'rightShoulder'],
            ['leftHip', 'leftKnee', 'leftAnkle', 'leftHeel', 'leftFoot'],
            ['rightHip', 'rightKnee', 'rightAnkle', 'rightHeel', 'rightFoot'],
            ['leftHip', 'rightHip', 'rightShoulder', 'leftShoulder', 'leftHip']
        ],
        'URL': {
            'tflite': 'https://github.com/google/mediapipe/raw/master/mediapipe/modules/pose_landmark/' +
                      'pose_landmark_heavy.tflite',
            'tflite_download_style': DownloadStyle.Direct.value,
            'info': 'https://github.com/google/mediapipe/tree/master/mediapipe/modules/pose_detection',
            'info2': 'https://github.com/vladmandic/blazepose/tree/fe647445507e37469d96da6fde5c8b0980f745bc'
        },
        'info': {
            'web_name': 'TODO',
            'size': 'tflite({})'.format(mt.add_color('xxxx MB', ops='c')),
            'fps': '{} {}'.format(mt.add_color('xxxx FPS'), fps_info),
            'info': 'TODO',
        },
    },
}
