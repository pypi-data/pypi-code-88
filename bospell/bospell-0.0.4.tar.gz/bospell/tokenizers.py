from abc import ABC, abstractmethod
from typing import List

from botok import Token, TokenMerge, WordTokenizer
from botok.text.modify import is_mistake


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
        tokens = self.tokenizer.tokenize(text)
        tokens = self.__merge_none_word_tokens(tokens)
        return tokens

    def __merge_none_word_tokens(self, tokens: List[Token]):
        merged_tokens = []
        current_mistake_token = None
        for token in tokens:
            if is_mistake(token):
                if current_mistake_token:
                    merge_token = TokenMerge(current_mistake_token, token)
                    current_mistake_token = merge_token.merge()
                else:
                    current_mistake_token = token
            else:
                if current_mistake_token:
                    merged_tokens.append(current_mistake_token)
                    current_mistake_token = None
                merged_tokens.append(token)
        else:
            if current_mistake_token:
                merged_tokens.append(current_mistake_token)

        return merged_tokens
