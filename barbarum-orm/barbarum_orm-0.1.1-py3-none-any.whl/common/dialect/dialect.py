from abc import ABC, abstractmethod
from typing import Any

class Dialect(ABC): 

    def __init__(self) -> None:
        super().__init__()
        self.options = dict()

    @abstractmethod
    def get_url(self) -> str: 
        raise NotImplementedError()

    @abstractmethod
    def get_dialect_name(self) -> str: 
        raise NotImplementedError()

    def get_options(self) -> dict:
        return self.options
    
    def set_option(self, name:str, value:Any):
        if name is None: 
            raise ValueError("option name can not be none.")
        name = name.strip()
        if len(name) == 0: 
            raise ValueError("optioin name can not be empty")
        self.options[name] = value
    
    def delete_option(self, name):
        if name is None: 
            raise ValueError("option name can not be none.")
        name = name.strip()
        if len(name) == 0: 
            raise ValueError("optioin name can not be empty")
        if name not in self.options: 
            return False
        del self.options[name]
        return True
    
