from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional, List, TypeVar, Tuple, Generic

from .with_parent import WithParent
from .with_tags import WithTags


class _Base(WithTags, WithParent):
    pass


V = TypeVar("V", bound="_Base")


class Artifact(ABC, Generic[V]):
    """
    Base class for all type of artifact
    """

    artifactType: str
    jobArtifactType: Optional[str] = None
    description: Optional[str] = None

    T = TypeVar("T", bound="Artifact")

    @abstractmethod
    def _get_delegate(self) -> V:
        pass

    def __str__(self):
        return f"{self.__class__.__name__}({self.jobArtifactType},{str(self._get_delegate())})"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.jobArtifactType},{str(self._get_delegate())})"

    def with_tag(self: T, key: str, value: str) -> T:
        """
        add a tag to the artifact
        :param key:
        :param value:
        :return:
        """
        self._get_delegate().with_tag(key, value)
        return self

    def with_tags(self: T, tags: List[Tuple[str, str]]) -> T:
        """
        add several tags to the artifact
        :param tags:
        :return:
        """
        self._get_delegate().with_tags(tags)
        return self

    def with_parent_id(self: T, parent_id: int) -> T:
        """
        linked the artifact to the parent.
        for a model_version, it is the id of the model
        for a dataset_version, it is the id of the dataset
        for a code_version, it is the id of the repository

        :param parent_id:
        :return:
        """
        self._get_delegate().with_parent_id(parent_id)
        return self

    def with_parent_name(self: T, parent_name: str) -> T:
        """
        linked the artifact to the parent.
        for a model_version, it is the name of the model
        for a dataset_version, it is the name of the dataset
        for a code_version, it is the name of the repository

        :param parent_name:
        :return:
        """
        self._get_delegate().with_parent_name(parent_name)
        return self
