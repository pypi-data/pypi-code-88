import sys
import os
import time
import math
import torch
import numpy as np
from torch.autograd import Variable

import itertools
import struct  # get_image_size
import imghdr  # get_image_size

from yolo_ens_dist.utilz import utils



def get_region_boxes(boxes_and_confs):

    # print('Getting boxes from boxes and confs ...')

    boxes_list = []
    confs_list = []

    for item in boxes_and_confs:
        boxes_list.append(item[0])
        confs_list.append(item[1])

    # boxes: [batch, num1 + num2 + num3, 1, 4]
    # confs: [batch, num1 + num2 + num3, num_classes]
    boxes = torch.cat(boxes_list, dim=1)
    confs = torch.cat(confs_list, dim=1)

    return [boxes, confs]

def get_region_boxes_uncertainty(boxes_and_confs_and_sigmas):

    boxes_list = []
    confs_list = []
    sigmas_list = []
    cls_stddev_list = []

    for item in boxes_and_confs_and_sigmas:
        boxes_list.append(item[0])
        confs_list.append(item[1])
        sigmas_list.append(item[2])
        cls_stddev_list.append(item[3])

    boxes = torch.cat(boxes_list, dim=1)
    confs = torch.cat(confs_list, dim=1)
    sigmas = torch.cat(sigmas_list, dim=1)
    cls_stddev = torch.cat(cls_stddev_list, dim=1)

    return [boxes, confs, sigmas, cls_stddev]


def do_detect(model, img, conf_thresh, nms_thresh, uncertainties=False, use_cuda=1):
    model.eval()
    t0 = time.time()

    if type(img) == np.ndarray and len(img.shape) == 3:  # cv2 image
        img = torch.from_numpy(img.transpose(2, 0, 1)).float().div(255.0).unsqueeze(0)
    elif type(img) == np.ndarray and len(img.shape) == 4:
        img = torch.from_numpy(img.transpose(0, 3, 1, 2)).float().div(255.0)
    else:
        print("unknow image type")
        exit(-1)

    if use_cuda:
        img = img.cuda()
    img = torch.autograd.Variable(img)
    
    t1 = time.time()

    output = model(img)

    t2 = time.time()

    # print('-----------------------------------')
    # print('           Preprocess : %f' % (t1 - t0))
    # print('      Model Inference : %f' % (t2 - t1))
    # print('-----------------------------------')

    if uncertainties:
        return utils.post_processing_uncertainties(img, conf_thresh, nms_thresh, output)
    else:
        return utils.post_processing(img, conf_thresh, nms_thresh, output)

