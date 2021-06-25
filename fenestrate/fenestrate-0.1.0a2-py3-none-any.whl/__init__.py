try:
    import importlib.metadata as importlib_metadata
except ModuleNotFoundError:
    import importlib_metadata  # type: ignore

__version__ = importlib_metadata.version(__name__)

from fenestrate.fenestrate import (DailyWindow, available_windows_between,
                                   concrete_windows_on_date,
                                   in_nonexcluded_window, in_window,
                                   next_window, windows_at_time)
