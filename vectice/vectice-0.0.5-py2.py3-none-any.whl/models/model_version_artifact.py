from __future__ import annotations

from typing import Optional

from .artifact import Artifact
from .artifact_type import ArtifactType
from .model_version import ModelVersion
from .with_metrics import WithDelegatedMetrics
from .with_properties import WithDelegatedProperties
from .with_version import WithDelegatedVersion


class ModelVersionArtifact(Artifact[ModelVersion], WithDelegatedProperties, WithDelegatedVersion, WithDelegatedMetrics):
    def __init__(self, model: ModelVersion, description: Optional[str] = None):
        self.artifactType = ArtifactType.MODEL
        self.description = description
        self.model: ModelVersion = model

    @classmethod
    def create(
        cls,
        description: Optional[str] = None,
    ) -> ModelVersionArtifact:
        return cls(ModelVersion(), description)

    def _get_delegate(self) -> ModelVersion:
        return self.model

    def with_algorithm(self, name: Optional[str]) -> ModelVersionArtifact:
        self._get_delegate().with_algorithm(name)
        return self
