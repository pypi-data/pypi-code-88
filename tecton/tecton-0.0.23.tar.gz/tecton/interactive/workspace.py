from typing import List

import tecton
from tecton import conf
from tecton._internals import errors
from tecton._internals.sdk_decorators import documented_by
from tecton._internals.sdk_decorators import sdk_public_method
from tecton.fco_listers import list_workspaces
from tecton.interactive.dataset import Dataset
from tecton.interactive.feature_table import FeatureTable
from tecton.interactive.feature_view import FeatureView
from tecton.interactive.new_transformation import NewTransformation
from tecton.interactive.transformation import Transformation


class Workspace:
    """
    Workspace class.

    This class represents a Workspace. The Workspace class is used to fetch Tecton Primitives are stored in a Workspace.
    """

    def __init__(self, workspace: str):
        workspaces = list_workspaces()
        if workspace not in workspaces:
            raise errors.NONEXISTENT_WORKSPACE(workspace, workspaces)
        self.workspace = workspace

    def __enter__(self):
        self.previous_workspace = conf.get("TECTON_WORKSPACE")
        conf.set("TECTON_WORKSPACE", self.workspace)

    def __exit__(self, type, value, traceback):
        conf.set("TECTON_WORKSPACE", self.previous_workspace)

    def _is_materializable(self) -> bool:
        from tecton_proto.metadataservice.metadata_service_pb2 import ListWorkspacesRequest
        from tecton._internals import metadata_service

        request = ListWorkspacesRequest()
        response = metadata_service.instance().ListWorkspaces(request)
        for workspace in response.workspaces:
            if workspace.name == self.workspace:
                return workspace.capabilities.materializable
        else:
            raise ValueError("Workspace not found")

    @classmethod
    @sdk_public_method
    def get(cls, name) -> "Workspace":
        """
        Fetch an existing :class:`Workspace` by name.

        :param name: Workspace name.
        """
        return Workspace(name)

    @sdk_public_method
    def get_feature_package(self, name: str):
        """
        Returns a FeaturePackage within a workspace.

        :param name: FeaturePackage name.
        """

        with self:
            return tecton.get_feature_package(name)

    @sdk_public_method
    def get_feature_view(self, name: str) -> FeatureView:
        """
        Returns a FeatureView within a workspace.

        :param name: FeatureView name
        :return: the named FeatureView
        """
        with self:
            return tecton.get_feature_view(name)

    @sdk_public_method
    def get_feature_table(self, name: str) -> FeatureTable:
        """
        Returns a FeatureTable within a workspace.

        :param name: FeatureTable name
        :return: the named FeatureTable
        """
        with self:
            return tecton.get_feature_table(name)

    @sdk_public_method
    def get_feature_service(self, name: str):
        """
        Returns a FeatureService within a workspace.

        :param name: FeatureService name.
        """

        with self:
            return tecton.get_feature_service(name)

    @sdk_public_method
    def get_data_source(self, name: str):
        """
        Returns a DataSource within a workspace.

        :param name: VirtualDataSource name.
        """

        with self:
            return tecton.get_data_source(name)

    @sdk_public_method
    def get_virtual_data_source(self, name: str):
        """
        Returns a VirtualDataSource within a workspace.

        :param name: VirtualDataSource name.
        """

        with self:
            return tecton.get_virtual_data_source(name)

    @sdk_public_method
    def get_entity(self, name: str):
        """
        Returns an Entity within a workspace.

        :param name: Entity name.
        """

        with self:
            return tecton.get_entity(name)

    @sdk_public_method
    def get_transformation(self, name: str) -> Transformation:
        """
        Returns a Transformation within a workspace.

        :param name: Transformation name.
        """

        with self:
            return tecton.get_transformation(name)

    @sdk_public_method
    def get_new_transformation(self, name: str) -> NewTransformation:
        """
        Returns a Transformation within a workspace.

        :param name: Transformation name.
        """

        with self:
            return tecton.get_new_transformation(name)

    @sdk_public_method
    def get_dataset(self, name) -> Dataset:
        """
        Returns a Dataset within a workspace.

        :param name: Dataset name.
        """
        with self:
            return tecton.get_dataset(name)

    @sdk_public_method
    def list_datasets(self) -> List[str]:
        """
        Returns a list of all registered Datasets within a workspace.

        :return: A list of strings.
        """
        with self:
            return tecton.list_datasets()

    @sdk_public_method
    def list_feature_packages(self) -> List[str]:
        """
        Returns a list of all registered FeaturePackages within a workspace.

        :return: A list of strings.
        """
        with self:
            return tecton.list_feature_packages()

    @sdk_public_method
    def list_feature_views(self) -> List[str]:
        """
        Returns a list of all registered FeatureViews within a workspace.

        :return: A list of strings.
        """
        with self:
            return tecton.list_feature_views()

    @sdk_public_method
    def list_feature_services(self) -> List[str]:
        """
        Returns a list of all registered FeatureServices within a workspace.

        :return: A list of strings.
        """
        with self:
            return tecton.list_feature_services()

    @sdk_public_method
    def list_transformations(self) -> List[str]:
        """
        Returns a list of all registered Transformations within a workspace.

        :return: A list of strings.
        """
        with self:
            return tecton.list_transformations()

    @sdk_public_method
    def list_new_transformations(self) -> List[str]:
        """
        Returns a list of all registered Transformations within a workspace.

        :return: A list of strings.
        """
        with self:
            return tecton.list_new_transformations()

    @sdk_public_method
    def list_entities(self) -> List[str]:
        """
        Returns a list of all registered Entities within a workspace.

        :returns: A list of strings.
        """
        with self:
            return tecton.list_entities()

    @sdk_public_method
    def list_virtual_data_sources(self) -> List[str]:
        """
        Returns a list of all registered VirtualDataSources within a workspace.

        :return: A list of strings.
        """
        with self:
            return tecton.list_virtual_data_sources()

    @sdk_public_method
    def list_data_sources(self) -> List[str]:
        """
        Returns a list of all registered VirtualDataSources within a workspace.

        :return: A list of strings.
        """
        with self:
            return tecton.list_data_sources()

    @sdk_public_method
    def list_feature_tables(self) -> List[str]:
        """
        Returns a list of all registered VirtualDataSources within a workspace.

        :return: A list of strings.
        """
        with self:
            return tecton.list_feature_tables()


@documented_by(Workspace.get)
@sdk_public_method
def get_workspace(name: str):
    return Workspace.get(name)
