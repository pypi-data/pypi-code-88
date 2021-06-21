from bs4 import BeautifulSoup

from mfc_scraper.locators.figure_collection_page_locators import FigureCollectionPageLocators
from mfc_scraper.parsers.figure import FigureParser


class NoFiguresFound(RuntimeError):
    pass


class FigureCollectionPage:
    def __init__(self, page_content: str):
        self.soup = BeautifulSoup(page_content, "html.parser")

    @property
    def figures(self):
        elements = self.soup.select(FigureCollectionPageLocators.FIGURES)
        if not len(elements):
            raise NoFiguresFound("No figures found")

        return [FigureParser(e) for e in elements]
