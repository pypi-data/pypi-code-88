"""For local task."""

import typing
from typing import Any, Dict, Optional, TypedDict

from blueqat import Circuit

from .abstract_result import AbstractResult
from .data import Status
from .task import AbstractTask


class LocalResult(AbstractResult):
    """Result object for LocalTask"""
    def __init__(self, shots: typing.Counter[str]):
        self._shots = shots

    def shots(self) -> typing.Counter[str]:
        return self._shots


class LocalTaskOptions(TypedDict, total=False):
    """Execute options for LocalTask"""
    backend: str
    run_options: Dict[str, Any]


class LocalTask(AbstractTask):
    """Task for local simulator."""
    def __init__(self, circuit: Circuit, result: LocalResult) -> None:
        self.circuit = circuit
        self.resultdata = result

    def status(self) -> Status:
        return Status.COMPLETED

    def update(self) -> None:
        pass

    def __repr__(self) -> str:
        return f'LocalTask({self.circuit}, {self.resultdata})'

    def wait(self, timeout: int = 0) -> Optional[LocalResult]:
        return self.resultdata

    def result(self) -> Optional[LocalResult]:
        return self.resultdata


def make_localtask(c: Circuit, shots: int, options: LocalTaskOptions) -> LocalTask:
    """Make a LocalTask"""
    backend = options.get('backend')
    run_options = options.get('run_options', {})
    return LocalTask(
        c,
        LocalResult(c.copy().m[:].run(backend=backend,
                                      shots=shots,
                                      **run_options)))
