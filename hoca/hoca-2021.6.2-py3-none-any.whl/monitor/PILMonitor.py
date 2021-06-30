# Copyright (C) 2021 Jean-Louis Paquelin <jean-louis.paquelin@villa-arson.fr>
#
# This file is part of the hoca (Higher-Order Cellular Automata) library.
#
# hoca is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# hoca is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with hoca.  If not, see <http://www.gnu.org/licenses/>.

import numpy
from PIL import Image


class PILMonitor:
    # TODO: performance should be enhanced
    def __init__(self, size, color_gradient):
        """

        :param size: tuple(int, int)
        :param color_gradient: hoca.core.monitor.ColorGradient instance
        """
        self.size = size
        self.color_gradient = color_gradient

        self.width = size[0]
        self.height = size[1]

        # The updates are temporarily stored in the _list_monitor list
        # They will be later accumulated in _numpy_monitor and arranged
        # as an image in the _image_monitor
        self._list_monitor = []
        self._list_monitor_actual_length = 0

        self._numpy_monitor = numpy.zeros(self.size, dtype=int)

        self._image_monitor = Image.new("RGB", self.size)
        self._image_monitor_data = self._image_monitor.load()

    def reset(self):
        # clear the previous monitored updates
        self._list_monitor_actual_length = 0
        self._numpy_monitor.fill(0)
        self._image_monitor = Image.new("RGB", self.size)
        self._image_monitor_data = self._image_monitor.load()

    def update(self, x, y):
        try:
            self._list_monitor[self._list_monitor_actual_length] = (x, y)
        except IndexError:
            self._list_monitor.append((x, y))
        finally:
            self._list_monitor_actual_length += 1

        if self._list_monitor_actual_length > (self.width * self.height / 2):
            # avoid to get the list too large
            _ = self.image

    @property
    def image(self):
        for i in range(self._list_monitor_actual_length):
            x, y = self._list_monitor[i]
            # Process _list_monitor to the _numpy_monitor and the _array_monitor image
            accumulated_updates = self._numpy_monitor[x, y] + 1
            self._numpy_monitor[x, y] = accumulated_updates
            bounded_accumulated_updates = min(accumulated_updates, self.color_gradient.max_color_index)

            self._image_monitor_data[x, y] = self.color_gradient.get_color(bounded_accumulated_updates)
            # Another implementation could be to compute the maximum of the values
            # in self._numpy_monitor (with numpy.amax()) and call self._color_gradient.get_color()
            # with the max_value keyword parameter.

            self._list_monitor_actual_length = 0

        return self._image_monitor
