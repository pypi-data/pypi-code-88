from typing import TextIO

from csvtea.cells import CellParser, DefaultCellParser, ParseError
from csvtea.format import DefaultCellFormatter, CellFormatter


class CSVParser:
    def __init__(
            self,
            file: TextIO,
            parser: CellParser = DefaultCellParser(),
            formatter: CellFormatter = DefaultCellFormatter(),
            *,
            debug: bool = False
    ):
        self.parser = parser
        self.formatter = formatter
        self.debug = debug

        self.text = file.read().strip('\r\n') + '\0'

    def parse(self) -> list[list[str]]:
        cells = []
        row = []
        text = self.text
        while text:
            try:
                cell, cell_end, row_done = self.parser.parse(text)
            except ParseError as e:
                if self.debug:
                    error = ParseError(f'Error in parse. Cannot match quoted key. '
                                       f'Text is {text!r}\ncells length is {len(cells)}\n'
                                       f'row length is {len(row)}')
                    raise error from e
                else:
                    raise
            cell = self.formatter.format(cell)
            row.append(cell)
            if row_done:
                cells.append(row)
                row = []
            text = text[cell_end:]
        return cells
