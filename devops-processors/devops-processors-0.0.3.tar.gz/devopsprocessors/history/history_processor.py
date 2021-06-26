from typing import Callable, Any, Generator

from cloudevents.http import CloudEvent
from devopsprocessor.processor import Processor

from devopsprocessors.history.history import History


class HistoryProcessor(Processor):

    def __init__(self, history: History):
        self.__history = history

    def __str__(self) -> str:
        return "history"

    def mapper(self) -> Callable[[CloudEvent], Any]:
        return lambda x: self.__history.persist(str(x))

    def close(self) -> None:
        self.__history.close()


def init_history_processor(db_path: str, input_file: str, environment: str) -> Generator:
    hist = History(db_path=db_path, context=(input_file, environment))
    proc = HistoryProcessor(history=hist)
    yield proc
    proc.close()
