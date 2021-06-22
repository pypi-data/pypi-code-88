"""Module for task."""
from time import sleep
import typing
from typing import List, Optional, SupportsIndex, TypedDict, overload

from .data import Status, TaskData, TaskListData
if typing.TYPE_CHECKING:
    from .api import Api
    from .abstract_result import AbstractResult


class AbstractTask:
    """Abstract task class."""
    def status(self) -> Status:
        """Return the status of task."""
        raise NotImplementedError

    def update(self) -> None:
        """Fetch result and update task."""

    def wait(self, timeout: int = 0) -> Optional['AbstractResult']:
        """Wait the result."""

    def result(self) -> Optional['AbstractResult']:
        """Return the result if it is ready."""


class CloudTaskOptions(TypedDict, total=False):
    """Executing options for CloudTask"""
    send_email: bool
    group: str


class CloudTask(AbstractTask):
    """Task of Blueqat Cloud."""
    def __init__(self,
                 api: 'Api',
                 taskdata: TaskData,
                 result: Optional['AbstractResult'] = None) -> None:
        self._api = api
        self.taskdata = taskdata
        self.resultdata = result

    def status(self) -> Status:
        return self._api.status(self.taskdata.id)

    def update(self) -> None:
        task = self._api.task_result(self.taskdata.id)
        self.taskdata = task.taskdata
        self.resultdata = task.resultdata

    def __repr__(self) -> str:
        return f'CloudTask({repr(self._api)}, {self.taskdata}, {self.resultdata})'

    def wait(self, timeout: int = 0) -> Optional['AbstractResult']:
        waiting_time = 5
        elipsed = 0
        if self.resultdata:
            return self.resultdata
        while not self.status().is_done():
            t = min(timeout - elipsed, waiting_time)
            sleep(t)
            elipsed += t
            if timeout > 0 and elipsed >= timeout:
                return None
        self.update()
        return self.resultdata

    def result(self) -> Optional['AbstractResult']:
        return self.resultdata


class TaskList:
    """Task list."""
    def __init__(self, api: 'Api', tasklist: TaskListData,
                 group: Optional[str], index: int, per: Optional[int],
                 option_fields: Optional[str]) -> None:
        self._api = api
        self.count = tasklist.count
        self.tasklist = [CloudTask(api, taskdata) for taskdata in tasklist.tasks]
        self.group = group
        self.index = index
        self.per = per
        self.option_fields = option_fields

    @overload
    def __getitem__(self, idx: SupportsIndex) -> CloudTask:
        ...

    @overload
    def __getitem__(self, idx: slice) -> List[CloudTask]:
        ...

    def __getitem__(self, idx):
        if isinstance(idx, SupportsIndex):
            return self.tasklist[idx]
        if isinstance(idx, slice):
            return self.tasklist[idx]
        raise TypeError(
            f'TypeList indices must be integer or slices, not {type(idx)}')

    def __len__(self) -> int:
        return len(self.tasklist)

    def __bool__(self) -> bool:
        return bool(self.tasklist)

    def nextpage(self) -> 'TaskList':
        """Get next page of task list."""
        return self._api.tasks(group=self.group,
                               index=self.index + 1,
                               per=self.per,
                               option_fields=self.option_fields)


class TaskIter:
    """Paginator of tasks."""
    def __init__(self, api: 'Api', group: Optional[str], index: int,
                 per: Optional[int], option_fields: Optional[str]) -> None:
        self.tasklist = api.tasks(group=group,
                                  index=index,
                                  per=per,
                                  option_fields=option_fields)
        self.next_i = 0

    def __iter__(self) -> 'TaskIter':
        return self

    def __next__(self) -> CloudTask:
        try:
            task = self.tasklist[self.next_i]
        except IndexError:
            self.tasklist = self.tasklist.nextpage()
            self.next_i = 0
            if len(self.tasklist) > 0:
                task = self.tasklist[self.next_i]
            else:
                raise StopIteration
        self.next_i += 1
        return task
