import re

point_matcher = re.compile("([+-]?[0-9]+[.][0-9]+) ([+-]?[0-9]+[.][0-9]+)")


class Point(str):
    @property
    def match_point(self):
        if not hasattr(self, "match"):
            self.match = point_matcher.findall(self)
        return self.match[0]

    @property
    def x(self):
        return self.match_point[0]

    @property
    def y(self):
        return self.match_point[1]
