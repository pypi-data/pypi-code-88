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
Contains methods to interact with organization api
"""

import json
import time
import uuid

from unify.apirequestsmng import ApiRequestManager
from unify.properties import Properties
from unify.properties import ClusterSetting


class OrgAdmin(ApiRequestManager):
    """
    Class to interact with organization endpoints
    """

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __init__(self, cluster=None, props=Properties(ClusterSetting.KEY_RING)):
        """
        Class constructor

        :param cluster: Cluster name to be used
        :type cluster: name
        :param props: Properties instantiated object
        :type props: class:`unify.properties.Properties`
        """

        super().__init__(cluster=cluster, props=props)

        self.epoch_time = int(time.time())
        self.pi_tag_export_limit = {"piTagExportLimit": 999}
        self.expiry = {"expiry": 999}

        try:

            self.orgs_api_url = self.props.get_remote(self.cluster) + 'api/management/v1/orgs'
            self.org_info_url = self.props.get_remote(self.cluster) + 'api/v1/orgs/{}'

        except Exception as error:
            raise error

    def get_org_info(self, org_id):
        """
        Retrieves the org metadata

        :param org_id: Org id to be queried
        :type org_id: id or str
        :return: List of information on the organization
        """

        self.verify_properties()

        jobs = self.session.get(
            self.org_info_url.format(org_id),
            headers=self.build_header(
                aut_token=self.props.get_auth_token(),
                org_id=org_id,
                others=self.content_type_header)
        )

        return json.loads(jobs.content), jobs.status_code

    def create_organization(self, org_name):
        """
        Creates an organization with the given name

        :param org_name: Name or organization to be created
        :type org_name: str
        :return: Server response or exception if org name already exists
        """

        try:

            if org_name is None:
                org_name = str(uuid.uuid4())

            payload = {
                "name": str(org_name),
                "piTagExportLimit": self.pi_tag_export_limit,
                "expiry": self.expiry
            }

            org_create_post = self.session.post(
                self.orgs_api_url,
                headers=self.build_header(
                    aut_token=self.props.get_auth_token(cluster=self.cluster),
                    others=self.content_type_header),
                data=json.dumps(payload)
            )

            if org_create_post.status_code == 200:
                return json.loads(org_create_post.content)["id"]

            raise Exception(org_create_post.content)

        except Exception as error:

            raise error

    def delete_organization(self, org_id):
        """
        Deletes the org that matched the given org id

        :param org_id: Org id to be deleted
        :type org_id: int or str
        :return: Delete successful message
        """
        try:

            delete_endpoint = self.props.get_remote(
                cluster=self.cluster
            ) + 'api/management/v1/orgs/' + str(org_id)

            delete_request = self.session.delete(
                delete_endpoint,
                headers=self.build_header(
                    aut_token=self.props.get_auth_token(cluster=self.cluster)
                )
            )

            if delete_request.status_code == 200:
                return json.loads(delete_request.content)

            raise Exception(json.loads(delete_request.content))

        except Exception as error:
            raise error

    def invite_user(self, org_id, email, name, role):
        """
        Adds an user to the given org

        :param org_id: Org id where the user is going to be added
        :type org_id: int or str
        :param email: User's email
        :type email: str
        :param name: User's Name
        :type name: str
        :param role: User role. Accepts "Admin" or "Contributor"
        :type role: str
        :return: Invite user status message
        """
        try:

            invite_user_url = self.org_info_url.format(org_id) + '/users'

            header = self.build_header(
                aut_token=self.props.get_auth_token(cluster=self.cluster),
                org_id=org_id,
                others=self.content_type_header
            )

            payload = {"fullName": name, "email": email, "roleNames": [role]}

            invite_user_post = self.session.post(
                invite_user_url,
                headers=header,
                data=json.dumps(payload)
            )

            if invite_user_post.status_code == 201:
                return json.loads(invite_user_post.content)

            raise Exception(json.loads(invite_user_post.content))

        except Exception as error:

            raise error

    def invite_machine_user(self, org_id, id, password, fullname, role):
        """
        Invites a machine user

        :param org_id: Org identification where the user is going to be added
        :type org_id: int or str
        :param id: User's ID
        :type id: int or str
        :param password: User's Password
        :type password: str
        :param role: User role. Accepts "Admin" or "Contributor"
        :type role: str
        :return: Invite machine user status message
        """
        try:

            invite_machine_user_url = self.org_info_url.format(org_id) + '/machine_users'

            header = self.build_header(
                aut_token=self.props.get_auth_token(cluster=self.cluster),
                org_id=org_id,
                others=self.content_type_header
            )

            payload = {
                "identifier": id,
                "password": password,
                "roleNames": [role],
                "fullName": fullname
            }

            invite_user_post = self.session.post(
                invite_machine_user_url,
                headers=header,
                data=json.dumps(payload)
            )

            if invite_user_post.status_code == 200:
                return json.loads(invite_user_post.content)

            raise Exception(json.loads(invite_user_post.content))

        except Exception as error:
            raise error

    def get_org_list(self):
        """
        Retrieves the org list of the current cluster, only the ones whos users has logged in

        :return: List of organizations
        """
        try:

            header = self.build_header(
                aut_token=self.props.get_auth_token(cluster=self.cluster)
            )

            request = self.session.get(
                '{}api/whoami'.format(
                    self.props.get_remote(cluster=self.cluster)),
                headers=header
            )

            if request.status_code == 200:
                return json.loads(request.content)["organizations"]

            raise Exception(request.content)

        except Exception as error:
            raise error
