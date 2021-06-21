"""Lemmatize nltk pos tag to wodnet tag."""
from typing import List

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

lemmatizer = WordNetLemmatizer()


def convert_tag(tag: str) -> str:
    """Convert nltk pos tag to wodnet tag."""
    res = tag[0].lower()

    if res in ["j"]:
        res = "a"
    if res not in ["a", "v", "n", "r"]:
        res = "n"

    return res


def normalize(text: str) -> List[str]:
    """Lemmatize text.

    [lemmatize(word, convert_tag(tag)) for word, tag in pos_tag(word_tokenize(text))]

    20s/1000 lines shakespeare
    3min 35s 210s/lines shakespeare
    >>> text = 'I am loving it'
    >>> normalize('I am loving it')[1] in ["be"]
    True
    """
    words = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(words)

    res = []
    for word, tag in tagged:
        _ = convert_tag(tag)
        res.append(lemmatizer.lemmatize(word, _))

    return res
