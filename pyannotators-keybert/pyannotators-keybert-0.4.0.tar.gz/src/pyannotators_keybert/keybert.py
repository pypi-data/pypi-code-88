import os
import re
from collections import defaultdict
from enum import Enum
from functools import lru_cache
from typing import Type, List, cast
import icu as icu
import stopwordsiso
from keybert import KeyBERT
from pydantic import BaseModel, Field
from pymultirole_plugins.v1.annotator import AnnotatorParameters, AnnotatorBase
from pymultirole_plugins.v1.schema import Document, Annotation, Term
from sklearn.feature_extraction.text import CountVectorizer

_home = os.path.expanduser('~')
xdg_cache_home = os.environ.get('XDG_CACHE_HOME') or os.path.join(_home, '.cache')


class SBERTModel(str, Enum):
    paraphrase_mpnet_base_v2 = 'paraphrase-mpnet-base-v2'
    paraphrase_multilingual_mpnet_base_v2 = 'paraphrase-multilingual-mpnet-base-v2'
    paraphrase_MiniLM_L6_v2 = 'paraphrase-MiniLM-L6-v2'
    paraphrase_multilingual_MiniLM_L12_v2 = 'paraphrase-multilingual-MiniLM-L12-v2'
    # distiluse_base_multilingual_cased_v1 = 'distiluse-base-multilingual-cased-v1'


class KeyBERTParameters(AnnotatorParameters):
    model: SBERTModel = Field(SBERTModel.paraphrase_multilingual_mpnet_base_v2,
                              description="""Which [SentenceTransformers model)(
                            https://www.sbert.net/docs/pretrained_models.html) to use, can be one of:<br/>
                            <li>`paraphrase-mpnet-base-v2`
                            <li>`paraphrase-multilingual-mpnet-base-v2`
                            <li>`paraphrase-MiniLM-L6-v2`
                            <li>`paraphrase-multilingual-MiniLM-L12-v2`.""")
    term_label: str = Field("term",
                            description="Label to use for extracted keywords",
                            extra="label")
    top_n: int = Field(5,
                       description="Return the top n keywords/keyphrases.",
                       extra="advanced")
    use_maxsum: bool = Field(False,
                             description="Whether to use Max Sum Similarity for the selection of keywords/keyphrases.",
                             extra="advanced")
    use_mmr: bool = Field(False,
                          description="Whether to use Maximal Marginal Relevance (MMR) for the selection of keywords/keyphrases.",
                          extra="advanced")
    diversity: float = Field(0.5,
                             description="The diversity of the results between 0 and 1 if use_mmr is set to True.",
                             extra="advanced")
    nr_candidates: int = Field(20,
                               description="The number of candidates to consider if use_maxsum is set to True.",
                               extra="advanced")
    max_features: int = Field(100000,
                              description="If not None, build a vocabulary that only consider the top max_features ordered by term frequency across the corpus.",
                              extra="advanced")
    min_df: str = Field("1",
                        description="When building the vocabulary ignore terms that have a document frequency strictly lower than the given threshold. If it is a float in range of [0.0, 1.0[, the parameter represents a proportion of documents, if is an integer >= 1 absolute counts.",
                        extra="advanced")
    max_df: str = Field("1.0",
                        description="When building the vocabulary ignore terms that have a document frequency strictly higher than the given threshold (corpus-specific stop words). If it is a float in range of [0.0, 1.0], the parameter represents a proportion of documents, if is an integer > 1 absolute counts.",
                        extra="advanced")
    ngram_range: List[int] = Field([1, 1],
                                   description="The lower and upper boundary of the range of n-values for different word n-grams or char n-grams to be extracted. All values of n such such that min_n <= n <= max_n will be used. For example an ngram_range of (1, 1) means only unigrams, (1, 2) means unigrams and bigrams, and (2, 2) means only bigrams.",
                                   extra="advanced")
    use_lower: bool = Field(True,
                            description="Use lower case tokens",
                            extra="advanced")
    stopwords: str = Field(None,
                           description="List of comma-separated language codes to use stopwords with tokenizer",
                           extra="advanced")


class KeyBERTAnnotator(AnnotatorBase):
    """[SentenceTransformers](https://www.sbert.net/docs/installation.html#install-sentencetransformers) KeyBERT.
    """

    # cache_dir = os.path.join(xdg_cache_home, 'trankit')

    def annotate(self, documents: List[Document], parameters: AnnotatorParameters) \
            -> List[Document]:
        params: KeyBERTParameters = \
            cast(KeyBERTParameters, parameters)
        vec = get_vectorizer(params.max_features, params.min_df, params.max_df, tuple(params.ngram_range),
                             params.use_lower, params.stopwords)
        ext = get_extractor(params.model)
        texts = [doc.text for doc in documents]
        term_lst = ext.extract_keywords(texts,
                                        keyphrase_ngram_range=parameters.ngram_range,
                                        top_n=parameters.top_n,
                                        use_maxsum=parameters.use_maxsum,
                                        use_mmr=parameters.use_mmr,
                                        diversity=parameters.diversity,
                                        nr_candidates=parameters.nr_candidates,
                                        vectorizer=vec)

        tokenizeds = tokenize_with_vectorizer(vec, texts)
        for weighted_terms, document, tokenized in zip(term_lst, documents, tokenizeds):
            terms, weights = zip(*weighted_terms)
            document.annotations = []
            tokens, spans = zip(*tokenized)
            if terms:
                tokenized_terms = []
                for tokenized_term in tokenize_with_vectorizer(vec, terms):
                    tokenized_terms.append(tuple(t[0] for t in tokenized_term))
                for i, j in left_longest_match_subfinder(tokens, tokenized_terms):
                    tokenized_term = tokenized_terms[j]
                    weight = weights[j]
                    start_span = spans[i]
                    end_span = spans[i + len(tokenized_term) - 1]
                    document.annotations.append(Annotation(start=start_span[0], end=end_span[1],
                                                           text=document.text[start_span[0]:end_span[1]],
                                                           score=weight,
                                                           label=params.term_label,
                                                           labelName=sanitize_label(params.term_label),
                                                           terms=[Term(identifier=terms[j], lexicon="KeyBERT")]))
        return documents

    @classmethod
    def get_model(cls) -> Type[BaseModel]:
        return KeyBERTParameters


def evaluate_min_max_df(min_df, max_df):
    min_df = int(min_df) if (min_df.isnumeric() and int(min_df) >= 1) else float(min_df)
    max_df = int(max_df) if (max_df.isnumeric() and int(min_df) > 1) else float(max_df)
    return min_df, max_df


def tokenize_with_vectorizer(vec, texts: List[str]):
    # if vec.tokenizer is not None:
    #     for tokens in list(vec.tokenizer.pipe(texts)):
    #         yield tokens
    token_pattern = re.compile(vec.token_pattern)
    for text in texts:
        tokens = []
        for match in token_pattern.finditer(text.lower() if vec.lowercase else text):
            if match:
                if not vec.stop_words or match[0] not in vec.stop_words:
                    tokens.append((match[0], match.span()))
        yield tokens


def left_longest_match_subfinder(seq, subseqs):
    n = len(seq)
    subseq0s = defaultdict(dict)
    for j, subseq in enumerate(subseqs):
        if subseq:
            subseq0s[subseq[0]][j] = len(subseq)
    for subseq0 in subseq0s.keys():
        subseq0s[subseq0] = sorted(subseq0s[subseq0].items(), key=lambda item: item[1], reverse=True)
    i = 0
    while i < n:
        inc = 1
        if seq[i] in subseq0s:
            for j, _ in subseq0s[seq[i]]:
                if seq[i:i + len(subseqs[j])] == subseqs[j]:
                    yield i, j
                    inc = len(subseqs[j])
                    break
        i += inc


@lru_cache(maxsize=None)
def get_extractor(model: str):
    return KeyBERT(model=model)


@lru_cache(maxsize=None)
def get_vectorizer(max_features: int, min_df: str, max_df: str, ngram_range, use_lower, stops):
    min_df, max_df = evaluate_min_max_df(min_df, max_df)
    stopwords_lst = None
    if stops:
        stop_langs = [x.strip() for x in stops.split(',')]
        stopwords_lst = stopwordsiso.stopwords(stop_langs)
    vectorizer = CountVectorizer(max_features=max_features,
                                 tokenizer=None,
                                 lowercase=use_lower,
                                 stop_words=stopwords_lst,
                                 ngram_range=ngram_range,
                                 min_df=min_df,
                                 max_df=max_df)
    return vectorizer


nonAlphanum = re.compile(r'[\W]+', flags=re.ASCII)
underscores = re.compile("_{2,}", flags=re.ASCII)
trailingAndLeadingUnderscores = re.compile(r"^_+|_+\$", flags=re.ASCII)
# see http://userguide.icu-project.org/transforms/general
transliterator = icu.Transliterator.createInstance(
    "Any-Latin; NFD; [:Nonspacing Mark:] Remove; NFC; Latin-ASCII; Lower;", icu.UTransDirection.FORWARD)


def sanitize_label(string):
    result = transliterator.transliterate(string)
    result = re.sub(nonAlphanum, "_", result)
    result = re.sub(underscores, "_", result)
    result = re.sub(trailingAndLeadingUnderscores, "", result)
    return result
