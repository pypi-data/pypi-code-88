#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" trinumberversion.py
TriNumberVersion is a versioning system which is defined by three numbers. This class does not enforce any special
meaning of the three number, but the Major number is more significant than the Moderate number which is more
significant than the Minor number. A good example of the tri-number framework can be found at https://semver.org/
"""
__author__ = "Anthony Fong"
__copyright__ = "Copyright 2021, Anthony Fong"
__credits__ = ["Anthony Fong"]
__license__ = ""
__version__ = "0.1.0"
__maintainer__ = "Anthony Fong"
__email__ = ""
__status__ = "Prototype"

# Default Libraries #

# Downloaded Libraries #

# Local Libraries #
from ..version import Version


# Definitions #
# Classes #
class TriNumberVersion(Version):
    """A dataclass like class that stores and handles a version number.

    Args:
        obj (int, str, :obj:`list`, :obj:`tuple`, optional): An object to derive a version from.
        major (int, optional):The major change number of the version.
        moderate (int, optional): The moderate change number of the version.
        minor (int, optional), optional: The minor change number of the version.
        ver_name (str, optional): The name of the version type being used.

    Attributes:
        major (int): The major change number of the version.
        moderate (int): The moderate change number of the version.
        minor (int): The minor change number of the version.
    """
    default_version_name = "TriNumber"
    __slots__ = ["major", "moderate", "minor"]

    # Construction/Destruction
    def __init__(self, obj=None, major=0, moderate=0, minor=0, ver_name=None, init=True):
        super().__init__(init=False)
        self.major = major
        self.moderate = moderate
        self.minor = minor

        if init:
            self.construct(obj, moderate, minor, major, ver_name)

    # Type Conversion
    def __str__(self):
        """Returns the str representation of the version.

        Returns:
            str: A str with the version numbers in order.
        """
        return f"{self.major}.{self.moderate}.{self.minor}"

    # Comparison
    def __eq__(self, other):
        """Expands on equals comparison to include comparing the version number.

        Args:
            other (:obj:): The object to compare to this object.

        Returns:
            bool: True if the other object or version number is equivalent.
        """
        other = self.cast(other, pass_=True)

        if isinstance(other, type(self)):
            return self.tuple() == other.tuple()
        elif "VERSION" in other.__dict__:
            return self.tuple() == other.VERSION.tuple()  # Todo: Maybe change the order to be cast friendly
        else:
            return super().__eq__(other)

    def __ne__(self, other):
        """Expands on not equals comparison to include comparing the version number.

        Args:
            other (:obj:): The object to compare to this object.

        Returns:
            bool: True if the other object or version number is not equivalent.
        """
        other = self.cast(other, pass_=True)

        if isinstance(other, type(self)):
            return self.tuple() != other.tuple()
        elif "VERSION" in other.__dict__:
            return self.tuple() != other.VERSION.tuple()
        else:
            return super().__ne__(other)

    def __lt__(self, other):
        """Creates the less than comparison for these objects which includes str, list, and tuple.

        Args:
            other (:obj:): The object to compare to this object.

        Returns:
            bool: True if this object is less than to the other objects' version number.

        Raises:
            TypeError: If 'other' is a type that cannot be compared to.
        """
        other = self.cast(other, pass_=True)

        if isinstance(other, type(self)):
            return self.tuple() < other.tuple()
        elif "VERSION" in other.__dict__:
            return self.tuple() < other.VERSION.tuple()
        else:
            raise TypeError(f"'>' not supported between instances of '{str(self)}' and '{str(other)}'")

    def __gt__(self, other):
        """Creates the greater than comparison for these objects which includes str, list, and tuple.

        Args:
            other (:obj:): The object to compare to this object.

        Returns:
            bool: True if this object is greater than to the other objects' version number.

        Raises:
            TypeError: If 'other' is a type that cannot be compared to.
        """
        other = self.cast(other, pass_=True)

        if isinstance(other, type(self)):
            return self.tuple() > other.tuple()
        elif "VERSION" in other.__dict__:
            return self.tuple() > other.VERSION.tuple()
        else:
            raise TypeError(f"'>' not supported between instances of '{str(self)}' and '{str(other)}'")

    def __le__(self, other):
        """Creates the less than or equal to comparison for these objects which includes str, list, and tuple.

        Args:
            other (:obj:): The object to compare to this object.

        Returns:
            bool: True if this object is less than or equal to to the other objects' version number.

        Raises:
            TypeError: If 'other' is a type that cannot be compared to.
        """
        other = self.cast(other, pass_=True)

        if isinstance(other, type(self)):
            return self.tuple() <= other.tuple()
        elif "VERSION" in other.__dict__:
            return self.tuple() <= other.VERSION.tuple()
        else:
            raise TypeError(f"'<=' not supported between instances of '{str(self)}' and '{str(other)}'")

    def __ge__(self, other):
        """Creates the greater than or equal to comparison for these objects which includes str, list, and tuple.

        Args:
            other (:obj:): The object to compare to this object.

        Returns:
            bool: True if this object is greater than or equal to to the other objects' version number.

        Raises:
            TypeError: If 'other' is a type that cannot be compared to.
        """
        other = self.cast(other, pass_=True)

        if isinstance(other, type(self)):
            return self.tuple() >= other.tuple()
        elif "VERSION" in other.__dict__:
            return self.tuple() >= other.VERSION.tuple()
        else:
            raise TypeError(f"'>=' not supported between instances of '{str(self)}' and '{str(other)}'")

    # Methods
    def construct(self, obj=None, moderate=0, minor=0, major=0, ver_name=None):
        """Constructs the version object based on inputs

        Args:
            obj (:obj:, optional): An object to derive a version from.
            major (int, optional):The major change number of the version.
            moderate (int, optional): The moderate change number of the version.
            minor (int, optional), optional: The minor change number of the version.
            ver_name (str, optional): The name of the version type being used.
        """
        if isinstance(obj, str):
            ranks = obj.split('.')
            for i, r in enumerate(ranks):
                ranks[i] = int(r)
            major, moderate, minor = ranks
        elif isinstance(obj, list) or isinstance(obj, tuple):
            major, moderate, minor = obj
        elif isinstance(obj, int):
            major = obj
        elif obj is not None:
            raise TypeError("Can't create {} from {}".format(self, major))

        self.major = major
        self.moderate = moderate
        self.minor = minor

        super().construct(ver_name)

    def list(self):
        """Returns the list representation of the version.

        Returns:
            :obj:`list` of :obj:`str`: A list with the version numbers in order.
        """
        return [self.major, self.moderate, self.minor]

    def tuple(self):
        """Returns the tuple representation of the version.

        Returns:
            :obj:`tuple` of :obj:`str`: A tuple with the version numbers in order.
        """
        return self.major, self.moderate, self.minor

    def str(self):
        """Returns the str representation of the version.

        Returns:
            str: A str with the version numbers in order.
        """
        return str(self)
