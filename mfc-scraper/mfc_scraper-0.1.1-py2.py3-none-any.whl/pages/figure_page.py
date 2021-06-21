from bs4 import BeautifulSoup

from mfc_scraper.locators.figure_page_locators import FigurePageLocators
from mfc_scraper.parsers.figure_data import FigureDataParser


class FigurePage:
    def __init__(self, figure_id: int, page_content: str):
        self.soup = BeautifulSoup(page_content, "html.parser")
        self.id = figure_id

    @property
    def data(self):
        return FigureDataParser(self.id, self.soup.select_one(FigurePageLocators.ALL_DATA))
