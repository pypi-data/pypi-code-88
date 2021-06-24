import logging
from abc import abstractmethod, ABC
from src.configuration import config

log = logging.getLogger(__name__)


class Person(ABC):

    def __init__(self, uid, name):
        self.uid = uid
        self.name = name

    @abstractmethod
    def create_person(self):
        raise NotImplementedError()


"""
Manager inherit from Person
"""


class Manager(Person):

    test = "test_value"
    """
    This is a constructor 
    """
    def __init__(self, uid, name, salary, sex, password):
        super().__init__(uid, name)
        self.salary = salary
        self.sex = sex
        self._password = password
        self.permissions = None

    @staticmethod
    def set_permissions(permissions):
        #if permissions is not None:
            for permission in permissions:
                if permission in ('execute', 'write'):
                    print("Permission is E/W: ", permission)
                else:
                    print("Read permission")
        #else:
        #    print("No permission")

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, new_password):
        if isinstance(new_password, str):
            self._password = new_password
        else:
            raise Exception("Invalid password")

    @password.deleter
    def password(self):
        del self._password

    def create_person(self):
        pass


# Encrypt & Decrypt
_fernet = None

def get_fernet(): 
    # not a variable as global
    global _fernet

    try:
        fernet_key = config.get('core', 'ccccc')
        if not fernet_key:
            log.warning("Encryption key is null")             
    except Exception as ex:
        raise Exception("Ex")


if __name__ == "__main__":

    print("*" * 80)
    paused = "false"
    is_paused = bool(paused == 'true')
    print(is_paused)

    manager = Manager(1, 'Massipssa', 1000, "male", "pwd")
    print("test: " + manager.test)
    print("id : ", manager.uid)
    print("sex : ", manager.sex)
    print(issubclass(Manager, Person))
    print(hasattr(manager, "sex"))
    print(getattr(manager, "email", "test@gmail.com"))

    if isinstance(manager, Person) or isinstance(manager, Manager):
        print("Yes")

    permissions = ["read", "write", "execute"]
    Manager.set_permissions(permissions)
    print("*" * 80)
