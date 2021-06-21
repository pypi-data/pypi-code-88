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

"""Here the different types of phasor diagrams are implemented."""

from math import degrees
from warnings import warn
import cmath
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtWidgets, QtGui


DEFAULT_WIDGET_SIZE = QtCore.QSize(500, 500)
DEFAULT_COLOR = (255, 255, 255)
DEFAULT_WIDTH = 1


class Arrow:
    """Arrow to be plotted."""
    def __init__(self, line, end, name=None):
        self.line = line
        self.end = end
        self.name = name
        self.visible = True

    def set_visible(self, value):
        """Sets arrow visible or not."""
        self.line.setVisible(value)
        self.end.setVisible(value)
        self.visible = value

    def update(self, amp, phi, amp_scale=1):
        """Update arrow."""
        if amp == 0:
            if self.visible:
                self.end.setVisible(False)
                self.line.setData([0], [0])
        else:
            if self.visible:
                self.end.setVisible(True)
            compl = cmath.rect(amp_scale*amp, phi)
            x = compl.real
            y = compl.imag

            self.line.setData([0, x], [0, y])
            self.end.setStyle(angle=180 - degrees(phi))
            self.end.setPos(x, y)

    def remove_from(self, widget):
        """Remove items from figure."""
        widget.removeItem(self.line)
        widget.removeItem(self.end)


class BasePhasorDiagram(pg.PlotWidget):
    """Base class for phasor diagrams."""
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setAspectLocked(True)
        self.addLine(x=0, pen=0.2)
        self.addLine(y=0, pen=0.2)
        self.showAxis('bottom', False)
        self.showAxis('left', False)

        policy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred,
            QtWidgets.QSizePolicy.Preferred,
        )
        policy.setHeightForWidth(True)
        self.setSizePolicy(policy)

        self.setMouseEnabled(x=False, y=False)
        self.disableAutoRange()
        self.plotItem.setMenuEnabled(False)
        self.hideButtons()

        self._arrows = {}
        self._legend = None

    def add_legend(self):
        """Add legend."""
        if self._legend:
            return

        self._legend = self.plotItem.addLegend()
        for key in self._arrows:
            self.plotItem.legend.addItem(
                self._arrows[key].line, self.__build_name(key))
            self.plotItem.legend.setColumnCount(self.__legend_cols())

    def _to_front(self, item):
        self.removeItem(item)
        self.addItem(item)

    def __build_name(self, key):
        if not self._arrows[key].name:
            return "{}".format(key)
        return self._arrows[key].name

    def __legend_cols(self):
        return 1 + (len(self._arrows) - 1) // 10

    def sizeHint(self):
        # pylint: disable=invalid-name,no-self-use,missing-docstring
        return DEFAULT_WIDGET_SIZE

    def heightForWidth(self, width):
        # pylint: disable=invalid-name,no-self-use,missing-docstring
        return width


DEFAULT_LINESTYLE = 'solid'
CIRCLES_NUM = 6
LABELS_NUM = 2


class PhasorDiagram(BasePhasorDiagram):
    """Widget for plotting phasor diagram.

    Parameters
    ----------
    parent: object
        Parent object
    """

    def __init__(self, parent=None, size=None, end=None):
        super().__init__(parent)

        _depr_arg(size, "size arg is deprecated and ignored")
        _depr_arg(end, "end arg is deprecated and ignored")

        self.__init_data()
        self.__init_grid()
        self.__init_labels()

        self.set_range(1)

    def __init_data(self):
        self._arrows = {}
        self._legend = None

    def __init_grid(self):
        self.__circles = []
        for _ in range(CIRCLES_NUM):
            circle = pg.QtGui.QGraphicsEllipseItem()
            circle.setPen(pg.mkPen(0.2))
            self.__circles.append(circle)
            self.addItem(circle)

    def __init_labels(self):
        self.__labels = []
        for _ in range(LABELS_NUM):
            label = pg.TextItem()
            self.__labels.append(label)
            self.addItem(label)

    def set_range(self, value):
        """Set range of diagram."""
        self.__range = value
        self.__update_grid()
        self.__update_labels()

    def add_phasor(self, key, amp=0, phi=0, name=None, **kwargs):
        """Create new phasor and add it to the diagram.

        Parameters
        ----------
        key: object
            Key for accessing the phasor.
        amp: float
            Amplitude.
        phi: float
            Phase in radians.
        name: str
            Name for legend.

        Other Parameters
        ----------------
        color: tuple
            Color. Default is (255, 255, 255).
        width: tuple
            Width of line and arrow. Default is 1.
        linestyle: str
            Style of line. Can be 'solid', 'dashed' or
            'dotted'. Default is 'solid'.
        """
        color = _val_if_none(kwargs.get('color'), DEFAULT_COLOR)
        width = _val_if_none(kwargs.get('width'), DEFAULT_WIDTH)
        linestyle = _val_if_none(kwargs.get('linestyle'), DEFAULT_LINESTYLE)

        dash = _linestyle_to_dash(linestyle, width)
        line = self.plot(pen=pg.mkPen(color, width=width, dash=dash))
        end = _end_item(color, width)
        self.addItem(end)

        self._arrows[key] = Arrow(line, end, name)

        for label in self.__labels:
            self._to_front(label)

        self.update_data(key, amp, phi)

    def set_visible(self, key, value=True):
        """Hide or show phasor."""
        if key in self._arrows:
            self._arrows[key].set_visible(value)

    def update_data(self, key, amp, phi):
        """Change phasor value."""
        self._arrows[key].update(amp, phi)

    def remove_phasors(self):
        """Remove all phasors and legend."""

        for key in self._arrows:
            self._arrows[key].remove_from(self)

        if self._legend is not None:
            self._legend.clear()
            self.removeItem(self._legend)

        self.__init_data()

    def __update_grid(self):
        for i in range(CIRCLES_NUM):
            rad = (i + 1) * self.__range / CIRCLES_NUM
            self.__circles[i].setRect(-rad, -rad, rad*2, rad*2)

        self.setRange(QtCore.QRectF(-self.__range, self.__range,
                                    2*self.__range, -2*self.__range))

    def __update_labels(self):
        for i in range(LABELS_NUM):
            value = (i + 1) * self.__range / LABELS_NUM
            self.__labels[i].setText("{}".format(value))
            self.__labels[i].setPos(0, value)

    def update_phasor(self, key, amp, phi):
        """Deprecated."""
        warn("update_phasor() is deprecated, use update_data()",
             FutureWarning)
        self.update_data(key, amp, phi)

    def set_phasor_visible(self, key, value=True):
        """Deprecated."""
        warn("set_phasor_visible() is deprecated, use set_visible()",
             FutureWarning)
        self.set_visible(key, value)

    def show_legend(self):
        """Show legend."""
        warn("show_legend() is deprecated, use add_legend()", FutureWarning)
        self.add_legend()


DEFAULT_MIN_RANGE = 0.001
I_SCALE = 2/3
ROUND_TO = 3
TEXT_FONT_SIZE = 14


class PhasorDiagramUI(BasePhasorDiagram):
    """Phasor diagram with two scales: for voltage and current phasors."""
    def __init__(self, parent=None,
                 auto_range=True, min_range=DEFAULT_MIN_RANGE):
        super().__init__(parent)

        self.__min_range = min_range
        self.__auto_range = auto_range

        self.__init_data()
        self.__init_grid()
        self.__init_labels()
        self.__init_text()

    def __init_data(self):
        self._arrows = {}
        self._legend = None
        self.__to_quant = {}
        self.__amps = {'u': {}, 'i': {}}
        self.__range = {'u': DEFAULT_MIN_RANGE, 'i': DEFAULT_MIN_RANGE}

    def __init_grid(self):
        self.__circles = {}
        for quant in ['u', 'i']:
            self.__circles[quant] = pg.QtGui.QGraphicsEllipseItem()
            self.__circles[quant].setPen(pg.mkPen(0.2))
            self.addItem(self.__circles[quant])

    def __init_labels(self):
        self.__labels = {}
        for quant in ['u', 'i']:
            self.__labels[quant] = pg.TextItem()
            self.addItem(self.__labels[quant])

    def __init_text(self):
        self.__text = pg.TextItem()
        self.__text.setAnchor((1, 0))
        font = QtGui.QFont()
        font.setPixelSize(TEXT_FONT_SIZE)
        self.__text.setFont(font)
        self.addItem(self.__text)

    def add_u(self, key, name=None, **kwargs):
        """Add new U phasor to the diagram."""
        self.__add_phasor(key, name, **kwargs)
        self.__to_quant[key] = 'u'

    def add_i(self, key, name=None, **kwargs):
        """Add new I phasor to the diagram."""
        self.__add_phasor(key, name, **kwargs)
        self.__to_quant[key] = 'i'

    def update_data(self, key, amp, phi):
        """Change phasor data."""
        quant = self.__to_quant[key]
        self.__amps[quant][key] = amp

        if self.__auto_range:
            self.__update_range_opt(key, amp)

        self._arrows[key].update(amp, phi, self.__get_amp_scale(key))

    def remove_phasors(self):
        """Remove all phasors and legend."""
        for key in self._arrows:
            self._arrows[key].remove_from(self)

        if self._legend is not None:
            self._legend.clear()
            self.removeItem(self._legend)

        self.__init_data()
        self.update_range()

    def set_visible(self, key, visible=True):
        """Hide or show phasor."""
        if key in self._arrows:
            self._arrows[key].set_visible(visible)
        if self.__auto_range:
            self.update_range()

    def update_range(self):
        """Update range manually."""
        self.__calc_range()
        self.__apply_range()

    def set_text(self, text):
        """Set text."""
        self.__text.setText(text)
        self.__update_text_pos()

    def __add_phasor(self, key, name=None, **kwargs):
        if key in self._arrows:
            raise ValueError("repeated key: {}".format(key))

        color = _val_if_none(kwargs.get('color'), DEFAULT_COLOR)
        width = _val_if_none(kwargs.get('width'), DEFAULT_WIDTH)

        line = self.plot(pen=pg.mkPen(color, width=width))
        end = _end_item(color, width)
        self.addItem(end)

        self._arrows[key] = Arrow(line, end, name)

        self._to_front(self.__labels['u'])
        self._to_front(self.__labels['i'])

    def __get_amp_scale(self, key):
        if self.__to_quant[key] == 'i':
            return self.__i_radius() / self.__range['i']
        return 1

    def __update_range_opt(self, key, amp):
        if not self._arrows[key].visible:
            return

        quant = self.__to_quant[key]

        if amp > self.__range[quant]:
            self.__range[quant] = amp
        else:
            self.__calc_range()

        self.__apply_range()

    def __calc_range(self):
        for quant in ['u', 'i']:
            self.__range[quant] = self.__min_range
            for key in self.__amps[quant]:
                if not self._arrows[key].visible:
                    continue
                self.__range[quant] = max(self.__range[quant],
                                          self.__amps[quant][key])

    def __apply_range(self):
        self.setRange(QtCore.QRectF(*self.__u_rect()))
        self.__update_grid()
        self.__update_labels()
        self.__update_text_pos()

    def __update_grid(self):
        self.__circles['u'].setRect(*self.__u_rect())
        rad = self.__i_radius()
        self.__circles['i'].setRect(-rad, -rad, 2*rad, 2*rad)

    def __u_rect(self):
        u_radius = self.__range['u']
        return (-u_radius, -u_radius, 2*u_radius, 2*u_radius)

    def __update_labels(self):
        for quant in ['u', 'i']:
            self.__labels[quant].setText("{}".format(
                round(self.__range[quant], ROUND_TO)))

        self.__labels['u'].setPos(0, self.__range['u'])
        self.__labels['i'].setPos(0, self.__i_radius())

    def __update_text_pos(self):
        self.__text.setPos(self.__range['u'], self.__range['u'])

    def __i_radius(self):
        return I_SCALE * self.__range['u']


def _end_item(color, width):
    return pg.ArrowItem(
        tailLen=0,
        tailWidth=1,
        pen=pg.mkPen(color, width=width),
        headLen=width+4)


def _linestyle_to_dash(style, width):
    if style == 'solid':
        return None

    if style == 'dashed':
        return (4, width)

    if style == 'dotted':
        return (1, width)

    raise ValueError("Unknown style")


def _val_if_none(var1, var2):
    return var1 if var1 is not None else var2


def _depr_arg(arg, msg):
    if arg is not None:
        warn(msg, FutureWarning)
