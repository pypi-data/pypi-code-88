"""Module for making Task and TaskData.

This module is for internal use.
"""
import typing
from typing import Any, Dict, Optional

from .device import Device
from .device_specific import aws_device
from .data import ExecutionRequest

if typing.TYPE_CHECKING:
    from blueqat import Circuit
    from .abstract_result import AbstractResult
    from .task import CloudTaskOptions


def make_executiondata(c: 'Circuit', dev: Device, shots: int,
                       options: 'CloudTaskOptions') -> ExecutionRequest:
    """Make ExecutionData for send job to the server."""
    group = options.get("group", None)
    send_email = options.get("send_email", False)
    if dev.value.startswith("aws/"):
        return aws_device.make_executiondata(c, dev, shots, group, send_email,
                                             options)
    raise ValueError(f"Cannot make {str(dev)} device task")


def make_result(data: Dict[str, Any],
                dev: Device) -> Optional['AbstractResult']:
    """Make AbstractResult from received data."""
    if not data:
        return None
    if dev.value.startswith("aws/"):
        return aws_device.make_result(data, dev)
    raise ValueError(f"Cannot make {str(dev)} result")
