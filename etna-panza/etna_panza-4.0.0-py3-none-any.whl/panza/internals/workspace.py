"""
Module providing constants and utilities related to job workspaces
"""

from dataclasses import dataclass
from functools import cached_property

from quixote import Blueprint

EXECUTOR_WORKSPACE_ROOT = "/panza"


class WorkspaceLayout:
    """
    Class providing helpers to retrieve paths to the different resources found in a workspace
    """

    _WORK_DIRECTORY: str = "workdir"
    _MOULINETTE_DIRECTORY: str = "moulinette"
    _RESOURCES_DIRECTORY: str = f"{_MOULINETTE_DIRECTORY}/resources"
    _DELIVERY_DIRECTORY: str = "rendu"
    _CONTEXT_FILE: str = f"{_WORK_DIRECTORY}/context.json"
    _RESULT_FILE: str = f"{_WORK_DIRECTORY}/result.json"

    def __init__(self, root: str):
        self.root = root

    @cached_property
    def work_directory(self) -> str:
        return f"{self.root}/{self._WORK_DIRECTORY}"

    @cached_property
    def moulinette_directory(self) -> str:
        return f"{self.root}/{self._MOULINETTE_DIRECTORY}"

    @cached_property
    def resources_directory(self) -> str:
        return f"{self.root}/{self._RESOURCES_DIRECTORY}"

    @cached_property
    def delivery_directory(self) -> str:
        return f"{self.root}/{self._DELIVERY_DIRECTORY}"

    @cached_property
    def context_file(self) -> str:
        return f"{self.root}/{self._CONTEXT_FILE}"

    @cached_property
    def result_file(self) -> str:
        return f"{self.root}/{self._RESULT_FILE}"


@dataclass
class BaseJobWorkspaceHandle:
    workspace: WorkspaceLayout
    blueprint: Blueprint
