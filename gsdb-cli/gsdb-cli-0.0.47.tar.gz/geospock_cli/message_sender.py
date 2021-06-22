# Copyright (c) 2014-2021 GeoSpock Ltd.

import os
import re
from getpass import getpass
from typing import Tuple, Optional

import requests
import urllib3

from .config_reader import ConfigReaderAndWriter
from .constants import envvars
from .constants import messages
from .constants import defaults
from .exceptions import CLIError

urllib3.disable_warnings()


class MessageSender:
    @staticmethod
    def parse_and_make_request(path: str, request_params: Optional[dict], method: str, body: Optional[dict],
                               ctx) -> requests.Response:
        config_reader = ConfigReaderAndWriter(ctx.obj["PROFILE"])
        user, password, request_address, ca_cert_file, disable_verification = \
            MessageSender.get_auth_and_request_address(config_reader,
                                                       ctx.obj["USER"],
                                                       ctx.obj["PASSWORD"],
                                                       ctx.obj["ENDPOINT"],
                                                       ctx.obj["CA_CERT_FILE"],
                                                       ctx.obj["DISABLE_VERIFICATION"])
        if request_address[-1] == "/":
            request_address = request_address[0:-1]
        if "http://" not in request_address and "https://" not in request_address:
            request_address = "https://" + request_address
        if re.match(r"^(https?://.*):(\d*)$", request_address) is None:
            request_address += ":" + str(defaults.endpoint_port)

        url = request_address + path
        auth = requests.auth.HTTPBasicAuth(user, password)
        verify = ca_cert_file or not disable_verification

        try:
            if method == "GET":
                response = requests.get(url, params=request_params, auth=auth, json=body, verify=verify)
            elif method == "POST":
                response = requests.post(url, params=request_params, auth=auth, json=body, verify=verify)
            elif method == "PUT":
                response = requests.put(url, params=request_params, auth=auth, json=body, verify=verify)
            elif method == "DELETE":
                response = requests.delete(url, params=request_params, auth=auth, json=body, verify=verify)
            elif method == "PATCH":
                response = requests.patch(url, params=request_params, auth=auth, json=body, verify=verify)
            else:
                raise CLIError("Unexpected request method: " + method)
            return response
        except requests.exceptions.Timeout:
            raise CLIError("Timeout when attempting to connect to the GeoSpock server.")
        except requests.exceptions.ConnectionError as ce:
            if len(ce.args) > 0:
                raise CLIError("Cannot connect to the GeoSpock server at endpoint {}. Error is: {}"
                               .format(request_address, ce.args[0].reason))
            else:
                raise CLIError("Cannot connect to the GeoSpock server at endpoint {}.".format(request_address))
        except requests.exceptions.InvalidSchema:
            raise CLIError("The request-address `{}` is not valid (this "
                           "address should start with `http://` or `https://`)".format(request_address))
        except Exception as e:
            raise CLIError("Unexpected error occurred: " + str(e))

    @staticmethod
    def get_auth_and_request_address(config_reader: ConfigReaderAndWriter,
                                     user: str,
                                     password: str,
                                     request_address: str,
                                     ca_cert_file: str,
                                     disable_verification: bool) -> Tuple[str, str, str, str, bool]:

        # Get request address from argument, environment variable or config (in that order)
        new_request_address = request_address or os.environ.get(envvars.endpoint)
        new_ca_cert_file = ca_cert_file or os.environ.get(envvars.ca_cert_file)

        if new_request_address is None or new_ca_cert_file is None:
            config_all = config_reader.get_config()
            if config_reader.profile != "default" and config_reader.profile not in config_all:
                raise CLIError(f"The profile '{config_reader.profile}' does not exist.")
            elif config_reader.profile in config_all:
                new_request_address = new_request_address or config_all[config_reader.profile]["request_address"]
                new_ca_cert_file = new_ca_cert_file or config_all[config_reader.profile]["ca_cert_file"]
                disable_verification = disable_verification or config_all[config_reader.profile]["disable_verification"]
            elif new_request_address is None:
                raise CLIError(f"No endpoint provided - please provide in the command line, as the {envvars.endpoint} "
                               f"environment variable or by using `gsdb configure`.")

        user = user or os.environ.get(envvars.user_name)
        password = password or os.environ.get(envvars.user_password)
        if user is not None and password is not None:
            return user, password, new_request_address, new_ca_cert_file, disable_verification
        elif user is not None:
            raise CLIError(messages.userButNoPassword)
        else:
            try:
                username, password = config_reader.decode()
                if not password:
                    password = getpass(messages.enterPassword)
                return username, password, new_request_address, new_ca_cert_file, disable_verification
            except CLIError as cli_error:
                raise cli_error
            except Exception:
                raise CLIError(messages.insufficientLoginDetails)
