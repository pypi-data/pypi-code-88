from __future__ import print_function

import re
from builtins import str


class Converter(object):
    def __init__(self, split, valid, action):
        self.pattern = re.compile(split, re.UNICODE)
        self.word_cls = get_word_cls(valid, action)

    def __call__(self, text, no_diacritics=False):
        words = []

        word = None
        for string in self.pattern.split(text):
            word = self.word_cls(string, prev=word)
            words.append(word)

        output = "".join(map(str, words))

        if no_diacritics:
            output = asciilator()

        return ''.join(map(str, words))


def applier(*funcs):
    def _(text):
        for func in funcs:
            text = func(text)
        return text

    return _


def get_word_cls(valid, action):
    valid = set(valid)

    class Word(object):
        def __init__(self, word='', prev=None, next_=None):
            self._word = word
            self._prev = prev
            self._next = next_
            if prev is not None:
                prev.set_next(self)

        def __repr__(self):
            return repr(self._word)

        def __str__(self):
            if not self:
                return self._word

            p, n, w = self.get_prev(), self.get_next(), action(self._word)

            if self.is_upper() and (p and p.is_upper() or n and n.is_upper()):
                return w.upper()

            if w and self._word.istitle():
                return w[0].upper() + w[1:].lower()

            return w

        def __bool__(self):
            return not set(self._word.upper()) - valid

        __nonzero__ = __bool__

        def get_next(self):
            if self._next is not None:
                if self._next:
                    return self._next
                self._next = self._next.get_next()
                return self._next

        def get_prev(self):
            if self._prev is not None:
                if self._prev:
                    return self._prev
                self._prev = self._prev.get_prev()
                return self._prev

        def is_upper(self):
            return self._word.isupper()

        def set_next(self, next_):
            self._next = next_

    return Word


def replacer(d):
    def _(text):
        for i, o in d.items():
            text = text.replace(i, o)
        return text

    return _


def translator(*args):
    trans = str.maketrans(*args)

    def _(text):
        return text.translate(trans)

    return _
