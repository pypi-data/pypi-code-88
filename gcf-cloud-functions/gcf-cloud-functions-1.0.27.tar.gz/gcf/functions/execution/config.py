from enum import Enum


class ExecutionStatus(str, Enum):
    RUNNING = 'running'
    FAILED = 'failed'
    SUCCESS = 'success'
    SLEEPING = 'sleeping'

    WAITING_EXECUTION = 'waiting_execution'
    WAITING_RETRY = 'waiting_retry'
    WAITING_SLEEP = 'waiting_sleep'


class EventType(str, Enum):
    TASK_STATUS_UPDATE = 'task_status_update'
    TASK_START = 'task_start'
    DISPATCH_START = 'dispatch_start'
