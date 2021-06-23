from gcf import __version__
from gcf.functions.execution.events.events import EventContext
from gcf.functions.execution.config import ExecutionStatus, EventType


class TaskStartEvent(EventContext):

    def __init__(self, task_name: str = None):
        EventContext.__init__(self,
                              api_version=__version__,
                              event_type=EventType.TASK_START,
                              task_name=task_name or 'undefined',
                              task_status=ExecutionStatus.WAITING_EXECUTION)


class TaskStatusUpdateEvent(EventContext):

    def __init__(self, task_name: str, task_status: ExecutionStatus):
        EventContext.__init__(self,
                              api_version=__version__,
                              event_type=EventType.TASK_STATUS_UPDATE,
                              task_name=task_name,
                              task_status=task_status)
