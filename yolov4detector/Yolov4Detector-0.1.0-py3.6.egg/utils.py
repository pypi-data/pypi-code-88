import os
import cv2
import random
import numpy as np
from Yolov4Detector import darknet
from PIL import Image, ImageFont, ImageDraw

def scale_coords(img1_shape, coords, img0_shape):
    h_src, w_src = img0_shape
    h_dst, w_dst = img1_shape

    coords = coords.astype(np.float)
    coords[:, [0, 2]] *= (w_src / w_dst)
    coords[:, [1, 3]] *= (h_src / h_dst)
    return coords

# def check_batch_shape(images, batch_size):
#     """
#         Image sizes should be the same width and height
#     """
#     shapes = [image.shape for image in images]
#     if len(set(shapes)) > 1:
#         raise ValueError("Images don't have same shape")
#     if len(shapes) > batch_size:
#         raise ValueError("Batch size higher than number of images")
#     return shapes[0]

def plot_one_box(x, img, color=None, label=None, line_thickness=None):
    # Plots one bounding box on image img
    tl = line_thickness or round(0.002 * (img.shape[0] + img.shape[1]) / 2) + 1  # line/font thickness
    color = color or [random.randint(0, 255) for _ in range(3)]
    c1, c2 = (int(x[0]), int(x[1])), (int(x[2]), int(x[3]))
    cv2.rectangle(img, c1, c2, color, thickness=tl)
    if label:
        tf = max(tl - 1, 1)  # font thickness
        t_size = cv2.getTextSize(label, 0, fontScale=tl / 3, thickness=tf)[0]
        c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
        cv2.putText(img, label, (c1[0], c1[1] - 2), 0, tl / 3, color, thickness=tf, lineType=cv2.LINE_AA)

# def prepare_batch(images, network, channels=3):
#     width = darknet.network_width(network)
#     height = darknet.network_height(network)

#     darknet_images = []
#     for image in images:
#         image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#         image_resized = cv2.resize(image_rgb, (width, height),
#                                    interpolation=cv2.INTER_LINEAR)
#         custom_image = image_resized.transpose(2, 0, 1)
#         darknet_images.append(custom_image)

#     batch_array = np.concatenate(darknet_images, axis=0)
#     batch_array = np.ascontiguousarray(batch_array.flat, dtype=np.float32)/255.0
#     darknet_images = batch_array.ctypes.data_as(darknet.POINTER(darknet.c_float))
#     return darknet.IMAGE(width, height, channels, darknet_images)

# def batch_detection(network, images, class_names, thresh=0.25, hier_thresh=.5, nms=.45, batch_size=4):
#     image_height, image_width, _ = check_batch_shape(images, batch_size)
#     darknet_images = prepare_batch(images, network)
#     batch_detections = darknet.network_predict_batch(network, darknet_images, batch_size, image_width,
#                                                      image_height, thresh, hier_thresh, None, 0, 0)
#     batch_predictions = []
#     for idx in range(batch_size):
#         num = batch_detections[idx].num
#         detections = batch_detections[idx].dets
#         if nms:
#             darknet.do_nms_obj(detections, num, len(class_names), nms)
#         predictions = darknet.remove_negatives(detections, class_names, num)
#         batch_predictions.append(predictions)
#     darknet.free_batch_detections(batch_detections, batch_size)
#     return batch_predictions
