from qts import QtCore
from qts import QtGui


def test_action_present() -> None:
    assert issubclass(QtGui.QWindow, QtCore.QObject)
