from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from git import Repo, InvalidGitRepositoryError


def _is_git_repo(path: str = ".", search_parent_directories: bool = True) -> bool:
    try:
        Repo(path, search_parent_directories=search_parent_directories)
        return True
    except InvalidGitRepositoryError:
        return False


def _extract_git_version(path: str = ".", search_parent_directories: bool = True) -> Optional[GitVersion]:
    try:
        repo = Repo(path, search_parent_directories=search_parent_directories)
        repository_name = repo.remotes.origin.url.split(".git")[0].split("/")[-1]
        branch_name = repo.active_branch.name
        commit_hash = repo.head.object.hexsha
        commit_comment = repo.head.object.message
        commit_author_name = repo.head.object.author.name
        commit_author_email = repo.head.object.author.email
        is_dirty = repo.is_dirty()
        uri = repo.remotes.origin.url
        return GitVersion(
            repository_name,
            branch_name,
            commit_hash,
            commit_comment,
            commit_author_name,
            commit_author_email,
            is_dirty,
            uri,
        )
    except InvalidGitRepositoryError:
        return None


@dataclass
class GitVersion:
    repositoryName: str
    branchName: str
    commitHash: str
    commitComment: str
    commitAuthorName: str
    commitAuthorEmail: str
    isDirty: bool
    uri: str

    @classmethod
    def create(cls, path: str, search_parent_directories: bool = True) -> Optional[GitVersion]:
        return _extract_git_version(path, search_parent_directories)
