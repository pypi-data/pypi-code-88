from .models import Detection, Coord2D, TrackedDetection
from .util import to_middle_bottom_part
from typing import Callable, List, Union
import numpy as np


def create_method(
    detector: Callable[[np.ndarray], List[List[Detection]]],
    coord_mapper: Callable[[Coord2D], Coord2D],
    tracker: Callable[[Detection], TrackedDetection] = None,
) -> Union[
    Callable[[np.ndarray], List[List[Coord2D]]],
    Callable[[np.ndarray], List[List[Coord2D]]],
]:
    """
    Create the mapping method given the necessary established steps.
    :param detector: the detector that is going to be used.
    :param coord_mapper: the coord mapper that is going to be used.
    :param tracker: the tracker that is going to be used (optional).
    :return: a function that given a frame batch, returns the mapped coordinates of each frame based on the provided
             steps.
    """

    def _func(batch: np.ndarray) -> List[List[Coord2D]]:
        frames = detector(batch)
        result = []
        for detections in frames:
            result.append([])
            for detection in detections:
                result[-1].append(coord_mapper(to_middle_bottom_part(tracker(detection))))
        return result

    return _func
