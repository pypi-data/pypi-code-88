# Copyright 2020 Q-CTRL Pty Ltd & Q-CTRL Inc. All rights reserved.
#
# Licensed under the Q-CTRL Terms of service (the "License"). Unauthorized
# copying or use of this file, via any medium, is strictly prohibited.
# Proprietary and confidential. You may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#     https://q-ctrl.com/terms
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS. See the
# License for the specific language.
# pylint:disable=missing-module-docstring
from copy import deepcopy
from typing import Any

from gql import Client
from graphql import (
    DocumentNode,
    GraphQLType,
)
from qctrlcommons.exceptions import QctrlGqlException

from .base import PatternQuery
from .multi import (
    MultiQuery,
    _suffix_document,
)
from .refresh_action import RefreshActionQuery


class StartActionQuery(PatternQuery):  # pylint:disable=too-few-public-methods
    """Query used to start an action."""

    query_pattern = """
        mutation startAction {
            %(mutation_name)s(input: %(payload)s)
            %(selection)s
        }
    """
    _action_selection_override = {
        "action": r"{ modelId name status errors { exception } progress }"
    }

    def __init__(
        self,
        client: Client,
        env: "GraphQLCustomEnvironment",
        mutation_name: str,
        input_type: GraphQLType,
        result_type: GraphQLType,
        data: Any,
    ):
        payload = env.format_payload(input_type, data)
        selection = env.get_selection(result_type, self._action_selection_override)

        super().__init__(
            client,
            mutation_name=mutation_name,
            payload=payload,
            selection=selection,
        )

        self._env = env
        self._result_type = result_type

    def create_result_object(self, data: Any) -> Any:
        """Creates a result object to store the response data."""
        result = self._env.load_data(self._result_type, data)

        if result.errors:
            raise QctrlGqlException(result.errors)

        return result

    def get_refresh_query(self) -> RefreshActionQuery:
        """Get the corresponding refresh query."""
        return self._env.build_refresh_query(self._result_type)


class MultiStartActionQuery(MultiQuery):
    """Starts multiple actions."""

    name = "startActions"

    def _transform_sub_query_document(
        self, index: int, document: DocumentNode
    ) -> DocumentNode:
        document = deepcopy(document)
        _suffix_document(document, str(index + 1))
        return document
