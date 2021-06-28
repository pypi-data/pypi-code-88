from collections import Counter
from typing import List

import spacy

from gradian.utils import load_spacy_en_trf


class SDC(Counter):
    def __init__(self, dependencies=None, **kwargs):
        if dependencies is None:
            self.dependencies = [
                'ROOT', 'acl', 'acomp', 'advcl', 'advmod', 'agent', 'amod', 'appos',
                'attr', 'aux', 'auxpass', 'case', 'cc', 'ccomp', 'compound', 'conj',
                'csubj', 'csubjpass', 'dative', 'dep', 'det', 'dobj', 'expl', 'intj',
                'mark', 'meta', 'neg', 'nmod', 'npadvmod', 'nsubj', 'nsubjpass', 'nummod',
                'oprd', 'parataxis', 'pcomp', 'pobj', 'poss', 'preconj', 'predet', 'prep',
                'prt', 'punct', 'quantmod', 'relcl', 'xcomp'
            ]
        else:
            self.dependencies = dependencies
        super().__init__(**kwargs)

    def update(self, x):
        if x is None:
            return
        if x is dict:
            assert set(x.keys()).issubset(self.dependencies)
        else:
            assert set(x).issubset(self.dependencies)
        super().update(x)

    @classmethod
    def from_string_arr(cls, texts: List[str]):
        nlp = load_spacy_en_trf(excludes=['tokenizer', 'tagger', 'ner',
                                          'lemmatizer', 'textcat'])
        sdc = SDC()
        for doc in nlp.pipe(texts):
            sdc.update([token.dep_ for token in doc]) 
        return sdc

    @classmethod
    def from_string(cls, s: str):
        nlp = load_spacy_en_trf(excludes=['tokenizer', 'tagger', 'ner',
                                          'lemmatizer', 'textcat'])
        sdc = SDC()
        doc = nlp(s)
        sdc.update([token.dep_ for token in doc]) 
        return sdc
