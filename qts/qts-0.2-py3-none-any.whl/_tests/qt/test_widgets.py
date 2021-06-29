from qts import QtCore
from qts import QtWidgets


def test_widget_present() -> None:
    assert issubclass(QtWidgets.QWidget, QtCore.QObject)
