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


"""Helpers for building Qt GUI."""

from warnings import warn
from PyQt5 import QtWidgets, QtGui


def add_action(window, name, slot, pic=None, shortcut=None, menu=None):
    """Add action to menu."""

    action = QtWidgets.QAction(name, window)
    action.triggered.connect(slot)

    if pic:
        action.setIcon(QtGui.QIcon(pic))

    if shortcut:
        action.setShortcut(shortcut)

    if menu is not None:
        menu.addAction(action)

    return action


def add_sublayout(parent_layout, direction=None):
    """Add layout to another layout."""

    if direction is not None:
        warn("Argument 'direction' is deprecated and ignored.")

    layout = get_sublayout(parent_layout)
    parent_layout.addLayout(layout)
    return layout


def get_sublayout(parent):
    """Get layout to put it to another one."""
    if parent.direction() == QtWidgets.QBoxLayout.TopToBottom:
        return QtWidgets.QHBoxLayout()

    return QtWidgets.QVBoxLayout()


def add_button(text, slot, layout):
    """Add button connected with slot to layout."""
    button = QtWidgets.QPushButton(text)
    button.clicked.connect(slot)
    layout.addWidget(button)
    return button


def add_edit(layout):
    """Add line edit to layout."""
    edit = QtWidgets.QLineEdit()
    layout.addWidget(edit)
    return edit


def add_label(text, layout):
    """Add text label to layout."""
    label = QtWidgets.QLabel(text)
    layout.addWidget(label)
    return label


def add_widget(widget, layout):
    """Add widget to layout."""
    layout.addWidget(widget)
    return widget


def show_about(title="About program", name="", version="",
               descr="", parent=None):
    """Show about window."""

    mbox = QtWidgets.QMessageBox(parent)
    mbox.setWindowTitle(title)
    text = "<p><b>{} {}</b></p>".format(name, version)
    text += "<p> {} </p>".format(descr)
    mbox.setText(text)
    mbox.exec()
