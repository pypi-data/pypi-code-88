# MIT License
#
# Copyright (c) 2021 Peter Goss
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""
    This is a simple string serialization-deserialization approach that should be mostly
    human readable but also extensible.

    Before an object can be serialized or deserialized a SerializationPair must be created
    and registered. (This, however has already been done for the following classes: None
    bool, int, float, datetime.date, datetime.time, datetime.datetime.)
    example:
        class MyClass: ... # assume some meaningful class definition
        def my_class_serializer(obj: MyClass) -> str: ... # assume some functional serialization
        def MyClassDeserializer(cls: type, string: str) -> MyClass: ... # assume this does the inverse of the above

        my_class_serialization_pair = SerializationPair(MyClass, my_class_serializer, my_class_deserializer)
        register_new_serialization_pair(my_class_serialization_pair)

    After the the SerializationPair has been registered you may now serialize and deserialize the objects
    of that type.
    example:
        my_obj = MyClass(creation_argument)
        cls_id, serialization_string = serialize(my_obj)
        ...
        # store away cls_id and serialization_string for later use
        ...
        re_created_my_obj = deserialize(cls_id, serialization_string)




"""
from typing import NamedTuple, Callable, Any, Dict, Tuple, Union, Type, cast
from datetime import datetime, date, time
from abc import ABCMeta


class SerializationError(Exception):
    """ An exception that indicates that serialization was not possible. """
    pass


class DeserializationError(Exception):
    """ An exception that indicates that deserialization was not possible. """
    pass


class ClassID(str):
    """ A simple subclass of str that is used to make type annotations a bit more clear. """
    pass


class SerializationPair(NamedTuple):
    """
        A SerializationPair is used to define 2 inverse functions ('serialize' and 'deserialize')
        that can be used to serialize and deserialize a particular class ('cls').
        ex:
            sp = SerializationPair(cls, serialize, deserialize)
    """
    cls: Any
    serialize: Callable[[Any], str]
    deserialize: Callable[[Type, str], Any]


def get_class_id(cls: Union[Type, object]) -> ClassID:
    """
        Generates a unique id for a class.
    """
    if type(cls) is type or type(cls) is ABCMeta:
        cls = cast(Type, cls)
        return ClassID(f'{cls.__module__}.{cls.__name__}')
    else:
        obj = cls
        return ClassID(f'{obj.__class__.__module__}.{obj.__class__.__name__}')


def basic_string_serializer(obj: Any) -> str:
    """
        A serializer that works for any class that produces a unique string (unique relative only
        to the class itself) for a particular object. (examples: None, bool, str, int, float)
    """
    return str(obj)


def basic_string_deserializer(cls: Type, string: str) -> Any:
    """
        A deserializer for any class that will take a string and produce a unique object from it.
        (examples: str, int, float)
    """
    return cls(string)


def none_string_deserializer(cls: Type, string: str) -> None:
    """A deserializer for None type. """
    if string == 'None':
        return None
    else:
        raise ValueError(f"Unknown None representation '{string}'")


def bool_string_deserializer(cls: Type, string: str) -> bool:
    """A deserializer for bool type. """
    if string == 'True':
        return True
    elif string == 'False':
        return False
    else:
        raise ValueError(f"Unknown boolean representation '{string}'")


def datetime_string_serializer(obj: Union[date, time, datetime]) -> str:
    """ A serializer for date, time and datetime objects. """
    return obj.isoformat()


def datetime_string_deserializer(cls: Type, string: str) -> Union[date, time, datetime]:
    """ A deserializer for date, time and datetime objects. """
    return cls.fromisoformat(string)


# dictionary of registered SerializationPairs
_SERIALIZATION_FUNCTIONS: Dict[ClassID, SerializationPair] = {}


def register_new_serialization_pair(serialization_pair: SerializationPair) -> None:
    """
        Used to add new serialization to the dictionary used to keep track of serialization pairs for various classes
    """
    _SERIALIZATION_FUNCTIONS[get_class_id(serialization_pair.cls)] = serialization_pair


# register default set of Serialization Pairs for Standard Library objects.
register_new_serialization_pair(SerializationPair(None, basic_string_serializer, none_string_deserializer))
register_new_serialization_pair(SerializationPair(str, basic_string_serializer, basic_string_deserializer))
register_new_serialization_pair(SerializationPair(bool, basic_string_serializer, bool_string_deserializer))
register_new_serialization_pair(SerializationPair(int, basic_string_serializer, basic_string_deserializer))
register_new_serialization_pair(SerializationPair(float, basic_string_serializer, basic_string_deserializer))
register_new_serialization_pair(SerializationPair(date, datetime_string_serializer, datetime_string_deserializer))
register_new_serialization_pair(SerializationPair(time, datetime_string_serializer, datetime_string_deserializer))
register_new_serialization_pair(SerializationPair(datetime, datetime_string_serializer, datetime_string_deserializer))


def serialize(obj:Any) -> Tuple[ClassID, str]:
    """ Serializes the given object into a class id and the serialized string of the object. """
    try:
        obj_cls_id = get_class_id(obj)
        serialized_obj = _SERIALIZATION_FUNCTIONS[obj_cls_id].serialize(obj)
        return obj_cls_id, serialized_obj
    except KeyError:
        raise SerializationError(f'attempt to serialize unknown object type {get_class_id(obj)}')


def deserialize(cls_id: ClassID, serialized_obj: str) -> Any:
    """ Takes a class id and a serialization string and returns the reconstituted object """
    try:
        cls = _SERIALIZATION_FUNCTIONS[cls_id].cls
        deserializer = _SERIALIZATION_FUNCTIONS[cls_id].deserialize
        return deserializer(cls, serialized_obj)
    except KeyError:
        raise DeserializationError(f'attempt to deserialize unknown object type {cls_id}')