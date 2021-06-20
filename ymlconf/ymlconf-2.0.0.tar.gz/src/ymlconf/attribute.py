#!/usr/bin/env python3

__all__ = [
    "Attribute",
]


class Attribute(object):
    def __set_name__(self, owner, name):
        self.name = name

    @classmethod
    def _check_and_format_value(cls, value):

        return value

    def __set__(self, instance, value):
        try:
            value = self._check_and_format_value(value)
        except Exception as e:
            raise AttributeError from e

        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self

        value = instance.__dict__.get(self.name, None)

        if value is None:
            instance.__dict__[self.name] = None

        return instance.__dict__[self.name]
