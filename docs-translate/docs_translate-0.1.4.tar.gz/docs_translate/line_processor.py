from typing import TYPE_CHECKING

from docs_translate.translator import get_translator_by_service_name, is_untranslated_paragraph
from docs_translate.util import get_indentation

if TYPE_CHECKING:
    from docs_translate.settings import Settings


class Line:
    code_mark: str = '```'

    new_line_symb = '\n'

    def __init__(self, settings: 'Settings', line: str) -> None:
        self.settings = settings
        self._translator = get_translator_by_service_name(settings.service_name)
        self._is_untranslated_paragraph: bool = is_untranslated_paragraph(settings.service_name, line, settings.source_lang)
        self._line: str = line
        self._translated_line = ''

    def __str__(self) -> str:
        return self._line

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}: "{self._line}"'

    @property
    def original(self) -> str:
        return self._line

    @property
    def translated(self) -> str:
        if not self._translated_line and self.can_be_translated():
            self._translate()
        return self._translated_line or self.original

    @property
    def fixed(self) -> str:
        translated = self.translated
        if self._line.startswith(' '):
            translated = ''.join([get_indentation(self._line), self.translated])
        if self._line.endswith('\n') and not translated.endswith('\n'):
            translated = ''.join([translated, '\n'])
        return translated

    def is_code_block_border(self) -> bool:
        if self._line == self.code_mark:
            return True
        return self._line.startswith(self.code_mark) and not self._line.endswith(
            self.code_mark
        )

    def can_be_translated(self) -> bool:
        return (
            not self._is_empty_line()
            and not self.is_code_block_border()
            and not self._is_single_code_line()
            and self._is_untranslated_paragraph
        )

    def _translate(self) -> None:
        try:
            self._translated_line = self._translator(
                self._line,
                from_language=self.settings.source_lang,
                to_language=self.settings.target_lang
            )
        except TypeError:
            pass

    def _is_single_code_line(self) -> bool:
        return (
            self._line.startswith(self.code_mark)
            and self._line.endswith(self.code_mark)
            and len(self._line) > 3
        )

    def _is_empty_line(self) -> bool:
        if self._line == self.new_line_symb:
            return True
        return not bool(self._line)
