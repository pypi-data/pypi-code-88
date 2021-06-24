# appteka - helpers collection

# Copyright (C) 2018-2021 Aleksandr Popov

# This program is free software: you can redistribute it and/or modify
# it under the terms of the Lesser GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# Lesser GNU General Public License for more details.

# You should have received a copy of the Lesser GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Select item Qt dialog."""

from PyQt5 import QtWidgets
from appteka.pyqt import gui


class SelectItemDialog(QtWidgets.QDialog):
    """Dialog for selecting string item from list."""

    def __init__(self, title="Select item", question="Select item",
                 ok_caption="Ok", cancel_caption="Cancel", parent=None):

        QtWidgets.QDialog.__init__(self, parent)
        self.__index = None
        self.__make_gui(title, question, ok_caption, cancel_caption)

    def set_items(self, str_list):
        """Set the names of items."""
        self.__widget.set_items(str_list)

    def get_item_name(self):
        """Return name of selected item."""
        self.__widget.get_item_name()

    def get_item_index(self):
        """Return index of selected item."""
        return self.__index

    def __on_ok(self):
        self.__index = self.__widget.current_row()
        self.accept()

    def __on_cancel(self):
        self.reject()

    def __make_gui(self, title, question, ok_caption, cancel_caption):
        self.setWindowTitle(title)
        layout = QtWidgets.QVBoxLayout(self)
        self.__widget = gui.add_widget(Items(question), layout)

        l_buttons = gui.add_sublayout(layout, 'h')
        gui.add_button(ok_caption, self.__on_ok, l_buttons)
        gui.add_button(cancel_caption, self.__on_cancel, l_buttons)


class Items(QtWidgets.QWidget):
    """Items to select."""
    def __init__(self, question="Select item", parent=None):
        super().__init__(parent)
        self.__items = []
        self.__make_gui(question)

    def __make_gui(self, question):
        layout = QtWidgets.QVBoxLayout(self)
        gui.add_label(question, layout)
        self.__w_list = gui.add_widget(QtWidgets.QListWidget(), layout)
        self.__w_list.setWordWrap(True)
        self.__w_list.setSpacing(2)

    def current_row(self):
        """Return current row."""
        return self.__w_list.currentRow()

    def set_items(self, items):
        """Set the names of items."""
        self.__items = items
        self.__w_list.clear()
        for item in self.__items:
            self.__w_list.addItem(item)

    def get_item_name(self):
        """Return name of selected item."""
        return self.__items[self.get_item_index()]
