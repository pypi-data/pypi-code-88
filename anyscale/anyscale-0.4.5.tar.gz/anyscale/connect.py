"""Anyscale connect implementation.

Here's an overview of how a connect call works. It goes through a few steps:
    1. Detecting the project and comparing build_id and compute_template_id
    2. Getting or creating a cluster if necessary.
    3. Acquiring a cluster lock via the Ray client (when not in multiclients mode)

Detecting the project: If the user is in a shell, we will create a
"scratch" project by default which is the empty directory. Otherwise, the
project must either be specified explicitly, or we autodetect it based on
the current working directory.

Getting or creating a cluster: If a cluster name is passed in, anyscale
will start a cluster with that name unless the cluster is already running.
If the cluster is already running we compare the new cluster env build_id and
compute_template_id with the new cluster, if they match we connect, if they do
not match, we fail and require explicitly updating the cluster.

Acquiring a cluster lock via the Ray client: To avoid multiple clients from
connecting to the same cluster, by default we acquire an exclusive lock on
the cluster. This is done by checking that "num_clients" == 1 in the
returned connection info object, which means that we are the first client.
You can also allow multiple clients to connect to one cluster by passing
ANYSCALE_ALLOW_MULTIPLE_CLIENTS=1
"""

import copy
from datetime import datetime, timezone
import getpass
import inspect
import json
import os
import shlex
import subprocess
import sys
import time
from types import ModuleType
from typing import Any, Callable, cast, Dict, List, Optional, Tuple, Union
from urllib.parse import parse_qs, urlparse
import uuid

import colorama  # type: ignore
from packaging import version
import requests
import yaml

from anyscale.api import get_api_client
from anyscale.client.openapi_client.api.default_api import DefaultApi
from anyscale.client.openapi_client.models.app_config import AppConfig
from anyscale.client.openapi_client.models.build import Build
from anyscale.client.openapi_client.models.session import Session
from anyscale.cloud import get_cloud_id_and_name
from anyscale.controllers.session_controller import SessionController
from anyscale.credentials import load_credentials
import anyscale.project
from anyscale.sdk.anyscale_client import (
    ComputeTemplateConfig,
    ComputeTemplateQuery,
    CreateComputeTemplate,
    CreateSession,
    StartSessionOptions,
    UpdateSession,
)
from anyscale.sdk.anyscale_client.sdk import AnyscaleSDK
from anyscale.util import get_endpoint, get_wheel_url, slugify, wait_for_session_start


# The default project directory to use, if no project is specified.
DEFAULT_SCRATCH_DIR = "~/.anyscale/scratch_{}".format(getpass.getuser())

# Max number of auto created sessions.
MAX_SESSIONS = 20

# Default minutes for autosuspend.
DEFAULT_AUTOSUSPEND_TIMEOUT = 120

# The paths to exclude when syncing the working directory in runtime env.
EXCLUDE_DIRS = [".git", "__pycache__"]
EXCLUDE_PATHS = [".anyscale.yaml", "session-default.yaml"]

# The supported parameters that we can provide in the url.
# e.g url="anyscale://ameer?param1=val1&param2=val2"
CONNECT_URL_PARAMS = ["cluster_compute", "cluster_env", "autosuspend", "update"]

# The type of the dict that can be passed to create a cluster env.
# e.g., {"base_image": "anyscale/ray-ml:1.1.0-gpu"}
CLUSTER_ENV_DICT_TYPE = Dict[str, Union[str, List[str]]]

# The cluster compute type. It can either be a string, eg my_template or a dict,
# eg, {"cloud_id": "id-123" ...}
CLUSTER_COMPUTE_DICT_TYPE = Dict[str, Any]

# Commands used to build Ray from source. Note that intermediate stages will
# be cached by the app config builder.
BUILD_STEPS = [
    "git clone https://github.com/ray-project/ray.git",
    "curl -fsSL https://bazel.build/bazel-release.pub.gpg | gpg --dearmor > bazel.gpg",
    "sudo mv bazel.gpg /etc/apt/trusted.gpg.d/",
    'echo "deb [arch=amd64] https://storage.googleapis.com/bazel-apt stable jdk1.8" | sudo tee /etc/apt/sources.list.d/bazel.list',
    "sudo apt-get update && sudo apt-get install -y bazel=3.2.0",
    'cd ray/python && sudo env "PATH=$PATH" python setup.py develop',
    "pip uninstall -y ray",
]

# Minimum default Ray version to return when a user either asks for `anyscale.connect required_ray_version`
# or when a Default Cluster Env is used
# TODO(ilr/nikita) Convert this to a backend call for the most recent Ray Version in the Dataplane!
MINIMUM_RAY_VERSION = "1.4.0"


# Default docker images to use for connect sessions.
def _get_base_image(image: str, ray_version: str, cpu_or_gpu: str) -> str:
    py_version = "".join(str(x) for x in sys.version_info[0:2])
    if py_version not in ["36", "37", "38"]:
        raise ValueError("No default docker image for py{}".format(py_version))
    return "anyscale/{}:{}-py{}-{}".format(image, ray_version, py_version, cpu_or_gpu)


def _get_interactive_shell_frame(frames: Optional[List[Any]] = None) -> Optional[Any]:
    if frames is None:
        frames = inspect.getouterframes(inspect.currentframe())

    first_non_anyscale = None

    for i, frame in enumerate(frames):
        if "anyscale" not in frame.filename and "ray" not in frame.filename:
            first_non_anyscale = i
            break

    if first_non_anyscale is None:
        return None

    return frames[first_non_anyscale]


def _is_in_shell(frames: Optional[List[Any]] = None) -> bool:
    """
    Determines whether we are in a Notebook / shell.
    This is done by inspecting the first non-Anyscale related frame.
    If this is from an interactive terminal it will be either STDIN or IPython's Input.
    If connect() is being run from a file (like python myscript.py), frame.filename will equal "myscript.py".
    """
    fr = _get_interactive_shell_frame(frames)

    if fr is None:
        return False

    is_ipython = fr.filename.startswith("<ipython-input") and fr.filename.endswith(">")
    is_regular_python_shell: bool = fr.filename == "<stdin>"
    return is_regular_python_shell or is_ipython


class _ConsoleLog:
    def __init__(self) -> None:
        self.t0 = time.time()

    def zero_time(self) -> None:
        self.t0 = time.time()

    def info(self, *msg: Any) -> None:
        print(
            "{}{}(anyscale +{}){} ".format(
                colorama.Style.BRIGHT,
                colorama.Fore.CYAN,
                self._time_string(),
                colorama.Style.RESET_ALL,
            ),
            end="",
        )
        print(*msg)

    def debug(self, *msg: str) -> None:
        if os.environ.get("ANYSCALE_DEBUG") == "1":
            print(
                "{}{}(anyscale +{}){} ".format(
                    colorama.Style.DIM,
                    colorama.Fore.CYAN,
                    self._time_string(),
                    colorama.Style.RESET_ALL,
                ),
                end="",
            )
            print(*msg)

    def error(self, *msg: str) -> None:
        print(
            "{}{}(anyscale +{}){} ".format(
                colorama.Style.BRIGHT,
                colorama.Fore.RED,
                self._time_string(),
                colorama.Style.RESET_ALL,
            ),
            end="",
        )
        print(*msg)

    def warning(self, *msg: str) -> None:
        print(
            "{}{}(anyscale +{}){} ".format(
                colorama.Style.NORMAL,
                colorama.Fore.YELLOW,
                self._time_string(),
                colorama.Style.RESET_ALL,
            ),
            end="",
        )
        print(*msg)

    def _time_string(self) -> str:
        delta = time.time() - self.t0
        hours = 0
        minutes = 0
        while delta > 3600:
            hours += 1
            delta -= 3600
        while delta > 60:
            minutes += 1
            delta -= 60
        output = ""
        if hours:
            output += "{}h".format(hours)
        if minutes:
            output += "{}m".format(minutes)
        output += "{}s".format(round(delta, 1))
        return output


class ClientBuilder:
    """This class lets you set cluster options and connect to Anyscale.

    It should not be constructed directly, but instead via ray.client("anyscale://").* methods
    exported at the package level.

    Examples:
        >>> # Raw client, creates new cluster on behalf of user
        >>> ray.client("anyscale://").connect()

        >>> # Get or create a named cluster
        >>> ray
        ...   .client("anyscale://my_named_cluster")
        ...   .connect()

        >>> # Specify a previously created cluster environment
        >>> ray
        ...   .client("anyscale://<cluster-name>?cluster_compute=compute:1")
        ...   .cluster_env(prev_created_config:2")
        ...   .autosuspend(hours=2)
        ...   .connect()

        >>> # Create new cluster from local env / from scratch
        >>> ray
        ...   .client("anyscale://<cluster-name>")
        ...   .project_dir("~/dev/my-project-folder")
        ...   .connect()

        >>> # Ray client connect is setup automatically
        >>> @ray.remote
        ... def my_func(value):
        ...   return value ** 2

        >>> # Remote functions are executed in the Anyscale cluster
        >>> print(ray.get([my_func.remote(x) for x in range(5)]))
        >>> [0, 1, 4, 9, 16]
    """

    def __init__(
        self,
        address: Optional[str] = None,
        scratch_dir: str = DEFAULT_SCRATCH_DIR,
        anyscale_sdk: AnyscaleSDK = None,
        subprocess: ModuleType = subprocess,
        requests: ModuleType = requests,
        _ray: Optional[ModuleType] = None,
        log: Any = _ConsoleLog(),
        _os: ModuleType = os,
        _ignore_version_check: bool = False,
        api_client: DefaultApi = None,
    ) -> None:

        # Class dependencies.
        self._log = log
        self._anyscale_sdk: AnyscaleSDK = None
        self._credentials = None
        if anyscale_sdk:
            self._anyscale_sdk = anyscale_sdk
        else:
            self._credentials = load_credentials()
            self._log.debug("Using host {}".format(anyscale.conf.ANYSCALE_HOST))
            self._log.debug("Using credentials {}".format(self._credentials[:6]))
            self._anyscale_sdk = AnyscaleSDK(
                self._credentials, os.path.join(anyscale.conf.ANYSCALE_HOST, "ext")
            )
        if api_client is None:
            api_client = get_api_client()
        self._api_client = api_client
        if not _ray:
            try:
                import ray
            except ModuleNotFoundError:
                raise RuntimeError(
                    "Ray is not installed. Please install with: \n"
                    "pip install -U --force-reinstall `python -m anyscale.connect required_ray_version`"
                )
            _ray = ray
        self._ray: Any = _ray
        self._subprocess: Any = subprocess
        self._os: Any = _os
        self._requests: Any = requests
        self._in_shell = _is_in_shell()

        # Environment variables
        # If we are running in an anyscale session, or IGNORE_VERSION_CHECK is set,
        # skip the pinned versions
        if "IGNORE_VERSION_CHECK" in os.environ or "ANYSCALE_SESSION_ID" in os.environ:
            _ignore_version_check = True
        self._ignore_version_check = _ignore_version_check

        s3_caching = os.environ.get("ANYSCALE_ENABLE_S3_CACHING")
        if s3_caching is not None and s3_caching == "1":
            self._log.debug("Using s3 caching to start cluster.")
            from anyscale.utils.runtime_env import (
                runtime_env_setup as s3_runtime_env_setup,
            )

            s3_runtime_env_setup()
            anyscale.utils.runtime_env.logger = log

        if os.environ.get("ANYSCALE_COMPUTE_CONFIG") == "1":
            self._log.info(
                "All anyscale.connect clusters will be started with compute configs so "
                "ANYSCALE_COMPUTE_CONFIG=1 no longer needs to be specified."
            )

        # Determines whether the gRPC connection the server will be over SSL.
        self._secure: bool = os.environ.get("ANYSCALE_CONNECT_SECURE") == "1"

        # Builder args.
        self._scratch_dir: str = scratch_dir
        self._ray_release: Optional[str] = None
        self._project_dir: Optional[str] = None
        self._project_name: Optional[str] = None
        self._cloud_name: Optional[str] = None
        self._cluster_name: Optional[str] = None
        self._requirements: Optional[str] = None
        self._cluster_compute_name: Optional[str] = None
        self._cluster_compute_dict: Optional[CLUSTER_COMPUTE_DICT_TYPE] = None
        self._cluster_env_name: Optional[str] = None
        self._cluster_env_dict: Optional[CLUSTER_ENV_DICT_TYPE] = None
        self._cluster_env_revision: Optional[int] = None
        self._initial_scale: List[Dict[str, float]] = []
        self._autosuspend_timeout = DEFAULT_AUTOSUSPEND_TIMEOUT
        self._run_mode: Optional[str] = None
        self._build_commit: Optional[str] = None
        self._build_pr: Optional[int] = None
        self._force_rebuild: bool = False
        self._job_config = self._ray.job_config.JobConfig()
        self._user_runtime_env: Optional[Dict[str, Any]] = None
        # Override default run mode.
        if "ANYSCALE_BACKGROUND" in os.environ:
            self._run_mode = "background"
            self._log.debug(
                "Using `run_mode=background` since ANYSCALE_BACKGROUND is set"
            )
        elif "ANYSCALE_LOCAL_DOCKER" in os.environ:
            self._run_mode = "local_docker"
            self._log.debug(
                "Using `run_mode=local_docker` since ANYSCALE_LOCAL_DOCKER is set"
            )

        # Whether to update the cluster when connecting to a fixed cluster.
        self._needs_update: bool = True
        self._parse_address(address)

    def _parse_address(self, address: Optional[str]) -> None:
        """Parses the anyscale address and sets parameters on this builder.
        Eg, address="<cluster-name>?cluster_compute=my_template&autosuspend=5&cluster_env=bla:1&update=True
        """
        if address is None or not address:
            return
        parsed_result = urlparse(address)

        # Parse the cluster name. e.g., what is before the question mark in the url.
        cluster_name = parsed_result.path
        if cluster_name:
            self.session(cluster_name)

        # parse the parameters (what comes after the question mark)
        # parsed_result.query here looks like "param1=val1&param2=val2"
        # params_dict looks like:
        # {'cluster_compute': ['my_template'], 'autosuspend': ['5'], 'cluster_env': ['bla:1']}.
        params_dict: Dict[str, Any] = parse_qs(parsed_result.query)
        for key, val in params_dict.items():
            if key == "autosuspend":
                self.autosuspend(minutes=int(val[0]))
            elif key == "cluster_env":
                self.cluster_env(val[0])
            elif key == "cluster_compute":
                self.cluster_compute(val[0])
            elif key == "update":
                self._needs_update = val[0] == "True" or val[0] == "true"
            else:
                raise ValueError(
                    "Provided parameter in the anyscale address is "
                    f"{key}. The supported parameters are: {CONNECT_URL_PARAMS}."
                )

    def env(self, runtime_env: Dict[str, Any]) -> "ClientBuilder":
        """Sets the custom user specified runtime environment dict.

        Args:
            runtime_env (Dict[str, Any]): a python dictionary with runtime environment
                specifications.

        Examples:
            >>> ray.client("anyscale://cluster_name").env({"pip": "./requirements.txt"}).connect()
            >>> ray.client("anyscale://cluster_name")
            ...     .env({"working_dir": "/tmp/bla", "pip": ["chess"]}).connect()
            >>> ray.client("anyscale://cluster_name").env({"conda": "conda.yaml"}).connect()
        """

        if not isinstance(runtime_env, dict):
            raise TypeError("runtime_env argument type should be dict.")
        self._user_runtime_env = copy.deepcopy(runtime_env)
        return self

    def namespace(self, namespace: str) -> "ClientBuilder":
        """Sets the namespace in the job config of the started job.

        Args:
            namespace (str): the name of to give to this namespace.

        Example:
            >> ray.client("anyscale://cluster_name").namespace("training_namespace").connect()
        """
        self._job_config.set_ray_namespace(namespace)
        return self

    def job_name(self, job_name: Optional[str] = None) -> "ClientBuilder":
        """Sets the job_name so the user can identify it in the UI.
        This name is only used for display purposes in the UI.

        Args:
            job_name (str): the name of this job, which will be shown in the UI.

        Example:
            >>> ray.client("anyscale://cluster_name").job_name("production_job").connect()
        """
        current_time_str = datetime.now(timezone.utc).strftime("%m-%d-%Y_%H:%M:%S")
        job_name = job_name if job_name else f"Job_{current_time_str}"
        self._job_config.set_metadata("job_name", job_name)
        return self

    def _set_runtime_env_in_job_config(self, project_dir: str) -> None:
        """Configures the runtime env inside self._job_config."""

        runtime_env = copy.deepcopy(self._user_runtime_env) or {}
        if "working_dir" not in runtime_env:
            runtime_env["working_dir"] = project_dir
        if "excludes" not in runtime_env:
            runtime_env["excludes"] = []
        runtime_env["excludes"] = EXCLUDE_DIRS + [
            os.path.join(project_dir, path)
            for path in (runtime_env["excludes"] + EXCLUDE_PATHS)
        ]
        self._job_config.set_runtime_env(runtime_env)

    def _set_metadata_in_job_config(self, project_id: str) -> None:
        """
        Specify creator_id in job config. This is needed so the job
        can correctly be created in the database. Specify default job name
        if not user provided. This will be displayed in the UI.
        """
        # TODO(nikita): A customer can spoof this value and pretend to be someone else.
        # Fix this once we have a plan for verification.
        user = self._api_client.get_user_info_api_v2_userinfo_get().result
        self._job_config.set_metadata("creator_id", user.id)
        if "job_name" not in self._job_config.metadata:
            self.job_name()

    def _build_cluster_env_if_needed(self, project_id: str):
        """Builds a new cluster env on the fly if a cluster env dict is provided by the user
        or if the user wants to build ray from source."""
        if self._build_pr or self._build_commit:
            self._cluster_env_name = self._build_app_config_from_source(project_id)

        if self._cluster_env_dict:
            self._log.info("building new docker image for the provided cluster env ...")
            # Replacing ":" with "-" because the cluster env name cannot include ":"
            self._cluster_env_name = (
                self._cluster_env_name
                or "anonymous_cluster_env-{}".format(
                    datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                )
            )
            self._anyscale_sdk.create_app_config(
                {
                    "name": self._cluster_env_name,
                    "project_id": project_id,
                    "config_json": self._cluster_env_dict,
                }
            )

    def _get_cloud_id(self, project_id: str) -> str:
        """Returns the cloud id from cloud name.
        If cloud name is not provided, returns the default cloud name if exists in organization.
        If default cloud name does not exist returns last used cloud.
        """
        if self._cloud_name is None:
            default_cloud_name = self._get_organization_default_cloud()
            if default_cloud_name:
                self._cloud_name = default_cloud_name
            else:
                self._cloud_name = self._get_last_used_cloud(project_id)
        cloud_id, _ = get_cloud_id_and_name(
            self._api_client, cloud_name=self._cloud_name
        )
        return cloud_id

    def _cluster_needs_up(self, project_id: str) -> bool:
        """Returns True if the cluster needs to be started/update or else returns False.

        Returns False only when the cluster is currently running and the user did not
        explicitly pass an update request (`.cluster_env(..., update=True)`).
        """

        if self._cluster_name:
            sess = self._get_session(project_id, self._cluster_name)
            if not sess or sess.state != "Running":
                # Unconditionally create the cluster if it isn't up.
                needs_up = True
            else:
                needs_up = self._needs_update

        else:
            needs_up = True

        return needs_up

    def _is_equal_cluster_compute(
        self, cluster_compute_1_id: str, cluster_compute_2_id: str,
    ) -> bool:
        """
        Compares config fields of two ComputeTemplate objects.
        """
        try:
            cluster_compute_1 = self._anyscale_sdk.get_compute_template(
                cluster_compute_1_id
            ).result.config
            cluster_compute_2 = self._anyscale_sdk.get_compute_template(
                cluster_compute_2_id
            ).result.config
            return bool(cluster_compute_1 == cluster_compute_2)
        except Exception as e:
            self._log.debug(f"Error comparing cluster compute: {e}")
            return False

    def _get_default_cluster_env_build(self) -> Build:
        py_version = "".join(str(x) for x in sys.version_info[0:2])
        if py_version not in ["36", "37", "38"]:
            raise ValueError("No default cluster env for py{}".format(py_version))
        ray_version = self._ray.__version__
        if version.parse(ray_version) < version.parse(MINIMUM_RAY_VERSION):
            raise ValueError(
                f"No default cluster env for ray version {ray_version}. Please upgrade "
                f"to a version >= {MINIMUM_RAY_VERSION}."
            )
        try:
            build = self._api_client.get_default_cluster_env_build_api_v2_builds_default_py_version_ray_version_get(
                f"py{py_version}", ray_version
            ).result
            return build
        except Exception as e:
            raise RuntimeError(
                f"Failed to get default cluster env build with error: {e}"
            )

    def _get_cluster_build_and_compute_ids(self, project_id: str) -> Tuple[Build, str]:
        """Returns the build id and compute template ids of the cluster to be created.

        By default we return the default cluster compute and env. Unless the user overrides.
        """
        # get cluster env build id
        if self._cluster_env_name:
            build = self._get_cluster_env_build(
                project_id, self._cluster_env_name, self._cluster_env_revision
            )
        else:
            build = self._get_default_cluster_env_build()

        # get cluster compute template
        if self._cluster_compute_name:
            compute_template_id = self._get_cluster_compute_id_from_name(
                project_id, self._cluster_compute_name
            )
        else:
            # If the user specifies _cluster_compute_dict use it, otherwise
            # use the default cluster compute template.
            if self._cluster_compute_dict:
                cluster_compute_class = ComputeTemplateConfig(
                    **self._cluster_compute_dict
                )
                config_object = cluster_compute_class
            else:
                cloud_id = self._get_cloud_id(project_id)
                config_object = self._anyscale_sdk.get_default_compute_config(
                    cloud_id
                ).result
            compute_template_id = self._register_compute_template(
                project_id, config_object
            )
        return build, compute_template_id

    def _validate_new_cluster_compute_and_env_match_existing_cluster(
        self, project_id: str, cluster_name: str
    ) -> None:
        cluster = self._get_session_or_die(project_id, cluster_name)
        build, compute_template_id = self._get_cluster_build_and_compute_ids(project_id)
        if self._cluster_env_name and build.id != cluster.build_id:
            current_cluster_build = self._anyscale_sdk.get_build(
                cluster.build_id
            ).result
            current_cluster_env = self._anyscale_sdk.get_app_config(
                current_cluster_build.application_template_id
            ).result
            raise ValueError(
                f"The cluster is currently using {current_cluster_env.name}:{current_cluster_build.revision} as the cluster env, "
                f"yet {self._cluster_env_name} was provided. To update the cluster, please specify "
                "`update=True` in the anyscale address, e.g.: "
                f'`ray.client("anyscale://{cluster_name}?cluster_env={self._cluster_env_name}&update=True").connect()`'
            )
        if self._cluster_compute_name and not self._is_equal_cluster_compute(
            compute_template_id, cluster.compute_template_id
        ):
            cluster_compute = self._anyscale_sdk.get_compute_template(
                cluster.compute_template_id
            ).result
            raise ValueError(
                f"The cluster is currently using {cluster_compute.name} as the cluster compute, "
                f"yet {self._cluster_compute_name} was provided. To update the cluster, please specify "
                "`update=True` in the anyscale address, e.g.: "
                f'`ray.client("anyscale://{cluster_name}?cluster_compute={self._cluster_compute_name}&update=True").connect()`'
            )
        if self._cluster_env_dict or self._cluster_compute_dict:
            self._log.warning(
                f"The cluster {cluster_name} is already active. To update the cluster please "
                "specify `update=True` in the anyscale address."
            )

    def connect(self) -> None:  # noqa
        """Connect to Anyscale using previously specified options.

        Examples:
            >>> ray.client("anyscale://cluster_name").connect()

        WARNING: using a new cluster_compute/cluster_env when connecting to an
        active cluster will not work unless the user passes `update=True`. e.g.:
            >>> ray.client("anyscale://cluster_name?update=True").connect()
        """
        # TODO(ilr) Make this import from self._ray
        from ray.autoscaler import sdk as ray_autoscaler_sdk

        # TODO(ekl) check for duplicate connections
        self._log.zero_time()

        if self._ray.util.client.ray.is_connected():
            raise RuntimeError(
                "Already connected to a Ray cluster, please "
                "run anyscale.connect in a new Python process."
            )

        # Allow the script to be run on the head node as well.
        if "ANYSCALE_SESSION_ID" in os.environ:
            self._ray.init(address="auto")
            return

        # Re-exec in the docker container.
        if self._run_mode == "local_docker":
            self._exec_self_in_local_docker()

        # Autodetect or create a scratch project.
        if self._project_dir is None:
            self._project_dir = anyscale.project.find_project_root(os.getcwd())
        if self._project_dir:
            self._ensure_project_setup_at_dir(self._project_dir, self._project_name)
        elif self._in_shell:
            self._project_dir = self._get_or_create_scratch_project()
        else:
            raise ValueError(
                "The current working directory is not associated with an "
                "Anyscale project. Please run ``anyscale init`` to setup a "
                "new project or specify ``.project_dir()`` prior to "
                "connecting. Anyscale Connect uses the project directory "
                "to find the Python code dependencies for your script."
            )

        proj_def = anyscale.project.ProjectDefinition(self._project_dir)
        project_id = anyscale.project.get_project_id(proj_def.root)
        self._set_metadata_in_job_config(project_id)
        self._log.info("Using project dir", proj_def.root)

        needs_up = self._cluster_needs_up(project_id)

        _allow_multiple_clients = (
            os.environ.get("ANYSCALE_ALLOW_MULTIPLE_CLIENTS") == "1"
        )
        if _allow_multiple_clients:
            if not self._cluster_name:
                self._log.warning(
                    "`ANYSCALE_ALLOW_MULTIPLE_CLIENTS` only works when a cluster_name is specified"
                )
            else:
                self._log.info(
                    "`ANYSCALE_ALLOW_MULTIPLE_CLIENTS` is set, multiple clients will be allowed to connect to one cluster."
                )

        # create the cluster if terminated or does not exist.
        if needs_up:
            self._build_cluster_env_if_needed(
                project_id
            )  # updates self._cluster_env_name
            build, compute_template_id = self._get_cluster_build_and_compute_ids(
                project_id
            )
            self._wait_for_app_build(project_id, build.id)
            self._cluster_name = self._create_cluster(
                project_id=project_id,
                build_id=build.id,
                compute_template_id=compute_template_id,
                cluster_name=self._cluster_name,
            )
        else:
            # `self._cluster_name` should always exist if `needs_up==False` based on the logic of
            # `_cluster_needs_up`, which returns True only when the cluster already exists.
            # Adding an assert for mypy.
            assert self._cluster_name
            self._validate_new_cluster_compute_and_env_match_existing_cluster(
                project_id, self._cluster_name
            )

        self._set_runtime_env_in_job_config(self._project_dir)
        assert self._cluster_name  # appeases mypy
        # Need to re-acquire the connection after the update.
        self._acquire_session_lock(
            self._get_session_or_die(project_id, self._cluster_name),
            raise_connection_error=True,
            connection_retries=10,
            job_config=self._job_config,
            allow_multiple_clients=_allow_multiple_clients,
        )

        # Connect Ray client.
        self._check_connection(project_id, self._cluster_name)

        # Issue request resources call.
        if self._initial_scale:
            self._log.debug("Calling request_resources({})".format(self._initial_scale))
            ray_autoscaler_sdk.request_resources(bundles=self._initial_scale)

        # Define ray in the notebook automatically for convenience.
        try:
            fr = _get_interactive_shell_frame()
            if self._in_shell and fr is not None and "ray" not in fr.frame.f_globals:
                self._log.debug("Auto importing Ray into the notebook.")
                fr.frame.f_globals["ray"] = self._ray
        except Exception as e:
            self._log.error("Failed to auto define `ray` in notebook", e)

        # If in background mode, execute the job in the remote session.
        if self._run_mode == "background":
            self._exec_self_in_head_node()

    def cloud(self, cloud_name: str) -> "ClientBuilder":
        """Set the name of the cloud to be used.

        This sets the name of the cloud that your connect cluster will be started
        in by default. This is completely ignored if you pass in a cluster compute config.

        Args:
            cloud_name (str): Name of the cloud to start the cluster in.

        Examples:
            >>> ray.client("anyscale://cluster_name").cloud("aws_test_account").connect()
        """
        self._cloud_name = cloud_name
        return self

    def project_dir(
        self, local_dir: str, name: Optional[str] = None
    ) -> "ClientBuilder":
        """Set the project directory path on the user's laptop.

        This sets the project code directory. If not specified, the project
        directory will be autodetected based on the current working directory.
        If no Anyscale project is found, a "scratch" project will be used.
        In general the project directory will be synced to all nodes in the
        cluster as required by Ray, except for when the user passes
        "working_dir" in `.env()` in which case we sync the latter instead.

        Args:
            local_dir (str): path to the project directory.
            name (str): optional name to use if the project doesn't exist.

        Examples:
            >>> ray.client("anyscale://cluster_name").project_dir("~/my-proj-dir").connect()
        """
        self._project_dir = os.path.abspath(os.path.expanduser(local_dir))
        self._project_name = name
        return self

    def session(self, cluster_name: str, update: bool = False) -> "ClientBuilder":
        """Set a fixed cluster name.

        Setting a fixed cluster name will create a new cluster if a cluster
        with cluster_name does not exist. Otherwise it will reconnect to an existing
        cluster.

        Args:
            cluster_name (str): fixed name of the cluster.
            update (bool): whether to update cluster configurations when
                connecting to an existing cluster. Note that this may restart
                the Ray runtime. By default update is set to False.

        Examples:
            >>> anyscale.session("prod_deployment", update=True).connect()
        """
        slugified_name = slugify(cluster_name)
        if slugified_name != cluster_name:
            self._log.error(
                f"Using `{slugified_name}` as the cluster name (instead of `{cluster_name}`)"
            )

        self._needs_update = update
        self._cluster_name = slugified_name

        return self

    def run_mode(self, run_mode: Optional[str] = None) -> "ClientBuilder":
        """Re-exec the driver program in the remote cluster or local docker.

        By setting ``run_mode("background")``, you can tell Anyscale
        to run the program driver remotely in the head node instead of executing
        locally. This allows you to e.g., close your laptop during development
        and have the program continue executing in the cluster.

        By setting ``run_mode("local_docker")``, you can tell Anyscale
        to re-exec the program driver in a local docker image, ensuring the
        driver environment will exactly match that of the remote cluster.

        You can also change the run mode by setting the ANYSCALE_BACKGROUND=1
        or ANYSCALE_LOCAL_DOCKER=1 environment variables. Changing the run mode
        is only supported for script execution. Attempting to change the run
        mode in a notebook or Python shell will raise an error.

        Args:
            run_mode (str): either None, "background", or "local_docker".

        Examples:
            >>> ray.client("anyscale://cluster_name").run_mode("background").connect()
        """
        if run_mode not in [None, "background", "local_docker"]:
            raise ValueError("Unknown run mode {}".format(run_mode))
        if self._in_shell:
            if run_mode == "background":
                raise ValueError("Background mode is not supported in Python shells.")
            if run_mode == "local_docker":
                raise ValueError("Local docker mode is not supported in Python shells.")
        self._run_mode = run_mode
        return self

    def base_docker_image(self, image_name: str) -> None:
        """[DEPRECATED] Set the docker image to use for the cluster.
        IMPORTANT: the Python minor version of the manually specified docker
        image must match the local Python version.
        Args:
            image_name (str): docker image name.
        Examples:
            >>> anyscale.base_docker_image("anyscale/ray-ml:latest").connect()
        """
        raise ValueError(
            "Anyscale connect doesn't support starting clusters with base docker images. "
            "Please specify a cluster_env instead. For example: "
            '`ray.client("anyscale://cluster_name?cluster_env=name:1").connect()`'
        )

    def require(self, requirements: Union[str, List[str]]) -> None:
        """[DEPRECATED] Set the Python requirements for the cluster.
        Args:
            requirements: either be a list of pip library specifications, or
            the path to a requirements.txt file.
        Examples:
            >>> anyscale.require("~/proj/requirements.txt").connect()
            >>> anyscale.require(["gym", "torch>=1.4.0"]).connect()
        """
        raise ValueError(
            "Anyscale connect no longer accepts the `.require()` argument."
            "Please specify these requirements in your runtime env instead."
            'For example `ray.client("anyscale://my_cluster").env({"pip":["chess"'
            ',"xgboost"]}).connect()`.'
        )

    def cluster_compute(
        self, cluster_compute: Union[str, CLUSTER_COMPUTE_DICT_TYPE]
    ) -> "ClientBuilder":
        """Set the Anyscale cluster compute to use for the cluster.

        Args:
            cluster_compute: Name of the cluster compute
                or a dictionary to build a new cluster compute.
                For example "my-cluster-compute".


        Examples:
            >>> ray.client("anyscale://cluster_name?cluster_compute=my_cluster_compute").connect()
            >>> ray.client("anyscale://cluster_name").cluster_compute("my_cluster_compute").connect()
            >>> ray.client("anyscale://cluster_name").cluster_compute({"cloud_id": "1234", ... }).connect()

        WARNING:
            If you want to pass a dictionary cluster_compute please pass it using
            the `.cluster_compute()` API. Passing it in the URL format will not work.
        """
        if isinstance(cluster_compute, str):
            self._cluster_compute_name = cluster_compute  # type: ignore
        elif isinstance(cluster_compute, dict):
            self._cluster_compute_dict = copy.deepcopy(cluster_compute)  # type: ignore
        else:
            raise TypeError(
                "cluster_compute should either be Dict[str, Any] or a string."
            )
        return self

    def cluster_env(
        self, cluster_env: Union[str, CLUSTER_ENV_DICT_TYPE]
    ) -> "ClientBuilder":
        """TODO(ameer): remove app_config below after a few releases.
        Set the Anyscale cluster environment to use for the cluster.

        IMPORTANT: the Python minor version of the manually specified cluster
        environment must match the local Python version, and the Ray version must
        also be compatible with the one on the client. for example, if your local
        laptop environment is using ray 1.4 and python 3.8, then the cluster environment
        ray version must be 1.4 and python version must be 3.8.

        Args:
            cluster_env: Name (and optionally revision) of
                the cluster environment or a dictionary to build a new cluster environment.
                For example "my_cluster_env:2" where the revision would be 2.
                If no revision is specified, use the latest revision.
                NOTE: if you pass a dictionary it will always rebuild a new cluster environment
                before starting the cluster.

        Examples:
            >>> ray.client("anyscale://cluster_name?cluster_env=prev_created_cluster_env:2").connect()
            >>> ray.client("anyscale://cluster_name").cluster_env("prev_created_cluster_env:2").connect()
            >>> ray.client("anyscale://cluster_name").cluster_env({"base_image": "anyscale/ray-ml:1.1.0-gpu"}).connect()

        WARNING:
            If you want to pass a dictionary cluster_compute please pass it using
            the `.cluster_compute()` API. Passing it in the URL format will not work.
        """
        self.app_config(cluster_env)
        return self

    def app_config(
        self, cluster_env: Union[str, CLUSTER_ENV_DICT_TYPE],
    ) -> "ClientBuilder":
        """Set the Anyscale app config to use for the session.

        IMPORTANT: the Python minor version of the manually specified app
        config must match the local Python version, and the Ray version must
        also be compatible with the one on the client.

        Args:
            cluster_env: Name (and optionally revision) of
            the cluster environment or a dictionary to build a new cluster environment.
            For example "my_cluster_env:2" where the revision would be 2.
            If no revision is specified, use the latest revision.

        Examples:
            >>> anyscale.app_config("prev_created_config:2").connect()
        """

        if self._build_commit or self._build_pr:
            raise ValueError("app_config() conflicts with build_from_source()")
        if isinstance(cluster_env, str):
            components = cluster_env.rsplit(":", 1)  # type: ignore
            self._cluster_env_name = components[0]
            if len(components) == 1:
                self._cluster_env_revision = None
            else:
                self._cluster_env_revision = int(components[1])
        elif isinstance(cluster_env, dict):
            cluster_env_copy: CLUSTER_ENV_DICT_TYPE = copy.deepcopy(cluster_env)  # type: ignore
            self._cluster_env_name = cluster_env_copy.pop("name", None)  # type: ignore
            self._cluster_env_dict = cluster_env_copy
        else:
            raise TypeError("The type of cluster_env must be either a str or a dict.")
        return self

    def download_results(self, *, remote_dir: str, local_dir: str) -> None:
        """Specify a directory to sync down from the cluster head node.

        IMPORTANT: the data is downloaded immediately after this call.
            `download_results` must not be called with `.connect()`. See examples below.

        Args:
            remote_dir (str): the result dir on the head node.
            local_dir (str): the local path to download the results to.

        Examples:
            >>> ray.client("anyscale://cluster_name")
            ...   .download_results(
            ...       local_dir="~/ray_results", remote_dir="/home/ray/proj_output")
            >>> ray.client("anyscale://").download_results(
            ...       local_dir="~/ray_results", remote_dir="/home/ray/proj_output")
            >>> anyscale.download_results(
            ...       local_dir="~/ray_results", remote_dir="/home/ray/proj_output")
        """
        if not self._ray.util.client.ray.is_connected():
            raise RuntimeError(
                "Not connected to cluster. Please re-run this after "
                'to a cluster via ray.client("anyscale://...").connect()'
            )

        self._download_results(remote_dir, local_dir)

    def autosuspend(
        self,
        enabled: bool = True,
        *,
        hours: Optional[int] = None,
        minutes: Optional[int] = None,
    ) -> "ClientBuilder":
        """Configure or disable cluster autosuspend behavior.

        The cluster will be autosuspend after the specified time period. By
        default, cluster auto terminate after one hour of idle.

        Args:
            enabled (bool): whether autosuspend is enabled.
            hours (int): specify idle time in hours.
            minutes (int): specify idle time in minutes. This is added to the
                idle time in hours.

        Examples:
            >>> ray.client("anyscale://cluster_name").autosuspend(False).connect()
            >>> ray.client("anyscale://cluster_name?autosuspend=10").connect()  # 10 minutes
            >>> ray.client("anyscale://cluster_name").autosuspend(hours=1, minutes=30).connect()
        """
        if enabled:
            if hours is None and minutes is None:
                timeout = DEFAULT_AUTOSUSPEND_TIMEOUT
            else:
                timeout = 0
                if hours is not None:
                    timeout += hours * 60
                if minutes is not None:
                    timeout += minutes
        else:
            timeout = -1
        self._autosuspend_timeout = timeout
        return self

    def nightly_build(self, git_commit: str) -> "ClientBuilder":
        """Use the specified nightly build commit for the cluster runtime.

        This is an experimental feature.

        Args:
            git_commit (str): git commit of the nightly Ray release.

        Examples:
            >>> anyscale
            ...   .nightly_build("f1e293c6997d1b14d61b8ca05965af42ae59d285")
            ...   .connect()
        """
        if len(git_commit) != 40:
            raise ValueError("Ray git commit hash must be 40 chars long")
        self._ray_release = "master/{}".format(git_commit)
        url = get_wheel_url(self._ray_release, "2.0.0.dev0")
        request = self._requests.head(url)
        if request.status_code != 200:
            raise ValueError(
                "Could not locate wheel in S3 (HTTP {}): {}".format(
                    request.status_code, url
                )
            )
        return self

    def build_from_source(
        self,
        *,
        git_commit: Optional[str] = None,
        github_pr_id: Optional[int] = None,
        force_rebuild: bool = False,
    ) -> "ClientBuilder":
        """Build Ray from source for the cluster runtime.

        This is an experimental feature.

        Note that the first build for a new base image might take upwards of
        half an hour. Subsequent builds will have cached compilation stages.

        Args:
            git_commit (Optional[str]): If specified, try to checkout the exact
                git commit from the Ray master branch. If pull_request_id is
                also specified, the commit may be from the PR branch as well.
            github_pr_id (Optional[int]): Specify the pull request id to use.
                If no git commit is specified, the latest commit from the pr
                will be used.
            force_rebuild (bool): Force rebuild of the app config.

        Examples:
            >>> anyscale
            ...   .build_from_source(git_commit="f1e293c", github_pr_id=12345)
            ...   .connect()
        """
        if self._cluster_env_name:
            raise ValueError("cluster_env() conflicts with build_from_source()")
        self._build_commit = git_commit
        self._build_pr = github_pr_id
        self._force_rebuild = force_rebuild
        return self

    def request_resources(
        self,
        *,
        num_cpus: Optional[int] = None,
        num_gpus: Optional[int] = None,
        bundles: Optional[List[Dict[str, float]]] = None,
    ) -> "ClientBuilder":
        """Configure the initial resources to scale to.

        The cluster will immediately attempt to scale to accomodate the
        requested resources, bypassing normal upscaling speed constraints.
        The requested resources are pinned and exempt from downscaling.

        Args:
            num_cpus (int): number of cpus to request.
            num_gpus (int): number of gpus to request.
            bundles (List[Dict[str, float]): resource bundles to
                request. Each bundle is a dict of resource_name to quantity
                that can be allocated on a single machine. Note that the
                ``num_cpus`` and ``num_gpus`` args simply desugar into
                ``[{"CPU": 1}] * num_cpus`` and ``[{"GPU": 1}] * num_gpus``
                respectively.

        Examples:
            >>> ray.client("anyscale://cluster_name").request_resources(num_cpus=200, num_gpus=30).connect()
            >>> ray.client("anyscale://cluster_name").request_resources(
            ...     num_cpus=8,
            ...     resource_bundles=[{"GPU": 8}, {"GPU": 8}, {"GPU": 1}],
            ... ).connect()
        """
        to_request: List[Dict[str, float]] = []
        if num_cpus:
            to_request += [{"CPU": 1}] * num_cpus
        if num_gpus:
            to_request += [{"GPU": 1}] * num_gpus
        if bundles:
            to_request += bundles
        self._initial_scale = to_request
        return self

    def _download_results(self, remote_dir: str, local_dir: str) -> None:
        # Determine the cluster's cluster ID by querying for the Anyscale Environment Variable
        # that is set on cluster startup. We achieve this by running a remote function against the cluster
        # using Ray Client.
        try:
            ray_id = self._ray.remote(
                lambda: os.environ.get("ANYSCALE_SESSION_ID")
            ).remote()
            session_id = self._ray.get(ray_id)
            self._session_name = self._anyscale_sdk.get_session(session_id).result.name
        except Exception as e:
            self._log.error(f"Failed to get SessionID with error: {e}")
            raise RuntimeError(
                "Unable to get SessionID for `download_results`!"
            ) from None
        session_controller = SessionController()
        session_controller.pull(self._session_name, source=remote_dir, target=local_dir)

    def _get_or_create_scratch_project(self) -> str:
        """Get or create a scratch project, including the directory."""
        project_dir = os.path.expanduser(self._scratch_dir)
        project_name = os.path.basename(self._scratch_dir)
        if not os.path.exists(project_dir) and self._find_project_id(project_name):
            self._clone_project(project_dir, project_name)
        else:
            self._ensure_project_setup_at_dir(project_dir, project_name)
        return project_dir

    def _find_project_id(self, project_name: str) -> Optional[str]:
        """Return id if a project of a given name exists."""
        resp = self._anyscale_sdk.search_projects({"name": {"equals": project_name}})
        if len(resp.results) > 0:
            return resp.results[0].id  # type: ignore
        else:
            return None

    def _clone_project(self, project_dir: str, project_name: str) -> None:
        """Clone a project into the given dir by name."""
        cur_dir = os.getcwd()
        try:
            parent_dir = os.path.dirname(project_dir)
            os.makedirs(parent_dir, exist_ok=True)
            os.chdir(parent_dir)
            self._subprocess.check_call(["anyscale", "clone", project_name])
        finally:
            os.chdir(cur_dir)

    def _ensure_project_setup_at_dir(
        self, project_dir: str, project_name: Optional[str]
    ) -> None:
        """Get or create an Anyscale project rooted at the given dir."""
        os.makedirs(project_dir, exist_ok=True)
        if project_name is None:
            project_name = os.path.basename(project_dir)

        # If the project yaml exists, assume we're already setup.
        project_yaml = os.path.join(project_dir, ".anyscale.yaml")
        if os.path.exists(project_yaml):
            return

        project_id = self._find_project_id(project_name)
        if project_id is None:
            self._log.info("Creating new project for", project_dir)
            project_response = self._anyscale_sdk.create_project(
                {
                    "name": project_name,
                    "description": "Automatically created by Anyscale Connect",
                }
            )
            project_id = project_response.result.id

        if not os.path.exists(project_yaml):
            with open(project_yaml, "w+") as f:
                f.write(yaml.dump({"project_id": project_id}))

    def _start_session(
        self,
        project_id: str,
        cluster_name: str,
        build_id: str,
        compute_template_id: str,
    ) -> None:
        """Start cluster from sdk. Create/update the cluster if required."""

        session = self._create_or_update_session_data(
            cluster_name,
            project_id,
            build_id,
            compute_template_id,
            self._autosuspend_timeout,
        )

        url = get_endpoint(f"/projects/{project_id}/sessions/{session.id}")
        self._log.info(f"Starting cluster {cluster_name}. View at {url}")

        self._anyscale_sdk.start_session(
            session.id,
            StartSessionOptions(
                build_id=build_id, compute_template_id=compute_template_id
            ),
        )

        wait_for_session_start(project_id, cluster_name, self._api_client)
        self._log.debug(f"Cluster {cluster_name} finished starting. View at {url}")

    def _create_or_update_session_data(
        self,
        cluster_name: str,
        project_id: str,
        build_id: str,
        compute_template_id: str,
        idle_timeout: Optional[int],
    ) -> Session:
        """
        Creates new cluster with cluster env if cluster with `cluster_name` doesn't
        already exist. Otherwise, update the `idle_timeout` of the existing
        cluster if provided.
        """

        session_list = self._api_client.list_sessions_api_v2_sessions_get(
            project_id=project_id, active_only=False, name=cluster_name
        ).results

        session_exists = len(session_list) > 0
        if not session_exists:
            # Create a new cluster if there is no existing cluster with the given cluster_name
            create_session_data = CreateSession(
                name=cluster_name,
                project_id=project_id,
                build_id=build_id,
                compute_template_id=compute_template_id,
                idle_timeout=idle_timeout,
                uses_app_config=True,
            )
            session = self._anyscale_sdk.create_session(create_session_data).result
        else:
            # Get the existing cluster and update the idle_timeout if required
            session = session_list[0]
            if idle_timeout:
                self._anyscale_sdk.update_session(
                    session.id, UpdateSession(idle_timeout=idle_timeout)
                )

        return session

    def _get_organization_default_cloud(self) -> Optional[str]:
        """Return default cloud name for organization if it exists and
        if user has correct permissions for it.

        Returns:
            Name of default cloud name for organization if it exists and
            if user has correct permissions for it.
        """
        user = self._api_client.get_user_info_api_v2_userinfo_get().result
        organization = user.organizations[0]  # Each user only has one org
        if organization.default_cloud_id:
            try:
                # Check permissions
                get_cloud_id_and_name(
                    self._api_client, cloud_id=organization.default_cloud_id
                )
                cloud_name = self._api_client.get_cloud_api_v2_clouds_cloud_id_get(
                    organization.default_cloud_id
                ).result.name
                return str(cloud_name)
            except Exception:
                return None
        return None

    def _get_last_used_cloud(self, project_id: str) -> str:
        """Return the name of the cloud last used in the project.

        Args:
            project_id (str): The project to get the last used cloud for.

        Returns:
            Name of the cloud last used in this project.
        """
        # TODO(pcm): Get rid of this and the below API call in the common case where
        # we can determine the cloud to use in the backend.
        cloud_id = self._anyscale_sdk.get_project(project_id).result.last_used_cloud_id

        # TODO(pcm): Replace this with an API call once the AnyscaleSDK supports it.
        p = self._subprocess.Popen(
            ["anyscale", "list", "clouds", "--json"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        out, err = p.communicate()
        if p.returncode != 0:
            msg = f"Failure listing clouds:\n{err.decode()}"
            self._log.error(msg)
            raise RuntimeError(msg)
        clouds = json.loads(out)

        if len(clouds) == 0:
            msg = "No cloud configured, please set up a cloud with 'anyscale cloud setup'."
            self._log.error(msg)
            raise RuntimeError(msg)

        if not cloud_id:
            # Clouds are sorted in descending order, pick the oldest one as default.
            cloud_id = clouds[-1]["id"]

        cloud_name = {cloud["id"]: cloud["name"] for cloud in clouds}[cloud_id]
        self._log.debug(
            (
                f"Using last active cloud '{cloud_name}'. "
                "Call anyscale.cloud('...').connect() to overwrite."
            )
        )
        return cast(str, cloud_name)

    def _create_cluster(  # noqa: C901
        self,
        project_id: str,
        build_id: str,
        compute_template_id: str,
        cluster_name: Optional[str],
    ) -> str:
        """create/start a terminated (or does not exist) cluster.

        Args:
            project_id (str): The project to use.
            build_id (str): Build to start cluster with.
            compute_template_id (str): Compute template to start cluster with
            cluster_name (Optional[str]): If specified, the given cluster
                will be created or updated as needed. Otherwise the cluster
                name will be picked automatically.

        Returns:
            The name of the cluster to connect to.
        """
        ray_cli = self._ray.util.client.ray
        results = self._list_sessions(project_id=project_id)
        if not cluster_name:
            self._log.debug("-> Starting a new cluster")
            used_names = [s.name for s in results]
            for i in range(MAX_SESSIONS):
                name = "cluster-{}".format(i)
                if name not in used_names:
                    cluster_name = name
                    self._log.debug("Starting cluster", cluster_name)
                    break

        # Should not happen.
        if cluster_name is None:
            raise RuntimeError("Could not create new cluster to connect to.")

        self._log.debug(
            f"Updating {cluster_name} to use build id {build_id} and compute template id {compute_template_id}"
        )
        # TODO(ekl): race condition here since "up" breaks the lock.
        if ray_cli.is_connected():
            self._ray.util.disconnect()
        # Update cluster.
        self._log.debug("Starting cluster with sdk and compute config.")
        self._start_session(
            project_id=project_id,
            cluster_name=cluster_name,
            build_id=build_id,
            compute_template_id=compute_template_id,
        )

        return cluster_name

    def _acquire_session_lock(
        self,
        session_meta: Session,
        raise_connection_error: bool,
        connection_retries: int,
        job_config: Optional[Any] = None,
        allow_multiple_clients: bool = False,
    ) -> None:
        """Connect to and acquire a lock on the cluster.

        The cluster lock is released by calling disconnect() on the returned
        Ray connection. This function also checks for Python version
        compatibility, it will not acquire the lock on version mismatch.

        """
        try:
            session_url, secure, metadata = self._get_connect_params(session_meta)
            if connection_retries > 0:
                self._log.debug("Beginning connection attempts")
            # Disable retries when acquiring cluster lock for fast failure.
            self._log.debug(
                "Info: ", session_url, secure, metadata, connection_retries, job_config,
            )
            if job_config is not None:
                self._log.debug("RuntimeEnv", job_config.runtime_env)
            info = self._ray.util.connect(
                session_url,
                secure=secure,
                metadata=metadata,
                connection_retries=connection_retries,
                job_config=job_config,
                ignore_version=True,
            )
            self._dynamic_check(info)
            self._log.debug("Connected server info: ", info)
        except Exception as e:
            if raise_connection_error:
                self._log.debug(
                    "Connection error after {} retries".format(connection_retries)
                )
                raise
            else:
                self._log.debug("Ignoring connection error", e)
                return
        if info["num_clients"] > 1 and (not allow_multiple_clients):
            self._log.debug(
                "Failed to acquire lock due to too many connections: ",
                info["num_clients"],
            )
            self._ray.util.disconnect()

    def _check_connection(self, project_id: str, cluster_name: str) -> None:
        """Check the connected cluster to make sure it's good"""
        if not self._ray.util.client.ray.is_connected():
            raise RuntimeError("Failed to acquire cluster we created")
        session_found = self._get_session_or_die(project_id, cluster_name)

        def func() -> str:
            return "Connected!"

        f_remote = self._ray.remote(func)
        ray_ref = f_remote.remote()
        self._log.debug(self._ray.get(ray_ref))
        self._log.info(
            "Connected to {}, see: {}".format(
                cluster_name,
                get_endpoint(f"/projects/{project_id}/clusters/{session_found.id}"),
            )
        )
        jupyter_notebook_url = session_found.jupyter_notebook_url
        if jupyter_notebook_url:
            # TODO(aguo): Replace this with host_name parameter from API
            # like "https://session-fqsx0p3pzfna71xxxxxxx.anyscaleuserdata.com"
            host_name = "https://{}".format(jupyter_notebook_url.split("/")[2].lower())
            self._log.info("URL for head node of cluster: {}".format(host_name))

    def _get_session_or_die(self, project_id: str, session_name: str) -> Session:
        """Query Anyscale for the given cluster's metadata."""
        session_found = self._get_session(project_id, session_name)
        if not session_found:
            raise RuntimeError("Failed to locate cluster: {}".format(session_name))
        return session_found

    def _get_session(self, project_id: str, session_name: str) -> Optional[Session]:
        """Query Anyscale for the given cluster's metadata."""
        results = self._list_sessions(project_id=project_id)
        session_found: Session = None
        for session in results:
            if session.name == session_name:
                session_found = session
                break
        return session_found

    def _get_connect_params(self, session_meta: Session) -> Tuple[str, bool, Any]:
        """Get the params from the cluster needed to use Ray client."""
        connect_url = None
        metadata = [("cookie", "anyscale-token=" + session_meta.access_token)]
        if session_meta.connect_url:
            url_components = session_meta.connect_url.split("?port=")
            metadata += [("port", url_components[1])] if len(url_components) > 1 else []
            connect_url = url_components[0]
        else:
            # This code path can go away once all sessions use session_meta.connect_url:
            # TODO(nikita): Use the service_proxy_url once it is fixed for anyscale up with file mounts.
            full_url = session_meta.jupyter_notebook_url
            assert (
                full_url is not None
            ), f"Unable to determine URL for Session: {session_meta.name}, please retry shortly or try a different session."
            # like "session-fqsx0p3pzfna71xxxxxxx.anyscaleuserdata.com"
            connect_url = full_url.split("/")[2].lower() + ":8081"
            metadata += [("port", "10001")]

        if self._secure:
            connect_url = connect_url.replace(":8081", "")

        return connect_url, self._secure, metadata

    def _get_cluster_compute_id_from_name(
        self, project_id: str, cluster_compute_name: str
    ) -> str:
        """gets the cluster compute id given a cluster name."""
        cluster_computes = self._api_client.search_compute_templates_api_v2_compute_templates_search_post(
            ComputeTemplateQuery(
                orgwide=True,
                name={"equals": cluster_compute_name},
                include_anonymous=True,
            )
        ).results
        if len(cluster_computes) == 0:
            raise ValueError(
                f"The cluster compute template {cluster_compute_name}"
                " is not registered."
            )
        return cluster_computes[0].id

    def _register_compute_template(
        self, project_id: str, config_object: ComputeTemplateConfig
    ) -> str:
        """
        Register compute template with a default name and return the compute template id."""
        created_template = self._api_client.create_compute_template_api_v2_compute_templates_post(
            create_compute_template=CreateComputeTemplate(
                name="connect-autogenerated-config-{}".format(
                    datetime.now().isoformat()
                ),
                project_id=project_id,
                config=config_object,
                anonymous=True,
            )
        ).result
        compute_template_id = str(created_template.id)
        return compute_template_id

    def _wait_for_app_build(self, project_id: str, build_id: str) -> Build:
        has_logged = False
        while True:
            build = self._anyscale_sdk.get_build(build_id).result
            if build.status in ["pending", "in_progress"]:
                if not has_logged:
                    url = get_endpoint(
                        f"projects/{project_id}/app-config-details/{build_id}"
                    )
                    self._log.info(
                        f"Waiting for cluster env to be built (see {url} for progress)..."
                    )
                    has_logged = True
                time.sleep(10.0)
            elif build.status in ["failed", "pending_cancellation", "canceled"]:
                raise RuntimeError(
                    "Cluster env status is '{}', please select another revision!".format(
                        build.status
                    )
                )
            else:
                assert build.status == "succeeded"
                return build

    def _get_cluster_env_build(
        self, project_id: str, app_config_name: str, app_config_revision: Optional[int]
    ) -> Build:
        app_template_id = None
        app_templates = self._list_app_configs(name_contains=app_config_name)
        for app_template in app_templates:
            if app_template.name == app_config_name:
                app_template_id = app_template.id
        if not app_template_id:
            app_templates = self._list_app_configs()
            raise RuntimeError(
                "Application config '{}' not found. ".format(app_config_name)
                + "Available app configs: {}".format(
                    ", ".join(a.name for a in app_templates)
                )
            )
        builds = self._list_builds(app_template_id)

        build_to_use = None
        if app_config_revision:
            for build in builds:
                if build.revision == app_config_revision:
                    build_to_use = build

            if not build_to_use:
                raise RuntimeError(
                    "Revision {} of app config '{}' not found.".format(
                        app_config_revision, app_config_name
                    )
                )
        else:
            latest_build_revision = -1
            for build in builds:
                if build.revision > latest_build_revision:
                    latest_build_revision = build.revision
                    build_to_use = build
            self._log.debug(
                "Using latest revision {} of {}".format(
                    latest_build_revision, app_config_name
                )
            )
        assert build_to_use  # for mypy
        return build_to_use

    def _build_app_config_from_source(self, project_id: str) -> str:
        config_name = "ray-build-{}-{}".format(self._build_pr, self._build_commit)
        # Force creation of a unique app config.
        if self._force_rebuild:
            config_name += "-{}".format(int(time.time()))
        app_templates = self._list_app_configs(name_contains=config_name)
        found = any(a.name == config_name for a in app_templates)
        if not found:
            build_steps = BUILD_STEPS.copy()
            # Add a unique command to bust the Makisu cache if needed.
            # Otherwise we could end up caching a previous fetch.
            build_steps.append("echo UNIQUE_ID={}".format(config_name))
            if self._build_pr:
                build_steps.append(
                    "cd ray && git fetch origin pull/{}/head:target && "
                    "git checkout target".format(self._build_pr)
                )
            if self._build_commit:
                build_steps.append(
                    "cd ray && git checkout {}".format(self._build_commit)
                )
            build_steps.append(
                'cd ray/python && sudo env "PATH=$PATH" python setup.py develop'
            )
            self._anyscale_sdk.create_app_config(
                {
                    "name": config_name,
                    "project_id": project_id,
                    "config_json": {
                        "base_image": _get_base_image("ray", "nightly", "cpu"),
                        "debian_packages": ["curl", "unzip", "zip", "gnupg"],
                        "post_build_cmds": build_steps,
                    },
                }
            )
        return config_name

    def _get_app_config_docker_image(self, project_id: str, build_to_use: Build) -> str:
        # Wait for build to complete:
        build_to_use = self._wait_for_app_build(project_id, build_to_use.id)
        return "localhost:5555/{}".format(build_to_use.docker_image_name)

    def _exec_self_in_head_node(self) -> None:
        """Run the current main file in the head node."""
        cur_file = os.path.abspath(sys.argv[0])
        # TODO(ekl) it would be nice to support keeping the original file name,
        # but "anyscale push" isn't escaping e.g., spaces correctly.
        tmp_file = "/tmp/anyscale-connect-{}.py".format(uuid.uuid4().hex)
        cur_dir = os.getcwd()
        try:
            assert self._project_dir is not None
            os.chdir(self._project_dir)
            command = [
                "anyscale",
                "push",
                self._cluster_name,
                "-s",
                cur_file,
                "-t",
                tmp_file,
            ]
            self._log.debug("Running", command)
            self._subprocess.check_output(
                command, stderr=subprocess.STDOUT,
            )
            command = (
                [
                    "anyscale",
                    "exec",
                    "--session-name",
                    self._cluster_name,
                    "python",
                    tmp_file,
                ]
                + sys.argv[1:]  # type: ignore
            )
            self._log.debug("Running", command)
            self._subprocess.check_call(command)
        finally:
            os.chdir(cur_dir)
        self._os._exit(0)

    def _exec_self_in_local_docker(self) -> None:
        """Run the current main file in a local docker image."""
        cur_file = os.path.abspath(sys.argv[0])
        docker_image = _get_base_image("ray-ml", MINIMUM_RAY_VERSION, "cpu")
        command = [
            "docker",
            "run",
            "--env",
            "ANYSCALE_HOST={}".format(anyscale.conf.ANYSCALE_HOST),
            "--env",
            "ANYSCALE_CLI_TOKEN={}".format(self._credentials),
            "-v",
            "{}:/user_main.py".format(cur_file),
            "--entrypoint=/bin/bash",
            docker_image,
            "-c",
            "python /user_main.py {}".format(
                " ".join([shlex.quote(x) for x in sys.argv[1:]])
            ),
        ]
        self._log.debug("Running", command)
        self._subprocess.check_call(command)
        self._os._exit(0)

    def _get_project_name(self, project_id: str) -> str:
        return str(self._anyscale_sdk.get_project(project_id).result.name)

    def _list_entities(
        self, list_function: Callable[..., Any], container_id: str
    ) -> List[Any]:
        entities = []
        has_more = True
        paging_token = None
        while has_more:
            resp = list_function(container_id, count=50, paging_token=paging_token)
            entities.extend(resp.results)
            paging_token = resp.metadata.next_paging_token
            has_more = paging_token is not None
        return entities

    def _list_sessions(self, project_id: str) -> List[Session]:
        return self._list_entities(self._anyscale_sdk.list_sessions, project_id)

    def _list_app_configs(
        self, project_id: Optional[str] = None, name_contains: Optional[str] = None
    ) -> List[AppConfig]:
        entities = []
        has_more = True
        paging_token = None
        while has_more:
            resp = self._anyscale_sdk.list_app_configs(
                project_id=project_id,
                name_contains=name_contains,
                count=50,
                paging_token=paging_token,
            )
            entities.extend(resp.results)
            paging_token = resp.metadata.next_paging_token
            has_more = paging_token is not None
        return entities

    def _list_builds(self, application_template_id: str) -> List[Build]:
        return self._list_entities(
            self._anyscale_sdk.list_builds, application_template_id
        )

    def _check_required_ray_version(
        self,
        ray_version: str,
        ray_commit: str,
        required_ray_version: str,
        required_ray_commit: str,
    ) -> None:
        if ray_commit == "{{RAY_COMMIT_SHA}}":
            self._log.warning(
                "Ray version checking is skipped because Ray is likely built locally for development. "
                "Compatibility between Ray and Anyscale connect is not guaranteed."
            )
            return

        if ray_version != required_ray_version:
            msg = "The local ray installation has version {}, but {} is required.".format(
                ray_version, required_ray_version
            )
        elif ray_commit != required_ray_commit:
            msg = "The local ray installation has commit {}, but {} is required.".format(
                ray_commit[:7], required_ray_commit[:7]
            )
        else:
            # Version and commit matches.
            return

        msg = (
            "{}\nPlease install the required "
            "Ray version by running:\n\t`pip uninstall ray -y && pip install -U {}`\nTo unsafely "
            "ignore this check, set IGNORE_VERSION_CHECK=1.".format(
                msg, get_wheel_url(required_ray_commit, required_ray_version),
            )
        )
        if self._ignore_version_check:
            self._log.debug(msg)
        else:
            raise ValueError(msg)

    def _dynamic_check(self, info: Dict[str, str]) -> None:
        self._check_required_ray_version(
            self._ray.__version__,
            self._ray.__commit__,
            info["ray_version"],
            info["ray_commit"],
        )

        # NOTE: This check should not be gated with IGNORE_VERSION_CHECK, because this is
        # replacing Ray Client's internal check.
        local_major_minor = f"{sys.version_info[0]}.{sys.version_info[1]}"
        client_version = f"{local_major_minor}.{sys.version_info[2]}"
        server_version = info["python_version"]
        assert server_version.startswith(
            local_major_minor
        ), f"Python minor versions differ between client ({client_version}) and server ({server_version}). Please ensure that they match."


# This implements the following utility function for users:
# $ pip install -U `python -m anyscale.connect required_ray_version`
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "required_ray_version":
        print(f"ray>={MINIMUM_RAY_VERSION}")
    else:
        raise ValueError("Unsupported argument.")
