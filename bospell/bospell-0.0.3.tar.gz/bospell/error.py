from abc import ABC, abstractmethod

from botok import Token as BotokToken
from botok.text.modify import is_mistake


class ErrorModelBase(ABC):
    @abstractmethod
    def is_error(self, word: str):
        pass


class NonWordErrorModel(ErrorModelBase):
    def is_error(self, token: BotokToken):
        return is_mistake(token)
