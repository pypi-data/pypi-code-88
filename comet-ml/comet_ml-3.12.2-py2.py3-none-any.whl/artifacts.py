# -*- coding: utf-8 -*-
# *******************************************************
#   ____                     _               _
#  / ___|___  _ __ ___   ___| |_   _ __ ___ | |
# | |   / _ \| '_ ` _ \ / _ \ __| | '_ ` _ \| |
# | |__| (_) | | | | | |  __/ |_ _| | | | | | |
#  \____\___/|_| |_| |_|\___|\__(_)_| |_| |_|_|
#
#  Sign up for free at http://www.comet.ml
#  Copyright (C) 2015-2021 Comet ML INC
#  This file can not be copied and/or distributed
#  without the express permission of Comet ML Inc.
# *******************************************************

import json
import os
import sys
import tempfile
from collections import namedtuple
from logging import getLogger

import requests
import semantic_version
import six

from ._typing import Any, Dict, Iterable, List, Optional, Set, Tuple, Union
from .config import Config
from .connection import RestApiClient, get_thread_session, write_stream_response_to_file
from .exceptions import (
    ArtifactDownloadException,
    ArtifactNotFound,
    CometRestApiException,
    GetArtifactException,
    LogArtifactException,
)
from .file_uploader import FileUpload, MemoryFileUpload, dispatch_user_file_upload
from .file_utils import file_sha1sum, io_sha1sum
from .logging_messages import (
    ARTIFACT_DOWNLOAD_FILE_OVERWRITTEN,
    ARTIFACT_VERSION_CREATED_WITH_PREVIOUS,
    ARTIFACT_VERSION_CREATED_WITHOUT_PREVIOUS,
)
from .parallel_utils import get_thread_pool
from .summary import Summary
from .utils import ImmutableDict, makedirs
from .validation_utils import validate_metadata

LOGGER = getLogger(__name__)


def _parse_artifact_name(artifact_name):
    # type: (str) -> Tuple[Optional[str], str, Optional[str]]
    """ Parse an artifact_name, potentially a fully-qualified name
    """

    splitted = artifact_name.split("/")

    # First parse the workspace
    if len(splitted) == 1:
        workspace = None
        artifact_name_version = splitted[0]
    else:
        workspace = splitted[0]
        artifact_name_version = splitted[1]

    name_version_splitted = artifact_name_version.split(":", 1)

    if len(name_version_splitted) == 1:
        artifact_name = name_version_splitted[0]
        version_or_alias = None
    else:
        artifact_name = name_version_splitted[0]
        version_or_alias = name_version_splitted[1]

    return (workspace, artifact_name, version_or_alias)


def _upsert_artifact(artifact, rest_api_client, experiment_key):
    # type: (Artifact, RestApiClient, str) -> Tuple[str, str]
    try:

        artifact_version = artifact.version
        if artifact_version is not None:
            artifact_version = str(artifact_version)

        response = rest_api_client.upsert_artifact(
            artifact_name=artifact.name,
            artifact_type=artifact.artifact_type,
            experiment_key=experiment_key,
            metadata=artifact.metadata,
            version=artifact_version,
            aliases=list(artifact.aliases),
            version_tags=list(artifact.version_tags),
        )
    except CometRestApiException as e:
        raise LogArtifactException(e.safe_msg, e.sdk_error_code)
    except requests.RequestException:
        raise LogArtifactException()

    result = response.json()

    artifact_id = result["artifactId"]
    artifact_version_id = result["artifactVersionId"]

    version = result["currentVersion"]
    _previous_version = result["previousVersion"]

    if _previous_version is None:
        LOGGER.info(ARTIFACT_VERSION_CREATED_WITHOUT_PREVIOUS, artifact.name, version)
    else:
        LOGGER.info(
            ARTIFACT_VERSION_CREATED_WITH_PREVIOUS,
            artifact.name,
            version,
            _previous_version,
        )

    return (artifact_id, artifact_version_id)


def _download_artifact_asset(
    url,  # type: str
    params,  # type: Dict[str, Any]
    headers,  # type: Dict[str, Any]
    timeout,  # type: int
    asset_id,  # type: str
    artifact_repr,  # type: str
    artifact_str,  # type: str
    asset_logical_path,  # type: str
    asset_path,  # type: str
    overwrite,  # type: bool
):
    # type: (...) -> None
    try:
        retry_session = get_thread_session(retry=True)

        response = retry_session.get(
            url=url, params=params, headers=headers, stream=True,
        )  # type: requests.Response

        if response.status_code != 200:
            response.close()
            raise CometRestApiException("GET", response)
    except Exception:
        raise ArtifactDownloadException(
            "Cannot download Asset %r for Artifact %s" % (asset_id, artifact_repr)
        )

    try:
        _write_artifact_asset_response_to_disk(
            artifact_str, asset_id, asset_logical_path, asset_path, overwrite, response
        )
    finally:
        try:
            response.close()
        except Exception:
            LOGGER.debug(
                "Error closing artifact asset download response", exc_info=True
            )
            pass

    return None


def _write_artifact_asset_response_to_disk(
    artifact_str,  # type: str
    asset_id,  # type: str
    asset_logical_path,  # type: str
    asset_path,  # type: str
    overwrite,  # type: bool
    response,  # type: requests.Response
):
    # type: (...) -> None
    if os.path.isfile(asset_path):
        if overwrite == "OVERWRITE":
            LOGGER.warning(
                ARTIFACT_DOWNLOAD_FILE_OVERWRITTEN,
                asset_path,
                asset_logical_path,
                artifact_str,
            )
        elif overwrite == "PRESERVE":
            # TODO: Print LOG message if content is different when we have the SHA1 stored the
            # backend
            pass
        else:
            # Download the file to a temporary file
            # TODO: Just compare the checksums
            try:
                existing_file_checksum = file_sha1sum(asset_path)
            except Exception:
                raise ArtifactDownloadException(
                    "Cannot read file %r to compare content, check logs for details"
                    % (asset_path)
                )

            try:
                with tempfile.NamedTemporaryFile() as f:
                    write_stream_response_to_file(response, f)

                    # Flush to be sure that everything is written
                    f.flush()
                    f.seek(0)

                    # Compute checksums
                    asset_checksum = io_sha1sum(f)

            except Exception:
                raise ArtifactDownloadException(
                    "Cannot write Asset %r on disk path %r, check logs for details"
                    % (asset_id, asset_path)
                )

            if asset_checksum != existing_file_checksum:
                raise ArtifactDownloadException(
                    "Cannot write Asset %r on path %r, a file already exists"
                    % (asset_id, asset_path,)
                )

            return None
    else:
        try:
            dirpart = os.path.dirname(asset_path)
            makedirs(dirpart, exist_ok=True)
        except Exception:
            raise ArtifactDownloadException(
                "Cannot write Asset %r on disk path %r, check logs for details"
                % (asset_id, asset_path,)
            )

    try:
        with open(asset_path, "wb") as f:
            write_stream_response_to_file(response, f)
    except Exception:
        raise ArtifactDownloadException(
            "Cannot write Asset %r on disk path %r, check logs for details"
            % (asset_id, asset_path,)
        )


def _validate_overwrite_strategy(user_overwrite_strategy):
    # type: (Any) -> str

    if isinstance(user_overwrite_strategy, six.string_types):
        lower_user_overwrite_strategy = user_overwrite_strategy.lower()
    else:
        lower_user_overwrite_strategy = user_overwrite_strategy

    if (
        lower_user_overwrite_strategy is False
        or lower_user_overwrite_strategy == "fail"
    ):
        return "FAIL"

    elif lower_user_overwrite_strategy == "preserve":
        return "PRESERVE"

    elif (
        lower_user_overwrite_strategy is True
        or lower_user_overwrite_strategy == "overwrite"
    ):
        return "OVERWRITE"

    else:
        raise ValueError("Invalid user_overwrite value %r" % user_overwrite_strategy)


class Artifact(object):
    def __init__(
        self,
        name,  # type: str
        artifact_type,  # type: str
        version=None,  # type: Optional[str]
        aliases=None,  # type: Optional[Iterable[str]]
        metadata=None,  # type: Any
        version_tags=None,  # type: Optional[Iterable[str]]
    ):
        # type: (...) -> None
        """
        Comet Artifacts allow keeping track of assets beyond any particular experiment. You can keep
        track of Artifact versions, create many types of assets, manage them, and use them in any
        step in your ML pipelines---from training to production deployment.

        Artifacts live in a Comet Project, are identified by their name and version string number.

        Example how to log an artifact with an asset:

        ```python
        from comet_ml import Artifact, Experiment

        experiment = Experiment()
        artifact = Artifact("Artifact-Name", "Artifact-Type")
        artifact.add("local-file")

        experiment.log_artifact(artifact)
        experiment.end()
        ```

        Example how to get and download an artifact assets:

        ```python
        from comet_ml import Experiment

        experiment = Experiment()
        artifact = experiment.get_artifact("Artifact-Name", WORKSPACE, PROJECT_NAME)

        artifact.download("/data/input")
        ```

        The artifact is created on the frontend only when calling `Experiment.log_artifact`

        Args:
            name: The artifact name.
            artifact_type: The artifact-type, for example `dataset`.
            version: Optional. The version number to create. If not provided, a new version number
                will be created automatically.
            aliases: Optional. Iterable of String. Some aliases to attach to the future Artifact
                Version. The aliases list is converted into a set for de-duplication.
            metadata: Optional. Some additional data to attach to the future Artifact Version. Must
                be a JSON-encodable dict.
        """

        # Artifact fields
        self.artifact_type = artifact_type
        self.name = name

        # Upsert fields
        if version is None:
            self.version = None
        else:
            self.version = semantic_version.Version(version)

        self.version_tags = set()  # type: Set[str]
        if version_tags is not None:
            self.version_tags = set(version_tags)

        self.aliases = set()  # type: Set[str]
        if aliases is not None:
            self.aliases = set(aliases)

        self.metadata = validate_metadata(metadata, raise_on_invalid=True)

        self._assets = []  # type: List[Dict[str, Any]]
        self._remote_assets = []  # type: List[Dict[str, Any]]

        self._download_local_path = None  # type: Optional[str]

    def add(
        self,
        local_path_or_data,
        logical_path=None,
        overwrite=False,
        copy_to_tmp=True,  # if local_path_or_data is a file pointer
        metadata=None,
    ):
        # type: (Any, Optional[str], bool, bool, Optional[int], Any) -> None
        """
        Add a local asset to the current pending artifact object.

        Args:
            local_path_or_data: String or File-like - either the file path of the file you want
                to log, or a file-like asset.
            logical_path: String - Optional. A custom file name to be displayed. If not
                provided the filename from the `local_path_or_data` argument will be used.
            overwrite: if True will overwrite all existing assets with the same name.
            copy_to_tmp: If `local_path_or_data` is a file-like object, then this flag determines
                if the file is first copied to a temporary file before upload. If
                `copy_to_tmp` is False, then it is sent directly to the cloud.
            metadata: Optional. Some additional data to attach to the the audio asset. Must be a
                JSON-encodable dict.
        """
        dispatched = dispatch_user_file_upload(local_path_or_data)

        if not isinstance(dispatched, (FileUpload, MemoryFileUpload)):
            raise ValueError(
                "Invalid file_data %r, must either be a valid file-path or an IO object"
                % local_path_or_data
            )

        self._assets.append(
            {
                "_size": getattr(dispatched, "file_size", 0),
                "copy_to_tmp": copy_to_tmp,
                "file_data": local_path_or_data,
                "file_name": logical_path,
                "metadata": metadata,
                "overwrite": overwrite,
            }
        )

    def add_remote(
        self,
        uri,  # type: Any
        logical_path=None,  # type: Any
        overwrite=False,
        asset_type="asset",
        metadata=None,
    ):
        # type: (...) -> None
        """
        Add a remote asset to the current pending artifact object. A Remote Asset is an asset but
        its content is not uploaded and stored on Comet. Rather a link for its location is stored so
        you can identify and distinguish between two experiment using different version of a dataset
        stored somewhere else.

        Args:
            uri: String - the remote asset location, there is no imposed format and it could be a
                private link.
            logical_path: String, Optional. The "name" of the remote asset, could be a dataset
                name, a model file name.
            overwrite: if True will overwrite all existing assets with the same name.
            metadata: Some additional data to attach to the the remote asset.
                Must be a JSON-encodable dict.
        """
        self._remote_assets.append(
            {
                "asset_type": asset_type,
                "metadata": metadata,
                "overwrite": overwrite,
                "remote_file_name": logical_path,
                "uri": uri,
            }
        )

    def __str__(self):
        return "%s(%r, artifact_type=%r)" % (
            self.__class__.__name__,
            self.name,
            self.artifact_type,
        )

    def __repr__(self):
        return (
            "%s(name=%r, artifact_type=%r, version=%r, aliases=%r, version_tags=%s)"
            % (
                self.__class__.__name__,
                self.name,
                self.artifact_type,
                self.version,
                self.aliases,
                self.version_tags,
            )
        )

    @property
    def assets(self):
        """
        The list of `ArtifactAssets` that have been logged with this `Artifact`.
        """
        artifact_version_assets = []

        for asset in self._assets:
            artifact_version_assets.append(
                ArtifactAsset(
                    False,
                    asset["file_name"],
                    asset["_size"],
                    None,
                    asset["metadata"],
                    None,
                    asset["file_data"],
                )
            )

        for remote_asset in self._remote_assets:
            artifact_version_assets.append(
                ArtifactAsset(
                    True,
                    remote_asset["remote_file_name"],
                    0,
                    remote_asset["uri"],
                    remote_asset["metadata"],
                    remote_asset["asset_type"],
                    None,
                )
            )

        return artifact_version_assets

    @property
    def download_local_path(self):
        # type: () -> Optional[str]
        """ If the Artifact object was returned by `LoggedArtifact.download`, returns the root path
        where the assets has been downloaded. Else, returns None.
        """
        return self._download_local_path


def _get_artifact(rest_api_client, get_artifact_params, experiment_id, summary, config):
    # type: (RestApiClient, Dict[str, str], str, Summary, Config) -> LoggedArtifact

    try:
        result = rest_api_client.get_artifact_version_details(**get_artifact_params)
    except CometRestApiException as e:
        if e.sdk_error_code == 624523:
            raise ArtifactNotFound("Artifact not found with %r" % (get_artifact_params))

        raise
    except Exception:
        raise GetArtifactException(
            "Get artifact failed with an error, check the logs for details"
        )

    artifact_name = result["artifact"]["artifactName"]
    artifact_version = result["artifactVersion"]
    artifact_metadata = result["metadata"]
    if artifact_metadata:
        try:
            artifact_metadata = json.loads(artifact_metadata)
        except Exception:
            LOGGER.warning(
                "Couldn't decode metadata for artifact %r:%r"
                % (artifact_name, artifact_version)
            )
            artifact_metadata = None

    return LoggedArtifact(
        artifact_id=result["artifact"]["artifactId"],
        artifact_version_id=result["artifactVersionId"],
        artifact_name=artifact_name,
        artifact_type=result["artifact"]["artifactType"],
        workspace=result["artifact"]["workspaceName"],
        rest_api_client=rest_api_client,
        experiment_key=experiment_id,  # TODO: Remove ME
        version=artifact_version,
        aliases=result["alias"],
        artifact_tags=result["artifact"]["tags"],
        version_tags=result["tags"],
        size=result["sizeInBytes"],
        metadata=artifact_metadata,
        summary=summary,
        config=config,
    )


class LoggedArtifact(object):
    def __init__(
        self,
        artifact_name,
        artifact_type,
        artifact_id,
        artifact_version_id,
        workspace,
        rest_api_client,  # type: RestApiClient
        experiment_key,
        version,
        aliases,
        artifact_tags,
        version_tags,
        size,
        metadata,
        summary,
        config,  # type: Config
    ):
        # type: (...) -> None
        """
        You shouldn't try to create this object by hand, please use
        [Experiment.get_artifact()](/docs/python-sdk/Experiment/#experimentget_artifact) instead to
        retrieve an artifact.
        """
        # Artifact fields
        self._artifact_type = artifact_type
        self._name = artifact_name
        self._artifact_id = artifact_id
        self._artifact_version_id = artifact_version_id

        self._version = semantic_version.Version(version)
        self._aliases = frozenset(aliases)
        self._rest_api_client = rest_api_client
        self._workspace = workspace
        self._artifact_tags = frozenset(artifact_tags)
        self._version_tags = frozenset(version_tags)
        self._size = size
        self._experiment_key = experiment_key  # TODO: Remove ME
        self._summary = summary
        self._config = config

        if metadata is not None:
            self._metadata = ImmutableDict(metadata)
        else:
            self._metadata = ImmutableDict()

    def _raw_assets(self):
        """ Returns the artifact version ID assets
        """
        return self._rest_api_client.get_artifact_files(
            workspace=self._workspace, name=self._name, version=str(self.version),
        )["files"]

    @property
    def assets(self):
        # type: () -> List[LoggedArtifactAsset]
        """
        The list of `LoggedArtifactAsset` that have been logged with this `LoggedArtifact`.
        """
        artifact_version_assets = []

        for asset in self._raw_assets():
            remote = asset["link"] is not None  # TODO: Fix me
            artifact_version_assets.append(
                LoggedArtifactAsset(
                    remote,
                    asset["fileName"],
                    asset["fileSize"],
                    asset["link"],
                    asset["metadata"],
                    asset["type"],
                    asset["assetId"],
                    self._artifact_version_id,
                    self._artifact_id,
                )
            )

        return artifact_version_assets

    @property
    def remote_assets(self):
        # type: () -> List[LoggedArtifactAsset]
        """
        The list of remote `LoggedArtifactAsset` that have been logged with this `LoggedArtifact`.
        """
        artifact_version_assets = []

        for asset in self._raw_assets():
            remote = asset["link"] is not None  # TODO: Fix me

            if not remote:
                continue

            artifact_version_assets.append(
                LoggedArtifactAsset(
                    remote,
                    asset["fileName"],
                    asset["fileSize"],
                    asset["link"],
                    asset["metadata"],
                    asset["type"],
                    asset["assetId"],
                    self._artifact_version_id,
                    self._artifact_id,
                )
            )

        return artifact_version_assets

    def download(self, path=None, overwrite_strategy=False):
        # type: (Optional[str], Union[bool, str]) -> Artifact
        """
        Download the current Artifact Version assets to a given directory (or the local directory by
        default). This downloads only non-remote assets. You can access remote assets link with the
        `artifact.assets` property.

        Args:
            path: String, Optional. Where to download artifact version assets. If not provided,
                a temporay path will be used, the root path can be accessed through the Artifact object
                which is returned by download under the `.download_local_path` attribute.
            overwrite_strategy: String or Boolean. One of the three possible strategies to handle
                conflict when trying to download an artifact version asset to a path with an existing
                file. See below for allowed values. Default is False or "FAIL".

        Overwrite strategy allowed values:

            * False or "FAIL": If a file already exists and its content is different, raise the
            `comet_ml.exceptions.ArtifactDownloadException`.
            * "PRESERVE": If a file already exists and its content is different, show a WARNING but
            preserve the existing content.
            * True or "OVERWRITE": If a file already exists and its content is different, replace it
            by the asset version asset.

        Returns: Artifact object
        """

        if path is None:
            root_path = tempfile.mkdtemp()
        else:
            root_path = path

        overwrite_strategy = _validate_overwrite_strategy(overwrite_strategy)

        new_artifact_assets = []
        new_artifact_remote_assets = []

        try:
            raw_assets = self._raw_assets()
        except Exception:
            raise ArtifactDownloadException(
                "Cannot get asset list for Artifact %r" % self
            )

        results = []

        worker_cpu_ratio = self._config.get_int(
            None, "comet.internal.file_upload_worker_ratio"
        )
        _, _, download_pool = get_thread_pool(worker_cpu_ratio)

        download_timeout = self._config.get_int(None, "comet.timeout.file_download")

        self_repr = repr(self)
        self_str = str(self)

        for asset in raw_assets:
            asset_metadata = asset["metadata"]
            if asset_metadata is not None:
                asset_metadata = json.loads(asset["metadata"])

            asset_remote = asset["link"] is not None  # TODO: Fixme
            if asset_remote is True:
                # We don't download remote assets
                new_artifact_remote_assets.append(
                    {
                        "asset_type": asset["type"],
                        "metadata": asset_metadata,
                        "overwrite": False,
                        "remote_file_name": asset["fileName"],
                        "uri": asset["link"],
                    }
                )

                self._summary.increment_section("downloads", "artifact assets")
            else:
                asset_filename = asset["fileName"]
                asset_path = os.path.join(root_path, asset_filename)
                asset_id = asset["assetId"]
                prepared_request = self._rest_api_client._prepare_experiment_asset_request(
                    asset_id, self._experiment_key, asset["artifactVersionId"]
                )
                url, params, headers = prepared_request

                result = download_pool.apply_async(
                    _download_artifact_asset,
                    args=(
                        url,
                        params,
                        headers,
                        download_timeout,
                        asset_id,
                        self_repr,
                        self_str,
                        asset_filename,
                        asset_path,
                        overwrite_strategy,
                    ),
                )

                results.append((result, asset_path, asset_filename, asset_metadata))

        # Forbid new usage
        download_pool.close()

        try:
            for (
                result,
                result_asset_path,
                result_asset_filename,
                result_asset_metadata,
            ) in results:
                result.get(download_timeout)

                new_asset_size = os.path.getsize(result_asset_path)

                self._summary.increment_section(
                    "downloads", "artifact assets", size=new_asset_size,
                )

                new_artifact_assets.append(
                    {
                        "_size": new_asset_size,
                        "copy_to_tmp": False,
                        "file_data": result_asset_path,
                        "file_name": result_asset_filename,
                        "metadata": result_asset_metadata,
                        "overwrite": False,
                    }
                )
        finally:
            download_pool.join()

        new_artifact = Artifact(self._name, self._artifact_type)
        new_artifact._assets = new_artifact_assets
        new_artifact._remote_assets = new_artifact_remote_assets
        new_artifact._download_local_path = root_path
        return new_artifact

    # Public properties
    @property
    def name(self):
        """
        The logged artifact name.
        """
        return self._name

    @property
    def artifact_type(self):
        """
        The logged artifact type.
        """
        return self._artifact_type

    @property
    def version(self):
        """
        The logged artifact version, as a SemanticVersion. See
        https://python-semanticversion.readthedocs.io/en/latest/reference.html#semantic_version.Version
        for reference
        """
        return self._version

    @property
    def workspace(self):
        """
        The logged artifact workspace name.
        """
        return self._workspace

    @property
    def aliases(self):
        """
        The set of logged artifact aliases.
        """
        return self._aliases

    @property
    def metadata(self):
        """
        The logged artifact metadata.
        """
        return self._metadata

    @property
    def version_tags(self):
        """
        The set of logged artifact version tags.
        """
        return self._version_tags

    @property
    def artifact_tags(self):
        """
        The set of logged artifact tags.
        """
        return self._artifact_tags

    @property
    def size(self):
        """
        The total size of logged artifact version; it is the sum of all the artifact version assets.
        """
        return self._size

    def __str__(self):
        return "<%s '%s/%s:%s'>" % (
            self.__class__.__name__,
            self._workspace,
            self._name,
            self._version,
        )

    def __repr__(self):
        return (
            self.__class__.__name__
            + "(artifact_name=%r, artifact_type=%r, workspace=%r, version=%r, aliases=%r, artifact_tags=%r, version_tags=%r, size=%r)"
            % (
                self._name,
                self._artifact_type,
                self._workspace,
                self._version,
                self._aliases,
                self._artifact_tags,
                self._version_tags,
                self._size,
            )
        )


ArtifactAsset = namedtuple(
    "ArtifactAsset",
    [
        "remote",
        "logical_path",
        "size",
        "link",
        "metadata",
        "asset_type",
        "local_path_or_data",
    ],
)

LoggedArtifactAsset = namedtuple(
    "LoggedArtifactAsset",
    [
        "remote",
        "logical_path",
        "size",
        "link",
        "metadata",
        "asset_type",
        "id",
        "artifact_version_id",
        "artifact_id",
    ],
)

# NamedTuple docstring can only be update starting with Python 3.5
if sys.version_info >= (3, 5):
    ArtifactAsset.__doc__ += ": represent local and remote assets added to an Artifact object but not yet uploaded"
    ArtifactAsset.remote.__doc__ = "Is the asset a remote asset or not, boolean"
    ArtifactAsset.logical_path.__doc__ = "Asset relative logical_path, str or None"
    ArtifactAsset.size.__doc__ = "Asset size if the asset is a non-remote asset, int"
    ArtifactAsset.link.__doc__ = "Asset remote link if the asset is remote, str or None"
    ArtifactAsset.metadata.__doc__ = "Asset metadata, dict"
    ArtifactAsset.asset_type.__doc__ = "Asset type if the asset is remote, str or None"
    ArtifactAsset.local_path_or_data.__doc__ = "Asset local path or in-memory file if the asset is non-remote, str, memory-file or None"

    LoggedArtifactAsset.__doc__ += ": represent assets logged to an Artifact"
    LoggedArtifactAsset.remote.__doc__ = "Is the asset a remote asset or not, boolean"
    LoggedArtifactAsset.logical_path.__doc__ = (
        "Asset relative logical_path, str or None"
    )
    LoggedArtifactAsset.size.__doc__ = (
        "Asset size if the asset is a non-remote asset, int"
    )
    LoggedArtifactAsset.link.__doc__ = (
        "Asset remote link if the asset is remote, str or None"
    )
    LoggedArtifactAsset.metadata.__doc__ = "Asset metadata, dict"
    LoggedArtifactAsset.id.__doc__ = "Asset unique id, str"
    LoggedArtifactAsset.artifact_version_id.__doc__ = "Artifact version id, str"
    LoggedArtifactAsset.artifact_id.__doc__ = "Artifact id, str"
