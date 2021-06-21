# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""The base class to hold all the AutoML events."""
from abc import ABC
from typing import Optional

from azureml.automl.core.shared._error_response_constants import ErrorCodes
from azureml.telemetry.contracts import ExtensionFields
from azureml.telemetry.contracts._standard_fields import FailureReason, TaskResult


class AutoMLBaseEvent(ABC):
    """
    Base class for all AutoML events. Subclasses can override `extension_fields` to log custom fields along with the
    events.The event name defaults to the name of the sub-class.
    """

    @property
    def event_name(self) -> str:
        """
        The name of the event - same as the class name.
        """
        return self.__class__.__name__

    @property
    def extension_fields(self) -> ExtensionFields:
        """
        The custom properties that describe the event. This is logged in the telemetry under 'custom_dimensions'
        """
        return ExtensionFields()

    @property
    def task_result(self) -> TaskResult:
        """
        The task result, describing if the event resulted in a successful or failed operation. Defaults to a neutral
        result (represented by TaskResult.Others, an enum with a value equal to 100)
        """
        return TaskResult.Others

    @property
    def failure_reason(self) -> Optional[FailureReason]:
        """
        If the task result was a failure, the failure reason indicates if the error was User or System caused.
        """
        return None


class RunFailed(AutoMLBaseEvent):
    """
    An AutoML run failure event. This is logged for all AutoML runs, with general information on the error.
    """

    def __init__(self, run_id: str, error_code: str, error: str) -> None:
        """
        Constructor for creating a RunFailed Event
        :param run_id: The run identifier for the event.
        :param error_code: The complete error hierarchy
        :param error: A telemetry-friendly (log safe) representation of the error. May include stack traces.
        """
        self._run_id = run_id
        self._error_code = error_code
        self._error = error

    @property
    def extension_fields(self) -> ExtensionFields:
        return ExtensionFields(
            {
                "run_id": self._run_id,
                "error_code": self._error_code,
                "error": self._error,
            }
        )

    @property
    def failure_reason(self) -> Optional[FailureReason]:
        if ErrorCodes.USER_ERROR in self._error_code:
            return FailureReason.UserError
        else:
            return FailureReason.SystemError

    @property
    def task_result(self) -> TaskResult:
        return TaskResult.Failure
