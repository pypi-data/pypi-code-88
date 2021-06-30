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

# The following code has been inspired by the linear gradient
# described in http://bsou.io/posts/color-gradients-with-python

from PIL import Image


class ColorGradient:
    @staticmethod
    def build_image_from_color_gradient(width, color_gradient):
        """

        :param width:
        :param color_gradient:
        :return: a PIL.Image
        """
        height = len(color_gradient)
        image = Image.new('RGB', (width, height))
        image_data = image.load()

        for x in range(image.size[0]):
            for y in range(image.size[1]):
                [r, g, b] = color_gradient[y]
                # fill the image from bottom to top
                image_data[x, image.size[1] - y - 1] = (r, g, b)

        return image

    @staticmethod
    def build_linear_color_gradient(color_list):
        assert len(color_list) > 1, 'color_list should contain at least two colors'

        def build_gradient_from_two_colors(start_color, end_color):
            # TODO: rewrite this to allow multiple byte change between start_color and end_color
            def extend_range(a, b):
                return (b + 1) if a <= b else (b - 1)

            def range_step(a, b):
                return 1 if a <= b else -1

            gradient = []

            (rs, gs, bs) = start_color
            (re, ge, be) = end_color
            # components will be the start and end colors of a linear gradient
            r_gradient = range(rs, extend_range(rs, re), range_step(rs, re))
            g_gradient = range(gs, extend_range(gs, ge), range_step(gs, ge))
            b_gradient = range(bs, extend_range(bs, be), range_step(bs, be))

            # this simplistic approach doesn't work if more than one component_select/byte changes
            for r in r_gradient:
                for g in g_gradient:
                    for b in b_gradient:
                        gradient.append((r, g, b))

            return gradient

        # build gradient from a list of colors
        gradient = []
        for cli in range(len(color_list) - 1):
            # get color components of color n and n+1
            # they will be the start and end colors of a new linear gradient
            gradient.extend(build_gradient_from_two_colors(color_list[cli], color_list[cli + 1]))

            # remove the last color of the gradient as it will be the first
            # of the next gradient
            gradient = gradient[:-1]

        # add the last color of the color list to the gradient to ensure the gradient is complete
        gradient.append(color_list[-1])

        return gradient

    def __init__(self, color_list):
        self.gradient = ColorGradient.build_linear_color_gradient(color_list)
        self.max_color_index = len(self.gradient) - 1

    def get_color(self, value, max_value=None):
        if max_value is not None:
            value = value * self.max_color_index / max_value

        return self.gradient[int(value)]

    def get_image(self, width):
        return ColorGradient.build_image_from_color_gradient(width, self.gradient)

    @staticmethod
    def create(gradient_name='bcgyormw'):
        color_lists = {'bcgyormw': ((0x00, 0x00, 0x80), (0x00, 0x00, 0xff), (0x00, 0xff, 0xff),
                                    (0x00, 0xff, 0x00), (0xff, 0xff, 0x00), (0xff, 0x00, 0x00),
                                    (0xff, 0x00, 0xff), (0xff, 0xff, 0xff)),
                       'cgy': ((0x00, 0xff, 0xff), (0x00, 0xff, 0x00), (0xff, 0xff, 0x00))}

        return ColorGradient(color_lists[gradient_name])


if __name__ == "__main__":
    # default gradient
    default_gradient = ColorGradient.create()
    print('default color gradient has', default_gradient.max_color_index + 1, 'colors')
    default_gradient_image = default_gradient.get_image(100)
    print('default color gradient image size is', default_gradient_image.size)
    default_gradient_image.show()

    cgy_gradient = ColorGradient.create(gradient_name='cgy')
    print('cgy color gradient has', cgy_gradient.max_color_index + 1, 'colors')
    cgy_gradient.get_image(100).show()
