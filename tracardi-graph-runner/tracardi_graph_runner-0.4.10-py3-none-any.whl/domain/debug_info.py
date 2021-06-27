from typing import List
from pydantic import BaseModel
from tracardi_graph_runner.domain.debug_call_info import DebugCallInfo
from tracardi_graph_runner.domain.entity import Entity
from tracardi_graph_runner.domain.flow_debug_info import FlowDebugInfo


class DebugInfo(BaseModel):
    timestamp: float
    event: Entity
    flow: FlowDebugInfo
    calls: List[DebugCallInfo] = []
