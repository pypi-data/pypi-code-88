from wizzi_utils import misc_tools as mt  # misc tools
from wizzi_utils.open_cv import open_cv_tools as cvt
from wizzi_utils.tflite.models_tfl_meta_data import MODELS_TFL_META_DATA
import numpy as np
import os
import math
# noinspection PyPackageRequirements
import cv2
# noinspection PyPackageRequirements
import tflite_runtime
from tflite_runtime.interpreter import Interpreter


# try:
#     # noinspection PyUnresolvedReferences
#     interpreter_found = tflite_runtime.interpreter.Interpreter
#     print('success using tflite_runtime.interpreter.Interpreter')
# except AttributeError:
#     # print('failure using tflite_runtime.interpreter.Interpreter')
#     try:
#         # noinspection PyPackageRequirements,PyUnresolvedReferences
#         import tensorflow as tf
#
#         interpreter_found = tf.lite.Interpreter
#         print('success using tf.lite.Interpreter')
#     except (ImportError, AttributeError):
#         pass
#         print('failure using tf.lite.Interpreter')


def get_tflite_version(ack: bool = False, tabs: int = 1) -> str:
    """
    :param ack:
    :param tabs:
    :return:
    see get_tflite_version_test()
    """
    string = mt.add_color('{}* TFLite Version {}'.format(tabs * '\t', tflite_runtime.__version__), ops=mt.SUCCESS_C)
    # string += mt.add_color(' - GPU detected ? ', op1=mt.SUCCESS_C)
    # if gpu_detected():
    #     string += mt.add_color('True', op1=mt.SUCCESS_C2[0], extra_ops=mt.SUCCESS_C2[1])
    # else:
    #     string += mt.add_color('False', op1=mt.FAIL_C2[0], extra_ops=mt.FAIL_C2[1])
    if ack:
        print(string)
    return string


def gpu_detected() -> bool:
    """
    :return:
    TODO FUTURE - maybe check if threads available
    """
    return False


class TfltObjectDetectionModels:
    """
    """
    # each MODELS_DNN_META_DATA entry should have this keys:
    MANDATORY_KEYS = ['job', 'default_threshold', 'default_nms', 'labels_dict', 'URL']

    DEFAULT_COLOR_D = {
        'bbox': 'r',
        'label_bbox': 'black',
        'text': 'white',
        'sub_image': 'blue',
    }

    def __init__(self,
                 save_load_dir: str,
                 model_name: str,
                 allowed_class: list = None,
                 threshold: float = None,
                 nms: dict = None,
                 tabs: int = 1
                 ):
        """
        :param save_load_dir: where the model is saved (or will be if not exists)
        :param model_name: valid name in MODEL_CONF.keys()
        :param threshold: only detection above this threshold will be pass first filter
        :param nms: non maximum suppression threshold 2 thresholds
            score_threshold and nms_threshold
            can be None in the cfg - if None pass and None on cfg: no nms
        :param allowed_class: ignore rest of class. list of strings
        :param tabs:
        see:
        best_model_images_test()
        best_model_video_test()
        best_model_cam_test()
        models_compare_images_test()
        models_compare_video_test()
        models_compare_cam_test()
        TODO measure fps
        """
        if model_name not in MODELS_TFL_META_DATA:
            mt.exception_error('model name must be one of {}'.format(list(MODELS_TFL_META_DATA.keys())),
                               real_exception=False, tabs=tabs)
            exit(-1)
        else:  # supported model
            self.model_conf = MODELS_TFL_META_DATA[model_name]
            mandatory_keys_list = self.MANDATORY_KEYS[:]
            current_keys_list = list(self.model_conf.keys())
            man_keys_not_found = []
            for man_k in mandatory_keys_list:
                if man_k not in current_keys_list:
                    man_keys_not_found.append(man_k)
            if len(man_keys_not_found) > 0:
                mt.exception_error('model config must have the keys {}'.format(man_keys_not_found),
                                   real_exception=False, tabs=tabs)
                exit(-1)
        self.tabs = tabs
        tabs_s = self.tabs * '\t'
        self.name = model_name
        self.local_path = save_load_dir
        self.labels = self.model_conf['labels_dict']['labels']
        self.allowed_class = allowed_class if allowed_class is not None else self.labels
        # detection threshold
        self.threshold = threshold if threshold is not None else self.model_conf['default_threshold']

        # self.nms_threshold could be none in the cfg
        self.nms = nms if nms is not None else self.model_conf['default_nms']

        if not os.path.exists(save_load_dir):
            mt.create_dir(save_load_dir)

        model_tflite = "{}/{}.tflite".format(self.local_path, self.name)
        print('{}Loading {}(size {}, {} classes)'.format(tabs_s, os.path.basename(model_tflite),
                                                         mt.file_or_folder_size(model_tflite), len(self.labels)))

        # noinspection PyProtectedMember
        cvt.DnnObjectDetectionModels._download_if_needed(local_path=model_tflite, url_dict=self.model_conf['URL'],
                                                         file_key='tflite')

        self.interpreter = Interpreter(model_path=model_tflite, num_threads=4)
        # try:  # should work on RPi
        #     # self.interpreter.set_num_threads(4)
        #     # self.interpreter.SetNumThreads(4)
        #     print('4 working threads')
        # except AttributeError as e:
        #     mt.exception_error('threads allocation failed: {}'.format(e), tabs=tabs)

        # allocate input output placeholders
        self.interpreter.allocate_tensors()
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()
        _, input_height, input_width, _ = self.interpreter.get_input_details()[0]['shape']
        self.model_conf['in_dims'] = (input_width, input_height)
        self.model_conf['input_type'] = self.interpreter.get_input_details()[0]['dtype']
        quantization = self.interpreter.get_input_details()[0]['quantization']
        # need to normalize if model doesn't do quantization (then quantization == (0.0, 0))
        # else e.g. quantization == (0.0078125, 128) - no need to normalize
        self.model_conf['normalize_RGB'] = True if quantization == (0.0, 0) else False

        # # you can print this to get more details on the model
        # mt.dict_as_table(self.interpreter.get_input_details()[0], title='input')
        # mt.dict_as_table(self.interpreter.get_output_details()[0], title='output')
        # mt.dict_as_table(self.interpreter.get_tensor_details()[0], title='tensor')
        return

    def __str__(self):
        string = '{}{}'.format(self.tabs * '\t', mt.add_color(string='TfltObjectDetectionModels:', ops='underlined'))
        string += '\n\t{}name={}'.format(self.tabs * '\t', self.name)
        string += '\n\t{}local_path={}'.format(self.tabs * '\t', self.local_path)
        string += '\n\t{}threshold={}'.format(self.tabs * '\t', self.threshold)
        string += '\n\t{}nms={}'.format(self.tabs * '\t', self.nms)
        string += '\n\t{}{}'.format(self.tabs * '\t', mt.to_str(self.allowed_class, 'allowed_class'))
        string += '\n\t{}tabs={}'.format(self.tabs * '\t', self.tabs)
        string += '\n{}'.format(mt.dict_as_table(self.model_conf, title='conf', fp=6, ack=False, tabs=self.tabs + 1))
        return string

    def prepare_input(self, cv_img: np.array) -> np.array:
        """
        :param cv_img:
        resize and change dtype to predefined params
        :return:
        """
        img_RGB = cvt.BGR_img_to_RGB(cv_img)
        if self.model_conf['normalize_RGB']:
            # normalization is done via the authors of the MobileNet SSD implementation
            center = 127.5
            img_RGB = (img_RGB - center) / center  # normalize image
        img = cv2.resize(img_RGB, self.model_conf['in_dims'])  # size of this model input
        img_processed = np.expand_dims(img, axis=0).astype(self.model_conf['input_type'])  # a,b,c -> 1,a,b,c

        return img_processed

    def run_network(self, img_preprocessed: np.array) -> None:
        self.interpreter.set_tensor(self.input_details[0]['index'], img_preprocessed)  # set input tensor
        self.interpreter.invoke()  # run
        return

    def extract_results(
            self,
            cv_img: np.array,
            fp: int = 2,
            ack: bool = False,
            tabs: int = 1,
            img_title: str = None
    ) -> list:
        """
        :param cv_img: cv image
        :param fp: float precision on the score precentage. e.g. fp=2: 0.1231231352353 -> 12.31%
        :param ack: if True: print meta data and detections
        :param tabs: if ack True: tabs for print
        :param img_title: if ack True: title for print
        :return: list of dicts:
        dict is a detection of an object above threshold.
            has items:
                label:str e.g. 'person'
                score_percentage: float e.g. 12.31
                bbox: dict with keys x0,y0,x1,y1
                #  pt1 = (x0, y0)  # obj frame top left corner
                #  pt2 = (x1, y1)  # obj frame bottom right corner
        """
        # get results
        boxes_np = self.interpreter.get_tensor(self.output_details[0]['index'])[0]  # bboxes
        labels_ids_np = self.interpreter.get_tensor(self.output_details[1]['index'])[0]  # labels as list of floats
        scores_np = self.interpreter.get_tensor(self.output_details[2]['index'])[0]  # confidence
        # count_np = interpreter.get_tensor(output_details[3]['index'])[0]  # number of detections

        if ack:
            title_suffix = '' if img_title is None else '{} '.format(img_title)
            title = '{} detections({}) on image {}{}:'.format(self.name, len(scores_np), title_suffix, cv_img.shape)
            print('{}{}'.format(tabs * '\t', title))
            print('\n{}Meta_data(all detections):'.format(tabs * '\t'))
            print('{}\t{}'.format(tabs * '\t', mt.to_str(labels_ids_np, 'labels_ids_np')))
            print('{}\t{}'.format(tabs * '\t', mt.to_str(scores_np, 'scores')))
            print('{}\t{}'.format(tabs * '\t', mt.to_str(boxes_np, 'boxes')))

            print('\n{}Detections post first threshold and allowed_class:'.format(tabs * '\t'))
        if len(scores_np) <= 0:
            # no detections made
            if ack:
                print('{}\tNo detections found'.format(tabs * '\t'))
            return []
        boxes_nms_form_list = []  # x,y,w,h in proportion to the image, UNLIKE boxes_np which is x0,y0,x1,y1
        passed_first_filter = []  # threshold <= confidence and label in self.allowed_class
        img_h, img_w = cv_img.shape[0], cv_img.shape[1]
        for i, (bbox, label_id, confidence) in enumerate(zip(boxes_np, labels_ids_np, scores_np)):
            if self.threshold <= confidence <= 1.0 and label_id is not math.isnan(label_id):
                label = self.labels[int(label_id)]
                if label in self.allowed_class:
                    # prepare box nms form and save index passed
                    center_x = int(bbox[0] * img_w)
                    center_y = int(bbox[1] * img_h)
                    w = int(bbox[2] * img_w)
                    h = int(bbox[3] * img_h)
                    x = center_x - w / 2
                    y = center_y - h / 2
                    boxes_nms_form_list.append([x, y, w, h])
                    passed_first_filter.append(i)
                    if ack:
                        msg = '{}\t{})Detected class {}: {}({:.2f}%)'
                        print(msg.format(tabs * '\t', i, int(label_id), label, confidence * 100))

        boxes_np = boxes_np[passed_first_filter]
        labels_ids_np = labels_ids_np[passed_first_filter]
        scores_np = scores_np[passed_first_filter]
        if len(scores_np) <= 0:
            if ack:
                print('{}\tNo detections passed first filter'.format(tabs * '\t'))
            return []
        if ack:
            print('{}Meta_data:'.format(tabs * '\t'))
            print('{}\t{}'.format(tabs * '\t', mt.to_str(labels_ids_np, 'labels_ids_np')))
            print('{}\t{}'.format(tabs * '\t', mt.to_str(scores_np, 'scores')))
            print('{}\t{}'.format(tabs * '\t', mt.to_str(boxes_np, 'boxes')))

        if self.nms is not None:  # activate nms
            # https://gist.github.com/leandrobmarinho/26bd5eb9267654dbb9e37f34788486b5
            passed_nms_filter = cv2.dnn.NMSBoxes(
                bboxes=boxes_nms_form_list,
                scores=scores_np.tolist(),
                score_threshold=self.nms['score_threshold'],
                nms_threshold=self.nms['nms_threshold']
            )
            if len(passed_nms_filter) > 0:
                passed_nms_filter = passed_nms_filter.flatten()
                boxes_np = boxes_np[passed_nms_filter]
                labels_ids_np = labels_ids_np[passed_nms_filter]
                scores_np = scores_np[passed_nms_filter]
            else:
                scores_np = []

            if ack:
                print('\n{}Meta_data(post-nms):'.format(tabs * '\t'))
                print('{}\t{}'.format(tabs * '\t', mt.to_str(passed_nms_filter, 'pick indices')))
                print('{}\t{}'.format(tabs * '\t', mt.to_str(labels_ids_np, 'labels_ids_np')))
                print('{}\t{}'.format(tabs * '\t', mt.to_str(scores_np, 'scores')))
                print('{}\t{}'.format(tabs * '\t', mt.to_str(boxes_np, 'boxes')))
                print('{}Detections:'.format(tabs * '\t'))
            if len(scores_np) <= 0:
                if ack:
                    print('{}\tNo detections passed nms filter'.format(tabs * '\t'))
                return []

        detections = []
        for i, (bbox, label_id, confidence) in enumerate(zip(boxes_np, labels_ids_np, scores_np)):
            if self.threshold <= confidence <= 1.0 and label_id is not math.isnan(label_id):
                label = self.labels[int(label_id)]
                if label in self.allowed_class:
                    x0 = max(int(bbox[1] * img_w), 0)  # dont exceed 0
                    y0 = max(int(bbox[0] * img_h), 0)  # dont exceed 0
                    x1 = min(int(bbox[3] * img_w), img_w)  # dont exceed frame width
                    y1 = min(int(bbox[2] * img_h), img_h)  # dont exceed frame height
                    score_percentage = round(confidence * 100, fp)

                    detection_d = {
                        'label': label,
                        'score_percentage': score_percentage,
                        'bbox': {
                            #  pt1 = (x0, y0)  # obj frame top left corner
                            #  pt2 = (x1, y1)  # obj frame bottom right corner
                            'x0': x0,
                            'y0': y0,
                            'x1': x1,
                            'y1': y1,
                        },
                    }
                    detections.append(detection_d)
                    if ack:
                        d_msg = '{}\t{})Detected {}({}%) in top left=({}), bottom right=({})'
                        print(d_msg.format(tabs * '\t', i, label, score_percentage, (x0, y0), (x1, y1)))
        return detections

    def detect_cv_img(
            self,
            cv_img: np.array,
            fp: int = 2,
            ack: bool = False,
            tabs: int = 1,
            img_title: str = None
    ) -> list:
        """
        :param cv_img: open cv image
        :param fp: float precision on the score precentage. e.g. fp=2: 0.1231231352353 -> 12.31%
        :param ack: if True: print meta data and detections
        :param tabs: if ack True: tabs for print
        :param img_title: if ack True: title for print
        :return: list of dicts. see extract_results()
        """

        img_preprocessed = self.prepare_input(cv_img)
        self.run_network(img_preprocessed)
        detections = self.extract_results(
            cv_img=cv_img,
            fp=fp,
            ack=ack,
            tabs=tabs,
            img_title=img_title
        )
        return detections

    @staticmethod
    def add_traffic_light_to_detections(detections: list, traffic_light_p: dict) -> list:
        """
        see cvt.dnn_models.add_traffic_light_to_detections
        """
        detections = cvt.DnnObjectDetectionModels.add_traffic_light_to_detections(
            detections=detections,
            traffic_light_p=traffic_light_p
        )
        return detections

    @staticmethod
    def add_sub_sub_image_to_detection(detections: list, cv_img: np.array, bbox_image_p: dict) -> list:
        """
        see cvt.dnn_models.add_sub_sub_image_to_detection
        """
        detections = cvt.DnnObjectDetectionModels.add_sub_sub_image_to_detection(
            detections=detections,
            cv_img=cv_img,
            bbox_image_p=bbox_image_p
        )
        return detections

    @staticmethod
    def draw_detections(
            detections: list,
            colors_d: dict,
            cv_img: np.array,
            draw_labels: bool = True,
            ack: bool = False,
            tabs: int = 1,
            img_title: str = None
    ) -> None:
        """
        see cvt.dnn_models.draw_detections
        """
        cvt.DnnObjectDetectionModels.draw_detections(
            detections=detections,
            colors_d=colors_d,
            cv_img=cv_img,
            draw_labels=draw_labels,
            ack=ack,
            tabs=tabs,
            img_title=img_title
        )
        return


def get_all_object_detection_models_info(ack: bool = False) -> list:
    model_names = []
    for i, (m_name, m_dict) in enumerate(MODELS_TFL_META_DATA.items()):
        if ack:
            mt.dict_as_table(table=m_dict['info'], title='{}: {}'.format(i + 1, m_name), tabs=0)
        model_names.append(m_name)
    return model_names
