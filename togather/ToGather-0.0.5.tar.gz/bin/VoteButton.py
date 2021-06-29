# Inheriting from the QRadioButton class, an event and rank is also associated
# with this child button for usage in the ranked choice voting algorithm.
# - Rebecca Ling
from PyQt5 import QtCore, QtGui, QtWidgets

class VoteButton(QtWidgets.QRadioButton):
    def __init__(self, f):
        super(VoteButton, self).__init__()
        QtWidgets.QRadioButton.__init__(self, f)
        self._value = 0
        self._ev = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val

    @property
    def ev(self):
        return self._ev

    @ev.setter
    def ev(self, e):
        self._ev = e