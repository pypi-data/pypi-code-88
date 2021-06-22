from dataclasses import dataclass
from typing import List

from . import BoSpell, utils
from .config import Config, DefaultConfig
from .tokenizers import TokenizerBase


@dataclass
class Span:
    start: int
    end: int


@dataclass
class Suggestions:
    candidates: List[str]
    span: Span


class Text:
    """Class Text represents the corrected text."""

    def __init__(self, content, config: Config = DefaultConfig()):
        self.tokenizer: TokenizerBase = utils.load_class(config.tokenizer_class)(config)
        self.spellcheck: BoSpell = BoSpell(config=config)
        self.content: str = content
        self.tokens: List = self.tokenizer.tokenize(content)
        self._suggestions = {}
        self._corrected = ""

    @property
    def suggestions(self):
        if self._suggestions:
            return self._suggestions

        for idx, token in enumerate(self.tokens):
            if self.spellcheck.is_error(token):
                suggestions = self.spellcheck.candidates(token.text, 5)
                span = Span(start=token.start, end=token.start + token.len)
                self._suggestions[idx] = Suggestions(candidates=suggestions, span=span)

        return self._suggestions

    @property
    def corrected(self):
        if self._corrected:
            return self._corrected

        for idx, token in enumerate(self.tokens):
            if idx in self.suggestions:
                self._corrected += self.suggestions[idx].candidates[0]
            else:
                self._corrected += token.text
        return self._corrected
