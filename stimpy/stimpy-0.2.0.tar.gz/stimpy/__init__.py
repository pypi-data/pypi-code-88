import importlib.metadata

from . import visual
from .animate import Animate
from .scene import Scene
from .trial import Trial
from .window import Window

__version__ = importlib.metadata.version("stimpy")
