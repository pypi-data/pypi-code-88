from typing import Tuple

from psychopy import visual
from psychopy.monitors import Monitor


class Window(visual.Window):
    def __init__(
        self,
        *,
        monitor: str,
        distance: float = None,
        width: float = None,
        units="deg",
        color=(-1, -1, -1),
        fullscr=True,
        size: Tuple[int, int] = None,
        **kwargs,
    ):
        """Wrapper of :class:`visual.Window`.

        :param monitor: Name of the monitor. Monitor attributes will be loaded
        automatically from disk if the monitor name is already defined.
        :param distance: Monitor distance.
        :param width: Monitor width.
        :param units: Defines the default units of stimuli drawn in the window.
        :param color: Color of background as [r, g, b] list or single value.
        Each gun can take values between -1.0 and 1.0.
        :param fullscr: Create a window in ‘full-screen’ mode. Better timing
        can be achieved in full-screen mode.
        :param size: Size of the window in pixels [x, y].
        :param kwargs: Keyword parameters for :class:`visual.Window`.
        """
        if size is None:
            try:
                import ctypes

                user32 = ctypes.windll.user32
                user32.SetProcessDPIAware()
                size = (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
            except AttributeError:
                pass

        monitor = Monitor(name=monitor, distance=distance, width=width)

        super().__init__(
            size=size,
            color=color,
            fullscr=fullscr,
            monitor=monitor,
            units=units,
            **kwargs,
        )
