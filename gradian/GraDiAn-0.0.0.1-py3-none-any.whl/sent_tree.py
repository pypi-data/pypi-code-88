import uuid
from typing import List

from nltk.tree import Tree
from spacy.tokens import Token

from gradian.utils import load_spacy_en_trf


class SentTree():
    def __init__(self, token: str, pos: str, dependency: str, sentiment: float, children: List = []):
        self.tid = token+pos+str(uuid.uuid4())
        self.token = token
        self.pos = pos
        self.sentiment = sentiment
        self.dependency = dependency
        self.children = children

    @classmethod
    def from_spacy_token(cls, t: Token, use_spacy_text_blob: bool = False):
        if use_spacy_text_blob:
            if t.n_lefts + t.n_rights > 0:
                return SentTree(t.text, t.pos_, t.dep_,
                                round(t._.polarity),
                                children=[cls.from_spacy_token(child, True) for child in
                                          t.children])
            else:
                return SentTree(t.text, t.pos_, t.dep_,
                                round(t._.polarity))
        else:
            if t.n_lefts + t.n_rights > 0:
                return SentTree(t.text, t.pos_, t.dep_, t.sentiment,
                                children=[cls.from_spacy_token(child) for child in
                                          t.children])
            else:
                return SentTree(t.text, t.pos_, t.dep_, t.sentiment)

    @classmethod
    def from_string(cls, s: str, use_spacy_text_blob: bool = False):
        nlp = load_spacy_en_trf()
        doc = nlp(s)
        trees = list()
        for sent in doc.sents:
            trees.append(cls.from_spacy_token(sent.root, use_spacy_text_blob))
        return trees

    def _get_attr(self, attr: str):
        if hasattr(self, attr):
            return getattr(self, attr)
        else:
            raise AttributeError('Attribute ' + attr + ' not found.')

    def attr_tree(self, attr: str, token: bool = False) -> Tree:
        val = self._get_attr(attr)

        if len(self.children) > 0:
            if token:
                return Tree(f'{self.token}:  {val}',
                            [child.attr_tree(attr, token) for child in
                                        self.children])
            else:
                return Tree(str(val), [child.attr_tree(attr) for child in
                                        self.children])
        else:
            if token:
                return self.token + ': ' + str(val)
            else:
                return str(val)

    def multi_attr_tree(self, attrs: List[str], token: bool = False) -> Tree:
        vals = ':'.join([str(self._get_attr(attr)) for attr in attrs])

        if len(self.children) > 0:
            if token:
                return Tree(f'{self.token}:{vals}',
                            [child.multi_attr_tree(attrs, token) for child in
                                        self.children])
            else:
                return Tree(str(vals), [child.multi_attr_tree(attrs) for child in
                                        self.children])
        else:
            if token:
                return self.token + ':' + vals
            else:
                return vals

    def equal_attr(self, t: object, attr: str) -> bool:
        val = self._get_attr(attr)

        if isinstance(t, SentTree):
            if len(self.children) == 0:
                return val == getattr(t, attr)
            else:
                children_eq = [i.equal_attr(j, attr) for i,j in zip(self.children,
                                                             t.children)]
                return val == getattr(t, attr) and set(children_eq) == {True}
        else:
            return False

