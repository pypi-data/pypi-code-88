# -*- coding:utf-8 -*-
import logging as log
from typing import Dict, List, Any

from fameio.source.logs import log_error_and_raise
from fameio.source.schema.schema import Schema
from fameio.source.time import FameTime
from fameio.source.tools import keys_to_lower, ensure_is_list


def _get_or_raise(dictionary: dict, key: str, message: str):
    """Returns value associated with `key` in given `dictionary`, or raises ScenarioException if key is missing"""
    if key not in dictionary:
        log_error_and_raise(ScenarioException(message.format(key)))
    else:
        return dictionary[key]


def _get_or_default(dictionary: dict, key: str, default_value):
    """Returns value associated with `key` in given `dictionary`, or the given `default_value` if key is missing"""
    if key in dictionary:
        return dictionary[key]
    else:
        log.debug("Using default value '{}' for missing key '{}'".format(default_value, key))
        return default_value


class ScenarioException(Exception):
    """Indicates an error while parsing a scenario or one of its components"""
    pass


class Attribute:
    """An Attribute of an agent in a scenario"""
    _VALUE_MISSING = "Value not specified for Attribute '{}' - leave out if default shall be used (if defined)."
    _OVERWRITE = "Value already defined for Attribute '{}' - overwriting value with new one!"
    _LIST_EMPTY = "Attribute '{}' was assigned an empty list - please remove or fill empty assignments."
    _DICT_EMPTY = "Attribute '{}' was assigned an empty dictionary - please remove or fill empty assignments."
    _MIXED_DATA = "Attribute '{}' was assigned a list with mixed complex and simple entries - please fix."

    def __init__(self, name: str, definitions) -> None:
        """Parses an Attribute's definition"""
        self._full_name = name

        if definitions is None:
            log_error_and_raise(ScenarioException(Attribute._VALUE_MISSING.format(name)))

        if isinstance(definitions, dict):
            self.value = None
            self.nested_list = None
            self.nested = Attribute._build_attribute_dict(name, definitions)
        elif Attribute._is_list_of_dict(name, definitions):
            self.nested = None
            self.value = None
            self.nested_list = list()
            for entry in definitions:
                self.nested_list.append(Attribute._build_attribute_dict(name, entry))
        else:
            self.nested = None
            self.nested_list = None
            self.value = definitions

    @staticmethod
    def _build_attribute_dict(name: str, definitions: Dict[str, Any]) -> Dict[str, 'Attribute']:
        """Returns a new dictionary containing Attributes generated from given `definitions` """
        if not definitions:
            log_error_and_raise(ScenarioException(Attribute._DICT_EMPTY.format(name)))

        dictionary = dict()
        for nested_name, value in definitions.items():
            full_name = name + "." + nested_name
            if nested_name in dictionary:
                log.warning(Attribute._OVERWRITE.format(full_name))
            dictionary[nested_name] = Attribute(full_name, value)
        return dictionary

    @staticmethod
    def _is_list_of_dict(name: str, definitions: Any) -> bool:
        """Returns True if given `definitions` is a list of dict"""
        if isinstance(definitions, list):
            if not definitions:
                log_error_and_raise(ScenarioException(Attribute._LIST_EMPTY.format(name)))

            all_dicts = no_dicts = True
            for item in definitions:
                if not isinstance(item, dict):
                    all_dicts = False
                else:
                    no_dicts = False
            if (not all_dicts) and (not no_dicts):
                log_error_and_raise(ScenarioException(Attribute._MIXED_DATA.format(name)))
            return all_dicts
        return False

    def has_nested(self) -> bool:
        """Returns True if nested Attributes are present"""
        return bool(self.nested)

    def has_nested_list(self) -> bool:
        """Returns True if list of nested items are present"""
        return bool(self.nested_list)

    def get_nested_by_name(self, key: str) -> 'Attribute':
        """Returns nested Attribute by specified name"""
        return self.nested[key]

    def get_nested_list(self) -> List[Dict[str, 'Attribute']]:
        """Return list of all nested Attribute dictionaries"""
        return self.nested_list

    def get_nested(self) -> Dict[str, 'Attribute']:
        """Returns dictionary of all nested Attributes"""
        return self.nested

    def has_value(self) -> bool:
        """Returns True if Attribute has any value assigned"""
        return self.value is not None

    def __repr__(self) -> str:
        return self._full_name


class Contract:
    """Contract between two Agents of a scenario"""
    _KEY_SENDER = "SenderId".lower()
    _KEY_RECEIVER = "ReceiverId".lower()
    _KEY_PRODUCT = "ProductName".lower()
    _KEY_FIRST_DELIVERY = "FirstDeliveryTime".lower()
    _KEY_INTERVAL = "DeliveryIntervalInSteps".lower()
    _KEY_EXPIRE = "ExpirationTime".lower()
    _KEY_ATTRIBUTES = "Attributes".lower()

    _MISSING_KEY = "Contract requires key '{}' but is missing it."
    _MULTI_CONTRACT_CORRUPT = "Definition of Contracts is valid only for One-to-One, One-to-many, Many-to-one, " \
                              "or N-to-N sender-to-receiver numbers. Found M-to-N pairing in Contract with " \
                              "Senders: {} and Receivers: {}."

    def __init__(self, definitions: dict) -> None:
        """Parses Contract from given `definitions`"""
        definitions = keys_to_lower(definitions)
        self.sender_id = _get_or_raise(definitions, Contract._KEY_SENDER, Contract._MISSING_KEY)
        self.receiver_id = _get_or_raise(definitions, Contract._KEY_RECEIVER, Contract._MISSING_KEY)
        self.product = _get_or_raise(definitions, Contract._KEY_PRODUCT, Contract._MISSING_KEY)
        self.first_delivery = FameTime.convert_string_if_is_datetime(
            _get_or_raise(definitions, Contract._KEY_FIRST_DELIVERY, Contract._MISSING_KEY))
        self.delivery_interval = _get_or_raise(definitions, Contract._KEY_INTERVAL, Contract._MISSING_KEY)
        expiration_time = _get_or_default(definitions, Contract._KEY_EXPIRE, None)
        self.expiration_time = FameTime.convert_string_if_is_datetime(expiration_time) if expiration_time else None
        self.attributes = dict()
        for name, value in _get_or_default(definitions, Contract._KEY_ATTRIBUTES, dict()).items():
            full_name = str(type) + "." + str(id) + name
            self.attributes[name] = Attribute(full_name, value)

    def get_attributes(self) -> Dict[str, Attribute]:
        """Returns dictionary of all Attributes of this agent"""
        return self.attributes

    @staticmethod
    def split_contract_definitions(multi_definition: dict) -> List[dict]:
        """Splits given `multi_definition` dictionary into list of individual Contract definitions"""
        contracts = list()
        base_data = dict()
        multi_definition = keys_to_lower(multi_definition)
        for key in [Contract._KEY_PRODUCT, Contract._KEY_FIRST_DELIVERY, Contract._KEY_FIRST_DELIVERY,
                    Contract._KEY_INTERVAL, Contract._KEY_EXPIRE, Contract._KEY_ATTRIBUTES]:
            if key in multi_definition:
                base_data[key] = multi_definition[key]
        senders = ensure_is_list(_get_or_raise(multi_definition, Contract._KEY_SENDER, Contract._MISSING_KEY))
        receivers = ensure_is_list(_get_or_raise(multi_definition, Contract._KEY_RECEIVER, Contract._MISSING_KEY))
        if len(senders) > 1 and len(receivers) == 1:
            for index in range(len(senders)):
                contracts.append(Contract._copy_contract(senders[index], receivers[0], base_data))
        elif len(senders) == 1 and len(receivers) > 1:
            for index in range(len(receivers)):
                contracts.append(Contract._copy_contract(senders[0], receivers[index], base_data))
        elif len(senders) == len(receivers):
            for index in range(len(senders)):
                contracts.append(Contract._copy_contract(senders[index], receivers[index], base_data))
        else:
            log_error_and_raise(ScenarioException(Contract._MULTI_CONTRACT_CORRUPT.format(senders, receivers)))
        return contracts

    @staticmethod
    def _copy_contract(sender: int, receiver: int, base_data: dict) -> dict:
        """Returns a new contract definition dictionary, with given `sender` and `receiver` and copied `base_data`"""
        contract = dict()
        contract[Contract._KEY_SENDER] = sender
        contract[Contract._KEY_RECEIVER] = receiver
        contract.update(base_data)
        return contract


class Agent:
    """Contains specifications for an agent in a scenario"""
    _KEY_TYPE = "Type".lower()
    _KEY_ID = "Id".lower()
    _KEY_ATTRIBUTES = "Attributes".lower()

    _MISSING_KEY = "Agent requires key '{}' but is missing it."

    def __init__(self, definitions: dict) -> None:
        """Parses an agent from provided `definitions`"""
        definitions = keys_to_lower(definitions)
        self.type = _get_or_raise(definitions, Agent._KEY_TYPE, Agent._MISSING_KEY)
        self.id = _get_or_raise(definitions, Agent._KEY_ID, Agent._MISSING_KEY)
        attribute_definitions = _get_or_default(definitions, Agent._KEY_ATTRIBUTES, dict())
        self.attributes = dict()
        for name, value in attribute_definitions.items():
            full_name = str(self.type) + "(" + str(self.id) + "): " + name
            self.attributes[name] = Attribute(full_name, value)

    def get_attributes(self) -> Dict[str, Attribute]:
        """Returns dictionary of all Attributes of this agent"""
        return self.attributes


class General:
    """Hosts general properties of this scenario"""
    _KEY_RUN = "RunId".lower()
    _KEY_SIMULATION = "Simulation".lower()
    _KEY_START = "StartTime".lower()
    _KEY_STOP = "StopTime".lower()
    _KEY_SEED = "RandomSeed".lower()
    _KEY_OUTPUT = "Output".lower()
    _KEY_INTERVAL = "Interval".lower()
    _KEY_PROCESS = "Process".lower()

    _MISSING_KEY = "General Properties requires key '{}' but it is missing."
    _SIMULATION_DURATION = "Simulation starts after its end time - check start and stop times."

    def __init__(self, definitions: dict) -> None:
        """Parse general properties from provided `definitions`"""
        definitions = keys_to_lower(definitions)
        self.run_id = _get_or_default(definitions, General._KEY_RUN, 1)

        simulation_definition = keys_to_lower(_get_or_raise(definitions, General._KEY_SIMULATION, General._MISSING_KEY))
        self.start_time = FameTime.convert_string_if_is_datetime(
            _get_or_raise(simulation_definition, General._KEY_START, General._MISSING_KEY))
        self.stop_time = FameTime.convert_string_if_is_datetime(
            _get_or_raise(simulation_definition, General._KEY_STOP, General._MISSING_KEY))
        if self.stop_time < self.start_time:
            log.warning(General._SIMULATION_DURATION)
        self.random_seed = _get_or_default(simulation_definition, General._KEY_SEED, 1)

        output_definitions = keys_to_lower(_get_or_default(definitions, General._KEY_OUTPUT, dict()))
        self.output_interval = _get_or_default(output_definitions, General._KEY_INTERVAL, 100)
        self.output_process = _get_or_default(output_definitions, General._KEY_PROCESS, 0)


class Scenario:
    """Definition of a scenario"""
    _KEY_SCHEMA = "Schema".lower()
    _KEY_GENERAL = "GeneralProperties".lower()
    _KEY_AGENTS = "Agents".lower()
    _KEY_CONTRACTS = "Contracts".lower()

    _MISSING_KEY = "Scenario definition misses required key '{}'."
    _AGENT_ID_NOT_UNIQUE = "Agents ID not unique: '{}.'"
    _AGENT_TYPE_UNKNOWN = "Agent type '{}' not known in Schema."

    def __init__(self, definitions: dict) -> None:
        """Parse scenario from provided `definitions`"""
        definitions = keys_to_lower(definitions)

        self._schema = Schema(_get_or_raise(definitions, Scenario._KEY_SCHEMA, Scenario._MISSING_KEY))
        self._general = General(_get_or_raise(definitions, Scenario._KEY_GENERAL, Scenario._MISSING_KEY))

        self._agents = list()
        self._agent_type_by_id = dict()
        for agent_definition in _get_or_raise(definitions, Scenario._KEY_AGENTS, Scenario._MISSING_KEY):
            self.add_agent(Agent(agent_definition))

        self._contracts = list()
        for multi_definition in _get_or_raise(definitions, Scenario._KEY_CONTRACTS, Scenario._MISSING_KEY):
            for single_contract_definition in Contract.split_contract_definitions(multi_definition):
                self._contracts.append(Contract(single_contract_definition))

    def add_agent(self, agent: Agent) -> None:
        """Adds an agent to this scenario - raises an Exception if id is not unique"""
        if agent.id in self._agent_type_by_id:
            log_error_and_raise(ScenarioException(Scenario._AGENT_ID_NOT_UNIQUE.format(agent.id)))
        if agent.type not in self._schema.types:
            log_error_and_raise(ScenarioException(Scenario._AGENT_TYPE_UNKNOWN.format(agent.type)))
        self._agent_type_by_id[agent.id] = agent.type
        self._agents.append(agent)

    def get_agents(self) -> List[Agent]:
        """Returns list of all Agents declared in this scenario"""
        return self._agents

    def get_schema(self) -> Schema:
        """Returns Schema associated with this scenario"""
        return self._schema

    def get_contracts(self):
        """Returns Contracts declared in this scenario"""
        return self._contracts

    def get_agent_type_by_id(self) -> Dict[int, str]:
        """Returns dictionary of AgentTypes by agent-ids"""
        return self._agent_type_by_id

    def get_general_properties(self) -> General:
        """Returns General properties of this scenario"""
        return self._general
