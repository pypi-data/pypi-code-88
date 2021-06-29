import abc
import re
from typing import Optional


class ParseError(ValueError):
    pass


class CellParser(abc.ABC):
    """
    A class that can take a string and parse out the CSV cells in the string. String should begin with the first CSV
    text. It can have an arbitrary number of cells afterwards.

    Classes must implement the `parse` method in order to be used for this. See below for a description of the
    signature and contract of that method

    Objects of this class can be passed to the __init__ of CSVParser in order to parse cells of a CSV
    """

    def __init_subclass__(cls) -> None:
        if 'parse' in cls.__dict__:
            raise AttributeError("Classes that subclass 'CellParser' must not override the 'parse' method")
        return super().__init_subclass__()

    @abc.abstractmethod
    def parser_hook(self, text: str) -> tuple[str, int, bool]:
        """
        A method that takes a string of 1 or more CSV cells and parses out the first cell in that string. It returns
        a tuple of the following: 0th - the contents of the first cell in the string `text`; 1st - the first index
        after the end of that cell 2nd - whether or not this the row has ended--i.e. the cell being returned is the
        last cell in a row.

        You must implement this method with the described signature in order to be used in CSVParser
        :param text: the string containing at least 1 CSV cell which must begin at index 0 of the string
        :return: a tuple containing the cell content, first index in the string after the cell, and whether
                 the cell being returned is the final cell in a row
        """
        pass

    def parse(self, text: str) -> tuple[str, int, bool]:
        """
        Called in the CSVParser so that the superclass CellParser can intervene before returning the values to
        the CSVParser. Classes should *NOT* override this method and instead should override parser_hook.
        """
        text, end, done = self.parser_hook(text)
        return text, end, done


class PlainCellParser(CellParser):
    """
    Parses cells that contain no special characters and are not quoted.
    """

    def parser_hook(self, text: str) -> tuple[str, int, bool]:
        def index(string: str, pattern: str, start: Optional[int] = 0):
            try:
                return string.index(pattern, start)
            except ValueError:
                return float('inf')

        comma = index(text, ',')
        newline = index(text, '\n')
        eot = index(text, '\0')
        end = min(comma, newline, eot)
        if end == float('inf'):
            end = len(text)
        content = text[0:end]
        row_done = not (comma < eot and comma < newline)
        end_index = end + 1
        return content, end_index, row_done


class QuotedCellParser(CellParser):
    """
    Parses cells that are quoted by double quotes and can contain special characters including new line but NOT including
    additional double quotes. Empty quoted cells are also allowed
    """

    def parser_hook(self, text: str) -> tuple[str, int, bool]:
        quoted_cell = re.compile(r'"(.*?)"([,\n\x00])', re.DOTALL | re.MULTILINE)
        value = quoted_cell.match(text)
        if value is None:
            raise ParseError("Cannot match quoted text in string starting at {}".format(0))

        content = value.group(1)
        end_index = value.span()[1]
        row_done = value.group(2) == '\n' or value.group(2) == '\x00'
        return content, end_index, row_done


class DefaultCellParser(QuotedCellParser, PlainCellParser):
    """
    Default parser for the CSVParser class: can parse either quoted or plain cells depending on the first character of
    the text that is passed. 
    """

    def parser_hook(self, text: str) -> tuple[str, int, bool]:
        if text[0] == '"':
            return QuotedCellParser.parser_hook(self, text)
        else:
            return PlainCellParser.parser_hook(self, text)
