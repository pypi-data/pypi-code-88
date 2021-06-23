from pathlib import Path
from typing import IO, TYPE_CHECKING, Any, List

from docs_translate.line_processor import Line
from docs_translate.logs import logger

if TYPE_CHECKING:
    from docs_translate.settings import Settings


class FileTranslator:
    default_open_mode: str = 'r'
    default_write_mode: str = 'w'
    default_encoding: str = 'utf8'

    def __init__(self, settings: 'Settings', file_path: Path, copy_path: Path) -> None:
        self.settings = settings
        self.file_path: Path = file_path
        self.copy_path: Path = copy_path
        self.file_contents_with_translation: list = []
        self.code_block: bool = False

    def __enter__(self) -> 'FileTranslator':
        self.__r_translating_file: IO = self.file_path.open(self.default_open_mode, encoding=self.default_encoding)
        return self

    def __exit__(self, *args: Any, **kwargs: Any) -> None:
        self.__r_translating_file.close()

    def translate(self) -> None:
        lines = self._get_lines()
        for _line in lines:
            line = Line(self.settings, _line)
            self.code_block = (
                not self.code_block if line.is_code_block_border() else self.code_block
            )
            if line.can_be_translated() and not self.code_block:
                self.file_contents_with_translation.append(line.fixed)
            else:
                self.file_contents_with_translation.append(line.original)
        self._write_translated_data_to_file()

    def _get_lines(self) -> List[str]:
        lines = self.__r_translating_file.readlines()
        logger.info(f'Got {len(lines)} lines to process')
        return lines

    def _write_translated_data_to_file(self) -> None:
        with open(self.copy_path, mode=self.default_write_mode, encoding=self.default_encoding) as writer:
            writer.writelines(self.file_contents_with_translation)
