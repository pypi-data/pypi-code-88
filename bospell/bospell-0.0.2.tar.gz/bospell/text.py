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
        self.suggestions = []

    def correct(self):
        if self.suggestions:
            pass

        for token in self.tokens:
            if self.spellcheck.is_error(token):
                suggestions = self.spellcheck.candidates(token.text, 5)
                span = Span(start=token.start, end=token.start + token.len)
                self.suggestions.append(Suggestions(candidates=suggestions, span=span))
