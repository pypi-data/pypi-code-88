import asyncio.subprocess as aio_subprocess
import logging
import os
from typing import Protocol

from panza.internals.build import DockerScriptGenerator
from panza.internals.blueprint import augmented_syspath
from panza.internals.workspace import BaseJobWorkspaceHandle
from panza.internals.pipe_stream import AsyncPipeStream

from ._utils import check_subprocess_exec


class _DockerBuilderConfigurationProtocol(Protocol):
    base_image: str
    always_pull: bool


class _DockerImageBuilderBackend:
    config: _DockerBuilderConfigurationProtocol
    logger: logging.Logger

    async def _build_environment(self, tag: str, job: BaseJobWorkspaceHandle):
        dockerfile_path = os.path.join(job.workspace.root, "Dockerfile")
        with augmented_syspath([job.workspace.root]):
            DockerScriptGenerator(self.config.base_image).generate_to_file(
                job.blueprint,
                dockerfile_path,
                extra_context={"resources_path": job.workspace.resources_directory}
            )

        extra_build_args = []
        if self.config.always_pull is True:
            extra_build_args.append("--pull")

        try:
            async with check_subprocess_exec(
                    "docker", "build", *extra_build_args, "-t", tag, job.workspace.root,
                    stderr=aio_subprocess.STDOUT,
                    stdout=aio_subprocess.PIPE,
            ) as proc:
                self.logger.debug("Environment builder output:")
                async for line in AsyncPipeStream(proc.stdout).iter_lines():
                    self.logger.debug("  " + line.rstrip())

            if proc.returncode != 0:
                raise RuntimeError(f"builder process exited with non-zero code {proc.returncode}")
        finally:
            os.remove(dockerfile_path)
