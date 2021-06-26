
# %%
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

class SynonymAugmentation(Component):
    defaults = {
        "minimum_synonym_example_count": 10,
    }

    def __init__(self, component_config: Dict[Text, Any] = None, response_dict=None) -> None:
        super(SynonymAugmentation, self).__init__(component_config)

    def normalize_text(self, text):
        return xNormalizer.tr_normalize(text).lower()

    def get_synonyms_backup(self, training_data):
        
        synonyms = {}
        for key, value in list(training_data.entity_synonyms.items()):
            # key : synonym values # ex: is bankasi
            # value : normalized synonym value # ex: ISCTR

            if key not in synonyms:
                synonyms[key] = set()
            synonyms[key].add(value)

        return synonyms

    def get_synonyms(self, training_data):
        
        synonyms = {}
        for key, value in list(training_data.entity_synonyms.items()):
            key = self.normalize_text(key)
            value = self.normalize_text(value)
            # key : synonym values # ex: is bankasi
            # value : normalized synonym value # ex: ISCTR

            if value not in synonyms:
                synonyms[value] = set()
            
            # synonyms[value].add(key)
            try:
                int(key)
            except:
                synonyms[value].add(key)
            try:
                int(value)
            except:
                synonyms[value].add(value)

        return synonyms

    def get_pairs_backup(self, training_data):

        synonyms = self.get_synonyms_backup(training_data)

        pairs = {}
        for synonym_key in synonyms:
            pairs[synonym_key] = {}
            pairs[synonym_key]['match_counts'] = {}
            pairs[synonym_key]['match_examples'] = []
            for synonym_i in synonyms[synonym_key]:
                pairs[synonym_key]['match_counts'][synonym_i] = 0

        for synonym_key in synonyms:
            
            for synonym_i in synonyms[synonym_key]:
                synonym_i_norm = self.normalize_text(synonym_i)

                for message in training_data.training_examples:
                    message_text = self.normalize_text(message.text)

                    token_starts = [t.start for t in message.data["tokens"]]
                    token_ends = [t.end for t in message.data["tokens"]]

                    
                    matches = re.finditer(rf'\b{synonym_i_norm}\b', message_text, )
                    for match in matches:
                        match_start, match_end = match.span()

                        if match_start in token_starts and match_end in token_ends:

                            pairs[synonym_key]['match_counts'][synonym_i] += 1
                            pairs[synonym_key]['match_examples'].append( (message, synonym_i, token_starts.index(match_start), token_ends.index(match_end)) )
        return pairs

    def get_pairs_backup_2(self, training_data):

        synonyms = self.get_synonyms(training_data)

        pairs = {}
        for synonym_key in synonyms:
            pairs[synonym_key] = {}
            pairs[synonym_key]['match_counts'] = {}
            pairs[synonym_key]['match_examples'] = []
            for synonym_i in synonyms[synonym_key]:
                pairs[synonym_key]['match_counts'][synonym_i] = 0

        for synonym_key in synonyms:
            
            for synonym_i in synonyms[synonym_key]:

                for message in training_data.training_examples:
                    message_text = self.normalize_text(message.text)
                    entities = message.get(ENTITIES, [])

                    for e in entities:
                        if message_text[e['start']:e['end']] == synonym_i:
                            pairs[synonym_key]['match_counts'][synonym_i] += 1
                            pairs[synonym_key]['match_examples'].append( (message, synonym_i, e['start'], e['end']) )

        return pairs

    
    def get_pairs(self, training_data):

        synonyms = self.get_synonyms(training_data)

        pairs = {}
        for synonym_key in synonyms:
            pairs[synonym_key] = {}
            pairs[synonym_key]['match_counts'] = {}
            pairs[synonym_key]['match_examples'] = []
            for synonym_i in synonyms[synonym_key]:
                pairs[synonym_key]['match_counts'][synonym_i] = 0


        for message in training_data.training_examples:
            message_text = self.normalize_text(message.text)
            entities = message.get(ENTITIES, [])

            for e in entities:
                e_text = message_text[e['start']:e['end']]

                for synonym_key in synonyms:
                    
                    for synonym_i in synonyms[synonym_key]:

                        if e_text == synonym_i:
                            pairs[synonym_key]['match_counts'][synonym_i] += 1
                            pairs[synonym_key]['match_examples'].append( (message, synonym_i, e['start'], e['end']) )

        return pairs

    def generate_examples(self, training_data):

        augmented_examples = []
        synonyms_with_not_enough_examples = set()

        pairs = self.get_pairs(training_data)

        for synonym_key in pairs:
            
            for synonym_i in pairs[synonym_key]['match_counts']:
                synonym_i_train_example_count = pairs[synonym_key]['match_counts'][synonym_i]
                synonym_i_available_augmentation_examples = [match_example for match_example in pairs[synonym_key]['match_examples'] if match_example[1] != synonym_i]
                
                if synonym_i_train_example_count < self.component_config["minimum_synonym_example_count"] :

                    required_example_count = self.component_config["minimum_synonym_example_count"] - synonym_i_train_example_count
                    if required_example_count < len(synonym_i_available_augmentation_examples):
                        synonym_i_available_augmentation_examples = random.sample(synonym_i_available_augmentation_examples, required_example_count)

                    if len(synonym_i_available_augmentation_examples) + synonym_i_train_example_count != self.component_config["minimum_synonym_example_count"]:
                        # aug_available_count = len(synonym_i_available_augmentation_examples)
                        # req_count = self.component_config["minimum_synonym_example_count"]
                        # print("THERE ARE NOT ENOUGH EXAMPLES TO AUGMENT.")
                        # print(f"SYNONYM : {synonym_i}")
                        # print(f"EXISTING COUNT : {synonym_i_train_example_count}")
                        # print(f"AUGMENTATION AVAILABLE COUNT : {aug_available_count}")
                        # print(f"REQUIRED COUNT : {req_count}")
                        # print()
                        synonyms_with_not_enough_examples.add(synonym_key)

                    for augmentation_example in synonym_i_available_augmentation_examples:
                        source_message, source_synonym_i , e_start, e_end = augmentation_example
                        
                        augmented_text = source_message.text
                        augmented_text = augmented_text[:e_start] + synonym_i + augmented_text[e_end:]
                        augmented_example_intent = source_message.get(INTENT)
                        augmented_entities = copy.deepcopy(source_message.get(ENTITIES, []))

                        for e in augmented_entities:
                            if e['start'] < e_start:
                                pass
                            elif e['start'] == e_start:
                                e['end'] = e['end'] - len(source_synonym_i) + len(synonym_i)
                            elif e['start'] > e_start:
                                e['start'] = e['start'] - len(source_synonym_i) + len(synonym_i)
                                e['end'] = e['end'] - len(source_synonym_i) + len(synonym_i)

                        augmented_example = Message(augmented_text, {INTENT:augmented_example_intent, ENTITIES: augmented_entities})
                        augmented_examples.append(augmented_example)
        
        print("THERE ARE NOT ENOUGH EXAMPLES TO AUGMENT IN THE FOLLOWING SYNONYMS.")
        print(synonyms_with_not_enough_examples)
        print()
        return augmented_examples



    def train(self, training_data: TrainingData, config: Optional[RasaNLUModelConfig] = None, **kwargs: Any,):

        augmented_examples = self.generate_examples(training_data)
        training_data.training_examples = training_data.training_examples + augmented_examples

        TrainingDataManager.reset_lazy_attributes(training_data)
        


class SynonymEntityAugmentation20210622(Component):
    defaults = {
        "partition_name": "synonym_entity",
        "minimum_synonym_example_count": 10,
    }

    def __init__(self, component_config: Dict[Text, Any] = None, response_dict=None) -> None:
        super(SynonymEntityAugmentation20210622, self).__init__(component_config)

    def normalize_text(self, text):
        return xNormalizer.tr_normalize(text).lower()

    def get_synonyms(self, training_data):
        
        synonyms = {}
        for key, value in list(training_data.entity_synonyms.items()):
            key = self.normalize_text(key)
            value = self.normalize_text(value)
            # key : synonym values # ex: is bankasi
            # value : normalized synonym value # ex: ISCTR

            if value not in synonyms:
                synonyms[value] = set()
            
            # synonyms[value].add(key)
            try:
                int(key)
            except:
                synonyms[value].add(key)
            try:
                int(value)
            except:
                synonyms[value].add(value)

        return synonyms
    
    def get_pairs(self, training_data):

        synonyms = self.get_synonyms(training_data)

        pairs = {}
        for synonym_key in synonyms:
            pairs[synonym_key] = {}
            pairs[synonym_key]['match_counts'] = {}
            pairs[synonym_key]['match_examples'] = []
            for synonym_i in synonyms[synonym_key]:
                pairs[synonym_key]['match_counts'][synonym_i] = 0


        for message in training_data.training_examples:
            message_text = self.normalize_text(message.text)
            entities = message.get(ENTITIES, [])

            for e in entities:
                e_text = message_text[e['start']:e['end']]

                for synonym_key in synonyms:
                    
                    for synonym_i in synonyms[synonym_key]:

                        if e_text == synonym_i:
                            pairs[synonym_key]['match_counts'][synonym_i] += 1
                            pairs[synonym_key]['match_examples'].append( (message, synonym_i, e['start'], e['end']) )

        return pairs

    def generate_examples(self, training_data):

        augmented_examples = []
        synonyms_with_not_enough_examples = set()

        pairs = self.get_pairs(training_data)

        for synonym_key in pairs:
            
            for synonym_i in pairs[synonym_key]['match_counts']:
                synonym_i_train_example_count = pairs[synonym_key]['match_counts'][synonym_i]
                synonym_i_available_augmentation_examples = [match_example for match_example in pairs[synonym_key]['match_examples'] if match_example[1] != synonym_i]
                
                if synonym_i_train_example_count < self.component_config["minimum_synonym_example_count"] :

                    required_example_count = self.component_config["minimum_synonym_example_count"] - synonym_i_train_example_count
                    if required_example_count < len(synonym_i_available_augmentation_examples):
                        synonym_i_available_augmentation_examples = random.sample(synonym_i_available_augmentation_examples, required_example_count)

                    if len(synonym_i_available_augmentation_examples) + synonym_i_train_example_count != self.component_config["minimum_synonym_example_count"]:
                        # aug_available_count = len(synonym_i_available_augmentation_examples)
                        # req_count = self.component_config["minimum_synonym_example_count"]
                        # print("THERE ARE NOT ENOUGH EXAMPLES TO AUGMENT.")
                        # print(f"SYNONYM : {synonym_i}")
                        # print(f"EXISTING COUNT : {synonym_i_train_example_count}")
                        # print(f"AUGMENTATION AVAILABLE COUNT : {aug_available_count}")
                        # print(f"REQUIRED COUNT : {req_count}")
                        # print()
                        synonyms_with_not_enough_examples.add(synonym_key)

                    for augmentation_example in synonym_i_available_augmentation_examples:
                        source_message, source_synonym_i , e_start, e_end = augmentation_example
                        
                        augmented_text = source_message.text
                        augmented_text = augmented_text[:e_start] + synonym_i + augmented_text[e_end:]
                        augmented_example_intent = source_message.get(INTENT)
                        augmented_entities = copy.deepcopy(source_message.get(ENTITIES, []))

                        for e in augmented_entities:
                            if e['start'] < e_start:
                                pass
                            elif e['start'] == e_start:
                                e['end'] = e['end'] - len(source_synonym_i) + len(synonym_i)
                            elif e['start'] > e_start:
                                e['start'] = e['start'] - len(source_synonym_i) + len(synonym_i)
                                e['end'] = e['end'] - len(source_synonym_i) + len(synonym_i)

                        augmented_example = Message(augmented_text, {INTENT:augmented_example_intent, ENTITIES: augmented_entities})
                        augmented_examples.append(augmented_example)
        
        print("THERE ARE NOT ENOUGH EXAMPLES TO AUGMENT IN THE FOLLOWING SYNONYMS.")
        print(synonyms_with_not_enough_examples)
        print()
        return augmented_examples



    def train(self, training_data: TrainingData, config: Optional[RasaNLUModelConfig] = None, **kwargs: Any,):
        
        augmented_examples = self.generate_examples(training_data)
        setattr(training_data, self.component_config["partition_name"], augmented_examples)
        

class SynonymTextAugmentation20210622(Component):
    defaults = {
        "partition_name": "synonym_text",
        "minimum_synonym_example_count": 10,
    }

    def __init__(self, component_config: Dict[Text, Any] = None, response_dict=None) -> None:
        super(SynonymTextAugmentation20210622, self).__init__(component_config)

    def normalize_text(self, text):
        return xNormalizer.tr_normalize(text).lower()

    def get_synonyms(self, training_data):
        
        synonyms = {}
        for key, value in list(training_data.entity_synonyms.items()):
            key = self.normalize_text(key)
            value = self.normalize_text(value)
            # key : synonym values # ex: is bankasi
            # value : normalized synonym value # ex: ISCTR

            if value not in synonyms:
                synonyms[value] = set()
            
            # synonyms[value].add(key)
            try:
                int(key)
            except:
                synonyms[value].add(key)
            try:
                int(value)
            except:
                synonyms[value].add(value)

        return synonyms
    
    def get_pairs(self, training_data):

        synonyms = self.get_synonyms(training_data)

        pairs = {}
        for synonym_key in synonyms:
            pairs[synonym_key] = {}
            pairs[synonym_key]['match_counts'] = {}
            pairs[synonym_key]['match_examples'] = []
            for synonym_i in synonyms[synonym_key]:
                pairs[synonym_key]['match_counts'][synonym_i] = {}

        for message in training_data.training_examples:
            message_text = self.normalize_text(message.text)
            intent = message.get(INTENT)

            for synonym_key in synonyms:
                for synonym_i in synonyms[synonym_key]:

                    matches = re.finditer(fr'(?<!\S){synonym_i}(?!\S)', message_text)
                    matches = list(matches)
                    for match in matches:
                        if intent not in pairs[synonym_key]['match_counts'][synonym_i]:
                            pairs[synonym_key]['match_counts'][synonym_i][intent] = 0
                        
                        pairs[synonym_key]['match_counts'][synonym_i][intent] += 1
                        pairs[synonym_key]['match_examples'].append( (message, intent, synonym_i, match.span()[0], match.span()[1]) )

        return pairs

    def generate_examples(self, training_data):

        augmented_examples = []
        synonyms_with_not_enough_examples = set()

        pairs = self.get_pairs(training_data)

        for synonym_key in pairs:


            # for synonym_i in pairs[synonym_key]['match_counts']:
            #     for intent_i in pairs[synonym_key]['match_counts'][synonym_i]:
            used_intents = list(set(sum([list(pairs[synonym_key]['match_counts'][e].keys()) for e in pairs[synonym_key]['match_counts']],[])))
            for intent_i in used_intents:
                for synonym_i in pairs[synonym_key]['match_counts']:

                    # synonym_i_train_example_count = pairs[synonym_key]['match_counts'][synonym_i][intent_i]
                    synonym_i_train_example_count = pairs[synonym_key]['match_counts'][synonym_i].get(intent_i,0)

                    
                    synonym_i_available_augmentation_examples = [match_example 
                                                                for match_example in pairs[synonym_key]['match_examples'] 
                                                                if match_example[2] != synonym_i and match_example[1] == intent_i]
                    

                    if synonym_i_train_example_count < self.component_config["minimum_synonym_example_count"] :

                        required_example_count = self.component_config["minimum_synonym_example_count"] - synonym_i_train_example_count
                        if required_example_count < len(synonym_i_available_augmentation_examples):
                            synonym_i_available_augmentation_examples = random.sample(synonym_i_available_augmentation_examples, required_example_count)

                        if len(synonym_i_available_augmentation_examples) + synonym_i_train_example_count != self.component_config["minimum_synonym_example_count"]:
                            synonyms_with_not_enough_examples.add(synonym_key)

                        for augmentation_example in synonym_i_available_augmentation_examples:
                            source_message, source_intent_i, source_synonym_i , e_start, e_end = augmentation_example
                            
                            augmented_text = source_message.text
                            augmented_text = augmented_text[:e_start] + synonym_i + augmented_text[e_end:]
                            augmented_example_intent = source_message.get(INTENT)

                            augmented_example = Message(augmented_text, {INTENT:augmented_example_intent, ENTITIES: []})
                            augmented_examples.append(augmented_example)
        
        print("THERE ARE NOT ENOUGH EXAMPLES TO AUGMENT IN THE FOLLOWING SYNONYMS.")
        print(synonyms_with_not_enough_examples)
        print()
        return augmented_examples



    def train(self, training_data: TrainingData, config: Optional[RasaNLUModelConfig] = None, **kwargs: Any,):
        
        augmented_examples = self.generate_examples(training_data)
        setattr(training_data, self.component_config["partition_name"], augmented_examples)
        