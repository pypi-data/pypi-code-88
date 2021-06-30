import os
import cv2
import numpy as np
from Yolov4Detector import darknet
from Yolov4Detector.utils import scale_coords

base_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'cfgs')
default_cfg_fp = os.path.join(base_dir, 'yolov4_tiny', 'yolov4-tiny.cfg')
default_weights_fp = os.path.join(base_dir, 'yolov4_tiny', 'yolov4-tiny.weights')
default_names_fp = os.path.join(base_dir, 'yolov4_tiny', 'coco.names')

class Detector():
    def __init__(self, cfg_fp=default_cfg_fp, names_fp=default_names_fp, weights_fp=default_weights_fp, batch_size=1):
        # write data fp
        temp_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'cfgs') 
        if not os.path.exists(temp_dir):
            os.mkdir(temp_dir)
        data_fp = os.path.join(temp_dir, 'temp.data')

        with open(names_fp, 'r') as f:
            classes = len([line for line in f if line.strip() != ""])

        with open(data_fp, 'w') as f:
            f.write("classes = " + str(classes) + "\n")
            f.write("names = " + names_fp + "\n")

        # init darknet
        self.network, self.class_names, _ = darknet.load_network(
            cfg_fp,
            data_fp,
            weights_fp,
            batch_size=batch_size
        )

    def detect(self, image_bgr, conf_thres=0.5, iou_thres=0.6):
        """
        conf_thres: for confidence filtering
        iou_thres: for nms

        Reture
        boexes: list of (x_min, y_min, x_max, y_max)
        """
        width, height, detections = darknet.detect_image(self.network, self.class_names, image_bgr, thresh=conf_thres, nms=iou_thres)
        
        # formating the detections results
        boxes, confs, clses = [], [], []
        if len(detections) > 0:
            for cls, conf, box in detections:
                boxes.append(darknet.bbox2points(box))
                confs.append(float(conf))
                clses.append(cls)
            boxes = scale_coords((height, width), np.array(boxes), image_bgr.shape[:2]).round()
        return boxes, np.array(confs), np.array(clses)


    def detect_batch(self, images_bgr, conf_thres=0.5, iou_thres=0.6, batch_size=4):
        steps = len(images_bgr) // batch_size
        less = len(images_bgr) % batch_size
        predictions = []
        for step in range(steps):
            st = step * batch_size
            width, height, batch_predictions = darknet.detect_one_batch(self.network, self.class_names, images_bgr[st:st+batch_size], batch_size=batch_size, thresh=conf_thres, nms=iou_thres)
            predictions.extend(batch_predictions)

        if less > 0:
            width, height, batch_predictions = darknet.detect_one_batch(self.network, self.class_names, images_bgr[-less:], batch_size=less, thresh=conf_thres, nms=iou_thres)
            predictions.extend(batch_predictions)

        # formating the detections results
        row_preds = []
        for row_idx, detections in enumerate(predictions):
            boxes, confs, clses = [], [], []
            if len(detections) > 0:
                for cls, conf, box in detections:
                    boxes.append(darknet.bbox2points(box))
                    confs.append(float(conf))
                    clses.append(cls)
                boxes = scale_coords((height, width), np.array(boxes), images_bgr[row_idx].shape[:2]).round()
            row_preds.append((boxes, confs, clses))
        return row_preds



