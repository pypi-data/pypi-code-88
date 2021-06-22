"""Data classes and enums for communications."""
from dataclasses import dataclass
from enum import Enum
from json import JSONEncoder
from typing import Any, Dict, List, Optional


@dataclass
class ExecutionRequest:
    """Internal data of task to be executed."""
    action: str
    device: str
    device_parameters: str
    shots: int
    task_group: Optional[str]
    send_email: bool


class ExecutionRequestEncoder(JSONEncoder):
    """JSONEncoder for ExecutionRequest"""
    def default(self, o):
        if isinstance(o, ExecutionRequest):
            return {
                'action': o.action,
                'device': o.device,
                'deviceParameters': o.device_parameters,
                'shots': o.shots,
                'taskGroup': o.task_group,
                'sendEmail': o.send_email
            }
        return super().default(o)


@dataclass
class TaskData:
    """Internal data of task object."""
    id: str
    userId: str
    action: Optional[str]
    device: str
    deviceParameters: Optional[str]
    shots: int
    createdAt: str
    updatedAt: str
    taskGroup: Optional[str]
    sendEmail: bool
    version: str

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> 'TaskData':
        return TaskData(
            id=d['id'],
            userId=d['userId'],
            action=d.get('action'),
            device=d['device'],
            deviceParameters=d.get('deviceParameters'),
            shots=d['shots'],
            createdAt=d['createdAt'],
            updatedAt=d['updatedAt'],
            taskGroup=d.get('taskGroup'),
            sendEmail=d['sendEmail'],
            version=d['version'],
        )


@dataclass
class TaskListData:
    """List of tasks which returns from API"""
    tasks: List[TaskData]
    count: int


class Status(str, Enum):
    """Statuses"""
    CREATED = "CREATED"
    QUEUED = "QUEUED"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    CANCELLING = "CANCELLING"
    CANCELLED = "CANCELLED"

    def is_done(self) -> bool:
        """Check whether the status is finished (completed, failed or cancelled) or not"""
        return self in (Status.COMPLETED, Status.FAILED, Status.CANCELLED)
