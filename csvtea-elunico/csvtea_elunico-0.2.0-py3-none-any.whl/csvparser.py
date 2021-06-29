from typing import TextIO

from csvtea.cells import CellParser, DefaultCellParser
from csvtea.format import DefaultCellFormatter, CellFormatter


class CSVParser:
    def __init__(self, file: TextIO, parser: CellParser = DefaultCellParser(),
                 formatter: CellFormatter = DefaultCellFormatter()):
        self.parser = parser
        self.formatter = formatter

        self.text = file.read().strip('\r\n') + '\0'

    def parse(self) -> list[list[str]]:
        cells = []
        row = []
        text = self.text
        while text:
            cell, cell_end, row_done = self.parser.parse(text)
            cell = self.formatter.format(cell)
            row.append(cell)
            if row_done:
                cells.append(row)
                row = []
            text = text[cell_end:]
        return cells
