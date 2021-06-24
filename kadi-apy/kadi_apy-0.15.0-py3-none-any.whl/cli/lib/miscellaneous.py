# Copyright 2020 Karlsruhe Institute of Technology
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from kadi_apy.cli.commons import raise_request_error
from kadi_apy.lib.miscellaneous import Miscellaneous


class CLIMiscellaneous(Miscellaneous):
    """Model to handle miscellaneous.

    :param manager: Manager to use for all API requests.
    :type manager: CLIKadiManager
    """

    def get_deleted_resources(self, **params):
        r"""Get a list of deleted resources in the trash using the CLI. Supports
            pagination.

        :param \**params: Additional parameters.
        :raises KadiAPYRequestError: If request was not successful.
        """

        response = super().get_deleted_resources(**params)

        if response.status_code == 200:
            payload = response.json()
            current_page = params["page"]
            if current_page is None:
                current_page = 1
            self.info(
                f"Found {payload['_pagination']['total_items']} resource(s) on "
                f"{payload['_pagination']['total_pages']} page(s).\n"
                f"Showing results of page {current_page}:"
            )
            for results in payload["items"]:
                self.info(
                    f"Found {results['type']} {results['id']} with title "
                    f"'{results['title']}' and identifier '{results['identifier']}'."
                )
        else:
            raise_request_error(response=response)

    def restore(self, item, item_id):
        """Restore an item from the trash using the CLI.

        :param item: The resource type defined as class.
        :param item_id: The ID of the item to restore.
        :type item_id: int
        :raises KadiAPYRequestError: If request was not successful.
        """

        response = super().restore(item=item, item_id=item_id)
        if response.status_code == 200:
            self.info(f"Successfully restored {item.name} {item_id} from the trash.")
        else:
            raise_request_error(response=response)

    def purge(self, item, item_id):
        """Purge an item from the trash  using the CLI.

        :param item: The resource type defined as class.
        :param item_id: The ID of the item to restore.
        :type item_id: int
        :raises KadiAPYRequestError: If request was not successful.
        """

        response = super().purge(item=item, item_id=item_id)
        if response.status_code == 202:
            self.info(f"Successfully purged {item.name} {item_id} from the trash.")
        else:
            raise_request_error(response=response)

    def get_licenses(self, **params):
        r"""Get a list of available licenses using the CLI.

        :param \**params: Additional parameters.
        :raises KadiAPYRequestError: If request was not successful.
        """

        response = super().get_licenses(**params)

        if response.status_code == 200:
            payload = response.json()
            current_page = params["page"]
            if current_page is None:
                current_page = 1
            self.info(
                f"Found {payload['_pagination']['total_items']} license(s) on "
                f"{payload['_pagination']['total_pages']} page(s).\n"
                f"Showing results of page {current_page}:"
            )
            for results in payload["items"]:
                self.info(f"{results['name']}")
        else:
            raise_request_error(response=response)

    def get_kadi_info(self, manager):
        """Print information about the Kadi instance and the config file.

        :param manager: Used Manager.
        :type manager: KadiManager, CLIKadiManager

        :raises KadiAPYRequestError: If request was not successful.
        """

        # pylint: disable=arguments-differ

        response = super().get_kadi_info()
        if response.status_code == 200:
            version = response.json()["version"]

            host = manager.host
            if host.endswith("/"):
                host = host[:-1]

            if host.endswith("/api"):
                host = host[:-4]

            if manager.instance is not None:
                print_instance = f"'{manager.instance}' "
            else:
                print_instance = ""

            token_mask = manager.token[:5].ljust(len(manager.token), "*")

            self.info(
                f"You are using the instance {print_instance}with the url '{host}' and"
                f" the Kadi4Mat version '{version}'.\nThe token is '{token_mask}'.\n"
                f"The token belongs to {manager.pat_user}.\n"
                f"Request timeout is configured to {manager.timeout} seconds and"
                " verification of the SSL/TLS certificate of the host is set to"
                f" {manager.verify}."
            )
        else:
            raise_request_error(response=response)
