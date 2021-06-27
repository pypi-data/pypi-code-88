from typing import List
from tracardi_graph_runner.domain.entity import Entity
from tracardi_graph_runner.domain.error_debug_info import ErrorDebugInfo


class FlowDebugInfo(Entity):
    error: List[ErrorDebugInfo] = []
