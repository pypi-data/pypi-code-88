from ..models import Resolution, Detection, Coord2D
from ..util import resize_image_batch

from typing import List, Callable, Tuple
import numpy as np
import tensorflow as tf


def yolo_v3(
        h5_model_file_path: str,
        yolo_v3_resolution: Resolution,
        original_resolution: Resolution,
        confidence_threshold: float = 0.7,
        iou_threshold: float = 0.5,
        classes_to_detect: List[int] = None,
        output_anchors: List[List[Tuple[int, int]]] = None,
) -> Callable[[np.ndarray], List[List[Detection]]]:
    """
    Given a number of parameters a function that takes a batch of images a return a batch of :class:`Detection` using
    the yolo v3 object detector is built and returned.

    :param h5_model_file_path: path to the h5 file containing the model and it's weights.
    :param yolo_v3_resolution: the resolution that the images are going to have when going through the network.
    :param original_resolution: the original size of the images.
    :param confidence_threshold: the confidence threshold of a detection.
    :param iou_threshold: the intersection over union threshold of the detections.
    :param classes_to_detect: the classes to detect.
    :param output_anchors: the output anchors of the network.
    :return: a function that used the built yolo v3 model to detect objects in a batch o images.
    """

    model = tf.keras.models.load_model(h5_model_file_path)

    if classes_to_detect is None:
        classes_to_detect = [x for x in range(80)]

    if output_anchors is None:
        output_anchors = [
            [(116, 90), (156, 198), (373, 326)],
            [(30, 61), (62, 45), (59, 119)],
            [(10, 13), (16, 30), (33, 23)],
        ]

    def _func(image_input: np.ndarray) -> List[List[Detection]]:
        image_input = resize_image_batch(image_input, yolo_v3_resolution)
        image_input = image_input / 255
        image_input = image_input.reshape((image_input.shape[0], *yolo_v3_resolution, 3))

        outputs = model.predict(image_input)
        handled_outputs = None
        for output, anchors in zip(outputs, output_anchors):
            result = _handle_output(output, yolo_v3_resolution, original_resolution, anchors)
            if handled_outputs is not None:
                handled_outputs = tf.concat([handled_outputs, result], axis=-2)
            else:
                handled_outputs = result
        handled_outputs = _nms(handled_outputs, confidence_threshold, iou_threshold)
        detections = _to_detections(handled_outputs, classes_to_detect)
        return detections
    return _func


def _handle_output(
        output: np.ndarray,
        yolo_v3_resolution: Resolution,
        original_resolution: Resolution,
        anchors: List[Tuple[int, int]],
) -> tf.Tensor:
    grid_resolution = Resolution(*output.shape[1:3])

    # 85 = 5 + len(coco_classes)
    output = tf.reshape(output, (-1, len(anchors) * grid_resolution.width * grid_resolution.height, 85))
    box_centers, box_shapes, box_confidence, classes_confidence = tf.split(output, (2, 2, 1, 80), axis=-1)

    stride = _stride(yolo_v3_resolution, grid_resolution)
    x_y_offset = _create_x_y_offset(grid_resolution, len(anchors))
    box_centers = (tf.nn.sigmoid(box_centers) + x_y_offset) * stride

    grid_anchors = _create_grid_anchors(grid_resolution, anchors)
    box_shapes = tf.exp(box_shapes) * grid_anchors

    box_confidence = tf.nn.sigmoid(box_confidence)

    classes_confidence = tf.nn.sigmoid(classes_confidence)

    center_x, center_y = tf.split(box_centers, (1, 1), axis=-1)
    width, height = tf.split(box_shapes, (1, 1), axis=-1)

    top_left_x = (center_x - width / 2) / yolo_v3_resolution.width * original_resolution.width
    top_left_y = (center_y - height / 2) / yolo_v3_resolution.height * original_resolution.height
    bottom_right_x = (center_x + width / 2) / yolo_v3_resolution.width * original_resolution.width
    bottom_right_y = (center_y + height / 2) / yolo_v3_resolution.height * original_resolution.height

    output = tf.concat(
        [top_left_x, top_left_y, bottom_right_x, bottom_right_y, box_confidence, classes_confidence],
        axis=-1
    )

    return output


def _create_x_y_offset(grid_resolution: Resolution, len_anchors: int) -> tf.Tensor:
    """
    Cria um tf.Tensor com o valor pelo qual cada detecção deve ser deslocada nos eixo X e Y de acordo com o tamanho do
    grid gerado (grid_resolution) e da quantidade de detecções que estão contidas em cada célula do grid (len_anchors).

    +----------------------------------------------+----------------------------------------------+
    |                       X                      |                       Y                      |
    +==============================================+==============================================+
    |                       0                      |                       0                      |
    +----------------------------------------------+----------------------------------------------+
    |                       0                      |                       0                      |
    +----------------------------------------------+----------------------------------------------+
    |                       1                      |                       0                      |
    +----------------------------------------------+----------------------------------------------+
    |                       1                      |                       1                      |
    +----------------------------------------------+----------------------------------------------+
    |                       2                      |                       1                      |
    +----------------------------------------------+----------------------------------------------+
    |                       2                      |                       1                      |
    +----------------------------------------------+----------------------------------------------+
    |                      ...                     |                      ...                     |
    +----------------------------------------------+----------------------------------------------+
    | (grid_width * grid_height * len_anchors) - 1 | (grid_width * grid_height * len_anchors) - 1 |
    +----------------------------------------------+----------------------------------------------+

    :param grid_resolution: a resolução (grid_width, grid_height) do grid de detecções gerado.
    :param len_anchors: a quantidade de detecções feitas em cada célula.
    :return: um 2 x grid_width * grid_height com os valores que cada detecção deve ser deslocada nos eixos X e Y
    respectivamente.
    """
    grid_width, grid_height = grid_resolution
    x = tf.range(grid_width, dtype=tf.float32)
    y = tf.range(grid_height, dtype=tf.float32)
    x_offset, y_offset = tf.meshgrid(x, y)
    x_offset = tf.reshape(x_offset, (-1, 1))
    y_offset = tf.reshape(y_offset, (-1, 1))
    x_y_offset = tf.concat([x_offset, y_offset], axis=-1)
    x_y_offset = tf.tile(x_y_offset, [1, len_anchors])
    x_y_offset = tf.reshape(x_y_offset, [1, -1, 2])
    return x_y_offset


def _stride(yolo_v3_resolution: Resolution, grid_resolution: Resolution) -> Tuple[float, float]:
    """
    A escala pela qual a imagem original utilizada no modelo está em relação ao grid gerado com as detecções.
    :param yolo_v3_resolution: resolução original da imagem utilizada no modelo.
    :param grid_resolution: resolução do grid de saida das detecções resultates da imagem original.
    :return: escala pela qual a imagem original utilizada no modelo está em relação ao grid gerado com as detecções.
    """
    yolo_width, yolo_height = yolo_v3_resolution
    grid_width, grid_height = grid_resolution
    return yolo_width / grid_width, yolo_height / grid_height


def _create_grid_anchors(grid_resolution: Resolution, anchors: List[Tuple[int, int]]) -> tf.Tensor:
    """
    Cria um tf.Tensor com as ancoras para serem utilizadas junto com as detecções encontradas no grid gerado pelo
    modelo. Esse tf.Tensor possui a dimensão 2 x grid_width * grid_height e possui as ancoras repetidamente uma atrás da
    outra na dimensão 1.

    +--------------------------+--------------------------+
    |            X             |            Y             |
    +==========================+==========================+
    |           a0.x           |           a0.y           |
    +--------------------------+--------------------------+
    |           a1.x           |           a1.y           |
    +--------------------------+--------------------------+
    |           a2.x           |           a2.y           |
    +--------------------------+--------------------------+
    |           a0.x           |           a0.y           |
    +--------------------------+--------------------------+
    |           a1.x           |           a1.y           |
    +--------------------------+--------------------------+
    |           a2.x           |           a2.y           |
    +--------------------------+--------------------------+
    |           a0.x           |           a0.y           |
    +--------------------------+--------------------------+
    |           a1.x           |           a1.y           |
    +--------------------------+--------------------------+
    |           a2.x           |           a2.y           |
    +--------------------------+--------------------------+
    |           ...            |           ...            |
    +--------------------------+--------------------------+
    | grid_width * grid_height | grid_width * grid_height |
    +--------------------------+--------------------------+

    :param grid_resolution: o tamanho do grid gerado pelo modelo que será usado para criar o tf.Tensor com as ancoras.
    :param anchors: as ancoras utilizadas para o grid gerado.
    :return: um tf.Tensor com as ancoras utilizadas para ajustas as dimensões das detecções.
    """
    grid_width, grid_height = grid_resolution
    grid_anchors = tf.tile(anchors, [grid_width * grid_height, 1])
    return tf.cast(grid_anchors, dtype=tf.float32)


def _nms(output: tf.Tensor, confidence_threshold: float, iou_threshold: float) -> List[List[List[float]]]:
    result = []
    for image_detections in tf.unstack(output):
        current_image_detections = []
        result.append(current_image_detections)
        image_detections = tf.boolean_mask(image_detections, image_detections[:, 4] > confidence_threshold)
        classes = tf.argmax(image_detections[:, 5:], axis=-1)
        classes = tf.expand_dims(tf.cast(classes, dtype=tf.float32), axis=-1)
        image_detections = tf.concat([image_detections[:, :5], classes], axis=-1)
        for cls in range(80):
            mask = tf.equal(image_detections[:, 5], cls)
            mask_shape = mask.get_shape()
            if mask_shape.ndims != 0:
                class_boxes = tf.boolean_mask(image_detections, mask)
                boxes_coords, boxes_conf_scores, _ = tf.split(class_boxes, [4, 1, -1], axis=-1)
                boxes_conf_scores = tf.reshape(boxes_conf_scores, [-1])
                indices = tf.image.non_max_suppression(boxes_coords, boxes_conf_scores, 10, iou_threshold)
                class_boxes = tf.gather(class_boxes, indices)
                if class_boxes.shape[0] > 0:
                    current_image_detection = np.array(class_boxes[:, :5])
                    current_image_detection = np.append(current_image_detection, cls)
                    current_image_detections.append(current_image_detection.tolist())
    return result


def _to_detections(output: List[List[List[float]]], classes_to_detect: List[int]) -> List[List[Detection]]:
    frames = []
    for i in range(len(output)):
        image_detections = output[i]
        detections = []
        for image_detection in image_detections:
            if image_detection[5] in classes_to_detect:
                detections.append(Detection(
                    Coord2D(round(image_detection[0]), round(image_detection[1])),
                    Coord2D(round(image_detection[2]), round(image_detection[3])),
                    image_detection[4],
                ))
        frames.append(detections)
    return frames
