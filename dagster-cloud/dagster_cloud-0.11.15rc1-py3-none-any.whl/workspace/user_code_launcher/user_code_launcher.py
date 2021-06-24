import sys
import threading
import time
from abc import abstractmethod
from typing import Dict, Set

from dagster import check
from dagster.api.get_server_id import sync_get_server_id
from dagster.core.host_representation.grpc_server_registry import GrpcServerRegistry
from dagster.core.host_representation.origin import RegisteredRepositoryLocationOrigin
from dagster.core.host_representation.repository_location import GrpcServerRepositoryLocation
from dagster.core.instance import MayHaveInstanceWeakref
from dagster.daemon.daemon import get_default_daemon_logger
from dagster.grpc.client import DagsterGrpcClient
from dagster.serdes.serdes import serialize_dagster_namedtuple
from dagster.utils.error import SerializableErrorInfo, serializable_error_info_from_exc_info
from dagster_cloud.api.dagster_cloud_api import (
    DagsterCloudRepositoryData,
    DagsterCloudWorkspaceEntry,
    LoadRepositoriesResponse,
)
from dagster_cloud.util import diff_serializable_namedtuple_map
from dagster_cloud.workspace.origin import CodeDeploymentMetadata
from dagster_cloud.workspace.user_code_launcher.query import UPDATE_WORKSPACE_ENTRY_MUTATION

USER_CODE_LAUNCHER_RECONCILE_INTERVAL = 1

UPDATE_WORKSPACE_ENTRY_MUTATION = """
    mutation updateWorkspaceEntryMutation($serializedWorkspaceEntry: String!) {
        workspace {
            updateWorkspaceEntry(serializedWorkspaceEntry: $serializedWorkspaceEntry) {
                ok
            }
        }
    }
"""


class DagsterCloudUserCodeLauncher(GrpcServerRegistry, MayHaveInstanceWeakref):
    def __init__(self, graphql_client=None):
        self._logger = get_default_daemon_logger("DagsterUserCodeLauncher")
        self._graphql_client = graphql_client  # Pulled from the instance outside of tests

    @abstractmethod
    def update_grpc_metadata(
        self, desired_metadata: Dict[str, CodeDeploymentMetadata], force_update_locations: Set[str]
    ):
        pass

    def supports_origin(self, repository_location_origin):
        return isinstance(repository_location_origin, RegisteredRepositoryLocationOrigin)

    @property
    def supports_reload(self):
        return False

    def reload_grpc_endpoint(self, repository_location_origin):
        raise NotImplementedError("Call update_grpc_metadata to update gRPC endpoints")

    @abstractmethod
    def _get_repository_location_origin(self, location_name):
        pass

    def _update_workspace_entry(self, workspace_entry):
        graphql_client = (
            self._graphql_client if self._graphql_client else self._instance.create_graphql_client()
        )
        update_workspace_entry_result = graphql_client.execute(
            UPDATE_WORKSPACE_ENTRY_MUTATION,
            variable_values={
                "serializedWorkspaceEntry": serialize_dagster_namedtuple(
                    check.inst_param(workspace_entry, "workspace_entry", DagsterCloudWorkspaceEntry)
                )
            },
        )
        if "errors" in update_workspace_entry_result:
            raise Exception("Failure updating workspace: " + str(update_workspace_entry_result))

    def _get_repository_load_data(self, repository_location):
        return LoadRepositoriesResponse(
            repository_datas=[
                DagsterCloudRepositoryData(
                    repo_name=external_repository.name,
                    code_pointer=repository_location.repository_code_pointer_dict[
                        external_repository.name
                    ],
                    external_repository_data=external_repository.external_repository_data,
                )
                for external_repository in repository_location.get_repositories().values()
            ],
            container_image=repository_location.container_image,
            executable_path=repository_location.executable_path,
        )

    def _update_location_error(self, location_name, error_info, metadata):
        self._logger.error(
            "Unable to load location {location_name}. Updating location with error data: {error_info}.".format(
                location_name=location_name,
                error_info=str(error_info),
            )
        )

        # Update serialized error
        errored_workspace_entry = DagsterCloudWorkspaceEntry(
            location_name=location_name,
            deployment_metadata=metadata,
            load_repositories_response=None,
            serialized_error_info=error_info,
        )

        self._update_workspace_entry(errored_workspace_entry)

    def _update_location_data(self, location_name, endpoint, metadata):
        self._logger.info(
            "Updating data for location {location_name}".format(location_name=location_name)
        )

        location_origin = self._get_repository_location_origin(location_name)

        if isinstance(endpoint, SerializableErrorInfo):
            self._update_location_error(location_name, error_info=endpoint, metadata=metadata)
            return

        try:
            repository_location = GrpcServerRepositoryLocation(
                origin=location_origin,
                server_id=endpoint.server_id,
                port=endpoint.port,
                socket=endpoint.socket,
                host=endpoint.host,
                heartbeat=True,
                watch_server=False,
                grpc_server_registry=self,
            )
            loaded_workspace_entry = DagsterCloudWorkspaceEntry(
                location_name=location_name,
                deployment_metadata=metadata,
                load_repositories_response=self._get_repository_load_data(repository_location),
                serialized_error_info=None,
            )
        except Exception:  # pylint: disable=broad-except
            self._update_location_error(
                location_name,
                error_info=serializable_error_info_from_exc_info(sys.exc_info()),
                metadata=metadata,
            )
            return

        self._logger.info(
            "Updating location {location_name} with repository load data".format(
                location_name=location_name,
            )
        )
        self._update_workspace_entry(loaded_workspace_entry)


class ReconcileUserCodeLauncher(DagsterCloudUserCodeLauncher):
    def __init__(self, graphql_client=None):
        self._grpc_endpoints = {}
        self._grpc_endpoints_lock = threading.Lock()
        self._logger = get_default_daemon_logger("ReconcileUserCodeLauncher")

        # periodically reconciles to make desired = actual
        self._desired_metadata = {}
        self._actual_metadata = {}
        self._force_update_keys = set()
        self._metadata_lock = threading.Lock()

        super().__init__(graphql_client=graphql_client)

        self._reconcile_count = 0
        self._reconcile_grpc_metadata_shutdown_event = threading.Event()
        self._reconcile_grpc_metadata_thread = threading.Thread(
            target=self._reconcile_thread,
            args=(self._reconcile_grpc_metadata_shutdown_event,),
            name="grpc-reconcile-watch",
        )
        self._reconcile_grpc_metadata_thread.daemon = True
        self._reconcile_grpc_metadata_thread.start()

    def update_grpc_metadata(self, desired_metadata, force_update_locations):
        check.dict_param(
            desired_metadata, "desired_metadata", key_type=str, value_type=CodeDeploymentMetadata
        )
        check.set_param(force_update_locations, "force_update_locations", str)
        with self._metadata_lock:
            self._desired_metadata = desired_metadata
            self._force_update_keys = force_update_locations

    def _get_repository_location_origin(self, location_name):
        return RegisteredRepositoryLocationOrigin(location_name)

    def _reconcile_thread(self, shutdown_event):
        while True:
            shutdown_event.wait(USER_CODE_LAUNCHER_RECONCILE_INTERVAL)
            if shutdown_event.is_set():
                break

            try:
                self.reconcile()
            except Exception:  # pylint: disable=broad-except
                self._logger.error(
                    "Failure updating user code servers: {exc_info}".format(
                        exc_info=sys.exc_info(),
                    )
                )

    def reconcile(self):
        with self._metadata_lock:
            self._reconcile()
            self._reconcile_count += 1

    def _reconcile(self):
        diff = diff_serializable_namedtuple_map(
            self._desired_metadata, self._actual_metadata, self._force_update_keys
        )

        for to_add_key in diff.to_add:
            try:
                new_endpoint = self._add_server(to_add_key, self._desired_metadata[to_add_key])
            except Exception:  # pylint: disable=broad-except
                error_info = serializable_error_info_from_exc_info(sys.exc_info())
                self._logger.error(
                    "Error while adding server for {to_add_key}: {error_info}".format(
                        to_add_key=to_add_key,
                        error_info=error_info,
                    )
                )
                new_endpoint = error_info

            with self._grpc_endpoints_lock:
                self._grpc_endpoints[to_add_key] = new_endpoint

            self._update_location_data(to_add_key, new_endpoint, self._desired_metadata[to_add_key])

            self._actual_metadata[to_add_key] = self._desired_metadata[to_add_key]

        for to_remove_key in diff.to_remove:
            try:
                self._remove_server(to_remove_key, self._actual_metadata[to_remove_key])
            except Exception:  # pylint: disable=broad-except
                self._logger.error(
                    "Error while removing server for {to_remove_key}: {error_info}".format(
                        to_remove_key=to_remove_key,
                        error_info=serializable_error_info_from_exc_info(sys.exc_info()),
                    )
                )

            with self._grpc_endpoints_lock:
                del self._grpc_endpoints[to_remove_key]
            del self._actual_metadata[to_remove_key]

        update_gens = {}
        for to_update_key in diff.to_update:
            update_gens[to_update_key] = self._gen_update_server(
                to_update_key,
                self._actual_metadata[to_update_key],
                self._desired_metadata[to_update_key],
            )
            try:
                new_updated_endpoint = next(update_gens[to_update_key])
            except Exception:  # pylint: disable=broad-except
                error_info = serializable_error_info_from_exc_info(sys.exc_info())
                self._logger.error(
                    "Error while updating server for {to_update_key}: {error_info}".format(
                        to_update_key=to_update_key,
                        error_info=error_info,
                    )
                )
                new_updated_endpoint = error_info

            with self._grpc_endpoints_lock:
                self._grpc_endpoints[to_update_key] = new_updated_endpoint

            self._update_location_data(
                to_update_key, new_updated_endpoint, self._desired_metadata[to_update_key]
            )

        for to_update_key, update_gen in update_gens.items():
            # Finish any remaining cleanup
            try:
                list(update_gen)
            except Exception:  # pylint: disable=broad-except
                self._logger.error(
                    "Error while cleaning up after updating server for {to_update_key}: {error_info}".format(
                        to_update_key=to_update_key,
                        error_info=serializable_error_info_from_exc_info(sys.exc_info()),
                    )
                )

            self._actual_metadata[to_update_key] = self._desired_metadata[to_update_key]
            if to_update_key in self._force_update_keys:
                self._force_update_keys.remove(to_update_key)

    def get_grpc_endpoint(self, repository_location_origin):
        with self._grpc_endpoints_lock:
            location_name = repository_location_origin.location_name
            endpoint = self._grpc_endpoints.get(location_name)

        if not endpoint:
            raise Exception(f"No server endpoint exists for location {location_name}")

        if isinstance(endpoint, SerializableErrorInfo):
            # Consider raising the original exception here instead of a wrapped one
            raise Exception(
                f"Failure loading server endpoint for location {location_name}: {endpoint}"
            )

        return endpoint

    def get_grpc_endpoints(self):
        with self._grpc_endpoints_lock:
            return self._grpc_endpoints.copy()

    @abstractmethod
    def _add_server(self, location_name, metadata):
        # Add a server for this location / metadata combination. This method should be idempotent
        # it's possible if will be called and the server already exists if an update failed
        # part-way through.
        pass

    @abstractmethod
    def _gen_update_server(self, location_name, old_metadata, new_metadata):
        # Update the server for the given location. Is a generator - should yield the new
        # GrpcServerEndpoint, then clean up any no longer needed resources
        pass

    @abstractmethod
    def _remove_server(self, location_name, metadata):
        pass

    def _wait_for_server(self, host, port, timeout=15, socket=None):
        # Wait for the server to be ready (while also loading the server ID)
        server_id = None
        start_time = time.time()
        while True:
            client = DagsterGrpcClient(port=port, host=host, socket=socket)
            try:
                server_id = sync_get_server_id(client)
                break
            except Exception:  # pylint: disable=broad-except
                pass

            if time.time() - start_time > timeout:
                raise Exception(f"Timed out waiting for server {host}:{port}")

            time.sleep(1)
        return server_id

    @abstractmethod
    def step_handler(self):
        pass

    @abstractmethod
    def run_launcher(self):
        pass
