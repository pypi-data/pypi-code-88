import abc
from typing import Any


class CellFormatter(abc.ABC):
    """
    Subclasses of this class can be used with CSVParser to determine the output of the parser on cells in the
    CSV file. A CellFormatter object passed to the constructor of a CSVParser will be given a chance to format
    the resulting text data of each text when it is parsed by the parser. After parsing out a text, the format
    method of the parser's CellFormatter object is called and then the content is placed in the data structure that
    is returned by the CSVParser object. """

    @abc.abstractmethod
    def format(self, content: str) -> Any:
        """Receives a single text's content during parsing of a CSV in CSVParser and should return the
        the text's content post formatting. Formatting can be arbitrary.

        A class should implement this method in order to be passed to the __init__ of CSVParser. Inheriting
        this class is not required, but it is recommended

        :param content: the content of the CSV text parsed by the CSVParser
        :raises ParseError: if the method cannot parse the content string. If CSVParser sets self.debug to True,
                    then this error is caught and a new error with more information is raised `from` this error.
                    Otherwise, this error is raised unchanged
        :returns: the result of formatting the text
        """
        pass


class DefaultCellFormatter(CellFormatter):
    """
    Does not change the contents of a CSV text. Exists as the default option in CSVParser
    """

    def format(self, content: str) -> str:
        return content


class CleanedCellFormatter(CellFormatter):
    """
    Removes whitespace other than a plain space and double quotes from the content of a CSV text. Since newlines
    are supported inside of double quoted cells by the CSVParser, this will remove them among other the other things
    listed.
    """

    def format(self, content: str) -> str:
        def cleaned(s: str) -> str:
            return s.replace('\r', '').replace('\n', '').replace('\t', '').replace('"', '')

        return cleaned(content)
