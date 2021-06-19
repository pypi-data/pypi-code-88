"""pipewire_python:
Python controller, player and recorder via pipewire's commands"""

__version__ = "0.0.83"

import sys

if sys.platform == "linux":
    # from pipewire_python.controller import *
    pass
else:
    raise NotImplementedError("By now, Pipewire only runs on linux.")
