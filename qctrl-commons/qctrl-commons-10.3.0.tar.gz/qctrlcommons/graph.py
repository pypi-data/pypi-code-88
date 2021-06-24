# Copyright 2021 Q-CTRL. All rights reserved.
#
# Licensed under the Q-CTRL Terms of service (the "License"). Unauthorized
# copying or use of this file, via any medium, is strictly prohibited.
# Proprietary and confidential. You may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#      https://q-ctrl.com/terms
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS. See the
# License for the specific language.
"""Module for custom Graph."""
import logging
from typing import (
    Callable,
    Dict,
    List,
)

from qctrlcommons.node.registry import NODE_REGISTRY
from qctrlcommons.node.wrapper import LOCAL_THREADING

LOGGER = logging.getLogger(__name__)


class Graph:
    """
    Dataflow graph can extending custom node
    """

    def __init__(
        self, operations: Dict[str, str] = None, dependencies: List = None, name=None
    ):
        self.name = name or id(self)
        self.operations = operations or {}
        self.dependencies = dependencies or []

    def __enter__(self):
        assert (
            getattr(LOCAL_THREADING, "default_graph", None) is None
        ), "cannot have more than one default graph"
        LOCAL_THREADING.default_graph = self
        return self

    def __exit__(self, *args):
        assert LOCAL_THREADING.default_graph is self
        LOCAL_THREADING.default_graph = None

    @classmethod
    def _extend_function(cls, func: Callable):
        """Extends the namespace class by adding functions as attributes. The
        function will be added as a staticmethod.

        Parameters
        ----------
        func : Callable
            function to be added to the namespace.

        Returns
        -------
        """
        func_name = func.__name__
        if hasattr(cls, func_name):
            LOGGER.debug("existing attr %s on namespace: %s", func_name, cls)
        else:
            LOGGER.debug("adding attr %s to namespace: %s", func_name, cls)
            setattr(cls, func_name, staticmethod(func))

    def __str__(self):
        return f"Q-CTRL Graph {self.name}"


# set nodes to Graph
for node_cls in NODE_REGISTRY.as_list():
    node = node_cls.create_pf()
    Graph._extend_function(node)  # pylint:disable=protected-access
