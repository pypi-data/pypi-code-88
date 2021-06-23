import json
import time
from functools import lru_cache
from typing import Type, List, cast, Dict, Any

import spacy
from pydantic import BaseModel, Field
from pymultirole_plugins.v1.schema import Document, Sentence
from pymultirole_plugins.v1.segmenter import SegmenterParameters, SegmenterBase
from pysegmenters_spacyrules.rule_sentencizer import RuleSentencizer
from spacy.cli.download import download_model, get_compatibility, get_version
from spacy.errors import OLD_MODEL_SHORTCUTS
from spacy.language import Language
from wasabi import msg

SPLIT_DEFAULT = [
    [
        {
            "__comment": "Split on double line breaks...",
            "TEXT": {
                "NOT_IN": [
                    ":", ",", "，", "："
                ]
            }
        },
        {
            "__comment": "...except if previous lines ends with : or ,",
            "IS_SPACE": True,
            "TEXT": {
                "REGEX": "(.?\n){2,}"
            }
        },
        {
            "__comment": "Sentence start at this token"
        }
    ],
    [
        {
            "__comment": "Split on hard punctuation",
            "IS_PUNCT": True,
            "TEXT": {
                "IN": [
                    "!", "?", "¿", "؟", "¡", "。", "？", "！", "·", "…", "……"
                ]
            }
        },
        {
            "__comment": "Sentence start at this token"
        }
    ],
    [
        {
            "__comment": "Split on full stop...n",
            "IS_PUNCT": True,
            "TEXT": "."
        },
        {
            "__comment": "...if not followed by lower case letter or digit",
            "SHAPE": {
                "REGEX": "^[^xd]"
            }
        }
    ]
]
JOIN_DEFAULT = [
    [
        {
            "__comment": "Some abbreviations not natively covered by Spacy...",
            "TEXT": {
                "IN": [
                    "Doc",
                    "Pres"
                ]
            }
        },
        {
            "__comment": "... followed by full stop",
            "IS_PUNCT": True,
            "TEXT": "."
        },
        {
            "IS_SENT_START": True
        }
    ]
]


class SpacyRulesParameters(SegmenterParameters):
    lang: str = Field("en",
                      description="Name of the 2-letter language of the documents")
    split_rules: List[List[Dict[str, Any]]] = Field(SPLIT_DEFAULT,
                                                    description="""List of split rules that operates over tokens based on the [Spacy Rule-based matcher](https://spacy.io/usage/rule-based-matching) syntax<br/>
                                                    The rules can refer to token annotations (e.g. the token text and flags (e.g. IS_PUNCT), the sentence start always at the last token a of sequennce.<br/>
                                                    Let's suppose you want to force sentence to start on word triggers like Title/Chapter, then you need to define a single rule composed of 2 tokens:<ol>
                                                    <li>A token whose `IS_SPACE` flag is set to true and that contains at least one line break `\\n`
                                                    <li>A token whose `TEXT` is in a list of predefined paragraph triggers `["Chapter", "Title"]`
                                                    </ol>
                                                    Then you need to define a rule like:<br/>
                                                    ```[```<br/>
                                                    ```    [```<br/>
                                                    ```        {```<br/>
                                                    ```            "__comment": "Split on line break...",```<br/>
                                                    ```            "IS_SPACE": True,```<br/>
                                                    ```            "TEXT": {```<br/>
                                                    ```                "REGEX": "(.?\n){1,}"```<br/>
                                                    ```            }```<br/>
                                                    ```        },```<br/>
                                                    ```        {```<br/>
                                                    ```            "__comment1": "... only if followed by paragraph trigger word",```<br/>
                                                    ```            "LOWER": {```<br/>
                                                    ```                "IN": [```<br/>
                                                    ```                    "chapter", "title"```<br/>
                                                    ```                ]```<br/>
                                                    ```            },```<br/>
                                                    ```            "__comment2": "... starting by an uppercase letter",```<br/>
                                                    ```            "SHAPE": {```<br/>
                                                    ```                "REGEX": "^X"```<br/>
                                                    ```            }```<br/>
                                                    ```        }```<br/>
                                                    ```    ]```<br/>
                                                    ```]```<br/>
                                                    Keys starting with `__comment` are considered as comments""",
                                                    extra="json")
    join_rules: List[List[Dict[str, Any]]] = Field(JOIN_DEFAULT,
                                                   description="List of exceptions rules that operates over tokens based on the [Spacy Rule-based matcher](https://spacy.io/usage/rule-based-matching) syntax",
                                                   extra="json")


class SpacyRulesSegmenter(SegmenterBase):
    """[SpacyRules](https://spacy.io/usage/rule-based-matching) segmenter.
    """

    def segment(self, documents: List[Document], parameters: SegmenterParameters) \
            -> List[Document]:
        params: SpacyRulesParameters = \
            cast(SpacyRulesParameters, parameters)
        # Retrieve nlp pipe
        nlp, enable_pipes = get_sentencizer_from_params(params)
        with nlp.select_pipes(enable=enable_pipes):
            for document in documents:
                document.sentences = []
                doc = nlp(document.text)
                if doc.has_annotation("SENT_START"):
                    for sent in doc.sents:
                        end_token = doc[sent.end - 2] if doc[sent.end - 1].is_space and len(sent) >= 2 else doc[
                            sent.end - 1]
                        document.sentences.append(Sentence(start=sent.start_char, end=end_token.idx + len(end_token)))
        return documents

    @classmethod
    def get_model(cls) -> Type[BaseModel]:
        return SpacyRulesParameters


def get_sentencizer_from_params(params):
    json_split = json_rules_to_string(params.split_rules)
    json_join = json_rules_to_string(params.join_rules)
    return get_sentencizer(params.lang,
                           json_split,
                           json_join,
                           ttl_hash=get_ttl_hash())


def json_rules_to_string(json_rules: List[List[Dict[str, Any]]]):
    str_rules = None
    if json_rules:
        for json_rule in json_rules:
            for token_rule in json_rule:
                # Remove comments if any
                for key in [k for k in token_rule if k.startswith('__comment')]:
                    del token_rule[key]
        str_rules = json.dumps(json_rules)
    return str_rules


# Deprecated model shortcuts, only used in errors and warnings
MODEL_SHORTCUTS = {
    "en": "en_core_web_sm", "de": "de_core_news_sm", "es": "es_core_news_sm",
    "pt": "pt_core_news_sm", "fr": "fr_core_news_sm", "it": "it_core_news_sm",
    "nl": "nl_core_news_sm", "el": "el_core_news_sm", "nb": "nb_core_news_sm",
    "lt": "lt_core_news_sm", "xx": "xx_ent_wiki_sm"
}


@lru_cache(maxsize=None)
def get_nlp(lang: str, ttl_hash=None):
    del ttl_hash
    model = MODEL_SHORTCUTS.get(lang, lang)
    # model = lang
    try:
        nlp: Language = spacy.load(model, exclude=["parser", "tagger", "ner", "lemmatizer"])
    except BaseException:
        nlp = load_spacy_model(model)
    return nlp


@lru_cache(maxsize=None)
def get_sentencizer(lang: str, json_split: str, json_join: str, ttl_hash=None):
    nlp = get_nlp(lang, ttl_hash=ttl_hash)
    split_rules = json.loads(json_split) if json_split else None
    join_rules = json.loads(json_join) if json_join else None
    unique_name = f"rule_sentencizer_{json_split if json_split else ''}_{json_join if json_join else ''}"
    sentencizer: RuleSentencizer = nlp.add_pipe("rule_sentencizer", name=unique_name,
                                                config={"split_patterns": split_rules, "join_patterns": join_rules})
    enable_pipes = [p for p in nlp.pipe_names if not p.startswith("rule_sentencizer_") or p == sentencizer.name]
    return nlp, enable_pipes


def get_ttl_hash(seconds=3600):
    """Return the same value withing `seconds` time period"""
    return round(time.time() / seconds)


def load_spacy_model(model, *pip_args):
    suffix = "-py3-none-any.whl"
    dl_tpl = "{m}-{v}/{m}-{v}{s}#egg={m}=={v}"
    model_name = model
    if model in OLD_MODEL_SHORTCUTS:
        msg.warn(
            f"As of spaCy v3.0, shortcuts like '{model}' are deprecated. Please "
            f"use the full pipeline package name '{OLD_MODEL_SHORTCUTS[model]}' instead."
        )
        model_name = OLD_MODEL_SHORTCUTS[model]
    compatibility = get_compatibility()
    version = get_version(model_name, compatibility)
    download_model(dl_tpl.format(m=model_name, v=version, s=suffix), pip_args)
    msg.good(
        "Download and installation successful",
        f"You can now load the package via spacy.load('{model_name}')",
    )
    # If a model is downloaded and then loaded within the same process, our
    # is_package check currently fails, because pkg_resources.working_set
    # is not refreshed automatically (see #3923). We're trying to work
    # around this here be requiring the package explicitly.
    require_package(model_name)
    return spacy.load(model_name, exclude=["parser", "tagger", "ner", "lemmatizer"])


def require_package(name):
    try:
        import pkg_resources

        pkg_resources.working_set.require(name)
        return True
    except:  # noqa: E722
        return False
