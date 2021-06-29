"""
Azure IoT Central functions
"""
import os
import subprocess
import json
from logging import getLogger
from datetime import datetime
from requests import Session
from requests import codes


class AzureIotCentralSession:
    """
    Session handling for Azure IoT Central
    """
    def __init__(self):
        self.logger = getLogger(__name__)
        self.management_headers = None
        self.apps_headers = None
        self.management_session = None
        self.apps_session = None
        self.params = None

    def connect(self, force_login=False):
        """
        Connect to IoT Central
        :param force_login: do not use cached token
        """
        management_tokens = self._get_local_auth_tokens()
        if not management_tokens or force_login:
            self._az_login()
            management_tokens = self._get_local_auth_tokens()

        apps_token = self._az_get_access_token()
        if not apps_token:
            raise Exception("Apps token could not be retrieved")

        # TODO - Select first token - is this a valid approach?
        management_token = management_tokens[0]
        self.management_session = Session()
        self.apps_session = Session()
        self.params = {"api-version":"1.0"}
        self.management_headers = {"Authorization": "Bearer {}".format(management_token['accessToken'])}
        self.apps_headers = {"Authorization": "Bearer {}".format(apps_token['accessToken'])}


    def _get_auth_tokens(self):
        """ Retrieve auth tokens from local storage """
        tokens = []
        token_dir = os.path.join(os.path.expanduser("~"), ".azure")
        self.logger.debug("Using tokens from '%s'", token_dir)
        token_file = os.path.join(token_dir, "accessTokens.json")
        with open(token_file, "rb") as json_file:
            tokens = json.load(json_file)

        return tokens

    def _is_token_valid(self, auth_token):
        """ Check if a local token is valid """
        if datetime.utcnow() > datetime.strptime(auth_token['expiresOn'], '%Y-%m-%d %H:%M:%S.%f'):
            return False
        return True

    def _az_get_access_token(self):
        """ Retrieve access tokens from Azure account using CLI """
        process = subprocess.run(["az","account", "get-access-token", "--resource", "https://apps.azureiotcentral.com"],
                            shell=True, stdout=subprocess.PIPE,  universal_newlines=True, check=True)
        if process.returncode:
            self.logger.error("Unable to run Azure CLI")
            raise Exception ("AZ CLI not installed, or inaccessible!")
        token = json.loads(process.stdout)
        self.logger.debug("Apps token collected:")
        self.logger.debug("Type: %s", token['tokenType'])
        self.logger.debug("Tenant: %s", token['tenant'])
        self.logger.debug("Subscription: %s", token['subscription'])
        self.logger.debug("Expires: %s", token['expiresOn'])
        return token

    def _check_all_token_validity(self, tokens):
        """ Filter tokens by validity """
        valid_tokens = []
        for token in tokens:
            if self._is_token_valid(token):
                valid_tokens.append(token)
            else:
                self.logger.debug("Expired token")

        return valid_tokens

    def _get_local_auth_tokens(self):
        """ Retrieve auth tokens from local storage """
        tokens = self._get_auth_tokens()
        self.logger.debug("Found %d tokens", len(tokens))
        if not tokens:
            self.logger.error("Unable to find auth tokens")
            raise Exception("No tokens found - install az")
        valid_tokens = self._check_all_token_validity(tokens)
        self.logger.debug("Found %d valid tokens", len(valid_tokens))
        management_tokens = []
        for token in valid_tokens:
            if "management.core.windows.net" in token['resource']:
                self.logger.info("Management token found")
                management_tokens.append(token)
        return management_tokens

    def _az_login(self):
        """ Login to Azure using CLI """
        self.logger.info("Logging in using 'az login'")
        process = subprocess.run(["az","login"], shell=True, check=True)
        if process.returncode:
            self.logger.error("Unable to run Azure CLI")
            raise Exception ("AZ CLI not installed, or inaccessible!")

    def az_cli_command(self, command):
        """ Execute an Azure CLI command """
        process = subprocess.run(command.split(' '), shell=True, stdout=subprocess.PIPE,
                                 universal_newlines=True, check=True)
        if process.returncode:
            self.logger.error("Unable to run Azure CLI")
            raise Exception ("AZ CLI not installed, or inaccessible!")
        return process.stdout

    def az_rest_get(self, url):
        """ Make a rest-api GET call to Azure IoTCentral"""
        if "api-version" in url:
            params = {}
        else:
            params = self.params

        if "management.azure" in url:
            return self.management_session.get(url=url, headers=self.management_headers, params=params).json()
        return self.apps_session.get(url=url, headers=self.apps_headers, params=params).json()

    def az_rest_put(self, url, json_content=None):
        """ Make a rest-api PUT call to Azure IoTCentral"""
        if "api-version" in url:
            params = {}
        else:
            params = self.params

        if "management.azure" in url:
            response = self.management_session.put(url=url, headers=self.management_headers,
                                                   params=params, json=json_content)
        else:
            response = self.apps_session.put(url=url, headers=self.apps_headers, params=params, json=json_content)

        if response.status_code != codes['ok']:
            raise Exception("Invalid response from IoTCentral")

        return response


class AzureIotCentral:
    """
    Wrapper for interaction with Azure IoT Central
    """
    def __init__ (self, session, app_name):
        self.logger = getLogger(__name__)
        self.session = session
        self.app_name = app_name

    def set_app_name(self, app_name):
        """ Set the app name """
        self.app_name = app_name

    # az commands using subprocess
    def list_applications(self):
        """ List applications using AZ CLI """
        self.logger.info("Retrieving application list")
        cmd ='az iot central app list'
        apps = self.session.az_cli_command(cmd)
        return json.loads(apps)

    def get_admin_role_id(self):
        """ Retrieve admin role from AZ CLI """
        self.logger.info("Retrieving admin role ID")
        cmd ="az rest -m get -u https://{}.azureiotcentral.com/api/roles --url-parameters api-version=1.0 "
        " --resource https://apps.azureiotcentral.com --query value[?displayName=='Administrator'].id -o tsv".format(
            self.app_name)
        role_id = self.session.az_cli_command(cmd)
        return role_id.strip()

    def get_operator_role_id(self):
        """ Retrieve operator role from AZ CLI """
        self.logger.info("Retrieving operator role ID")
        cmd ="az rest -m get -u https://{}.azureiotcentral.com/api/roles --url-parameters api-version=1.0 "
        " --resource https://apps.azureiotcentral.com --query value[?displayName=='Operator'].id -o tsv".format(
            self.app_name)
        role_id = self.session.az_cli_command(cmd)
        return role_id.strip()

    # Rest-API calls
    def get_subscriptions(self):
        """ Retrieve subscriptions via REST API call """
        return self.session.az_rest_get("https://management.azure.com/subscriptions?api-version=2021-04-01")

    def get_roles(self):
        """ Retrieve roles via REST API call """
        url = "https://{}.azureiotcentral.com/api/roles".format(self.app_name)
        return self.session.az_rest_get(url)

    def get_device_templates(self):
        """ Retrieve device templates via REST API call """
        url = "https://{}.azureiotcentral.com/api/deviceTemplates".format(self.app_name)
        result = self.session.az_rest_get(url)
        return result

    def get_users(self):
        """ Retrieve users via REST API call """
        url = "https://{}.azureiotcentral.com/api/users?api-version=1.0".format(self.app_name)
        return self.session.az_rest_get(url)

    def create_device(self, device_id, template, display_name=None):
        """ Creaste device via REST API call """
        url = "https://{}.azureiotcentral.com/api/devices/{}".format(self.app_name, device_id)
        if not display_name:
            display_name = device_id
        device = {
            'displayName': display_name,
            'simulated': False,
            'template': template
        }
        return self.session.az_rest_put(url, json_content=device)

    def get_device(self, device_id):
        """ Retrieve device info via REST API call """
        url = "https://{}.azureiotcentral.com/api/devices/{}?".format(self.app_name, device_id)
        return self.session.az_rest_get(url)

    def get_device_attestation(self, device_id):
        """ Retrieve device attestation via REST API call """
        url = "https://{}.azureiotcentral.com/api/devices/{}/attestation".format(self.app_name, device_id)
        return self.session.az_rest_get(url)

    def create_device_attestation(self, device_id, certificate):
        """ Create device attestation via REST API call """
        url = "https://{}.azureiotcentral.com/api/devices/{}/attestation".format(self.app_name, device_id)
        attestation = {
            "type": "x509",
            "x509": {
                "clientCertificates": {
                    "primary": {
                        "certificate": certificate
                    }
                }
            }
        }
        return  self.session.az_rest_put(url, json_content=attestation)
