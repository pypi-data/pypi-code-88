import logging
from typing import Tuple, Union

from psychopy import visual
from psychopy.monitors import Monitor

logger = logging.getLogger("stimpy")
logger.setLevel(logging.WARNING)


class Window(visual.Window):
    def __init__(
        self,
        *,
        monitor: Union[str, Monitor] = None,
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
        if monitor is None:
            monitor = "__blank__"
        if not isinstance(monitor, Monitor):
            monitor = Monitor(monitor)

        monitor.setDistance(distance)
        monitor.setWidth(width)

        if size is None:
            try:
                import ctypes

                user32 = ctypes.windll.user32
                user32.SetProcessDPIAware()
                size = (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
            except AttributeError:
                size = monitor.getSizePix()
                if size is not None:
                    logger.warning(
                        "Monitor resolution cannot be found "
                        f"and is set to {size[0]}x{size[1]}. Set the "
                        "resolution manually with the 'size' argument."
                    )
                else:
                    logger.error(
                        "Monitor resolution cannot be found. Set the "
                        "resolution manually with the 'size' argument."
                    )
        monitor.setSizePix(size)

        super().__init__(
            size=size,
            color=color,
            fullscr=fullscr,
            monitor=monitor,
            units=units,
            **kwargs,
        )
