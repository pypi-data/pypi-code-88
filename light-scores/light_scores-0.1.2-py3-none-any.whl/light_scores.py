"""Calculate bm scores of two lists."""
from typing import List, Union
import numpy as np

import nltk
from rank_bm25 import BM25Okapi

# from loguru import logger
import logzero
from logzero import logger

from light_scores.normalize import normalize

logzero.loglevel(20)
PUNCTUATION = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'


def light_scores(
    text_en: Union[str, List[str]],
    text_tr: Union[str, List[str]],
    norm: bool = False,
    remove_stopwords: bool = False,
    clean: bool = True,
    lower: bool = True,
) -> np.ndarray:
    """Calculate bm scores of two lists.

    norm: bool = False
    remove_stopwords: bool = False
    clean: bool = True
    lower: bool = True

    import nltk
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('wordnet')
    nltk.download('stopwords')
    """
    if isinstance(text_en, str):
        text_en = [elm.strip() for elm in text_en.splitlines() if elm.strip()]
    if isinstance(text_tr, str):
        text_tr = [elm.strip() for elm in text_tr.splitlines() if elm.strip()]

    # List of str

    def seg_to_words(lines, norm=True):
        if isinstance(lines, str):
            lines = [lines]
        res = []
        for line in lines:
            if lower:
                line = line.lower()
            if norm:
                words = normalize(line)
            else:
                words = nltk.word_tokenize(line)
            res.append(words)

        return res

    # tokenize to words, normalize if norm is True
    token_list_en = seg_to_words(text_en, norm)
    token_list_tr = seg_to_words(text_tr, norm)

    # logger.debug(f" befoe stopwords removed, token_list_en[:10: {token_list_en[:10}")

    # lowercase, clean, split,
    if remove_stopwords:
        # remove stop words
        from nltk.corpus import stopwords
        stop_words_eng = set(stopwords.words('english'))

        def remove_(words_lines: List[List[str]]) -> List[str]:
            res = []
            for line in words_lines:
                _ = [w for w in line if w.lower() not in stop_words_eng]
                res.append(_)
            return res

        token_list_en = remove_(token_list_en)
        token_list_tr = remove_(token_list_tr)

        logger.debug(f" stopwords removed: {token_list_en[:10]}")

    tokenized_corpus = token_list_en
    logger.debug(f" tokenized_corpus: {tokenized_corpus[:10]}")

    logger.debug(f" query: {token_list_tr[:10]}")

    # tokenized_corpus = []
    if not tokenized_corpus:
        raise Exception(" tokenized_corpus is empty, something has gone awry.")

    bm25 = BM25Okapi(tokenized_corpus)

    corr_mat = []
    for idx, sent in enumerate(token_list_tr):
        corr = bm25.get_scores(sent)
        corr_mat.append(corr)

    # return np.array([1])
    # return np.array(corr_mat)
    return np.array(corr_mat).T
