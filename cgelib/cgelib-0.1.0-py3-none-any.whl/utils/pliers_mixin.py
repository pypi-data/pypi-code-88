#!/usr/bin/env python3

from git import Repo
from git.exc import InvalidGitRepositoryError


class PliersMixin():

    @staticmethod
    def get_version_commit(gitdir):
        """
            Input: Path to git directory
            Return: (version, commmit_hash)

            commmit_hash: The 40 character hash describing the exact commit of
            the git directory.
            version: The tag of the current commit. If no tag exists the first
            7 characters of the commit hash will be returned instead.

            If the given directory is not a git directory the returned values
            will be 'unknown'.
        """
        try:
            repo = Repo(gitdir)
        except InvalidGitRepositoryError:
            return ("unknown", "unknown")

        com2tag = {}
        for tag in repo.tags:
            com2tag[tag.commit.hexsha] = str(tag)

        version = com2tag.get(repo.commit().hexsha, repo.commit().hexsha[:7])

        return (version, repo.commit().hexsha)
