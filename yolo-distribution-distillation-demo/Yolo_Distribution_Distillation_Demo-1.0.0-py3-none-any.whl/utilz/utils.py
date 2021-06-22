import sys
import os
import time
import math
import numpy as np
import matplotlib.pyplot as plt
import cv2

from torchvision.ops import nms
import torch

import itertools
import struct  # get_image_size
import imghdr  # get_image_size


def nms_cpu(boxes, confs, nms_thresh=0.5, min_mode=False):
    # print(boxes.shape)
    x1 = boxes[:, 0]
    y1 = boxes[:, 1]
    x2 = boxes[:, 2]
    y2 = boxes[:, 3]

    areas = (x2 - x1) * (y2 - y1)
    order = confs.argsort()[::-1]

    keep = []
    while order.size > 0:
        idx_self = order[0]
        idx_other = order[1:]

        keep.append(idx_self)

        xx1 = np.maximum(x1[idx_self], x1[idx_other])
        yy1 = np.maximum(y1[idx_self], y1[idx_other])
        xx2 = np.minimum(x2[idx_self], x2[idx_other])
        yy2 = np.minimum(y2[idx_self], y2[idx_other])

        w = np.maximum(0.0, xx2 - xx1)
        h = np.maximum(0.0, yy2 - yy1)
        inter = w * h

        if min_mode:
            over = inter / np.minimum(areas[order[0]], areas[order[1:]])
        else:
            over = inter / (areas[order[0]] + areas[order[1:]] - inter)

        inds = np.where(over <= nms_thresh)[0]
        order = order[inds + 1]
    
    return np.array(keep)



def plot_boxes_cv2(img, boxes, savename=None, class_names=None, color=None):

    colors = np.array([[1, 0, 1], [0, 0, 1], [0, 1, 1], [0, 1, 0], [1, 1, 0], [1, 0, 0]], dtype=np.float32)

    def get_color(c, x, max_val):
        ratio = float(x) / max_val * 5
        i = int(math.floor(ratio))
        j = int(math.ceil(ratio))
        ratio = ratio - i
        r = (1 - ratio) * colors[i][c] + ratio * colors[j][c]
        return int(r * 255)

    width = img.shape[1]
    height = img.shape[0]

    if len(boxes) > 1:
        for i in range(len(boxes)):
            box = boxes[i]
            x1 = int(box[0] * width)
            y1 = int(box[1] * height)
            x2 = int(box[2] * width)
            y2 = int(box[3] * height)

            if color:
                rgb = color
            else:
                rgb = (255, 0, 0)

            cls_conf = box[4]
            cls_id = int(box[5])

            print('%s: %f' % (class_names[cls_id], cls_conf))

            classes = len(class_names)
            offset = cls_id * 123457 % classes
            red = get_color(2, offset, classes)
            green = get_color(1, offset, classes)
            blue = get_color(0, offset, classes)

            if color is None:
                rgb = (red, green, blue)
                box_color = (0, 0, 255)
            # img = cv2.putText(img, class_names[cls_id], (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1.2, rgb, 1)
            # img = cv2.putText(img, class_names[cls_id] + "  " + str(np.round(cls_conf.item(), decimals=2)),
            #                   (x1, y1), cv2.FONT_HERSHEY_SIMPLEX,
            #                   1.2,
            #                   rgb, 1)
            img = cv2.rectangle(img, (x1, y1), (x2, y2), rgb, 1)

            sigma_cls = float(box[10])

            def draw_text(img, text,
                          font=cv2.FONT_HERSHEY_PLAIN,
                          pos=(0, 0),
                          font_scale=1,
                          font_thickness=2,
                          text_color=(0, 0, 0),
                          text_color_bg=(0, 0, 0)
                          ):

                x, y = pos
                text_size, _ = cv2.getTextSize(text, font, font_scale, font_thickness)
                text_w, text_h = text_size
                cv2.rectangle(img, pos, (x + text_w, y + text_h), text_color_bg, -1)
                cv2.putText(img, text, (x, y + text_h + font_scale - 1), font, font_scale, text_color, font_thickness)

                return text_size
            
            draw_text(img,  class_names[cls_id] + str(np.round(cls_conf.item() * 100, decimals=2)) +  "; (" + str(np.round(sigma_cls * 100, decimals=2)) + ")",
                      pos=(x1, y1), text_color_bg=rgb)


    if savename:
        print("save plot results to %s" % savename)
        cv2.imwrite(savename, img)
    return img



def plot_boxes_cv2_uncertainty(img, boxes, savename=None, class_names=None, color=None):
    # img = np.copy(img)
    colors = np.array([[1, 0, 1], [0, 0, 1], [0, 1, 1], [0, 1, 0], [1, 1, 0], [1, 0, 0]], dtype=np.float32)

    def get_color(c, x, max_val):
        ratio = float(x) / max_val * 5
        i = int(math.floor(ratio))
        j = int(math.ceil(ratio))
        ratio = ratio - i
        r = (1 - ratio) * colors[i][c] + ratio * colors[j][c]
        return int(r * 255)

    width = img.shape[1]
    height = img.shape[0]

    if len(boxes) > 1:
        for i in range(len(boxes)):

            box = boxes[i]
            x1 = int(box[0] * width)
            y1 = int(box[1] * height)
            x2 = int(box[2] * width)
            y2 = int(box[3] * height)

            sigma_x1 = int(box[6] * width) / 3
            sigma_y1 = int(box[7] * height) / 3
            sigma_x2 = int(box[8] * width) / 3
            sigma_y2 = int(box[9] * height) / 3

            sigma_cls = float(box[10])

            if color:
                rgb = color
            else:
                rgb = (255, 0, 0)

            overlay = img.copy()
            alpha = 0.4

            cls_conf = box[4]
            cls_id = int(box[5])

            print('%s: %f' % (class_names[cls_id], cls_conf))

            classes = len(class_names)
            offset = cls_id * 123457 % classes
            red = get_color(2, offset, classes)
            green = get_color(1, offset, classes)
            blue = get_color(0, offset, classes)

            if color is None:
                rgb = (red, green, blue)
                box_color = (0, 0, 255)

            # Mean bounding box
            # img = cv2.rectangle(img, (x1, y1), (x2, y2), rgb, 1)

            # Left edge
            cv2.rectangle(overlay, (int(x1 - sigma_x1 / 2), int(y1 - sigma_y1 / 2)),
                          (int(x1 + sigma_x1 / 2), int(y2 + sigma_y2 / 2)), rgb, -1)
            # Upper edge
            cv2.rectangle(overlay, (int(x1 - sigma_x1 / 2), int(y1 + sigma_y1 / 2)),
                          (int(x2 + sigma_x2 / 2), int(y1 - sigma_y1 / 2)), rgb, -1)
            # Right edge
            cv2.rectangle(overlay, (int(x2 - sigma_x2 / 2), int(y1 + sigma_y1 / 2)),
                          (int(x2 + sigma_x2 / 2), int(y2 - sigma_y2 / 2)), rgb, -1)
            # Lower edge
            cv2.rectangle(overlay, (int(x1 - sigma_x1 / 2), int(y2 - sigma_y2 / 2)),
                          (int(x2 + sigma_x2 / 2), int(y2 + sigma_y2 / 2)), rgb, -1)


            img = cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0)

            # img = cv2.putText(img, class_names[cls_id] + "(" + str(np.round(cls_conf.item(), decimals=2)) +
            #                   ";" + str(np.round(sigma_cls, decimals=2)) + ")", (x1, y1), cv2.FONT_HERSHEY_PLAIN, 1.2,
            #                   rgb, 1)

            def draw_text(img, text,
                          font=cv2.FONT_HERSHEY_PLAIN,
                          pos=(0, 0),
                          font_scale=1,
                          font_thickness=2,
                          text_color=(0, 0, 0),
                          text_color_bg=(0, 0, 0)
                          ):

                x, y = pos
                text_size, _ = cv2.getTextSize(text, font, font_scale, font_thickness)
                text_w, text_h = text_size
                cv2.rectangle(img, pos, (x + text_w, y + text_h), text_color_bg, -1)
                cv2.putText(img, text, (x, y + text_h + font_scale - 1), font, font_scale, text_color, font_thickness)

                return text_size

            draw_text(img,  class_names[cls_id] + str(np.round(cls_conf.item() * 100, decimals=2)) +  "; (" + str(np.round(sigma_cls * 100, decimals=2)) + ")",
                      pos=(x1, y1), text_color_bg=rgb)


    if savename:
        print("save plot results to %s" % savename)
        cv2.imwrite(savename, img)
    return img



def draw_blackbox(img):

    import cv2

    color = (0, 0, 0)
    # color = (150, 150, 150)
    width = img.shape[1]
    height = img.shape[0]

    x4 = 150
    y4 = 300

    w4 = 80
    h4 = 100

    x5 = 300
    y5 = 280

    w5 = 150
    h5 = 100

    img = cv2.rectangle(img=img, pt1=(x4, y4), pt2=(x4 + w4, y4 + h4), color=color, thickness=-1)
    img = cv2.rectangle(img=img, pt1=(x5, y5), pt2=(x5 + w5, y5 + h5), color=color, thickness=-1)

    return img



def show_bounding_boxes(boxes: np.ndarray, labels: np.ndarray, scores: np.ndarray,
                        orig_image: np.ndarray, class_list: list, input_dim: tuple = (512, 512), thresh=0, PATH: str = None):

    import cv2

    # resize image
    orig_image = cv2.resize(orig_image, input_dim, interpolation=cv2.INTER_AREA)

    plt.figure(figsize=(20, 12))
    plt.imshow(orig_image)
    current_axis = plt.gca()
    colors = plt.cm.hsv(np.linspace(0, 1, len(class_list))).tolist()

    for box, label, score in zip(boxes, labels, scores):
        # Transform the predicted bounding boxes for the 512x512 image to the original image dimensions.
        # xmin = float(box[0] * orig_image.shape[1] / input_dim[0])
        # ymin = float(box[1] * orig_image.shape[0] / input_dim[1])
        # xmax = float(box[2] * orig_image.shape[1] / input_dim[0])
        # ymax = float(box[3] * orig_image.shape[0] / input_dim[1])

        xmin = float(box[0] * input_dim[0])
        ymin = float(box[1] * input_dim[1])
        xmax = float(box[2] * input_dim[0])
        ymax = float(box[3] * input_dim[1])

        color = colors[int(label)]
        label = '{}: {:.2f}'.format(class_list[int(round((float(label))))], score*100)

        if score > thresh:
            current_axis.add_patch(plt.Rectangle((xmin, ymin), xmax-xmin, ymax-ymin, color=color, fill=False, linewidth=2))
            current_axis.text(xmin, ymin, label, size='x-large', color='white', bbox={'facecolor': color, 'alpha': 1.0})

    if PATH is not None:
        plt.savefig(PATH, bbox_inches='tight')
    plt.show()



def show_uncertainty_boxes(boxes, labels, scores, std_boxes, std_cls, classes, orig_image, input_dim=(512, 512), PATH: str = None):

    import cv2

    # resize image
    orig_image = cv2.resize(orig_image, input_dim, interpolation=cv2.INTER_AREA)

    # plt.figure()
    plt.figure(figsize=(20, 12))
    plt.imshow(orig_image)
    current_axis = plt.gca()

    colors = plt.cm.hsv(np.linspace(0, 1, len(classes))).tolist()

    for box, label, score, std, cls in zip(boxes, labels, scores, std_boxes, std_cls):


        xmin = float(box[0] * input_dim[0])
        ymin = float(box[1] * input_dim[1])
        xmax = float(box[2] * input_dim[0])
        ymax = float(box[3] * input_dim[1])

        color = colors[int(label)]
        label = '{}: {:.2f}'.format(classes[int(round((float(label))))], score*100)
        # current_axis.add_patch(plt.Rectangle((xmin, ymin), xmax-xmin, ymax-ymin, color=color, fill=False, linewidth=2))
        current_axis.text(xmin, ymin, label + "({:2.2f})".format(cls*100), size='x-large', color='white', bbox={'facecolor':color, 'alpha':1.0})


        std_xmin = float(std[0] * input_dim[0]) / 5
        std_ymin = float(std[1] * input_dim[1]) / 5
        std_xmax = float(std[2] * input_dim[0]) / 5
        std_ymax = float(std[3] * input_dim[1]) / 5

        # Blue coverage of bounding box
        color_fill = (0.1, 0.2, 0.5, 0.3)
        current_axis.fill([xmin, xmin, xmax, xmax], [ymin, ymax, ymax, ymin], color = color_fill)
        current_axis.fill([xmin + std_xmin, xmin + std_xmin, xmax - std_xmax, xmax - std_xmax],
                          [ymin + std_ymin, ymax - std_ymax, ymax - std_ymax, ymin + std_ymin], color=color_fill, lw=None)

        # Edges with uncertainty widths
        color_fill = (0.5, 0.08, 0.08, 0.6)
        current_axis.fill([xmin - std_xmin, xmin - std_xmin, xmax + std_xmax, xmax + std_xmax],
                          [ymin - std_ymin, ymin + std_ymin, ymin + std_ymin, ymin - std_ymin], color=color_fill, lw=None)

        current_axis.fill([xmin - std_xmin, xmin - std_xmin, xmax + std_xmax, xmax + std_xmax],
                          [ymax - std_ymax, ymax + std_ymax, ymax + std_ymax, ymax - std_ymax], color=color_fill, lw=None)

        current_axis.fill([xmin - std_xmin, xmin - std_xmin, xmin + std_xmin, xmin + std_xmin],
                          [ymin + std_ymin, ymax - std_ymax, ymax - std_ymax, ymin + std_ymin], color=color_fill, lw=None)

        current_axis.fill([xmax - std_xmax, xmax - std_xmax, xmax + std_xmax, xmax + std_xmax],
                          [ymin + std_ymin, ymax - std_ymax, ymax - std_ymax, ymin + std_ymin], color=color_fill, lw=None)
    if PATH is not None:
        plt.savefig(PATH, bbox_inches='tight')
    plt.show()




def load_class_names(namesfile):
    class_names = []
    with open(namesfile, 'r') as fp:
        lines = fp.readlines()
    for line in lines:
        line = line.rstrip()
        class_names.append(line)
    return class_names


def post_processing(img, conf_thresh, nms_thresh, output):

    # anchors = [12, 16, 19, 36, 40, 28, 36, 75, 76, 55, 72, 146, 142, 110, 192, 243, 459, 401]
    # num_anchors = 9
    # anchor_masks = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    # strides = [8, 16, 32]
    # anchor_step = len(anchors) // num_anchors

    # [batch, num, 1, 4]
    box_array = output[0]
    # [batch, num, num_classes]
    confs = output[1]

    if len(output) == 3:
        var_array = output[2]

    t1 = time.time()

    if type(box_array).__name__ != 'ndarray':
        box_array = box_array.cpu().detach().numpy()
        confs = confs.cpu().detach().numpy()
        if len(output) == 3:
            var_array = var_array.cpu().detach().numpy()

    num_classes = confs.shape[2]

    # [batch, num, 4]
    box_array = box_array[:, :, 0]
    if len(output) == 3:
        var_array = var_array[:, :, 0]

    # [batch, num, num_classes] --> [batch, num]
    max_conf = np.max(confs, axis=2)
    max_id = np.argmax(confs, axis=2)

    t2 = time.time()

    bboxes_batch = []
    for i in range(box_array.shape[0]):
       
        argwhere = max_conf[i] > conf_thresh
        l_box_array = box_array[i, argwhere, :]
        l_max_conf = max_conf[i, argwhere]
        l_max_id = max_id[i, argwhere]
        if len(output) == 3:
            l_var_array = var_array[i, argwhere, :]

        bboxes = []
        # nms for each class
        for j in range(num_classes):

            cls_argwhere = l_max_id == j
            ll_box_array = l_box_array[cls_argwhere, :]
            ll_max_conf = l_max_conf[cls_argwhere]
            ll_max_id = l_max_id[cls_argwhere]

            if len(output) == 3:
                ll_var_array = l_var_array[cls_argwhere, :]

            keep = nms_cpu(ll_box_array, ll_max_conf, nms_thresh)
            # keep = nms(torch.tensor(ll_box_array), torch.tensor(ll_max_conf), torch.tensor(nms_thresh))
            # keep = keep.cpu().detach().numpy()
            
            if (keep.size > 0):
                ll_box_array = ll_box_array[keep, :]
                ll_max_conf = ll_max_conf[keep]
                ll_max_id = ll_max_id[keep]

                if len(output) == 3:
                    ll_var_array = l_var_array[keep, :]

                for k in range(ll_box_array.shape[0]):
                    if len(output) == 3:
                        bboxes.append([ll_box_array[k, 0], ll_box_array[k, 1], ll_box_array[k, 2], ll_box_array[k, 3],
                                       ll_max_conf[k], ll_max_id[k], ll_var_array[k, 0], ll_var_array[k, 1], ll_var_array[k, 2], ll_var_array[k, 3]])
                    else:
                        bboxes.append([ll_box_array[k, 0], ll_box_array[k, 1], ll_box_array[k, 2], ll_box_array[k, 3], ll_max_conf[k], ll_max_id[k]])
        
        bboxes_batch.append(bboxes)

    t3 = time.time()
    
    return bboxes_batch


def post_processing_uncertainties(img, conf_thresh, nms_thresh, output):
    # anchors = [12, 16, 19, 36, 40, 28, 36, 75, 76, 55, 72, 146, 142, 110, 192, 243, 459, 401]
    # num_anchors = 9
    # anchor_masks = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    # strides = [8, 16, 32]
    # anchor_step = len(anchors) // num_anchors

    # [batch, num, 1, 4]
    box_array = output[0]
    # [batch, num, num_classes]
    confs = output[1]

    if len(output) == 4:
        var_array = output[2]
        cls_stddev = output[3]

    t1 = time.time()

    if type(box_array).__name__ != 'ndarray':
        box_array = box_array.cpu().detach().numpy()
        confs = confs.cpu().detach().numpy()
        if len(output) == 4:
            var_array = var_array.cpu().detach().numpy()
            cls_stddev = cls_stddev.cpu().detach().numpy()

    num_classes = confs.shape[2]

    # [batch, num, 4]
    box_array = box_array[:, :, 0]
    if len(output) == 4:
        var_array = var_array[:, :, 0]

    # [batch, num, num_classes] --> [batch, num]
    max_conf = np.max(confs, axis=2)
    max_id = np.argmax(confs, axis=2)

    t2 = time.time()

    bboxes_batch = []
    confs_batch = []

    for i in range(box_array.shape[0]):

        argwhere = max_conf[i] > conf_thresh
        l_box_array = box_array[i, argwhere, :]
        l_max_conf = max_conf[i, argwhere]
        l_max_id = max_id[i, argwhere]
        l_conf_array = confs[i, argwhere, :]

        if len(output) == 4:
            l_var_array = var_array[i, argwhere, :]
            l_max_cls_stddev = cls_stddev[i, argwhere, :]

        bboxes = []
        confs_dist = []

        # nms for each class
        for j in range(num_classes):

            cls_argwhere = l_max_id == j
            ll_box_array = l_box_array[cls_argwhere, :]
            ll_max_conf = l_max_conf[cls_argwhere]
            ll_max_id = l_max_id[cls_argwhere]
            ll_conf_array = l_conf_array[cls_argwhere, :]

            if len(output) == 4:
                ll_var_array = l_var_array[cls_argwhere, :]
                ll_max_cls_stddev = l_max_cls_stddev[cls_argwhere, :]

            keep = nms_cpu(ll_box_array, ll_max_conf, nms_thresh)
            # keep = nms(torch.tensor(ll_box_array), torch.tensor(ll_max_conf), torch.tensor(nms_thresh))
            # keep = keep.cpu().detach().numpy()

            if (keep.size > 0):
                ll_box_array = ll_box_array[keep, :]
                ll_max_conf = ll_max_conf[keep]
                ll_max_id = ll_max_id[keep]

                ll_conf_array = ll_conf_array[keep, :]

                if len(output) == 4:
                    ll_var_array = l_var_array[keep, :]
                    ll_max_cls_stddev = ll_max_cls_stddev[keep, :]
                    ll_max_cls_stddev = np.max(ll_max_cls_stddev, axis=1)

                for k in range(ll_box_array.shape[0]):
                    if len(output) == 4:
                        bboxes.append([ll_box_array[k, 0], ll_box_array[k, 1], ll_box_array[k, 2], ll_box_array[k, 3],
                                       ll_max_conf[k], ll_max_id[k], ll_var_array[k, 0], ll_var_array[k, 1],
                                       ll_var_array[k, 2], ll_var_array[k, 3], ll_max_cls_stddev[k]])
                    else:
                        bboxes.append([ll_box_array[k, 0], ll_box_array[k, 1], ll_box_array[k, 2], ll_box_array[k, 3],
                                       ll_max_conf[k], ll_max_id[k]])

                    confs_dist.append(ll_conf_array[k, :])

        bboxes_batch.append(bboxes)
        confs_batch.append(confs_dist)

    t3 = time.time()

    return bboxes_batch, confs_batch
