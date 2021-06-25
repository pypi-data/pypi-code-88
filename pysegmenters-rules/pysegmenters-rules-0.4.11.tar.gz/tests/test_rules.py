from typing import List
from pysegmenters_rules.rules import RulesSegmenter, RulesParameters, get_sentencizer_from_params, RuleEngine
from pymultirole_plugins.v1.schema import Document


def test_rules_en():
    TEXT = """CLAIRSSON INTERNATIONAL REPORTS LOSS

Clairson International Corp. said it expects to report a net loss for its second quarter ended March 26.
The company doesn’t expect to meet analysts’ profit estimates of $3.9 to $4 million, or 76 cents a share to 79 cents a share, for its year ending Sept. 24, according to Pres. John Doe."""
    model = RulesSegmenter.get_model()
    model_class = model.construct().__class__
    assert model_class == RulesParameters
    segmenter = RulesSegmenter()
    parameters = RulesParameters(lang='en', engine=RuleEngine.Custom, join_rules=[])
    docs: List[Document] = segmenter.segment([Document(text=TEXT)], parameters)
    doc0 = docs[0]
    assert len(doc0.sentences) == 4
    sents = [doc0.text[s.start:s.end] for s in doc0.sentences]
    assert sents[0] == "CLAIRSSON INTERNATIONAL REPORTS LOSS"
    assert sents[1] == "Clairson International Corp. said it expects to report a net loss for its second quarter ended March 26."
    assert sents[2] == "The company doesn’t expect to meet analysts’ profit estimates of $3.9 to $4 million, or 76 cents a share to 79 cents a share, for its year ending Sept. 24, according to Pres."
    assert sents[3] == "John Doe."
    # With abbrev
    parameters = RulesParameters(lang='en', engine=RuleEngine.Custom)
    docs: List[Document] = segmenter.segment([Document(text=TEXT)], parameters)
    doc0 = docs[0]
    assert len(doc0.sentences) == 3
    sents = [doc0.text[s.start:s.end] for s in doc0.sentences]
    assert sents[0] == "CLAIRSSON INTERNATIONAL REPORTS LOSS"
    assert sents[1] == "Clairson International Corp. said it expects to report a net loss for its second quarter ended March 26."
    assert sents[2] == "The company doesn’t expect to meet analysts’ profit estimates of $3.9 to $4 million, or 76 cents a share to 79 cents a share, for its year ending Sept. 24, according to Pres. John Doe."
    # With PySDB
    parameters = RulesParameters(lang='en', engine=RuleEngine.PySBD)
    docs: List[Document] = segmenter.segment([Document(text=TEXT)], parameters)
    doc0 = docs[0]
    assert len(doc0.sentences) == 4
    sents = [doc0.text[s.start:s.end] for s in doc0.sentences]
    assert sents[0] == "CLAIRSSON INTERNATIONAL REPORTS LOSS"
    assert sents[1] == "Clairson International Corp. said it expects to report a net loss for its second quarter ended March 26."
    assert sents[2] == "The company doesn’t expect to meet analysts’ profit estimates of $3.9 to $4 million, or 76 cents a share to 79 cents a share, for its year ending Sept. 24, according to Pres."
    assert sents[3] == "John Doe."


def test_rules_fr():
    TEXT = """ARTICLE I
Chapitre 1
chapitre bla, bla, bla, bla, bla, bla
Chapitre 2
chapitre bla, bla, bla, bla, bla, bla
ARTICLE II
Chapitre 1
chapitre bla, bla, bla, bla, bla, bla
Chapitre 2
chapitre bla, bla, bla, bla, bla, bla
"""
    SPLIT_DEFAULT = [
        [
            {
                "__comment": "Split on line break...",
                "IS_SPACE": True,
                "TEXT": {
                    "REGEX": "(.?\n){1,}"
                }
            },
            {
                "__comment": "... only if followed by paragraph trigger, sentence start at this token",
                "LOWER": {
                    "IN": [
                        "article", "chapitre"
                    ]
                },
                "SHAPE": {
                    "REGEX": "^X"
                }
            }
        ]
    ]
    model = RulesSegmenter.get_model()
    model_class = model.construct().__class__
    assert model_class == RulesParameters
    segmenter = RulesSegmenter()
    parameters = RulesParameters(lang='fr', engine=RuleEngine.Custom, split_rules=SPLIT_DEFAULT, join_rules=[])
    docs: List[Document] = segmenter.segment([Document(text=TEXT)], parameters)
    doc0 = docs[0]
    assert len(doc0.sentences) == 6
    sents = [doc0.text[s.start:s.end] for s in doc0.sentences]
    assert sents[0].startswith("ARTICLE")
    assert sents[1].startswith("Chapitre")
    assert sents[2].startswith("Chapitre")
    assert sents[3].startswith("ARTICLE")
    assert sents[4].startswith("Chapitre")
    assert sents[5].startswith("Chapitre")

    # With PySBD
    parameters = RulesParameters(lang='fr', engine=RuleEngine.PySBD)
    docs: List[Document] = segmenter.segment([Document(text=TEXT)], parameters)
    doc0 = docs[0]
    assert len(doc0.sentences) == 10
    sents = [doc0.text[s.start:s.end] for s in doc0.sentences]
    assert sents[0].startswith("ARTICLE")
    assert sents[1].startswith("Chapitre")
    assert sents[2].startswith("chapitre")
    assert sents[3].startswith("Chapitre")
    assert sents[4].startswith("chapitre")
    assert sents[5].startswith("ARTICLE")
    assert sents[6].startswith("Chapitre")
    assert sents[7].startswith("chapitre")
    assert sents[8].startswith("Chapitre")
    assert sents[9].startswith("chapitre")


def test_cached_nlp():
    parameters1 = RulesParameters(engine=RuleEngine.Custom)
    nlp1, enable_pipes1 = get_sentencizer_from_params(parameters1)
    parameters2 = RulesParameters(engine=RuleEngine.Custom, split_rules=[[{}]])
    nlp2, enable_pipes2 = get_sentencizer_from_params(parameters2)
    assert id(nlp1) == id(nlp2)
    assert id(enable_pipes1) != id(enable_pipes2)
