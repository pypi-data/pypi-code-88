# TODO: maybe manage to not bypass this strict check
#       https://github.com/python-qt-tools/qts/issues/8
# mypy: implicit_reexport

import typing

from qts._core import (
    an_available_wrapper,
    autoset_wrapper,
    available_wrapper,
    available_wrappers,
    pyqt_5_wrapper,
    pyqt_6_wrapper,
    pyside_5_wrapper,
    pyside_6_wrapper,
    set_wrapper,
    Wrapper,
    wrapper_by_name,
    supported_wrappers,
)
from qts._errors import (
    InternalError,
    InvalidWrapperError,
    MultipleWrappersAvailableError,
    NoWrapperAvailableError,
    QtsError,
    WrapperAlreadySelectedError,
)
from qts._version import get_versions

__version__: str = get_versions()["version"]  # type: ignore[no-untyped-call]
"""The qts version string."""
del get_versions


wrapper: typing.Optional[Wrapper] = None
"""The presently active wrapper.  :data:`None` if no wrapper is set."""
is_pyqt_5_wrapper: bool = False
"""``True`` if the PyQt/Qt5 wrapper is active."""
is_pyqt_6_wrapper: bool = False
"""``True`` if the PyQt/Qt6 wrapper is active."""
is_pyside_5_wrapper: bool = False
"""``True`` if the PySide/Qt5 wrapper is active."""
is_pyside_6_wrapper: bool = False
"""``True`` if the PySide/Qt6 wrapper is active."""

_building_docs: bool = False
"""Set to ``True`` when building the documentation."""
