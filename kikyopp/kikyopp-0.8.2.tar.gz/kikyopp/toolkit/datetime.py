import datetime as dt

__all__ = [
    'get_current_datetime',
]


def get_current_datetime():
    return dt.datetime.now().astimezone()
