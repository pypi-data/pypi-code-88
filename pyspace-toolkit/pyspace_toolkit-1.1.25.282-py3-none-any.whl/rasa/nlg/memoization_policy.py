import zlib

import base64
import json
import logging
import os
from tqdm import tqdm
from typing import Optional, Any, Dict, List, Text

import rasa.utils.io

from rasa.core.domain import Domain
from rasa.core.events import ActionExecuted
from rasa.core.featurizers import TrackerFeaturizer, MaxHistoryTrackerFeaturizer
from rasa.core.policies.policy import Policy
from rasa.core.trackers import DialogueStateTracker
from rasa.utils.common import is_logging_disabled
from rasa.core.constants import MEMOIZATION_POLICY_PRIORITY

logger = logging.getLogger(__name__)


class CustomMemoizationPolicy(Policy):
    """The policy that remembers exact examples of
        `max_history` turns from training stories.
        Since `slots` that are set some time in the past are
        preserved in all future feature vectors until they are set
        to None, this policy implicitly remembers and most importantly
        recalls examples in the context of the current dialogue
        longer than `max_history`.
        This policy is not supposed to be the only policy in an ensemble,
        it is optimized for precision and not recall.
        It should get a 100% precision because it emits probabilities of 1.1
        along it's predictions, which makes every mistake fatal as
        no other policy can overrule it.
        If it is needed to recall turns from training dialogues where
        some slots might not be set during prediction time, and there are
        training stories for this, use AugmentedMemoizationPolicy.
    """

    ENABLE_FEATURE_STRING_COMPRESSION = True

    SUPPORTS_ONLINE_TRAINING = True

    USE_NLU_CONFIDENCE_AS_SCORE = False

    @staticmethod
    def _standard_featurizer(
        max_history: Optional[int] = None,
    ) -> MaxHistoryTrackerFeaturizer:
        # Memoization policy always uses MaxHistoryTrackerFeaturizer
        # without state_featurizer
        return MaxHistoryTrackerFeaturizer(
            state_featurizer=None,
            max_history=max_history,
            use_intent_probabilities=False,
        )

    def __init__(
        self,
        policy_probability = 1.0,
        featurizer: Optional[TrackerFeaturizer] = None,
        priority: int = MEMOIZATION_POLICY_PRIORITY,
        max_history: Optional[int] = None,
        lookup: Optional[Dict] = None,
    ) -> None:

        if not featurizer:
            featurizer = self._standard_featurizer(max_history)

        super().__init__(featurizer, priority)

        self.max_history = self.featurizer.max_history
        self.lookup = lookup if lookup is not None else {}
        self.is_enabled = True
        self.policy_probability = policy_probability

    def toggle(self, activate: bool) -> None:
        self.is_enabled = activate

    def _add_states_to_lookup(
        self, trackers_as_states, trackers_as_actions, domain, online=False
    ) -> None:
        """Add states to lookup dict"""
        if not trackers_as_states:
            return

        assert len(trackers_as_states[0]) == self.max_history, (
            "Trying to mem featurized data with {} historic turns. Expected: "
            "{}".format(len(trackers_as_states[0]), self.max_history)
        )

        assert len(trackers_as_actions[0]) == 1, (
            "The second dimension of trackers_as_action should be 1, "
            "instead of {}".format(len(trackers_as_actions[0]))
        )

        ambiguous_feature_keys = set()

        pbar = tqdm(
            zip(trackers_as_states, trackers_as_actions),
            desc="Processed actions",
            disable=is_logging_disabled(),
        )
        for states, actions in pbar:
            action = actions[0]

            feature_key = self._create_feature_key(states)
            feature_item = domain.index_for_action(action)

            if feature_key not in ambiguous_feature_keys:
                if feature_key in self.lookup.keys():
                    if self.lookup[feature_key] != feature_item:
                        if online:
                            logger.info(
                                "Original stories are "
                                "different for {} -- {}\n"
                                "Memorized the new ones for "
                                "now. Delete contradicting "
                                "examples after exporting "
                                "the new stories."
                                "".format(states, action)
                            )
                            self.lookup[feature_key] = feature_item
                        else:
                            # delete contradicting example created by
                            # partial history augmentation from memory
                            ambiguous_feature_keys.add(feature_key)
                            del self.lookup[feature_key]
                else:
                    self.lookup[feature_key] = feature_item
            pbar.set_postfix({"# examples": "{:d}".format(len(self.lookup))})

    def _create_feature_key(self, states: List[Dict]) -> Text:
        from rasa.utils import io

        feature_str = json.dumps(states, sort_keys=True).replace('"', "")
        if self.ENABLE_FEATURE_STRING_COMPRESSION:
            compressed = zlib.compress(bytes(feature_str, io.DEFAULT_ENCODING))
            return base64.b64encode(compressed).decode(io.DEFAULT_ENCODING)
        else:
            return feature_str

    def train(
        self,
        training_trackers: List[DialogueStateTracker],
        domain: Domain,
        **kwargs: Any,
    ) -> None:
        """Trains the policy on given training trackers."""
        self.lookup = {}
        # only considers original trackers (no augmented ones)
        training_trackers = [
            t
            for t in training_trackers
            if not hasattr(t, "is_augmented") or not t.is_augmented
        ]
        (
            trackers_as_states,
            trackers_as_actions,
        ) = self.featurizer.training_states_and_actions(training_trackers, domain)
        self._add_states_to_lookup(trackers_as_states, trackers_as_actions, domain)
        logger.debug("Memorized {} unique examples.".format(len(self.lookup)))

    def _recall_states(self, states: List[Dict[Text, float]]) -> Optional[int]:

        return self.lookup.get(self._create_feature_key(states))

    def recall(
        self,
        states: List[Dict[Text, float]],
        tracker: DialogueStateTracker,
        domain: Domain,
    ) -> Optional[int]:

        return self._recall_states(states)

    def predict_action_probabilities(
        self, tracker: DialogueStateTracker, domain: Domain
    ) -> List[float]:
        """Predicts the next action the bot should take after seeing the tracker.
        Returns the list of probabilities for the next actions.
        If memorized action was found returns 1 for its index,
        else returns 0 for all actions.
        """
        result = self._default_predictions(domain)

        if not self.is_enabled:
            return result

        tracker_as_states = self.featurizer.prediction_states([tracker], domain)
        states = tracker_as_states[0]
        logger.debug(f"Current tracker state {states}")
        recalled = self.recall(states, tracker, domain)
        if recalled is not None:
            logger.debug(
                f"There is a memorised next action '{domain.action_names[recalled]}'"
            )

            if self.USE_NLU_CONFIDENCE_AS_SCORE:
                # the memoization will use the confidence of NLU on the latest
                # user message to set the confidence of the action
                score = tracker.latest_message.intent.get("confidence", self.policy_probability)
            else:
                score = self.policy_probability

            result[recalled] = score
        else:
            logger.debug("There is no memorised next action")

        return result

    def persist(self, path: Text) -> None:

        self.featurizer.persist(path)

        memorized_file = os.path.join(path, "memorized_turns.json")
        data = {
            "priority": self.priority,
            "max_history": self.max_history,
            "lookup": self.lookup,
            "policy_probability": self.policy_probability,
        }
        rasa.utils.io.create_directory_for_file(memorized_file)
        rasa.utils.io.dump_obj_as_json_to_file(memorized_file, data)

    @classmethod
    def load(cls, path: Text) -> "CustomMemoizationPolicy":

        featurizer = TrackerFeaturizer.load(path)
        memorized_file = os.path.join(path, "memorized_turns.json")
        if os.path.isfile(memorized_file):
            data = json.loads(rasa.utils.io.read_file(memorized_file))
            return cls(
                policy_probability=data["policy_probability"],featurizer=featurizer, priority=data["priority"], lookup=data["lookup"]
            )
        else:
            logger.info(
                "Couldn't load memoization for policy. "
                "File '{}' doesn't exist. Falling back to empty "
                "turn memory.".format(memorized_file)
            )
        return cls()


class TestMemoizationPolicy(Policy):
    """The policy that remembers exact examples of
        `max_history` turns from training stories.
        Since `slots` that are set some time in the past are
        preserved in all future feature vectors until they are set
        to None, this policy implicitly remembers and most importantly
        recalls examples in the context of the current dialogue
        longer than `max_history`.
        This policy is not supposed to be the only policy in an ensemble,
        it is optimized for precision and not recall.
        It should get a 100% precision because it emits probabilities of 1.1
        along it's predictions, which makes every mistake fatal as
        no other policy can overrule it.
        If it is needed to recall turns from training dialogues where
        some slots might not be set during prediction time, and there are
        training stories for this, use AugmentedMemoizationPolicy.
    """

    ENABLE_FEATURE_STRING_COMPRESSION = True

    SUPPORTS_ONLINE_TRAINING = True

    USE_NLU_CONFIDENCE_AS_SCORE = False

    @staticmethod
    def _standard_featurizer(
        max_history: Optional[int] = None,
    ) -> MaxHistoryTrackerFeaturizer:
        # Memoization policy always uses MaxHistoryTrackerFeaturizer
        # without state_featurizer
        return MaxHistoryTrackerFeaturizer(
            state_featurizer=None,
            max_history=max_history,
            use_intent_probabilities=False,
        )

    def __init__(
        self,
        policy_probability = 1.0,
        featurizer: Optional[TrackerFeaturizer] = None,
        priority: int = MEMOIZATION_POLICY_PRIORITY,
        max_history: Optional[int] = None,
        lookup: Optional[Dict] = None,
    ) -> None:

        if not featurizer:
            featurizer = self._standard_featurizer(max_history)

        super().__init__(featurizer, priority)

        self.max_history = self.featurizer.max_history
        self.lookup = lookup if lookup is not None else {}
        self.is_enabled = True
        self.policy_probability = policy_probability

    def toggle(self, activate: bool) -> None:
        self.is_enabled = activate

    def _add_states_to_lookup(
        self, trackers_as_states, trackers_as_actions, domain, online=False
    ) -> None:
        """Add states to lookup dict"""
        if not trackers_as_states:
            return

        assert len(trackers_as_states[0]) == self.max_history, (
            "Trying to mem featurized data with {} historic turns. Expected: "
            "{}".format(len(trackers_as_states[0]), self.max_history)
        )

        assert len(trackers_as_actions[0]) == 1, (
            "The second dimension of trackers_as_action should be 1, "
            "instead of {}".format(len(trackers_as_actions[0]))
        )

        ambiguous_feature_keys = set()

        pbar = tqdm(
            zip(trackers_as_states, trackers_as_actions),
            desc="Processed actions",
            disable=is_logging_disabled(),
        )
        for states, actions in pbar:
            action = actions[0]

            feature_key = self._create_feature_key(states)
            feature_item = domain.index_for_action(action)

            if feature_key not in ambiguous_feature_keys:
                if feature_key in self.lookup.keys():
                    if self.lookup[feature_key] != feature_item:
                        if online:
                            logger.info(
                                "Original stories are "
                                "different for {} -- {}\n"
                                "Memorized the new ones for "
                                "now. Delete contradicting "
                                "examples after exporting "
                                "the new stories."
                                "".format(states, action)
                            )
                            self.lookup[feature_key] = feature_item
                        else:
                            # delete contradicting example created by
                            # partial history augmentation from memory
                            ambiguous_feature_keys.add(feature_key)
                            del self.lookup[feature_key]
                else:
                    self.lookup[feature_key] = feature_item
            pbar.set_postfix({"# examples": "{:d}".format(len(self.lookup))})

    def _create_feature_key(self, states: List[Dict]) -> Text:
        from rasa.utils import io

        feature_str = json.dumps(states, sort_keys=True).replace('"', "")
        if self.ENABLE_FEATURE_STRING_COMPRESSION:
            compressed = zlib.compress(bytes(feature_str, io.DEFAULT_ENCODING))
            return base64.b64encode(compressed).decode(io.DEFAULT_ENCODING)
        else:
            return feature_str

    def train(
        self,
        training_trackers: List[DialogueStateTracker],
        domain: Domain,
        **kwargs: Any,
    ) -> None:
        """Trains the policy on given training trackers."""
        self.lookup = {}
        # only considers original trackers (no augmented ones)
        training_trackers = [
            t
            for t in training_trackers
            if not hasattr(t, "is_augmented") or not t.is_augmented
        ]

        ########################################################################################
        for t in training_trackers:
            logger.debug(t.current_state())
            logger.debug('---------------------------------------------\n\n')
        logger.debug('---------------------------------------------\n\n')
        ### unfeaturized
        '''
        2021-05-07 10:45:50 DEBUG    pyspace.rasa.nlg.memoization_policy  - {'sender_id': 'odeme_yapma_bes', 'slots': {'city': None, 'disambiguation_message': None, 'district': None, 'fallback_language': 'tr', 'requested_slot': None}, 'latest_message': {'text': '/odeme_yapma{"urun_type": "BES"}', 'intent': {'name': 'odeme_yapma', 'confidence': 1.0}, 'intent_ranking': [{'name': 'odeme_yapma', 'confidence': 1.0}], 'entities': [{'entity': 'urun_type', 'start': 11, 'end': 31, 'value': 'BES'}]}, 'latest_event_time': 1620384339.1564314, 'followup_action': None, 'paused': False, 'events': None, 'latest_input_channel': None, 'active_form': {}, 'latest_action_name': 'action_listen'}
        2021-05-07 10:45:50 DEBUG    pyspace.rasa.nlg.memoization_policy  - {'sender_id': 'hesap_birlestirme_bes', 'slots': {'city': None, 'disambiguation_message': None, 'district': None, 'fallback_language': 'tr', 'requested_slot': None}, 'latest_message': {'text': '/hesap_birlestirme{"urun_type": "BES"}', 'intent': {'name': 'hesap_birlestirme', 'confidence': 1.0}, 'intent_ranking': [{'name': 'hesap_birlestirme', 'confidence': 1.0}], 'entities': [{'entity': 'urun_type', 'start': 17, 'end': 37, 'value': 'BES'}]}, 'latest_event_time': 1620384339.1176512, 'followup_action': None, 'paused': False, 'events': None, 'latest_input_channel': None, 'active_form': {}, 'latest_action_name': 'action_listen'}
        2021-05-07 10:45:50 DEBUG    pyspace.rasa.nlg.memoization_policy  - {'sender_id': 'borc_alma_hayat', 'slots': {'city': None, 'disambiguation_message': None, 'district': None, 'fallback_language': 'tr', 'requested_slot': None}, 'latest_message': {'text': '/borc_alma{"urun_type": "HS"}', 'intent': {'name': 'borc_alma', 'confidence': 1.0}, 'intent_ranking': [{'name': 'borc_alma', 'confidence': 1.0}], 'entities': [{'entity': 'urun_type', 'start': 9, 'end': 28, 'value': 'HS'}]}, 'latest_event_time': 1620384339.126703, 'followup_action': None, 'paused': False, 'events': None, 'latest_input_channel': None, 'active_form': {}, 'latest_action_name': 'action_listen'}

        '''
        ### categorical
        '''
        2021-05-07 11:59:17 DEBUG    pyspace.rasa.nlg.memoization_policy  - {'sender_id': 'odeme_yapma_bes', 'slots': {'city': None, 'disambiguation_message': None, 'district': None, 'fallback_language': 'tr', 'urun_type': None, 'ygk': None, 'requested_slot': None}, 'latest_message': {'text': '/odeme_yapma_bes', 'intent': {'name': 'odeme_yapma_bes', 'confidence': 1.0}, 'intent_ranking': [{'name': 'odeme_yapma_bes', 'confidence': 1.0}], 'entities': []}, 'latest_event_time': 1620388742.697043, 'followup_action': None, 'paused': False, 'events': None, 'latest_input_channel': None, 'active_form': {}, 'latest_action_name': 'action_listen'}
        2021-05-07 11:59:17 DEBUG    pyspace.rasa.nlg.memoization_policy  - {'sender_id': 'odeme_yapma_bes', 'slots': {'city': None, 'disambiguation_message': None, 'district': None, 'fallback_language': 'tr', 'urun_type': 'BES', 'ygk': None, 'requested_slot': None}, 'latest_message': {'text': '/odeme_yapma{"urun_type": "BES"}', 'intent': {'name': 'odeme_yapma', 'confidence': 1.0}, 'intent_ranking': [{'name': 'odeme_yapma', 'confidence': 1.0}], 'entities': [{'entity': 'urun_type', 'start': 11, 'end': 31, 'value': 'BES'}]}, 'latest_event_time': 1620388742.697043, 'followup_action': None, 'paused': False, 'events': None, 'latest_input_channel': None, 'active_form': {}, 'latest_action_name': 'action_listen'}
        2021-05-07 11:59:17 DEBUG    pyspace.rasa.nlg.memoization_policy  - {'sender_id': 'hesap_birlestirme_bes', 'slots': {'city': None, 'disambiguation_message': None, 'district': None, 'fallback_language': 'tr', 'urun_type': 'BES', 'ygk': None, 'requested_slot': None}, 'latest_message': {'text': '/hesap_birlestirme{"urun_type": "BES"}', 'intent': {'name': 'hesap_birlestirme', 'confidence': 1.0}, 'intent_ranking': [{'name': 'hesap_birlestirme', 'confidence': 1.0}], 'entities': [{'entity': 'urun_type', 'start': 17, 'end': 37, 'value': 'BES'}]}, 'latest_event_time': 1620388742.6543787, 'followup_action': None, 'paused': False, 'events': None, 'latest_input_channel': None, 'active_form': {}, 'latest_action_name': 'action_listen'}
        2021-05-07 11:59:17 DEBUG    pyspace.rasa.nlg.memoization_policy  - {'sender_id': 'borc_alma_hayat', 'slots': {'city': None, 'disambiguation_message': None, 'district': None, 'fallback_language': 'tr', 'urun_type': 'HS', 'ygk': None, 'requested_slot': None}, 'latest_message': {'text': '/borc_alma{"urun_type": "HS"}', 'intent': {'name': 'borc_alma', 'confidence': 1.0}, 'intent_ranking': [{'name': 'borc_alma', 'confidence': 1.0}], 'entities': [{'entity': 'urun_type', 'start': 9, 'end': 28, 'value': 'HS'}]}, 'latest_event_time': 1620388742.6638176, 'followup_action': None, 'paused': False, 'events': None, 'latest_input_channel': None, 'active_form': {}, 'latest_action_name': 'action_listen'}
        '''

        ### unfeaturized vs categorical
        '''
        slots: {'urun_type': 'BES', 'ygk': None, }

        '''

        ########################################################################################
        (
            trackers_as_states,
            trackers_as_actions,
        ) = self.featurizer.training_states_and_actions(training_trackers, domain)

        ########################################################################################
        for s,a in zip(trackers_as_states, trackers_as_actions):
            logger.debug(s)
            logger.debug(a)
            logger.debug('---------------------------------------------\n\n')    
        logger.debug('---------------------------------------------\n\n')
        ### unfeaturized
        '''
        2021-05-07 10:45:51 DEBUG    pyspace.rasa.nlg.memoization_policy  - [None, None, None, {}, {'intent_urun_bilgi': 1.0, 'prev_action_listen': 1.0, 'entity_urun_type': 1.0}]
        2021-05-07 10:45:51 DEBUG    pyspace.rasa.nlg.memoization_policy  - ['utter_a6-f-7X1jv']
        2021-05-07 10:45:51 DEBUG    pyspace.rasa.nlg.memoization_policy  - ---------------------------------------------

        2021-05-07 10:45:51 DEBUG    pyspace.rasa.nlg.memoization_policy  - [None, None, {}, {'intent_urun_bilgi': 1.0, 'prev_action_listen': 1.0, 'entity_urun_type': 1.0}, {'intent_urun_bilgi': 1.0, 'prev_utter_a6-f-7X1jv': 1.0, 'entity_urun_type': 1.0}]
        2021-05-07 10:45:51 DEBUG    pyspace.rasa.nlg.memoization_policy  - ['utter_k97J6qWB7']
        2021-05-07 10:45:51 DEBUG    pyspace.rasa.nlg.memoization_policy  - ---------------------------------------------
        '''
        ### categorical
        '''
        2021-05-07 11:59:17 DEBUG    pyspace.rasa.nlg.memoization_policy  - [None, None, None, {}, {'prev_action_listen': 1.0, 'slot_urun_type_3': 1.0, 'intent_urun_bilgi': 1.0, 'entity_urun_type': 1.0}]
        2021-05-07 11:59:17 DEBUG    pyspace.rasa.nlg.memoization_policy  - ['utter_a6-f-7X1jv']
        2021-05-07 11:59:17 DEBUG    pyspace.rasa.nlg.memoization_policy  - ---------------------------------------------

        2021-05-07 11:59:17 DEBUG    pyspace.rasa.nlg.memoization_policy  - [None, None, {}, {'prev_action_listen': 1.0, 'slot_urun_type_3': 1.0, 'intent_urun_bilgi': 1.0, 'entity_urun_type': 1.0}, {'slot_urun_type_3': 1.0, 'intent_urun_bilgi': 1.0, 'prev_utter_a6-f-7X1jv': 1.0, 'entity_urun_type': 1.0}]
        2021-05-07 11:59:17 DEBUG    pyspace.rasa.nlg.memoization_policy  - ['utter_k97J6qWB7']
        2021-05-07 11:59:17 DEBUG    pyspace.rasa.nlg.memoization_policy  - ---------------------------------------------
        '''
        ########################################################################################

        self._add_states_to_lookup(trackers_as_states, trackers_as_actions, domain)


        ########################################################################################

        # for l in self.lookup:
        #     logger.debug(l)
        #     logger.debug(self.lookup[l])
        #     logger.debug('---------------------------------------------\n\n')    
        # logger.debug('---------------------------------------------\n\n')

        '''
        2021-05-07 10:45:51 DEBUG    pyspace.rasa.nlg.memoization_policy  - eJyLzivNydFRgJDVtUCcmleSWVIZX1pUmhdfUlmQaqVgqGego5CZVwKUiU/KL0qOT8zJTYQKFxSllsUnJpdk5ufF52QWA9WAJcg0qLSkJLUoPivZxM+toDIlMQdiViwA9to5ww==
        2021-05-07 10:45:51 DEBUG    pyspace.rasa.nlg.memoization_policy  - ---------------------------------------------

        2021-05-07 10:45:51 DEBUG    pyspace.rasa.nlg.memoization_policy  - eJyLzivNydFRQCara4E4M68kNa8kPic1oySxKDMvPiMxOwfIsFIw1DPQUSgoSi2LT0wuyczPi8/JLAYqBUvUxgIAdQ4cMw==
        2021-05-07 10:45:51 DEBUG    pyspace.rasa.nlg.memoization_policy  - ---------------------------------------------

        2021-05-07 10:45:51 DEBUG    pyspace.rasa.nlg.memoization_policy  - eJyLzivNydFRgJDVtUCcmVeSmlcSn5OaUZJYlJkXn5GYnQNkWCkY6hnoKBQUpZbFJyaXZObnxedkFgOVgiWI1FhaUpJaFO8S6B9hnpNWFgXRGgsAZhgu1Q==
        2021-05-07 10:45:51 DEBUG    pyspace.rasa.nlg.memoization_policy  - ---------------------------------------------
        '''
        
        ########################################################################################


        logger.debug("Memorized {} unique examples.".format(len(self.lookup)))

    def _recall_states(self, states: List[Dict[Text, float]]) -> Optional[int]:

        return self.lookup.get(self._create_feature_key(states))

    def recall(
        self,
        states: List[Dict[Text, float]],
        tracker: DialogueStateTracker,
        domain: Domain,
    ) -> Optional[int]:

        return self._recall_states(states)

    def predict_action_probabilities(
        self, tracker: DialogueStateTracker, domain: Domain
    ) -> List[float]:
        """Predicts the next action the bot should take after seeing the tracker.
        Returns the list of probabilities for the next actions.
        If memorized action was found returns 1 for its index,
        else returns 0 for all actions.
        """
        result = self._default_predictions(domain)

        if not self.is_enabled:
            return result

        tracker_as_states = self.featurizer.prediction_states([tracker], domain)
        states = tracker_as_states[0]
        logger.debug(f"Current tracker state {states}")
        recalled = self.recall(states, tracker, domain)
        if recalled is not None:
            logger.debug(
                f"There is a memorised next action '{domain.action_names[recalled]}'"
            )

            if self.USE_NLU_CONFIDENCE_AS_SCORE:
                # the memoization will use the confidence of NLU on the latest
                # user message to set the confidence of the action
                score = tracker.latest_message.intent.get("confidence", self.policy_probability)
            else:
                score = self.policy_probability

            result[recalled] = score
        else:
            logger.debug("There is no memorised next action")

        return result

    def persist(self, path: Text) -> None:

        self.featurizer.persist(path)

        memorized_file = os.path.join(path, "memorized_turns.json")
        data = {
            "priority": self.priority,
            "max_history": self.max_history,
            "lookup": self.lookup,
            "policy_probability": self.policy_probability,
        }
        rasa.utils.io.create_directory_for_file(memorized_file)
        rasa.utils.io.dump_obj_as_json_to_file(memorized_file, data)

    @classmethod
    def load(cls, path: Text) -> "CustomMemoizationPolicy":

        featurizer = TrackerFeaturizer.load(path)
        memorized_file = os.path.join(path, "memorized_turns.json")
        if os.path.isfile(memorized_file):
            data = json.loads(rasa.utils.io.read_file(memorized_file))
            return cls(
                policy_probability=data["policy_probability"],featurizer=featurizer, priority=data["priority"], lookup=data["lookup"]
            )
        else:
            logger.info(
                "Couldn't load memoization for policy. "
                "File '{}' doesn't exist. Falling back to empty "
                "turn memory.".format(memorized_file)
            )
        return cls()



class MemoizationPolicy(Policy):

    @staticmethod
    def _standard_featurizer(max_history: Optional[int] = None,) -> MaxHistoryTrackerFeaturizer:
        return MaxHistoryTrackerFeaturizer(state_featurizer=None,max_history=max_history,use_intent_probabilities=False,)

    def __init__(self,policy_probability = 1.0,
                config = [[0, 'default', 3]],
                priority = MEMOIZATION_POLICY_PRIORITY,
                lookup = None,) -> None:

        super().__init__(None, priority)

        self.config = sorted(config, key=lambda x:x[0])
        self.config_x = []
        
        for ci in self.config:
            self.config_x.append( [ci[1], self._standard_featurizer(ci[2])] )

        self.lookup = lookup if lookup is not None else {}
        self.policy_probability = policy_probability

    def _add_states_to_lookup(self, trackers_as_states, trackers_as_actions, domain, online=False) -> None:
        if not trackers_as_states:
            return

        ambiguous_feature_keys = set()

        pbar = tqdm(zip(trackers_as_states, trackers_as_actions),desc="Processed actions",disable=is_logging_disabled(),)
        for states, actions in pbar:
            action = actions[0]

            feature_key = self._create_feature_key(states)
            feature_item = domain.index_for_action(action)

            if feature_key not in ambiguous_feature_keys:
                if feature_key in self.lookup.keys():
                    if self.lookup[feature_key] != feature_item:
                        if online:
                            self.lookup[feature_key] = feature_item
                        else:
                            #################################################################
                            logger.debug("AMBIGUOUS STATES\n")
                            logger.debug(states)
                            logger.debug(action)
                            #################################################################

                            ambiguous_feature_keys.add(feature_key)
                            # del self.lookup[feature_key]
                else:
                    self.lookup[feature_key] = feature_item
            pbar.set_postfix({"# examples": "{:d}".format(len(self.lookup))})

    def _create_feature_key(self, states: List[Dict]) -> Text:
        from rasa.utils import io
        feature_str = json.dumps(states, sort_keys=True).replace('"', "")
        compressed = zlib.compress(bytes(feature_str, io.DEFAULT_ENCODING))
        return base64.b64encode(compressed).decode(io.DEFAULT_ENCODING)

    def train(self,training_trackers: List[DialogueStateTracker],domain: Domain,**kwargs: Any,) -> None:
        """Trains the policy on given training trackers."""
        self.lookup = {}

        for ci in self.config_x:
            (trackers_as_states, trackers_as_actions,) = ci[1].training_states_and_actions(training_trackers, domain)
            self._add_states_to_lookup(trackers_as_states, trackers_as_actions, domain)

        logger.debug("Memorized {} unique examples.".format(len(self.lookup)))

    def _recall_states(self, states: List[Dict[Text, float]]) -> Optional[int]:

        return self.lookup.get(self._create_feature_key(states))

    def recall(
        self,
        states: List[Dict[Text, float]],
        tracker: DialogueStateTracker,
        domain: Domain,
    ) -> Optional[int]:

        return self._recall_states(states)

    def predict_action_probabilities(
        self, tracker: DialogueStateTracker, domain: Domain
    ) -> List[float]:
        """Predicts the next action the bot should take after seeing the tracker.
        Returns the list of probabilities for the next actions.
        If memorized action was found returns 1 for its index,
        else returns 0 for all actions.
        """
        logger.debug("-------------------------------------------------------------------------------")

        ## TODO
        # [{'intent_acenteler': 1.0, 'prev_action_listen': 1.0}, 
        # {'prev_city_district_for_agent_form': 1.0, 'active_form_city_district_for_agent_form': 1.0, 'intent_acenteler': 1.0}, 
        # {'entity_district': 1.0, 'active_form_city_district_for_agent_form': 1.0, 'intent_inform': 1.0, 'prev_action_listen': 1.0}]
        
        result = self._default_predictions(domain)

        for ci in self.config_x:
            
            tracker_as_states = ci[1].prediction_states([tracker], domain)
            states = tracker_as_states[0]
            
            memoization_slot_mode = ci[0]
            memoization_history = ci[1].max_history
            logger.debug(f" >> Memoization slot mode : {memoization_slot_mode}, history : {memoization_history}")
            # logger.debug(ci[0])
            # logger.debug(ci[1].max_history)

            if ci[0] == 'default':
                pass
            elif ci[0] == 'no_prev_slot':
                logger.debug(f"Raw tracker state {states}")
                # {'sender_id': 'odeme_yapma_bes', 'slots': {'city': None, 'disambiguation_message': None, 'district': None, 'fallback_language': 'tr', 'urun_type': 'BES', 'ygk': None, 'requested_slot': None}, 
                # 'latest_message': {'text': '/odeme_yapma{"urun_type": "BES"}', 'intent': {'name': 'odeme_yapma', 'confidence': 1.0}, 'intent_ranking': [{'name': 'odeme_yapma', 'confidence': 1.0}], 
                # 'entities': [{'entity': 'urun_type', 'start': 11, 'end': 31, 'value': 'BES'}]}, 
                # 'latest_event_time': 1620388742.697043, 'followup_action': None, 'paused': False, 'events': None, 'latest_input_channel': None, 'active_form': {}, 'latest_action_name': 'action_listen'}

                tracker_current = tracker.current_state()
                entities = tracker_current['latest_message']['entities']
                entities = set([e['entity'] for e in entities])

                # tracker_state_entities = set(
                #     [tas_k[7:] for tas in states for tas_k in tas if tas is not None and tas_k[:7] == 'entity_'] +
                #     [tas_k[5:].rsplit('_',1)[0] for tas in states for tas_k in tas if tas is not None and tas_k[:5] == 'slot_']
                # )
                tracker_state_entities = set(
                    [tas_k[7:] for tas in states if tas is not None for tas_k in tas if tas_k[:7] == 'entity_'] +
                    [tas_k[5:].rsplit('_',1)[0] for tas in states if tas is not None for tas_k in tas if tas_k[:5] == 'slot_']
                )
                remove_entities = tracker_state_entities - entities

                for _rent in remove_entities:
                    for tas in states:
                        if tas is not None:
                            for tas_k in list(tas):
                                if tas_k[:7+len(_rent)] == 'entity_'+_rent:
                                    del tas[tas_k]
                                elif tas_k[:5+len(_rent)] == 'slot_'+_rent:
                                    del tas[tas_k]


                pass
            elif ci[0] == 'no_slot':
                logger.debug(f"Raw tracker state {states}")
                for tas in states:
                    if tas is not None:
                        for tas_k in list(tas):
                            # [None, None, {}, {'intent_urun_bilgi': 1.0, 'prev_action_listen': 1.0, 'entity_urun_type': 1.0}, 
                            # {'intent_urun_bilgi': 1.0, 'prev_utter_a6-f-7X1jv': 1.0, 'entity_urun_type': 1.0}]
                            if tas_k[:7] == 'entity_':
                                del tas[tas_k]
                            elif tas_k[:5] == 'slot_':
                                del tas[tas_k]

                pass

            logger.debug(f"Current tracker state {states}")
            recalled = self.recall(states, tracker, domain)
            if recalled is not None:
                logger.debug(f"There is a memorised next action '{domain.action_names[recalled]}'" )
                logger.debug("-------------------------------------------------------------------------------")

                score = self.policy_probability
                result[recalled] = score
                return result
            else:
                logger.debug("There is no memorised next action")

        return result

    def persist(self, path: Text) -> None:
        memorized_file = os.path.join(path, "memorized_turns.json")
        data = {
            "priority": self.priority,
            "config": self.config,
            "lookup": self.lookup,
            "policy_probability": self.policy_probability,
        }
        rasa.utils.io.create_directory_for_file(memorized_file)
        rasa.utils.io.dump_obj_as_json_to_file(memorized_file, data)

    @classmethod
    def load(cls, path: Text) -> "MemoizationPolicy":
        memorized_file = os.path.join(path, "memorized_turns.json")
        data = json.loads(rasa.utils.io.read_file(memorized_file))
        return cls(policy_probability=data["policy_probability"],config=data["config"], priority=data["priority"], lookup=data["lookup"])
