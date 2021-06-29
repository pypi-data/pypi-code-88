# Copyright 2021 Element Analytics, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
A organization client includes methods needed for connectors.
"""
import logging
from enum import Enum
from unify.properties import Properties, ClusterSetting
from unify.orgadmin import OrgAdmin
from unify.sources import Sources
from unify.templates import Templates


class DatasetOperation(Enum):
    UPDATE = 1
    APPEND = 2

class OrganizationClient:
    """
    Common connector class
    """
    def __init__(self, user_name, password, org_id, cluster):
        self.user_name = user_name
        self.password = password
        self.org_id = org_id
        self.cluster = cluster

        self.app_name = 'imc'
        self.props = Properties(ClusterSetting.MEMORY)
        self.props.store_cluster(user_name, password, cluster, self.app_name)
        try:
            org_admin = OrgAdmin(self.app_name, self.props)
            token = org_admin.auth_token()
            self.props.set_auth_token(
                token=token,
                cluster=self.app_name
            )
        except Exception as error:
            logging.error('Failed to login. %s', error)
            raise error

        try:
            self.sources = Sources(self.app_name, self.props)
            self.templates = Templates(self.app_name, self.props)
        except Exception as error:
            logging.error('Failed to get organization sources client.')
            raise error

        try:
            self.templates = Templates(self.app_name, self.props)
        except Exception as error:
            logging.error('Failed to get organization templates client.')
            raise error

    def list_datasets(self):
        """
        Retrieve all datasets.
        """
        return self.sources.get_sources(org_id=self.org_id)

    def create_dataset(self, name, dataset_csv):
        """
        Create a new dataset.

        :type name: string
        :param name: Name of dataset
        :type dataset_csv: string
        :param dataset_csv: Content to upload
        """
        return self.sources.create_api_data_set_with_content(name, self.org_id, dataset_csv)

    def update_dataset(self, dataset_csv, dataset_name=None, dataset_id=None):
        """
        Update a dataset. If dataset does not exist, create a new dataset.

        :type dataset_csv: string
        :param dataset_csv: Content to upload
        :type dataset_name: string
        :param dataset_name: Name of dataset
        :type dataset_id: string
        :param dataset_id: Existing dataset id
        """
        existing_datasets = [dataset.get("id") for dataset in self.list_datasets()]
        if dataset_id is None or dataset_id not in existing_datasets:
            response = self.create_dataset(name=dataset_name, dataset_csv=dataset_csv)
            dataset_id = response.get("data_set_id")
        else:
            self.truncate_dataset(dataset_id=dataset_id)
            self.append_dataset(dataset_id=dataset_id, dataset_csv=dataset_csv)
        return dataset_id

    def truncate_dataset(self, dataset_id):
        """
        Truncate a dataset.

        :type dataset_id: string
        :param dataset_id: Existing dataset id
        """
        return self.sources.truncate_data_set(org_id=self.org_id, data_set_id=dataset_id)

    def append_dataset(self, dataset_id, dataset_csv):
        """
        Append a dataset.

        :type dataset_csv: string
        :param dataset_csv: Content to upload
        :type dataset_id: string
        :param dataset_id: Existing dataset id
        """
        return self.sources.append_dataset(
            org_id=self.org_id,
            data_set_id=dataset_id,
            content=dataset_csv)

    def update_dataset_labels(self, dataset_id, labels):
        """
        Updates labels for a dataset.

        :type dataset_id: string
        :param dataset_id: Existing dataset id
        :type labels: dict
        :param labels: Labels
        """
        return self.sources.label(self.org_id, dataset_id, labels)
    
    def operate_dataset(self, dataset_csv, dataset_id=None, dataset_name=None, operation=DatasetOperation.UPDATE):
        """
        Operate dataset on given dataset_id. If dataset_id is not given, create a dataset first. If dataset is not valid, throw an error.

        :type dataset_csv: string
        :param dataset_csv: Content to upload
        :type dataset_name: string
        :param dataset_name: Name of dataset
        :type dataset_id: string
        :param dataset_id: Existing dataset id
        :type operation: Enum
        :param operation: Operation on dataset, update or append
        """
        if dataset_id is None:
            dataset_id = self.create_dataset(dataset_name, dataset_csv)['data_set_id']
            logging.info('create dataset %s id %s to cluster: %s, organization: %d', dataset_name, dataset_id, self.cluster, self.org_id)
        else:
            # validate dataset_id
            existing_datasets = [dataset.get("id") for dataset in self.list_datasets()]
            if dataset_id not in existing_datasets:
                raise Exception('Given dataset id {} does not exists.'.format(dataset_id))
            if operation is DatasetOperation.UPDATE:
                self.truncate_dataset(dataset_id=dataset_id)
                self.append_dataset(dataset_id=dataset_id, dataset_csv=dataset_csv)
                logging.info('update dataset %s  to cluster: %s, organization: %d', dataset_id, self.cluster, self.org_id)
            elif operation is DatasetOperation.APPEND:
                self.append_dataset(dataset_id, dataset_csv)
                logging.info('append dataset %s to cluster: %s, organization: %d', dataset_id, self.cluster, self.org_id)
        return dataset_id


    def upload_template(self, template_csv):
        """
        Upload asset template definition csv.

        :type template_csv: string
        :param template_csv: asset template definition in csv format
        """
        return self.templates.upload_string_content_file(self.org_id, template_csv)

    def upload_template_configuration(self, config_csv):
        """
        Upload asset template configuration parameter definition csv.

        :type config_csv: string
        :param config_csv: asset template configuration parameter definition in csv format
        """
        return self.templates.upload_config_with_content(self.org_id, config_csv)

    def update_template_categories(self, template_id, template_name, version, categories):
        """
        Update categories to an asset template.

        :type template_id: string
        :param template_id: Existing template id
        :type template_name: string
        :param template_name: Existing template name
        :type version: string
        :param version: Existing template id
        :type categories: dict
        :param categories: Labels
        """
        return self.templates.category(self.org_id, template_id, template_name, version, categories)

    def list_templates(self):
        """
        Retrieve all asset templates
        """
        return self.templates.list_asset_templates(self.org_id)
    