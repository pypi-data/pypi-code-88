from wizzi_utils.misc import misc_tools as mt
from wizzi_utils.misc.test import test_misc_tools as mtt
from wizzi_utils.open_cv import open_cv_tools as cvt
from wizzi_utils.socket import socket_tools as st
from wizzi_utils.pyplot import pyplot_tools as pyplt
import numpy as np
import os
# noinspection PyPackageRequirements
import cv2

LOOP_TESTS = 50
BLOCK_MS_NORMAL = 2000  # 0 to block
ITERS_CAM_TEST = 10  # 0 to block
MODEL_FRAMES_CAM = 3
SAVE_SCOPE = 'CVT'
OD_BEST_MODEL = 'yolov4'
# POSE_BEST_MODEL = 'openpose_pose_coco'
# POSE_BEST_MODEL = 'openpose_pose_mpi'
# POSE_BEST_MODEL = 'hand_pose'
POSE_BEST_MODEL = 'body25'
BEST_MODELS = 'best_models'
ALL_MODELS = 'all_models'


def load_img_from_web(name: str) -> np.array:
    f = mtt.IMAGES_INPUTS
    url = mtt.IMAGES_D[name]
    suffix = 'jpg'  # default
    # if '.webm' in url:
    #     suffix = 'webm'
    dst = '{}/{}.{}'.format(f, name, suffix)

    if not os.path.exists(dst):
        if not os.path.exists(f):
            mt.create_dir(f)
        success = st.download_file(url, dst)
        if not success:
            mt.exception_error('download failed - creating random img', real_exception=False)
            img = mt.np_random_integers(size=(240, 320, 3), low=0, high=255)
            img = img.astype('uint8')
            cvt.save_img(dst, img)

    img = cvt.load_img(path=dst)
    return img


def get_vid_from_web(name: str) -> str:
    f = mtt.VIDEOS_INPUTS
    url = mtt.VIDEOS_D[name]
    suffix = 'mp4'  # default
    if '.webm' in url:
        suffix = 'webm'
    dst = '{}/{}.{}'.format(f, name, suffix)

    if not os.path.exists(dst):
        if not os.path.exists(f):
            mt.create_dir(f)
        success = st.download_file(url, dst)
        if not success:
            mt.exception_error('download failed - creating random img', real_exception=False)
            dst = None

    return dst


def get_cv_version_test():
    mt.get_function_name(ack=True, tabs=0)
    cvt.get_cv_version(ack=True, tabs=1)
    return


def imread_imwrite_test():
    mt.get_function_name(ack=True, tabs=0)
    name = mtt.SO_LOGO
    img = load_img_from_web(name)

    f = mtt.IMAGES_INPUTS
    url = mtt.IMAGES_D[name]
    dst_path = '{}/{}'.format(f, os.path.basename(url).replace('.png', '_copy.png'))

    cvt.save_img(dst_path, img, ack=True)
    img_loaded = cvt.load_img(dst_path, ack=True)
    print(mt.to_str(img_loaded, '\timg_copy'))
    mt.delete_file(dst_path, ack=True)
    # mt.delete_file(file=mtt.SO_LOGO_PATH, ack=True)
    return


def list_to_cv_image_test():
    mt.get_function_name(ack=True, tabs=0)
    img = load_img_from_web(mtt.SO_LOGO)
    img_list = img.tolist()
    print(mt.to_str(img_list, '\timg_list'))
    img = cvt.list_to_cv_image(img_list)
    print(mt.to_str(img, '\timg'))
    # mt.delete_file(file=mtt.TEMP_IMAGE_PATH, ack=True)
    return


def display_open_cv_image_test():
    mt.get_function_name(ack=True, tabs=0)
    img = load_img_from_web(mtt.SO_LOGO)
    print('\tVisual test: stack overflow logo')
    loc = (70, 200)  # move to X,Y
    resize = 1.7  # enlarge to 170%
    cvt.display_open_cv_image(
        img=img,
        ms=1,  # not blocking
        title='stack overflow logo moved to {} and re-sized to {}'.format(loc, resize),
        loc=loc,  # start from x =70 y = 0
        resize=resize
    )
    loc = pyplt.Location.TOP_RIGHT.value  # move to top right corner
    resize = 1.7  # enlarge to 170%
    cvt.display_open_cv_image(
        img=img,
        ms=BLOCK_MS_NORMAL,  # blocking
        title='stack overflow logo moved to {} and re-sized to {}'.format(loc, resize),
        loc=loc,  # start from x =70 y = 0
        resize=resize
    )
    cv2.destroyAllWindows()
    # mt.delete_file(file=mtt.SO_LOGO_PATH, ack=True)
    return


def display_open_cv_image_loop_test():
    mt.get_function_name(ack=True, tabs=0)
    img = load_img_from_web(mtt.SO_LOGO)
    loc = (70, 200)  # move to X,Y
    resize = 1.7  # enlarge to 170%
    title = 'stack overflow logo moved to {} and re-sized to {} - {} iterations'.format(loc, resize, LOOP_TESTS)
    print('\tVisual test: {}'.format(title))
    for i in range(LOOP_TESTS):
        cvt.display_open_cv_image(
            img=img,
            ms=1,  # not blocking
            title=title,
            loc=loc,  # start from x =70 y = 0
            resize=resize
        )
        if i == 0:  # move just first iter
            loc = None
    cv2.destroyAllWindows()
    # mt.delete_file(file=mtt.SO_LOGO_PATH, ack=True)
    return


def resize_opencv_image_test():
    mt.get_function_name(ack=True, tabs=0)
    img = load_img_from_web(mtt.SO_LOGO)
    print(mt.to_str(img, '\timg'))
    img = cvt.resize_opencv_image(img, scale_percent=0.6)
    print(mt.to_str(img, '\timg re-sized to 60%'))
    # mt.delete_file(file=mtt.SO_LOGO_PATH, ack=True)
    return


def move_cv_img_x_y_test():
    mt.get_function_name(ack=True, tabs=0)
    img = load_img_from_web(mtt.SO_LOGO)
    options = [(0, 0), (100, 0), (0, 100), (150, 150), (400, 400), (250, 350)]
    print('\tVisual test: move to all options {}'.format(options))
    print('\t\tClick Esc to close all')
    for x_y in options:
        title = 'move to ({})'.format(x_y)
        cv2.imshow(title, img)
        cvt.move_cv_img_x_y(title, x_y)
    cv2.waitKey(BLOCK_MS_NORMAL)
    cv2.destroyAllWindows()
    # mt.delete_file(file=mtt.SO_LOGO_PATH, ack=True)
    return


def move_cv_img_by_str_test():
    mt.get_function_name(ack=True, tabs=0)
    img = load_img_from_web(mtt.SO_LOGO)
    options = pyplt.Location.get_location_list_by_rows()
    print('\tVisual test: move to all options {}'.format(options))
    print('\t\tClick Esc to close all')
    for where_to in options:
        title = 'move to {}'.format(where_to)
        cv2.imshow(title, img)
        cvt.move_cv_img_by_str(img, title, where=where_to)
    cv2.waitKey(BLOCK_MS_NORMAL)
    cv2.destroyAllWindows()
    # mt.delete_file(file=mtt.SO_LOGO_PATH, ack=True)
    return


def unpack_list_imgs_to_big_image_test():
    mt.get_function_name(ack=True, tabs=0)
    img = load_img_from_web(mtt.SO_LOGO)
    gray = cvt.BGR_img_to_gray(img)
    big_img = cvt.unpack_list_imgs_to_big_image(
        imgs=[img, gray, img],
        resize=None,
        grid=(2, 2)
    )
    title = 'stack overflow logo 2x2(1 empty)'
    print('\tVisual test: {}'.format(title))
    cvt.display_open_cv_image(
        img=big_img,
        ms=BLOCK_MS_NORMAL,  # blocking
        title=title,
        loc=(0, 0),
        resize=None
    )
    cv2.destroyAllWindows()
    # mt.delete_file(file=mtt.SO_LOGO_PATH, ack=True)
    return


def display_open_cv_images_test():
    mt.get_function_name(ack=True, tabs=0)
    img = load_img_from_web(mtt.SO_LOGO)
    title = '2x1 grid'
    print('\tVisual test: {}'.format(title))
    loc1 = (0, 0)
    cvt.display_open_cv_images(
        imgs=[img, img],
        ms=1,  # blocking
        title='{} loc={}'.format(title, loc1),
        loc=loc1,
        resize=None,
        grid=(2, 1),
        header='{} loc={}'.format(title, loc1),
    )
    loc2 = pyplt.Location.BOTTOM_CENTER.value
    cvt.display_open_cv_images(
        imgs=[img, img],
        ms=BLOCK_MS_NORMAL,  # blocking
        title='{} loc={}'.format(title, loc2),
        loc=loc2,
        resize=None,
        grid=(2, 1),
        header='{} loc={}'.format(title, loc1),
    )
    cv2.destroyAllWindows()
    # mt.delete_file(file=mtt.SO_LOGO_PATH, ack=True)
    return


def display_open_cv_images_loop_test():
    mt.get_function_name(ack=True, tabs=0)
    img = load_img_from_web(mtt.SO_LOGO)
    loc = (70, 200)  # move to X,Y
    title = 'stack overflow logo moved to {} - {} iterations'.format(loc, LOOP_TESTS)
    print('\tVisual test: {}'.format(title))
    for i in range(LOOP_TESTS):
        cvt.display_open_cv_images(
            imgs=[img, img],
            ms=1,  # blocking
            title=title,
            loc=loc,
            resize=None,
            grid=(2, 1),
            header=None
        )
        if i == 0:  # move just first iter
            loc = None
    cv2.destroyAllWindows()
    # mt.delete_file(file=mtt.SO_LOGO_PATH, ack=True)
    return


def gray_to_BGR_and_back_test():
    mt.get_function_name(ack=True, tabs=0)
    img = load_img_from_web(mtt.SO_LOGO)
    print(mt.to_str(img, '\timgRGB'))
    gray = cvt.BGR_img_to_gray(img)
    print(mt.to_str(img, '\timg_gray'))
    img = cvt.gray_scale_img_to_BGR_form(gray)
    print(mt.to_str(img, '\timgRGB'))
    # mt.delete_file(file=mtt.SO_LOGO_PATH, ack=True)
    return


def BGR_img_to_RGB_and_back_test():
    mt.get_function_name(ack=True, tabs=0)
    imgBGR1 = load_img_from_web(mtt.SO_LOGO)
    print(mt.to_str(imgBGR1, '\timgBGR'))
    imgRGB = cvt.BGR_img_to_RGB(imgBGR1)
    print(mt.to_str(imgRGB, '\timgRGB'))
    imgBGR2 = cvt.RGB_img_to_BGR(imgRGB)
    print(mt.to_str(imgBGR2, '\timgBGR2'))

    cvt.display_open_cv_images(
        imgs=[imgBGR1, imgRGB, imgBGR2],
        ms=BLOCK_MS_NORMAL,  # blocking
        title='imgBGR1, imgRGB, imgBGR2',
        loc=pyplt.Location.CENTER_CENTER,
        resize=None,
        grid=(3, 1),
        header='compare'
    )
    cv2.destroyAllWindows()
    # mt.delete_file(file=mtt.SO_LOGO_PATH, ack=True)
    return


def CameraWu_test(type_cam: str):
    WITH_SLEEP = False
    ports = [0, 1, 13]
    cams = []
    for port in ports:
        cam = cvt.CameraWu.open_camera(port=port, type_cam=type_cam)
        if cam is not None:
            cams.append(cam)

    for cam in cams:
        title = 'CameraWu_test({}) on port {}'.format(cam.type_cam, cam.port)
        fps = mt.FPS(summary_title=title)
        for i in range(ITERS_CAM_TEST):
            fps.start()
            success, cv_img = cam.read_img()
            if WITH_SLEEP:
                mt.sleep(1)

            if success:
                cvt.display_open_cv_image(
                    img=cv_img,
                    ms=1,
                    title=title,
                    loc=pyplt.Location.CENTER_CENTER,
                    resize=None,
                    header='{}/{}'.format(i + 1, ITERS_CAM_TEST)
                )
            fps.update()
        fps.finalize()
    cv2.destroyAllWindows()
    return


def CameraWu_cv2_test():
    mt.get_function_name(ack=True, tabs=0)
    CameraWu_test(type_cam='cv2')
    return


def CameraWu_acapture_test():
    mt.get_function_name(ack=True, tabs=0)
    CameraWu_test(type_cam='acapture')
    return


def CameraWu_imutils_test():
    mt.get_function_name(ack=True, tabs=0)
    CameraWu_test(type_cam='imutils')
    return


def od_fps_models_test():
    iterations = 10
    images_names = [mtt.DOGS1] * iterations
    cv_imgs_orig = [load_img_from_web(image_name) for image_name in images_names]
    print(images_names)
    od_models_compare_images_test(
        cv_imgs_orig=cv_imgs_orig,
        images_names=images_names,
        models_selection=ALL_MODELS,
        ms=1
    )
    return


def __pose_get_models(models_selection: str = BEST_MODELS):
    if models_selection == BEST_MODELS:
        # preparing 4 best models
        grid = (2, 2)
        display_im_size = (640, 480)
        models_names = [
            'openpose_pose_mpi',
            'openpose_pose_coco',
            'body25',
            'hand_pose',
        ]
    elif models_selection == ALL_MODELS:
        # preparing all(4) models
        grid = (2, 2)
        display_im_size = (640, 480)
        models_names = cvt.get_all_pose_models_info(ack=False)
        pass
    else:
        # preparing 1 models - default is BEST_MODEL
        grid = (1, 1)
        display_im_size = (640, 480)
        models_names = [models_selection]
    models = []
    for m_name in models_names:
        save_dir = '{}/{}/{}'.format(mtt.CV2_MODELS, cvt.MODELS_OPEN_POSE_META_DATA[m_name]['job'], m_name)
        m = cvt.DnnOpenPoseModels(
            save_load_dir=save_dir,
            model_name=m_name,
            tabs=1,
            # threshold=x,  # take default
            # in_dims=(x, x),  # take default
            # scalefactor=x,  # take default
            # mean=(0, 0, 0),  # take default
            # swapRB=x,  # take default
            # crop=x,  # take default
        )
        print(m)
        models.append(m)
    return models, grid, display_im_size


def __od_get_models(models_selection: str = BEST_MODELS):
    if models_selection == BEST_MODELS:
        # preparing 4 best models
        grid = (2, 2)
        display_im_size = (640, 480)
        models_names = [
            'yolov3',
            'yolov3-ssp',
            'yolov4',
            'yolov4-tiny',
        ]
    elif models_selection == ALL_MODELS:
        # preparing all(19) models
        grid = (4, 5)
        display_im_size = (320, 240)
        models_names = cvt.get_all_object_detection_models_info(ack=False)
    else:
        # preparing 1 models - default is BEST_MODEL
        grid = (1, 1)
        display_im_size = (640, 480)
        models_names = [models_selection]
    models = []
    for m_name in models_names:
        save_dir = '{}/{}/{}'.format(mtt.CV2_MODELS, cvt.MODELS_DNN_OBJECT_DETECTION_META_DATA[m_name]['job'], m_name)
        m = cvt.DnnObjectDetectionModels(
            save_load_dir=save_dir,
            model_name=m_name,
            # allowed_class=['dog', 'cat'],
            tabs=1,
            # threshold=0.1,  # take default
            # nms_threshold=0.3,  # take default
            # in_dims=(416, 416),  # take default
            # scalefactor=1 / 127.5,  # take default
            # mean=(0, 0, 0),  # take default
            # swapRB=True,  # take default
            # crop=False,  # take default
        )
        print(m)
        models.append(m)
    return models, grid, display_im_size


def __od_models_images_test(
        models: list,
        images_names: list,
        cv_imgs_orig: list,
        grid: tuple,
        delay_ms: int,
        save_dir: (str, None),
        display_im_size: tuple,
        with_tf: tuple = False,
        with_sub: tuple = False,
):
    """
    AUX FUNCTION
    :param models:
    :param images_names: for debugging (name of classification, save output name ...)
    :param cv_imgs_orig: will classify on this images
    :param grid:
    :param delay_ms:
    :param save_dir:
    :param display_im_size:
    :return:
    """
    # Prepare cv images list
    fps_list = [mt.FPS(summary_title='detection {}'.format(models[i].name)) for i in range(len(models))]
    for cv_img, img_name in zip(cv_imgs_orig, images_names):
        cv_img_per_model = []
        for j, model in enumerate(models):
            cv_img_clone = cv_img.copy()
            fps_list[j].start()
            detections = model.detect_cv_img(
                cv_img=cv_img,
                fp=2,
                ack=False, # TODO False
                tabs=2,
                img_title=img_name
            )
            fps_list[j].update(ack_progress=True, tabs=1, with_title=True)
            if with_tf:
                detections = model.add_traffic_light_to_detections(
                    detections,
                    traffic_light_p={
                        'up': 0.2,
                        'mid': 0.3,
                        'down': 0.4
                    }
                )
            if with_sub:
                detections = model.add_sub_sub_image_to_detection(
                    detections,
                    cv_img=cv_img,
                    bbox_image_p={
                        'x_start': 0.2,
                        'x_end': 0.8,
                        'y_start': 1,
                        'y_end': 0.5,
                    },
                )

            model.draw_detections(
                detections,
                # colors_d=tflt.ssd_mobilenet_coco.DEFAULT_COLOR_D,
                colors_d={
                    'bbox': 'r',
                    'label_bbox': 'black',
                    'text': 'white',
                    'sub_image': 'blue',
                    'person_bbox': 'lightgreen',
                    'dog_bbox': 'blue',
                },
                cv_img=cv_img_clone,
                draw_labels=True,
                ack=False,
                tabs=1,
                img_title=img_name,
            )
            title = 'detections({}) on image {} {}:'.format(len(detections), img_name, cv_img.shape)
            cvt.add_header(cv_img_clone, header=title, loc=pyplt.Location.TOP_LEFT.value, bg_font_scale=2)
            cvt.add_header(cv_img_clone, header=model.name, loc=pyplt.Location.BOTTOM_LEFT.value, bg_font_scale=1)
            cv_img_clone = cv2.resize(cv_img_clone, display_im_size, interpolation=cv2.INTER_AREA)
            cv_img_per_model.append(cv_img_clone)

        if save_dir is not None:
            save_path = '{}/{}.jpg'.format(save_dir, img_name)
        else:
            save_path = None

        cvt.display_open_cv_images(
            cv_img_per_model,
            ms=delay_ms,
            title='{}'.format(img_name),
            loc=pyplt.Location.CENTER_CENTER.value,
            resize=None,
            grid=grid,
            header=None,
            save_path=save_path
        )
        cv2.destroyAllWindows()
    for fps in fps_list:
        fps.finalize()
    return


def __od_models_cap_test(
        models: list,
        cap: (cv2.VideoCapture, cvt.CameraWu),
        total_frames: int,
        work_every_x_frames: int,
        grid: tuple,
        delay_ms: int,
        save_dir: (str, None),
        display_im_size: tuple,
        cap_desc: str,
        with_tf: tuple = False,
        with_sub: tuple = False,
):
    """
    AUX FUNCTION
    :param models:
    :param grid:
    :param delay_ms:
    :param display_im_size:
    :return:
    """
    if save_dir is not None:
        out_fp = '{}/{}_detected.mp4'.format(save_dir, cap_desc)
        out_dims = (display_im_size[0] * grid[1], display_im_size[1] * grid[0])
        mp4 = cvt.Mp4_creator(
            out_full_path=out_fp,
            out_fps=20.0,
            out_dims=out_dims
        )
        print(mp4)
        print('\tvid size output will be {}'.format(out_dims))
    else:
        mp4 = None
    fps_list = [mt.FPS(summary_title='detection {}'.format(models[i].name)) for i in range(len(models))]

    for i in range(total_frames):
        if isinstance(cap, cv2.VideoCapture):
            success, cv_img = cap.read()
        else:
            success, cv_img = cap.read_img()
        if i % work_every_x_frames != 0:  # s
            # do only 10 frames
            continue
        print('\tframe {}/{}:'.format(i + 1, total_frames))
        if success:
            cv_img_per_model = []
            for j, model in enumerate(models):
                cv_img_clone = cv_img.copy()
                fps_list[j].start()
                detections = model.detect_cv_img(
                    cv_img=cv_img,
                    fp=2,
                    ack=False,
                    tabs=1,
                    img_title='frame {}'.format(i + 1)
                )
                fps_list[j].update(ack_progress=True, tabs=2, with_title=True)
                if with_tf:
                    detections = model.add_traffic_light_to_detections(
                        detections,
                        traffic_light_p={
                            'up': 0.2,
                            'mid': 0.3,
                            'down': 0.4
                        }
                    )
                if with_sub:
                    detections = model.add_sub_sub_image_to_detection(
                        detections,
                        cv_img=cv_img,
                        bbox_image_p={
                            'x_start': 0.2,
                            'x_end': 0.8,
                            'y_start': 1,
                            'y_end': 0.5,
                        },
                    )

                model.draw_detections(
                    detections,
                    # colors_d=tflt.ssd_mobilenet_coco.DEFAULT_COLOR_D,
                    colors_d={
                        'bbox': 'r',
                        'label_bbox': 'black',
                        'text': 'white',
                        'sub_image': 'blue',
                        'person_bbox': 'lightgreen',
                        'dog_bbox': 'blue',
                    },
                    cv_img=cv_img_clone,
                    draw_labels=True,
                    ack=False,
                    tabs=1,
                    img_title='frame {}'.format(i + 1),
                )
                title = 'detections({}) on frame {}/{} {}:'.format(len(detections), (i + 1), total_frames, cv_img.shape)
                cvt.add_header(cv_img_clone, header=title, loc=pyplt.Location.TOP_LEFT.value, bg_font_scale=2)
                cvt.add_header(cv_img_clone, header=model.name, loc=pyplt.Location.BOTTOM_LEFT.value, bg_font_scale=1)
                cv_img_clone = cv2.resize(cv_img_clone, display_im_size, interpolation=cv2.INTER_AREA)
                cv_img_per_model.append(cv_img_clone)
            if mp4 is not None:
                big_img = cvt.unpack_list_imgs_to_big_image(cv_img_per_model, grid=grid, resize=None)
                mp4.add_frame(big_img)
            cv_title = '{} models'.format(len(models)) if len(models) > 1 else models[0].name
            cv_title += ' on {}'.format(cap_desc)
            cvt.display_open_cv_images(
                cv_img_per_model,
                ms=delay_ms,
                title=cv_title,
                loc=pyplt.Location.CENTER_CENTER.value,
                resize=None,
                grid=grid,
                header=None,
                save_path=None
            )
    for fps in fps_list:
        fps.finalize()
    cv2.destroyAllWindows()
    if mp4 is not None:
        mp4.finalize()
    return


def od_best_model_images_test(m_name: str = OD_BEST_MODEL, ms: int = BLOCK_MS_NORMAL):
    mt.get_function_name(ack=True, tabs=0)
    od_models_compare_images_test(
        models_selection=m_name,
        ms=ms
    )
    return


def od_models_compare_images_test(
        cv_imgs_orig: list = None,
        images_names: list = None,
        models_selection: str = BEST_MODELS,
        ms: int = BLOCK_MS_NORMAL
):
    mt.get_function_name(ack=True, tabs=0)
    models, grid, im_size = __od_get_models(models_selection)

    if cv_imgs_orig is None:
        images_names = [mtt.DOGS1, mtt.PERSON, mtt.FACES]
        cv_imgs_orig = [load_img_from_web(image_name) for image_name in images_names]
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
    __od_models_images_test(
        models=models,
        images_names=images_names,
        cv_imgs_orig=cv_imgs_orig,
        grid=grid,
        delay_ms=ms,
        save_dir=save_dir,
        display_im_size=im_size
    )
    return


def od_best_model_video_test(
        m_name: str = OD_BEST_MODEL,
        video_path: str = None,
        video_name: str = 'unknown',
        work: int = 80
):
    mt.get_function_name(ack=True, tabs=0)
    od_models_compare_video_test(
        video_path=video_path,
        video_name=video_name,
        models_selection=m_name,
        work=work
    )
    return


def od_models_compare_video_test(
        video_path: str = None,
        video_name: str = 'unknown',
        work: int = 80,
        models_selection: str = BEST_MODELS
):
    mt.get_function_name(ack=True, tabs=0)
    models, grid, im_size = __od_get_models(models_selection)
    if video_path is None:  # default video
        video_name = mtt.DOG1
        video_path = get_vid_from_web(name=video_name)

    if not os.path.exists(video_path):
        mt.exception_error(mt.NOT_FOUND.format(video_path), real_exception=False)
        return
    cap = cv2.VideoCapture(video_path)
    if cap.isOpened():
        video_total_frames = cvt.get_frames_from_cap(cap)
        print('\tvid {} has {} frames'.format(video_name, video_total_frames))
        save_dir = '{}/{}/{}/{}'.format(mtt.VIDEOS_OUTPUTS, mt.get_function_name(), SAVE_SCOPE, models_selection)
        mt.create_dir(save_dir)

        __od_models_cap_test(
            models=models,
            cap=cap,
            total_frames=video_total_frames,
            work_every_x_frames=work,
            grid=grid,
            delay_ms=1,
            save_dir=save_dir,
            display_im_size=im_size,
            cap_desc=video_name,
        )
    else:
        mt.exception_error('cap is closed.', real_exception=False)
    return


def od_best_model_cam_test(
        m_name: str = OD_BEST_MODEL,
        total_frames: int = MODEL_FRAMES_CAM
):
    mt.get_function_name(ack=True, tabs=0)
    od_models_compare_cam_test(
        models_selection=m_name,
        total_frames=total_frames
    )
    return


def od_models_compare_cam_test(
        models_selection: str = BEST_MODELS,
        total_frames: int = MODEL_FRAMES_CAM
):
    mt.get_function_name(ack=True, tabs=0)
    models, grid, im_size = __od_get_models(models_selection)
    cam = cvt.CameraWu.open_camera(port=0, type_cam='cv2')
    if cam is not None:
        save_dir = '{}/{}/{}/{}'.format(mtt.VIDEOS_OUTPUTS, mt.get_function_name(), SAVE_SCOPE, models_selection)
        mt.create_dir(save_dir)
        __od_models_cap_test(
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


def add_text_test():
    mt.get_function_name(ack=True, tabs=0)
    img = load_img_from_web(mtt.HORSES)
    cvt.add_text(img, header='test text', pos=(100, 100), text_color='r', with_rect=True, bg_color='y', bg_font_scale=2)
    cvt.add_text(img, header='test text', pos=(100, 200), text_color='black', with_rect=True, bg_color='b',
                 bg_font_scale=1)
    cvt.display_open_cv_image(img, ms=BLOCK_MS_NORMAL, loc=pyplt.Location.CENTER_CENTER.value)
    cv2.destroyAllWindows()
    return


def add_header_test():
    mt.get_function_name(ack=True, tabs=0)
    img = load_img_from_web(mtt.HORSES)

    cvt.add_header(img, header='TOP_LEFT', loc=pyplt.Location.TOP_LEFT.value,
                   text_color='lime', with_rect=True, bg_color='azure', bg_font_scale=1)
    cvt.add_header(img, header='BOTTOM_LEFT', loc=pyplt.Location.BOTTOM_LEFT.value,
                   text_color='fuchsia', with_rect=True, bg_color='black', bg_font_scale=2)
    cvt.display_open_cv_image(img, ms=BLOCK_MS_NORMAL, loc=pyplt.Location.CENTER_CENTER.value)
    cv2.destroyAllWindows()

    img = load_img_from_web(mtt.DOG)
    cvt.display_open_cv_image(
        img,
        ms=BLOCK_MS_NORMAL,
        loc=pyplt.Location.CENTER_CENTER.value,
        header='direct header into display_open_cv_image'
    )
    cv2.destroyAllWindows()
    return


def Mp4_creator_test():
    mt.get_function_name(ack=True, tabs=0)
    # now open video file
    vid_name = mtt.DOG1
    video_path = get_vid_from_web(name=vid_name)

    if not os.path.exists(video_path):
        mt.exception_error(mt.NOT_FOUND.format(video_path), real_exception=False)
        return
    cap = cv2.VideoCapture(video_path)
    if cap.isOpened():
        out_dims = cvt.get_dims_from_cap(cap)
        video_total_frames = cvt.get_frames_from_cap(cap)
        print('\tvid {} has {} frames'.format(vid_name, video_total_frames))
        print('\tvid size is {}'.format(out_dims))
    else:
        mt.exception_error('cap is closed.', real_exception=False)
        return

    out_dir = '{}/create_mp4_test'.format(mtt.VIDEOS_OUTPUTS)
    mt.create_dir(out_dir)
    out_fp = '{}/{}_output.mp4'.format(out_dir, vid_name)

    mp4_creator = cvt.Mp4_creator(
        out_full_path=out_fp,
        out_fps=20.0,
        out_dims=out_dims
    )
    print(mp4_creator)

    for i in range(video_total_frames):
        success, frame = cap.read()
        if i % int(video_total_frames / 10) != 0:  # s
            # do only 10 frames
            continue
        print('\tframe {}/{}:'.format(i + 1, video_total_frames))
        # print('\t\t{}'.format(mt.to_str(frame)))
        if success:
            cvt.add_header(
                frame,
                header='create_mp4_test frame {}/{}'.format(i + 1, video_total_frames),
                loc=pyplt.Location.BOTTOM_LEFT.value,
                text_color=pyplt.get_random_color(),
                bg_color=pyplt.get_random_color(),
            )
            cvt.display_open_cv_image(frame, ms=1, title=vid_name, loc=None,
                                      header='{}/{}'.format(i + 1, video_total_frames))
            mp4_creator.add_frame(frame, ack=True, tabs=2)

    cap.release()
    mp4_creator.finalize()
    cv2.destroyAllWindows()
    return


def __pose_models_images_test(
        models: list,
        images_names: list,
        cv_imgs_orig: list,
        grid: tuple,
        delay_ms: int,
        save_dir: (str, None),
        display_im_size: tuple,
):
    """
    AUX FUNCTION
    :param models:
    :param images_names: for debugging (name of classification, save output name ...)
    :param cv_imgs_orig: will classify on this images
    :param grid:
    :param delay_ms:
    :param save_dir:
    :param display_im_size:
    :return:
    """
    # Prepare cv images list
    fps_list = [mt.FPS(summary_title='detection {}'.format(models[i].name)) for i in range(len(models))]
    for cv_img, img_name in zip(cv_imgs_orig, images_names):
        cv_img_per_model = []
        for j, model in enumerate(models):
            cv_img_clone = cv_img.copy()
            fps_list[j].start()
            detections = model.detect_cv_img(
                cv_img=cv_img,
                fp=2,
                ack=False,  # todo False
                tabs=2,
                img_title=img_name
            )
            fps_list[j].update(ack_progress=True, tabs=1, with_title=True)

            model.draw_detections(
                detections,
                colors_d={
                    'joint_c': 'red',
                    'edge_c': 'lightgreen',
                    'text_c': 'white',
                },
                cv_img=cv_img_clone,
                draw_pose=True,
                draw_points=False,  # todo False
                ack=False,  # todo False
                tabs=1,
                img_title=img_name,
            )
            title = 'detections({}) on image {} {}:'.format(len(detections), img_name, cv_img.shape)
            cvt.add_header(cv_img_clone, header=title, loc=pyplt.Location.TOP_LEFT.value, bg_font_scale=2)
            cvt.add_header(cv_img_clone, header=model.name, loc=pyplt.Location.BOTTOM_LEFT.value, bg_font_scale=1)
            cv_img_clone = cv2.resize(cv_img_clone, display_im_size, interpolation=cv2.INTER_AREA)
            cv_img_per_model.append(cv_img_clone)

        if save_dir is not None:
            save_path = '{}/{}.jpg'.format(save_dir, img_name)
        else:
            save_path = None

        cvt.display_open_cv_images(
            cv_img_per_model,
            ms=delay_ms,
            title='{}'.format(img_name),
            loc=pyplt.Location.CENTER_CENTER.value,
            resize=None,
            grid=grid,
            header=None,
            save_path=save_path
        )
        cv2.destroyAllWindows()
    for fps in fps_list:
        fps.finalize()
    return


def pose_best_model_images_test(m_name: str = POSE_BEST_MODEL, ms: int = BLOCK_MS_NORMAL):
    mt.get_function_name(ack=True, tabs=0)

    pose_models_compare_images_test(
        models_selection=m_name,
        ms=ms
    )
    return


def pose_models_compare_images_test(
        cv_imgs_orig: list = None,
        images_names: list = None,
        models_selection: str = BEST_MODELS,
        ms: int = BLOCK_MS_NORMAL
):
    mt.get_function_name(ack=True, tabs=0)
    models, grid, im_size = __pose_get_models(models_selection)

    if cv_imgs_orig is None:
        images_names = [mtt.PERSON]
        cv_imgs_orig = [load_img_from_web(image_name) for image_name in images_names]
    else:
        if images_names is None:
            images_names = []
            for i in range(len(cv_imgs_orig)):
                images_names.append('unknown{}'.format(i))
        if len(images_names) != len(cv_imgs_orig):
            mt.exception_error('lists length differ {}, {}'.format(len(images_names), len(cv_imgs_orig)),
                               real_exception=False)
            return

    # images_dir = '{}/Input2'.format(mtt.IMAGES_PATH)
    # images_paths = mt.find_files_in_folder(dir_path=images_dir, file_suffix='PNG', ack=True)
    # images_paths += mt.find_files_in_folder(dir_path=images_dir, file_suffix='jpg', ack=True)
    # images_names = [os.path.basename(img_path).split('.')[0] for img_path in images_paths]
    # cv_imgs_orig = [cvt.load_img(img_path) for img_path in images_paths]

    save_dir = '{}/{}/{}/{}'.format(mtt.IMAGES_OUTPUTS, mt.get_function_name(), SAVE_SCOPE, models_selection)
    if not os.path.exists(save_dir):
        mt.create_dir(save_dir)
    __pose_models_images_test(
        models=models,
        images_names=images_names,
        cv_imgs_orig=cv_imgs_orig,
        grid=grid,
        delay_ms=ms,
        save_dir=save_dir,
        display_im_size=im_size
    )
    return


def pose_best_model_cam_test(
        m_name: str = POSE_BEST_MODEL,
        total_frames: int = MODEL_FRAMES_CAM
):
    mt.get_function_name(ack=True, tabs=0)
    pose_models_compare_cam_test(
        models_selection=m_name,
        total_frames=total_frames
    )
    return


def pose_models_compare_cam_test(
        models_selection: str = BEST_MODELS,
        total_frames: int = MODEL_FRAMES_CAM
):
    mt.get_function_name(ack=True, tabs=0)
    models, grid, im_size = __pose_get_models(models_selection)
    cam = cvt.CameraWu.open_camera(port=0, type_cam='cv2')
    if cam is not None:
        save_dir = '{}/{}/{}/{}'.format(mtt.VIDEOS_OUTPUTS, mt.get_function_name(), SAVE_SCOPE, models_selection)
        mt.create_dir(save_dir)
        __pose_models_cap_test(
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


def __pose_models_cap_test(
        models: list,
        cap: (cv2.VideoCapture, cvt.CameraWu),
        total_frames: int,
        work_every_x_frames: int,
        grid: tuple,
        delay_ms: int,
        save_dir: (str, None),
        display_im_size: tuple,
        cap_desc: str,
):
    """
    AUX FUNCTION
    :param models:
    :param grid:
    :param delay_ms:
    :param display_im_size:
    :return:
    """
    if save_dir is not None:
        out_fp = '{}/{}_detected.mp4'.format(save_dir, cap_desc)
        out_dims = (display_im_size[0] * grid[1], display_im_size[1] * grid[0])
        mp4 = cvt.Mp4_creator(
            out_full_path=out_fp,
            out_fps=20.0,
            out_dims=out_dims
        )
        print(mp4)
        print('\tvid size output will be {}'.format(out_dims))
    else:
        mp4 = None
    fps_list = [mt.FPS(summary_title='detection {}'.format(models[i].name)) for i in range(len(models))]

    for i in range(total_frames):
        if isinstance(cap, cv2.VideoCapture):
            success, cv_img = cap.read()
        else:
            success, cv_img = cap.read_img()
        if i % work_every_x_frames != 0:  # s
            # do only 10 frames
            continue
        print('\tframe {}/{}:'.format(i + 1, total_frames))
        if success:
            cv_img_per_model = []
            for j, model in enumerate(models):
                cv_img_clone = cv_img.copy()
                fps_list[j].start()
                detections = model.detect_cv_img(
                    cv_img=cv_img,
                    fp=2,
                    ack=False,  # todo False
                    tabs=1,
                    img_title='frame {}'.format(i + 1)
                )
                fps_list[j].update(ack_progress=True, tabs=2, with_title=True)

                model.draw_detections(
                    detections,
                    colors_d={
                        'joint_c': 'red',
                        'edge_c': 'lightgreen',
                        'text_c': 'white',
                    },
                    cv_img=cv_img_clone,
                    draw_pose=True,
                    draw_points=False,
                    ack=False,  # todo False
                    tabs=1,
                    img_title='frame {}'.format(i + 1),
                )
                title = 'detections({}) on frame {}/{} {}:'.format(len(detections), (i + 1), total_frames, cv_img.shape)
                cvt.add_header(cv_img_clone, header=title, loc=pyplt.Location.TOP_LEFT.value, bg_font_scale=2)
                cvt.add_header(cv_img_clone, header=model.name, loc=pyplt.Location.BOTTOM_LEFT.value, bg_font_scale=1)
                cv_img_clone = cv2.resize(cv_img_clone, display_im_size, interpolation=cv2.INTER_AREA)
                cv_img_per_model.append(cv_img_clone)
            if mp4 is not None:
                big_img = cvt.unpack_list_imgs_to_big_image(cv_img_per_model, grid=grid, resize=None)
                mp4.add_frame(big_img)
            cv_title = '{} models'.format(len(models)) if len(models) > 1 else models[0].name
            cv_title += ' on {}'.format(cap_desc)
            cvt.display_open_cv_images(
                cv_img_per_model,
                ms=delay_ms,
                title=cv_title,
                loc=pyplt.Location.CENTER_CENTER.value,
                resize=None,
                grid=grid,
                header=None,
                save_path=None
            )
    for fps in fps_list:
        fps.finalize()
    cv2.destroyAllWindows()
    if mp4 is not None:
        mp4.finalize()
    return


def test_all():
    print('{}{}:'.format('-' * 5, mt.get_base_file_and_function_name()))
    get_cv_version_test()
    imread_imwrite_test()
    list_to_cv_image_test()
    display_open_cv_image_test()
    display_open_cv_image_loop_test()
    resize_opencv_image_test()
    move_cv_img_x_y_test()
    move_cv_img_by_str_test()
    unpack_list_imgs_to_big_image_test()
    display_open_cv_images_test()
    display_open_cv_images_loop_test()
    gray_to_BGR_and_back_test()
    BGR_img_to_RGB_and_back_test()
    add_header_test()
    add_text_test()
    CameraWu_cv2_test()
    CameraWu_acapture_test()
    CameraWu_imutils_test()
    od_best_model_images_test()
    od_best_model_video_test()
    od_best_model_cam_test()
    od_models_compare_images_test()
    od_models_compare_video_test()
    od_models_compare_cam_test()
    Mp4_creator_test()
    pose_best_model_images_test()
    pose_best_model_cam_test()
    print('{}'.format('-' * 20))
    return
