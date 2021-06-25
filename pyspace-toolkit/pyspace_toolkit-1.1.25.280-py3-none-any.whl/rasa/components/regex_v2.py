import logging
import os
import re
from typing import Any, Dict, List, Optional, Text, Union, Type

import warnings
from rasa.nlu.utils import write_json_to_file

import numpy as np
import copy

from rasa.constants import DOCS_URL_TRAINING_DATA_NLU
import rasa.utils.io
import rasa.utils.io
import scipy.sparse
from rasa.nlu import utils
from rasa.nlu.config import RasaNLUModelConfig
from rasa.nlu.constants import (
    CLS_TOKEN,
    RESPONSE,
    SPARSE_FEATURE_NAMES,
    TEXT,
    TOKENS_NAMES,
)
from rasa.nlu.tokenizers.tokenizer import Tokenizer
from rasa.nlu.components import Component
from rasa.nlu.featurizers.featurizer import SparseFeaturizer
from rasa.nlu.extractors.extractor import EntityExtractor
from rasa.nlu.training_data import Message, TrainingData
import rasa.utils.common as common_utils
from rasa.nlu.model import Metadata

import pyspace
from pyspace.nlp.preprocessing.normalizer.xnormalizer import xNormalizer

logger = logging.getLogger(__name__)


class RegexEntityExtractor20210528(EntityExtractor):

    defaults = {
        "prediction_entity_write_attribute": "regex",
        "prediction_in_train_time": False,
    }

    def __init__(
        self,
        component_config: Optional[Dict[Text, Text]] = None,
        regex_features: Optional[Dict[Text, Any]] = None
    ) -> None:
        super(RegexEntityExtractor20210528, self).__init__(component_config)

        self.regex_features = regex_features if regex_features else []

    def train(self, training_data: TrainingData, config: RasaNLUModelConfig, **kwargs: Any) -> None:
        self.regex_features = copy.deepcopy(training_data.regex_features) 
        
        if self.component_config["prediction_in_train_time"]:
            for message in training_data.training_examples:        
                self.process(message,)

    def match_regex(self, message):
        extracted = []
        for d in self.regex_features:

            __pattern = d['pattern']
            __text = xNormalizer.tr_normalize(message).lower()
            __flag = re.I
            __group = 0 if 'group' not in d else d['group']

            try:
                # match = re.search(pattern=d['pattern'], string=message)
                matches = re.finditer(pattern=__pattern, string=__text, flags=__flag)
                matches = list(matches)
            except:
                print('regex entity extractor process error')
                print(__pattern)

            for match in matches:
                # match # whole token with word boundaries
                entity = {
                    "start": match.span()[0], # whole token start 
                    "end": match.span()[1], # whole token end
                    "value": match.group(__group), # regex entity group # e.g. without suffixes
                    # "confidence": 1.0,
                    "entity": d['name'],
                }
                extracted.append(entity)

        extracted = self.add_extractor_name(extracted)
        return extracted

    def process(self, message: Message, **kwargs: Any) -> None:
        """Process an incoming message."""
        # print('regex entity extractor process')

        extracted = self.match_regex(message.text)

        wattr = self.component_config["prediction_entity_write_attribute"]
        message.set(wattr, message.get(wattr, []) + extracted, add_to_output=True)

    def persist(self, file_name: Text, model_dir: Text) -> Optional[Dict[Text, Any]]:
        """Persist this component to disk for future loading."""

        import pickle
        regex_file_name = file_name + "_regex.pkl"
        with open(os.path.join(model_dir, regex_file_name), 'wb') as f:
            pickle.dump(self.regex_features, f)

        return {"regex_file_name": regex_file_name}

    @classmethod
    def load(
            cls,
            meta: Dict[Text, Any],
            model_dir: Optional[Text] = None,
            model_metadata: Optional[Metadata] = None,
            cached_component: Optional["RegexEntityExtractor20210528"] = None,
            **kwargs: Any
    ) -> "RegexEntityExtractor20210528":

        # try except
        try:
            regex_file_name = meta.get("regex_file_name")
            regex_file = os.path.join(model_dir, regex_file_name)
            import pickle
            with open(regex_file, 'rb') as f:
                regex_features = pickle.load(f)

            # print(regex_features[-1])
        except:
            print('regex entity extractor load error')
        return cls(meta, regex_features)

