from heaobject import root
import yarl
import copy
from typing import Optional, List


class Resource(root.AbstractShareableHEAObject):
    """
    A REST resource that is served by a HEA component.

    Public data attributes:
        resource_type_name: an HEAObject type that is provided by this service.
        base_path: the URL path to this HEAObject type.
    """

    def __init__(self):
        """
        Constructor.
        """
        super().__init__()
        self.__resource_type_name: Optional[str] = None
        self.base_path: Optional[str] = None

    @property
    def resource_type_name(self) -> Optional[str]:
        """
        The type name of HEAObject that is served by this resource. The setter accepts either a type name or a type. If
        the latter is used, the property will automatically extract the type name.
        """
        return self.__resource_type_name

    @resource_type_name.setter
    def resource_type_name(self, type_name: str):
        if not root.is_heaobject_type(type_name):
            raise ValueError('type_name not a type of HEAObject')
        self.__resource_type_name = type_name


class Component(root.AbstractShareableHEAObject):
    """
    A HEA service.
    """

    def __init__(self) -> None:
        super().__init__()
        self.__base_url: Optional[str] = None
        self.__resources: List[Resource] = []

    @property
    def base_url(self) -> Optional[str]:
        """
        The base URL of the service. The property's setter accepts a string or a yarl URL. In the latter case, it
        converts the URL to a string.
        """
        return self.__base_url

    @base_url.setter
    def base_url(self, value: Optional[str]) -> None:
        if value is not None:
            if not isinstance(value, str):
                raise TypeError('value must be a str')
            self.__base_url = value
        else:
            self.__base_url = None

    @property
    def resources(self) -> List[Resource]:
        """
        The list of REST resources that are served by this component. The property's setter accepts any iterable and
        converts it to a list.
        """
        return copy.deepcopy(self.__resources)

    @resources.setter
    def resources(self, value: List[Resource]) -> None:
        if value is None:
            raise ValueError('value cannot be None')
        if not all(isinstance(r, Resource) for r in value):
            raise TypeError('value must contain all Resource objects')
        self.__resources = list(copy.deepcopy(r) for r in value)

    def add_resource(self, value: Resource) -> None:
        """
        Adds a REST resource to the list of resources that are served by this component.
        :param value: a Resource object.
        """
        if not isinstance(value, Resource):
            raise TypeError('value must be a Resource')
        self.__resources.append(copy.deepcopy(value))

    def remove_resource(self, value: Resource) -> None:
        """
        Removes a REST resource from the list of resources that are served by this component. Ignores None values.
        :param value: a Resource object.
        """
        if not isinstance(value, Resource):
            raise TypeError('value must be a Resource')
        self.__resources.remove(value)

    def get_resource_url_by_type(self, type_name: str) -> Optional[str]:
        """
        Returns the base URL of resources of the given type.
        :param type_name: a HEA object type or type name.
        :return: a URL string, or None if this service does not serve resources of the given type.
        """
        if not root.is_heaobject_type(type_name):
            raise ValueError('type_name not a type of HEAObject')

        for resource in self.__resources:
            if type_name == resource.resource_type_name:
                if self.__base_url:
                    return str(yarl.URL(self.__base_url).join(yarl.URL(resource.base_path)))  # type: ignore[arg-type]
                else:
                    return resource.base_path
        return None


class Property(root.AbstractShareableHEAObject):
    def __init__(self):
        super().__init__()
        self.value = None
