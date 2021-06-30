from ..models import Coord2D, Detection, Resolution
from ..util import resize_image_batch
from typing import Callable, List
import numpy as np
import tensorflow as tf


def faster_r_cnn_inception_v2_coco(
        model_path: str,
        network_resolution: Resolution,
        original_resolution: Resolution,
        confidence_threshold: int = 0.5,
        classes_to_detect: List[int] = None
) -> Callable[[np.ndarray], List[List[Detection]]]:
    """
    Given a number of parameters, build's a function that takes a batch of images a return a batch of :class:`Detection`
    using the faster r cnn inception v2 object detector is built and returned.

    :param model_path: path to the tensorflow file containing the model and it's weights.
    :param network_resolution: the resolution that the images are going to have when going through the network.
    :param original_resolution: the original size of the images.
    :param confidence_threshold: the confidence threshold of a detection.
    :param classes_to_detect: the classes to detect.
    :return: a function that used the built yolo v3 model to detect objects in a batch o images.
    """

    if classes_to_detect is None:
        classes_to_detect = [i + 1 for i in range(90)]

    model = tf.saved_model.load(model_path).signatures["serving_default"]

    def _func(image_input: np.ndarray) -> List[List[Detection]]:
        detections = [[]]
        image_input = resize_image_batch(image_input, network_resolution)
        for image in image_input:
            output = model(tf.constant(image, tf.uint8))
            boxes, scores, classes, num_detections = \
                output["detection_boxes"].numpy()[0], \
                output["detection_scores"].numpy()[0], \
                output["detection_classes"].numpy()[0], \
                output["num_detections"].numpy()[0],
            detections.append([])
            for i in range(int(num_detections)):
                obj_class = int(classes[i])
                obj_score = scores[i]
                if obj_score >= confidence_threshold and obj_class in classes_to_detect:
                    xtl = boxes[i][1] * original_resolution.width
                    ytl = boxes[i][0] * original_resolution.height
                    xbr = boxes[i][3] * original_resolution.width
                    ybr = boxes[i][2] * original_resolution.height
                    detections[-1].append(Detection(
                        Coord2D(round(xtl), round(ytl)),
                        Coord2D(round(xbr), round(ybr)),
                        obj_score,
                    ))
        return detections

    return _func
