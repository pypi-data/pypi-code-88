from heaobject import root
from typing import Optional
import copy


class Folder(root.AbstractShareableHEAObject):

    def __init__(self):
        super().__init__()


class Item(root.AbstractNonShareableHEAObject):

    def __init__(self):
        super().__init__()
        self.__actual_object_type_name: Optional[str] = None
        self.__actual_object_id: Optional[str] = None
        self.__actual_object: Optional[root.HEAObject] = None
        self.__folder_id: Optional[str] = None

    @property
    def actual_object_type_name(self) -> Optional[str]:
        """
        The name of the type of the actual HEAObject.
        """
        return self.__actual_object_type_name

    @actual_object_type_name.setter
    def actual_object_type_name(self, actual_object_type_name: Optional[str]) -> None:
        self.__actual_object_type_name = str(actual_object_type_name)

    @property
    def actual_object_id(self) -> Optional[str]:
        """
        The id of the actual HEAObject.
        """
        return self.__actual_object_id

    @actual_object_id.setter
    def actual_object_id(self, actual_object_id: Optional[str]) -> None:
        self.__actual_object_id = str(actual_object_id)

    @property
    def actual_object(self) -> Optional[root.HEAObject]:
        """
        The actual HEAObject.
        """
        return self.__actual_object

    @actual_object.setter
    def actual_object(self, actual_object: Optional[root.HEAObject]) -> None:
        self.__actual_object = copy.deepcopy(actual_object)

    @property
    def folder_id(self) -> Optional[str]:
        """
        The id of this item's folder.
        """
        return self.__folder_id

    @folder_id.setter
    def folder_id(self, folder_id: Optional[str]) -> None:
        self.__folder_id = str(folder_id)

