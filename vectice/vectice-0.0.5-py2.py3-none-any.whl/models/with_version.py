from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional, TypeVar

from .artifact_version import ArtifactVersion
from .user_declared_version import UserDeclaredVersion


class WithVersionTrait(ABC):
    T = TypeVar("T", bound="WithVersionTrait")

    @abstractmethod
    def with_user_version(
        self: T,
        user_version: str,
        name: Optional[str] = None,
        uri: Optional[str] = None,
        description: Optional[str] = None,
    ) -> T:
        pass

    @abstractmethod
    def with_existing_version_id(self: T, version_number: int) -> T:
        pass

    @abstractmethod
    def with_existing_version_name(self: T, version_name: str) -> T:
        pass


@dataclass
class WithVersion(WithVersionTrait):
    version: Optional[ArtifactVersion] = None
    """
    existing version of the artifact defined by an id or a name
    """
    userDeclaredVersion: Optional[UserDeclaredVersion] = None
    """
    new version of the artifact defined by the user.

    The version can only be declared once.
    """

    T = TypeVar("T", bound="WithVersion")

    def with_user_version(
        self: T,
        user_version: str,
        name: Optional[str] = None,
        uri: Optional[str] = None,
        description: Optional[str] = None,
    ) -> T:
        self.userDeclaredVersion = UserDeclaredVersion(user_version, name, uri, description)
        self.version = None
        return self

    def with_existing_version_id(self: T, version_number: int) -> T:
        self.userDeclaredVersion = None
        self.version = ArtifactVersion(version_number, None)
        return self

    def with_existing_version_name(self: T, version_name: str) -> T:
        self.userDeclaredVersion = None
        self.version = ArtifactVersion(None, version_name)
        return self


class WithDelegatedVersion(WithVersionTrait, ABC):
    T = TypeVar("T", bound="WithDelegatedVersion")

    @abstractmethod
    def _get_delegate(self) -> WithVersionTrait:
        pass

    def with_user_version(
        self: T,
        user_version: str,
        name: Optional[str] = None,
        uri: Optional[str] = None,
        description: Optional[str] = None,
    ) -> T:
        self._get_delegate().with_user_version(user_version, name, uri, description)
        return self

    def with_existing_version_id(self: T, version_number: int) -> T:
        self._get_delegate().with_existing_version_id(version_number)
        return self

    def with_existing_version_name(self: T, version_name: str) -> T:
        self._get_delegate().with_existing_version_name(version_name)
        return self
