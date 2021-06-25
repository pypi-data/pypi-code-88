from typing import Optional

from .code_version_artifact import CodeVersionArtifact
from .dataset_version_artifact import DatasetVersionArtifact
from .model_version_artifact import ModelVersionArtifact


class Artifacts:
    """
    factory class for Artifacts.
    """

    @classmethod
    def create_dataset_version(
        cls,
        description: Optional[str] = None,
    ) -> DatasetVersionArtifact:
        """create an artifact for a dataset"""
        return DatasetVersionArtifact.create(description)

    @classmethod
    def create_model_version(
        cls,
        description: Optional[str] = None,
    ) -> ModelVersionArtifact:
        """create an artifact for a model"""
        return ModelVersionArtifact.create(description)

    @classmethod
    def create_code_version(cls, path: str = ".") -> Optional[CodeVersionArtifact]:
        """create an artifact for the code"""
        return CodeVersionArtifact.create(path)
