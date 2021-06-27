import itertools
from enum import Enum


def inherit_attribute(name, f):
    def decorator(cls):
        old_value = getattr(cls, name)
        new_value = f([getattr(base, name) for base in cls.__bases__ if hasattr(base, name)], old_value)
        setattr(cls, name, new_value)
        return cls
    return decorator

def merge_class_val(base_values, my_value = []):
    chain_object = itertools.chain.from_iterable(base_values)
    return list(chain_object) + my_value

def merge_inheritance(name):
    return inherit_attribute(name, merge_class_val)

class CaseInsensitiveEnum(Enum):
    @classmethod
    def _missing_(cls, value):
        for member in cls:
            if member.name.upper() == value.upper():
                return member
        super()._missing_(cls, value)