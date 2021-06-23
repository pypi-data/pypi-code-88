import json
import os
from types import SimpleNamespace
from typing import List

from helix_catalog_sdk.enums import HelixEnvironment


class DataSource:
    def __init__(
        self,
        data_source_name: str,
        content: SimpleNamespace,
        environment: HelixEnvironment,
    ):
        self.name = data_source_name
        self.base_connection = content.base_connection
        self.base_connection_formatted = self.get_connection(content, environment)
        self.production = content.production
        self.staging = content.staging
        self.qa = content.qa
        self.dev = content.dev
        self.connection_type = content.connection_type
        self.resources: List[ResourceItem] = []
        for resource_item in content.resources:
            self.resources.append(
                ResourceItem(resource_item, self.base_connection_formatted)
            )
        self.pipeline_subscriptions: List[PipelineSubscription] = []
        for pipeline_subscription in content.pipeline_subscriptions:
            self.pipeline_subscriptions.append(
                PipelineSubscription(pipeline_subscription)
            )

    def get_connection(
        self, content: SimpleNamespace, environment: HelixEnvironment
    ) -> str:
        base_connection_formatted: str = content.base_connection
        if environment == HelixEnvironment.PRODUCTION:
            base_connection_formatted = content.base_connection.format(
                env=content.production
            )
        elif environment == HelixEnvironment.STAGING:
            base_connection_formatted = content.base_connection.format(
                env=content.staging
            )
        elif environment == HelixEnvironment.QA:
            base_connection_formatted = content.base_connection.format(env=content.qa)
        elif environment == HelixEnvironment.DEV:
            base_connection_formatted = content.base_connection.format(env=content.dev)

        return base_connection_formatted

    def to_json(self) -> str:
        """
        convert the instance of this class to json
        """
        return json.dumps(self, indent=4, default=lambda o: o.__dict__)


class ResourceItem:
    def __init__(self, content: SimpleNamespace, base_connection_formatted: str):
        self.name = content.name
        self.path = content.path
        self.path_slug = content.path_slug
        self.full_path_slug = os.path.join(base_connection_formatted, content.path_slug)
        self.full_path = os.path.join(base_connection_formatted, content.path)


class PipelineSubscription:
    def __init__(self, content: SimpleNamespace):
        self.flow_name = content.flow_name
        self.flow_parameters: List[str] = []
        if hasattr(content, "flow_parameters"):
            self.flow_parameters = content.flow_parameters
