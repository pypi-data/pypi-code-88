# SPDX-License-Identifier: MIT

import threading
import typing

from types import TracebackType
from typing import Any, List, Optional, Type


try:
    from typing import Literal, Protocol, runtime_checkable
except ImportError:
    from typing_extensions import Literal, Protocol, runtime_checkable  # type: ignore


__version__ = '0.2.0'


class ReportType:
    INPUT = 0x01
    OUTPUT = 0x02
    FEATURE = 0x03


_ReportType = Literal[0x01, 0x02, 0x03]  # why mypy :(


@runtime_checkable
class Interface(Protocol):
    '''
    Simple HID interface.
    '''
    @property
    def name(self) -> str:
        '''Device name.'''

    @property
    def vid(self) -> int:
        '''Device vendor ID.'''

    @property
    def pid(self) -> int:
        '''Device product ID.'''

    def read(self) -> List[int]:
        '''Read HID reports from the *INTERRUPT IN* endpoint.'''

    def write(self, data: List[int]) -> None:
        '''
        Send HID reports to the *INTERRUPT OUT* endpoint, or, if the device does
        not support it, via ``SET_REPORT`` transfers.
        '''


@runtime_checkable
class ExtendedInterface(Interface, Protocol):
    '''Builds on :py:class:`Interface` and allows to access further data.'''

    def get_report_descriptor(self) -> List[int]:
        '''Fetches the HID report descriptor for the device.'''


@runtime_checkable
class FullInterface(ExtendedInterface, Protocol):
    '''
    Provides full access to the HID interface.
    '''

    def get_report(self, type_: _ReportType, data: List[int]) -> List[int]:
        '''Performs a `GET_REPORT` request.'''

    def set_report(self, type_: _ReportType, data: List[int]) -> List[int]:
        '''Performs a `SET_REPORT` request.'''


class _Lock(Protocol):
    def acquire(self) -> Any: ...
    def release(self) -> Any: ...


_T = typing.TypeVar('_T', bound=Interface)


class Device(typing.Generic[_T]):
    '''HID device. Implements a context manager to acquire the underlying interface.'''

    def __init__(self, interface: _T, lock_cls: Type[_Lock] = threading.Lock) -> None:
        self._interface = interface
        self._lock = lock_cls()

    def __enter__(self) -> _T:
        '''Acquire the HID interface. Prevents other users using the interface at the same time.'''
        self._lock.acquire()
        return self._interface

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> Literal[False]:
        '''Release the HID interface.'''
        self._lock.release()
        return False  # False means we did not handle the exception :)

    @property
    def name(self) -> str:
        '''Device name.'''
        return self._interface.name

    @property
    def vid(self) -> int:
        '''Device vendor ID.'''
        return self._interface.vid

    @property
    def pid(self) -> int:
        '''Device product ID.'''
        return self._interface.pid
