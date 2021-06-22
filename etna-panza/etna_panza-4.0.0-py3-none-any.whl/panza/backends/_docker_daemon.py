import asyncio
import asyncio.subprocess as aio_subprocess
import os
import tempfile
import shutil
import time
from textwrap import dedent
from typing import List

from panza.errors import JobExecutionBackendError

from ._utils import subprocess_exec


class DockerDaemonSetupError(JobExecutionBackendError):
    """
    Exception class representing an execution error related to the setup of an additional Docker daemon
    """

    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return f"cannot setup an additional docker daemon: {self.message}"


class DockerDaemon:
    """
    Class managing a manually-started Docker daemon
    """

    def __init__(self):
        self.dockerd = None
        self.root_dir = tempfile.TemporaryDirectory(prefix="panza_").name
        self.network_brige_name = os.path.basename(self.root_dir).replace('_', '-')

    async def launch(self, *, bridge_ip: str, dns: List[str] = None):
        """
        Launch the daemon

        :param bridge_ip:           the IP mask to use for the bridge
        :param dns:                 a list of servers IP addresses to use as DNS
        """
        dns = dns or []

        script = dedent(
            f"""
            set -e

            ip link add name {self.network_brige_name} type bridge
            ip addr add {bridge_ip} dev {self.network_brige_name}
            ip link set dev {self.network_brige_name} up
            """
        )
        return_code = await subprocess_exec("bash", "-c", script)
        if return_code != 0:
            raise DockerDaemonSetupError(f"cannot configure a network bridge: exit status {return_code}")
        command = dedent(
            f"""
            dockerd \
              --bridge={self.network_brige_name} \
              --data-root={self.root_dir}/data \
              --exec-root={self.root_dir}/exec \
              --host=unix://{self.root_dir}/docker.sock \
              --pidfile={self.root_dir}/docker.pid \
              {' '.join(f"--dns {ip}" for ip in dns)}
              """
        )
        self.dockerd = await aio_subprocess.create_subprocess_exec(
            "bash", "-c", command,
            stdout=aio_subprocess.DEVNULL,
            stderr=aio_subprocess.DEVNULL
        )

    async def poll_for_readiness(self, *, timeout: float) -> bool:
        try:
            return_code = await asyncio.wait_for(
                subprocess_exec("bash", "-c", f"docker -H unix://{self.socket_path()}"),
                timeout,
            )
            return return_code == 0
        except asyncio.TimeoutError:
            return False

    READINESS_POLLING_DELAY = 0.5

    async def wait_until_started(self, *, wait_for_seconds: float):
        now = time.time()
        max_time = now + wait_for_seconds
        while now < max_time:
            if await self.poll_for_readiness(timeout=max_time - now):
                break
            await asyncio.sleep(self.READINESS_POLLING_DELAY)
            now = time.time()
        else:
            raise DockerDaemonSetupError(f"timeout after waiting {wait_for_seconds} seconds for dockerd")

    async def stop(self):
        """
        Stop the daemon and cleanup the resources
        """
        if self.dockerd is not None:
            self.dockerd.terminate()
            await self.dockerd.wait()
            shutil.rmtree(self.root_dir, ignore_errors=True)
            script = dedent(f"""\
            ip link set {self.network_brige_name} down
            ip link delete {self.network_brige_name}
            """)
            await subprocess_exec("bash", "-c", script)

    def socket_path(self) -> str:
        """
        Get the path to the Docker socket

        :return:                    the path to the Docker socket
        """
        return f"{self.root_dir}/docker.sock"
