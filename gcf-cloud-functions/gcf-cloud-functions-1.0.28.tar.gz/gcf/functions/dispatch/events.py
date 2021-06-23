# -*- coding: utf-8 -*-
"""Events that the dispatch service can handle.

The objects represent events that can be handled by the dispatcher module,
such as `failed` or `done`.
Whenever a task is completed it must create a document in the ``events``
collection using one of the events defined here.

We only treat events of success type (with status `done`) in order to
trigger the next steps of the workflow.
"""

from gcf import __version__
from gcf.functions.execution.events.events import EventContext
from gcf.functions.execution.config import ExecutionStatus, EventType


class DispatchStartEvent(EventContext):

    def __init__(self):
        EventContext.__init__(self,
                              api_version=__version__,
                              event_type=EventType.DISPATCH_START,
                              task_name='dispatch',
                              task_status=ExecutionStatus.WAITING_EXECUTION)
