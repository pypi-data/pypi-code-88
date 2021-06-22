import asyncio
import asyncio.subprocess as aio_subprocess
from dataclasses import dataclass, field
import json
import logging
import os
from typing import Union, Dict, Any, Optional, Mapping, List, Tuple

from panza import metadata
from panza.errors import InspectionError, JobExecutionTimeout

from panza.internals.workspace import BaseJobWorkspaceHandle, EXECUTOR_WORKSPACE_ROOT
from panza.internals.pipe_stream import AsyncPipeStream
from panza.internals.result_serialization import load_result

from . import Backend
from ._utils import check_subprocess_exec, subprocess_exec, generate_unique_name

from ._docker_builder import _DockerImageBuilderBackend
from ._docker_daemon import DockerDaemon


@dataclass
class DockerConfiguration:
    base_image: str = f"etnajawa/panza-base:{metadata.__version__}"
    always_pull: bool = False


@dataclass
class DockerWithAdditionalDaemonConfiguration:
    network_bridge_mask: str
    base_image: str = f"etnajawa/panza-base:{metadata.__version__}"
    always_pull: bool = False
    max_wait_time: float = 10.0
    dns: List[str] = field(default_factory=list)


class _DockerContainerBackend:
    config: Union[DockerConfiguration, DockerWithAdditionalDaemonConfiguration]
    logger: logging.Logger

    def _configure_job_directory(self, context: Mapping[str, Any], workspace):
        os.mkdir(workspace.work_directory)

        with open(workspace.context_file, 'w') as context_file:
            json.dump(context, context_file)

    async def _destroy_container(self, container_name: str):
        await subprocess_exec("docker", "kill", container_name)
        await subprocess_exec("docker", "rm", container_name)

    async def _run(
            self,
            context: Mapping[str, Any],
            environment_tag: str,
            job: BaseJobWorkspaceHandle,
            timeout: Optional[float],
            extra_volumes: List[Tuple[str, str]] = None,
    ) -> Dict[str, Any]:
        self._configure_job_directory(context, job.workspace)

        volumes = [(job.workspace.root, EXECUTOR_WORKSPACE_ROOT)]
        if extra_volumes is not None:
            volumes.extend(extra_volumes)
        volumes_args = map(lambda vol: f"-v{vol[0]}:{vol[1]}", volumes)

        container_name = generate_unique_name()

        try:
            async with check_subprocess_exec(
                    "docker", "run", "--name", container_name, *volumes_args, environment_tag, "panza_executor.py",
                    stderr=aio_subprocess.STDOUT,
                    stdout=aio_subprocess.PIPE,
            ) as proc:
                self.logger.debug("Inspection output:")
                try:
                    async for line in AsyncPipeStream(proc.stdout).iter_lines(with_timeout=timeout):
                        self.logger.debug("  " + line.rstrip())
                except asyncio.TimeoutError:
                    proc.kill()
                    raise JobExecutionTimeout(timeout)

            if proc.returncode != 0:
                raise InspectionError(f"inspector process exited with error status {proc.returncode}")

        finally:
            await self._destroy_container(container_name)

        return load_result(job.workspace.result_file)


class DockerBackend(_DockerImageBuilderBackend, _DockerContainerBackend, Backend):
    def __init__(self, config: DockerConfiguration):
        self.config: DockerConfiguration = config
        self.logger = logging.getLogger("panza.docker")

    async def build_environment(self, tag: str, job: BaseJobWorkspaceHandle):
        return await self._build_environment(tag, job)

    async def run(
            self,
            context: Mapping[str, Any],
            environment_tag: str,
            job: BaseJobWorkspaceHandle,
            timeout: Optional[float]
    ) -> Dict[str, Any]:
        return await self._run(context, environment_tag, job, timeout)


class DockerWithAdditionalDaemonBackend(_DockerImageBuilderBackend, _DockerContainerBackend, Backend):
    def __init__(self, config: DockerWithAdditionalDaemonConfiguration):
        self.config: DockerWithAdditionalDaemonConfiguration = config
        self.logger = logging.getLogger("panza.docker")

    async def build_environment(self, tag: str, job: BaseJobWorkspaceHandle):
        return await self._build_environment(tag, job)

    async def _launch_additional_docker_daemon(self):
        dockerd = DockerDaemon()
        self.logger.info("Starting docker daemon...")
        await dockerd.launch(
            bridge_ip=self.config.network_bridge_mask,
            dns=self.config.dns,
        )
        return dockerd

    async def run(
            self,
            context: Mapping[str, Any],
            environment_tag: str,
            job: BaseJobWorkspaceHandle,
            timeout: Optional[float],
    ) -> Dict[str, Any]:

        dockerd = None

        try:
            if job.blueprint.allow_docker is True:
                dockerd = await self._launch_additional_docker_daemon()

                self.logger.debug("Waiting for Docker Daemon to start...")
                await dockerd.wait_until_started(
                    wait_for_seconds=self.config.max_wait_time
                )

                return await self._run(
                    context,
                    environment_tag,
                    job,
                    timeout,
                    extra_volumes=[(dockerd.socket_path(), "/var/run/docker.sock")]
                )

            return await self._run(context, environment_tag, job, timeout)

        finally:
            if dockerd is not None:
                self.logger.info("Stopping docker daemon...")
                await dockerd.stop()
