#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" versionedclass.py
VersionedClass is an abstract class which has an associated version which can be used to compare against other
VersionedClasses. Typically, a base class for a version schema should directly inherit from VersionedClass then the
actual versions should inherit from that base class.
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
from baseobjects import BaseMeta

# Local Libraries #
from .version import Version
from .versionregistry import VersionRegistry


# Definitions #
# Classes #
class VersionedMeta(BaseMeta):
    """A Meta Class that can compare the specified version of the classes.

    Class Attributes:
        _VERSION_TYPE (:obj:`VersionType`): The type of version this object will be.
        VERSION (:obj:`Version`): The version of this class as a string.
    """
    _VERSION_TYPE = None
    VERSION = None

    # Methods
    # Comparison
    def __eq__(cls, other):
        """Expands on equals comparison to include comparing the version.

        Args:
            other (:obj:): The object to compare to this class.

        Returns:
            bool: True if the other object is equivalent to this class, including version.

        Raises:
            TypeError: If 'other' is a type that cannot be compared to.
        """
        if isinstance(other, type(cls)):
            if cls._VERSION_TYPE != other._VERSION_TYPE:
                raise TypeError(f"'==' not supported between instances of '{str(cls)}' and '{str(other)}'")
            other_version = other.VERSION
        elif isinstance(other, Version):
            other_version = other
        else:
            other_version = cls.VERSION.cast(other)

        if isinstance(other_version, type(cls.VERSION)):
            return cls.VERSION == other_version
        else:
            raise TypeError(f"'==' not supported between instances of '{str(cls)}' and '{str(other)}'")

    def __ne__(cls, other):
        """Expands on not equals comparison to include comparing the version.

        Args:
            other (:obj:): The object to compare to this class.

        Returns:
            bool: True if the other object is not equivalent to this class, including version number.

        Raises:
            TypeError: If 'other' is a type that cannot be compared to.
        """
        if isinstance(other, type(cls)):
            if cls._VERSION_TYPE != other._VERSION_TYPE:
                raise TypeError(f"'!=' not supported between instances of '{str(cls)}' and '{str(other)}'")
            other_version = other.VERSION
        elif isinstance(other, Version):
            other_version = other
        else:
            other_version = cls.VERSION.cast(other)

        if isinstance(other_version, type(cls.VERSION)):
            return cls.VERSION != other_version
        else:
            raise TypeError(f"'!=' not supported between instances of '{str(cls)}' and '{str(other)}'")

    def __lt__(cls, other):
        """Creates the less than comparison which compares the version of this class.

        Args:
            other (:obj:): The object to compare to this class.

        Returns:
            bool: True if the this object is less than to the other classes' version.

        Raises:
            TypeError: If 'other' is a type that cannot be compared to.
        """
        if isinstance(other, type(cls)):
            if cls._VERSION_TYPE != other._VERSION_TYPE:
                raise TypeError(f"'<' not supported between instances of '{str(cls)}' and '{str(other)}'")
            other_version = other.VERSION
        elif isinstance(other, Version):
            other_version = other
        else:
            other_version = cls.VERSION.cast(other)

        if isinstance(other_version, type(cls.VERSION)):
            return cls.VERSION < other_version
        else:
            raise TypeError(f"'<' not supported between instances of '{str(cls)}' and '{str(other)}'")

    def __gt__(cls, other):
        """Creates the greater than comparison which compares the version of this class.

        Args:
            other (:obj:): The object to compare to this class.

        Returns:
            bool: True if the this object is greater than to the other classes' version.

        Raises:
            TypeError: If 'other' is a type that cannot be compared to.
        """
        if isinstance(other, type(cls)):
            if cls._VERSION_TYPE != other._VERSION_TYPE:
                raise TypeError(f"'>' not supported between instances of '{str(cls)}' and '{str(other)}'")
            other_version = other.VERSION
        elif isinstance(other, Version):
            other_version = other
        else:
            other_version = cls.VERSION.cast(other)

        if isinstance(other_version, type(cls.VERSION)):
            return cls.VERSION > other_version
        else:
            raise TypeError(f"'>' not supported between instances of '{str(cls)}' and '{str(other)}'")

    def __le__(cls, other):
        """Creates the less than or equal to comparison which compares the version of this class.

        Args:
            other (:obj:): The object to compare to this class.

        Returns:
            bool: True if the this object is less than or equal to the other classes' version.

        Raises:
            TypeError: If 'other' is a type that cannot be compared to.
        """
        if isinstance(other, type(cls)):
            if cls._VERSION_TYPE != other._VERSION_TYPE:
                raise TypeError(f"'<=' not supported between instances of '{str(cls)}' and '{str(other)}'")
            other_version = other.VERSION
        elif isinstance(other, Version):
            other_version = other
        else:
            other_version = cls.VERSION.cast(other)

        if isinstance(other_version, type(cls.VERSION)):
            return cls.VERSION <= other_version
        else:
            raise TypeError(f"'<=' not supported between instances of '{str(cls)}' and '{str(other)}'")

    def __ge__(cls, other):
        """Creates the greater than or equal to comparison which compares the version of this class.

        Args:
            other (:obj:): The object to compare to this class.

        Returns:
            bool: True if the this object is greater than or equal to the other classes' version.

        Raises:
            TypeError: If 'other' is a type that cannot be compared to.
        """
        if isinstance(other, type(cls)):
            if cls._VERSION_TYPE != other._VERSION_TYPE:
                raise TypeError(f"'>=' not supported between instances of '{str(cls)}' and '{str(other)}'")
            other_version = other.VERSION
        elif isinstance(other, Version):
            other_version = other
        else:
            other_version = cls.VERSION.cast(other)

        if isinstance(other_version, type(cls.VERSION)):
            return cls.VERSION <= other_version
        else:
            raise TypeError(f"'>=' not supported between instances of '{str(cls)}' and '{str(other)}'")


class VersionedClass(metaclass=VersionedMeta):
    """An abstract class allows child classes to specify its version which it can use to compare.

    Class Attributes:
        _registry (:obj:`VersionRegistry`): A registry of all subclasses and versions of this class.
        _registration (bool): Specifies if versions will tracked and will recurse to parent.
        _VERSION_TYPE (:obj:`VersionType`): The type of version this object will be.
        VERSION (:obj:`Version`): The version of this class as a string.
    """
    _registry = VersionRegistry()
    _registration = True
    _VERSION_TYPE = None
    VERSION = None

    # Class Methods
    # Construction/Destruction
    def __init_subclass__(cls, **kwargs):
        """Adds the future child classes to the registry upon class instantiation"""
        super().__init_subclass__(**kwargs)

        type_ = cls._VERSION_TYPE
        class_ = cls._VERSION_TYPE.class_

        if not isinstance(cls.VERSION, class_):
            cls.VERSION = class_(cls.VERSION)

        cls.VERSION.version_type = type_

        if cls._registration:
            cls._registry.add_item(cls, type_)

    @staticmethod
    def get_version_from_object(obj):
        """An optional abstract method that must return a version from an object."""
        raise NotImplementedError("This method needs to be defined in the subclass.")

    @classmethod
    def get_version_class(cls, version, type_=None, exact=False, sort=False):
        """Gets a class class based on the version.

        Args:
            version (str, list, tuple, :obj:`Version`): The key to search for the class with.
            type_ (str, optional): The type of class to get.
            exact (bool, optional): Determines whether the exact version is need or return the closest version.
            sort (bool, optional): If True, sorts the registry before getting the class.

        Returns:
            obj: The class found.
        """
        if type_ is None:
            type_ = cls._VERSION_TYPE

        if sort:
            cls._registry.sort(type_)

        if not isinstance(version, str) and not isinstance(version, list) and \
           not isinstance(version, tuple) and not isinstance(version, Version):
            version = cls.get_version_from_object(version)

        return cls._registry.get_version(type_, version, exact=exact)
