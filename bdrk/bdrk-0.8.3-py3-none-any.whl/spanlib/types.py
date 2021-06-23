from enum import Enum


class ModelServerStatus(str, Enum):
    DEPLOYING = "DEPLOYING"
    DEPLOYED = "DEPLOYED"
    STOPPING = "STOPPING"  # aka Undeploying
    STOPPED = "STOPPED"  # aka Not deployed
    FAILED = "FAILED"
    ERROR = "ERROR"
    NEW = "NEW"


class NotebookStatus(str, Enum):
    STARTING = "STARTING"
    RUNNING = "RUNNING"
    FAILED = "FAILED"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"
    ERROR = "ERROR"
    UNKNOWN = "UNKNOWN"


class PipelineRunStatus(str, Enum):
    ACCEPTED = "Accepted"
    REJECTED = "Rejected"
    QUEUED = "Queued"
    RUNNING = "Running"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"
    UNKNOWN = "Unknown"
    STOPPING = "Stopping"
    STOPPED = "Stopped"
