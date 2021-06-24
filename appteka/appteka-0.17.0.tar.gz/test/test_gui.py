import unittest
from pyqtest import TestApp
from PyQt5 import QtWidgets
from appteka.pyqt import gui


class Test_gui(unittest.TestCase):
    def test_add_elements(self):
        app = TestApp(self)
        w = QtWidgets.QWidget()
        lt = QtWidgets.QVBoxLayout(w)
        gui.add_sublayout(lt)
        gui.add_label("Label 1", lt)
        gui.add_button("Button 1", lambda: None, lt)
        gui.add_edit(lt)
        app(w, ["label", "button", "edit"])

    def test_get_sublayout(self):
        l1 = QtWidgets.QVBoxLayout()

        l2 = gui.get_sublayout(l1)
        self.assertEqual(l2.direction(), QtWidgets.QBoxLayout.LeftToRight)

        l3 = gui.get_sublayout(l2)
        self.assertEqual(l3.direction(), QtWidgets.QBoxLayout.TopToBottom)
