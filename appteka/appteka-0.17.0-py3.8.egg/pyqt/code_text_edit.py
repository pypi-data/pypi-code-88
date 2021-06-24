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

"""Here the text edit with line numbers and highlighting of current
line is implemented."""

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QSize, QRect, Qt

LINE_COLOR = QtGui.QColor(Qt.yellow).lighter(160)
FONT = "monospace"


class CodeTextEdit(QtWidgets.QPlainTextEdit):
    """Text field for editing the source code."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__number_area = LineNumberArea(self)

        self.blockCountChanged.connect(self.__update_line_number_area_width)
        self.updateRequest.connect(self.__update_line_number_area)
        self.cursorPositionChanged.connect(self.__highlight_current_line)

        self.__update_line_number_area_width(0)
        self.__highlight_current_line()

        font = QtGui.QFont(FONT)
        font.setStyleHint(QtGui.QFont.Monospace)
        self.setFont(font)

    def set_text(self, text):
        """Set text."""
        self.document().setPlainText(text)

    def line_number_area_width(self):
        """Return the width of the number area."""

        count = max(1, self.blockCount())
        digits = 1
        while count >= 10:
            count = count / 10
            digits = digits + 1

        return 3 + self.fontMetrics().horizontalAdvance('9') * digits

    def __highlight_current_line(self):
        extra_selections = []
        if not self.isReadOnly():
            selection = QtWidgets.QTextEdit.ExtraSelection()
            selection.format.setBackground(LINE_COLOR)
            selection.format.setProperty(
                QtGui.QTextFormat.FullWidthSelection, True)
            selection.cursor = self.textCursor()
            selection.cursor.clearSelection()
            extra_selections.append(selection)

        self.setExtraSelections(extra_selections)

    def __update_line_number_area_width(self, new_block_count):
        # pylint: disable=unused-argument
        self.setViewportMargins(self.line_number_area_width(), 0, 0, 0)

    def __update_line_number_area(self, rect, delta_y):
        if delta_y:
            self.__number_area.scroll(0, delta_y)
        else:
            self.__number_area.update(
                0, rect.y(),
                self.__number_area.width(),
                rect.height())

        if rect.contains(self.viewport().rect()):
            self.__update_line_number_area_width(0)

    def lineNumberAreaPaintEvent(self, event):
        # pylint: disable=invalid-name,missing-docstring

        painter = QtGui.QPainter(self.__number_area)
        painter.fillRect(event.rect(), Qt.lightGray)

        block = self.firstVisibleBlock()
        block_number = block.blockNumber()
        top = self.blockBoundingGeometry(block).translated(
            self.contentOffset()).top()
        bottom = top + self.blockBoundingRect(block).height()

        while block.isValid() and top <= event.rect().bottom():
            if block.isVisible() and bottom >= event.rect().top():
                number = "{}".format(block_number + 1)
                painter.setPen(Qt.black)
                painter.drawText(
                    0, top, self.__number_area.width(),
                    self.fontMetrics().height(), Qt.AlignRight,
                    number)

            block = block.next()
            top = bottom
            bottom = top + self.blockBoundingRect(block).height()
            block_number = block_number + 1

    def resizeEvent(self, e):
        # pylint: disable=invalid-name,missing-docstring

        super().resizeEvent(e)

        rect = self.contentsRect()
        self.__number_area.setGeometry(QRect(
            rect.left(), rect.top(),
            self.line_number_area_width(), rect.height()))


class LineNumberArea(QtWidgets.QWidget):
    """Area for the line numbers."""

    def __init__(self, editor):
        super().__init__(editor)
        self.code_editor = editor

    def sizeHint(self):
        # pylint: disable=invalid-name,missing-docstring
        return QSize(self.code_editor.line_number_area_width(), 0)

    def paintEvent(self, event):
        # pylint: disable=invalid-name,missing-docstring
        self.code_editor.lineNumberAreaPaintEvent(event)
