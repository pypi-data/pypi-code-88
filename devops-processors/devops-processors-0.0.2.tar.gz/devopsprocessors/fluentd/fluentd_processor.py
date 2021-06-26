from typing import Callable, Any, Generator

from cloudevents.http import CloudEvent
from devopsprocessor.processor import Processor

from devopsprocessors.fluentd.fluentd_logger import FluentdLogger


class FluentdProcessor(Processor):

    def __init__(self, fluentd_logger: FluentdLogger):
        self.__fluentd_logger = fluentd_logger

    def mapper(self) -> Callable[[CloudEvent], Any]:
        return lambda x: self.__fluentd_logger.forward(x)

    def close(self) -> None:
        self.__fluentd_logger.close()


def init_fluentd_processor(tag: str, label: str, host: str, port: int) -> Generator:
    fld = FluentdLogger(tag=tag, label=label, host=host, port=port)
    proc = FluentdProcessor(fluentd_logger=fld)
    yield proc
    proc.close()
