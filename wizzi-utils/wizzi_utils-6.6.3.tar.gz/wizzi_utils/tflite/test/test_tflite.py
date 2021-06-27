from wizzi_utils.tflite import tflite_tools as tflt
from wizzi_utils.misc import misc_tools as mt
from wizzi_utils.misc.test import test_misc_tools as mtt
from wizzi_utils.open_cv import open_cv_tools as cvt
from wizzi_utils.open_cv.test import test_open_cv_tools as cvtt
import os
# noinspection PyPackageRequirements
import cv2

SAVE_SCOPE = 'TFL'
BEST_MODEL = 'ssd_mobilenet_v2_mnasfpn'


def get_tflite_version_test():
    mt.get_function_name(ack=True, tabs=0)
    tflt.get_tflite_version(ack=True)
    return


def fps_models_test():
    iterations = 10
    images_names = [mtt.DOGS1] * iterations
    cv_imgs_orig = [cvtt.load_img_from_web(image_name) for image_name in images_names]
    print(images_names)
    models_compare_images_test(
        cv_imgs_orig=cv_imgs_orig,
        images_names=images_names,
        models_selection=cvtt.ALL_MODELS,
        ms=1
    )
    return


def __get_models(models_selection: str = cvtt.BEST_MODELS):
    if models_selection == cvtt.BEST_MODELS:
        # preparing 4 best models
        grid = (2, 2)
        display_im_size = (640, 480)
        models_names = [
            'ssd_mobilenet_v3_small_coco_2020_01_14',
            'ssd_mobilenet_v2_mnasfpn',
            'ssd_mobilenet_v3_large_coco_2020_01_14',
            'ssdlite_mobiledet_cpu_320x320_coco_2020_05_19',
            # 'ssd_mobilenet_v1_1_metadata_1',
            # 'ssdlite_mobilenet_v2_coco_300_integer_quant_with_postprocess',
            # 'coco_ssd_mobilenet_v1_1_0_quant_2018_06_29'
        ]
    elif models_selection == cvtt.ALL_MODELS:
        # preparing all(7) models
        grid = (2, 4)
        display_im_size = (320, 240)
        models_names = tflt.get_all_object_detection_models_info(ack=False)
    else:
        # preparing 1 models - default is BEST_MODEL
        grid = (1, 1)
        display_im_size = (640, 480)
        models_names = [models_selection]
    models = []
    for m_name in models_names:
        save_dir = '{}/{}/{}'.format(mtt.TFL_MODELS, tflt.MODELS_TFL_META_DATA[BEST_MODEL]['job'], m_name)
        m = tflt.TfltObjectDetectionModels(
            save_load_dir=save_dir,
            model_name=m_name,
            # allowed_class=['dog', 'cat'],
            allowed_class=None,
            tabs=1,
            # threshold=0.2,  # take default
            # nms={'score_threshold': 0.4, 'nms_threshold': 0.4},  # take default
        )
        print(m)
        models.append(m)
    return models, grid, display_im_size


def best_model_images_test(m_name: str = BEST_MODEL, ms: int = cvtt.BLOCK_MS_NORMAL):
    mt.get_function_name(ack=True, tabs=0)
    models_compare_images_test(
        models_selection=m_name,
        ms=ms
    )
    return


def models_compare_images_test(
        cv_imgs_orig: list = None,
        images_names: list = None,
        models_selection: str = cvtt.BEST_MODELS,
        ms: int = cvtt.BLOCK_MS_NORMAL
):
    mt.get_function_name(ack=True, tabs=0)
    models, grid, im_size = __get_models(models_selection)

    if cv_imgs_orig is None:
        images_names = [mtt.DOG, mtt.DOGS1, mtt.PERSON]
        cv_imgs_orig = [cvtt.load_img_from_web(image_name) for image_name in images_names]
    else:
        if images_names is None:
            images_names = []
            for i in range(len(cv_imgs_orig)):
                images_names.append('unknown{}'.format(i))
        if len(images_names) != len(cv_imgs_orig):
            mt.exception_error('lists length differ {}, {}'.format(len(images_names), len(cv_imgs_orig)),
                               real_exception=False)
            return

    save_dir = '{}/{}/{}/{}'.format(mtt.IMAGES_OUTPUTS, mt.get_function_name(), SAVE_SCOPE, models_selection)
    mt.create_dir(save_dir)
    cvtt.__models_images_test(
        models=models,
        images_names=images_names,
        cv_imgs_orig=cv_imgs_orig,
        grid=grid,
        delay_ms=ms,
        save_dir=save_dir,
        display_im_size=im_size
    )
    return


def best_model_video_test(
        m_name: str = BEST_MODEL,
        video_path: str = None,
        video_name: str = 'unknown',
        work: int = 80
):
    mt.get_function_name(ack=True, tabs=0)
    models_compare_video_test(
        video_path=video_path,
        video_name=video_name,
        models_selection=m_name,
        work=work
    )
    return


def models_compare_video_test(
        video_path: str = None,
        video_name: str = 'unknown',
        work: int = 80,
        models_selection: str = cvtt.BEST_MODELS
):
    mt.get_function_name(ack=True, tabs=0)
    models, grid, im_size = __get_models(models_selection)

    if video_path is None:  # default video
        video_name = mtt.DOG1
        video_path = cvtt.get_vid_from_web(name=video_name)

    if not os.path.exists(video_path):
        mt.exception_error(mt.NOT_FOUND.format(video_path), real_exception=False)
        return
    cap = cv2.VideoCapture(video_path)
    if cap.isOpened():
        video_total_frames = cvt.get_frames_from_cap(cap)
        print('\tvid {} has {} frames'.format(video_name, video_total_frames))
        save_dir = '{}/{}/{}/{}'.format(mtt.VIDEOS_OUTPUTS, mt.get_function_name(), SAVE_SCOPE, models_selection)
        mt.create_dir(save_dir)
        cvtt.__models_cap_test(
            models=models,
            cap=cap,
            total_frames=video_total_frames,
            work_every_x_frames=work,
            grid=grid,
            delay_ms=1,
            save_dir=save_dir,
            display_im_size=im_size,
            cap_desc=video_name
        )
    else:
        mt.exception_error('cap is closed.', real_exception=False)
    return


def best_model_cam_test(
        m_name: str = BEST_MODEL,
        total_frames: int = cvtt.MODEL_FRAMES_CAM
):
    mt.get_function_name(ack=True, tabs=0)
    models_compare_cam_test(
        models_selection=m_name,
        total_frames=total_frames
    )
    return


def models_compare_cam_test(
        models_selection: str = cvtt.BEST_MODELS,
        total_frames: int = cvtt.MODEL_FRAMES_CAM
):
    mt.get_function_name(ack=True, tabs=0)
    models, grid, im_size = __get_models(models_selection)

    cam = cvt.CameraWu.open_camera(port=0, type_cam='cv2')
    if cam is not None:
        save_dir = '{}/{}/{}/{}'.format(mtt.VIDEOS_OUTPUTS, mt.get_function_name(), SAVE_SCOPE, models_selection)
        mt.create_dir(save_dir)
        cvtt.__models_cap_test(
            models=models,
            cap=cam,
            total_frames=total_frames,
            work_every_x_frames=1,
            grid=grid,
            delay_ms=1,
            save_dir=save_dir,
            display_im_size=im_size,
            cap_desc='cam 0'
        )
    else:
        mt.exception_error('cap is closed.', real_exception=False)
    return


def test_all():
    print('{}{}:'.format('-' * 5, mt.get_base_file_and_function_name()))
    get_tflite_version_test()
    best_model_images_test()
    best_model_video_test()
    best_model_cam_test()
    models_compare_images_test()
    models_compare_video_test()
    models_compare_cam_test()
    print('{}'.format('-' * 20))
    return
