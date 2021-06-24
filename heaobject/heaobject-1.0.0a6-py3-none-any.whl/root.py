import json
from datetime import datetime, date
from heaobject.error import DeserializeException
from heaobject import user
from enum import Enum, auto
from typing import Optional, List, Union, Mapping, Any, Type, Iterator, Iterable, Callable, Generic, TypeVar
import dateutil.parser
import importlib
import copy
import inspect
import abc


class _AutoName(Enum):
    """
    Subclass of Enum in which auto() returns the name as a string.
    """
    def _generate_next_value_(name, start, count, last_values):
        return name


class Permission(_AutoName):
    """
    The standard permissions that apply to all items in HEA.
    """
    VIEWER = auto()
    EDITOR = auto()
    COOWNER = auto()
    EXECUTOR = auto()
    SHARER = auto()

    def __str__(self) -> str:
        return self.name


class HEAObject(abc.ABC):
    """
    Interface for all HEA objects.

    All subclasses of HEAObject must have a zero-argument constructor.

    All non-callable instance members will be included in the to_dict() and json_dumps() methods.

    Copies and deep copies using the copy module will copy all non-callable instance members of any subclass of
    HEAObject. Override __copy__ and __deepcopy__ to change that behavior.
    """

    @property # type: ignore
    @abc.abstractmethod
    def id(self) -> Optional[str]:
        """
        The object's resource unique identifier. It must be unique among all objects of the same type.
        """
        pass

    @id.setter # type: ignore
    @abc.abstractmethod
    def id(self, id_: Optional[str]) -> None:
        pass

    @property # type: ignore
    @abc.abstractmethod
    def source(self) -> Optional[str]:
        """
        The id of a Source object representing this object's source.
        """
        pass

    @source.setter # type: ignore
    @abc.abstractmethod
    def source(self, source: Optional[str]) -> Optional[str]:
        pass

    @property # type: ignore
    @abc.abstractmethod
    def version(self) -> Optional[str]:
        """
        The version of this object.
        """
        pass

    @version.setter # type: ignore
    @abc.abstractmethod
    def version(self, version: Optional[str]) -> Optional[str]:
        pass

    @property # type: ignore
    @abc.abstractmethod
    def name(self) -> Optional[str]:
        """
        This object's name. If specified, the name must be unique across all objects of the same type.
        """
        pass

    @name.setter # type: ignore
    @abc.abstractmethod
    def name(self, name: Optional[str]) -> Optional[str]:
        pass

    @property # type: ignore
    @abc.abstractmethod
    def display_name(self) -> Optional[str]:
        """
        The object's display name. The default value is the object's name.
        """
        pass

    @display_name.setter # type: ignore
    @abc.abstractmethod
    def display_name(self, display_name: Optional[str]) -> Optional[str]:
        pass

    @property # type: ignore
    @abc.abstractmethod
    def description(self) -> Optional[str]:
        """
        The object's description.
        """
        pass

    @name.setter # type: ignore
    @abc.abstractmethod
    def description(self, description: Optional[str]) -> Optional[str]:
        pass

    @property # type: ignore
    @abc.abstractmethod
    def owner(self) -> str:
        """
        The username of the object's owner. Cannot be None.
        """
        pass

    @owner.setter # type: ignore
    @abc.abstractmethod
    def owner(self, owner: str) -> None:
        pass

    @property # type: ignore
    @abc.abstractmethod
    def created(self) -> Optional[Union[date, datetime]]:
        """
        This object's created timestamp as a date or datetime object. Setting this property with an ISO 8601
        string will also work -- the ISO string will be parsed automatically as a datetime object.
        """
        pass

    @created.setter # type: ignore
    @abc.abstractmethod
    def created(self, value: Optional[Union[date, datetime]]) -> None:
        pass

    @property # type: ignore
    @abc.abstractmethod
    def modified(self) -> Optional[Union[date, datetime]]:
        """
        This object's last modified timestamp as a date or datetime object. Setting this property with an ISO 8601
        string will also work -- the ISO string will be parsed automatically as a datetime object.
        """
        pass

    @modified.setter # type: ignore
    @abc.abstractmethod
    def modified(self, value: Optional[Union[date, datetime]]) -> None:
        pass

    @property # type: ignore
    @abc.abstractmethod
    def derived_by(self) -> Optional[str]:
        """
        The id of the mechanism by which this object was derived, if any.
        """
        pass

    @derived_by.setter # type: ignore
    @abc.abstractmethod
    def derived_by(self, derived_by: Optional[str]) -> Optional[str]:
        pass

    @property # type: ignore
    @abc.abstractmethod
    def derived_from(self) -> List[str]:
        """
        A list of the ids of the HEAObjects from which this object was derived. Cannot be None.
        """
        pass

    @derived_from.setter # type: ignore
    @abc.abstractmethod
    def derived_from(self, derived_from: List[str]) -> None:
        pass

    @abc.abstractmethod
    def to_dict(self) -> Mapping[str, Any]:
        """
        Returns a dict containing the attributes of this HEAObject instance. It gets the attributes to include by
        calling the get_attributes class method.

        :return: a dict of attribute names to attribute values.
        """
        pass

    @abc.abstractmethod
    def json_dumps(self, dumps: Callable[[Mapping[str, Any]], str] = json.dumps) -> str:
        """
        Returns a JSON-formatted string from the attributes of this instance. Passes the json_encode function as the
        default parameter.

        :param dumps: any callable that accepts a HEAObject and returns a string.
        :return: a string.
        """
        pass

    @abc.abstractmethod
    def json_loads(self, jsn: str, loads: Callable[[Union[str]], Mapping[str, Any]] = json.loads) -> None:
        """
        Populates the object's attributes with the property values in the provided JSON. If the provided JSON has a
        type property, this method requires that it match this object's type.

        :param jsn: a JSON string.
        :param loads: any callable that accepts str and returns dict with parsed JSON (json.loads() by default).
        :raises DeserializeException: if any of the JSON object's values are wrong, or the provided JSON
        document is not a valid JSON document.
        """
        pass

    @abc.abstractmethod
    def from_dict(self, d: Mapping[str, Any]) -> None:
        """
        Populates the object's attributes with the property values in the given dict. Supports nested dicts and lists.

        :param d: a dict.
        :raises DeserializeException: if any of the dict's values are wrong.
        """
        pass

    @property # type: ignore
    @abc.abstractmethod
    def type(self) -> str:
        """
        The string representation of this object's type.

        :return: a string.
        """
        pass

    @abc.abstractmethod
    def get_attributes(self) -> Iterator[str]:
        """
        Returns a tuple containing the attributes that to_dict will write to a dictionary.

        :return: an iterator of attribute names.
        """
        pass

    @abc.abstractmethod
    def get_all_attributes(self) -> Iterator[str]:
        """
        Returns a tuple containing all of this object's attributes.

        :return: an iterator of attribute names.
        """
        pass

    @classmethod
    @abc.abstractmethod
    def get_prompt(cls, field_name: Optional[str]) -> Optional[str]:
        pass

    @classmethod
    @abc.abstractmethod
    def is_displayed(cls, field_name: Optional[str]) -> bool:
        pass

    @classmethod
    @abc.abstractmethod
    def get_type_name(cls) -> str:
        """
        Returns a string representation of a HEAObject type.

        :return: a type string.
        """
        pass

    @classmethod
    @abc.abstractmethod
    def get_type_display_name(cls) -> Optional[str]:
        """
        Returns a display name for the HEAObject type, or None if there is no display name for this type.

        :return: the display name string
        """
        pass


class NonShareableHEAObject(HEAObject, abc.ABC):
    """
    Interface for HEAObjects that are not shareable with other users.
    """
    pass


class PermissionAssignment(NonShareableHEAObject, abc.ABC):
    """
    Interface for permission assignment classes.
    """

    @property # type: ignore
    @abc.abstractmethod
    def user(self) -> str:
        """
        The user whose permissions will be impacted.
        """
        pass

    @user.setter # type: ignore
    @abc.abstractmethod
    def user(self, user_: str) -> None:
        pass

    @property # type: ignore
    @abc.abstractmethod
    def permissions(self) -> List[Permission]:
        """
        The list of permissions assigned.
        """
        pass

    @permissions.setter # type: ignore
    @abc.abstractmethod
    def permissions(self, perms: List[Permission]):
        pass


class Invite(PermissionAssignment, abc.ABC):
    """
    Interface for invites to access a HEAObject.
    """

    @property # type: ignore
    @abc.abstractmethod
    def accepted(self) -> bool:
        """
        Whether the user has accepted the invite.
        """
        pass

    @accepted.setter # type: ignore
    @abc.abstractmethod
    def accepted(self, accepted: bool) -> bool:
        pass


class Share(PermissionAssignment, abc.ABC):
    @property # type: ignore
    @abc.abstractmethod
    def invite(self) -> Invite:
        """
        The invite, if any.
        """
        pass

    @invite.setter # type: ignore
    @abc.abstractmethod
    def invite(self, invite: Invite) -> None:
        pass


class ShareableHEAObject(HEAObject, abc.ABC):
    """
    Interface for objects that can be shared with other users. In general, all non-nested objects
    can be shared.
    """



    @property # type: ignore
    @abc.abstractmethod
    def invites(self) -> List[Invite]:
        """
        A list of Invite objects representing the users who have been invited to access this object. Cannot be None.
        """
        pass

    @invites.setter # type: ignore
    @abc.abstractmethod
    def invites(self, invites: List[Invite]) -> None:
        pass

    @property # type: ignore
    @abc.abstractmethod
    def shares(self) -> List[Share]:
        """
        A list of Share objects representing the users with whom this object has been shared.
        """
        pass

    @shares.setter # type: ignore
    @abc.abstractmethod
    def shares(self, shares: List[Share]) -> None:
        pass


NONSHAREABLE_HEAOBJECT_TYPEVAR = TypeVar('NONSHAREABLE_HEAOBJECT_TYPEVAR', bound=NonShareableHEAObject)


class AbstractHEAObject(HEAObject, abc.ABC):
    """
    Abstract base class for all HEA objects.

    All subclasses of HEAObject must have a zero-argument constructor.

    All non-callable instance members will be included in the to_dict() and json_dumps() methods.

    Copies and deep copies using the copy module will copy all non-callable instance members of any subclass of
    HEAObject. Override __copy__ and __deepcopy__ to change that behavior.
    """
    def __init__(self):
        self.__id: Optional[str] = None
        self.__source: Optional[str] = None
        self.__version: Optional[str] = None
        self.__name: Optional[str] = None
        self.__display_name: Optional[str] = None
        self.__description: Optional[str] = None
        self.__owner = user.NONE_USER
        self.__created: Optional[Union[datetime, date]] = None  # The datetime when the object was created
        self.__modified: Optional[Union[datetime, date]] = None  # The datetime when the object was last modified
        self.__derived_by = None
        self.__derived_from = []

    @property
    def id(self) -> Optional[str]:
        return self.__id

    @id.setter
    def id(self, id_: Optional[str]) -> None:
        self.__id = str(id_) if id_ else None

    @property
    def source(self) -> Optional[str]:
        return self.__source

    @source.setter
    def source(self, source: Optional[str]) -> None:
        self.__source = str(source) if source else None

    @property
    def version(self) -> Optional[str]:
        return self.__version

    @version.setter
    def version(self, version: Optional[str]) -> None:
        self.__version = str(version) if version else None

    @property
    def name(self) -> Optional[str]:
        return self.__name

    @name.setter
    def name(self, name: Optional[str]) -> None:
        self.__name = str(name) if name else None

    @property
    def display_name(self) -> Optional[str]:
        return self.__display_name

    @display_name.setter
    def display_name(self, display_name: Optional[str]) -> None:
        self.__display_name = str(display_name) if display_name else self.__name

    @property
    def description(self) -> Optional[str]:
        return self.__description

    @description.setter
    def description(self, description: Optional[str]) -> None:
        self.__description = str(description) if description else None

    @property
    def owner(self) -> str:
        return self.__owner

    @owner.setter
    def owner(self, owner: str) -> None:
        if owner:
            self.__owner = str(owner)
        else:
            raise ValueError('owner cannot be None')

    @property
    def created(self) -> Optional[Union[date, datetime]]:
        return self.__created

    @created.setter
    def created(self, value: Optional[Union[date, datetime]]) -> None:
        if value is None or isinstance(value, (datetime, date)):
            self.__created = value
        else:
            self.__created = dateutil.parser.isoparse(value)

    @property
    def modified(self) -> Optional[Union[date, datetime]]:
        return self.__modified

    @modified.setter
    def modified(self, value: Optional[Union[date, datetime]]) -> None:
        if value is None or isinstance(value, (datetime, date)):
            self.__modified = value
        else:
            self.__modified = dateutil.parser.isoparse(value)

    @property
    def derived_by(self) -> Optional[str]:
        return self.__derived_by

    @derived_by.setter
    def derived_by(self, derived_by: Optional[str]) -> None:
        self.__derived_by = str(derived_by) if derived_by else None

    @property
    def derived_from(self) -> List[str]:
        return list(self.__derived_from)

    @derived_from.setter
    def derived_from(self, derived_from: List[str]) -> None:
        if derived_from is None:
            raise ValueError('derived_from cannot be None')
        if not all(isinstance(s, str) for s in derived_from):
            raise TypeError('derived_from can only contain str objects')
        self.__derived_from = list(derived_from)

    def to_dict(self) -> Mapping[str, Any]:
        def nested(obj):
            if isinstance(obj, HEAObject):
                return obj.to_dict()
            elif isinstance(obj, list):
                return [nested(o) for o in obj]
            else:
                return obj

        return {a: nested(getattr(self, a)) for a in self.get_attributes()}

    def json_dumps(self, dumps: Callable[[Mapping[str, Any]], str] = json.dumps) -> str:
        return dumps(self.to_dict())

    def json_loads(self, jsn: str, loads: Callable[[Union[str]], Mapping[str, Any]] = json.loads) -> None:
        try:
            self.from_dict(loads(jsn))
        except json.JSONDecodeError as e:
            raise DeserializeException from e

    def from_dict(self, d: Mapping[str, Any]) -> None:
        try:
            for k, v in d.items():
                if k in self.get_attributes():
                    if isinstance(v, list):
                        lst = []
                        for e in v:
                            if isinstance(e, dict):
                                if 'type' not in e:
                                    raise ValueError(
                                        'type property is required in nested dicts but is missing from {}'.format(e))
                                obj = type_for_name(e['type'])()
                                obj.from_dict(e)
                                lst.append(obj)
                            else:
                                lst.append(e)
                        setattr(self, k, lst)
                    elif isinstance(v, dict):
                        if 'type' not in v:
                            raise ValueError(
                                'type property is required in nested dicts but is missing from {}'.format(v))
                        obj = type_for_name(v['type'])()
                        obj.from_dict(v)
                        setattr(self, k, obj)
                    elif k != 'type':
                        setattr(self, k, v)
                    else:
                        if v != self.type:
                            raise ValueError(
                                f"type property does not match object type: object type is {self.type} but the dict's type property has value {v}")
        except (ValueError, TypeError) as e:
            raise DeserializeException from e

    @property
    def type(self) -> str:
        return self.get_type_name()

    def get_attributes(self) -> Iterator[str]:
        return (m[0] for m in inspect.getmembers(self, self.__is_not_callable)
                if not m[0].startswith('_') and m not in inspect.getmembers(type(self), self.__is_not_callable))

    def get_all_attributes(self) -> Iterator[str]:
        return (m[0] for m in inspect.getmembers(self, self.__is_not_callable)
                if not m[0].startswith('_') and m not in inspect.getmembers(type(self), self.__is_not_callable))

    @classmethod
    def get_prompt(cls, field_name: Optional[str]) -> Optional[str]:
        return field_name

    @classmethod
    def is_displayed(cls, field_name: Optional[str]) -> bool:
        return True if field_name != 'id' else False

    @classmethod
    def get_type_name(cls) -> str:
        return cls.__module__ + '.' + cls.__name__

    @classmethod
    def get_type_display_name(cls) -> Optional[str]:
        """
        Returns a display name for the HEAObject type, or None if there is no display name for this type. The default
        implementation returns None. A concrete type implementation should override this method to return a display
        name for the type.

        :return: the display name string
        """
        return None

    def _check_owner(self, nested_obj: NONSHAREABLE_HEAOBJECT_TYPEVAR) -> NONSHAREABLE_HEAOBJECT_TYPEVAR:
        if nested_obj.owner == user.NONE_USER and self.__owner != user.NONE_USER:
            c = copy.copy(nested_obj)
            c.owner = self.__owner
            return c
        elif nested_obj.owner != self.__owner:
            raise ValueError("SharedWith instance has wrong owner: expected %s; actual %s" %
                             (self.__owner, nested_obj.owner))
        return nested_obj

    @staticmethod
    def __is_not_callable(x) -> bool:
        return not callable(x)

    def __eq__(self, other) -> bool:
        if not isinstance(other, type(self)):
            return NotImplemented
        attrs = set(self.get_all_attributes()).union(other.get_all_attributes())
        return all(getattr(self, a, None) == getattr(other, a, None) for a in attrs)

    def __repr__(self) -> str:
        return 'heaobject.root.from_dict(' + repr(self.to_dict()) + ')'

    def __str__(self) -> str:
        if self.display_name:
            return self.display_name
        else:
            return 'Untitled ' + type(self).__name__

    def __copy__(self):
        clz = type(self)
        result = clz()
        for a in self.get_attributes():
            try:
                setattr(result, a, getattr(self, a))
            except AttributeError:
                pass  # Skip read-only attributes
        return result

    def __deepcopy__(self, memo):
        result = type(self)()
        for a in self.get_attributes():
            try:
                setattr(result, a, copy.deepcopy(getattr(self, a), memo))
            except AttributeError:
                pass  # Skip read-only attributes
        return result


class AbstractNonShareableHEAObject(AbstractHEAObject, NonShareableHEAObject, abc.ABC):
    """
    Abstract base class for all HEAObjects that cannot be shared with other users.
    """
    pass


class AbstractPermissionAssignment(AbstractNonShareableHEAObject, PermissionAssignment, abc.ABC):
    """
    Abstract base class for permissions-related classes.
    """
    def __init__(self):
        super().__init__()
        self.__user = user.NONE_USER
        self.__permissions: Iterable[Permission] = []

    @property
    def user(self) -> str:
        return self.__user

    @user.setter
    def user(self, user_: str) -> None:
        self.__user = str(user_)

    @property
    def permissions(self) -> List[Permission]:
        return list(self.__permissions)

    @permissions.setter
    def permissions(self, perms: List[Permission]):
        self.__permissions = set(perms)


class InviteImpl(AbstractPermissionAssignment, Invite):
    """
    Implementation of an invite.
    """
    def __init__(self):
        super().__init__()
        self.__accepted = False

    @property
    def accepted(self) -> bool:
        return self.__accepted

    @accepted.setter
    def accepted(self, accepted: bool) -> None:
        if accepted is None:
            raise ValueError('accepted cannot be None')
        self.__accepted = accepted


class ShareImpl(AbstractPermissionAssignment, Share):
    """
    Implementation of a share.
    """
    def __init__(self):
        super().__init__()
        self.__invite: Invite = None

    @property
    def invite(self) -> Invite:
        return self.__invite

    @invite.setter
    def invite(self, invite: Invite) -> None:
        if invite is not None and not isinstance(invite, Invite):
            raise TypeError('invite not an Invite')
        self.__invite = invite


class AbstractShareableHEAObject(AbstractHEAObject, ShareableHEAObject, abc.ABC):
    """
    Abstract base class representing objects that can be shared with other users. In general, all non-nested objects
    can be shared.
    """

    def __init__(self):
        super().__init__()
        self.__invites: List[Invite] = []
        self.__shares: List[Share] = []

    @property
    def invites(self) -> List[Invite]:
        """
        A list of Invite objects representing the users who have been invited to access this object. Cannot be None.
        """
        return copy.deepcopy(self.__invites)

    @invites.setter
    def invites(self, invites: List[Invite]) -> None:
        if invites is None:
            raise ValueError('invites cannot be None')
        if not all(isinstance(s, Invite) for s in invites):
            raise TypeError('invites can only contain Invite objects')
        self.__invites = [self._check_owner(s) for s in invites]

    @property
    def shares(self) -> List[Share]:
        """
        A list of Share objects representing the users with whom this object has been shared.
        """
        return copy.deepcopy(self.__shares)

    @shares.setter
    def shares(self, shares: List[Share]) -> None:
        if shares is None:
            raise ValueError("shares cannot be None")
        if not all(isinstance(s, Share) for s in shares):
            raise TypeError("shares can only contain Share objects")
        self.__shares = [self._check_owner(s) for s in shares]


def json_dumps(o: HEAObject, dumps=json.dumps):
    """
    Serialize an HEAObject to a JSON document. It set the default parameter to the json_encode function.

    :param o: the HEAObject to serialize.
    :param dumps: the deserializer.
    :return: a JSON document.
    """
    return dumps(o.to_dict(), default=json_encode)


def json_encode(o) -> str:
    """
    Function to pass into the json.dumps default parameter that customizes encoding for HEAObject objects.

    :param o: the object to encode.
    :return: the object after encoding.
    """
    if isinstance(o, (datetime, date)):
        return o.isoformat()
    else:
        return o


def is_heaobject_type(name: str) -> bool:
    """
    Returns whether the supplied string is the name of an HEAObject type.
    :param name: a string.
    :return: True if the string is the name of an HEAObject type, or False if not.
    """
    try:
        mod_str, cls_str = name.rsplit('.', 1)
        result = getattr(importlib.import_module(mod_str), cls_str)
        if not issubclass(result, HEAObject):
            return False
        return True
    except ValueError:
        return False


def type_for_name(name: str) -> Type[HEAObject]:
    """
    Returns the HEAObject type for the given string.

    :param name: a type string.
    :return: a HEAObject type.
    """
    try:
        mod_str, cls_str = name.rsplit('.', 1)
        result = getattr(importlib.import_module(mod_str), cls_str)
        if not issubclass(result, HEAObject):
            raise TypeError(f'Name must be the name of an HEAObject type, but was {name}')
        return result
    except ValueError:
        raise ValueError(f'{name} does not look like a module path')


def from_dict(d: Mapping[str, Any]) -> HEAObject:
    """
    Creates a HEA object from the given dict.

    :param d: a dict. It must have, at minimum, a type key with the type name of the HEA object to create. It must
    additionally have key-value pairs for any mandatory attributes of the HEA object.
    :return: a HEAObject.
    """
    type_name = d.get('type', None)
    if not type_name:
        raise ValueError('type key is required')
    obj = type_for_name(type_name)()
    obj.from_dict(d)
    return obj
