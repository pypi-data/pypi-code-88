from __future__ import annotations

import logging
from typing import Optional

from .artifact import Artifact, _Base
from .artifact_type import ArtifactType
from .code_version import CodeVersion
from .git_version import GitVersion


class CodeVersionArtifact(Artifact):
    def __init__(self, code: CodeVersion, description: Optional[str] = None):
        self.artifactType = ArtifactType.CODE
        self.description = description
        self.code: CodeVersion = code

    @classmethod
    def create(
        cls,
        path: str = ".",
    ) -> Optional[CodeVersionArtifact]:
        """
        create an artifact based on the git information relative to the given path.

        :param path: the path to look for the git repository
        :return: a CodeVersion of None if a git repository was not found.
        """
        git_version = GitVersion.create(path)
        if git_version is not None:
            return cls(CodeVersion(git_version))
        else:
            logging.warning(f"path {path} is not part of a git repository")
            return None

    def _get_delegate(self) -> _Base:
        return self.code
