import lib
from constants import *

__all__ = ["PasswordChecker"]


class PasswordChecker:
    def __init__(self, default: bool = False):
        self.properties: list = []
        self.positive: bool = True
        if default:
            self.default_setup()

    def default_setup(self):
        # SEE : https://www.economie.gouv.fr/particuliers/creer-mot-passe-securise
        self.min(
            12).has().uppercase().has().lowercase().has().digits().has().symbols().not_common()

    def validate(self, pwd: str):
        """"""
        return all(self.__is_password_valid_for(prop, pwd) for prop in
                   self.properties)

    def __register_property(self, func, *args) -> None:
        self.properties.append({
            'method': func,
            'positive': self.positive,
            'arguments': args,
        })

    @staticmethod
    def __is_password_valid_for(prop, password):
        return prop['method'](password, prop['positive'], *prop['arguments'])

    @staticmethod
    def __validate_num(num):
        assert (type(num) == 'int' or num > 0), error[
            'length']  # Pylint: disable=unidiomatic-typecheck

    def has(self, regexp: str = None):
        self.positive: bool = True
        if regexp:
            self.__register_property(lib.apply_regexp, [re.compile(regexp)])
        return self

    def no(self, regexp: str = None):
        self.positive: bool = not self.positive
        if regexp:
            self.__register_property(lib.apply_regexp, [re.compile(regexp)])
        return self

    def uppercase(self):
        self.__register_property(lib.uppercase)
        return self

    def lowercase(self):
        self.__register_property(lib.lowercase)
        return self

    def letters(self, min_: int = 0, max_: int = 0):
        self.__register_property(lib.letters, min_, max_)
        return self

    def not_common(self):
        self.__register_property(lib.not_common)
        return self

    def digits(self, min_: int = 0, max_: int = 0):
        self.__register_property(lib.digits, min_, max_)
        return self

    def min(self, min_: int = 10):
        self.__register_property(lib.minimum, min_)
        return self

    def max(self, max_: int = 100):
        self.__register_property(lib.maximum, max_)
        return self

    def spaces(self, min_: int = 0, max_: int = 0):
        self.__register_property(lib.spaces, min_, max_)
        return self

    def symbols(self, min_: int = 0, max_: int = 0):
        self.__register_property(lib.symbols, min_, max_)
        return self


if __name__ == '__main__':
    pwd = PasswordChecker().has().lowercase() \
        .min(0).max(100) \
        .not_common().validate("hello")
    print(pwd)
