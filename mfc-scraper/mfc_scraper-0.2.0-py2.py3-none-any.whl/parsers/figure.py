from bs4 import element
import re

from mfc_scraper.locators.figure_locators import FigureLocators


class FigureParser:
    """
    Parses the content of an HTML element to retrieve basic information
    about a particular figure within a list
    """

    def __init__(self, parent: element.Tag):
        self._parent = parent

    def __repr__(self) -> str:
        return f"'{self.name}' ({self.id})"

    @property
    def id(self) -> int:
        id_str = self._parent.select_one(FigureLocators.ID).attrs.get("content")
        matcher = re.search("\d+\:(\d+)", id_str)
        return matcher.group(1)

    @property
    def name(self) -> str:
        return str(self._parent.select_one(FigureLocators.NAME).attrs.get("alt"))
