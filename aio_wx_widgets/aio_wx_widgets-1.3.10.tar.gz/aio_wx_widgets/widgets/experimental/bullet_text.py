"""Experimental bullet text"""

from aio_wx_widgets.containers import Grid
from aio_wx_widgets.widgets import Text


class BulletText(Grid):
    """Text with a bullet."""

    def __init__(self, text: str, font_scale=1, bullet: str = "-", wrap=True):
        self._text = str(text)
        self._font_scale = font_scale
        self._bullet = bullet
        self._wrap = wrap

        super().__init__()

    def init(self, parent, *args, **kwargs):
        super().init(parent)
        self.add(Text(self._bullet, font_size=self._font_scale))
        self.add(Text(self._text, font_size=self._font_scale, wrap=True), weight=1)
        return self
