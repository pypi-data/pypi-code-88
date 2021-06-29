from enum import Enum


class DeviceState(Enum):
    UP = 1
    DOWN = 2
    CONNECTIVITY_CHANGE = 3
    NO_INTERNET = 4

