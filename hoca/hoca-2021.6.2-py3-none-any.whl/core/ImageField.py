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

from .automata_framework import Field
from PIL import Image
import numpy


class ImageField(Field):
    """
    WARNING: even if ImageField instances have __getitem__() and __setitem__()
    that return numpy arrays, you can't write:
        my_image_field = my_image_field / 2
    You should write instead:
        my_image_field[:, :, :] = my_image_field[:, :, :] / 2
    or
       my_image_field.data = my_image_field.data / 2
    That's because ImageField inherits of Field and numpy is a client class.
    """

    @classmethod
    def from_image(cls, image_path, image_mode=None, **kwargs):
        """

        :param image_path: str
        :param image_mode: str PIL.Image mode
        :param kwargs: these are passed to the class constructor
        :return: ImageField instance
        """
        image = Image.open(image_path)

        if image_mode is not None:
            image = image.convert(mode=image_mode)

        return cls(image, **kwargs)

    @classmethod
    def blank(cls, size, image_mode=None, **kwargs):
        """
        :param size:
        :param image_mode: PIL.Image mode
        :param kwargs: these are passed to the class constructor
        :return: ImageField instance filled with zeros
        """
        image = Image.new(image_mode, size)

        return cls(image, **kwargs)

    def __init__(self, image, **kwargs):
        """
        :param image: PIL.Image
        """
        super().__init__(**kwargs)

        self._image = image

        # convert image as a numpy array of [0, 1] values
        self._data = numpy.asarray(image).transpose(1, 0, 2) / 255
        # Note: the PIL Image and the numpy array have their coordinates swapped
        # The reason is PIL.Image.size: (width, height) while numpy.ndarray.shape is (rows, columns)
        # Hence the transpose() call

        self._data_written = True

        if self.io_mode == Field.IOMode.IN:
            # The data should not be changed
            self._data.setflags(write=False)

    @property
    def image(self):
        if self._data_written:
            # convert data back to an image
            # rebuild the image from the numpy data
            self._image = Image.fromarray((self._data.transpose(1, 0, 2) * 255).astype(numpy.uint8))
            self._data_written = False

        return self._image

    @property
    def size(self):
        return self._image.size

    @property
    def width(self):
        return self._image.size[0]

    @property
    def height(self):
        return self._image.size[1]

    @property
    def depth(self):
        return len(self._image.getbands())

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    def __getitem__(self, idx):
        """
        Index 0 is the abscissa
        Index 1 is the ordinate
        Index 3 is the color component_select

        TODO: a better documentation
        :param idx: slice
        :return: a value
        """
        return self._data[idx]

    def __setitem__(self, idx, value):
        """
        TODO: a better documentation
        :param idx: slice
        :param value:
        :return: None
        """
        self._data[idx] = value
        self._data_written = True

    def is_in(self, coordinates):
        """Tests if some coordinates are within the field.
        If a coordinate value is None, it will be be ignored. So calling my_field.in_in((3, None, 2))
        will only check the first and the third coordinates against the field dimensions.

        Note: Even if the PILImageFields are implemented with numpy arrays accepting negative indices,
        the is_in() method will return False for any negative coordinates."""
        for length, coordinate in zip(self._data.shape, coordinates):
            if coordinate is not None and (coordinate < 0 or coordinate >= length):
                return False
        return True

    def __str__(self):
        return f"""Field: {self.__class__.__name__}
    width: {self.width}
    height: {self.height}
    mode: {self._image.mode}"""


if __name__ == "__main__":
    image_field = ImageField('images/Edward Hopper_Nighthawks_1942.jpg')
    image_field.image.show()

