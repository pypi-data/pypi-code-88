import importlib.metadata

from . import visual
from .animate import Animate
from .stim import Stimuli
from .trial import Trial
from .window import Window

__version__ = importlib.metadata.version("stimpy")
