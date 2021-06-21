import docker
import sys
import threading
import time
import queue
import socket
import ast
import subprocess
import dateutil.parser

from select import select
from slai.clients.cli import get_cli_client
from slai_cli import log
from slai_cli.exceptions import RetryException

DOCKER_SOCKET_READ_SIZE = 1024
DOCKER_INPUT_UPDATE_RATE = 0.2


def _socket_input_worker(input_queue, stop_event):
    while not stop_event.is_set():
        # TODO: this apparently will not work on windows, need to find a solution for that
        _input, _, _ = select([sys.stdin], [], [], DOCKER_INPUT_UPDATE_RATE)

        if _input:
            _line = sys.stdin.readline()
            for c in _line:
                input_queue.put(c)


def _decode_string(s):
    frame_indices = []
    idx = 0
    in_frame = False
    current_start_index = 0

    while idx < len(s):
        if not in_frame:
            if s[idx] == 0x01:
                in_frame = True
                current_start_index = idx

        elif in_frame:
            if s[idx] != 0x00:
                frame_length = idx - current_start_index

                if frame_length == 8:
                    frame_indices.append([current_start_index, idx])
                    in_frame = False

        idx = idx + 1

    s = bytearray(s)
    initial_length = len(s)
    for frame in frame_indices:
        offset = len(s) - initial_length
        del s[frame[0] + offset : frame[1] + offset]  # noqa

    return s.decode("utf-8", "ignore")


def _socket_output_worker(s, output_queue, stop_event):
    while not stop_event.is_set():
        try:
            msg = s._sock.recv(DOCKER_SOCKET_READ_SIZE)
            msg = _decode_string(msg)
            output_queue.put(msg)
        except socket.timeout:
            pass


class DockerClient:
    def __init__(self, *, project_name, project_id):
        self.project_name = project_name
        self.project_id = project_id

        self.cli_client = get_cli_client()
        self.cli_version = self.cli_client.get_cli_version()

        self.earliest_image_creation_time = dateutil.parser.isoparse(
            self.cli_version["earliest_docker_image_creation_time"]
        )

        try:
            self.client = docker.from_env()
            self.docker_api_client = docker.APIClient(
                base_url="unix://var/run/docker.sock"
            )  # TODO: support other platforms
        except docker.errors.DockerException:
            raise RuntimeError("unable_to_launch_container")

        self._connect_to_container()

    def _connect_to_container(self):
        self.project_container = None
        containers = self.client.containers.list(
            filters={"name": f"slai-{self.project_name}-{self.project_id}-workspace"}
        )

        if len(containers) == 1:
            self.project_container = containers[0]
            self.project_container_id = self.project_container.id
            self.host_port = self.project_container.ports["8888/tcp"][0]["HostPort"]

            self.image_creation_time = dateutil.parser.isoparse(
                self.project_container.image.attrs["Created"]
            )
            if self.image_creation_time < self.earliest_image_creation_time:
                log.warn(
                    "Project container is out of date, please update to the latest image with: `docker-compose pull`"  # noqa
                )
                raise RuntimeError("out_of_date_container")

        else:
            log.warn("Unable to connect to docker container, attempting to start...")
            try:
                _ = subprocess.check_call(
                    "docker-compose up -d",
                    shell=True,
                )
                self._connect_to_container()
            except subprocess.CalledProcessError:
                raise RuntimeError("unable_to_launch_container")

    def _start_socket_io_worker(self, worker_function, args=()):
        _thread = threading.Thread(target=worker_function, args=args)
        _thread.daemon = True
        _thread.start()

    def create_model_environment(self, *, model_name):
        log.info(f"Checking if an environment exists for model: {model_name}...")

        _, output = self.project_container.exec_run(
            f"python /workspace/bin/create.py {model_name}",
        )

        if "exists" in output.decode("utf-8"):
            log.action(f"Using existing virtual environment for model: {model_name}")
        else:
            log.action(f"Created new virtual environment for model: {model_name}")

    def run_trainer(self, *, model_name, model_version):
        exit_code = self._run_interactive_command(
            cmd=f"/workspace/env/{model_name}/bin/python /workspace/models/{model_name}/{model_version['name']}/trainer.py"  # noqa
        )
        return exit_code

    def test_model(self, *, model_name, model_version):
        exit_code = self._run_interactive_command(
            cmd=f"/workspace/env/{model_name}/bin/python /workspace/bin/setup_test_environment.py {model_name} {model_version['id']}"  # noqa
        )
        if exit_code != 0:
            return exit_code

        exit_code = self._run_interactive_command(
            cmd=f"/workspace/env/{model_name}/bin/python /workspace/bin/test_model.py {model_name} {model_version['id']} {model_version['name']}"  # noqa
        )

        return exit_code

    def install_requirement(self, *, model_name, requirement):
        exit_code = self._run_interactive_command(
            cmd=f"/workspace/env/{model_name}/bin/python -m pip install {requirement}"
        )
        return exit_code

    def check_model_requirements(self, *, model_name, requirements):
        log.action("Verifying artifact requirements...")

        req_string = " ".join(
            [f"{req}{version}" for req, version in requirements.items()]
        )
        exit_code = self._run_interactive_command(
            cmd=f"/workspace/env/{model_name}/bin/python -m pip install {req_string}"
        )
        return exit_code

    def check_trainer_imports(self, *, model_name, model_version):
        trainer_path = (
            f"/workspace/models/{model_name}/{model_version['name']}/trainer.py"
        )

        exit_code = self._run_interactive_command(
            cmd=f"/workspace/env/{model_name}/bin/python /workspace/bin/check_imports.py {trainer_path}"  # noqa
        )
        return exit_code

    def generate_model_handler_requirements(self, *, model_name, model_version):
        _, output = self.project_container.exec_run(
            f"/workspace/env/{model_name}/bin/python /workspace/bin/generate_handler_requirements.py {model_name} {model_version['name']}",  # noqa
        )
        model_handler_requirements = ast.literal_eval(output.decode("utf-8"))
        return model_handler_requirements

    def check_handler_imports(self, *, model_name, model_version):
        handler_path = (
            f"/workspace/handlers/{model_name}/{model_version['name']}/handler.py"
        )
        exit_code = self._run_interactive_command(
            cmd=f"/workspace/env/{model_name}/bin/python /workspace/bin/check_imports.py {handler_path}"  # noqa
        )
        return exit_code

    def launch_local_notebook_server(self, *, model_name):
        _, output = self.project_container.exec_run(
            "fuser -k 8888/tcp"
        )  # kill any running notebook servers

        killed_process = output.decode("utf-8").strip()
        if killed_process:
            log.action(f"Stopped existing notebook server: {killed_process}")

        try:
            _, output = self.project_container.exec_run(
                f"/workspace/env/{model_name}/bin/python -m jupyter notebook --allow-root --ip='0.0.0.0' --NotebookApp.token='' --NotebookApp.password='' --no-browser",  # noqa
                detach=True,
            )
        except docker.errors.APIError as e:
            if "python: no such file" in e.response.json()["message"]:
                log.warn(
                    "No virtual environment found for this model, checking environment..."
                )
                self.create_model_environment(model_name=model_name)
                raise RetryException
            else:
                return False

        return True

    def _run_interactive_command(self, *, cmd, silent=False):
        input_queue = queue.Queue()
        output_queue = queue.Queue()
        stop_event = threading.Event()

        exec_id = self.docker_api_client.exec_create(
            self.project_container_id,
            cmd,
            tty=True,
            stdin=True,
        )

        s = self.docker_api_client.exec_start(exec_id, socket=True)
        self._start_socket_io_worker(
            _socket_input_worker, args=(input_queue, stop_event)
        )
        self._start_socket_io_worker(
            _socket_output_worker, args=(s, output_queue, stop_event)
        )

        last_update = time.time()
        to_send = None

        process_info = self.docker_api_client.exec_inspect(exec_id)
        process_running = process_info["Running"]

        while process_running:
            if time.time() - last_update > DOCKER_INPUT_UPDATE_RATE:
                sys.stdout.flush()
                last_update = time.time()

            if not input_queue.empty():
                to_send = input_queue.get()
                s._sock.send(to_send.encode("utf-8"))
                to_send = None

            if not output_queue.empty():
                resp = output_queue.get()
                if not silent:
                    sys.stdout.write(resp)
                    sys.stdout.flush()

            process_info = self.docker_api_client.exec_inspect(exec_id)
            process_running = process_info["Running"]

        stop_event.set()
        s.close()

        if not silent:
            sys.stdout.write("\n")
            sys.stdout.flush()

        return process_info["ExitCode"]
