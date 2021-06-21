from typing import List
from pysegmenters_spacyrules.spacyrules import SpacyRulesSegmenter, SpacyRulesParameters, get_sentencizer_from_params
from pymultirole_plugins.v1.schema import Document


def test_spacyrules():
    TEXT = """CLAIRSSON INTERNATIONAL REPORTS LOSS

Clairson International Corp. said it expects to report a net loss for its
second quarter ended March 26. The company doesn’t expect to meet analysts’ profit
estimates of $3.9 to $4 million, or 76 cents a share to 79 cents a share, for its
year ending Sept. 24, according to Pres. John Doe."""
    model = SpacyRulesSegmenter.get_model()
    model_class = model.construct().__class__
    assert model_class == SpacyRulesParameters
    segmenter = SpacyRulesSegmenter()
    parameters = SpacyRulesParameters(lang='en', join_rules=[])
    docs: List[Document] = segmenter.segment([Document(text=TEXT)], parameters)
    doc0 = docs[0]
    assert len(doc0.sentences) == 4
    sents = [doc0.text[s.start:s.end] for s in doc0.sentences]
    assert sents[0] == "CLAIRSSON INTERNATIONAL REPORTS LOSS"
    assert sents[1] == """Clairson International Corp. said it expects to report a net loss for its
second quarter ended March 26."""
    assert sents[2] == """The company doesn’t expect to meet analysts’ profit
estimates of $3.9 to $4 million, or 76 cents a share to 79 cents a share, for its
year ending Sept. 24, according to Pres."""
    assert sents[3] == "John Doe."
    # With abbrev
    parameters = SpacyRulesParameters(lang='en')
    docs: List[Document] = segmenter.segment([Document(text=TEXT)], parameters)
    doc0 = docs[0]
    assert len(doc0.sentences) == 3
    sents = [doc0.text[s.start:s.end] for s in doc0.sentences]
    assert sents[0] == "CLAIRSSON INTERNATIONAL REPORTS LOSS"
    assert sents[1] == """Clairson International Corp. said it expects to report a net loss for its
second quarter ended March 26."""
    assert sents[2] == """The company doesn’t expect to meet analysts’ profit
estimates of $3.9 to $4 million, or 76 cents a share to 79 cents a share, for its
year ending Sept. 24, according to Pres. John Doe."""


def test_cached_nlp():
    parameters1 = SpacyRulesParameters()
    nlp1, enable_pipes1 = get_sentencizer_from_params(parameters1)
    parameters2 = SpacyRulesParameters(split_rules=[[{}]])
    nlp2, enable_pipes2 = get_sentencizer_from_params(parameters2)
    assert id(nlp1) == id(nlp2)
    assert id(enable_pipes1) != id(enable_pipes2)
