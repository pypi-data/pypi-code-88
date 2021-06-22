import re
from typing import Dict, List, Union
from datetime import date
from bs4 import element

from mfc_scraper.locators.figure_page_locators import FigurePageLocators


class FigureDataParser:
    """
    Parses the content of an HTML element to retrieve complete information
    about a particular figure
    """

    def __init__(self, figure_id: int, parent: element.Tag):
        self._parent = parent
        self._data = None
        self.id = figure_id

    def __get_all_data(self) -> Dict[str, element.Tag]:
        if not self._data:
            data_names = [e.string.lower() for e in self._parent.select(FigurePageLocators.DATA_NAME)]
            data_values = self._parent.select(FigurePageLocators.DATA_VALUE)
            self._data = dict(zip(data_names, data_values))

        return self._data

    @property
    def origin(self) -> str:
        try:
            return str(self.__get_all_data().get("origin").select_one("span").string)
        except AttributeError:
            return "UNDEFINED"

    @property
    def characters(self) -> List[str]:
        try:
            return [str(e.string) for e in self.__get_all_data().get("characters").select("span")]
        except AttributeError:
            try:
                return [str(self.__get_all_data().get("character").select_one("span").string)]
            except AttributeError:
                return []

    @property
    def companies(self) -> List[str]:
        try:
            return [str(e.string) for e in self.__get_all_data().get("companies").select("span")]
        except AttributeError:
            try:
                return [str(self.__get_all_data().get("company").select_one("span").string)]
            except AttributeError:
                return []

    @property
    def classifications(self) -> List[str]:
        try:
            return [str(e.string) for e in self.__get_all_data().get("classifications").select("span")]
        except AttributeError:
            try:
                return [str(self.__get_all_data().get("classification").select_one("span").string)]
            except AttributeError:
                return []

    @property
    def version(self) -> str:
        try:
            return str(self.__get_all_data().get("version").select_one("a").string)
        except AttributeError:
            return "UNDEFINED"

    @property
    def image_urls(self):
        try:
            return [self._parent.select_one(FigurePageLocators.PICTURE).attrs.get("src")]
        except AttributeError:
            return []

    @property
    def release_date(self) -> date:
        try:
            raw_date_str = self.__get_all_data().get("release date").select_one("a").attrs.get("href")
            matcher = re.search("year=(\d+)&month=(\d+)", raw_date_str)
            return date(int(matcher.group(1)), int(matcher.group(2)) or 1, 1)
        except ValueError:
            print(raw_date_str)
            return date(1970, 1, 1)
        except AttributeError:
            return date(1970, 1, 1)

    def to_dict(self) -> Dict[str, Union[List, str, int]]:
        return {
                "id": self.id,
                "origin": self.origin,
                "characters": self.characters,
                "companies": self.companies,
                "classifications": self.classifications,
                "version": self.version,
                "release_date": self.release_date.strftime("%Y/%m"),
                "image_urls": self.image_urls,
            }
