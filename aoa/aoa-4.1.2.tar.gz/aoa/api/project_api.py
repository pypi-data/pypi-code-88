from __future__ import absolute_import
from typing import Dict

from aoa.api.iterator_base_api import IteratorBaseApi


class ProjectApi(IteratorBaseApi):

    path = "/api/projects/"

    def _get_header_params(self):
        header_vars = ['Accept']
        header_vals = ['application/json']

        return self.generate_params(header_vars, header_vals)

    def save(self, project: Dict[str, str]):
        """
        create a project

        Parameters:
           project (dict): project to create

        Returns:
            (dict): project
        """
        header_vars = ['Accept']
        header_vals = ['application/json']
        header_params = self.generate_params(header_vars, header_vals)

        query_params = {}

        self.required_params(['description', 'gitRepositoryUrl', 'groupId', 'name'], project)

        return self.aoa_client.post_request(
            self.path,
            header_params,
            query_params,
            project)

    def update(self, project: Dict[str, str]):
        """
        update a project

        Parameters:
           project (dict): project to update

        Returns:
            (dict): project
        """
        header_vars = ['Accept']
        header_vals = ['application/json']
        header_params = self.generate_params(header_vars, header_vals)

        query_params = {}

        self.required_params(['description', 'gitRepositoryUrl', 'groupId', 'name'], project)

        return self.aoa_client.put_request(
            self.path + self.aoa_client.project_id,
            header_params,
            query_params,
            project)
