import pyglet

from pyglet.gl import *
from .vector import Vector


class Sprite:
    colors = {
        "BLACK": (0, 0, 0, 255),
        "WHITE": (255, 255, 255, 255),
        "RED": (255, 0, 0, 255),
        "GREEN": (0, 255, 0, 255),
        "CYAN": (0, 255, 255, 255),
        "RUSTY": (139, 49, 3, 255),
        "ORANGE": (255, 125, 0, 255),
        "YELLOW": (255, 255, 0, 255),
        "PINK": (255, 105, 180, 255),
        "SIENNA": (160, 82, 45, 255),
        "BLUE": (0, 0, 255, 255),
        "PURPLE": (255, 0, 255, 255),
    }

    def __init__(self, sprite, offset=Vector.new(0.0, 0.0)):
        self.sprite = sprite

        self.offset = offset

        self.label = pyglet.text.Label(
            self.sprite,
            font_name='Consolas',
            font_size=13,
            anchor_x='center',
            anchor_y='center'
        )

        self._color = "WHITE"

        self.color = self._color

    def render(self, environment, global_frame, transform):
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

        t = transform.from_perspective(
            environment.transform,
            origin=environment.origin * environment.transform.scale
        )

        offset = Vector.rotate(self.offset, t.angle)

        glTranslatef(
            t.pos[0] + offset[0],
            t.pos[1] + offset[1],
            0.0
        )
        glScalef(
            t.scale[0],
            t.scale[1],
            1.0
        )
        glRotatef(t.angle, 0.0, 0.0, 1.0)

        self.label.draw()

        glLoadIdentity()

    def set_sprite(self, new_sprite):
        self.label.text = new_sprite

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if type(value) is str:
            value = self.colors[value]
        self._color = value
        self.label.color = value

    def set_anchor_x(self, value):
        # TO-DO(?): make defines for LEFT, CENTER, RIGHT.
        """
            Values between "left", "center", "right".
        """
        self.label.anchor_x = value

    def set_anchor_y(self, value):
        """
            Values between "bottom", "baseline", "center", "top".
        """
        self.label.anchor_y = value

    """
        These two are useless.
        Sprite(".").height == Sprite("o").height == Sprite("@").height

    @property
    def height(self):
        return self.label.content_height

    @property
    def width(self):
        return self.label.content_width
    """
