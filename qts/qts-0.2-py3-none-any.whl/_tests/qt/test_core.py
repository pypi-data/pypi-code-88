from qts import QtCore


def test_signal() -> None:
    assert isinstance(QtCore.QObject.destroyed, QtCore.Signal)


def test_bound_signal() -> None:
    qt_object = QtCore.QObject()
    assert isinstance(qt_object.destroyed, QtCore.SignalInstance)
