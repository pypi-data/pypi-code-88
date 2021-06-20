from abc import ABC, abstractmethod

from botok import WordTokenizer


class TokenBase:
    def __init__(self, form, pos, lemma):
        self.form = form
        self.pos = pos
        self.lemma = lemma


class TokenizerBase(ABC):
    """All tokenizer should be subclass of TokenizerBase."""

    @abstractmethod
    def tokenize(self, text):
        pass


class BotokWordTokenizer(TokenizerBase):
    def __init__(self, config):
        self.config = config
        self.tokenizer = WordTokenizer()

    def tokenize(self, text):
        return self.tokenizer.tokenize(text)
