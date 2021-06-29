# TODO: maybe manage to not bypass this strict check
#       https://github.com/python-qt-tools/qts/issues/8
# mypy: implicit_reexport

# start-after qts.is_* example
import qts


if qts.wrapper is None:
    qts.autoset_wrapper()

if qts.is_pyqt_5_wrapper:
    from PyQt5.QtCore import *
elif qts.is_pyqt_6_wrapper:
    from PyQt6.QtCore import *
elif qts.is_pyside_5_wrapper:
    from PySide2.QtCore import *
elif qts.is_pyside_6_wrapper:
    from PySide6.QtCore import *
else:
    raise qts.InvalidWrapperError(wrapper=qts.wrapper)
# end-before qts.is_* example

if qts.is_pyqt_5_wrapper or qts.is_pyqt_6_wrapper:
    Signal = pyqtSignal
    del pyqtSignal

    SignalInstance = pyqtBoundSignal
    del pyqtBoundSignal


Signal = Signal
"""
The class attribute :class:`PySide2.QtCore.Signal` object.  It is a
:ref:`descriptor <descriptors>` that evaluates to a :class:`SignalInstance`
when accessed on an instance of its owning class.

* PyQt - ``pyqtSignal``
* PySide - ``Signal``
"""


SignalInstance = SignalInstance
"""
The instance attribute :class:`PySide2.QtCore.Signal` object that allows subscription
to the signal via ``.connect()`` and emission via ``.emit()`` and so on.

* PyQt - ``pyqtBoundSignal``
* PySide - ``SignalInstance``
"""
