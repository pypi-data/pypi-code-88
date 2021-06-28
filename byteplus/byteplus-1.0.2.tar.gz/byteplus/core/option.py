import datetime
from abc import abstractmethod

from byteplus.core.options import _Options


class Option(object):
    @abstractmethod
    def fill(self, options: _Options) -> None:
        raise NotImplementedError

    @staticmethod
    def conv_to_options(opts: tuple) -> _Options:
        options: _Options = _Options()
        for opt in opts:
            opt.fill(options)
        return options

    @staticmethod
    def with_timeout(timeout: datetime.timedelta):
        class OptionImpl(Option):
            def fill(self, options: _Options) -> None:
                options.timeout = timeout

        return OptionImpl()

    @staticmethod
    def with_request_id(request_id: str):
        class OptionImpl(Option):
            def fill(self, options: _Options) -> None:
                options.request_id = request_id

        return OptionImpl()

    @staticmethod
    def with_headers(headers: dict):
        class OptionImpl(Option):
            def fill(self, options: _Options) -> None:
                options.headers = headers

        return OptionImpl()
