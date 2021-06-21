import numpy as np
import math
from . import BaseAnnotationDefinition


class RotationBox(BaseAnnotationDefinition):
    """
        Box annotation object
    """
    type = "box"

    def __init__(self, top_left, top_right, bottom_left, bottom_right, label, attributes=None, description=None):
        super().__init__(description=description)
        self.top_left = top_left
        self.top_right = top_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right
        self.label = label
        self.angle = math.atan2(top_right[1] - top_left[1], top_right[0] - top_left[0])
        if attributes is None:
            attributes = list()
        self.attributes = attributes

    @property
    def x(self):
        return [self.top_left[0], self.top_right[0], self.bottom_left[0], self.bottom_right[0]]

    @property
    def y(self):
        return [self.top_left[1], self.top_right[1], self.bottom_left[1], self.bottom_right[1]]

    @property
    def geo(self):
        return [
            self.top_left, self.bottom_left, self.bottom_right, self.top_right
        ]

    def show(self, image, thickness, with_text, height, width, annotation_format, color):
        """
        Show annotation as ndarray
        :param image: empty or image to draw on
        :param thickness:
        :param with_text: not required
        :param height: item height
        :param width: item width
        :param annotation_format: options: list(dl.ViewAnnotationOptions)
        :param color: color
        :return: ndarray
        """
        try:
            import cv2
        except ImportError:
            self.logger.error(
                'Import Error! Cant import cv2. Annotations operations will be limited. import manually and fix errors')
            raise

        if thickness is None:
            thickness = 2

        image = cv2.drawContours(
            image=image,
            contours=[np.round(self.geo).astype(int)],
            contourIdx=-1,
            color=color,
            thickness=thickness,
        )
        return image

    def to_coordinates(self, color):
        return [{"x": float(x), "y": float(y), "z": 0} for x, y in self.geo]

    @staticmethod
    def from_coordinates(coordinates):
        return np.asarray([[pt["x"], pt["y"]] for pt in coordinates])

    @classmethod
    def from_json(cls, _json):
        if "coordinates" in _json:
            geo = cls.from_coordinates(_json["coordinates"])
        elif "data" in _json:
            geo = cls.from_coordinates(_json["data"])
        else:
            raise ValueError('can not find "coordinates" or "data" in annotation. id: {}'.format(_json["id"]))
        top_left = geo[0]
        top_right = geo[1]
        bottom_left = geo[2]
        bottom_right = geo[3]

        attributes = _json.get("attributes", list())

        return cls(
            top_left=top_left,
            top_right=top_right,
            bottom_left=bottom_left,
            bottom_right=bottom_right,
            label=_json["label"],
            attributes=attributes,
        )
