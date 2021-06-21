from platform import system as _system
from os import getenv
from os import environ


if _system() == 'Windows':
    from .windows import setenv, unsetenv
else:
    from .unix import setenv, unsetenv


def getenvall() -> dict:
    return environ.copy()
