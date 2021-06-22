"""
Module providing helpers to manipulate jobs
"""

import asyncio
from dataclasses import dataclass
import logging
import os
import shutil
from typing import Any, Dict

import quixote

from .cache import Cache
from .errors import *

from .backends import Backend

from .internals.blueprint import augmented_syspath, scoped_module_imports, BlueprintLoader
from .internals.build import DockerScriptGenerator
from .internals.workspace import BaseJobWorkspaceHandle, WorkspaceLayout
from .internals.pipe_stream import AsyncPipeStream

_LOGGER = logging.getLogger(__name__)

# Add a NullHandler to prevent logging to sys.stderr if logging is not configured by the application
_LOGGER.addHandler(logging.NullHandler())


class AsyncExecutableJobHandle(BaseJobWorkspaceHandle):
    """
    Class representing a job that is ready to be executed
    """

    def __init__(
            self,
            backend: Backend,
            workspace: WorkspaceLayout,
            blueprint: quixote.Blueprint,
    ):
        super().__init__(workspace=workspace, blueprint=blueprint)
        self.backend = backend

    async def execute_job(self, context: Dict[str, Any], environment_tag: str, timeout: float = None) -> Dict[str, Any]:
        """
        Execute the job and collect its result (async equivalent of execute_job)

        :param context:         the context to use when calling the inspection steps
        :param environment_tag: a tag identifying the environment that must be used to run the job
        :param timeout:         the timeout

        :raise                  panza.errors.JobExecutionError
        """

        _LOGGER.info("Running inspections in the job's environment...")
        try:
            result = await self.backend.run(context, environment_tag, self, timeout)
        except asyncio.TimeoutError:
            raise JobExecutionTimeout(timeout)
        except Exception as e:
            _LOGGER.error(f"Error raised by the backend: {e}")
            raise

        if "error" in result:
            raise InspectionError(result["error"]["message"])
        return result["success"]


class AsyncDataAwaitingJobHandle:
    """
    Class representing a job whose environment is already built, and needs to fetch data to operate on
    """

    def __init__(
            self,
            backend: Backend,
            workspace: WorkspaceLayout,
            blueprint: quixote.Blueprint,
    ):
        self.backend = backend
        self.workspace = workspace
        self.blueprint = blueprint

    def _fetch_data(self, fetcher):
        try:
            fetcher()
        except Exception as e:
            raise DataFetchingError(e)

    async def fetch_to(self, context: Dict[str, Any], path: str):
        with augmented_syspath([self.workspace.root]):
            with quixote.new_context(
                    **context,
                    delivery_path=path,
                    resources_path=self.workspace.resources_directory
            ):
                for fetcher in self.blueprint.fetchers:
                    await asyncio.get_running_loop().run_in_executor(
                        None,
                        lambda: self._fetch_data(fetcher)
                    )

    async def fetch_data(
            self,
            context: Dict[str, Any],
            *,
            cache: Cache = None,
            cache_entry: str = None,
    ) -> AsyncExecutableJobHandle:
        """
        Fetch the data on which this job will operate
        The fetcher functions specified in the blueprint will be used

        :param context:         the context to use when calling the fetch steps
        :param cache:           the cache to use to store fetched data (can be omitted to disable caching)
        :param cache_entry:     the name of the cache entry to use (must be set if and only if cache is set)

        :raise                  panza.errors.DataFetchingError
        """

        job_name = os.path.basename(self.workspace.root)
        _LOGGER.info(f"Fetching data for job {job_name}")
        wants_cache = cache is not None and all(f.cached for f in self.blueprint.fetchers)
        if not wants_cache:
            await self.fetch_to(context, self.workspace.delivery_directory)
        else:
            if cache_entry is None:
                raise TypeError(f"'cache_entry' must be provided")

            if not cache.has_entry(cache_entry):
                with cache.add_entry(cache_entry) as path:
                    _LOGGER.debug(f"No cache entry found, fetching data to '{path}'")
                    await self.fetch_to(context, path)
            else:
                path = cache.get_entry(cache_entry)
                _LOGGER.debug(f"Reusing cached data from directory '{path}'")
            shutil.copytree(path, self.workspace.delivery_directory)
        return AsyncExecutableJobHandle(self.backend, self.workspace, self.blueprint)


class AsyncJobWorkspaceHandle(BaseJobWorkspaceHandle):
    """
    Class representing a job workspace, that is, a job with its working directory and its resources
    """

    def __init__(self, backend: Backend, workspace: WorkspaceLayout, blueprint: quixote.Blueprint):
        super().__init__(workspace=workspace, blueprint=blueprint)
        self.backend = backend

    def __enter__(self):
        return self

    def cleanup(self):
        """
        Cleanup the job's working directory
        """
        _LOGGER.info(f"Cleaning up workspace...")
        shutil.rmtree(self.workspace.root)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cleanup()

    async def build_job_environment(self, env_name: str) -> AsyncDataAwaitingJobHandle:
        """
        Build the environment specified by the blueprint for this job (async equivalent of build_job_environment).
        The builder functions specified in the blueprint will be used to build a suitable Docker image.

        :param env_name:        the name to give to the resulting environment

        :raise                  panza.errors.EnvironmentBuildError
        """

        _LOGGER.info(f"Building environment {env_name}...")

        try:
            await self.backend.build_environment(env_name, self)
        except Exception as e:
            _LOGGER.error(f"unable to build environment {env_name}: {str(e)}")
            raise EnvironmentBuildError(e)

        return AsyncDataAwaitingJobHandle(self.backend, self.workspace, self.blueprint)


def new_async_job_workspace(backend: Backend, with_files: str, with_root: str) -> AsyncJobWorkspaceHandle:
    """
    Create a workspace in which the job can be executed.
    This will create a directory, copy the required files, and load the blueprint

    :param backend:             the job backend to use for this job
    :param with_files:          the path to the directory containing the job's resources files
    :param with_root:           the path to use as workspace root for the job

    :raise                      panza.errors.WorkspaceCreationError
    """

    workspace_layout = WorkspaceLayout(root=os.path.normpath(with_root))
    _LOGGER.info(f"Creating workspace {workspace_layout.root}...")

    try:
        shutil.copytree(with_files, workspace_layout.moulinette_directory)
    except OSError as e:
        raise WorkspaceCreationError(e)

    _LOGGER.info(f"Loading blueprint from {workspace_layout.moulinette_directory}...")

    try:
        with augmented_syspath([workspace_layout.moulinette_directory]):
            with scoped_module_imports():
                blueprint = BlueprintLoader.load_from_directory(workspace_layout.moulinette_directory)
    except BlueprintLoadError as e:
        shutil.rmtree(workspace_layout.root)
        raise WorkspaceCreationError(e)

    return AsyncJobWorkspaceHandle(backend, workspace_layout, blueprint)


@dataclass
class ExecutableJobHandle:
    """
    Class representing a job that is ready to be executed
    """

    async_handle: AsyncExecutableJobHandle

    def __getattr__(self, item):
        return getattr(self.async_handle, item)

    def execute_job(self, context: Dict[str, Any], environment_tag: str, timeout: float = None) -> Dict[str, Any]:
        """
        Execute the job and collect its result

        :param context:         the context to use when calling the inspection steps
        :param environment_tag: a tag identifying the environment that must be used to run the job
        :param timeout:         the timeout

        :raise                  panza.errors.JobExecutionError
        """

        return asyncio.run(self.async_handle.execute_job(context, environment_tag, timeout))


@dataclass
class DataAwaitingJobHandle:
    """
    Class representing a job whose environment is already built, and needs to fetch data to operate on
    """

    async_handle: AsyncDataAwaitingJobHandle

    def __getattr__(self, item):
        return getattr(self.async_handle, item)

    def fetch_data(
            self,
            context: Dict[str, Any],
            *,
            cache: Cache = None,
            cache_entry: str = None,
    ) -> ExecutableJobHandle:
        """
        Fetch the data on which this job will operate
        The fetcher functions specified in the blueprint will be used

        :param context:         the context to use when calling the fetch steps
        :param cache:           the cache to use to store fetched data (can be omitted to disable caching)
        :param cache_entry:     the name of the cache entry to use (must be set if and only if cache is set)

        :raise                  panza.errors.DataFetchingError
        """

        async_handle = asyncio.run(self.async_handle.fetch_data(context, cache=cache, cache_entry=cache_entry))
        return ExecutableJobHandle(async_handle)


@dataclass
class JobWorkspaceHandle:
    """
    Class representing a job workspace, that is, a job with its working directory and its resources
    """

    async_handle: AsyncJobWorkspaceHandle

    def __getattr__(self, item):
        return getattr(self.async_handle, item)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.async_handle.cleanup()

    def build_job_environment(self, env_name: str) -> DataAwaitingJobHandle:
        """
        Build the environment specified by the blueprint for this job.
        The builder functions specified in the blueprint will be used to build a suitable Docker image.

        :param env_name:        the name to give to the resulting environment

        :raise                  panza.errors.EnvironmentBuildError
        """

        async_handle = asyncio.run(self.async_handle.build_job_environment(env_name))
        return DataAwaitingJobHandle(async_handle)


def new_job_workspace(backend: Backend, with_files: str, with_root: str) -> JobWorkspaceHandle:
    """
    Create a workspace in which the job can be executed.
    This will create a directory, copy the required files, and load the blueprint

    :param backend:             the job backend to use for this job
    :param with_files:          the path to the directory containing the job's resources files
    :param with_root:           the path to use as workspace root for the job

    :raise                      panza.errors.WorkspaceCreationError
    """

    async_handle = new_async_job_workspace(backend, with_files, with_root)
    return JobWorkspaceHandle(async_handle)
