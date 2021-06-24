import unittest
from pyqtest import TestApp
from appteka.pyqt.select_item_dialog import Items


class TestItems(unittest.TestCase):
    def test_empty(self):
        app = TestApp(self)
        w = Items()
        app(w, ["no items"])

    def test_custom_question(self):
        app = TestApp(self)
        w = Items(question="Custom")
        w.set_items(["one", "two", "three"])
        w.set_items(["one", "two", "three"])
        app(w, [
            "3 items",
            "question is 'Custom'",
        ])
