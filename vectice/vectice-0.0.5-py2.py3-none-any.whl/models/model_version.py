from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from .artifact import _Base
from .with_metrics import WithMetrics
from .with_properties import WithProperties
from .with_version import WithVersion


@dataclass
class ModelVersion(_Base, WithVersion, WithProperties, WithMetrics):
    algorithmName: Optional[str] = None

    def with_algorithm(self, name: Optional[str]):
        self.algorithmName = name
