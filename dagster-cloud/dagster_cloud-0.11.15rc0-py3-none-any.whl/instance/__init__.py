from dagster import Field, check
from dagster.config.validate import process_config, resolve_to_config_type
from dagster.core.errors import DagsterInvalidConfigError, DagsterInvariantViolationError
from dagster.core.instance import DagsterInstance
from dagster.core.instance.config import config_field_for_configurable_class
from dagster.core.instance.ref import configurable_class_data

from ..storage.client import create_proxy_client, dagster_cloud_api_config


class DagsterCloudInstance(DagsterInstance):
    pass


class DagsterCloudAgentInstance(DagsterCloudInstance):
    def __init__(self, *args, dagster_cloud_api, user_code_launcher=None, **kwargs):
        super().__init__(*args, **kwargs)

        processed_api_config = process_config(
            resolve_to_config_type(dagster_cloud_api_config()),
            check.dict_param(dagster_cloud_api, "dagster_cloud_api"),
        )

        if not processed_api_config.success:
            raise DagsterInvalidConfigError(
                "Errors whilst loading dagster_cloud_api config",
                processed_api_config.errors,
                dagster_cloud_api,
            )

        self._dagster_cloud_api_config = processed_api_config.value

        self._user_code_launcher_data = (
            configurable_class_data(user_code_launcher) if user_code_launcher else None
        )

        self._graphql_client = None

    def create_graphql_client(self):
        return create_proxy_client(self.dagster_cloud_graphql_url, self._dagster_cloud_api_config)

    @property
    def graphql_client(self):
        if self._graphql_client == None:
            self._graphql_client = self.create_graphql_client()

        return self._graphql_client

    @property
    def dagster_cloud_url(self):
        return self._dagster_cloud_api_config["url"]

    @property
    def dagster_cloud_graphql_url(self):
        return f"{self.dagster_cloud_url}/graphql"

    @property
    def dagster_cloud_username(self):
        return self._dagster_cloud_api_config.get("username")

    @property
    def dagster_cloud_password(self):
        return self._dagster_cloud_api_config.get("password")

    def create_user_code_launcher(self):
        if not self._user_code_launcher_data:
            # This is a user facing error. We should have more actionable advice and link to docs here.
            raise DagsterInvariantViolationError(
                "User code launcher is not configured for DagsterCloudAgentInstance. "
                "Configure a user code launcher under the user_code_launcher: key in your dagster.yaml file."
            )

        user_code_launcher = self._user_code_launcher_data.rehydrate()
        user_code_launcher.register_instance(self)
        return user_code_launcher

    @staticmethod
    def get():  # pylint: disable=arguments-differ
        instance = DagsterInstance.get()
        if not isinstance(instance, DagsterCloudAgentInstance):
            raise DagsterInvariantViolationError(
                """
DagsterInstance.get() did not return a DagsterCloudAgentInstance. Make sure that your"
`dagster.yaml` file is correctly configured to include the following:
custom_instance_class:
  module: dagster_cloud.instance
  class: DagsterCloudAgentInstance
"""
            )
        return instance

    @classmethod
    def config_schema(cls):
        return {
            "dagster_cloud_api": Field(dagster_cloud_api_config(), is_required=True),
            "user_code_launcher": config_field_for_configurable_class(),
        }

    def get_required_daemon_types(self):
        from dagster_cloud.daemon.dagster_cloud_api_daemon import DagsterCloudApiDaemon

        return [DagsterCloudApiDaemon.daemon_type()]
