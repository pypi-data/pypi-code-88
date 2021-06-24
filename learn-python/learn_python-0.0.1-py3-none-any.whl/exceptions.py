from typing import Optional


class MyException(Exception):
    status_code = 500
    message = ""

    def __init__(self, message, exception: Optional[Exception]) -> None:
        if message:
            self.message = message
        self._exception = exception
        super().__init__(self.message)

    @property
    def exception(self) -> Optional[Exception]:
        return self._exception


class ConfigException(MyException):
    """
    Raise when there ies configuration exception
    """


class InvalidFilePath(MyException):
    """
    Raise when there file path is invalid
    """