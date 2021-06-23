import datetime
import inspect
import json
from typing import Dict, Iterable, Callable, Union

import pysolr

from .exceptions import PySolaarConfigurationError


class DocumentFields(dict):
    def __init__(self, **kwargs):
        dict.__init__(self, **kwargs)


class BaseMeta:
    pysolaar_type: str
    fields_and_types: Dict = {}
    transforms: Dict = {}
    child_fields_and_types: Dict = {}
    child_transforms: Dict = {}

    default_search_field: str = "text"
    fields_as_json: Iterable = set()
    fields_as_child_docs: Iterable = set()
    output_transformations: Dict[str, Callable] = {}
    store_document_fields: DocumentFields = DocumentFields()

    def __init_subclass__(cls) -> None:
        # print(">>", cls.__dict__)
        cls.fields_and_types = _fields_from_meta_return_document_fields(cls)
        cls.transforms = _unpack_transforms(cls.fields_and_types)

        cls.child_fields_and_types = {
            k: _fields_from_meta_return_document_fields(return_document_fields=v)
            for k, v in cls.fields_and_types.items()
            if isinstance(v, ChildDocument)
        }
        cls.child_transforms = {
            k: _unpack_transforms(v) for k, v in cls.child_fields_and_types.items()
        }


def is_transform(t):
    return isinstance(t, Transform) or (inspect.isclass(t) and issubclass(t, Transform))


def _unpack_transforms(fields_and_types):
    transforms = {k: t for k, t in fields_and_types.items() if is_transform(t)}
    return transforms


class AndOnClass(type):
    transform_function = None

    def __and__(cls, right):
        if not is_transform(right):
            raise PySolaarConfigurationError(
                "Transform classes can only be confined with other Transform classes"
            )

        def combined_transform_func(key, value):
            key, value = cls.transform_function(key, value)
            key, value = right.transform_function(key, value)
            return key, value

        return Transform(combined_transform_func)


class ChildDocument(DocumentFields):
    transform_function: Union[Callable, None] = None

    def __and__(self, right):
        if not is_transform(right):
            raise PySolaarConfigurationError(
                "Transform classes can only be confined with other Transform classes"
            )

        if not self.transform_function:
            self.transform_function = right.transform_function

        else:
            tf = self.transform_function

            def f(key, value):
                key, value = tf(key, value)
                key, value = right.transform_function(key, value)
                return key, value

            self.transform_function = f

        return self


class JsonChildDocument(ChildDocument):
    pass


class SplattedChildDocument(ChildDocument):
    pass


# AsDict is **not** a transform but a DocumentFields type
class AsDict(DocumentFields):
    pass


def is_transform(t):
    return isinstance(t, Transform) or (inspect.isclass(t) and issubclass(t, Transform))


class Transform(metaclass=AndOnClass):
    """Provide a function to transform a key/value pair,
    returning a (key, value) tuple

    E.g. lambda key, value: (key, value.upper())

    Set raise_error to False to return the original key/value
    pair instead of throwing an error.
    """

    __slots__ = "tf", "raise_error"

    def __init__(self, tf, raise_error=True):
        self.tf = tf

    def transform_function(self, key, value):
        return self.tf(key, value)

    def __and__(self, right):
        if not is_transform(right):
            raise PySolaarConfigurationError(
                "Transform classes can only be confined with other Transform classes"
            )

        def combined_transform_func(key, value):
            key, value = self.transform_function(key, value)
            key, value = right.transform_function(key, value)
            return key, value

        return Transform(combined_transform_func)


class SingleValue(Transform):
    """When a field is expected to contain a single value, automatically unpack it
    instead of returning a list of length 1."""

    def __init__(self):
        pass

    @staticmethod
    def transform_function(key, l):
        # If for some reason this is mis-combined such that it's passed a string
        # we want to just return the value, not the first letter of the value!
        if type(l) is not list:
            return key, l
        # Otherwise just return first value of list
        return key, l[0]


class AsDateTime(Transform):
    def __init__(self):
        pass

    @staticmethod
    def transform_function(key, l):
        value = l[0]
        possible_datetime = pysolr.DATETIME_REGEX.search(value)
        if possible_datetime:
            date_values = possible_datetime.groupdict()

            for dk, dv in date_values.items():
                date_values[dk] = int(dv)

            value = datetime.datetime(
                date_values["year"],
                date_values["month"],
                date_values["day"],
                date_values["hour"],
                date_values["minute"],
                date_values["second"],
            )
        return key, value


def recursive_unjson(j, transforms={}):
    try:
        block = json.loads(j)
    except:
        block = j
    if isinstance(block, list):
        return [recursive_unjson(i, transforms=transforms) for i in block]
    if isinstance(block, dict):
        new_block = {}

        for k, v in block.items():
            if isinstance(transforms, dict) and k in transforms:

                new_key, new_value = transforms[k].transform_function(
                    k, recursive_unjson(v, transforms=transforms[k])
                )
                new_block[new_key] = new_value
            else:
                new_block[k] = recursive_unjson(v)
        return new_block
    return block


class JsonToDict(Transform):
    """Convert a field stored as JSON in Solr into a Python dict. Specify field
    transformations as arguments."""

    def __init__(self, **kwargs):
        self.transforms = kwargs
        self.transform_function = self.tf

    # A field declared as JSON will have a single value, but be returned
    # from Solr as a list; so we need to take the first value from list
    # to call json.loads on
    def tf(self, key, value):
        return (key, recursive_unjson(value[0], transforms=self.transforms))

    transform_function = staticmethod(lambda k, v: (k, recursive_unjson(v[0])))


class TransformKey(Transform):
    """Provide a function to transform the name of the key
    if required, or provide a string to simply rename the key.

    E.g. lambda key: key.upper()

    Set raise_error to False to return the original key
    instead of throwing an error.
    """

    def __init__(self, func):
        if isinstance(func, str):
            self.tf = lambda k: func
        else:
            self.tf = func

    # The goal is to tweak each Transform function so that it takes
    # two values, but only modifies the right one...
    def transform_function(self, key, value):
        return (self.tf(key), value)


class TransformValues(Transform):
    """Provide a function to transform the value of a field.

    E.g. lambda value: value.upper()

    Set raise_error to False to return the original value
    instead of throwing an error.
    """

    def transform_function(self, key, value):
        return key, [self.tf(v) for v in value]


def _fields_from_meta_return_document_fields(meta=None, return_document_fields=None):
    """Unpacks all the return-field declarations from a Meta class into a dict
    of key and type/transform mappings. Also, because used too widely, can take
    return_document_fields directly, for child doc handling (avoids having to
    re-nest in a Meta class for no reason.

    Eventually, this should be called once for each class from its Meta class on
    subclassing ... thereby saving all this runtime (return-time) work."""

    def unpack(field_key_value_dict, key="", acc={}):
        for k, v in field_key_value_dict.items():
            if type(v) is not AsDict:
                if key:
                    acc[f"{key}__{k}"] = v
                else:
                    acc[k] = v
            else:
                nk = f"{key}__{k}" if key else k
                r = unpack(v, key=nk, acc=acc)
                acc = {**acc, **r}
        return acc

    if meta and hasattr(meta, "return_document_fields"):
        return unpack(meta.return_document_fields)
    elif return_document_fields:
        return unpack(return_document_fields)
    else:
        return {}
