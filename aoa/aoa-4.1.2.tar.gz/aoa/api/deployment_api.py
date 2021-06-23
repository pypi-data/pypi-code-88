from __future__ import absolute_import

from aoa.api.iterator_base_api import IteratorBaseApi


class DeploymentApi(IteratorBaseApi):
    path = "/api/deployments/"

    def find_by_archived(self, archived: bool = False, projection: str = None, page: int = None, size: int = None, sort: str = None):
        raise NotImplemented("Archiving not supported for Deployments")

    def _get_header_params(self):
        header_vars = ['AOA-Project-ID', 'Accept']
        header_vals = [
            self.aoa_client.project_id,
            self.aoa_client.select_header_accept([
                'application/json',
                'application/hal+json',
                'text/uri-list',
                'application/x-spring-data-compact+json'])]

        return self.generate_params(header_vars, header_vals)

    def find_active_by_trained_model_and_engine_type(self, trained_model_id: str, engine_type: str, projection: str = None):
        """
        returns deployments by trained model and engine type

        Parameters:
           trained_model_id (str): trained model id(string) to find
           engine_type (str): engine type(string) to find
           projection (str): projection type

        Returns:
            (dict): deployments
        """
        header_vars = ['AOA-Project-ID', 'Accept']
        header_vals = [
            self.aoa_client.project_id,
            self.aoa_client.select_header_accept([
                'application/json',
                'application/hal+json',
                'text/uri-list',
                'application/x-spring-data-compact+json'])]
        header_params = self.generate_params(header_vars, header_vals)

        query_vars = ['trainedModelId', 'engineType', 'projection']
        query_vals = [trained_model_id, engine_type, projection]
        query_params = self.generate_params(query_vars, query_vals)

        return self.aoa_client.get_request(
            self.path + "search/findActiveByTrainedModelIdAndEngineType",
            header_params,
            query_params)
