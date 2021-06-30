import math
from typing import Callable, List, Any
import numpy as np
import skimage.transform
import tensorflow as tf

from . import nn_matching
from ...models import Detection, TrackedDetection, Coord2D
from .track import Track
from .tracker import Tracker
from .tracking_detection import TrackingDetection


def deep_sort(
        feature_descriptor_model_path: str,
        matching_metric: str = "cosine",
        matching_metric_threshold: float = 0.2,
        matching_metric_budget: Any = None,
) -> Callable[[np.ndarray, List[Detection]], List[TrackedDetection]]:
    """
    Given the parameters, build's a function that uses the original implementation of the deep sort object tracking
    algorithm to take a frame and a list of detection to build a list of tracked detections.
    :param feature_descriptor_model_path: the path to the feature descriptor model.
    :param matching_metric: a matching metric (cosine or euclidean).
    :param matching_metric_threshold: a matching threshold.
    :param matching_metric_budget: a matching budget.
    :return: a function that uses the original implementation of the deep sort object tracking algorithm to take a frame
             and a list of detection to build a list of tracked detections.
    """

    metric = nn_matching.NearestNeighborDistanceMetric(
        matching_metric,
        matching_metric_threshold,
        matching_metric_budget
    )
    tracker = Tracker(metric)

    feature_descriptor = tf.saved_model.load(feature_descriptor_model_path) \
        .signatures["serving_default"]

    def _func(frame: np.ndarray, detections: List[Detection]) -> List[TrackedDetection]:
        tracking_detections = []
        for detection in detections:
            try:
                detection_area = frame[round(detection.p0.y): round(detection.p0.y + (detection.p1.y - detection.p0.y)),
                                       round(detection.p0.x): round(detection.p0.x + (detection.p1.x - detection.p0.x))]
                detection_area = skimage.transform.resize(detection_area, (128, 64))
                detection_area = detection_area.reshape((1, 128, 64, 3))
                description = feature_descriptor(tf.constant(detection_area, tf.uint8))
                description = description['out'].numpy()[0]
                tlwh = _tlrb_to_tlwh(np.array([detection.p0.x, detection.p0.y, detection.p1.x, detection.p1.y]))
                tracking_detection = TrackingDetection(tlwh, detection.confidence, description)
                tracking_detections.append(tracking_detection)
            except:
                pass
        tracker.predict()
        tracker.update(tracking_detections)
        return _tracks_to_tracking_detections(tracker.tracks)

    return _func


def _tracks_to_tracking_detections(tracks: List[Track]) -> List[TrackedDetection]:
    result = []
    for track in tracks:
        if track.is_confirmed():
            tlbr = track.to_tlbr()
            result.append(TrackedDetection(
                p0=Coord2D(tlbr[0], tlbr[1]),
                p1=Coord2D(tlbr[2], tlbr[3]),
                track_id=str(track.track_id),
                confidence=math.inf,
            ))
    return result


def _tlrb_to_tlwh(x):
    """
    top-left x, top-left y, right-bottom x, right-bottom y

    to

    top left x, top left y, width, height
    """
    y = np.zeros(x.shape)
    y[..., 0] = x[..., 0]
    y[..., 1] = x[..., 1]
    y[..., 2] = x[..., 2] - x[..., 0]
    y[..., 3] = x[..., 3] - x[..., 1]
    return y

