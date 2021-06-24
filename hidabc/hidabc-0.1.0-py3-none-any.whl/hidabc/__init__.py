# SPDX-License-Identifier: MIT

from typing import List, Literal

try:
    from typing import Protocol, runtime_checkable
except ImportError:
    from typing_extensions import Protocol, runtime_checkable  # type: ignore


class ReportType:
    INPUT = 0x01
    OUTPUT = 0x02
    FEATURE = 0x03


_ReportType = Literal[0x01, 0x02, 0x03]  # why mypy :(


@runtime_checkable
class Device(Protocol):
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
class ExtendedDevice(Protocol, Device):
    '''Builds on :py:class:`Device` and allows to access further data.'''

    def get_report_descriptor(self) -> List[int]:
        '''Fetches the HID report descriptor for the device.'''


@runtime_checkable
class FullDevice(Protocol, ExtendedDevice):
    '''
    Provides full access to the HID interface.
    '''

    def get_report(self, type_: _ReportType, data: List[int]) -> List[int]:
        '''Performs a `GET_REPORT` request.'''

    def set_report(self, type_: _ReportType, data: List[int]) -> List[int]:
        '''Performs a `SET_REPORT` request.'''
