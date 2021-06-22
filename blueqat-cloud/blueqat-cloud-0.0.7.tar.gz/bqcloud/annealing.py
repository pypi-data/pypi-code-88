"""Module for annealing"""

from dataclasses import dataclass
from typing import Any, Dict, List
import pandas as pd


@dataclass
class AnnealingResult:
    """Result for annealing."""
    task: Dict[str, Any]

    def table(self) -> pd.DataFrame:
        return pd.read_json(self.task['dataframe']).sort_values('energy')


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
