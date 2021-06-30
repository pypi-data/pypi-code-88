# -*- coding:utf-8 -*-

from fameio.source.logs import log_error_and_raise
from fameio.source.schema.agent import AgentType
from fameio.source.schema.exception import SchemaException
from fameio.source.tools import keys_to_lower


class Schema:
    """Definition of a schema"""
    _AGENT_TYPES_MISSING = "Keyword AgentTypes not found in Schema."

    _KEY_AGENT_TYPE = 'AgentTypes'.lower()

    def __init__(self, definition: dict):
        """Load definitions from given `schema`"""
        definition = keys_to_lower(definition)
        if Schema._KEY_AGENT_TYPE not in definition:
            log_error_and_raise(SchemaException(Schema._AGENT_TYPES_MISSING))

        self.types = dict()
        for agent_type_name, agent_definition in definition[Schema._KEY_AGENT_TYPE].items():
            self.types[agent_type_name] = AgentType(agent_type_name, agent_definition)
