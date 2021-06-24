import json
from datetime import datetime

class Filter:

    def to_JSON(self):
        return self.__dict__

    @staticmethod
    def create(aim: str = None, left_top_bound: list = None, right_bottom_bound: list = None, max_age: int = None) -> 'Filter':
        filter = Filter()
        filter.Aim = aim
        if left_top_bound and right_bottom_bound:
            filter.Bounds = {"leftTop": left_top_bound, "RightBottom": right_bottom_bound}
        else:
            filter.Bounds = None

        filter.MaxAge = max_age

        return filter

class FilterEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Filter):
            return obj.to_JSON()

        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)
