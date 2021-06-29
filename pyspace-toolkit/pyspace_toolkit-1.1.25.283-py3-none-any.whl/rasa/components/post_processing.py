
# %%
import logging
import re
import os
from typing import Any, Dict, List, Optional, Text, Union, Type

# %%
from rasa.nlu.tokenizers.tokenizer import Token, Tokenizer
from rasa.nlu.components import Component
from rasa.nlu.featurizers.featurizer import SparseFeaturizer
from rasa.nlu.training_data import Message, TrainingData

from rasa.nlu.constants import TOKENS_NAMES, MESSAGE_ATTRIBUTES
from rasa.constants import DOCS_URL_TRAINING_DATA_NLU
from rasa.nlu.constants import (
    CLS_TOKEN,
    RESPONSE,
    SPARSE_FEATURE_NAMES,
    TEXT,
    TOKENS_NAMES,
    INTENT,
    MESSAGE_ATTRIBUTES,
    ENTITIES,
)

from rasa.nlu.config import RasaNLUModelConfig

import rasa.utils.io as io_utils
from rasa.nlu import utils
import rasa.utils.common as common_utils
from rasa.nlu.model import Metadata

# %%
from pyspace.nlp.preprocessing.normalizer.xnormalizer import xNormalizer

from pyspace.nlp.task.date_extractor import DateParser

from pyspace.rasa.components.data_management import TrainingDataManager

# %%
import copy
import pickle

from rasa.core.domain import Domain
from pathlib import Path

import random
import datetime

try:
    from pymongo import MongoClient
    pymongo_bool = True
except:
    pymongo_bool = False

class RegexPostProcessing(Component):

    def __init__(self, component_config: Dict[Text, Any] = None, response_dict=None) -> None:
        super(RegexPostProcessing, self).__init__(component_config)
        self.read_config()

    def read_config(self,):
        mongo_url = os.environ.get('MONGO_URL','')
        if mongo_url == '':
            self.post_processing_config = []
        else:
            client = MongoClient(mongo_url)
            db = client.bf
            projects_col = db.projects
            self.post_processing_config = projects_col.find_one({'_id':'bf'})['regex_post_processing_config']
            client.close()

    def apply_post_processing(self,):
        
        for c in self.post_processing_config:
            pass

        pass

    def process(self, message: Message, **kwargs: Any) -> None:
        if message.text == 'sofie_regex_post_processing_config_update':
            self.read_config()
        else:
            self.apply_post_processing()