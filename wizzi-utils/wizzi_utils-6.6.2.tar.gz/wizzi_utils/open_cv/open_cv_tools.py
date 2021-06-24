import numpy as np
import math
import os
from wizzi_utils.pyplot import pyplot_tools as pyplt
from wizzi_utils.misc import misc_tools as mt
from wizzi_utils.socket import socket_tools as st
from wizzi_utils.open_cv.models_dnn_meta_data import MODELS_DNN_OBJECT_DETECTION_META_DATA
from wizzi_utils.open_cv.models_dnn_meta_data import Jobs
from wizzi_utils.open_cv.models_dnn_meta_data import DnnFamily
from wizzi_utils.open_cv.models_dnn_meta_data import DownloadStyle
# noinspection PyPackageRequirements
import cv2


def get_cv_version(ack: bool = False, tabs: int = 1) -> str:
    """ see get_cv_version_test() """
    """ see get_cv_version_test() """
    string = mt.add_color('{}* OpenCv Version {}'.format(tabs * '\t', cv2.getVersionString()), ops=mt.SUCCESS_C)
    if ack:
        print(string)
    return string


def load_img(path: str, ack: bool = True, tabs: int = 1) -> np.array:
    """ see imread_imwrite_test() """
    if os.path.exists(path):
        img = cv2.imread(path)
        if ack:
            size_s = mt.file_or_folder_size(path)
            file_msg = '{}({}) of shape {}'.format(path, size_s, img.shape)
            print('{}{}'.format(tabs * '\t', mt.LOADED.format(file_msg)))
    else:
        mt.exception_error(mt.NOT_FOUND.format(path), real_exception=False, tabs=tabs)
        img = None
    return img


def save_img(path: str, img: np.array, ack: bool = True, tabs: int = 1) -> None:
    """ see imread_imwrite_test() """
    if os.path.exists(os.path.dirname(path)):
        cv2.imwrite(path, img)
        if ack:
            size_s = mt.file_or_folder_size(path)
            file_msg = '{}({}) of shape {}'.format(path, size_s, img.shape)
            print('{}{}'.format(tabs * '\t', mt.SAVED.format(file_msg)))
    else:
        mt.exception_error(mt.NOT_FOUND.format(os.path.dirname(path)), real_exception=False)
    return


def list_to_cv_image(cv_img: [list, np.array]) -> np.array:
    """
    :param cv_img: numpy or list. if list: convert to numpy with dtype uint8
    :return: cv_img
    see list_to_cv_image_test()
    """
    if mt.is_list(cv_img):
        cv_img = np.array(cv_img, dtype='uint8')
    return cv_img


def display_open_cv_image(
        img: np.array,
        ms: int = 0,
        title: str = 'cv_image',
        loc: (tuple, str) = None,
        resize: float = None,
        header: str = None,
        save_path: str = None,
        tabs: int = 1,
) -> None:
    """
    :param img: cv image in numpy array or list
    :param ms: 0 blocks, else time in milliseconds before image is closed
    :param title: window title
    :param loc: top left corner window location
        if tuple: x,y coordinates
        if str: see Location enum in pyplt. e.g. pyplt.Location.TOP_LEFT.value (which is 'top_left')
    :param resize: None for original size. else img_size *= resize (resize > 0)
    :param header: text to add at the top left
    :param save_path: if not none, saves image to this path
    :param tabs:
    see display_open_cv_image_test()
    """
    img = list_to_cv_image(img)
    if resize is not None:
        img = resize_opencv_image(img, resize)
    if header is not None:
        add_header(img, header, bg_font_scale=2)
    if save_path is not None:
        save_img(path=save_path, img=img, ack=True, tabs=tabs)
    cv2.imshow(title, img)
    if loc is not None:
        if mt.is_str(loc):
            move_cv_img_by_str(img, title, where=loc)
        elif mt.is_tuple(loc):
            move_cv_img_x_y(title, x_y=loc)
    cv2.waitKey(ms)
    return


def resize_opencv_image(img: np.array, scale_percent: float):
    """
    :param img: cv img
    :param scale_percent: float>0(could be bigger than 1)
    img_size *= scale_percent
    see resize_opencv_image_test()
    """
    if scale_percent is None or scale_percent <= 0:
        resize_image = img
        mt.exception_error('illegal value for scale_percent={}'.format(scale_percent), real_exception=False, tabs=0)
    else:
        width = math.ceil(img.shape[1] * scale_percent)
        height = math.ceil(img.shape[0] * scale_percent)
        dim = (width, height)
        resize_image = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    return resize_image


def move_cv_img_x_y(win_title: str, x_y: tuple) -> None:
    """
    :param win_title: cv img with win_title to be moved
    :param x_y: tuple of ints. x,y of top left corner
    Move cv img upper left corner to pixel (x, y)
    see move_cv_img_x_y_test()
    """
    cv2.moveWindow(win_title, x_y[0], x_y[1])
    return


def move_cv_img_by_str(img: np.array, win_title: str, where: str = pyplt.Location.TOP_LEFT.value) -> None:
    """
    :param img: to get the dims of the image
    :param win_title: cv img with win_title to be moved
    :param where: see Location enum in pyplt. e.g. pyplt.Location.TOP_LEFT.value (which is 'top_left')
    Move cv img upper left corner to pixel (x, y)
    see move_cv_img_by_str_test()
    """
    try:
        window_w, window_h = pyplt.screen_dims()  # screen dims in pixels
        if window_w != -1 and window_h != -1:
            fig_w, fig_h = img.shape[1], img.shape[0]
            task_bar_offset = 75  # about 75 pixels due to task bar

            x, y = 0, 0  # Location.TOP_LEFT.value: default
            if where == pyplt.Location.TOP_CENTER.value:
                x = (window_w - fig_w) / 2
                y = 0
            elif where == pyplt.Location.TOP_RIGHT.value:
                x = window_w - fig_w
                y = 0
            elif where == pyplt.Location.CENTER_LEFT.value:
                x = 0
                y = (window_h - fig_h - task_bar_offset) / 2
            elif where == pyplt.Location.CENTER_CENTER.value:
                x = (window_w - fig_w) / 2
                y = (window_h - fig_h - task_bar_offset) / 2
            elif where == pyplt.Location.CENTER_RIGHT.value:
                x = window_w - fig_w
                y = (window_h - fig_h - task_bar_offset) / 2
            elif where == pyplt.Location.BOTTOM_LEFT.value:
                x = 0
                y = window_h - fig_h - task_bar_offset
            elif where == pyplt.Location.BOTTOM_CENTER.value:
                x = (window_w - fig_w) / 2
                y = window_h - fig_h - task_bar_offset
            elif where == pyplt.Location.BOTTOM_RIGHT.value:
                x = window_w - fig_w
                y = window_h - fig_h - task_bar_offset
            x, y = int(x), int(y)
            move_cv_img_x_y(win_title, x_y=(x, y))
        else:
            move_cv_img_x_y(win_title, x_y=(0, 0))
    except (ValueError, Exception) as e:
        mt.exception_error(e, real_exception=True)
        move_cv_img_x_y(win_title, x_y=(0, 0))
    return


def unpack_list_imgs_to_big_image(imgs: list, grid: tuple, resize: float = None) -> np.array:
    """
    :param imgs: list of cv images
    :param resize: resize factor
    :param grid: the layout you want as output
        (1,len(imgs)): 1 row
        (len(imgs),1): 1 col
        (2,2): 2x2 grid - supports len(imgs)<=4 but not more
    see unpack_list_imgs_to_big_image_test()
    """
    for i in range(len(imgs)):
        imgs[i] = list_to_cv_image(imgs[i])
        if resize is not None:
            imgs[i] = resize_opencv_image(imgs[i], resize)
        if len(imgs[i].shape) == 2:  # if gray - see as rgb
            imgs[i] = gray_scale_img_to_BGR_form(imgs[i])

    imgs_n = len(imgs)
    if imgs_n == 1:
        big_img = imgs[0]
    else:
        padding_bgr = list(pyplt.get_BGR_color('red'))
        height, width, cnls = imgs[0].shape
        rows, cols = grid
        big_img = np.zeros(shape=(height * rows, width * cols, cnls), dtype='uint8') + 255  # white big image

        row_ind, col_ind = 1, 1
        for i, img in enumerate(imgs):
            h_begin, h_end = height * (row_ind - 1), height * row_ind
            w_begin, w_end = width * (col_ind - 1), width * col_ind
            big_img[h_begin:h_end, w_begin:w_end, :] = img  # 0

            if rows > 1:  # draw bounding box on the edges. no need if there is 1 row or 1 col
                big_img[h_begin, w_begin:w_end, :] = padding_bgr
                big_img[h_end - 1, w_begin:w_end - 1, :] = padding_bgr
            if cols > 1:
                big_img[h_begin:h_end, w_begin, :] = padding_bgr
                big_img[h_begin:h_end, w_end - 1, :] = padding_bgr

            col_ind += 1
            if col_ind > cols:
                col_ind = 1
                row_ind += 1
    return big_img


def display_open_cv_images(
        imgs: list,
        ms: int = 0,
        title: str = 'cv_image',
        loc: (tuple, str) = None,
        resize: float = None,
        grid: tuple = (1, 2),
        header: str = None,
        save_path: str = None,
        tabs: int = 1,
) -> None:
    """
    :param imgs: list of RGB or gray scale images
    :param ms: 0 blocks, else time in milliseconds before image is closed
    :param title: window title
    :param loc: top left corner window location
        if tuple: x,y coordinates
        if str: see Location enum in pyplt. e.g. pyplt.Location.TOP_LEFT.value (which is 'top_left')
    :param resize: None for original size. else img_size *= resize (resize > 0)
    :param grid: size of rows and cols of the new image. e.g. (2,1) 2 rows with 1 img on each
        grid slots must be >= len(imgs)
    :param header: text to add at the top left
    :param save_path: if not none, saves image to this path
    :param tabs:
    see display_open_cv_images_test()
    """
    imgs_n = len(imgs)
    if imgs_n > 0:
        total_slots = grid[0] * grid[1]
        assert imgs_n <= total_slots, 'grid has {} total_slots, but len(imgs)={}'.format(total_slots, imgs_n)
        big_img = unpack_list_imgs_to_big_image(imgs, grid=grid, resize=resize)
        display_open_cv_image(big_img, ms=ms, title=title, loc=loc, resize=None, header=header, save_path=save_path,
                              tabs=tabs)
    return


def gray_scale_img_to_BGR_form(gray_img: np.array) -> np.array:
    """
    :param gray_img: from shape (x,y) - 1 channel (gray)
    e.g 480,640
    :return: RGB form image e.g 480,640,3. no real colors added - just shape as RGB
    see gray_to_BGR_and_back_test()
    """
    BGR_image = cv2.cvtColor(gray_img, cv2.COLOR_GRAY2BGR)
    return BGR_image


def BGR_img_to_gray(bgr_img: np.array) -> np.array:
    """
    :param bgr_img: from shape (x,y,3) - 3 channels
    e.g 480,640,3
    :return: gray image e.g 480,640. colors are replaced to gray colors
    see gray_to_BGR_and_back_test()
    """
    gray = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)
    return gray


def BGR_img_to_RGB(bgr_img: np.array) -> np.array:
    """
    :param bgr_img: from shape (x,y,3) - 3 channels
    e.g 480,640,3
    :return: rgb image
    see BGR_img_to_RGB_and_back_test()
    """
    rgb_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2RGB)
    return rgb_img


def RGB_img_to_BGR(rgb_img: np.array) -> np.array:
    """
    :param rgb_img: from shape (x,y,3) - 3 channels
    e.g 480,640,3
    :return: bgr image
    see BGR_img_to_RGB_and_back_test()
    """
    bgr_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2BGR)
    return bgr_img


class CameraWu:
    def __init__(self, port: int, type_cam: str = 'cv2'):
        self.port = port
        self.type_cam = type_cam
        try:
            pip_err = 'Error {}. pip install {}'
            failed_err = 'Failed to open CameraWu({}) on port {}'.format(type_cam, port)
            if type_cam == 'acapture':
                try:
                    # noinspection PyPackageRequirements
                    import acapture  # pip install acapture
                    if mt.is_linux():  # NOT TESTED
                        acapture.camera_info()
                    if not self.check_port_valid(port):
                        self.cam = None
                        raise Exception(failed_err)
                    self.cam = acapture.open(port)
                    success, frame = self.cam.read()
                    if frame is None:
                        self.cam = None
                        raise Exception(failed_err)
                except ModuleNotFoundError as e:
                    self.cam = None
                    raise ModuleNotFoundError(pip_err.format(e, 'acapture'))
            elif type_cam == 'imutils':
                try:
                    # noinspection PyPackageRequirements,PyUnresolvedReferences
                    from imutils import video  # pip install imutils
                    self.cam = video.VideoStream(src=port).start()
                    frame = self.cam.read()
                    if frame is None:
                        self.cam = None
                        raise Exception(failed_err)
                except ModuleNotFoundError as e:
                    self.cam = None
                    raise ModuleNotFoundError(pip_err.format(e, 'imutils'))
            else:  # type_cam == 'cv2'
                self.cam = cv2.VideoCapture(port)
                if not self.cam.isOpened():
                    self.cam = None
                    raise Exception(failed_err)
        except Exception as e:
            raise e
        return

    @classmethod
    def open_camera(cls, port: int, type_cam: str = 'cv2'):
        try:
            cam = cls(port, type_cam)
            print('\tCameraWu({}) successfully open on port {}'.format(type_cam, port))
        except (ModuleNotFoundError, Exception) as e:
            mt.exception_error(e, real_exception=True, tabs=1)
            cam = None
        return cam

    @staticmethod
    def check_port_valid(port: int) -> bool:
        """
        :param port:
        :return:
        """
        temp_cam = cv2.VideoCapture(port)
        if temp_cam.isOpened():
            ret = True
            temp_cam.release()
        else:
            ret = False
        return ret

    def __del__(self):
        try:
            if self.cam is not None:
                if self.type_cam == 'acapture':
                    # noinspection PyUnresolvedReferences
                    self.cam.destroy()
                    mt.sleep(2, ack=True, tabs=2)  # acapture need a moment to release
                elif self.type_cam == 'imutils':
                    # noinspection PyUnresolvedReferences
                    self.cam.stop()
                    mt.sleep(2, ack=True, tabs=2)  # imutils need a moment to release
                else:  # type_cam == 'cv2'
                    if self.cam.isOpened():
                        self.cam.release()
                        mt.sleep(2, ack=True, tabs=2)  # just in case
                print('\tCameraWu({}) closed on port {}'.format(self.type_cam, self.port))
        except AttributeError as e:
            mt.exception_error('e {}. can\'t close CameraWu'.format(e), real_exception=True)
        return

    def read_img(self) -> (bool, np.array):
        try:
            frame = None
            if self.type_cam == 'acapture':
                _, frame = self.cam.read()
                if frame is not None:
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            elif self.type_cam == 'imutils':
                frame = self.cam.read()
            else:  # type_cam == 'cv2'
                if self.cam.isOpened():
                    # self.cam.release()
                    # self.cam = cv2.VideoCapture(self.port)
                    _, frame = self.cam.read()
                    # self.cam.set(cv2.CAP_PROP_POS_FRAMES, 0)
            success = False if frame is None else True
        except Exception as e:
            mt.exception_error('CameraWu: failed capture image. e {}'.format(e), real_exception=True)
            success, frame = False, None
        return success, frame


def add_text(
        cv_img: np.array,
        header: str,
        pos: tuple,
        text_color: str = 'white',
        with_rect: bool = True,
        bg_color: str = 'black',
        bg_font_scale: int = 1
):
    """
    :param cv_img:
    :param header:
    :param pos:
    :param text_color: str
    :param with_rect:
    :param bg_color: str
    :param bg_font_scale: int. 1 or 2 - pos changes by scale and font
    :return:
    see add_text_test()
    """
    x, y = pos
    if bg_font_scale == 1:  # big font and scale
        font: int = cv2.FONT_HERSHEY_DUPLEX
        font_scale: float = 1
        font_thickness: int = 1
        text_size, _ = cv2.getTextSize(header, font, font_scale, font_thickness)
        text_w, text_h = text_size
        rect_pt1 = (x, y - 20)
        rect_pt2 = (x + text_w, y + text_h - 20)
    else:
        font: int = cv2.FONT_HERSHEY_DUPLEX
        font_scale: float = 0.5
        font_thickness: int = 1
        text_size, _ = cv2.getTextSize(header, font, font_scale, font_thickness)
        text_w, text_h = text_size
        rect_pt1 = (x, y)
        rect_pt2 = (x + text_w, y + text_h - 20)
    text_color = pyplt.get_BGR_color(text_color)

    # print(pos, (x + text_w, y + text_h))
    if with_rect:
        bg_color = pyplt.get_BGR_color(bg_color)
        cv2.rectangle(cv_img, pt1=rect_pt1, pt2=rect_pt2, color=bg_color, thickness=-1)
    cv2.putText(cv_img, text=header, org=pos, fontFace=font, fontScale=font_scale, color=text_color,
                thickness=font_thickness)
    return


def add_header(
        cv_img: np.array,
        header: str,
        loc: str = pyplt.Location.TOP_LEFT.value,
        text_color: str = 'white',
        with_rect: bool = True,
        bg_color: str = 'black',
        bg_font_scale: int = 1
) -> None:
    """
    :param cv_img: frame
    :param header: some text. e.g. iteration, timestamp ....
    :param loc: supports pyplt.Location.TOP_LEFT.value,  pyplt.Location.BOTTOM_LEFT.value
    :param text_color: as string e.g. 'red'
    :param with_rect: add rect around header
    :param bg_color: background rect color
    :param bg_font_scale: int. 1 or 2 - pos changes by scale and font
    :return:
    see add_header_test()
    """
    if bg_font_scale == 1:
        if loc == pyplt.Location.BOTTOM_LEFT.value:
            pos = (0, cv_img.shape[0])
        else:  # loc == pyplt.Location.TOP_LEFT.value:
            pos = (0, 20)
    else:
        if loc == pyplt.Location.BOTTOM_LEFT.value:
            pos = (0, cv_img.shape[0])
        else:  # loc == pyplt.Location.TOP_LEFT.value:
            pos = (0, 10)

    add_text(cv_img, header, pos=pos, text_color=text_color, with_rect=with_rect, bg_color=bg_color,
             bg_font_scale=bg_font_scale)
    return


class DnnObjectDetectionModels:
    # each MODELS_DNN_META_DATA entry should have this keys:
    MANDATORY_KEYS = [
        'job', 'family', 'in_dims', 'scalefactor', 'mean',
        'swapRB', 'crop', 'default_threshold', 'default_nms_threshold', 'labels_dict',
        'URL'
    ]
    DEFAULT_COLOR_D = {
        'bbox': 'r',
        'label_bbox': 'black',
        'text': 'white',
        'sub_image': 'blue',
    }

    @staticmethod
    def _download_if_needed(local_path: str, url_dict: dict, file_key: str) -> None:
        if not os.path.exists(local_path):
            download_style = url_dict['{}_download_style'.format(file_key)]
            url = url_dict['{}'.format(file_key)]
            if download_style == DownloadStyle.Direct.value:
                st.download_file(url=url, dst_path=local_path)
            elif download_style in [DownloadStyle.Tar.value, DownloadStyle.Zip.value]:
                root_d = os.path.dirname(local_path)
                comp_path = '{}/compressed.{}'.format(root_d, download_style)
                st.download_file(url=url, dst_path=comp_path)  # download compressed
                extracted_folder = '{}/ex'.format(root_d)
                if mt.is_windows():
                    extracted_folder = mt.full_path_no_limit(extracted_folder)
                
                mt.extract_file(src=comp_path, dst_folder=extracted_folder,
                                file_type=download_style)  # extract
                target_file_in_tar = url_dict['{}_name'.format(file_key)]
                # find target file
                target_files = mt.find_files_in_folder(dir_path=extracted_folder, file_suffix=target_file_in_tar)
                if len(target_files) != 1:
                    err_msg = 'not found or found more than 1 target file in downloaded folder: {}'.format(target_files)
                    mt.exception_error(err_msg, real_exception=False)
                    exit(-1)
                mt.move_file(file_src=target_files[0], file_dst=local_path)  # move file

                mt.delete_file(file=comp_path)  # clean up tar\zip
                mt.delete_dir_with_files(dir_path=extracted_folder)  # clean up extracted_folder
        return

    def __init__(self,
                 save_load_dir: str,
                 model_name: str,
                 allowed_class: list = None,
                 tabs: int = 1,
                 threshold: float = None,
                 nms_threshold: float = None,
                 in_dims: tuple = None,
                 scalefactor: float = None,
                 mean: tuple = None,
                 swapRB: bool = None,
                 crop: bool = None,
                 ):
        """
        :param save_load_dir: where the model is saved (or will be if not exists)
        :param model_name: valid name in MODEL_CONF.keys()
        :param tabs:
        :param allowed_class: ignore rest of class. list of strings
            if None - all classes allowed
        for all the following - if is None: take default value from MODELS_DNN_OBJECT_DETECTION_META_DATA['model_name']
        :param threshold: only detection above this threshold will be returned
        :param nms_threshold: non maximum suppression threshold
        :param in_dims:
        :param scalefactor:
        :param mean:
        :param swapRB:
        :param crop:
        see:
        best_model_images_test()
        best_model_video_test()
        best_model_cam_test()
        models_compare_images_test()
        models_compare_video_test()
        models_compare_cam_test()
        """
        if model_name not in MODELS_DNN_OBJECT_DETECTION_META_DATA:
            mt.exception_error(
                'model name must be one of {}'.format(list(MODELS_DNN_OBJECT_DETECTION_META_DATA.keys())),
                real_exception=False, tabs=tabs)
            exit(-1)
        else:  # supported model
            self.model_conf = MODELS_DNN_OBJECT_DETECTION_META_DATA[model_name]
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
            if self.model_conf['job'] != Jobs.OBJECT_DETECTION.value:
                mt.exception_error('this class supports only {}'.format(Jobs.OBJECT_DETECTION.value),
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
        # non maximum suppression threshold
        self.nms_threshold = nms_threshold if nms_threshold is not None else self.model_conf['default_nms_threshold']
        net = None

        # self.time_since_last_detection = -np.inf
        # noinspection PyPackageRequirements
        # import pyttsx3  # pip install pyttsx3  # HANDLE REQ
        # self.speech_engine = pyttsx3.init()
        # self.announcement_timeout_frame = 10  # param
        # self.announcement_frames = self.announcement_timeout_frame  # on first detection say and wait
        if not os.path.exists(save_load_dir):
            mt.create_dir(save_load_dir)

        print('{}Loading {}({} classes)'.format(tabs_s, self.name, len(self.labels)))
        if self.model_conf['family'] == DnnFamily.Caffe.value:
            model_prototxt = "{}/{}.prototxt".format(self.local_path, self.name)
            model_caffe = "{}/{}.caffemodel".format(self.local_path, self.name)
            self._download_if_needed(local_path=model_prototxt, url_dict=self.model_conf['URL'], file_key='prototxt')
            self._download_if_needed(local_path=model_caffe, url_dict=self.model_conf['URL'], file_key='caffemodel')
            print('{}\tprototxt({}): {}'.format(tabs_s, mt.file_or_folder_size(model_prototxt), model_prototxt))
            print('{}\tcaffemodel({}): {}'.format(tabs_s, mt.file_or_folder_size(model_caffe), model_caffe))
            net = cv2.dnn.readNetFromCaffe(prototxt=model_prototxt, caffeModel=model_caffe)

        elif self.model_conf['family'] == DnnFamily.Darknet.value:
            model_cfg = "{}/{}.cfg".format(self.local_path, self.name)
            model_weights = "{}/{}.weights".format(self.local_path, self.name)
            self._download_if_needed(local_path=model_cfg, url_dict=self.model_conf['URL'], file_key='cfg')
            self._download_if_needed(local_path=model_weights, url_dict=self.model_conf['URL'], file_key='weights')
            print('{}\tcfg({}): {}'.format(tabs_s, mt.file_or_folder_size(model_cfg), model_cfg))
            print('{}\tweights({}): {}'.format(tabs_s, mt.file_or_folder_size(model_weights), model_weights))
            net = cv2.dnn.readNetFromDarknet(cfgFile=model_cfg, darknetModel=model_weights)

        elif self.model_conf['family'] == DnnFamily.TF.value:
            model_pbtxt = "{}/{}.pbtxt".format(self.local_path, self.name)
            model_pb = "{}/{}.pb".format(self.local_path, self.name)
            self._download_if_needed(local_path=model_pbtxt, url_dict=self.model_conf['URL'], file_key='pbtxt')
            self._download_if_needed(local_path=model_pb, url_dict=self.model_conf['URL'], file_key='pb')
            print('{}\tpbtxt({}): {}'.format(tabs_s, mt.file_or_folder_size(model_pbtxt), model_pbtxt))
            print('{}\tpb({}): {}'.format(tabs_s, mt.file_or_folder_size(model_pb), model_pb))
            net = cv2.dnn.readNetFromTensorflow(model=model_pb, config=model_pbtxt)
        # elif self.model_conf['family'] == Family.ONNX.value:
        #     model_onnx = "{}/{}.onnx".format(self.local_path, self.name)
        #     print('{}\tpb({}): {}'.format(tabs_s, wu.file_or_folder_size(model_onnx), model_onnx))
        #     net = cv2.dnn.readNetFromONNX(onnxFile=model_onnx)

        if net is None:
            mt.exception_error('Failed to create network', real_exception=False)
            exit(-1)

        self.model = cv2.dnn_DetectionModel(net)
        if in_dims is not None:
            self.model_conf['in_dims'] = in_dims
        if scalefactor is not None:
            self.model_conf['scalefactor'] = scalefactor
        if mean is not None:
            self.model_conf['mean'] = mean
        if swapRB is not None:
            self.model_conf['swapRB'] = swapRB
        if crop is not None:
            self.model_conf['crop'] = crop

        # self.model.setInputParams(size=(416, 416), scale=1 / 255, swapRB=True)
        self.model.setInputParams(
            scale=self.model_conf['scalefactor'],
            size=self.model_conf['in_dims'],
            mean=self.model_conf['mean'],
            swapRB=self.model_conf['swapRB'],
            crop=self.model_conf['crop']
        )

        # TODO test GPU with cuda 11 installed
        # count = cv2.cuda.getCudaEnabledDeviceCount()
        # print(count)
        # self.network.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
        # self.network.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
        return

    def __str__(self):
        string = '{}{}'.format(self.tabs * '\t', mt.add_color(string='DnnObjectDetectionModels:', ops='underlined'))
        string += '\n\t{}name={}'.format(self.tabs * '\t', self.name)
        string += '\n\t{}local_path={}'.format(self.tabs * '\t', self.local_path)
        string += '\n\t{}threshold={}'.format(self.tabs * '\t', self.threshold)
        string += '\n\t{}nms_threshold={}'.format(self.tabs * '\t', self.nms_threshold)
        string += '\n\t{}{}'.format(self.tabs * '\t', mt.to_str(self.allowed_class, 'allowed_class'))
        string += '\n\t{}tabs={}'.format(self.tabs * '\t', self.tabs)
        string += '\n{}'.format(mt.dict_as_table(self.model_conf, title='conf', fp=6, ack=False, tabs=self.tabs + 1))
        return string

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
        classes, scores, boxes = self.model.detect(cv_img, self.threshold, self.nms_threshold)
        # print('{}\t{}'.format(tabs * '\t', mt.to_str(classes, 'classes')))
        # print('{}\t{}'.format(tabs * '\t', mt.to_str(scores, 'scores')))
        # print('{}\t{}'.format(tabs * '\t', mt.to_str(boxes, 'boxes')))
        if len(classes) > 0 and len(scores) > 0:
            classes = classes.flatten()
            scores = scores.flatten()

        detections = self.extract_results(
            classes=classes,
            scores=scores,
            boxes=boxes,
            cv_img=cv_img,
            fp=fp,
            ack=ack,
            tabs=tabs,
            img_title=img_title
        )

        return detections

    def extract_results(
            self,
            classes: np.array,
            scores: np.array,
            boxes: np.array,
            cv_img: np.array,
            fp: int = 2,
            ack: bool = False,
            tabs: int = 1,
            img_title: str = None
    ) -> list:
        """
        :param classes: result of classes, scores, boxes = self.model.detect(cv_img, self.threshold, self.nms_threshold)
        :param scores: result of classes, scores, boxes = self.model.detect(cv_img, self.threshold, self.nms_threshold)
        :param boxes: result of classes, scores, boxes = self.model.detect(cv_img, self.threshold, self.nms_threshold)
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

        if ack:
            title_suffix = '' if img_title is None else '{} '.format(img_title)
            title = '{} detections({}) on image {}{}:'.format(self.name, len(classes), title_suffix, cv_img.shape)

            print('{}{}'.format(tabs * '\t', title))
            print('{}Meta_data:'.format(tabs * '\t'))
            print('{}\t{}'.format(tabs * '\t', mt.to_str(classes, 'classes')))
            print('{}\t{}'.format(tabs * '\t', mt.to_str(scores, 'scores')))
            print('{}\t{}'.format(tabs * '\t', mt.to_str(boxes, 'boxes')))
            print('{}Detections:'.format(tabs * '\t'))

        img_h, img_w = cv_img.shape[0], cv_img.shape[1]
        detections = []
        for i, (class_id, score_frac, bbox) in enumerate(zip(classes, scores, boxes)):
            label = self.labels[class_id]
            if label in self.allowed_class:
                score_percentage = round(score_frac * 100, fp)

                (x0, y0) = (bbox[0], bbox[1])
                (w, h) = (bbox[2], bbox[3])

                x1 = min(x0 + w, img_w)  # dont exceed frame width
                y1 = min(y0 + h, img_h)  # dont exceed frame height

                if 'need_normalize' in self.model_conf:
                    in_dims_w, in_dims_h = self.model_conf['in_dims']
                    x0 = int(x0 * (img_w / in_dims_w))
                    x1 = int(x1 * (img_w / in_dims_w))
                    y0 = int(y0 * (img_h / in_dims_h))
                    y1 = int(y1 * (img_h / in_dims_h))

                detection_d = {
                    'label': label,
                    'score_percentage': score_percentage,
                    'bbox': {
                        #  pt1 = (x0, y0)  # obj frame top left corner
                        #  pt2 = (x1, y1)  # obj frame bottom right corner
                        'x0': int(x0),
                        'y0': int(y0),
                        'x1': int(x1),
                        'y1': int(y1),
                    },
                }

                detections.append(detection_d)
                if ack:
                    d_msg = '{}\t{})Detected {}({}%) in top left=({}), bottom right=({})'
                    print(d_msg.format(tabs * '\t', i, label, score_percentage, (x0, y0), (x1, y1)))

        return detections

    @staticmethod
    def add_traffic_light_to_detections(detections: list, traffic_light_p: dict) -> list:
        """
        :param detections: detections from classify_cv_img()
        :param traffic_light_p: dict of loc to float percentage
            if not none get 3 2d points in a traffic_light form
            e.g. traffic_light={
                    # x of all traffic_light points is frame_width / 2
                    'up': 0.2,  # red light will be take from y = frame_height * 0.2
                    'mid': 0.3,  # yellow light will be take from y = frame_height * 0.3
                    'down': 0.4  # green light will be take from y = frame_height * 0.3
                }
        :return: for each detection in detections: add entry 'traffic_light' with a dict with keys up, mid, down
                    each has location to dict of point and color:
            e.g.
                'traffic_light'= { # x_mid = frame_width / 2
                'up': {'point': [x_mid, y_up], 'color': 'red'},  # y_up = frame_height * traffic_light['up']
                'mid': {'point': [x_mid, y_mid], 'color': 'yellow'},
                'down': {'point': [x_mid, y_down], 'color': 'green'}
                }
        """
        for detection_d in detections:
            # label = detection_d['label']
            # score = detection_d['score_percentage']
            x0 = detection_d['bbox']['x0']
            y0 = detection_d['bbox']['y0']
            x1 = detection_d['bbox']['x1']
            y1 = detection_d['bbox']['y1']
            y_dist = y0 - y1  # image is flipped on y axis
            x_dist = x1 - x0
            # prepare 'traffic_light' points
            # on x middle
            # on y 20% 30% 40% from the top
            x_mid = int(x0 + 0.5 * x_dist)
            y_up = int(y0 - traffic_light_p['up'] * y_dist)
            y_mid = int(y0 - traffic_light_p['mid'] * y_dist)
            y_down = int(y0 - traffic_light_p['down'] * y_dist)
            traffic_light_out = {
                'up': {'point': [x_mid, y_up], 'color': 'red'},
                'mid': {'point': [x_mid, y_mid], 'color': 'yellow'},
                'down': {'point': [x_mid, y_down], 'color': 'green'}
            }
            detection_d['traffic_light'] = traffic_light_out
        return detections

    @staticmethod
    def add_sub_sub_image_to_detection(detections: list, cv_img: np.array, bbox_image_p: dict) -> list:
        """
        :param detections:
        :param cv_img:
        :param bbox_image_p: dict that specify how much from the bbox to save
                bbox_image_p={  # all bbox
                    'x_start': 0,
                    'x_end': 1,
                    'y_start': 0,
                    'y_end': 1,
                },
                bbox_image_p={  # sub bbox
                    'x_start': 0.5,  # start from middle
                    'x_end': 0.9,     # go to the right until 90% of the width
                    'y_start': 0,  # 0 start from the bottom
                    'y_end': 0.4,  # end at 40% from bottom
                },
        :return: for each detection in detections: add entry 'bbox_sub_image' with a dict with keys image,x0,x1,y0,y1
                    if you imshow - you will get the bbox of the detection (according to bbox_image_p)
        """
        for detection_d in detections:
            # label = detection_d['label']
            # confidence = detection_d['score_percentage']
            x0 = detection_d['bbox']['x0']
            y0 = detection_d['bbox']['y0']
            x1 = detection_d['bbox']['x1']
            y1 = detection_d['bbox']['y1']
            y_dist = y0 - y1  # image is flipped on y axis
            x_dist = x1 - x0
            # prepare sub sub image (a part of the bbox)
            # y1 is the bottom
            sub_y0 = int(y1 + bbox_image_p['y_start'] * y_dist)
            sub_y1 = int(y1 + bbox_image_p['y_end'] * y_dist)
            sub_x0 = int(x0 + bbox_image_p['x_start'] * x_dist)
            sub_x1 = int(x0 + bbox_image_p['x_end'] * x_dist)
            detection_d['bbox_sub_image'] = {
                'image': cv_img[sub_y0:sub_y1, sub_x0:sub_x1].tolist(),
                'x0': sub_x0,
                'y0': sub_y0,
                'x1': sub_x1,
                'y1': sub_y1,
            }
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
        :param detections: output of self.classify_cv_img()
        :param colors_d: colors in str form:
            bbox color
            label_bbox color
            text color
            if class_id_bbox exist - color the bbox of that class in the given color
                e.g. colors_d={
                        'bbox': 'r',
                        'label_bbox': 'black',
                        'text': 'white',
                        'person_bbox': 'lightgreen',
                    },
        :param cv_img: the same that was given input to self.classify_cv_img()
        :param draw_labels: draw label(label_bbox and text on it) on the bbox
        :param ack: if True print the results
        :param tabs: if ack True
        :param img_title: if ack True
        :return:
        """
        if ack:
            title_suffix = '' if img_title is None else '{} '.format(img_title)
            title = 'detections({}) on image {}{}:'.format(len(detections), title_suffix, cv_img.shape)
            print('{}{}'.format(tabs * '\t', title))
        for detection in detections:
            if ack:
                print('{}\t{}'.format(tabs * '\t', mt.to_str(detection, 'detection', chars=300, wm=False)))
            label = detection['label']
            score_percentage = detection['score_percentage']
            x0 = detection['bbox']['x0']
            y0 = detection['bbox']['y0']
            x1 = detection['bbox']['x1']
            y1 = detection['bbox']['y1']
            traffic_light_d = detection['traffic_light'] if 'traffic_light' in detection else {}
            bbox_sub_image_d = detection['bbox_sub_image'] if 'bbox_sub_image' in detection else None

            # check custom color for this class
            k = '{}_bbox'.format(label)
            color_bgr = pyplt.get_BGR_color(colors_d[k]) if k in colors_d else pyplt.get_BGR_color(
                colors_d['bbox'])
            cv2.rectangle(img=cv_img, pt1=(x0, y0), pt2=(x1, y1), color=color_bgr, thickness=2)

            for loc, point_and_color in traffic_light_d.items():
                cv2.circle(cv_img, center=tuple(point_and_color['point']), radius=2,
                           color=pyplt.get_BGR_color(point_and_color['color']), thickness=-1)

            if bbox_sub_image_d is not None:
                pt1 = (bbox_sub_image_d['x0'], bbox_sub_image_d['y0'])
                pt2 = (bbox_sub_image_d['x1'], bbox_sub_image_d['y1'])
                cv2.rectangle(img=cv_img, pt1=pt1, pt2=pt2, color=pyplt.get_BGR_color(colors_d['sub_image']),
                              thickness=1)  # sub image

            if draw_labels:
                label_conf = '{}({}%)'.format(label, score_percentage)
                add_text(cv_img, header=label_conf, pos=(x0, y1), text_color=colors_d['text'], with_rect=True,
                         bg_color=colors_d['label_bbox'], bg_font_scale=2)

        return


def get_dims_from_cap(cap: cv2.VideoCapture) -> tuple:
    """
    :param cap:
    frames size as (int, int)
    :return:
    see Mp4_creator_test()
    """
    out_dims = None
    if cap.isOpened():
        orig_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # float `width`
        orig_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # float `height`
        out_dims = (orig_width, orig_height)
    return out_dims


def get_frames_from_cap(cap: cv2.VideoCapture) -> int:
    """
    :param cap:
    :return:
    see Mp4_creator_test()
    """
    video_total_frames = None
    if cap.isOpened():
        video_total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    return video_total_frames


class Mp4_creator:
    def __init__(self, out_full_path: str, out_fps: float, out_dims: tuple, tabs: int = 1):
        """
        :param out_full_path:
        :param out_fps:
        :param out_dims:
        :param tabs:
        see Mp4_creator_test()
        """
        # fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        fourcc = cv2.VideoWriter_fourcc(c1='m', c2='p', c3='4', c4='v')

        self.out_full_path = out_full_path
        self.out_fps = out_fps
        self.out_dims = out_dims
        self.tabs = tabs
        self.frames_count = 0
        if not os.path.exists(os.path.dirname(out_full_path)):
            mt.exception_error('Cant create cv2.VideoWriter', real_exception=False, tabs=self.tabs)
            mt.exception_error(mt.NOT_FOUND.format(os.path.dirname(out_full_path)), real_exception=False,
                               tabs=self.tabs)
            self.result = None
        else:
            self.result = cv2.VideoWriter(
                filename=out_full_path,
                fourcc=fourcc,
                fps=out_fps,
                frameSize=out_dims
            )
        return

    def __del__(self):
        if self.result is not None:
            self.result.release()
            self.result = None
        return

    def __str__(self):
        string = '{}Mp4_creator\n'.format(self.tabs * '\t')
        string += '{}\ttarget file path: {}\n'.format(self.tabs * '\t', self.out_full_path)
        string += '{}\tfps: {}\n'.format(self.tabs * '\t', self.out_fps)
        string += '{}\tout_dims: {}'.format(self.tabs * '\t', self.out_dims)
        return string

    def add_frame(self, frame: np.array, ack: bool = False, tabs: int = 1) -> None:
        if self.result is not None:
            cur_out_dims = (frame.shape[1], frame.shape[0])
            if cur_out_dims == self.out_dims:
                self.result.write(frame)
                self.frames_count += 1
                if ack:
                    print('{}frame {} added'.format(tabs * '\t', self.frames_count))
            else:
                mt.exception_error(
                    'Shapes mismatch: Frame.shape={}, Video shape={}'.format(cur_out_dims, self.out_dims),
                    real_exception=False, tabs=tabs)
        else:
            mt.exception_error('Cant write frame', real_exception=False, tabs=self.tabs)
        return

    def finalize(self):
        if self.result is not None:
            self.result.release()
            self.result = None
            print('{}File ready({} frames): {}'.format(self.tabs * '\t', self.frames_count, self.out_full_path))
        return


def get_all_object_detection_models_info(ack: bool = False) -> list:
    model_names = []
    for i, (m_name, m_dict) in enumerate(MODELS_DNN_OBJECT_DETECTION_META_DATA.items()):
        if ack:
            mt.dict_as_table(table=m_dict['info'], title='{}: {}'.format(i + 1, m_name), tabs=0)
        model_names.append(m_name)
    return model_names
