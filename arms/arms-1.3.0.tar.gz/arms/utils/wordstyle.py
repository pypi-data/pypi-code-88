from typing import Tuple, List, NamedTuple, Dict
from enum import Enum
from arms.utils.common import captitalize
import re


class WordStyle(Enum):
    upper_camel = 1
    lower_camel = 2
    upper_snake = 3
    lower_snake = 4
    other = 5


class WordSeed(NamedTuple):
    word_style: WordStyle
    tokens: List[str]

    def __str__(self) -> str:
        if not self.tokens:
            return ''
        elif self.word_style == WordStyle.upper_camel:
            return ''.join(token.capitalize() for token in self.tokens)
        elif self.word_style == WordStyle.lower_camel:
            return self.tokens[0] + ''.join(token.capitalize() for token in self.tokens[1:])
        elif self.word_style == WordStyle.upper_snake:
            return '_'.join(self.tokens).upper()
        elif self.word_style == WordStyle.lower_snake:
            return '_'.join(self.tokens)
        else:
            return ''.join(self.tokens)

    @classmethod
    def of(cls, word: str) -> 'WordSeed':
        if '_' in word:
            if re.match(r'^[a-z_]+$', word):
                return WordSeed(WordStyle.lower_snake, word.split('_'))
            elif re.match(r'^[A-Z_]+$', word):
                return WordSeed(WordStyle.lower_snake, [seg.lower() for seg in word.split('_')])
        elif re.match(r'^[A-Z][A-Za-z]+$', word):
            return WordSeed(WordStyle.upper_camel, [seg.lower() for seg in re.findall(r'[A-Z][a-z]*', word)])
        elif re.match(r'^[a-z][A-Za-z]+$', word):
            return WordSeed(WordStyle.lower_camel, [seg.lower() for seg in re.findall(r'[A-Z][a-z]*', captitalize(word))])
        return WordSeed(WordStyle.other, [word])


def replace_dict(oldword: str, newword: str):
    old_word_seed = WordSeed.of(oldword)
    new_word_seed = WordSeed.of(newword)
    return {
        str(WordSeed(word_style, old_word_seed.tokens)): str(WordSeed(word_style, new_word_seed.tokens))
        for word_style
        in [WordStyle.upper_snake, WordStyle.lower_snake, WordStyle.upper_camel, WordStyle.lower_camel, ]
    }


def replace_all(text: str, repl_dict: Dict):
    for in_word, out_word in repl_dict.items():
        text = text.replace(in_word, out_word)
    return text
