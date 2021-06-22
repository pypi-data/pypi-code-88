"""Module for annealing"""

from dataclasses import dataclass
from typing import Any, Dict, List


@dataclass
class AnnealingResult:
    """Result for annealing."""
    solutions: List[List[int]]
    solutionCounts: List[int]
    values: List[float]
    variableCount: int
    taskMetadata: Dict[str, Any]
    additionalMetadata: Dict[str, Any]


class AnnealingTask:
    """Annealing task."""
    def __init__(self, api, **kwargs) -> None:
        self.api = api
        self.data = kwargs

    def detail(self) -> AnnealingResult:
        """This method may be changed."""
        path = "v1/quantum-tasks/get"
        body = {
            "id": self.data['id'],
        }
        return AnnealingResult(**self.api.post_request(path, body))
