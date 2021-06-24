from __future__ import annotations

import logging
from pathlib import Path
from typing import TYPE_CHECKING

from aio_wx_widgets.containers.grid import Grid
from aio_wx_widgets.containers.group import Section
from aio_wx_widgets.panels.panel import SimplePanel
from aio_wx_widgets.widgets.text import Text

if TYPE_CHECKING:
    from demo.controller.controller_one import ControllerOne

_LOGGER = logging.getLogger(__name__)

IMAGE_FOLDER = (Path(__file__).parent) / "image"


class ViewOne(SimplePanel["ControllerOne"]):
    def __init__(self, parent, controller: "ControllerOne"):
        super().__init__(parent, controller, scrollable=False)

    def populate(self):
        """Populate this view."""

        with self.add(Section("Min width")) as grp:
            with grp.add(Grid()) as grd:
                grd.add(Text("This is a text exceeding 80 min size", min_width=80))
                grd.add(Text("Other text."))

            with grp.add(Grid()) as grd:
                grd.add(Text("text < 80", min_width=80))
                grd.add(Text("Other text."))
