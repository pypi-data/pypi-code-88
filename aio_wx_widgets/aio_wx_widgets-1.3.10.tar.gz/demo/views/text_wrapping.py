import logging

from demo.controller.text_wrapping_controller import TextWrappingController

from aio_wx_widgets.panels.panel import SimplePanel
from aio_wx_widgets.widgets import LabelledItem, Text
from aio_wx_widgets.widgets.experimental.bullet_text import BulletText
from aio_wx_widgets.widgets.experimental.fixed_grid import DynamicGrid, FixedGrid

_LOGGER = logging.getLogger(__name__)

LONG_TEXT = 10 * "very very long text that should just wrap.."


class TextWrappingView(SimplePanel[TextWrappingController]):
    """A text wrapping view test."""

    def populate(self):
        with self.add(DynamicGrid()) as grd:
            grd.add(Text(text=LONG_TEXT, wrap=True), col=1)
            grd.add(Text(text=LONG_TEXT, wrap=True), col=2)
        with self.add(FixedGrid()) as grd:
            grd.add_spacer()
            grd.add(Text(text=LONG_TEXT, wrap=True))
            grd.add_spacer()
        self.add(
            LabelledItem(
                label_text="This is the label", item=Text("Just text"), item_weight=3
            )
        )
        with self.add(FixedGrid()) as grd:
            grd.add_spacer()
            grd.add(BulletText(text=LONG_TEXT, wrap=True))
            grd.add_spacer()
