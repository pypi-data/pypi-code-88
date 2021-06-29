"""
Objects representing AWS entities like Regions.
"""

import haversine
import json
import pkg_resources


class Region(object):
    """
    Represents an AWS region.
    """

    __slots__ = ("code", "lat", "long", "_closest_regions", "_closest_regions_unique")

    def __init__(self, code, lat, long):
        """
        Create a new AWS region object.

        :param code: the AWS region code i.e. us-east-1, eu-central-1, etc.
        :type code: str
        :param lat: the latitude coordinate
        :type lat: float
        :param long: the longitude coordinate
        :type long: float
        """
        self.code = code
        self.lat = lat
        self.long = long
        self._closest_regions = []  # type: list[tuple[Region, float]]
        self._closest_regions_unique = set()  # type: set[Region]

    @property
    def closest_regions(self):
        """
        Return a list of all AWS regions sorted by their geographic proximity to this region.
        Distance comparisons are performed using haversine module.

        :return: a list of AWS region codes starting with the closest region to this one
        :rtype: list[Region]
        """
        self._closest_regions.sort(key=lambda x: x[1])  # sort by the 2nd element which would be the distance
        return [region for region, distance in self._closest_regions]

    def add_region(self, other):
        """
        Add another Region object to this Region so it can be sorted into its proximity list.

        :param other:
        :type other: Region
        """
        if other in self._closest_regions_unique:
            # don't add if it's already in our list
            return
        # distance = haversine.haversine((self.lat, self.long), (other.lat, other.long))
        distance = self - other
        self._closest_regions.append((other, distance))
        self._closest_regions_unique.add(other)

    def remove_region(self, other):
        """
        Remove a region that was previously added to this Region for distance comparisons.

        :param other: the region to remove from comparison
        :type other: Region
        """
        for idx, region_distance in enumerate(self._closest_regions):
            if other == region_distance[0]:
                del self._closest_regions[idx]
                break
        self._closest_regions_unique.remove(other)

    def __eq__(self, other):
        if self is other:
            return True
        try:
            self.code == other.code
        except Exception:
            return False

    def __hash__(self):
        return hash(self.code)

    def __sub__(self, other):
        """
        When subtracting two regions, return their distance using haversine.

        :param other: another Region object is expected here to compare its distance from us
        :type other: Region
        :return: the distance between this Region and the other by comparing their coordinates
        :rtype: float
        """
        if self is other:
            return 0.0
        self_coords = (self.lat, self.long)
        other_coords = (other.lat, other.long)
        distance = haversine.haversine(self_coords, other_coords)

        return distance

    @classmethod
    def from_json_dict(cls, jdict):
        """
        Construct a Region object from a dictionary from aws-regions.json

        :param jdict: one dictionary from the list found in aws-regions.json
        :type jdict: dict
        :return: a new instance of Region with the code, latitude, and longitude taken from the given dict
        :rtype: Region
        """
        return cls(code=jdict["code"], lat=jdict["lat"], long=jdict["long"])

    def __str__(self):
        return '%s @ "%s,%s"' % (self.code, self.lat, self.long)

    def __repr__(self):
        return "Region(%s, %s, %s)" % (self.code, self.lat, self.long)


def _read_regions_from_file():
    """
    aws-regions.json was obtained from here:
    https://gist.github.com/atyachin/a011edf76df66c5aa1eac0cdca412ea9

    :return: list of Region objects
    :rtype: list[Region]
    """
    resource = pkg_resources.resource_filename('aws_region_proximity', 'aws-regions.json')
    with open(resource, "r", encoding="utf-8") as region_file:
        r = json.load(region_file)
    region_list = []
    for region in r:
        r_obj = Region.from_json_dict(region)
        region_list.append(r_obj)
    for r in region_list:  # add all regions to each others' lists
        for o in region_list:
            r.add_region(o)
    return region_list


regions = _read_regions_from_file()
